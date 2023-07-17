# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.event_id import EventId


class AgentLog(pydantic.BaseModel):
    """
    A log of an agent execution
    """

    event_id: EventId = pydantic.Field(alias="eventId")
    success: bool = pydantic.Field(description="Whether the agent execution was successful")
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    completed_at: dt.datetime = pydantic.Field(alias="completedAt")
    log: typing.Optional[str] = pydantic.Field(description="The log of the agent execution")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
