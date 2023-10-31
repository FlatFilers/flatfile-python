# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .reference_property_relationship import ReferencePropertyRelationship

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ReferencePropertyConfig(pydantic.BaseModel):
    ref: str = pydantic.Field(description="Full path reference to a sheet configuration. Must be in the same workbook.")
    key: str = pydantic.Field(description="Key of the property to use as the reference key. Defaults to `id`")
    relationship: ReferencePropertyRelationship = pydantic.Field(description="The type of relationship this defines")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
