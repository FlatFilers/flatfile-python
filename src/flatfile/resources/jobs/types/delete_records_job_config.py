# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.filter import Filter
from ...commons.types.filter_field import FilterField
from ...commons.types.record_id import RecordId
from ...commons.types.search_field import SearchField
from ...commons.types.search_value import SearchValue
from ...commons.types.sheet_id import SheetId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DeleteRecordsJobConfig(pydantic.BaseModel):
    """
    The configuration for a delete job
    """

    filter: typing.Optional[Filter]
    filter_field: typing.Optional[FilterField] = pydantic.Field(alias="filterField")
    search_value: typing.Optional[SearchValue] = pydantic.Field(alias="searchValue")
    search_field: typing.Optional[SearchField] = pydantic.Field(alias="searchField")
    q: typing.Optional[str] = pydantic.Field(description="FFQL query to filter records")
    sheet: SheetId
    exceptions: typing.Optional[typing.List[RecordId]] = pydantic.Field(
        description="List of record ids to exclude from deletion"
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
