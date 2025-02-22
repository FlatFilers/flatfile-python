# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...commons.types.space_id import SpaceId
from ...core.serialization import FieldMetadata
from ...commons.types.app_id import AppId
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class AiGenerateSampleDataJobConfig(UniversalBaseModel):
    space_id: typing_extensions.Annotated[SpaceId, FieldMetadata(alias="spaceId")]
    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
