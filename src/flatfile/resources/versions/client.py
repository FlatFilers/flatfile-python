# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ..commons.types.sheet_id import SheetId
from ..commons.types.version_id import VersionId
from .types.version_response import VersionResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_id(
        self, *, sheet_id: typing.Optional[SheetId] = OMIT, parent_version_id: typing.Optional[VersionId] = OMIT
    ) -> VersionResponse:
        """
        Creates a new version id that can be used to group record updates

        Parameters:
            - sheet_id: typing.Optional[SheetId].

            - parent_version_id: typing.Optional[VersionId].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if sheet_id is not OMIT:
            _request["sheetId"] = sheet_id
        if parent_version_id is not OMIT:
            _request["parentVersionId"] = parent_version_id
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "versions"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(VersionResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_id(
        self, *, sheet_id: typing.Optional[SheetId] = OMIT, parent_version_id: typing.Optional[VersionId] = OMIT
    ) -> VersionResponse:
        """
        Creates a new version id that can be used to group record updates

        Parameters:
            - sheet_id: typing.Optional[SheetId].

            - parent_version_id: typing.Optional[VersionId].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if sheet_id is not OMIT:
            _request["sheetId"] = sheet_id
        if parent_version_id is not OMIT:
            _request["parentVersionId"] = parent_version_id
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "versions"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(VersionResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
