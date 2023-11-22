# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...events.types.event_topic import EventTopic
from .compiler import Compiler

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AgentConfig(pydantic.BaseModel):
    """
    Properties used to create a new agent
    ---
    from flatfile import AgentConfig, Compiler, EventTopic

    AgentConfig(
        topics=[EventTopic.WORKBOOK_UPDATED],
        compiler=Compiler.JS,
        source="module.exports = { routeEvent: async (...args) => { console.log(args) } }",
    )
    """

    topics: typing.Optional[typing.List[EventTopic]] = pydantic.Field(
        description="The topics the agent should listen for"
    )
    compiler: typing.Optional[Compiler] = pydantic.Field(description="The compiler of the agent")
    source: typing.Optional[str] = pydantic.Field(description="The source of the agent")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
