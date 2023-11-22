# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.types.filter import Filter
from ..commons.types.filter_field import FilterField
from ..commons.types.page_number import PageNumber
from ..commons.types.page_size import PageSize
from ..commons.types.search_value import SearchValue
from ..commons.types.sheet_id import SheetId
from ..commons.types.sort_direction import SortDirection
from ..commons.types.sort_field import SortField
from .types.cells_response import CellsResponse
from .types.distinct import Distinct
from .types.field_key import FieldKey
from .types.include_counts import IncludeCounts

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CellsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_values(
        self,
        sheet_id: SheetId,
        *,
        field_key: typing.Optional[FieldKey] = None,
        sort_field: typing.Optional[SortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[FilterField] = None,
        page_size: typing.Optional[PageSize] = None,
        page_number: typing.Optional[PageNumber] = None,
        distinct: typing.Optional[Distinct] = None,
        include_counts: typing.Optional[IncludeCounts] = None,
        search_value: typing.Optional[SearchValue] = None,
    ) -> CellsResponse:
        """
        Returns record cell values grouped by all fields in the sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - field_key: typing.Optional[FieldKey].

            - sort_field: typing.Optional[SortField].

            - sort_direction: typing.Optional[SortDirection].

            - filter: typing.Optional[Filter].

            - filter_field: typing.Optional[FilterField]. Name of field by which to filter records

            - page_size: typing.Optional[PageSize]. Number of records to return in a page (default 1000 if pageNumber included)

            - page_number: typing.Optional[PageNumber]. Based on pageSize, which page of records to return

            - distinct: typing.Optional[Distinct].

            - include_counts: typing.Optional[IncludeCounts].

            - search_value: typing.Optional[SearchValue]. A value to find for a given field in a sheet. Wrap the value in "" for exact match
        ---
        from flatfile import Filter, SortDirection
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.get_values(
            sheet_id="us_sh_YOUR_ID",
            field_key="firstName",
            sort_field="firstName",
            sort_direction=SortDirection.ASC,
            filter=Filter.VALID,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/cells"),
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
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_values(
        self,
        sheet_id: SheetId,
        *,
        field_key: typing.Optional[FieldKey] = None,
        sort_field: typing.Optional[SortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filter: typing.Optional[Filter] = None,
        filter_field: typing.Optional[FilterField] = None,
        page_size: typing.Optional[PageSize] = None,
        page_number: typing.Optional[PageNumber] = None,
        distinct: typing.Optional[Distinct] = None,
        include_counts: typing.Optional[IncludeCounts] = None,
        search_value: typing.Optional[SearchValue] = None,
    ) -> CellsResponse:
        """
        Returns record cell values grouped by all fields in the sheet

        Parameters:
            - sheet_id: SheetId. ID of sheet

            - field_key: typing.Optional[FieldKey].

            - sort_field: typing.Optional[SortField].

            - sort_direction: typing.Optional[SortDirection].

            - filter: typing.Optional[Filter].

            - filter_field: typing.Optional[FilterField]. Name of field by which to filter records

            - page_size: typing.Optional[PageSize]. Number of records to return in a page (default 1000 if pageNumber included)

            - page_number: typing.Optional[PageNumber]. Based on pageSize, which page of records to return

            - distinct: typing.Optional[Distinct].

            - include_counts: typing.Optional[IncludeCounts].

            - search_value: typing.Optional[SearchValue]. A value to find for a given field in a sheet. Wrap the value in "" for exact match
        ---
        from flatfile import Filter, SortDirection
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.get_values(
            sheet_id="us_sh_YOUR_ID",
            field_key="firstName",
            sort_field="firstName",
            sort_direction=SortDirection.ASC,
            filter=Filter.VALID,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sheets/{sheet_id}/cells"),
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
