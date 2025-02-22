<a name="v0.4.0"></a>
# [v0.4.0](https://github.com/julep-ai/julep/releases/tag/v0.4.0) - 28 Sep 2024

## What's Changed
* feat(agents-api): Add cozo migrations for tasks schema by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/349
* feat(agents-api): updated openapi schema for tasks spec by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/350
* Update README.md by [@ijindal1](https://github.com/ijindal1) in https://github.com/julep-ai/julep/pull/384
* Update README.md by [@ijindal1](https://github.com/ijindal1) in https://github.com/julep-ai/julep/pull/385
* feat(agents-api): cozo queries for tasks by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/352
* fix(sdks/ts): Fixed bugs, updated sdk by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/390
* feat(agents-api): Toy implementation of Tasks by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/391
* feat(agents-api): Adaptive context (via recursive summarization) by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/306
* chore(deps-dev): bump braces from 3.0.2 to 3.0.3 in /sdks/ts in the npm_and_yarn group across 1 directory by [@dependabot](https://github.com/dependabot) in https://github.com/julep-ai/julep/pull/394
* v/0.3.9 by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/395
* feat(tasks): Enable all fields of ExecutionInput by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/396
* feat(tasks): Update execution transition relation by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/397
* fix: Handle prompt too big error by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/401
* feat(sdks/ts): Add adaptive context options to the SDK by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/404
* feat(sdks/ts): Add runtime validations for TS SDK by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/425
* refactor(agents-api): Rework routers to split routes into individual files by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/422
* support for `Hermes-2-Theta-Llama-3-8B` as default OSS model by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/424
* fix: Add exception handler for litellm API error by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/432
* fix(openapi): Fix mistakes in openapi.yaml file by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/434
* fix: Apply various small fixes to task execution logic by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/436
* Codegen for all new typespec types by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/435
* feat(agents-api): New chat context query and model by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/437
* feat(agents-api): Add get_transition query by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/438
* chore: Disable all the routes except of tasks and agents by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/439
* fix(agents-api): Fix execution input query by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/440
* f/wait for input step by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/441
* feat(agents-api): Implement doc* models by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/442
* Reimplement tests for queries and operations by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/443
* feat(agents-api): Hybrid docs search by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/444
* feat(agents-api): Add temporal workflow lookup relation and queries by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/446
* feat: new routes for docs, users, search by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/445
* feat(agents-api): Add litellm proxy to docker compose by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/448
* fix(agents-api): Fixed tests for models and queries by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/449
* creatorrr/f add missing tests by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/450
* feat(agents-api): Add route tests by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/451
* Add tests for docs routes by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/452
* feat(agents-api): Preliminary implementation of session.chat by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/453
* feat(agents-api): Make chat route tests pass by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/454
* feat(agents-api): Add some workflow tests by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/456
* fix(agents-api): Minor fix to tests by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/457
* f/task tests by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/458
* feat(agents-api): ALL TESTS PASS!! :D by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/459
* feat: Add test for evaluate step by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/460
* fix(agents-api): Fix typespec for foreach step and regenerate by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/461
* fix(agents-api): Fix the typespec bug and regenerate by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/462
* x/fix codec by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/463
* feat(agents-api): Add YAML support by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/464
* refactor(agents-api): Minor refactors to typespec types by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/465
* fix(agents-api): Fix map reduce step and activity by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/466
* fix(agents-api): Make the sample work by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/467
* Dev tasks by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/447
* fix: Build cozo-bin docker image directly from cozo repo by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/469
* feat(memory-store): Add backup cronjob by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/470
* fix: Fix deployment docker compose and move temporal into separate service by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/471
* fix(agents-api): Fix prompt step by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/472
* fix(agents-api): Fix task execution logic by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/473
* Fix create agent tool by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/474
* fix(agents-api): Fix bug in task-execution workflow and uuid-int-list-to-str fn by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/476
* fix(agents-api): Fix prompt render, codec and task execution by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/478
* fix(agents-api): Fix more render issues, execution logic by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/479
* x/fix task execution by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/482
* text-embeddings-inference-cpu temp fix for Apple Silicon CPUs by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/480
* fix(agents-api): Fix task execution logical errors by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/483
* feat(agents-api): Transitions stream SSE endpoint by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/485
* feat(agents-api): Set/get steps based on workflow state by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/484
* Scrum 22 [FIX] agents api list agent tools is returning an empty list by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/487
* fix(agents-api,typespec): Fix chat/entry typespec models to include tool_calls by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/489
* fix: Change log-step to a jinja template rather than a simpleeval expression by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/488
* feat(agents-api): Add parallelism option to map-reduce step by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/490
* fix: Fix import by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/494
* misc fixes by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/495
* build(deps): Bump the npm_and_yarn group across 2 directories with 2 updates by [@dependabot](https://github.com/dependabot) in https://github.com/julep-ai/julep/pull/493
* hotfix: Apply a temp hotfix for sessions.chat by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/497
* hotfix(agents-api): Fix session.situation not being rendered by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/499
* feat: Add agent tools to completion data before sending to litellm in prompt by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/498
* dev -> main by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/502
* fix(agents-api): fix create_agent and create_or_update_agent query by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/503
* fix(llm-proxy): Update docker image to main-v1.46.2 by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/504
* Add custom api key support to chat endpoint by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/507
* fix(agents-api): Fix doc recall using search by text by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/506
* docs: update api.md by [@eltociear](https://github.com/eltociear) in https://github.com/julep-ai/julep/pull/508
* fix: Get PostgreSQL settings via env vars by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/509
* main <- dev by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/511
* Vertex AI client by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/510
* fix: Retry worker on runtime errors by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/512
* dev -> main by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/514
* Implement ToolCallStep & Fix transition after PromptStep by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/513
* doc: Update README.md with announcement update by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/517
* feat: Add basic support for integration tools to ToolStep by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/519
* feat(integration-service): Add integrations service by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/520
* feat(agents-api,integrations): Working integrations for tool-call step by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/521
* fix(agents-api): Fix wait for input step by [@HamadaSalhab](https://github.com/HamadaSalhab) in https://github.com/julep-ai/julep/pull/522
* feat(agents-api): Add support for reading setup args from metadata and Upgrade to python 3.12 by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/525
* feat: Add docker bake builder by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/528
* fix: Minor fix to docker bake github actions by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/529
* feat: Add changelog from release notes by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/530

## New Contributors
* [@ijindal1](https://github.com/ijindal1) made their first contribution in https://github.com/julep-ai/julep/pull/384
* [@HamadaSalhab](https://github.com/HamadaSalhab) made their first contribution in https://github.com/julep-ai/julep/pull/474
* [@eltociear](https://github.com/eltociear) made their first contribution in https://github.com/julep-ai/julep/pull/508

**Full Changelog**: https://github.com/julep-ai/julep/compare/v0.3.4...v0.4.0

[Changes][v0.4.0]


<a name="v0.3.4"></a>
# [v0.3.4](https://github.com/julep-ai/julep/releases/tag/v0.3.4) - 31 May 2024

## What's Changed
* feat: Implement filtering by metadata by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/337
* session.chat working without specifying user by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/338
* feat: Cache generated responses by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/336
* Add docs-text-embeddings-inference service to deploy/docker-compose.yml by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/339
* add missing ports and volumes in deploy/docker-compose by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/341
* feat: Add launching entry point by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/334
* feat: Add an explicit platform declaration to the services in deploy/docker-compose.yml by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/342
* [wip] feat(agents-api,sdks): multimodal support by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/343
* fix(sdks/ts): Fix codegen issue by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/374
* Version 0.3.4 by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/375
* fix: Convert messages content to JSON by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/376
* fix: Convert IDs to UUID before passing to query executing functions by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/377
* fix(agents-api): fix fn calling and local deployment by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/378
* feat: Improve typehints by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/379


**Full Changelog**: https://github.com/julep-ai/julep/compare/v0.3.3...v0.3.4

[Changes][v0.3.4]


<a name="v0.3.3"></a>
# [v0.3.3](https://github.com/julep-ai/julep/releases/tag/v0.3.3) - 17 May 2024

## What's Changed
* fix: Add summarizer source type to the query by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/301
* fix: Get summarization model form env var and create a corresponsing … by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/302
* feat: Make docs content be splited by users by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/303
* feat: litellm for multiple model support by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/304
* use VALID_MODELS to support JULEP_MODELS by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/308
* Agent creation fixes by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/309
* feat: Add new agents docs embbeddings functionality by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/305
* Fix docs search by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/311
* Make embeddings asynchronous using temporal by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/332
* feat: Add doc IDs to the session chat response by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/331
* chore: Update SDKs by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/333


**Full Changelog**: https://github.com/julep-ai/julep/compare/v0.3.2...v0.3.3

[Changes][v0.3.3]


<a name="v0.3.2"></a>
# [v0.3.2](https://github.com/julep-ai/julep/releases/tag/v0.3.2) - 27 Apr 2024

- Initial github release

## What's Changed
* fix(python-sdk): temporarily remove async types by [@philipbalbas](https://github.com/philipbalbas) in https://github.com/julep-ai/julep/pull/196
* fix: Set empty string as a default value for function description by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/195
* feat: exception handling for api keys and models by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/197
* feat: Create and push docker images to hub by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/198
* fix: Sessions update by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/201
* fix: Sessions update by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/202
* feat(sdk): update tools by [@philipbalbas](https://github.com/philipbalbas) in https://github.com/julep-ai/julep/pull/206
* fix: Merge agent and user metadata by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/204
* fix: Display agent instructions by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/205
* fix: Disable model-serving by default by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/207
* fix: patch fix for function calling by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/203
* remove model surgery notebooks by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/208
* feat: Create github action changelog-ci.yml by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/209
* Sweep: Add a detailed README.md in the memory-store/ directory by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/214
* fix: Display agent instructions by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/216
* Sweep: Add a detailed README.md in the examples/ directory by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/215
* fix: Set metadata to an empty dict by default by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/217
* Sweep: Update the docstrings and comments in sdks/ts/src/env.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/235
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/memory.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/236
* Sweep: Update the docstrings and comments in sdks/ts/src/utils/invariant.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/237
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/agent.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/238
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/tool.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/239
* Sweep: Update the docstrings and comments in sdks/ts/src/utils/isValidUuid4.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/240
* Sweep: Update the docstrings and comments in sdks/ts/src/client.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/241
* Sweep: Update the docstrings and comments in sdks/ts/src/utils/requestConstructor.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/242
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/base.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/243
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/user.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/244
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/session.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/245
* Sweep: Update the docstrings and comments in sdks/ts/src/utils/openaiPatch.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/246
* Sweep: Update the docstrings and comments in sdks/ts/src/managers/doc.ts to fix any issues and mismatch between the comment and associated code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/247
* doc(sdks/ts): Generate documentation for the typescript SDK by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/248
* Sweep: Update the docstrings and comments in sdks/python/julep/env.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/262
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/memory.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/271
* Sweep: Update the docstrings and comments in sdks/python/julep/utils/openai_patch.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/270
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/base.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/263
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/types.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/269
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/utils.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/268
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/tool.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/267
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/doc.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/266
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/session.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/265
* Sweep: Update the docstrings and comments in sdks/python/julep/managers/agent.py to fix any issues and mismatch between the comments present and surrounding code by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/264
* refactor(agents-api): Add decorator to wrap cozo queries inside and execute by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/273
* feat: update python sdk docs by [@philipbalbas](https://github.com/philipbalbas) in https://github.com/julep-ai/julep/pull/272
* fix: Set default values for function description and parameters by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/274
* feat(openapi): Update spec to include role=function + render_templates by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/276
* docs: update SUMMARY.md by [@philipbalbas](https://github.com/philipbalbas) in https://github.com/julep-ai/julep/pull/281
* chore(deps): bump fastapi from 0.109.2 to 0.110.1 in /agents-api in the pip group across 1 directory by [@dependabot](https://github.com/dependabot) in https://github.com/julep-ai/julep/pull/280
* chore(deps): bump idna from 3.6 to 3.7 in /memory-store/backup by [@dependabot](https://github.com/dependabot) in https://github.com/julep-ai/julep/pull/278
* chore(deps): bump follow-redirects from 1.15.5 to 1.15.6 in /sdks/ts by [@dependabot](https://github.com/dependabot) in https://github.com/julep-ai/julep/pull/277
* F/update julep docs by [@philipbalbas](https://github.com/philipbalbas) in https://github.com/julep-ai/julep/pull/282
* fix: Fix queries calls by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/283
* Sweep: Create CONTRIBUTING.md based on README.md in the root / directory by [@sweep-ai](https://github.com/sweep-ai) in https://github.com/julep-ai/julep/pull/285
* feat: added docker-compose.yml and .env.example for self-hosting by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/286
* fix: Set default value for user's about text by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/287
* fix: Update sessions with given IDs only by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/290
* F/readme update by [@alt-glitch](https://github.com/alt-glitch) in https://github.com/julep-ai/julep/pull/291
* feat: Truncate messages by [@whiterabbit1983](https://github.com/whiterabbit1983) in https://github.com/julep-ai/julep/pull/294
* x/fix python sdk by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/296
* feat(agents-api): Allow single instructions str for agents by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/297
* fix: Session.user_id should be optional by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/298
* feat(agents-api): Add jinja templates support by [@creatorrr](https://github.com/creatorrr) in https://github.com/julep-ai/julep/pull/300

## New Contributors
* [@dependabot](https://github.com/dependabot) made their first contribution in https://github.com/julep-ai/julep/pull/280

**Full Changelog**: https://github.com/julep-ai/julep/commits/v0.3.2

[Changes][v0.3.2]


<a name="v0.3.0"></a>
# [v0.3.0](https://github.com/julep-ai/julep/releases/tag/v0.3.0) - 27 Apr 2024



[Changes][v0.3.0]


<a name="v0.2.12"></a>
# [v0.2.12](https://github.com/julep-ai/julep/releases/tag/v0.2.12) - 27 Apr 2024



[Changes][v0.2.12]


[v0.4.0]: https://github.com/julep-ai/julep/compare/v0.3.4...v0.4.0
[v0.3.4]: https://github.com/julep-ai/julep/compare/v0.3.3...v0.3.4
[v0.3.3]: https://github.com/julep-ai/julep/compare/v0.3.2...v0.3.3
[v0.3.2]: https://github.com/julep-ai/julep/compare/v0.3.0...v0.3.2
[v0.3.0]: https://github.com/julep-ai/julep/compare/v0.2.12...v0.3.0
[v0.2.12]: https://github.com/julep-ai/julep/tree/v0.2.12

<!-- Generated by https://github.com/rhysd/changelog-from-release v3.7.2 -->
