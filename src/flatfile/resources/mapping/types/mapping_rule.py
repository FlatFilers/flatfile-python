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


class MappingRule(MappingRuleConfig):
    """
    import datetime

    from flatfile import MappingRule

    MappingRule(
        id="mapping-rule-id",
        name="Assign mapping rule",
        type="assign",
        config={},
        confidence=1,
        created_by="us_usr_YOUR_ID",
        created_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
    )
    """

    id: MappingId = pydantic.Field(description="ID of the mapping rule")
    confidence: typing.Optional[int] = pydantic.Field(description="Confidence of the mapping rule")
    created_by: typing.Optional[UserId] = pydantic.Field(
        alias="createdBy", description="User ID of the user who suggested the mapping rule"
    )
    created_at: dt.datetime = pydantic.Field(alias="createdAt", description="Time the mapping rule was created")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt", description="Time the mapping rule was last updated")
    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="deletedAt", description="Time the mapping rule was deleted"
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
