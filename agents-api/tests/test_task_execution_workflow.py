import uuid
from datetime import timedelta
from unittest.mock import Mock, patch

from agents_api.activities import task_steps
from agents_api.autogen.openapi_model import (
    Agent,
    CaseThen,
    GetStep,
    SwitchStep,
    TaskSpecDef,
    TaskToolDef,
    ToolCallStep,
    TransitionTarget,
    Workflow,
)
from agents_api.common.protocol.tasks import (
    ExecutionInput,
    PartialTransition,
    StepContext,
    StepOutcome,
)
from agents_api.common.retry_policies import DEFAULT_RETRY_POLICY
from agents_api.common.utils.datetime import utcnow
from agents_api.env import temporal_heartbeat_timeout
from agents_api.workflows.task_execution import TaskExecutionWorkflow
from temporalio.exceptions import ApplicationError
from ward import raises, test


@test("task execution workflow: handle function tool call step")
async def _():
    async def _resp():
        return "function_tool_call_response"

    wf = TaskExecutionWorkflow()
    step = ToolCallStep(tool="tool1")
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    output = {"type": "function"}
    outcome = StepOutcome(output=output)
    with patch("agents_api.workflows.task_execution.workflow") as workflow:
        workflow.execute_activity.return_value = _resp()
        result = await wf.handle_step(
            context=context,
            step=step,
            outcome=outcome,
        )
        assert result == PartialTransition(type="resume", output="function_tool_call_response")
        workflow.execute_activity.assert_called_once_with(
            task_steps.raise_complete_async,
            args=[context, output],
            schedule_to_close_timeout=timedelta(days=31),
            retry_policy=DEFAULT_RETRY_POLICY,
            heartbeat_timeout=timedelta(seconds=temporal_heartbeat_timeout),
        )


@test("task execution workflow: handle integration tool call step")
async def _():
    async def _resp():
        return "integration_tool_call_response"

    wf = TaskExecutionWorkflow()
    step = ToolCallStep(tool="tool1")
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[TaskToolDef(type="integration", name="tool1", spec={})],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    outcome = StepOutcome(
        output={"type": "integration", "integration": {"name": "tool1", "arguments": {}}}
    )
    with patch("agents_api.workflows.task_execution.workflow") as workflow:
        workflow.execute_activity.return_value = _resp()
        result = await wf.handle_step(
            context=context,
            step=step,
            outcome=outcome,
        )
        assert result == PartialTransition(output="integration_tool_call_response")


@test("task execution workflow: handle integration tool call step, integration tools not found")
async def _():
    wf = TaskExecutionWorkflow()
    step = ToolCallStep(tool="tool1")
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[TaskToolDef(type="integration", name="tool2", spec={})],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    outcome = StepOutcome(
        output={"type": "integration", "integration": {"name": "tool1", "arguments": {}}}
    )
    with patch("agents_api.workflows.task_execution.workflow") as workflow:
        workflow.execute_activity.return_value = "integration_tool_call_response"
        with raises(ApplicationError) as exc:
            await wf.handle_step(
                context=context,
                step=step,
                outcome=outcome,
            )
        assert str(exc.raised) == "Integration tool1 not found"


@test("task execution workflow: handle api_call tool call step")
async def _():
    async def _resp():
        return "api_call_tool_call_response"

    wf = TaskExecutionWorkflow()
    step = ToolCallStep(tool="tool1")
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    outcome = StepOutcome(output={"type": "function"})
    with patch("agents_api.workflows.task_execution.workflow") as workflow:
        workflow.execute_activity.return_value = _resp()
        result = await wf.handle_step(
            context=context,
            step=step,
            outcome=outcome,
        )
        assert result == PartialTransition(type="resume", output="api_call_tool_call_response")


@test("task execution workflow: handle switch step, index is positive")
async def _():
    wf = TaskExecutionWorkflow()
    step = SwitchStep(switch=[CaseThen(case="_", then=GetStep(get="key1"))])
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    outcome = StepOutcome(output=1)
    with patch(
        "agents_api.workflows.task_execution.execute_switch_branch"
    ) as execute_switch_branch:
        execute_switch_branch.return_value = "switch_response"
        result = await wf.handle_step(
            context=context,
            step=step,
            outcome=outcome,
        )
        assert result == PartialTransition(output="switch_response")


@test("task execution workflow: handle switch step, index is negative")
async def _():
    wf = TaskExecutionWorkflow()
    step = SwitchStep(switch=[CaseThen(case="_", then=GetStep(get="key1"))])
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    outcome = StepOutcome(output=-1)
    with patch("agents_api.workflows.task_execution.workflow") as workflow:
        workflow.logger = Mock()
        with raises(ApplicationError):
            await wf.handle_step(
                context=context,
                step=step,
                outcome=outcome,
            )


@test("task execution workflow: handle switch step, index is zero")
async def _():
    wf = TaskExecutionWorkflow()
    step = SwitchStep(switch=[CaseThen(case="_", then=GetStep(get="key1"))])
    execution_input = ExecutionInput(
        developer_id=uuid.uuid4(),
        agent=Agent(
            id=uuid.uuid4(),
            created_at=utcnow(),
            updated_at=utcnow(),
            name="agent1",
        ),
        agent_tools=[],
        arguments={},
        task=TaskSpecDef(
            name="task1",
            tools=[],
            workflows=[Workflow(name="main", steps=[step])],
        ),
    )
    context = StepContext(
        execution_input=execution_input,
        inputs=["value 1"],
        cursor=TransitionTarget(
            workflow="main",
            step=0,
        ),
    )
    outcome = StepOutcome(output=0)
    with patch("agents_api.workflows.task_execution.workflow") as workflow:
        workflow.logger = Mock()

        assert (
            await wf.handle_step(
                context=context,
                step=step,
                outcome=outcome,
            )
            is None
        )
