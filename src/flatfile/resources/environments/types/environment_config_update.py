# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .guest_authentication_enum import GuestAuthenticationEnum

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EnvironmentConfigUpdate(pydantic.BaseModel):
    """
    Properties used to update an environment
    ---
    from flatfile import EnvironmentConfigUpdate, GuestAuthenticationEnum

    EnvironmentConfigUpdate(
        name="dev",
        is_prod=False,
        guest_authentication=[GuestAuthenticationEnum.MAGIC_LINK],
        metadata={"key": "value"},
        namespaces=["default"],
    )
    """

    name: typing.Optional[str] = pydantic.Field(default=None, description="The name of the environment")
    is_prod: typing.Optional[bool] = pydantic.Field(
        alias="isProd", default=None, description="Whether or not the environment is a production environment"
    )
    guest_authentication: typing.Optional[typing.List[GuestAuthenticationEnum]] = pydantic.Field(
        alias="guestAuthentication", default=None
    )
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    translations_path: typing.Optional[str] = pydantic.Field(alias="translationsPath", default=None)
    namespaces: typing.Optional[typing.List[str]] = None
    language_override: typing.Optional[str] = pydantic.Field(alias="languageOverride", default=None)

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
