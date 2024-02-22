# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.forbidden_error import ForbiddenError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.actor_role_id import ActorRoleId
from ..commons.types.agent_id import AgentId
from ..commons.types.environment_id import EnvironmentId
from ..commons.types.errors import Errors
from ..commons.types.event_id import EventId
from ..commons.types.page_number import PageNumber
from ..commons.types.page_size import PageSize
from ..commons.types.space_id import SpaceId
from ..commons.types.success import Success
from ..commons.types.success_query_parameter import SuccessQueryParameter
from ..roles.types.assign_actor_role_request import AssignActorRoleRequest
from ..roles.types.assign_role_response import AssignRoleResponse
from ..roles.types.list_actor_roles_response import ListActorRolesResponse
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
            token="YOUR_TOKEN",
        )
        client.agents.list(
            environment_id="us_env_YOUR_ID",
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
            token="YOUR_TOKEN",
        )
        client.agents.create(
            environment_id="us_env_YOUR_ID",
            request=AgentConfig(
                topics=[EventTopic.WORKBOOK_UPDATED],
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
            token="YOUR_TOKEN",
        )
        client.agents.get(
            agent_id="us_ag_YOUR_ID",
            environment_id="us_env_YOUR_ID",
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

    def list_agent_roles(self, agent_id: AgentId) -> ListActorRolesResponse:
        """
        Lists roles assigned to an agent.

        Parameters:
            - agent_id: AgentId. The agent id
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/roles"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListActorRolesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def assign_agent_role(self, agent_id: AgentId, *, request: AssignActorRoleRequest) -> AssignRoleResponse:
        """
        Assigns a role to a agent.

        Parameters:
            - agent_id: AgentId. The agent id

            - request: AssignActorRoleRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/roles"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AssignRoleResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_agent_role(self, agent_id: AgentId, actor_role_id: ActorRoleId) -> Success:
        """
        Removes a role from an agent.

        Parameters:
            - agent_id: AgentId. The agent id

            - actor_role_id: ActorRoleId. The actor role id
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/roles/{actor_role_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
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
            token="YOUR_TOKEN",
        )
        client.agents.get_agent_logs(
            agent_id="us_ag_YOUR_ID",
            environment_id="us_env_YOUR_ID",
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
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.agents.get_agent_log(
            event_id="commons.EventId",
            environment_id="us_env_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/log/{event_id}"),
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
        space_id: typing.Optional[SpaceId] = None,
        success: typing.Optional[SuccessQueryParameter] = None,
        page_size: typing.Optional[PageSize] = None,
        page_number: typing.Optional[PageNumber] = None,
    ) -> GetDetailedAgentLogsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: typing.Optional[SpaceId].

            - success: typing.Optional[SuccessQueryParameter].

            - page_size: typing.Optional[PageSize].

            - page_number: typing.Optional[PageNumber].
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.agents.get_environment_agent_logs(
            environment_id="us_env_YOUR_ID",
            space_id="us_sp_YOUR_ID",
            success=True,
            page_size=20,
            page_number=1,
        )
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
        space_id: typing.Optional[SpaceId] = None,
        success: typing.Optional[SuccessQueryParameter] = None,
        page_size: typing.Optional[PageSize] = None,
        page_number: typing.Optional[PageNumber] = None,
    ) -> GetExecutionsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: typing.Optional[SpaceId].

            - success: typing.Optional[SuccessQueryParameter].

            - page_size: typing.Optional[PageSize].

            - page_number: typing.Optional[PageNumber].
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.agents.get_environment_agent_executions(
            environment_id="us_env_YOUR_ID",
            space_id="us_sp_YOUR_ID",
            success=True,
            page_size=20,
            page_number=1,
        )
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

    def delete(self, agent_id: AgentId, *, environment_id: EnvironmentId) -> Success:
        """
        Deletes a single agent

        Parameters:
            - agent_id: AgentId.

            - environment_id: EnvironmentId.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.agents.delete(
            agent_id="us_ag_YOUR_ID",
            environment_id="us_env_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}"),
            params=remove_none_from_dict({"environmentId": environment_id}),
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
            token="YOUR_TOKEN",
        )
        await client.agents.list(
            environment_id="us_env_YOUR_ID",
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
            token="YOUR_TOKEN",
        )
        await client.agents.create(
            environment_id="us_env_YOUR_ID",
            request=AgentConfig(
                topics=[EventTopic.WORKBOOK_UPDATED],
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
            token="YOUR_TOKEN",
        )
        await client.agents.get(
            agent_id="us_ag_YOUR_ID",
            environment_id="us_env_YOUR_ID",
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

    async def list_agent_roles(self, agent_id: AgentId) -> ListActorRolesResponse:
        """
        Lists roles assigned to an agent.

        Parameters:
            - agent_id: AgentId. The agent id
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/roles"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListActorRolesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def assign_agent_role(self, agent_id: AgentId, *, request: AssignActorRoleRequest) -> AssignRoleResponse:
        """
        Assigns a role to a agent.

        Parameters:
            - agent_id: AgentId. The agent id

            - request: AssignActorRoleRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/roles"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AssignRoleResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_agent_role(self, agent_id: AgentId, actor_role_id: ActorRoleId) -> Success:
        """
        Removes a role from an agent.

        Parameters:
            - agent_id: AgentId. The agent id

            - actor_role_id: ActorRoleId. The actor role id
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}/roles/{actor_role_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Success, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
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
            token="YOUR_TOKEN",
        )
        await client.agents.get_agent_logs(
            agent_id="us_ag_YOUR_ID",
            environment_id="us_env_YOUR_ID",
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
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.agents.get_agent_log(
            event_id="commons.EventId",
            environment_id="us_env_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/log/{event_id}"),
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
        space_id: typing.Optional[SpaceId] = None,
        success: typing.Optional[SuccessQueryParameter] = None,
        page_size: typing.Optional[PageSize] = None,
        page_number: typing.Optional[PageNumber] = None,
    ) -> GetDetailedAgentLogsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: typing.Optional[SpaceId].

            - success: typing.Optional[SuccessQueryParameter].

            - page_size: typing.Optional[PageSize].

            - page_number: typing.Optional[PageNumber].
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.agents.get_environment_agent_logs(
            environment_id="us_env_YOUR_ID",
            space_id="us_sp_YOUR_ID",
            success=True,
            page_size=20,
            page_number=1,
        )
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
        space_id: typing.Optional[SpaceId] = None,
        success: typing.Optional[SuccessQueryParameter] = None,
        page_size: typing.Optional[PageSize] = None,
        page_number: typing.Optional[PageNumber] = None,
    ) -> GetExecutionsResponse:
        """
        Parameters:
            - environment_id: EnvironmentId.

            - space_id: typing.Optional[SpaceId].

            - success: typing.Optional[SuccessQueryParameter].

            - page_size: typing.Optional[PageSize].

            - page_number: typing.Optional[PageNumber].
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.agents.get_environment_agent_executions(
            environment_id="us_env_YOUR_ID",
            space_id="us_sp_YOUR_ID",
            success=True,
            page_size=20,
            page_number=1,
        )
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

    async def delete(self, agent_id: AgentId, *, environment_id: EnvironmentId) -> Success:
        """
        Deletes a single agent

        Parameters:
            - agent_id: AgentId.

            - environment_id: EnvironmentId.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )
        await client.agents.delete(
            agent_id="us_ag_YOUR_ID",
            environment_id="us_env_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"agents/{agent_id}"),
            params=remove_none_from_dict({"environmentId": environment_id}),
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
