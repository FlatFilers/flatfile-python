# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class JobAckDetails(pydantic.BaseModel):
    """
    Details about the user who acknowledged the job
    ---
    import datetime

    from flatfile import JobAckDetails

    JobAckDetails(
        info="Acknowledged by user",
        progress=100,
        estimated_completion_at=datetime.datetime.fromisoformat(
            "2023-10-30 20:04:32.074000+00:00",
        ),
    )
    """

    info: typing.Optional[str]
    progress: typing.Optional[int] = pydantic.Field(
        description="the progress of the job. Whole number between 0 and 100"
    )
    estimated_completion_at: typing.Optional[dt.datetime] = pydantic.Field(alias="estimatedCompletionAt")

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
