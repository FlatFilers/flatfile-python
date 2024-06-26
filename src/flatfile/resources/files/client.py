# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ... import core
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.action import Action
from ..commons.types.environment_id import EnvironmentId
from ..commons.types.errors import Errors
from ..commons.types.file_id import FileId
from ..commons.types.space_id import SpaceId
from ..commons.types.success import Success
from ..commons.types.workbook_id import WorkbookId
from .types.file_origin import FileOrigin
from .types.file_response import FileResponse
from .types.list_files_response import ListFilesResponse
from .types.mode import Mode
from .types.model_file_status_enum import ModelFileStatusEnum

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        space_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        mode: typing.Optional[Mode] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFilesResponse:
        """
        Parameters:
            - space_id: typing.Optional[str].

            - page_size: typing.Optional[int]. Number of files to return in a page (default 20)

            - page_number: typing.Optional[int]. Based on pageSize, which page of files to return

            - mode: typing.Optional[Mode]. The storage mode of file to fetch, defaults to "import"

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.files.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "spaceId": space_id,
                        "pageSize": page_size,
                        "pageNumber": page_number,
                        "mode": mode,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListFilesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upload(
        self,
        *,
        space_id: SpaceId,
        environment_id: EnvironmentId,
        mode: typing.Optional[Mode] = None,
        file: core.File,
        actions: typing.Optional[typing.List[Action]] = None,
        origin: typing.Optional[FileOrigin] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileResponse:
        """
        Parameters:
            - space_id: SpaceId.

            - environment_id: EnvironmentId.

            - mode: typing.Optional[Mode]. The storage mode of file to insert, defaults to "import"

            - file: core.File. See core.File for more documentation

            - actions: typing.Optional[typing.List[Action]]. The actions attached to the file

            - origin: typing.Optional[FileOrigin]. The origin of the file, ie filesystem

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "spaceId": space_id,
                        "environmentId": environment_id,
                        "mode": mode,
                        "actions": actions,
                        "origin": origin,
                    }
                )
            )
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "spaceId": space_id,
                            "environmentId": environment_id,
                            "mode": mode,
                            "actions": actions,
                            "origin": origin,
                        }
                    )
                ),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"file": file})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FileResponse:
        """
        Parameters:
            - file_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.files.get(
            file_id="us_fl_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Parameters:
            - file_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
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

    def update(
        self,
        file_id: str,
        *,
        workbook_id: typing.Optional[WorkbookId] = OMIT,
        name: typing.Optional[str] = OMIT,
        mode: typing.Optional[Mode] = OMIT,
        status: typing.Optional[ModelFileStatusEnum] = OMIT,
        actions: typing.Optional[typing.Sequence[Action]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileResponse:
        """
        Update a file, to change the workbook id for example

        Parameters:
            - file_id: str. ID of file to update

            - workbook_id: typing.Optional[WorkbookId].

            - name: typing.Optional[str]. The name of the file

            - mode: typing.Optional[Mode]. The storage mode of file to update

            - status: typing.Optional[ModelFileStatusEnum]. Status of the file

            - actions: typing.Optional[typing.Sequence[Action]]. The actions attached to the file

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.files.update(
            file_id="us_fl_YOUR_ID",
            name="NewFileName",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if workbook_id is not OMIT:
            _request["workbookId"] = workbook_id
        if name is not OMIT:
            _request["name"] = name
        if mode is not OMIT:
            _request["mode"] = mode.value if mode is not None else None
        if status is not OMIT:
            _request["status"] = status.value if status is not None else None
        if actions is not OMIT:
            _request["actions"] = actions
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def download(
        self, file_id: FileId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters:
            - file_id: FileId.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        with self._client_wrapper.httpx_client.stream(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}/download"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            if _response.status_code == 400:
                raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        space_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        mode: typing.Optional[Mode] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFilesResponse:
        """
        Parameters:
            - space_id: typing.Optional[str].

            - page_size: typing.Optional[int]. Number of files to return in a page (default 20)

            - page_number: typing.Optional[int]. Based on pageSize, which page of files to return

            - mode: typing.Optional[Mode]. The storage mode of file to fetch, defaults to "import"

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.files.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "spaceId": space_id,
                        "pageSize": page_size,
                        "pageNumber": page_number,
                        "mode": mode,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListFilesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upload(
        self,
        *,
        space_id: SpaceId,
        environment_id: EnvironmentId,
        mode: typing.Optional[Mode] = None,
        file: core.File,
        actions: typing.Optional[typing.List[Action]] = None,
        origin: typing.Optional[FileOrigin] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileResponse:
        """
        Parameters:
            - space_id: SpaceId.

            - environment_id: EnvironmentId.

            - mode: typing.Optional[Mode]. The storage mode of file to insert, defaults to "import"

            - file: core.File. See core.File for more documentation

            - actions: typing.Optional[typing.List[Action]]. The actions attached to the file

            - origin: typing.Optional[FileOrigin]. The origin of the file, ie filesystem

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "spaceId": space_id,
                        "environmentId": environment_id,
                        "mode": mode,
                        "actions": actions,
                        "origin": origin,
                    }
                )
            )
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "spaceId": space_id,
                            "environmentId": environment_id,
                            "mode": mode,
                            "actions": actions,
                            "origin": origin,
                        }
                    )
                ),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"file": file})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FileResponse:
        """
        Parameters:
            - file_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.files.get(
            file_id="us_fl_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Parameters:
            - file_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
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

    async def update(
        self,
        file_id: str,
        *,
        workbook_id: typing.Optional[WorkbookId] = OMIT,
        name: typing.Optional[str] = OMIT,
        mode: typing.Optional[Mode] = OMIT,
        status: typing.Optional[ModelFileStatusEnum] = OMIT,
        actions: typing.Optional[typing.Sequence[Action]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileResponse:
        """
        Update a file, to change the workbook id for example

        Parameters:
            - file_id: str. ID of file to update

            - workbook_id: typing.Optional[WorkbookId].

            - name: typing.Optional[str]. The name of the file

            - mode: typing.Optional[Mode]. The storage mode of file to update

            - status: typing.Optional[ModelFileStatusEnum]. Status of the file

            - actions: typing.Optional[typing.Sequence[Action]]. The actions attached to the file

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.files.update(
            file_id="us_fl_YOUR_ID",
            name="NewFileName",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if workbook_id is not OMIT:
            _request["workbookId"] = workbook_id
        if name is not OMIT:
            _request["name"] = name
        if mode is not OMIT:
            _request["mode"] = mode.value if mode is not None else None
        if status is not OMIT:
            _request["status"] = status.value if status is not None else None
        if actions is not OMIT:
            _request["actions"] = actions
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def download(
        self, file_id: FileId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters:
            - file_id: FileId.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        async with self._client_wrapper.httpx_client.stream(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(file_id)}/download"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            if _response.status_code == 400:
                raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)
