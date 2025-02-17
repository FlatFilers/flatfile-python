# This file was auto-generated by Fern from our API Definition.

from .base_property import BaseProperty
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class StringListProperty(BaseProperty):
    """
    Defines a property that should be stored and read as an array of strings. Database engines should expect any number of items to be provided here. The maximum number of items that can be in this list is `100`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
