# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from ...commons.types.sheet_id import SheetId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class WorkbookConfigSettings(UniversalBaseModel):
    """
    Settings for a workbook
    """

    track_changes: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="trackChanges")] = (
        pydantic.Field(default=None)
    )
    """
    Whether to track changes for this workbook. Defaults to false. Tracking changes on a workbook allows for disabling workbook and sheet actions while data in the workbook is still being processed. You must run a recordHook listener if you enable this feature.
    """

    no_mapping_redirect: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="noMappingRedirect")
    ] = pydantic.Field(default=None)
    """
    When noMappingRedirect is set to true, dragging a file into a sheet will not redirect to the mapping screen. Defaults to false.
    """

    sheet_sidebar_order: typing_extensions.Annotated[
        typing.Optional[typing.List[SheetId]], FieldMetadata(alias="sheetSidebarOrder")
    ] = pydantic.Field(default=None)
    """
    Used to set the order of sheets in the sidebar. Sheets that are not specified will be shown after those listed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
