# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.user_id import UserId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MappingRuleConfig(pydantic.BaseModel):
    """
    from flatfile import MappingRuleConfig

    MappingRuleConfig(
        name="Assign mapping rule",
        type="assign",
        config={},
        metadata={},
    )
    """

    name: str = pydantic.Field(description="Name of the mapping rule")
    type: str
    config: typing.Optional[typing.Any] = None
    accepted_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="acceptedAt", default=None, description="Time the mapping rule was last updated"
    )
    accepted_by: typing.Optional[UserId] = pydantic.Field(
        alias="acceptedBy", default=None, description="User ID of the contributor of the mapping rule"
    )
    metadata: typing.Optional[typing.Any] = pydantic.Field(default=None, description="Metadata of the mapping rule")

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
