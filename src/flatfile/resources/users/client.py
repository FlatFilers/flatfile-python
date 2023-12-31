# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.types.user_id import UserId
from .types.list_users_response import ListUsersResponse
from .types.user_response import UserResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, email: typing.Optional[str] = None) -> ListUsersResponse:
        """
        Gets a list of users

        Parameters:
            - email: typing.Optional[str]. Email of guest to return
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.users.list(
            email="john.smith@example.com",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "users"),
            params=remove_none_from_dict({"email": email}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListUsersResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, user_id: UserId) -> UserResponse:
        """
        Gets a user

        Parameters:
            - user_id: UserId. The user id
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.users.get(
            user_id="us_usr_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, email: typing.Optional[str] = None) -> ListUsersResponse:
        """
        Gets a list of users

        Parameters:
            - email: typing.Optional[str]. Email of guest to return
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.users.list(
            email="john.smith@example.com",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "users"),
            params=remove_none_from_dict({"email": email}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListUsersResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, user_id: UserId) -> UserResponse:
        """
        Gets a user

        Parameters:
            - user_id: UserId. The user id
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.users.get(
            user_id="us_usr_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
