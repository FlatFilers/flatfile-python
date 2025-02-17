# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class JobAckDetails(UniversalBaseModel):
    """
    Details about the user who acknowledged the job

    Examples
    --------
    import datetime

    from flatfile.jobs import JobAckDetails

    JobAckDetails(
        info="Acknowledged by user",
        progress=100,
        estimated_completion_at=datetime.datetime.fromisoformat(
            "2023-10-30 20:04:32.074000+00:00",
        ),
    )
    """

    info: typing.Optional[str] = None
    progress: typing.Optional[int] = pydantic.Field(default=None)
    """
    the progress of the job. Whole number between 0 and 100
    """

    estimated_completion_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="estimatedCompletionAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
