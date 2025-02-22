# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class JobOutcomeNextView(UniversalBaseModel):
    sheet_id: typing_extensions.Annotated[str, FieldMetadata(alias="sheetId")]
    hidden_columns: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="hiddenColumns")] = (
        pydantic.Field()
    )
    """
    An array of field keys from the sheet
    """

    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
