# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.actor_role_id import ActorRoleId
from ...commons.types.role_id import RoleId
from .actor_id_union import ActorIdUnion
from .resource_id_union import ResourceIdUnion

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ActorRoleResponse(pydantic.BaseModel):
    id: ActorRoleId
    role_id: RoleId = pydantic.Field(alias="roleId")
    actor_id: ActorIdUnion = pydantic.Field(alias="actorId")
    resource_id: ResourceIdUnion = pydantic.Field(alias="resourceId")
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}