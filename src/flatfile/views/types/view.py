# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...commons.types.view_id import ViewId
import pydantic
import typing_extensions
from ...commons.types.sheet_id import SheetId
from ...core.serialization import FieldMetadata
from .view_config import ViewConfig
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class View(UniversalBaseModel):
    """
    A view

    Examples
    --------
    from flatfile.views import View, ViewConfig

    View(
        id="us_vi_YOUR_ID",
        sheet_id="us_sh_YOUR_ID",
        name="My View",
        config=ViewConfig(
            filter="error",
            filter_field="email",
            q="firstname like %John%",
            sort_field="email",
            sort_direction="asc",
        ),
        created_by="us_usr_YOUR_ID",
    )
    """

    id: ViewId = pydantic.Field()
    """
    The ID of the view
    """

    sheet_id: typing_extensions.Annotated[SheetId, FieldMetadata(alias="sheetId")] = pydantic.Field()
    """
    The associated sheet ID of the view
    """

    name: str = pydantic.Field()
    """
    The name of the view
    """

    config: ViewConfig = pydantic.Field()
    """
    The view filters of the view
    """

    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy")] = pydantic.Field()
    """
    ID of the actor who created the view
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
