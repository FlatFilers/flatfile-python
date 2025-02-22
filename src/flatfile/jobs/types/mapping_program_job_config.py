# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...commons.types.sheet_id import SheetId
from ...core.serialization import FieldMetadata
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MappingProgramJobConfig(UniversalBaseModel):
    source_sheet_id: typing_extensions.Annotated[SheetId, FieldMetadata(alias="sourceSheetId")]
    destination_sheet_id: typing_extensions.Annotated[SheetId, FieldMetadata(alias="destinationSheetId")]
    mapping_rules: typing_extensions.Annotated[
        typing.List[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="mappingRules")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
