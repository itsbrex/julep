#!/usr/bin/env python3

import asyncio
from datetime import timedelta
from typing import Any

from temporalio import workflow
from temporalio.exceptions import ApplicationError

# Import necessary modules and types
with workflow.unsafe.imports_passed_through():
    from pydantic import RootModel

    from ...activities import task_steps
    from ...activities.execute_api_call import execute_api_call
    from ...activities.execute_integration import execute_integration
    from ...activities.execute_system import execute_system
    from ...activities.sync_items_remote import save_inputs_remote
    from ...autogen.openapi_model import (
        ApiCallDef,
        BaseIntegrationDef,
        ErrorWorkflowStep,
        EvaluateStep,
        ForeachStep,
        GetStep,
        IfElseWorkflowStep,
        LogStep,
        MapReduceStep,
        ParallelStep,
        PromptStep,
        ReturnStep,
        SetStep,
        SleepStep,
        SwitchStep,
        SystemDef,
        ToolCallStep,
        TransitionTarget,
        WaitForInputStep,
        WorkflowStep,
        YieldStep,
    )
    from ...common.protocol.tasks import (
        ExecutionInput,
        PartialTransition,
        StepContext,
        StepOutcome,
    )
    from ...common.retry_policies import DEFAULT_RETRY_POLICY
    from ...env import (
        debug,
        temporal_heartbeat_timeout,
        temporal_schedule_to_close_timeout,
        testing,
    )
    from ...exceptions import LastErrorInput
    from .helpers import (
        continue_as_child,
        execute_foreach_step,
        execute_if_else_branch,
        execute_map_reduce_step,
        execute_map_reduce_step_parallel,
        execute_switch_branch,
    )
    from .transition import transition


# Supported steps
# ---------------

# TODO: Implement the rest of the steps

# WorkflowStep = (
#     EvaluateStep  # ✅
#     | ToolCallStep  # ✅
#     | PromptStep  # 🟡    <--- high priority
#     | GetStep  # ✅
#     | SetStep  # ✅
#     | LogStep  # ✅
#     | ReturnStep  # ✅
#     | SleepStep  # ✅
#     | ErrorWorkflowStep  # ✅
#     | YieldStep  # ✅
#     | WaitForInputStep  # ✅
#     | IfElseWorkflowStep  # ✅
#     | SwitchStep  # ✅
#     | ForeachStep  # ✅
#     | ParallelStep  # ❌
#     | MapReduceStep  # ✅
# )

# Mapping of step types to their corresponding activities
STEP_TO_ACTIVITY = {
    PromptStep: task_steps.prompt_step,
    ToolCallStep: task_steps.tool_call_step,
    WaitForInputStep: task_steps.wait_for_input_step,
    SwitchStep: task_steps.switch_step,
    LogStep: task_steps.log_step,
    EvaluateStep: task_steps.evaluate_step,
    ReturnStep: task_steps.return_step,
    YieldStep: task_steps.yield_step,
    IfElseWorkflowStep: task_steps.if_else_step,
    ForeachStep: task_steps.for_each_step,
    MapReduceStep: task_steps.map_reduce_step,
    SetStep: task_steps.set_value_step,
    # GetStep: task_steps.get_value_step,
}


GenericStep = RootModel[WorkflowStep]


# TODO: find a way to transition to error if workflow or activity times out.

# TODO: Implement reasonable timeouts for steps, activities and workflows
# SCRUM-13

# TODO: The timeouts should be configurable per task


# TODO: Review the current user state storage method
#       Probably can be implemented much more efficiently


# Main workflow definition
@workflow.defn
class TaskExecutionWorkflow:
    last_error: BaseException | None = None
    context: StepContext | None = None
    outcome: StepOutcome | None = None

    def __init__(self):
        self.last_error = None

    @workflow.signal
    async def set_last_error(self, value: LastErrorInput):
        self.last_error = value.last_error

    async def _handle_LogStep(
        self,
        step: LogStep,
    ):
        workflow.logger.info(f"Log step: {step.log}")

        # Set the output to the current input
        # Add the logged message to metadata
        return PartialTransition(
            output=self.context.current_input,
            metadata={
                "step_type": type(self.context.current_step).__name__,
                "log": step.log,
            },
        )

    async def _handle_ReturnStep(
        self,
        step: ReturnStep,
    ):
        output = self.outcome.output
        workflow.logger.info("Return step: Finishing workflow with output")
        workflow.logger.debug(f"Return step: {output}")
        await transition(
            self.context,
            output=output,
            type="finish" if self.context.is_main else "finish_branch",
            next=None,
            last_error=self.last_error,
        )
        return output

    async def _handle_SwitchStep(
        self,
        step: SwitchStep,
    ):
        index = self.outcome.output
        if index > 0:
            result = await execute_switch_branch(
                context=self.context,
                execution_input=self.context.execution_input,
                switch=step.switch,
                index=index,
                current_input=self.context.current_input,
            )
            return PartialTransition(output=result)
        if index < 0:
            workflow.logger.error("Switch step: Invalid negative index")
            msg = "Negative indices not allowed"
            raise ApplicationError(msg)
        return None

    async def _handle_IfElseWorkflowStep(
        self,
        step: IfElseWorkflowStep,
    ):
        result = await execute_if_else_branch(
            context=self.context,
            execution_input=self.context.execution_input,
            then_branch=step.then,
            else_branch=step.else_,
            condition=self.outcome.output,
            current_input=self.context.current_input,
        )

        return PartialTransition(output=result)

    async def _handle_ForeachStep(
        self,
        step: ForeachStep,
    ):
        result = await execute_foreach_step(
            context=self.context,
            execution_input=self.context.execution_input,
            do_step=step.foreach.do,
            items=self.outcome.output,
            current_input=self.context.current_input,
        )
        return PartialTransition(output=result)

    async def _handle_MapReduceStep(
        self,
        step: MapReduceStep,
    ):
        parallelism = step.parallelism
        if parallelism is None or parallelism == 1:
            result = await execute_map_reduce_step(
                context=self.context,
                execution_input=self.context.execution_input,
                map_defn=step.map,
                items=self.outcome.output,
                reduce=step.reduce,
                initial=step.initial,
                current_input=self.context.current_input,
            )
        else:
            result = await execute_map_reduce_step_parallel(
                context=self.context,
                execution_input=self.context.execution_input,
                map_defn=step.map,
                items=self.outcome.output,
                current_input=self.context.current_input,
                initial=step.initial,
                reduce=step.reduce,
                parallelism=parallelism,
            )

        return PartialTransition(output=result)

    async def _handle_SleepStep(
        self,
        step: SleepStep,
    ):
        sleep = step.sleep
        total_seconds = (
            sleep.seconds
            + sleep.minutes * 60
            + sleep.hours * 60 * 60
            + sleep.days * 24 * 60 * 60
        )
        workflow.logger.info(f"Sleep step: Sleeping for {total_seconds} seconds")
        assert total_seconds > 0, "Sleep duration must be greater than 0"

        result = await asyncio.sleep(total_seconds, result=self.context.current_input)

        return PartialTransition(output=result)

    async def _handle_EvaluateStep(
        self,
        step: EvaluateStep,
    ):
        output = self.outcome.output
        workflow.logger.debug(f"Evaluate step: Completed evaluation with output: {output}")
        return PartialTransition(output=output)

    async def _handle_ErrorWorkflowStep(
        self,
        step: ErrorWorkflowStep,
    ):
        error = step.error
        workflow.logger.error(f"Error step: {error}")

        state = PartialTransition(type="error", output=error)
        await transition(
            self.context,
            state,
            last_error=self.last_error,
        )

        msg = f"Error raised by ErrorWorkflowStep: {error}"
        raise ApplicationError(msg)

    async def _handle_YieldStep(
        self,
        step: YieldStep,
    ):
        output = self.outcome.output
        yield_transition_type, yield_next_target = self.outcome.transition_to
        workflow.logger.info(f"Yield step: Transitioning to {yield_transition_type}")
        await transition(
            self.context,
            output=output,
            type=yield_transition_type,
            next=yield_next_target,
            last_error=self.last_error,
        )

        result = await continue_as_child(
            self.context,
            start=yield_next_target,
            current_input=output,
        )

        return PartialTransition(output=result)

    async def _handle_WaitForInputStep(
        self,
        step: WaitForInputStep,
    ):
        workflow.logger.info("Wait for input step: Waiting for external input")

        result = await workflow.execute_activity(
            task_steps.raise_complete_async,
            args=[self.context, self.outcome.output],
            schedule_to_close_timeout=timedelta(days=31),
            retry_policy=DEFAULT_RETRY_POLICY,
            heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
        )

        return PartialTransition(type="resume", output=result)

    async def _handle_PromptStep(
        self,
        step: PromptStep,
    ):
        message = self.outcome.output
        choice = message["choices"][0]
        finish_reason = choice["finish_reason"]
        if step.unwrap or not step.auto_run_tools or finish_reason != "tool_calls":
            workflow.logger.debug(f"Prompt step: Received response: {message}")
            return PartialTransition(output=message)

        tool_calls_input = choice["message"]["tool_calls"]
        input_type = tool_calls_input[0]["type"]

        if input_type == "function":
            workflow.logger.debug("Prompt step: Received FUNCTION tool call")

            # Enter a wait-for-input step to ask the developer to run the tool calls
            tool_calls_results = await workflow.execute_activity(
                task_steps.raise_complete_async,
                args=[self.context, tool_calls_input],
                schedule_to_close_timeout=timedelta(days=31),
                retry_policy=DEFAULT_RETRY_POLICY,
                heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
            )

            # Feed the tool call results back to the model
            self.context.current_step.prompt.append(message)
            self.context.current_step.prompt.append(tool_calls_results)
            new_response = await workflow.execute_activity(
                task_steps.prompt_step,
                self.context,
                schedule_to_close_timeout=timedelta(
                    seconds=30 if debug or testing else temporal_schedule_to_close_timeout
                ),
                retry_policy=DEFAULT_RETRY_POLICY,
                heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
            )
            return PartialTransition(output=new_response.output, type="resume")
        if input_type == "integrations":
            workflow.logger.debug("Prompt step: Received INTEGRATION tool call")
            # FIXME: Implement integration tool calls
            # See: MANUAL TOOL CALL INTEGRATION (below)
            msg = "Integration tool calls not yet supported"
            raise NotImplementedError(msg)

            # TODO: Feed the tool call results back to the model (see above)
        if input_type == "api_call":
            workflow.logger.debug("Prompt step: Received API_CALL tool call")

            # FIXME: Implement API_CALL tool calls
            # See: MANUAL TOOL CALL API_CALL (below)
            msg = "API_CALL tool calls not yet supported"
            raise NotImplementedError(msg)

            # TODO: Feed the tool call results back to the model (see above)
        if input_type == "system":
            workflow.logger.debug("Prompt step: Received SYSTEM tool call")

            # FIXME: Implement SYSTEM tool calls
            # See: MANUAL TOOL CALL SYSTEM (below)
            msg = "SYSTEM tool calls not yet supported"
            raise NotImplementedError(msg)

            # TODO: Feed the tool call results back to the model (see above)
        workflow.logger.debug(
            f"Prompt step: Received unknown tool call: {tool_calls_input[0]['type']}"
        )
        return PartialTransition(output=message)

    async def _handle_SetStep(
        self,
        step: SetStep,
    ):
        workflow.logger.info("Set step: Updating user state")

        # Pass along the previous output unchanged
        return PartialTransition(
            output=self.context.current_input, user_state=self.outcome.output
        )

    async def _handle_GetStep(
        self,
        step: GetStep,
    ):
        key = step.get
        workflow.logger.info(f"Get step: Fetching '{key}' from user state")
        value = workflow.memo_value(key, default=None)
        workflow.logger.debug(f"Retrieved value: {value}")

        return PartialTransition(output=value)

    async def _handle_ParallelStep(
        self,
        step: ParallelStep,
    ):
        # FIXME: Implement ParallelStep
        # SCRUM-17
        workflow.logger.error("ParallelStep not yet implemented")
        msg = "Not implemented"
        raise ApplicationError(msg)

    async def _handle_ToolCallStep(
        self,
        step: ToolCallStep,
    ):
        tool_call = self.outcome.output
        if tool_call["type"] == "function":
            tool_call_response = await workflow.execute_activity(
                task_steps.raise_complete_async,
                args=[self.context, tool_call],
                schedule_to_close_timeout=timedelta(days=31),
                retry_policy=DEFAULT_RETRY_POLICY,
                heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
            )

            return PartialTransition(output=tool_call_response, type="resume")

        if tool_call["type"] == "integration":
            # MANUAL TOOL CALL INTEGRATION
            workflow.logger.debug("ToolCallStep: Received INTEGRATION tool call")
            call = tool_call["integration"]
            tool_name = call["name"]
            arguments = call["arguments"]
            integration_tool = next(
                (t for t in self.context.tools if t.name == tool_name), None
            )

            if integration_tool is None:
                msg = f"Integration {tool_name} not found"
                raise ApplicationError(msg)

            provider = integration_tool.integration.provider
            setup = (
                integration_tool.integration.setup
                and integration_tool.integration.setup.model_dump()
            )
            method = integration_tool.integration.method

            integration = BaseIntegrationDef(
                provider=provider,
                setup=setup,
                method=method,
                arguments=arguments,
            )

            tool_call_response = await workflow.execute_activity(
                execute_integration,
                args=[self.context, tool_name, integration, arguments],
                schedule_to_close_timeout=timedelta(
                    seconds=30 if debug or testing else temporal_schedule_to_close_timeout
                ),
                retry_policy=DEFAULT_RETRY_POLICY,
                heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
            )

            return PartialTransition(output=tool_call_response)

        if tool_call["type"] == "api_call":
            # MANUAL TOOL CALL API_CALL
            workflow.logger.debug("ToolCallStep: Received API_CALL tool call")
            call = tool_call["api_call"]
            tool_name = call["name"]
            arguments = call["arguments"]
            apicall_tool = next((t for t in self.context.tools if t.name == tool_name), None)

            if apicall_tool is None:
                msg = f"Integration {tool_name} not found"
                raise ApplicationError(msg)

            api_call = ApiCallDef(
                method=apicall_tool.api_call.method,
                url=apicall_tool.api_call.url,
                headers=apicall_tool.api_call.headers,
                follow_redirects=apicall_tool.api_call.follow_redirects,
            )

            if "json_" in arguments:
                arguments["json"] = arguments["json_"]
                del arguments["json_"]

            # Execute the API call using the `execute_api_call` function
            tool_call_response = await workflow.execute_activity(
                execute_api_call,
                args=[
                    api_call,
                    arguments,
                ],
                schedule_to_close_timeout=timedelta(
                    seconds=30 if debug or testing else temporal_schedule_to_close_timeout
                ),
                heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
            )

            return PartialTransition(output=tool_call_response)

        if tool_call["type"] == "system":
            # MANUAL TOOL CALL SYSTEM
            workflow.logger.debug("ToolCallStep: Received SYSTEM tool call")
            call = tool_call.get("system")

            system_call = SystemDef(**call)
            tool_call_response = await workflow.execute_activity(
                execute_system,
                args=[self.context, system_call],
                schedule_to_close_timeout=timedelta(
                    seconds=30 if debug or testing else temporal_schedule_to_close_timeout
                ),
                heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
            )

            return PartialTransition(output=tool_call_response)
        return None

    async def handle_step(self, step: WorkflowStep):
        meth = getattr(self, f"_handle_{type(step).__name__}", None)
        if not meth:
            workflow.logger.error(
                f"Unhandled step type: {type(self.context.current_step).__name__}"
            )
            msg = "Not implemented"
            state = PartialTransition(type="error", output=msg)
            await transition(
                self.context,
                state,
                last_error=self.last_error,
            )

            raise ApplicationError(msg)

        return await meth(step)

    # Main workflow run method
    @workflow.run
    async def run(
        self,
        execution_input: ExecutionInput,
        start: TransitionTarget,
        current_input: Any,
    ) -> Any:
        if not execution_input.task:
            msg = "execution_input.task cannot be None"
            raise ApplicationError(msg)

        workflow.logger.info(
            f"TaskExecutionWorkflow for task {execution_input.task.id}"
            f" [LOC {start.workflow}.{start.step}]"
        )

        # 0. Prepare context
        context = StepContext(
            execution_input=execution_input,
            current_input=current_input,
            cursor=start,
        )

        step_type = type(context.current_step)
        continued_as_new = workflow.info().continued_run_id is not None

        # 1. Transition to starting if not done yet
        if context.is_first_step and not continued_as_new:
            await transition(
                context,
                type="init" if context.is_main else "init_branch",
                output=context.current_input,
                next=context.cursor,
                metadata={},
                last_error=self.last_error,
            )

        # 2. Execute the current step's activity if applicable
        workflow.logger.info(
            f"Executing step {context.cursor.step} of type {step_type.__name__}"
        )

        activity = STEP_TO_ACTIVITY.get(step_type)

        outcome = None

        if activity:
            try:
                outcome: StepOutcome = await workflow.execute_activity(
                    activity,
                    context,
                    #
                    schedule_to_close_timeout=timedelta(
                        seconds=30 if debug or testing else temporal_schedule_to_close_timeout
                    ),
                    retry_policy=DEFAULT_RETRY_POLICY,
                    heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
                )
                workflow.logger.debug(f"Step {context.cursor.step} completed successfully")

            except Exception as e:
                workflow.logger.error(f"Error in step {context.cursor.step}: {e!s}")
                await transition(context, type="error", output=str(e))
                msg = f"Activity {activity} threw error: {e}"
                raise ApplicationError(msg) from e

        # 3. Then, based on the outcome and step type, decide what to do next
        workflow.logger.info(f"Processing outcome for step {context.cursor.step}")

        error = outcome.error
        if error is not None:
            workflow.logger.error(f"Error in step {context.cursor.step}: {error}")
            await transition(context, type="error", output=error)
            msg = f"Step {type(context.current_step).__name__} threw error: {error}"
            raise ApplicationError(msg)

        self.context = context
        self.outcome = outcome

        state = await self.handle_step(
            step=context.current_step,
        )
        if isinstance(context.current_step, ReturnStep):
            return state

        # 4. Transition to the next step
        workflow.logger.info(f"Transitioning after step {context.cursor.step}")

        # The returned value is the transition finally created
        state = state or PartialTransition(type="error", output="Not implemented")
        final_state = await transition(
            context,
            state,
            last_error=self.last_error,
        )

        # 5a. End if the last step
        if final_state.type in ("finish", "finish_branch", "cancelled"):
            workflow.logger.info(f"Workflow finished with state: {final_state.type}")
            return final_state.output

        # 5b. Recurse to the next step
        if not final_state.next:
            msg = "No next step"
            raise ApplicationError(msg)

        workflow.logger.info(
            f"Continuing to next step: {final_state.next.workflow}.{final_state.next.step}"
        )

        # Save the final output to the blob store
        [final_output] = await workflow.execute_activity(
            save_inputs_remote,
            args=[[final_state.output]],
            schedule_to_close_timeout=timedelta(
                seconds=10 if debug or testing else temporal_schedule_to_close_timeout
            ),
            retry_policy=DEFAULT_RETRY_POLICY,
            heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
        )

        # Continue as a child workflow
        return await continue_as_child(
            context.execution_input,
            start=final_state.next,
            current_input=final_output,
            user_state=state.user_state,
        )
