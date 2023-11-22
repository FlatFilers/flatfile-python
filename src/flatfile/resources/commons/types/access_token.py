# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .account_id import AccountId
from .user_id import UserId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AccessToken(pydantic.BaseModel):
    """
    Properties used to allow users to request our private services
    ---
    from flatfile import AccessToken

    AccessToken(
        access_token="eyJhbGciO_VERY_LONG_TOKEN_STRING",
        expires_in="86400",
        expires="2022-09-18T00:19:57.007Z",
        email="yourEmail@example.com",
        user_id="UserId.Example0",
        account_id="AccountId.Example0",
    )
    """

    access_token: str = pydantic.Field(alias="accessToken")
    expires_in: str = pydantic.Field(alias="expiresIn")
    expires: str
    email: typing.Optional[str]
    user_id: typing.Optional[UserId] = pydantic.Field(alias="userId")
    account_id: typing.Optional[AccountId] = pydantic.Field(alias="accountId")

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