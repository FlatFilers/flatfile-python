# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...environments.types.guest_authentication_enum import GuestAuthenticationEnum
from .internal_space_config_base import InternalSpaceConfigBase

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SpaceConfig(InternalSpaceConfigBase):
    """
    Properties used to create a new Space
    """

    name: typing.Optional[str] = pydantic.Field(description="The name of the space")
    display_order: typing.Optional[int] = pydantic.Field(alias="displayOrder", description="The display order")
    guest_authentication: typing.Optional[typing.List[GuestAuthenticationEnum]] = pydantic.Field(
        alias="guestAuthentication"
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
