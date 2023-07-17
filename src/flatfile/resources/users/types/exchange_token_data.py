# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class ExchangeTokenData(pydantic.BaseModel):
    valid: bool = pydantic.Field(description="Whether the provided token was valid")
    token: typing.Optional[str] = pydantic.Field(description="The refreshed token, if the provided token was valid")
    sent_to: typing.Optional[str] = pydantic.Field(
        alias="sentTo",
        description="The email address the recovery email was sent to, if the provided token was not valid",
    )

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
