# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .arrayable_property import ArrayableProperty
from .base_property import BaseProperty
from .enum_property_config import EnumPropertyConfig


class EnumProperty(BaseProperty, ArrayableProperty):
    """
    Defines an enumerated list of options for the user to select from. Matching tooling attempts to resolve incoming data assigment to a valid option. The maximum number of options for this list is `100`. For larger lists, users should use the reference or future `lookup` types.
    """

    multi: typing.Optional[bool] = pydantic.Field(
        description="Will allow multiple values and store / provide the values in an array if set. Not all field types support arrays."
    )
    config: EnumPropertyConfig

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
