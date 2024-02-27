# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .arrayable_property import ArrayableProperty
from .base_property import BaseProperty
from .number_config import NumberConfig


class NumberProperty(BaseProperty, ArrayableProperty):
    """
    Defines a property that should be stored and read as either an integer or floating point number. Database engines should look at the configuration to determine ideal storage format.
    """

    config: typing.Optional[NumberConfig] = None

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
