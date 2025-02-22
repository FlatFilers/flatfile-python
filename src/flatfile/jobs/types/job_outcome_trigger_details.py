# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .job_outcome_trigger_type import JobOutcomeTriggerType
import typing
from .job_outcome_trigger_audience import JobOutcomeTriggerAudience
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class JobOutcomeTriggerDetails(UniversalBaseModel):
    """
    Details about the trigger for the job outcome
    """

    type: JobOutcomeTriggerType
    audience: typing.Optional[JobOutcomeTriggerAudience] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
