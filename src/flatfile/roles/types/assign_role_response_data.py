# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...commons.types.actor_role_id import ActorRoleId
import typing_extensions
from ...commons.types.role_id import RoleId
from ...core.serialization import FieldMetadata
from ...commons.types.actor_id_union import ActorIdUnion
from .resource_id_union import ResourceIdUnion
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class AssignRoleResponseData(UniversalBaseModel):
    id: ActorRoleId
    role_id: typing_extensions.Annotated[RoleId, FieldMetadata(alias="roleId")]
    actor_id: typing_extensions.Annotated[ActorIdUnion, FieldMetadata(alias="actorId")]
    resource_id: typing_extensions.Annotated[ResourceIdUnion, FieldMetadata(alias="resourceId")]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
