# This file was auto-generated by Fern from our API Definition.

from .action import Action
from .action_id import ActionId
import typing_extensions
from ...core.serialization import FieldMetadata
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ApiAction(Action):
    id: ActionId
    target_id: typing_extensions.Annotated[str, FieldMetadata(alias="targetId")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
