# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...commons.types.version_id import VersionId
from ...core.serialization import FieldMetadata
import pydantic
from ...commons.types.commit_id import CommitId
from ...commons.types.sort_field import SortField
from ...commons.types.sort_direction import SortDirection
from ...commons.types.filter import Filter
from ...commons.types.filter_field import FilterField
from ...commons.types.search_value import SearchValue
from ...commons.types.search_field import SearchField
from ...commons.types.record_id import RecordId
from ...commons.types.event_id import EventId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ViewConfig(UniversalBaseModel):
    """
    The configuration of a view. Filters, sorting, and search query.

    Examples
    --------
    from flatfile.views import ViewConfig

    ViewConfig(
        filter="error",
        filter_field="email",
        q="firstname like %John%",
        sort_field="email",
        sort_direction="asc",
    )
    """

    version_id: typing_extensions.Annotated[typing.Optional[VersionId], FieldMetadata(alias="versionId")] = (
        pydantic.Field(default=None)
    )
    """
    Deprecated, use `commitId` instead.
    """

    commit_id: typing_extensions.Annotated[typing.Optional[CommitId], FieldMetadata(alias="commitId")] = None
    since_version_id: typing_extensions.Annotated[typing.Optional[VersionId], FieldMetadata(alias="sinceVersionId")] = (
        pydantic.Field(default=None)
    )
    """
    Deprecated, use `sinceCommitId` instead.
    """

    since_commit_id: typing_extensions.Annotated[typing.Optional[CommitId], FieldMetadata(alias="sinceCommitId")] = None
    sort_field: typing_extensions.Annotated[typing.Optional[SortField], FieldMetadata(alias="sortField")] = None
    sort_direction: typing_extensions.Annotated[
        typing.Optional[SortDirection], FieldMetadata(alias="sortDirection")
    ] = None
    filter: typing.Optional[Filter] = None
    filter_field: typing_extensions.Annotated[typing.Optional[FilterField], FieldMetadata(alias="filterField")] = (
        pydantic.Field(default=None)
    )
    """
    Name of field by which to filter records
    """

    search_value: typing_extensions.Annotated[typing.Optional[SearchValue], FieldMetadata(alias="searchValue")] = None
    search_field: typing_extensions.Annotated[typing.Optional[SearchField], FieldMetadata(alias="searchField")] = None
    ids: typing.Optional[typing.List[RecordId]] = pydantic.Field(default=None)
    """
    The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' | 'error' | 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records. Maximum of 100 allowed.
    """

    page_size: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="pageSize")] = pydantic.Field(
        default=None
    )
    """
    Number of records to return in a page (default 10,000)
    """

    page_number: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="pageNumber")] = pydantic.Field(
        default=None
    )
    """
    Based on pageSize, which page of records to return (Note - numbers start at 1)
    """

    include_counts: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="includeCounts")] = (
        pydantic.Field(default=None)
    )
    """
    **DEPRECATED** Use GET /sheets/:sheetId/counts
    """

    include_length: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="includeLength")] = (
        pydantic.Field(default=None)
    )
    """
    The length of the record result set, returned as counts.total
    """

    include_links: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="includeLinks")] = (
        pydantic.Field(default=None)
    )
    """
    If true, linked records will be included in the results. Defaults to false.
    """

    include_messages: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="includeMessages")] = (
        pydantic.Field(default=None)
    )
    """
    Include error messages, defaults to false.
    """

    for_: typing_extensions.Annotated[typing.Optional[EventId], FieldMetadata(alias="for")] = pydantic.Field(
        default=None
    )
    """
    if "for" is provided, the query parameters will be pulled from the event payload
    """

    q: typing.Optional[str] = pydantic.Field(default=None)
    """
    An FFQL query used to filter the result set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
