# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.data_retention_policy_id import DataRetentionPolicyId
from ..commons.types.environment_id import EnvironmentId
from ..commons.types.errors import Errors
from ..commons.types.success import Success
from .types.data_retention_policy_config import DataRetentionPolicyConfig
from .types.data_retention_policy_response import DataRetentionPolicyResponse
from .types.list_data_retention_policies_response import ListDataRetentionPoliciesResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DataRetentionPoliciesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        environment_id: typing.Optional[EnvironmentId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDataRetentionPoliciesResponse:
        """
        Returns all data retention policies on an account matching a filter for environmentId

        Parameters:
            - environment_id: typing.Optional[EnvironmentId]. The associated Environment ID of the policy.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.data_retention_policies.list(
            environment_id="us_env_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "data-retention-policies"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "environmentId": environment_id,
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
            return pydantic.parse_obj_as(ListDataRetentionPoliciesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: DataRetentionPolicyConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> DataRetentionPolicyResponse:
        """
        Add a new data retention policy to the space

        Parameters:
            - request: DataRetentionPolicyConfig.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import DataRetentionPolicyConfig, DataRetentionPolicyEnum
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.data_retention_policies.create(
            request=DataRetentionPolicyConfig(
                type=DataRetentionPolicyEnum.LAST_ACTIVITY,
                period=5,
                environment_id="us_env_YOUR_ID",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "data-retention-policies"),
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
            return pydantic.parse_obj_as(DataRetentionPolicyResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, id: DataRetentionPolicyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DataRetentionPolicyResponse:
        """
        Returns a single data retention policy

        Parameters:
            - id: DataRetentionPolicyId. ID of data retention policy to return

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.data_retention_policies.get(
            id="us_drp_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"data-retention-policies/{jsonable_encoder(id)}"
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
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DataRetentionPolicyResponse, _response.json())  # type: ignore
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
        id: DataRetentionPolicyId,
        *,
        request: DataRetentionPolicyConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataRetentionPolicyResponse:
        """
        Updates a single data retention policy

        Parameters:
            - id: DataRetentionPolicyId. ID of data retention policy to update

            - request: DataRetentionPolicyConfig.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import DataRetentionPolicyConfig, DataRetentionPolicyEnum
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.data_retention_policies.update(
            id="us_drp_YOUR_ID",
            request=DataRetentionPolicyConfig(
                type=DataRetentionPolicyEnum.LAST_ACTIVITY,
                period=5,
                environment_id="us_env_YOUR_ID",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"data-retention-policies/{jsonable_encoder(id)}"
            ),
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
            return pydantic.parse_obj_as(DataRetentionPolicyResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: DataRetentionPolicyId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Deletes a single data retention policy

        Parameters:
            - id: DataRetentionPolicyId. ID of data retention policy to delete

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"data-retention-policies/{jsonable_encoder(id)}"
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


class AsyncDataRetentionPoliciesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        environment_id: typing.Optional[EnvironmentId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDataRetentionPoliciesResponse:
        """
        Returns all data retention policies on an account matching a filter for environmentId

        Parameters:
            - environment_id: typing.Optional[EnvironmentId]. The associated Environment ID of the policy.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.data_retention_policies.list(
            environment_id="us_env_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "data-retention-policies"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "environmentId": environment_id,
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
            return pydantic.parse_obj_as(ListDataRetentionPoliciesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: DataRetentionPolicyConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> DataRetentionPolicyResponse:
        """
        Add a new data retention policy to the space

        Parameters:
            - request: DataRetentionPolicyConfig.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import DataRetentionPolicyConfig, DataRetentionPolicyEnum
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.data_retention_policies.create(
            request=DataRetentionPolicyConfig(
                type=DataRetentionPolicyEnum.LAST_ACTIVITY,
                period=5,
                environment_id="us_env_YOUR_ID",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "data-retention-policies"),
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
            return pydantic.parse_obj_as(DataRetentionPolicyResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: DataRetentionPolicyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DataRetentionPolicyResponse:
        """
        Returns a single data retention policy

        Parameters:
            - id: DataRetentionPolicyId. ID of data retention policy to return

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.data_retention_policies.get(
            id="us_drp_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"data-retention-policies/{jsonable_encoder(id)}"
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
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DataRetentionPolicyResponse, _response.json())  # type: ignore
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
        id: DataRetentionPolicyId,
        *,
        request: DataRetentionPolicyConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataRetentionPolicyResponse:
        """
        Updates a single data retention policy

        Parameters:
            - id: DataRetentionPolicyId. ID of data retention policy to update

            - request: DataRetentionPolicyConfig.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from flatfile import DataRetentionPolicyConfig, DataRetentionPolicyEnum
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.data_retention_policies.update(
            id="us_drp_YOUR_ID",
            request=DataRetentionPolicyConfig(
                type=DataRetentionPolicyEnum.LAST_ACTIVITY,
                period=5,
                environment_id="us_env_YOUR_ID",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"data-retention-policies/{jsonable_encoder(id)}"
            ),
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
            return pydantic.parse_obj_as(DataRetentionPolicyResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, id: DataRetentionPolicyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        Deletes a single data retention policy

        Parameters:
            - id: DataRetentionPolicyId. ID of data retention policy to delete

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"data-retention-policies/{jsonable_encoder(id)}"
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
