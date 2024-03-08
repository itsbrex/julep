# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .memory_emotions_item import MemoryEmotionsItem
from .memory_type import MemoryType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Memory(pydantic.BaseModel):
    type: MemoryType = pydantic.Field(
        description="Type of memory (`episode` or `belief`)"
    )
    agent_id: str = pydantic.Field(description="ID of the agent")
    user_id: str = pydantic.Field(description="ID of the user")
    content: str = pydantic.Field(description="Content of the memory")
    weight: typing.Optional[float] = pydantic.Field(
        description="Weight (importance) of the memory on a scale of 0-100"
    )
    created_at: dt.datetime = pydantic.Field(
        description="Memory created at (RFC-3339 format)"
    )
    last_accessed_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Memory last accessed at (RFC-3339 format)"
    )
    timestamp: typing.Optional[dt.datetime] = pydantic.Field(
        description="Memory happened at (RFC-3339 format)"
    )
    sentiment: typing.Optional[float] = pydantic.Field(
        description="Sentiment (valence) of the memory on a scale of -1 to 1"
    )
    duration: typing.Optional[float] = pydantic.Field(
        description="Duration of the Memory (in seconds)"
    )
    id: str = pydantic.Field(description="Memory id (UUID)")
    emotions: typing.Optional[typing.List[MemoryEmotionsItem]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
