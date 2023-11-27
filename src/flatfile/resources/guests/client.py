# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.types.guest_id import GuestId
from ..commons.types.space_id import SpaceId
from ..commons.types.success import Success
from .types.create_guest_response import CreateGuestResponse
from .types.guest_config import GuestConfig
from .types.guest_config_update import GuestConfigUpdate
from .types.guest_response import GuestResponse
from .types.guest_token_response import GuestTokenResponse
from .types.invite import Invite
from .types.list_guests_response import ListGuestsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GuestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, space_id: SpaceId, email: typing.Optional[str] = None) -> ListGuestsResponse:
        """
        Returns all guests

        Parameters:
            - space_id: SpaceId. ID of space to return

            - email: typing.Optional[str]. Email of guest to return
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.list(
            space_id="us_sp_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "guests"),
            params=remove_none_from_dict({"spaceId": space_id, "email": email}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListGuestsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: typing.List[GuestConfig]) -> CreateGuestResponse:
        """
        Guests are only there to upload, edit, and download files and perform their tasks in a specific Space.

        Parameters:
            - request: typing.List[GuestConfig].
        ---
        import datetime

        from flatfile import GuestConfig, GuestSpace, GuestWorkbook
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.create(
            request=[
                GuestConfig(
                    environment_id="us_env_YOUR_ID",
                    email="email@example.com",
                    name="Your Name",
                    spaces=[
                        GuestSpace(
                            id="us_sp_YOUR_ID",
                            workbooks=[
                                GuestWorkbook(
                                    id="us_wb_YOUR_ID",
                                )
                            ],
                            last_accessed=datetime.datetime.fromisoformat(
                                "2023-10-30 16:59:45.735000+00:00",
                            ),
                        )
                    ],
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "guests"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateGuestResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, guest_id: GuestId) -> GuestResponse:
        """
        Returns a single guest

        Parameters:
            - guest_id: GuestId. ID of guest to return
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.get(
            guest_id="us_g_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GuestResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, guest_id: GuestId) -> Success:
        """
        Deletes a single guest

        Parameters:
            - guest_id: GuestId. ID of guest to return
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.delete(
            guest_id="us_g_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, guest_id: GuestId, *, request: GuestConfigUpdate) -> GuestResponse:
        """
        Updates a single guest, for example to change name or email

        Parameters:
            - guest_id: GuestId. ID of guest to return

            - request: GuestConfigUpdate.
        ---
        from flatfile import GuestConfigUpdate
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.update(
            guest_id="us_g_YOUR_ID",
            request=GuestConfigUpdate(
                email="updated@example.com",
                name="Your Name Updated",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GuestResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_guest_token(self, guest_id: GuestId, *, space_id: typing.Optional[SpaceId] = None) -> GuestTokenResponse:
        """
        Returns a single guest token

        Parameters:
            - guest_id: GuestId. ID of guest to return

            - space_id: typing.Optional[SpaceId]. ID of space to return
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.get_guest_token(
            guest_id="us_g_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}/token"),
            params=remove_none_from_dict({"spaceId": space_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GuestTokenResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def invite(self, *, request: typing.List[Invite]) -> Success:
        """
        Guests can be created as a named guest on the Space or there’s a global link that will let anonymous guests into the space.

        Parameters:
            - request: typing.List[Invite].
        ---
        from flatfile import Invite
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.invite(
            request=[
                Invite(
                    guest_id="us_g_YOUR_ID",
                    space_id="us_sp_YOUR_ID",
                    from_name="Your Name",
                    message="Hello, I would like to invite you to my space.",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "invitations"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGuestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, space_id: SpaceId, email: typing.Optional[str] = None) -> ListGuestsResponse:
        """
        Returns all guests

        Parameters:
            - space_id: SpaceId. ID of space to return

            - email: typing.Optional[str]. Email of guest to return
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.list(
            space_id="us_sp_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "guests"),
            params=remove_none_from_dict({"spaceId": space_id, "email": email}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListGuestsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: typing.List[GuestConfig]) -> CreateGuestResponse:
        """
        Guests are only there to upload, edit, and download files and perform their tasks in a specific Space.

        Parameters:
            - request: typing.List[GuestConfig].
        ---
        import datetime

        from flatfile import GuestConfig, GuestSpace, GuestWorkbook
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.create(
            request=[
                GuestConfig(
                    environment_id="us_env_YOUR_ID",
                    email="email@example.com",
                    name="Your Name",
                    spaces=[
                        GuestSpace(
                            id="us_sp_YOUR_ID",
                            workbooks=[
                                GuestWorkbook(
                                    id="us_wb_YOUR_ID",
                                )
                            ],
                            last_accessed=datetime.datetime.fromisoformat(
                                "2023-10-30 16:59:45.735000+00:00",
                            ),
                        )
                    ],
                )
            ],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "guests"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateGuestResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, guest_id: GuestId) -> GuestResponse:
        """
        Returns a single guest

        Parameters:
            - guest_id: GuestId. ID of guest to return
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.get(
            guest_id="us_g_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GuestResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, guest_id: GuestId) -> Success:
        """
        Deletes a single guest

        Parameters:
            - guest_id: GuestId. ID of guest to return
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.delete(
            guest_id="us_g_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, guest_id: GuestId, *, request: GuestConfigUpdate) -> GuestResponse:
        """
        Updates a single guest, for example to change name or email

        Parameters:
            - guest_id: GuestId. ID of guest to return

            - request: GuestConfigUpdate.
        ---
        from flatfile import GuestConfigUpdate
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.update(
            guest_id="us_g_YOUR_ID",
            request=GuestConfigUpdate(
                email="updated@example.com",
                name="Your Name Updated",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GuestResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_guest_token(
        self, guest_id: GuestId, *, space_id: typing.Optional[SpaceId] = None
    ) -> GuestTokenResponse:
        """
        Returns a single guest token

        Parameters:
            - guest_id: GuestId. ID of guest to return

            - space_id: typing.Optional[SpaceId]. ID of space to return
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.get_guest_token(
            guest_id="us_g_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"guests/{guest_id}/token"),
            params=remove_none_from_dict({"spaceId": space_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GuestTokenResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def invite(self, *, request: typing.List[Invite]) -> Success:
        """
        Guests can be created as a named guest on the Space or there’s a global link that will let anonymous guests into the space.

        Parameters:
            - request: typing.List[Invite].
        ---
        from flatfile import Invite
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.invite(
            request=[
                Invite(
                    guest_id="us_g_YOUR_ID",
                    space_id="us_sp_YOUR_ID",
                    from_name="Your Name",
                    message="Hello, I would like to invite you to my space.",
                )
            ],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "invitations"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
