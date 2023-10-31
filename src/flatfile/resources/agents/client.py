# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.agent_id import AgentId
from ..commons.types.environment_id import EnvironmentId
from ..commons.types.errors import Errors
from ..commons.types.event_id import EventId
from ..commons.types.space_id import SpaceId
from ..commons.types.success import Success
from .types.agent_config import AgentConfig
from .types.agent_response import AgentResponse
from .types.get_agent_logs_response import GetAgentLogsResponse
from .types.get_detailed_agent_log_response import GetDetailedAgentLogResponse
from .types.get_detailed_agent_logs_response import GetDetailedAgentLogsResponse
from .types.get_executions_response import GetExecutionsResponse
from .types.list_agents_response import ListAgentsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, environment_id: EnvironmentId) -> ListAgentsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.list(
            environment_id="us_env_hVXkXs0b",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListAgentsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, environment_id: EnvironmentId, request: AgentConfig) -> AgentResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - request: AgentConfig.
        ---
        from flatfile import AgentConfig, Compiler, EventTopic
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.create(
            environment_id="us_env_hVXkXs0b",
            request=AgentConfig(
                topics=[EventTopic.FILE_CREATED],
                compiler=Compiler.JS,
                source="module.exports = { routeEvent: async (...args) => { console.log(args) } }",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, agent_id: AgentId, *, environment_id: EnvironmentId) -> AgentResponse:
        """
        Parameters:
            - agent_id: AgentId.

            - environment_id: EnvironmentId.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.get(
            agent_id="us_ag_qGZbKwDW",
            environment_id="us_env_hVXkXs0b",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_agent_logs(self, agent_id: AgentId, *, environment_id: EnvironmentId) -> GetAgentLogsResponse:
        """
        Parameters:
            - agent_id: AgentId.

            - environment_id: EnvironmentId.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.get_agent_logs(
            agent_id="us_ag_qGZbKwDW",
            environment_id="us_env_hVXkXs0b",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/logs"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetAgentLogsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_agent_log(self, event_id: EventId, *, environment_id: EnvironmentId) -> GetDetailedAgentLogResponse:
        """
        Parameters:
            - event_id: EventId.

            - environment_id: EnvironmentId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/logs/{event_id}"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDetailedAgentLogResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_environment_agent_logs(
        self,
        *,
        environment_id: EnvironmentId,
        space_id: SpaceId,
        success: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> GetDetailedAgentLogsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: SpaceId.

            - success: typing.Optional[bool].

            - page_size: typing.Optional[int]. Number of logs to return in a page (default 20)

            - page_number: typing.Optional[int]. Based on pageSize, which page of records to return
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents/logs"),
            params=remove_none_from_dict(
                {
                    "environmentId": environment_id,
                    "spaceId": space_id,
                    "success": success,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDetailedAgentLogsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_environment_agent_executions(
        self,
        *,
        environment_id: EnvironmentId,
        space_id: SpaceId,
        success: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> GetExecutionsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: SpaceId.

            - success: typing.Optional[bool].

            - page_size: typing.Optional[int]. Number of logs to return in a page (default 20)

            - page_number: typing.Optional[int]. Based on pageSize, which page of records to return
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents/executions"),
            params=remove_none_from_dict(
                {
                    "environmentId": environment_id,
                    "spaceId": space_id,
                    "success": success,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExecutionsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, agent_id: AgentId) -> Success:
        """
        Deletes a single agent

        Parameters:
            - agent_id: AgentId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}"),
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


class AsyncAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, environment_id: EnvironmentId) -> ListAgentsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.list(
            environment_id="us_env_hVXkXs0b",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListAgentsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, environment_id: EnvironmentId, request: AgentConfig) -> AgentResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - request: AgentConfig.
        ---
        from flatfile import AgentConfig, Compiler, EventTopic
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.create(
            environment_id="us_env_hVXkXs0b",
            request=AgentConfig(
                topics=[EventTopic.FILE_CREATED],
                compiler=Compiler.JS,
                source="module.exports = { routeEvent: async (...args) => { console.log(args) } }",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, agent_id: AgentId, *, environment_id: EnvironmentId) -> AgentResponse:
        """
        Parameters:
            - agent_id: AgentId.

            - environment_id: EnvironmentId.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.get(
            agent_id="us_ag_qGZbKwDW",
            environment_id="us_env_hVXkXs0b",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_agent_logs(self, agent_id: AgentId, *, environment_id: EnvironmentId) -> GetAgentLogsResponse:
        """
        Parameters:
            - agent_id: AgentId.

            - environment_id: EnvironmentId.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.get_agent_logs(
            agent_id="us_ag_qGZbKwDW",
            environment_id="us_env_hVXkXs0b",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/logs"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetAgentLogsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_agent_log(self, event_id: EventId, *, environment_id: EnvironmentId) -> GetDetailedAgentLogResponse:
        """
        Parameters:
            - event_id: EventId.

            - environment_id: EnvironmentId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/logs/{event_id}"),
            params=remove_none_from_dict({"environmentId": environment_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDetailedAgentLogResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_environment_agent_logs(
        self,
        *,
        environment_id: EnvironmentId,
        space_id: SpaceId,
        success: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> GetDetailedAgentLogsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: SpaceId.

            - success: typing.Optional[bool].

            - page_size: typing.Optional[int]. Number of logs to return in a page (default 20)

            - page_number: typing.Optional[int]. Based on pageSize, which page of records to return
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents/logs"),
            params=remove_none_from_dict(
                {
                    "environmentId": environment_id,
                    "spaceId": space_id,
                    "success": success,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDetailedAgentLogsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_environment_agent_executions(
        self,
        *,
        environment_id: EnvironmentId,
        space_id: SpaceId,
        success: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> GetExecutionsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: SpaceId.

            - success: typing.Optional[bool].

            - page_size: typing.Optional[int]. Number of logs to return in a page (default 20)

            - page_number: typing.Optional[int]. Based on pageSize, which page of records to return
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "agents/executions"),
            params=remove_none_from_dict(
                {
                    "environmentId": environment_id,
                    "spaceId": space_id,
                    "success": success,
                    "pageSize": page_size,
                    "pageNumber": page_number,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExecutionsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, agent_id: AgentId) -> Success:
        """
        Deletes a single agent

        Parameters:
            - agent_id: AgentId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}"),
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
