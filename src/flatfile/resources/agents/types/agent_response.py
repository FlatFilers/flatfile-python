# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .agent import Agent

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AgentResponse(pydantic.BaseModel):
    """
    from flatfile import Agent, AgentResponse, Compiler, EventTopic

    AgentResponse(
        data=Agent(
            id="us_ag_YOUR_ID",
            topics=[EventTopic.WORKBOOK_UPDATED],
            compiler=Compiler.JS,
            source="module.exports = { routeEvent: async (...args) => { console.log(args) } }",
            slug="default",
        ),
    )
    """

    data: typing.Optional[Agent] = None

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
