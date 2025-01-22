# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..commons.types.prompt_id import PromptId
from ..commons.types.success import Success
from .types.prompt_create import PromptCreate
from .types.prompt_patch import PromptPatch
from .types.prompt_response import PromptResponse
from .types.prompt_type_query_enum import PromptTypeQueryEnum
from .types.prompts_response import PromptsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AssistantClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        prompt_type: typing.Optional[PromptTypeQueryEnum] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsResponse:
        """
        Returns prompts created by user

        Parameters:
            - prompt_type: typing.Optional[PromptTypeQueryEnum]. Type of prompt (default AI_ASSIST)

            - page_size: typing.Optional[int]. Number of prompts to return in a page (default 7)

            - page_number: typing.Optional[int]. Based on pageSize, which page of prompts to return

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.assistant.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "prompts"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "promptType": prompt_type,
                        "pageSize": page_size,
                        "pageNumber": page_number,
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
            return pydantic.parse_obj_as(PromptsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, prompt_id: PromptId, *, request_options: typing.Optional[RequestOptions] = None) -> PromptResponse:
        """
        Returns a prompt

        Parameters:
            - prompt_id: PromptId. ID of prompts

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.assistant.get(
            prompt_id="us_pr_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"prompts/{jsonable_encoder(prompt_id)}"),
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
            return pydantic.parse_obj_as(PromptResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, prompt_id: PromptId, *, request: PromptPatch, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptResponse:
        """
        Updates a prompt

        Parameters:
            - prompt_id: PromptId. ID of prompts

            - request: PromptPatch.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import PromptPatch
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.assistant.update(
            prompt_id="us_pr_YOUR_ID",
            request=PromptPatch(
                prompt="Combine first name and last name into a new column called Full Name",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"prompts/{jsonable_encoder(prompt_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(PromptResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: PromptCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptResponse:
        """
        Creates a prompt

        Parameters:
            - request: PromptCreate.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import PromptCreate
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.assistant.create(
            request=PromptCreate(
                prompt="Combine first name and last name into a new column called Full Name",
                environment_id="us_env_YOUR_ID",
                space_id="us_sp_YOUR_ID",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "prompts"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(PromptResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, prompt_id: PromptId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Deletes a prompts

        Parameters:
            - prompt_id: PromptId. ID of prompts

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.assistant.delete(
            prompt_id="us_pr_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"prompts/{jsonable_encoder(prompt_id)}"),
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAssistantClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        prompt_type: typing.Optional[PromptTypeQueryEnum] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsResponse:
        """
        Returns prompts created by user

        Parameters:
            - prompt_type: typing.Optional[PromptTypeQueryEnum]. Type of prompt (default AI_ASSIST)

            - page_size: typing.Optional[int]. Number of prompts to return in a page (default 7)

            - page_number: typing.Optional[int]. Based on pageSize, which page of prompts to return

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.assistant.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "prompts"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "promptType": prompt_type,
                        "pageSize": page_size,
                        "pageNumber": page_number,
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
            return pydantic.parse_obj_as(PromptsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, prompt_id: PromptId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptResponse:
        """
        Returns a prompt

        Parameters:
            - prompt_id: PromptId. ID of prompts

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.assistant.get(
            prompt_id="us_pr_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"prompts/{jsonable_encoder(prompt_id)}"),
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
            return pydantic.parse_obj_as(PromptResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, prompt_id: PromptId, *, request: PromptPatch, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptResponse:
        """
        Updates a prompt

        Parameters:
            - prompt_id: PromptId. ID of prompts

            - request: PromptPatch.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import PromptPatch
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.assistant.update(
            prompt_id="us_pr_YOUR_ID",
            request=PromptPatch(
                prompt="Combine first name and last name into a new column called Full Name",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"prompts/{jsonable_encoder(prompt_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(PromptResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: PromptCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptResponse:
        """
        Creates a prompt

        Parameters:
            - request: PromptCreate.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import PromptCreate
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.assistant.create(
            request=PromptCreate(
                prompt="Combine first name and last name into a new column called Full Name",
                environment_id="us_env_YOUR_ID",
                space_id="us_sp_YOUR_ID",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "prompts"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(PromptResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, prompt_id: PromptId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Deletes a prompts

        Parameters:
            - prompt_id: PromptId. ID of prompts

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.assistant.delete(
            prompt_id="us_pr_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"prompts/{jsonable_encoder(prompt_id)}"),
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
