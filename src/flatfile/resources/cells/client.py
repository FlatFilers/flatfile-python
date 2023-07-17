# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ...environment import FlatfileEnvironment
from ..commons.types.filter import Filter
from ..commons.types.sheet_id import SheetId
from ..commons.types.sort_direction import SortDirection
from ..commons.types.sort_field import SortField
from .types.cells_response import CellsResponse


class CellsClient:
    def __init__(
        self, *, environment: FlatfileEnvironment = FlatfileEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def get_values(
        self,
        sheet_id: SheetId,
        *,
        field_key: str,
        sort_field: typing.Optional[SortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        distinct: typing.Optional[bool] = None,
        include_counts: typing.Optional[bool] = None,
        search_value: typing.Optional[str] = None,
    ) -> CellsResponse:
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"sheets/{sheet_id}/cells"),
            params=remove_none_from_dict(
                {
                    "fieldKey": field_key,
                    "sortField": sort_field,
                    "sortDirection": sort_direction,
                    "filter": filter,
                    "filterField": filter_field,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                    "distinct": distinct,
                    "includeCounts": include_counts,
                    "searchValue": search_value,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CellsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCellsClient:
    def __init__(
        self, *, environment: FlatfileEnvironment = FlatfileEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def get_values(
        self,
        sheet_id: SheetId,
        *,
        field_key: str,
        sort_field: typing.Optional[SortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        distinct: typing.Optional[bool] = None,
        include_counts: typing.Optional[bool] = None,
        search_value: typing.Optional[str] = None,
    ) -> CellsResponse:
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"sheets/{sheet_id}/cells"),
            params=remove_none_from_dict(
                {
                    "fieldKey": field_key,
                    "sortField": sort_field,
                    "sortDirection": sort_direction,
                    "filter": filter,
                    "filterField": filter_field,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                    "distinct": distinct,
                    "includeCounts": include_counts,
                    "searchValue": search_value,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CellsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
