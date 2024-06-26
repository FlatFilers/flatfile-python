# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.json_path_string import JsonPathString
from .validation_source import ValidationSource
from .validation_type import ValidationType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ValidationMessage(pydantic.BaseModel):
    """
    Record data validation messages
    """

    field: typing.Optional[str] = None
    type: typing.Optional[ValidationType] = None
    source: typing.Optional[ValidationSource] = None
    message: typing.Optional[str] = None
    path: typing.Optional[JsonPathString] = pydantic.Field(
        default=None, description="This JSONPath is based on the root of mapped cell object."
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
        json_encoders = {dt.datetime: serialize_datetime}
