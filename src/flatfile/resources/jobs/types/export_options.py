# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.commit_id import CommitId
from ...commons.types.filter import Filter
from ...commons.types.filter_field import FilterField
from ...commons.types.record_id import RecordId
from ...commons.types.search_field import SearchField
from ...commons.types.search_value import SearchValue
from ...commons.types.sort_direction import SortDirection
from ...commons.types.sort_field import SortField
from ...commons.types.version_id import VersionId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ExportOptions(pydantic.BaseModel):
    version_id: typing.Optional[VersionId] = pydantic.Field(
        alias="versionId", default=None, description="Deprecated, use `commitId` instead"
    )
    commit_id: typing.Optional[CommitId] = pydantic.Field(
        alias="commitId",
        default=None,
        description="If provided, the snapshot version of the workbook will be used for the export",
    )
    sort_field: typing.Optional[SortField] = pydantic.Field(
        alias="sortField", default=None, description="The field to sort the records on"
    )
    sort_direction: typing.Optional[SortDirection] = pydantic.Field(
        alias="sortDirection", default=None, description="The direction to sort the records"
    )
    filter: typing.Optional[Filter] = pydantic.Field(default=None, description="The filter to apply to the records")
    filter_field: typing.Optional[FilterField] = pydantic.Field(
        alias="filterField", default=None, description="The field to filter on"
    )
    search_value: typing.Optional[SearchValue] = pydantic.Field(
        alias="searchValue", default=None, description="The value to search for"
    )
    search_field: typing.Optional[SearchField] = pydantic.Field(
        alias="searchField", default=None, description="The field to search for the search value in"
    )
    q: typing.Optional[str] = pydantic.Field(default=None, description="The FFQL query to filter records")
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
