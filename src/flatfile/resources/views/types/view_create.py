# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.sheet_id import SheetId
from .view_config import ViewConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ViewCreate(pydantic.BaseModel):
    """
    from flatfile import Filter, SortDirection, ViewConfig, ViewCreate

    ViewCreate(
        sheet_id="us_sh_YOUR_ID",
        name="My View",
        config=ViewConfig(
            filter=Filter.ERROR,
            filter_field="email",
            q="firstname like %John%",
            sort_field="email",
            sort_direction=SortDirection.ASC,
        ),
    )
    """

    sheet_id: SheetId = pydantic.Field(alias="sheetId")
    name: str
    config: ViewConfig

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
