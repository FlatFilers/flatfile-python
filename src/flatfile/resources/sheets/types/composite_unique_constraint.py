# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .composite_unique_constraint_strategy import CompositeUniqueConstraintStrategy

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CompositeUniqueConstraint(pydantic.BaseModel):
    name: str = pydantic.Field(description="The name of the constraint")
    fields: typing.List[str] = pydantic.Field(description="The fields that must be unique together")
    required_fields: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="requiredFields",
        default=None,
        description="Fields that, when empty, will cause this unique constraint to be ignored",
    )
    strategy: CompositeUniqueConstraintStrategy

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
