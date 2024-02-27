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


class MutateJobConfig(pydantic.BaseModel):
    sheet_id: SheetId = pydantic.Field(alias="sheetId")
    mutate_record: str = pydantic.Field(
        alias="mutateRecord",
        description="A JavaScript function that will be run on each record in the sheet, it should return a mutated record.",
    )
    mutation_id: typing.Optional[str] = pydantic.Field(
        alias="mutationId",
        default=None,
        description="If the mutation was generated through some sort of id-ed process, this links this job and that process.",
    )
    filter: typing.Optional[Filter] = None
    filter_field: typing.Optional[FilterField] = pydantic.Field(alias="filterField", default=None)
    search_value: typing.Optional[SearchValue] = pydantic.Field(alias="searchValue", default=None)
    search_field: typing.Optional[SearchField] = pydantic.Field(alias="searchField", default=None)
    q: typing.Optional[str] = None
    ids: typing.Optional[typing.List[RecordId]] = pydantic.Field(
        default=None,
        description=(
            "The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' \n"
            " 'error' \n"
            " 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records\n"
        ),
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
