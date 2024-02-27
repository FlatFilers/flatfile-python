# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .cell_value_union import CellValueUnion
from .validation_message import ValidationMessage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CellValue(pydantic.BaseModel):
    valid: typing.Optional[bool] = None
    messages: typing.Optional[typing.List[ValidationMessage]] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    value: typing.Optional[CellValueUnion] = None
    layer: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(alias="updatedAt", default=None)

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
