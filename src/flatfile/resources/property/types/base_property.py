# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .constraint import Constraint

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BaseProperty(pydantic.BaseModel):
    key: str
    label: typing.Optional[str] = pydantic.Field(description="User friendly field name")
    description: typing.Optional[str]
    constraints: typing.Optional[typing.List[Constraint]]
    readonly: typing.Optional[bool]
    metadata: typing.Optional[typing.Any] = pydantic.Field(
        description="Useful for any contextual metadata regarding the schema. Store any valid json here."
    )
    treatments: typing.Optional[typing.List[str]]
    alternative_names: typing.Optional[typing.List[str]] = pydantic.Field(alias="alternativeNames")

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
