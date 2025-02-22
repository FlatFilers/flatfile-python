# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .validation_message import ValidationMessage
import pydantic
from .cell_value_union import CellValueUnion
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CellValue(UniversalBaseModel):
    valid: typing.Optional[bool] = None
    messages: typing.Optional[typing.List[ValidationMessage]] = None
    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Deprecated, use record level metadata instead.
    """

    value: typing.Optional[CellValueUnion] = None
    layer: typing.Optional[str] = None
    updated_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
