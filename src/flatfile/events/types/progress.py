# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Progress(UniversalBaseModel):
    """
    The progress of the event within a collection of iterable events
    """

    current: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current progress of the event
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of events in this group
    """

    percent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The percent complete of the event group
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
