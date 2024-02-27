# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.app_id import AppId
from .app_type import AppType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class App(pydantic.BaseModel):
    """
    An app
    ---
    import datetime

    from flatfile import App, AppType

    App(id="us_app_YOUR_ID", name="Nightly Data Loads", namespace="nightly-data", type=AppType.CUSTOM, entity="Sync", entity_plural="Syncs", icon='<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 16">
      <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1z"/>
    </svg>', metadata={"foo": "bar"}, created_at=datetime.datetime.fromisoformat("2023-10-30 16:59:45.735000+00:00", ), updated_at=datetime.datetime.fromisoformat("2023-10-30 16:59:45.735000+00:00", ), )
    """

    id: AppId
    name: str
    namespace: str
    type: AppType
    entity: str
    entity_plural: str = pydantic.Field(alias="entityPlural")
    icon: typing.Optional[str] = None
    metadata: typing.Any
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(alias="deletedAt", default=None)
    activated_at: typing.Optional[dt.datetime] = pydantic.Field(alias="activatedAt", default=None)

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
