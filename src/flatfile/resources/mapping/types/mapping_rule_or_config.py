# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.mapping_id import MappingId
from ...commons.types.user_id import UserId
from .mapping_rule_config import MappingRuleConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MappingRuleOrConfig(MappingRuleConfig):
    id: typing.Optional[MappingId] = pydantic.Field(default=None, description="ID of the mapping rule")
    confidence: typing.Optional[int] = pydantic.Field(default=None, description="Confidence of the mapping rule")
    created_by: typing.Optional[UserId] = pydantic.Field(
        alias="createdBy", default=None, description="User ID of the creator of the mapping rule"
    )
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="createdAt", default=None, description="Time the mapping rule was created"
    )
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="updatedAt", default=None, description="Time the mapping rule was last updated"
    )
    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="deletedAt", default=None, description="Time the mapping rule was deleted"
    )

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