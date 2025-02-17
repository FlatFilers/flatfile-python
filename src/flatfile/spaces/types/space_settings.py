# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .space_sidebar_config import SpaceSidebarConfig
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class SpaceSettings(UniversalBaseModel):
    """
    Settings for a space
    """

    sidebar_config: typing_extensions.Annotated[
        typing.Optional[SpaceSidebarConfig], FieldMetadata(alias="sidebarConfig")
    ] = pydantic.Field(default=None)
    """
    The sidebar configuration for the space. (This will eventually replace metadata.sidebarconfig)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
