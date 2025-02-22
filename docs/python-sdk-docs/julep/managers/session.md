# Session

[Julep Python SDK Index](../../README.md#julep-python-sdk-index) / [Julep](../index.md#julep) / [Managers](./index.md#managers) / Session

> Auto-generated documentation for [julep.managers.session](../../../../../../julep/managers/session.py) module.

- [Session](#session)
  - [AsyncSessionsManager](#asyncsessionsmanager)
  - [BaseSessionsManager](#basesessionsmanager)
  - [SessionCreateArgs](#sessioncreateargs)
  - [SessionUpdateArgs](#sessionupdateargs)
  - [SessionsManager](#sessionsmanager)

## AsyncSessionsManager

[Show source in session.py:800](../../../../../../julep/managers/session.py#L800)

A class for managing asynchronous sessions.

This class handles operations related to creating, retrieving, updating,
deleting, and interacting with sessions asynchronously. It extends the
functionality of BaseSessionsManager with asynchronous behavior.

#### Attributes

Inherits attributes from the BaseSessionsManager class.

#### Methods

- `async` *get(id* - Union[UUID, str]) -> Session:
    Retrieves a session by its ID.

async create(*, user_id: Union[str, UUID], agent_id: Union[str, UUID], situation: Optional[str]=None) -> ResourceCreatedResponse:
    Creates a new session with the specified user and agent IDs, and an optional situation.

async list(*, limit: Optional[int]=None, offset: Optional[int]=None) -> List[Session]:
    Lists sessions with an optional limit and offset for pagination.

- `async` *delete(session_id* - Union[str, UUID]):
    Deletes a session by its ID.

async update(*, session_id: Union[str, UUID], situation: str) -> ResourceUpdatedResponse:
    Updates the situation for a session by its ID.

async chat(*, session_id: str, messages: List[InputChatMlMessage], tools: Optional[List[Tool]]=None, tool_choice: Optional[ToolChoiceOption]=None, frequency_penalty: Optional[float]=None, length_penalty: Optional[float]=None, logit_bias: Optional[Dict[str, Optional[int]]]=None, max_tokens: Optional[int]=None, presence_penalty: Optional[float]=None, repetition_penalty: Optional[float]=None, response_format: Optional[ChatSettingsResponseFormat]=None, seed: Optional[int]=None, stop: Optional[ChatSettingsStop]=None, stream: Optional[bool]=None, temperature: Optional[float]=None, top_p: Optional[float]=None, recall: Optional[bool]=None, remember: Optional[bool]=None) -> ChatResponse:
    Initiates a chat session with given messages and optional parameters for the chat behavior and output.

async suggestions(*, session_id: Union[str, UUID], limit: Optional[int]=None, offset: Optional[int]=None) -> List[Suggestion]:
    Retrieves suggestions related to a session optionally limited and paginated.

async history(*, session_id: Union[str, UUID], limit: Optional[int]=None, offset: Optional[int]=None) -> List[ChatMlMessage]:
    Retrieves the history of messages in a session, optionally limited and paginated.

- `async` *delete_history(session_id* - Union[str, UUID]) -> None:

#### Notes

The `@beartype` decorator is used for runtime type checking of the arguments.

Additional methods may be provided by the BaseSessionsManager.

#### Signature

```python
class AsyncSessionsManager(BaseSessionsManager): ...
```

#### See also

- [BaseSessionsManager](#basesessionsmanager)

### AsyncSessionsManager().chat

[Show source in session.py:975](../../../../../../julep/managers/session.py#L975)

Sends a message in an asynchronous chat session and retrieves the response.

This method leverages the messaging interface with various options to adjust the behavior of the chat bot.

#### Arguments

- `session_id` *str* - The unique identifier for the chat session.
- `messages` *List[InputChatMlMessage]* - A list of chat messages in the session's context.
- `tools` *Optional[List[Tool]]* - A list of tools, if provided, to enhance the chat capabilities.
- `tool_choice` *Optional[ToolChoiceOption]* - A preference for tool selection during the chat.
- `frequency_penalty` *Optional[float]* - Adjusts how much the model should avoid repeating the same line of thought.
- `length_penalty` *Optional[float]* - Penalizes longer responses.
logit_bias (Optional[Dict[str, Optional[int]]]): Biases the model's prediction towards or away from certain tokens.
- `max_tokens` *Optional[int]* - The maximum length of the generated response.
- `presence_penalty` *Optional[float]* - Adjusts how much the model should consider new concepts.
- `repetition_penalty` *Optional[float]* - Adjusts how much the model should avoid repeating previous input.
- `response_format` *Optional[ChatSettingsResponseFormat]* - The desired format for the response.
- `seed` *Optional[int]* - A seed used to initialize the model's random number generator.
- `stop` *Optional[ChatSettingsStop]* - Tokens that signify the end of the response.
- `stream` *Optional[bool]* - Whether or not to stream the responses.
- `temperature` *Optional[float]* - Controls randomness in the response generation.
- `top_p` *Optional[float]* - Controls diversity via nucleus sampling.
- `recall` *Optional[bool]* - If true, the model recalls previous messages within the same session.
- `remember` *Optional[bool]* - If true, the model incorporates the context from the previous conversations in the session.

#### Returns

- `ChatResponse` - The response from the chat bot, encapsulating the result of the chat action.

#### Notes

This function is decorated with `@beartype`, which enforces type annotations at runtime.

#### Examples

```python
>>> response = await chat(...)
>>> print(response)
```

#### Signature

```python
@beartype
async def chat(
    self,
    session_id: str,
    messages: List[Union[InputChatMlMessageDict, InputChatMlMessage]],
    tools: Optional[List[Union[ToolDict, Tool]]] = None,
    tool_choice: Optional[ToolChoiceOption] = None,
    frequency_penalty: Optional[float] = None,
    length_penalty: Optional[float] = None,
    logit_bias: Optional[Dict[str, Optional[int]]] = None,
    max_tokens: Optional[int] = None,
    presence_penalty: Optional[float] = None,
    repetition_penalty: Optional[float] = None,
    response_format: Optional[
        Union[ChatSettingsResponseFormatDict, ChatSettingsResponseFormat]
    ] = None,
    seed: Optional[int] = None,
    stop: Optional[ChatSettingsStop] = None,
    stream: Optional[bool] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    recall: Optional[bool] = None,
    remember: Optional[bool] = None,
) -> ChatResponse: ...
```

### AsyncSessionsManager().create

[Show source in session.py:872](../../../../../../julep/managers/session.py#L872)

Asynchronously create a resource with the specified user and agent identifiers.

This function wraps an internal _create method and is decorated with `beartype` for run-time type checking.

#### Arguments

user_id (Union[str, UUID]): Unique identifier for the user.
agent_id (Union[str, UUID]): Unique identifier for the agent.
- `situation` *Optional[str], optional* - Description of the situation, defaults to None.

#### Returns

- `Session` - The created Session object

#### Raises

- `BeartypeException` - If any of the input arguments do not match their expected types.
Any exception raised by the internal _create method.

#### Signature

```python
@beartype
@rewrap_in_class(Session)
async def create(self, **kwargs: SessionCreateArgs) -> Session: ...
```

#### See also

- [SessionCreateArgs](#sessioncreateargs)

### AsyncSessionsManager().delete

[Show source in session.py:925](../../../../../../julep/managers/session.py#L925)

Asynchronously delete a session given its ID.

#### Arguments

session_id (Union[str, UUID]): The unique identifier for the session, which can
    be either a string or a UUID.

#### Returns

Coroutine[Any, Any, Any]: A coroutine that, when awaited, completes the deletion process.

#### Raises

The decorators or the body of the '_delete' method may define specific exceptions that
could be raised during the execution. Generally, include any exceptions that are raised
by the '_delete' method or by the 'beartype' decorator in this section.

#### Signature

```python
@beartype
async def delete(self, session_id: Union[str, UUID]): ...
```

### AsyncSessionsManager().delete_history

[Show source in session.py:1120](../../../../../../julep/managers/session.py#L1120)

Delete the history of a session asynchronously.

#### Arguments

session_id (Union[str, UUID]): The unique identifier for the session.

#### Returns

- `None` - The result of the delete operation.

#### Raises

- `AssertionError` - If the `session_id` is not a valid UUID v4.

#### Signature

```python
@beartype
async def delete_history(self, session_id: Union[str, UUID]) -> None: ...
```

### AsyncSessionsManager().get

[Show source in session.py:844](../../../../../../julep/managers/session.py#L844)

Asynchronously get a Session object by its identifier.

This method retrieves a Session based on the provided `id`. It uses an underlying
asynchronous '_get' method to perform the operation.

#### Arguments

id (Union[UUID, str]): The unique identifier of the Session to retrieve. It can be
    either a string representation or a UUID object.

#### Returns

- `Session` - The retrieved Session object associated with the given id.

#### Raises

- `TypeError` - If the `id` is not of type UUID or str.
- `ValueError` - If the `id` is not a valid UUID or an invalid string is provided.
- `AnyExceptionRaisedBy_get` - Descriptive name of specific exceptions that '_get'
    might raise, if any. Replace this with the actual exceptions.

#### Notes

The `@beartype` decorator is being used to enforce type checking at runtime.
This ensures that the argument `id` is of the correct type (UUID or str) and
that the return value is a Session object.

#### Signature

```python
@beartype
async def get(self, id: Union[UUID, str]) -> Session: ...
```

### AsyncSessionsManager().history

[Show source in session.py:1088](../../../../../../julep/managers/session.py#L1088)

Retrieve a history of chat messages based on the session ID, with optional limit and offset.

This function is decorated with 'beartype' for runtime type checking.

#### Arguments

session_id (Union[str, UUID]): The unique identifier for the chat session.
- `limit` *Optional[int], optional* - The maximum number of chat messages to return. Defaults to None.
- `offset` *Optional[int], optional* - The number of chat messages to skip before starting to collect the history slice. Defaults to None.

#### Returns

- `List[ChatMlMessage]` - A list of chat messages from the history that match the criteria.

#### Raises

Any exceptions that may be raised by the underlying '_history' method or 'beartype' decorator.

#### Signature

```python
@beartype
async def history(
    self,
    session_id: Union[str, UUID],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[ChatMlMessage]: ...
```

### AsyncSessionsManager().list

[Show source in session.py:895](../../../../../../julep/managers/session.py#L895)

Asynchronously retrieves a list of sessions with optional pagination.

This method utilizes `_list_items` internally to obtain session data with support for limit and offset parameters. The `beartype` decorator is used to ensure that the function parameters match the expected types.

#### Arguments

- `limit` *Optional[int], optional* - The maximum number of sessions to retrieve. Default is None, which retrieves all available sessions.
- `offset` *Optional[int], optional* - The number to skip before starting to collect the response set. Default is None.

#### Returns

- `List[Session]` - A list of `Session` objects containing session data.

#### Signature

```python
@beartype
async def list(
    self,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    metadata_filter: Dict[str, Any] = {},
) -> List[Session]: ...
```

### AsyncSessionsManager().suggestions

[Show source in session.py:1056](../../../../../../julep/managers/session.py#L1056)

Retrieve a list of suggestions asynchronously.

This function asynchronously fetches suggestions based on the provided session ID, with optional limit and offset parameters for pagination.

#### Arguments

session_id (Union[str, UUID]): The session identifier for which suggestions are to be retrieved.
- `limit` *Optional[int]* - The maximum number of suggestions to return. Defaults to None, which means no limit.
- `offset` *Optional[int]* - The number of suggestions to skip before starting to return results. Defaults to None, which means no offset.

#### Returns

- `List[Suggestion]` - A list of Suggestion objects.

#### Raises

- `Exception` - Raises an exception if the underlying _suggestions call fails.

#### Signature

```python
@beartype
async def suggestions(
    self,
    session_id: Union[str, UUID],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[Suggestion]: ...
```

### AsyncSessionsManager().update

[Show source in session.py:944](../../../../../../julep/managers/session.py#L944)

Asynchronously update a resource with the given situation.

This method wraps the private `_update` method which performs the actual update
operation asynchronously.

#### Arguments

session_id (Union[str, UUID]): The session ID of the resource to update.
    It can be either a `str` or a `UUID` object.
- `situation` *str* - Description of the situation to update the resource with.

#### Returns

- `Session` - The updated Session object

#### Notes

This function is decorated with `@beartype`, which will perform runtime type
checking on the arguments.

#### Raises

- `BeartypeCallHintParamViolation` - If the `session_id` or `situation`
    arguments do not match their annotated types.

#### Signature

```python
@beartype
@rewrap_in_class(Session)
async def update(self, **kwargs: SessionUpdateArgs) -> Session: ...
```

#### See also

- [SessionUpdateArgs](#sessionupdateargs)



## BaseSessionsManager

[Show source in session.py:57](../../../../../../julep/managers/session.py#L57)

A class to manage sessions using base API client methods.

This manager handles CRUD operations and additional actions on the session data,
such as chatting and retrieving history or suggestions.

#### Attributes

- `api_client` - The client used for communicating with an API.

#### Methods

_get(id):
    Retrieve a specific session by its identifier.

#### Arguments

id (Union[str, UUID]): The unique identifier for the session.

agent_id (Union[str, UUID]): The unique identifier for the agent.
user_id (Optional[Union[str, UUID]]): The unique identifier for the user.
- `situation` *Optional[str]* - An optional description of the situation for the session.

- `limit` *Optional[int]* - The limit on the number of items to be retrieved.
- `offset` *Optional[int]* - The number of items to be skipped before starting to collect the result set.

session_id (Union[str, UUID]): The unique identifier for the session to be deleted.

session_id (Union[str, UUID]): The unique identifier for the session to be updated.
- `situation` *str* - The new situation description for the session.

- `session_id` *str* - The unique identifier for the session.
- `messages` *List[InputChatMlMessage]* - The list of input chat messages to be sent.
- `tools` *Optional[List[Tool]]* - ...
- `tool_choice` *Optional[ToolChoiceOption]* - ...
- `...` - Other optional parameters for chat settings and modifiers.

session_id (Union[str, UUID]): The unique identifier for the session.
- `limit` *Optional[int]* - The limit on the number of suggestions to be retrieved.
- `offset` *Optional[int]* - The number of suggestions to be skipped before starting to collect the result set.

session_id (Union[str, UUID]): The unique identifier for the session.
- `limit` *Optional[int]* - The limit on the number of history entries to be retrieved.
- `offset` *Optional[int]* - The number of history entries to be skipped before starting to collect the result set.

session_id (Union[str, UUID]): The unique identifier for the session.

#### Returns

- `Union[Session,` *Awaitable[Session]]* - The session object or an awaitable yielding it.

- `Union[ResourceCreatedResponse,` *Awaitable[ResourceCreatedResponse]]* - The response for the created session or an awaitable yielding it.

_list_items(limit, offset):
    List multiple session items with optional pagination.

- `Union[ListSessionsResponse,` *Awaitable[ListSessionsResponse]]* - The list of sessions or an awaitable yielding it.

_delete(session_id):
    Delete a session by its identifier.

- `Union[None,` *Awaitable[None]]* - None or an awaitable yielding None if the operation is successful.

_update(session_id, situation):
    Update the situation for an existing session.

- `Union[ResourceUpdatedResponse,` *Awaitable[ResourceUpdatedResponse]]* - The response for the updated session or an awaitable yielding it.

_chat(session_id, messages, ...):
    Send chat messages and get responses during a session.

- `Union[ChatResponse,` *Awaitable[ChatResponse]]* - The chat response for the session or an awaitable yielding it.

_suggestions(session_id, limit, offset):
    Get suggestions for a session.

- `Union[GetSuggestionsResponse,` *Awaitable[GetSuggestionsResponse]]* - The suggestions response for the session or an awaitable yielding it.

_history(session_id, limit, offset):
    Get the history for a session.

- `Union[GetHistoryResponse,` *Awaitable[GetHistoryResponse]]* - The history response for the session or an awaitable yielding it.

_delete_history(session_id):
    Delete the history of a session.

- `Union[None,` *Awaitable[None]]* - None or an awaitable yielding None if the operation is successful.

#### Raises

- `ValueError` - If the `id` is not a valid UUID.
- `NetworkError` - If there is an issue communicating with the API.

_create(user_id, agent_id, situation):
    Create a new session with specified user and agent identifiers.

#### Signature

```python
class BaseSessionsManager(BaseManager): ...
```

### BaseSessionsManager()._chat

[Show source in session.py:310](../../../../../../julep/managers/session.py#L310)

Conducts a chat conversation with an AI model using specific parameters.

#### Arguments

- `session_id` *str* - A unique identifier for the chat session.
- `messages` *List[InputChatMlMessage]* - A list of input messages for the AI to respond to.
- `tools` *Optional[List[Tool]]* - A list of tools to be used during the chat session.
- `tool_choice` *Optional[ToolChoiceOption]* - A method for choosing which tools to apply.
- `frequency_penalty` *Optional[float]* - A modifier to decrease the likelihood of frequency-based repetitions.
- `length_penalty` *Optional[float]* - A modifier to control the length of the generated responses.
logit_bias (Optional[Dict[str, Optional[int]]]): Adjustments to the likelihood of specific tokens appearing.
- `max_tokens` *Optional[int]* - The maximum number of tokens to generate in the output.
- `presence_penalty` *Optional[float]* - A modifier to control for new concepts' appearance.
- `repetition_penalty` *Optional[float]* - A modifier to discourage repetitive responses.
- `response_format` *Optional[ChatSettingsResponseFormat]* - The format in which the response is to be delivered.
- `seed` *Optional[int]* - An integer to seed the random number generator for reproducibility.
- `stop` *Optional[ChatSettingsStop]* - Tokens at which to stop generating further tokens.
- `stream` *Optional[bool]* - Whether to stream the response or deliver it when it's complete.
- `temperature` *Optional[float]* - A value to control the randomness of the output.
- `top_p` *Optional[float]* - A value to control the nucleus sampling, i.e., the cumulative probability cutoff.
- `recall` *Optional[bool]* - A flag to control the recall capability of the AI model.
- `remember` *Optional[bool]* - A flag to control the persistence of the chat history in the AI's memory.

#### Returns

- `Union[ChatResponse,` *Awaitable[ChatResponse]]* - The response from the AI given the input messages and parameters. This could be a synchronous `ChatResponse` object or an asynchronous `Awaitable[ChatResponse]` if the `stream` parameter is True.

#### Notes

The precise types of some arguments, like `Tool`, `ToolChoiceOption`, `ChatSettingsResponseFormat`, and `ChatSettingsStop`, are not defined within the given context. It's assumed that these types have been defined elsewhere in the code base.

#### Raises

It is not specified what exceptions this function might raise. Typically, one would expect potential exceptions to be associated with the underlying API client's `chat` method failure modes, such as network issues, invalid parameters, etc.

#### Signature

```python
def _chat(
    self,
    session_id: str,
    messages: List[Union[InputChatMlMessageDict, InputChatMlMessage]],
    tools: Optional[List[Union[ToolDict, Tool]]] = None,
    tool_choice: Optional[ToolChoiceOption] = None,
    frequency_penalty: Optional[float] = None,
    length_penalty: Optional[float] = None,
    logit_bias: Optional[Dict[str, Optional[int]]] = None,
    max_tokens: Optional[int] = None,
    presence_penalty: Optional[float] = None,
    repetition_penalty: Optional[float] = None,
    response_format: Optional[
        Union[ChatSettingsResponseFormatDict, ChatSettingsResponseFormat]
    ] = None,
    seed: Optional[int] = None,
    stop: Optional[ChatSettingsStop] = None,
    stream: Optional[bool] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    recall: Optional[bool] = None,
    remember: Optional[bool] = None,
) -> Union[ChatResponse, Awaitable[ChatResponse]]: ...
```

### BaseSessionsManager()._create

[Show source in session.py:182](../../../../../../julep/managers/session.py#L182)

Creates a session for a specified user and agent.

This internal method is responsible for creating a session using the API client. It validates that both the user and agent IDs are valid UUID v4 strings before proceeding with session creation.

#### Arguments

agent_id (Union[str, UUID]): The agent's identifier which could be a string or a UUID object.
user_id (Optional[Union[str, UUID]]): The user's identifier which could be a string or a UUID object.
- `situation` *Optional[str], optional* - An optional description of the situation.
metadata (Dict[str, Any])
- `render_templates` *bool, optional* - Whether to render templates in the metadata. Defaults to False.

#### Returns

- `Union[ResourceCreatedResponse,` *Awaitable[ResourceCreatedResponse]]* - The response from the API client upon successful session creation, which can be a synchronous `ResourceCreatedResponse` or an asynchronous `Awaitable` of it.

#### Raises

- `AssertionError` - If either `user_id` or `agent_id` is not a valid UUID v4.

#### Signature

```python
def _create(
    self,
    agent_id: Union[str, UUID],
    user_id: Optional[Union[str, UUID]] = None,
    situation: Optional[str] = None,
    metadata: Dict[str, Any] = {},
    render_templates: bool = False,
    token_budget: Optional[int] = None,
    context_overflow: Optional[str] = None,
) -> Union[ResourceCreatedResponse, Awaitable[ResourceCreatedResponse]]: ...
```

### BaseSessionsManager()._delete

[Show source in session.py:251](../../../../../../julep/managers/session.py#L251)

Delete a session given its session ID.

This is an internal method that asserts the provided session_id is a valid UUID v4
before making the delete request through the API client.

Args:
    session_id (Union[str, UUID]): The session identifier, which should be a valid UUID v4.

Returns:
    Union[None, Awaitable[None]]: The result of the delete operation, which can be either
    None or an Awaitable that resolves to None, depending on whether this is a synchronous
    or asynchronous call.

Raises:
    AssertionError: If the `session_id` is not a valid UUID v4.

#### Signature

```python
def _delete(self, session_id: Union[str, UUID]) -> Union[None, Awaitable[None]]: ...
```

### BaseSessionsManager()._delete_history

[Show source in session.py:444](../../../../../../julep/managers/session.py#L444)

Delete the history of a session.

#### Arguments

session_id (Union[str, UUID]): The unique identifier for the session.

#### Returns

- `Union[None,` *Awaitable[None]]* - The result of the delete operation, which can be either
None or an Awaitable that resolves to None, depending on whether this is a synchronous
or asynchronous call.

#### Raises

- `AssertionError` - If the `session_id` is not a valid UUID v4.

#### Signature

```python
def _delete_history(
    self, session_id: Union[str, UUID]
) -> Union[None, Awaitable[None]]: ...
```

### BaseSessionsManager()._get

[Show source in session.py:166](../../../../../../julep/managers/session.py#L166)

Get a session by its ID.

#### Arguments

id (Union[str, UUID]): A string or UUID representing the session ID.

#### Returns

- `Union[Session,` *Awaitable[Session]]* - The session object associated with the given ID, which can be either a `Session` instance or an `Awaitable` that resolves to a `Session`.

#### Raises

- `AssertionError` - If the id is not a valid UUID v4.

#### Signature

```python
def _get(self, id: Union[str, UUID]) -> Union[Session, Awaitable[Session]]: ...
```

### BaseSessionsManager()._history

[Show source in session.py:416](../../../../../../julep/managers/session.py#L416)

Retrieve a session's history with optional pagination controls.

Args:
    session_id (Union[str, UUID]): Unique identifier for the session
        whose history is being queried. Can be a string or a UUID object.
    limit (Optional[int], optional): The maximum number of history
        entries to retrieve. Defaults to None, which uses the API's default setting.
    offset (Optional[int], optional): The number of initial history
        entries to skip. Defaults to None, which means no offset is applied.

Returns:
    Union[GetHistoryResponse, Awaitable[GetHistoryResponse]]:
        The history response object, which may be either synchronous or
        asynchronous (awaitable), depending on the API client configuration.

#### Signature

```python
def _history(
    self,
    session_id: Union[str, UUID],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Union[GetHistoryResponse, Awaitable[GetHistoryResponse]]: ...
```

### BaseSessionsManager()._list_items

[Show source in session.py:226](../../../../../../julep/managers/session.py#L226)

List items with optional pagination.

#### Arguments

- `limit` *Optional[int]* - The maximum number of items to return. Defaults to None.
- `offset` *Optional[int]* - The number of items to skip before starting to collect the result set. Defaults to None.

#### Returns

- `Union[ListSessionsResponse,` *Awaitable[ListSessionsResponse]]* - The response object containing the list of items or an awaitable response object if called asynchronously.

#### Notes

The '_list_items' function is assumed to be a method of a class that has an 'api_client' attribute capable of listing sessions.

#### Signature

```python
def _list_items(
    self,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    metadata_filter: str = "{}",
) -> Union[ListSessionsResponse, Awaitable[ListSessionsResponse]]: ...
```

### BaseSessionsManager()._suggestions

[Show source in session.py:393](../../../../../../julep/managers/session.py#L393)

Retrieve a list of suggestions for a given session.

Args:
    session_id (Union[str, UUID]): The ID of the session for which to get suggestions.
    limit (Optional[int], optional): The maximum number of suggestions to retrieve. Defaults to None.
    offset (Optional[int], optional): The offset from where to start retrieving suggestions. Defaults to None.

Returns:
    Union[GetSuggestionsResponse, Awaitable[GetSuggestionsResponse]]: The response containing the list of suggestions synchronously or asynchronously, depending on the API client.

#### Signature

```python
def _suggestions(
    self,
    session_id: Union[str, UUID],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Union[GetSuggestionsResponse, Awaitable[GetSuggestionsResponse]]: ...
```

### BaseSessionsManager()._update

[Show source in session.py:272](../../../../../../julep/managers/session.py#L272)

Update a session with a given situation.

#### Arguments

session_id (Union[str, UUID]): The session identifier, which can be a string-formatted UUID or an actual UUID object.
- `situation` *str* - A string describing the current situation.
- `overwrite` *bool, optional* - Whether to overwrite the existing situation. Defaults to False.

#### Returns

- `Union[ResourceUpdatedResponse,` *Awaitable[ResourceUpdatedResponse]]* - The response from the update operation, which can be either synchronous or asynchronous.

#### Raises

- `AssertionError` - If `session_id` is not a valid UUID v4.

#### Signature

```python
def _update(
    self,
    session_id: Union[str, UUID],
    situation: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    overwrite: bool = False,
    token_budget: Optional[int] = None,
    context_overflow: Optional[str] = None,
) -> Union[ResourceUpdatedResponse, Awaitable[ResourceUpdatedResponse]]: ...
```



## SessionCreateArgs

[Show source in session.py:37](../../../../../../julep/managers/session.py#L37)

#### Signature

```python
class SessionCreateArgs(TypedDict): ...
```



## SessionUpdateArgs

[Show source in session.py:47](../../../../../../julep/managers/session.py#L47)

#### Signature

```python
class SessionUpdateArgs(TypedDict): ...
```



## SessionsManager

[Show source in session.py:466](../../../../../../julep/managers/session.py#L466)

A class responsible for managing session interactions.

This class extends [BaseSessionsManager](#basesessionsmanager) and provides methods to get, create,
list, delete, and update sessions, as well as to initiate a chat within a session,
request suggestions, and access session history.

#### Methods

- `get` *(id* - Union[str, UUID]) -> Session:
    Retrieves a session by its identifier.

create (
    *,
    - `user_id` - Union[str, UUID],
    - `agent_id` - Union[str, UUID],
    - `situation` - Optional[str]=None
) -> ResourceCreatedResponse:
    Creates a new session given a user ID and an agent ID, and optionally
    a description of the situation.

list (
    *,
    - `limit` - Optional[int]=None,
    - `offset` - Optional[int]=None
) -> List[Session]:
    Lists sessions with optional pagination via limit and offset.

- `delete` *(session_id* - Union[str, UUID]):
    Deletes a session identified by the given session ID.

update (
    *,
    - `session_id` - Union[str, UUID],
    - `situation` - str
) -> ResourceUpdatedResponse:
    Updates the situation of a specific session by its ID.

chat (
    *args
    see full method signature for detailed arguments
) -> ChatResponse:
    Initiates a chat in the given session with messages and various settings,
    including tools, penalties, biases, tokens, response format, etc.

suggestions (
    *,
    - `session_id` - Union[str, UUID],
    - `limit` - Optional[int]=None,
    - `offset` - Optional[int]=None
) -> List[Suggestion]:
    Retrieves a list of suggestions for a given session, supported by
    optional pagination parameters.

history (
    *,
    - `session_id` - Union[str, UUID],
    - `limit` - Optional[int]=None,
    - `offset` - Optional[int]=None
) -> List[ChatMlMessage]:
    Retrieves the chat history for a given session, supported by
    optional pagination parameters.

- `delete_history` *(session_id* - Union[str, UUID]) -> None:

Each method is decorated with `@beartype` for runtime type enforcement.

#### Signature

```python
class SessionsManager(BaseSessionsManager): ...
```

#### See also

- [BaseSessionsManager](#basesessionsmanager)

### SessionsManager().chat

[Show source in session.py:647](../../../../../../julep/managers/session.py#L647)

Initiate a chat session with the provided inputs and configurations.

#### Arguments

- `session_id` *str* - Unique identifier for the chat session.
- `messages` *List[InputChatMlMessage]* - List of messages to send in the chat session.
- `tools` *Optional[List[Tool]], optional* - List of tools to be used in the session. Defaults to None.
- `tool_choice` *Optional[ToolChoiceOption], optional* - The choice of tool to optimize response for. Defaults to None.
- `frequency_penalty` *Optional[float], optional* - Penalty for frequent tokens to control repetition. Defaults to None.
- `length_penalty` *Optional[float], optional* - Penalty for longer responses to control verbosity. Defaults to None.
logit_bias (Optional[Dict[str, Optional[int]]], optional): Bias for or against specific tokens. Defaults to None.
- `max_tokens` *Optional[int], optional* - Maximum number of tokens to generate in the response. Defaults to None.
- `presence_penalty` *Optional[float], optional* - Penalty for new tokens to control topic introduction. Defaults to None.
- `repetition_penalty` *Optional[float], optional* - Penalty to discourage repetition. Defaults to None.
- `response_format` *Optional[ChatSettingsResponseFormat], optional* - Format of the response. Defaults to None.
- `seed` *Optional[int], optional* - Random seed for deterministic responses. Defaults to None.
- `stop` *Optional[ChatSettingsStop], optional* - Sequence at which to stop generating further tokens. Defaults to None.
- `stream` *Optional[bool], optional* - Whether to stream responses or not. Defaults to None.
- `temperature` *Optional[float], optional* - Sampling temperature for randomness in the response. Defaults to None.
- `top_p` *Optional[float], optional* - Nucleus sampling parameter to control diversity. Defaults to None.
- `recall` *Optional[bool], optional* - Whether to allow recalling previous parts of the chat. Defaults to None.
- `remember` *Optional[bool], optional* - Whether to allow the model to remember previous chats. Defaults to None.

#### Returns

- `ChatResponse` - The response object after processing chat messages.

#### Notes

The 'beartype' decorator is used for runtime type checking.

#### Signature

```python
@beartype
def chat(
    self,
    session_id: str,
    messages: List[Union[InputChatMlMessageDict, InputChatMlMessage]],
    tools: Optional[List[Union[ToolDict, Tool]]] = None,
    tool_choice: Optional[ToolChoiceOption] = None,
    frequency_penalty: Optional[float] = None,
    length_penalty: Optional[float] = None,
    logit_bias: Optional[Dict[str, Optional[int]]] = None,
    max_tokens: Optional[int] = None,
    presence_penalty: Optional[float] = None,
    repetition_penalty: Optional[float] = None,
    response_format: Optional[
        Union[ChatSettingsResponseFormatDict, ChatSettingsResponseFormat]
    ] = None,
    seed: Optional[int] = None,
    stop: Optional[ChatSettingsStop] = None,
    stream: Optional[bool] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    recall: Optional[bool] = None,
    remember: Optional[bool] = None,
) -> ChatResponse: ...
```

### SessionsManager().create

[Show source in session.py:551](../../../../../../julep/managers/session.py#L551)

Create a new resource with a user ID and an agent ID, optionally including a situation description.

#### Arguments

user_id (Union[str, UUID]): The unique identifier for the user.
agent_id (Union[str, UUID]): The unique identifier for the agent.
- `situation` *Optional[str]* - An optional description of the situation.

#### Returns

- `Session` - The created Session object.

#### Raises

- `BeartypeException` - If the provided `user_id` or `agent_id` do not match the required type.
Any other exception that `_create` might raise.

#### Signature

```python
@beartype
@rewrap_in_class(Session)
def create(self, **kwargs: SessionCreateArgs) -> Session: ...
```

#### See also

- [SessionCreateArgs](#sessioncreateargs)

### SessionsManager().delete

[Show source in session.py:603](../../../../../../julep/managers/session.py#L603)

Deletes a session based on its session ID.

#### Arguments

session_id (Union[str, UUID]): The session ID to be deleted, which can be a string or a UUID object.

#### Returns

The result from the internal `_delete` method call.

#### Raises

The specific exceptions that `self._delete` might raise, which should be documented in its docstring.

#### Signature

```python
@beartype
def delete(self, session_id: Union[str, UUID]): ...
```

### SessionsManager().delete_history

[Show source in session.py:783](../../../../../../julep/managers/session.py#L783)

Delete the history of a session.

#### Arguments

session_id (Union[str, UUID]): The unique identifier for the session.

#### Returns

- `None` - The result of the delete operation.

#### Raises

- `AssertionError` - If the `session_id` is not a valid UUID v4.

#### Signature

```python
@beartype
def delete_history(self, session_id: Union[str, UUID]) -> None: ...
```

### SessionsManager().get

[Show source in session.py:534](../../../../../../julep/managers/session.py#L534)

Retrieve a Session object based on a given identifier.

Args:
    id (Union[str, UUID]): The identifier of the session, which can be either a string or a UUID.

Returns:
    Session: The session object associated with the given id.

Raises:
    TypeError: If the id is neither a string nor a UUID.
    KeyError: If the session with the given id does not exist.

#### Signature

```python
@beartype
def get(self, id: Union[str, UUID]) -> Session: ...
```

### SessionsManager().history

[Show source in session.py:756](../../../../../../julep/managers/session.py#L756)

Retrieve a history of ChatMl messages for a given session.

This method uses the private method `_history` to fetch the message history and returns a list of ChatMlMessage objects.

Args:
    session_id (Union[str, UUID]): The session identifier to fetch the chat history for.
    limit (Optional[int], optional): The maximum number of messages to return. If None, no limit is applied. Defaults to None.
    offset (Optional[int], optional): The offset from where to start fetching messages. If None, no offset is applied. Defaults to None.

Returns:
    List[ChatMlMessage]: A list of ChatMlMessage objects representing the history of messages for the session.

#### Signature

```python
@beartype
def history(
    self,
    session_id: Union[str, UUID],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[ChatMlMessage]: ...
```

### SessionsManager().list

[Show source in session.py:572](../../../../../../julep/managers/session.py#L572)

Retrieve a list of Session objects with optional pagination.

Args:
    limit (Optional[int]): The maximum number of Session objects to return.
        Defaults to None, which indicates no limit.
    offset (Optional[int]): The number of items to skip before starting to return the results.
        Defaults to None, which indicates no offset.

Returns:
    List[Session]: A list of Session objects meeting the criteria.

Raises:
    BeartypeException: If the input arguments do not match their annotated types.

#### Signature

```python
@beartype
def list(
    self,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    metadata_filter: Dict[str, Any] = {},
) -> List[Session]: ...
```

### SessionsManager().suggestions

[Show source in session.py:722](../../../../../../julep/managers/session.py#L722)

Provides a list of suggestion objects based on the given session ID.

This method retrieves suggestions and is decorated with `beartype` for runtime type
checking of the passed arguments.

#### Arguments

session_id (Union[str, UUID]): The ID of the session to retrieve suggestions for.
- `limit` *Optional[int], optional* - The maximum number of suggestions to return.
    Defaults to None, which means no limit.
- `offset` *Optional[int], optional* - The number to offset the list of returned
    suggestions by. Defaults to None, which means no offset.

#### Returns

- `List[Suggestion]` - A list of suggestion objects.

#### Raises

Any exceptions that `_suggestions` might raise, for example, if the method is unable
to retrieve suggestions based on the provided session ID.

#### Signature

```python
@beartype
def suggestions(
    self,
    session_id: Union[str, UUID],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[Suggestion]: ...
```

### SessionsManager().update

[Show source in session.py:619](../../../../../../julep/managers/session.py#L619)

Updates the state of a resource based on a given situation.

This function is type-checked using beartype to ensure that the `session_id` parameter
is either a string or a UUID and that the `situation` parameter is a string. It delegates
the actual update process to an internal method '_update'.

#### Arguments

session_id (Union[str, UUID]): The session identifier, which can be a UUID or a
    string that uniquely identifies the session.
- `situation` *str* - A string that represents the new situation for the resource update.
- `overwrite` *bool, optional* - A flag to indicate whether to overwrite the existing

#### Returns

- `Session` - The updated Session object.

#### Notes

The `@beartype` decorator is used for runtime type checking of the function arguments.

#### Signature

```python
@beartype
@rewrap_in_class(Session)
def update(self, **kwargs: SessionUpdateArgs) -> Session: ...
```

#### See also

- [SessionUpdateArgs](#sessionupdateargs)