# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .validation_type import ValidationType
from .validation_source import ValidationSource
from ...commons.types.json_path_string import JsonPathString
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ValidationMessage(UniversalBaseModel):
    """
    Record data validation messages
    """

    field: typing.Optional[str] = None
    type: typing.Optional[ValidationType] = None
    source: typing.Optional[ValidationSource] = None
    message: typing.Optional[str] = None
    path: typing.Optional[JsonPathString] = pydantic.Field(default=None)
    """
    This JSONPath is based on the root of mapped cell object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
