# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.action import Action
from ...commons.types.app_id import AppId
from ...commons.types.environment_id import EnvironmentId
from ...commons.types.space_config_id import SpaceConfigId
from ...commons.types.workbook_id import WorkbookId
from .space_access import SpaceAccess
from .space_settings import SpaceSettings

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InternalSpaceConfigBase(pydantic.BaseModel):
    space_config_id: typing.Optional[SpaceConfigId] = pydantic.Field(alias="spaceConfigId", default=None)
    environment_id: typing.Optional[EnvironmentId] = pydantic.Field(alias="environmentId", default=None)
    primary_workbook_id: typing.Optional[WorkbookId] = pydantic.Field(
        alias="primaryWorkbookId",
        default=None,
        description="The ID of the primary workbook for the space. This should not be included in create space requests.",
    )
    metadata: typing.Optional[typing.Any] = pydantic.Field(default=None, description="Metadata for the space")
    settings: typing.Optional[SpaceSettings] = pydantic.Field(default=None, description="The Space settings.")
    actions: typing.Optional[typing.List[Action]] = None
    access: typing.Optional[typing.List[SpaceAccess]] = None
    auto_configure: typing.Optional[bool] = pydantic.Field(alias="autoConfigure", default=None)
    namespace: typing.Optional[str] = None
    labels: typing.Optional[typing.List[str]] = None
    translations_path: typing.Optional[str] = pydantic.Field(alias="translationsPath", default=None)
    language_override: typing.Optional[str] = pydantic.Field(alias="languageOverride", default=None)
    archived_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="archivedAt", default=None, description="Date when space was archived"
    )
    app_id: typing.Optional[AppId] = pydantic.Field(
        alias="appId", default=None, description="The ID of the App that space is associated with"
    )
    is_app_template: typing.Optional[bool] = pydantic.Field(
        alias="isAppTemplate",
        default=None,
        description="Whether the space is an app template. Only one space per app can be an app template.",
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
