# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .progress import Progress


class EventAttributes(pydantic.BaseModel):
    """
    The attributes of the event
    """

    target_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="targetUpdatedAt", description="Date the related entity was last updated"
    )
    progress: typing.Optional[Progress] = pydantic.Field(
        description="The progress of the event within a collection of iterable events"
    )

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
