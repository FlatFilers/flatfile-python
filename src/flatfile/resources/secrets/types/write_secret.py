# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.environment_id import EnvironmentId
from ...commons.types.space_id import SpaceId
from .secret_name import SecretName
from .secret_value import SecretValue


class WriteSecret(pydantic.BaseModel):
    """
    The properties required to write to a secret. Value is the only mutable property. Name, environmentId, spaceId (optional) are used for finding the secret.
    """

    name: SecretName
    value: SecretValue
    environment_id: EnvironmentId = pydantic.Field(alias="environmentId")
    space_id: typing.Optional[SpaceId] = pydantic.Field(alias="spaceId")

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
