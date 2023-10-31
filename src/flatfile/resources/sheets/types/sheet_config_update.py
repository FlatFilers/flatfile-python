# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.action import Action
from ...property.types.property import Property
from .sheet_access import SheetAccess

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SheetConfigUpdate(pydantic.BaseModel):
    """
    Changes to make to an existing sheet config
    """

    name: typing.Optional[str]
    description: typing.Optional[str]
    slug: typing.Optional[str]
    readonly: typing.Optional[bool]
    allow_additional_fields: typing.Optional[bool] = pydantic.Field(alias="allowAdditionalFields")
    access: typing.Optional[typing.List[SheetAccess]]
    fields: typing.Optional[typing.List[Property]]
    actions: typing.Optional[typing.List[Action]]

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
