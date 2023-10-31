# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commits.types.list_commits_response import ListCommitsResponse
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.errors import Errors
from ..commons.types.filter import Filter
from ..commons.types.filter_field import FilterField
from ..commons.types.record_id import RecordId
from ..commons.types.search_field import SearchField
from ..commons.types.search_value import SearchValue
from ..commons.types.sheet_id import SheetId
from ..commons.types.sort_direction import SortDirection
from ..commons.types.sort_field import SortField
from ..commons.types.success import Success
from ..commons.types.version_id import VersionId
from ..commons.types.workbook_id import WorkbookId
from ..property.types.property import Property
from .types.field_config_response import FieldConfigResponse
from .types.list_sheets_response import ListSheetsResponse
from .types.record_counts_response import RecordCountsResponse
from .types.sheet_response import SheetResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SheetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, workbook_id: WorkbookId) -> ListSheetsResponse:
        """
        Returns sheets in a workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "sheets"),
            params=remove_none_from_dict({"workbookId": workbook_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListSheetsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, sheet_id: SheetId) -> SheetResponse:
        """
        Returns a sheet in a workbook

        Parameters:
            - sheet_id: SheetId. ID of sheet
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SheetResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, sheet_id: SheetId) -> Success:
        """
        Deletes a specific sheet from a workbook

        Parameters:
            - sheet_id: SheetId. ID of sheet
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate(self, sheet_id: SheetId) -> Success:
        """
        Trigger data hooks and validation to run on a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/validate"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_records_as_csv(
        self,
        sheet_id: SheetId,
        *,
        version_id: typing.Optional[str] = None,
        since_version_id: typing.Optional[VersionId] = None,
        sort_field: typing.Optional[SortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[FilterField] = None,
        search_value: typing.Optional[SearchValue] = None,
        search_field: typing.Optional[SearchField] = None,
        ids: typing.Optional[typing.Union[RecordId, typing.List[RecordId]]] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns records from a sheet in a workbook as a csv file

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - version_id: typing.Optional[str].

            - since_version_id: typing.Optional[VersionId].

            - sort_field: typing.Optional[SortField].

            - sort_direction: typing.Optional[SortDirection]. Sort direction - asc (ascending) or desc (descending)

            - filter: typing.Optional[Filter]. Options to filter records

            - filter_field: typing.Optional[FilterField].

            - search_value: typing.Optional[SearchValue].

            - search_field: typing.Optional[SearchField].

            - ids: typing.Optional[typing.Union[RecordId, typing.List[RecordId]]]. The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' | 'error' | 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records

        """
        with self._client_wrapper.httpx_client.stream(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/download"),
            params=remove_none_from_dict(
                {
                    "versionId": version_id,
                    "sinceVersionId": since_version_id,
                    "sortField": sort_field,
                    "sortDirection": sort_direction,
                    "filter": filter,
                    "filterField": filter_field,
                    "searchValue": search_value,
                    "searchField": search_field,
                    "ids": ids,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_record_counts(
        self,
        sheet_id: SheetId,
        *,
        version_id: typing.Optional[str] = None,
        since_version_id: typing.Optional[VersionId] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[FilterField] = None,
        search_value: typing.Optional[SearchValue] = None,
        search_field: typing.Optional[SearchField] = None,
        by_field: typing.Optional[bool] = None,
        q: typing.Optional[str] = None,
    ) -> RecordCountsResponse:
        """
        Returns counts of records from a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - version_id: typing.Optional[str].

            - since_version_id: typing.Optional[VersionId].

            - filter: typing.Optional[Filter]. Options to filter records

            - filter_field: typing.Optional[FilterField].

            - search_value: typing.Optional[SearchValue].

            - search_field: typing.Optional[SearchField].

            - by_field: typing.Optional[bool]. If true, the error counts for each field will also be returned

            - q: typing.Optional[str]. An FFQL query used to filter the result set to be counted
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/counts"),
            params=remove_none_from_dict(
                {
                    "versionId": version_id,
                    "sinceVersionId": since_version_id,
                    "filter": filter,
                    "filterField": filter_field,
                    "searchValue": search_value,
                    "searchField": search_field,
                    "byField": by_field,
                    "q": q,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecordCountsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add_field(self, sheet_id: SheetId, *, request: Property) -> FieldConfigResponse:
        """
        Adds a new field to a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - request: Property.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/fields"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FieldConfigResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_sheet_commits(self, sheet_id: SheetId, *, completed: typing.Optional[bool] = None) -> ListCommitsResponse:
        """
        Returns the commit versions for a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - completed: typing.Optional[bool]. If true, only return commits that have been completed. If false, only return commits that have not been completed. If not provided, return all commits.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/commits"),
            params=remove_none_from_dict({"completed": completed}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListCommitsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSheetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, workbook_id: WorkbookId) -> ListSheetsResponse:
        """
        Returns sheets in a workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "sheets"),
            params=remove_none_from_dict({"workbookId": workbook_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListSheetsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, sheet_id: SheetId) -> SheetResponse:
        """
        Returns a sheet in a workbook

        Parameters:
            - sheet_id: SheetId. ID of sheet
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SheetResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, sheet_id: SheetId) -> Success:
        """
        Deletes a specific sheet from a workbook

        Parameters:
            - sheet_id: SheetId. ID of sheet
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate(self, sheet_id: SheetId) -> Success:
        """
        Trigger data hooks and validation to run on a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/validate"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_records_as_csv(
        self,
        sheet_id: SheetId,
        *,
        version_id: typing.Optional[str] = None,
        since_version_id: typing.Optional[VersionId] = None,
        sort_field: typing.Optional[SortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[FilterField] = None,
        search_value: typing.Optional[SearchValue] = None,
        search_field: typing.Optional[SearchField] = None,
        ids: typing.Optional[typing.Union[RecordId, typing.List[RecordId]]] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns records from a sheet in a workbook as a csv file

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - version_id: typing.Optional[str].

            - since_version_id: typing.Optional[VersionId].

            - sort_field: typing.Optional[SortField].

            - sort_direction: typing.Optional[SortDirection]. Sort direction - asc (ascending) or desc (descending)

            - filter: typing.Optional[Filter]. Options to filter records

            - filter_field: typing.Optional[FilterField].

            - search_value: typing.Optional[SearchValue].

            - search_field: typing.Optional[SearchField].

            - ids: typing.Optional[typing.Union[RecordId, typing.List[RecordId]]]. The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' | 'error' | 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records

        """
        async with self._client_wrapper.httpx_client.stream(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/download"),
            params=remove_none_from_dict(
                {
                    "versionId": version_id,
                    "sinceVersionId": since_version_id,
                    "sortField": sort_field,
                    "sortDirection": sort_direction,
                    "filter": filter,
                    "filterField": filter_field,
                    "searchValue": search_value,
                    "searchField": search_field,
                    "ids": ids,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_record_counts(
        self,
        sheet_id: SheetId,
        *,
        version_id: typing.Optional[str] = None,
        since_version_id: typing.Optional[VersionId] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[FilterField] = None,
        search_value: typing.Optional[SearchValue] = None,
        search_field: typing.Optional[SearchField] = None,
        by_field: typing.Optional[bool] = None,
        q: typing.Optional[str] = None,
    ) -> RecordCountsResponse:
        """
        Returns counts of records from a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - version_id: typing.Optional[str].

            - since_version_id: typing.Optional[VersionId].

            - filter: typing.Optional[Filter]. Options to filter records

            - filter_field: typing.Optional[FilterField].

            - search_value: typing.Optional[SearchValue].

            - search_field: typing.Optional[SearchField].

            - by_field: typing.Optional[bool]. If true, the error counts for each field will also be returned

            - q: typing.Optional[str]. An FFQL query used to filter the result set to be counted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/counts"),
            params=remove_none_from_dict(
                {
                    "versionId": version_id,
                    "sinceVersionId": since_version_id,
                    "filter": filter,
                    "filterField": filter_field,
                    "searchValue": search_value,
                    "searchField": search_field,
                    "byField": by_field,
                    "q": q,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecordCountsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add_field(self, sheet_id: SheetId, *, request: Property) -> FieldConfigResponse:
        """
        Adds a new field to a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - request: Property.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/fields"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FieldConfigResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_sheet_commits(
        self, sheet_id: SheetId, *, completed: typing.Optional[bool] = None
    ) -> ListCommitsResponse:
        """
        Returns the commit versions for a sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - completed: typing.Optional[bool]. If true, only return commits that have been completed. If false, only return commits that have not been completed. If not provided, return all commits.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/commits"),
            params=remove_none_from_dict({"completed": completed}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListCommitsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
