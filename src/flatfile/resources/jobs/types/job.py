# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.job_id import JobId
from .job_config import JobConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Job(JobConfig):
    """
    A single unit of work that will execute asynchronously
    """

    id: JobId
    created_at: dt.datetime = pydantic.Field(alias="createdAt", description="Date the item was created")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt", description="Date the item was last updated")
    started_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="startedAt", description="the time that the job started at"
    )
    finished_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="finishedAt", description="the time that the job finished at"
    )
    outcome_acknowledged_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="outcomeAcknowledgedAt", description="the time that the job's outcome has been acknowledged by a user"
    )

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
