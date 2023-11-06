# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.agent_id import AgentId
from .agent_config import AgentConfig


class Agent(AgentConfig):
    """
    from flatfile import Agent, Compiler, EventTopic

    Agent(
        id="us_ag_YOUR_ID",
        topics=[EventTopic.FILE_CREATED],
        compiler=Compiler.JS,
        source="module.exports = { routeEvent: async (...args) => { console.log(args) } }",
    )
    """

    id: AgentId

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
