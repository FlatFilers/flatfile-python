# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .job_outcome import JobOutcome

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class JobCompleteDetails(pydantic.BaseModel):
    """
    Outcome summary of a job
    ---
    from flatfile import JobCompleteDetails, JobOutcome, JobOutcomeNext_Id

    JobCompleteDetails(
        outcome=JobOutcome(
            acknowledge=True,
            button_text="Acknowledge",
            next=JobOutcomeNext_Id(
                type="id",
                id="us_jb_YOUR_ID",
            ),
            heading="Success",
            message="Job was successful",
        ),
        info="Job is Complete",
    )
    """

    outcome: typing.Optional[JobOutcome] = None
    info: typing.Optional[str] = None

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
