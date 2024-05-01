# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.sheet_id import SheetId
from ...commons.types.view_id import ViewId
from .view_config import ViewConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class View(pydantic.BaseModel):
    """
    A view
    ---
    from flatfile import Filter, SortDirection, View, ViewConfig

    View(
        id="us_vi_YOUR_ID",
        sheet_id="us_sh_YOUR_ID",
        name="My View",
        config=ViewConfig(
            filter=Filter.ERROR,
            filter_field="email",
            q="firstname like %John%",
            sort_field="email",
            sort_direction=SortDirection.ASC,
        ),
        created_by="us_usr_YOUR_ID",
    )
    """

    id: ViewId = pydantic.Field(description="The ID of the view")
    sheet_id: SheetId = pydantic.Field(alias="sheetId", description="The associated sheet ID of the view")
    name: str = pydantic.Field(description="The name of the view")
    config: ViewConfig = pydantic.Field(description="The view filters of the view")
    created_by: str = pydantic.Field(alias="createdBy", description="ID of the actor who created the view")

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
