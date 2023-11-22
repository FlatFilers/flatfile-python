# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.account_id import AccountId
from ...commons.types.environment_id import EnvironmentId
from .api_key_id import ApiKeyId
from .api_key_operation import ApiKeyOperation
from .api_key_type import ApiKeyType
from .raw_key import RawKey

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ApiKey(pydantic.BaseModel):
    """
    API Key used for authenticating against our APIs
    ---
    import datetime

    from flatfile import ApiKey, ApiKeyOperation, ApiKeyType

    ApiKey(
        id="us_key_YOUR_ID",
        raw_key="pk_YOUR_RAW_API_KEY",
        type=ApiKeyType.PUBLISHABLE,
        environment_id="us_env_YOUR_ID",
        account_id="us_acc_YOUR_ID",
        operations=[
            ApiKeyOperation(
                path="/v1/spaces",
                method="POST",
            )
        ],
        created_at=datetime.datetime.fromisoformat(
            "2017-07-21 17:32:28+00:00",
        ),
    )
    """

    id: ApiKeyId
    raw_key: typing.Optional[RawKey] = pydantic.Field(alias="rawKey")
    type: ApiKeyType
    environment_id: typing.Optional[EnvironmentId] = pydantic.Field(alias="environmentId")
    account_id: typing.Optional[AccountId] = pydantic.Field(alias="accountId")
    operations: typing.List[ApiKeyOperation]
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(alias="updatedAt")
    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(alias="deletedAt")
    secret: typing.Optional[str]

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
