# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.environment_id import EnvironmentId
from ..commons.types.errors import Errors
from ..commons.types.event_id import EventId
from ..commons.types.space_id import SpaceId
from ..commons.types.success import Success
from ..spaces.types.event_token_response import EventTokenResponse
from .types.create_event_config import CreateEventConfig
from .types.event_response import EventResponse
from .types.list_all_events_response import ListAllEventsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        environment_id: typing.Optional[EnvironmentId] = None,
        space_id: typing.Optional[SpaceId] = None,
        domain: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        include_acknowledged: typing.Optional[bool] = None,
    ) -> ListAllEventsResponse:
        """
        Event topics that the Flatfile Platform emits.

        Parameters:
            - environment_id: typing.Optional[EnvironmentId]. Filter by environment

            - space_id: typing.Optional[SpaceId]. Filter by space

            - domain: typing.Optional[str]. Filter by event domain

            - topic: typing.Optional[str]. Filter by event topic

            - since: typing.Optional[dt.datetime]. Filter by event timestamp

            - page_size: typing.Optional[int]. Number of results to return in a page (default 10)

            - page_number: typing.Optional[int]. Based on pageSize, which page of results to return

            - include_acknowledged: typing.Optional[bool]. Include acknowledged events
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events"),
            params=remove_none_from_dict(
                {
                    "environmentId": environment_id,
                    "spaceId": space_id,
                    "domain": domain,
                    "topic": topic,
                    "since": serialize_datetime(since) if since is not None else None,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                    "includeAcknowledged": include_acknowledged,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListAllEventsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: CreateEventConfig) -> EventResponse:
        """
        Parameters:
            - request: CreateEventConfig.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, event_id: EventId) -> EventResponse:
        """
        Parameters:
            - event_id: EventId. The event id
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/{event_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def ack(self, event_id: EventId) -> Success:
        """
        Parameters:
            - event_id: EventId. The event id
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/{event_id}/ack"),
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

    def get_event_token(
        self, *, space_id: typing.Optional[SpaceId] = None, scope: typing.Optional[str] = None
    ) -> EventTokenResponse:
        """
        Get a token which can be used to subscribe to events for this space

        Parameters:
            - space_id: typing.Optional[SpaceId]. The space id

            - scope: typing.Optional[str]. The scope of the event stream (space or environment id)
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "subscription"),
            params=remove_none_from_dict({"spaceId": space_id, "scope": scope}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventTokenResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        environment_id: typing.Optional[EnvironmentId] = None,
        space_id: typing.Optional[SpaceId] = None,
        domain: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        include_acknowledged: typing.Optional[bool] = None,
    ) -> ListAllEventsResponse:
        """
        Event topics that the Flatfile Platform emits.

        Parameters:
            - environment_id: typing.Optional[EnvironmentId]. Filter by environment

            - space_id: typing.Optional[SpaceId]. Filter by space

            - domain: typing.Optional[str]. Filter by event domain

            - topic: typing.Optional[str]. Filter by event topic

            - since: typing.Optional[dt.datetime]. Filter by event timestamp

            - page_size: typing.Optional[int]. Number of results to return in a page (default 10)

            - page_number: typing.Optional[int]. Based on pageSize, which page of results to return

            - include_acknowledged: typing.Optional[bool]. Include acknowledged events
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events"),
            params=remove_none_from_dict(
                {
                    "environmentId": environment_id,
                    "spaceId": space_id,
                    "domain": domain,
                    "topic": topic,
                    "since": serialize_datetime(since) if since is not None else None,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                    "includeAcknowledged": include_acknowledged,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListAllEventsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: CreateEventConfig) -> EventResponse:
        """
        Parameters:
            - request: CreateEventConfig.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, event_id: EventId) -> EventResponse:
        """
        Parameters:
            - event_id: EventId. The event id
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/{event_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def ack(self, event_id: EventId) -> Success:
        """
        Parameters:
            - event_id: EventId. The event id
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/{event_id}/ack"),
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

    async def get_event_token(
        self, *, space_id: typing.Optional[SpaceId] = None, scope: typing.Optional[str] = None
    ) -> EventTokenResponse:
        """
        Get a token which can be used to subscribe to events for this space

        Parameters:
            - space_id: typing.Optional[SpaceId]. The space id

            - scope: typing.Optional[str]. The scope of the event stream (space or environment id)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "subscription"),
            params=remove_none_from_dict({"spaceId": space_id, "scope": scope}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventTokenResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
