# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.family_id import FamilyId
from ...commons.types.user_id import UserId
from .mapping_rule_or_config import MappingRuleOrConfig
from .program_summary import ProgramSummary

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Program(pydantic.BaseModel):
    rules: typing.List[MappingRuleOrConfig] = pydantic.Field(description="Mapping rules")
    id: typing.Optional[str] = pydantic.Field(
        default=None, description="If this program was saved, this is the ID of the program"
    )
    namespace: typing.Optional[str] = pydantic.Field(default=None, description="Namespace of the program")
    family_id: typing.Optional[FamilyId] = pydantic.Field(
        alias="familyId", default=None, description="Family ID of the program, if it belongs to a family"
    )
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="createdAt", default=None, description="If this program was saved, this is the time it was created"
    )
    created_by: typing.Optional[UserId] = pydantic.Field(
        alias="createdBy", default=None, description="If this program was saved, this is the user ID of the creator"
    )
    source_keys: typing.List[str] = pydantic.Field(alias="sourceKeys", description="Source keys")
    destination_keys: typing.List[str] = pydantic.Field(alias="destinationKeys", description="Destination keys")
    summary: typing.Optional[ProgramSummary] = pydantic.Field(default=None, description="Summary of the mapping rules")
    access_token: typing.Optional[str] = pydantic.Field(
        alias="accessToken",
        default=None,
        description="If this program was saved, this token allows you to modify the program",
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
