# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commits.types.list_commits_response import ListCommitsResponse
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.errors import Errors
from ..commons.types.space_id import SpaceId
from ..commons.types.success import Success
from ..commons.types.workbook_id import WorkbookId
from .types.create_workbook_config import CreateWorkbookConfig
from .types.list_workbooks_response import ListWorkbooksResponse
from .types.workbook_response import WorkbookResponse
from .types.workbook_update import WorkbookUpdate

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WorkbooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, space_id: typing.Optional[SpaceId] = None, include_counts: typing.Optional[bool] = None
    ) -> ListWorkbooksResponse:
        """
        Returns all workbooks matching a filter for an account or space

        Parameters:
            - space_id: typing.Optional[SpaceId]. The associated Space ID of the Workbook.

            - include_counts: typing.Optional[bool]. Include counts for the workbook
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.workbooks.list(
            space_id="us_sp_YOUR_ID",
            include_counts=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workbooks"),
            params=remove_none_from_dict({"spaceId": space_id, "includeCounts": include_counts}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListWorkbooksResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: CreateWorkbookConfig) -> WorkbookResponse:
        """
        Creates a workbook and adds it to a space

        Parameters:
            - request: CreateWorkbookConfig.
        ---
        from flatfile import (
            Action,
            ActionMode,
            CreateWorkbookConfig,
            Property_String,
            SheetConfig,
            WorkbookConfigSettings,
        )
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.workbooks.create(
            request=CreateWorkbookConfig(
                name="My First Workbook",
                sheets=[
                    SheetConfig(
                        name="Contacts",
                        slug="contacts",
                        fields=[
                            Property_String(
                                type="string",
                                key="firstName",
                                label="First Name",
                            ),
                            Property_String(
                                type="string",
                                key="lastName",
                                label="Last Name",
                            ),
                            Property_String(
                                type="string",
                                key="email",
                                label="Email",
                            ),
                        ],
                        mapping_confidence_threshold=0.5,
                    )
                ],
                labels=["simple-demo"],
                actions=[
                    Action(
                        operation="submitAction",
                        mode=ActionMode.FOREGROUND,
                        label="Submit",
                        description="Submit data to webhook.site",
                        primary=True,
                    )
                ],
                settings=WorkbookConfigSettings(
                    track_changes=True,
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workbooks"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WorkbookResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, workbook_id: WorkbookId) -> WorkbookResponse:
        """
        Returns a single workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook to return
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.workbooks.get(
            workbook_id="us_wb_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WorkbookResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, workbook_id: WorkbookId) -> Success:
        """
        Deletes a workbook and all of its record data permanently

        Parameters:
            - workbook_id: WorkbookId. ID of workbook to delete
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.workbooks.delete(
            workbook_id="us_wb_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}"),
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

    def update(self, workbook_id: WorkbookId, *, request: WorkbookUpdate) -> WorkbookResponse:
        """
        Updates a workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook to update

            - request: WorkbookUpdate.
        ---
        from flatfile import Action, ActionMode, WorkbookUpdate
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.workbooks.update(
            workbook_id="us_wb_YOUR_ID",
            request=WorkbookUpdate(
                name="My Updated Workbook",
                labels=["my-new-label"],
                actions=[
                    Action(
                        operation="submitAction",
                        mode=ActionMode.FOREGROUND,
                        label="Submit Changes",
                        description="Submit data to webhook.site",
                        primary=True,
                    )
                ],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WorkbookResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_workbook_commits(
        self, workbook_id: WorkbookId, *, completed: typing.Optional[bool] = None
    ) -> ListCommitsResponse:
        """
        Returns the commits for a workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook

            - completed: typing.Optional[bool]. If true, only return commits that have been completed. If false, only return commits that have not been completed. If not provided, return all commits.
        ---
        from flatfile.client import Flatfile

        client = Flatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        client.workbooks.get_workbook_commits(
            workbook_id="us_wb_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}/commits"),
            params=remove_none_from_dict({"completed": completed}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListCommitsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWorkbooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, space_id: typing.Optional[SpaceId] = None, include_counts: typing.Optional[bool] = None
    ) -> ListWorkbooksResponse:
        """
        Returns all workbooks matching a filter for an account or space

        Parameters:
            - space_id: typing.Optional[SpaceId]. The associated Space ID of the Workbook.

            - include_counts: typing.Optional[bool]. Include counts for the workbook
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.workbooks.list(
            space_id="us_sp_YOUR_ID",
            include_counts=True,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workbooks"),
            params=remove_none_from_dict({"spaceId": space_id, "includeCounts": include_counts}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListWorkbooksResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: CreateWorkbookConfig) -> WorkbookResponse:
        """
        Creates a workbook and adds it to a space

        Parameters:
            - request: CreateWorkbookConfig.
        ---
        from flatfile import (
            Action,
            ActionMode,
            CreateWorkbookConfig,
            Property_String,
            SheetConfig,
            WorkbookConfigSettings,
        )
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.workbooks.create(
            request=CreateWorkbookConfig(
                name="My First Workbook",
                sheets=[
                    SheetConfig(
                        name="Contacts",
                        slug="contacts",
                        fields=[
                            Property_String(
                                type="string",
                                key="firstName",
                                label="First Name",
                            ),
                            Property_String(
                                type="string",
                                key="lastName",
                                label="Last Name",
                            ),
                            Property_String(
                                type="string",
                                key="email",
                                label="Email",
                            ),
                        ],
                        mapping_confidence_threshold=0.5,
                    )
                ],
                labels=["simple-demo"],
                actions=[
                    Action(
                        operation="submitAction",
                        mode=ActionMode.FOREGROUND,
                        label="Submit",
                        description="Submit data to webhook.site",
                        primary=True,
                    )
                ],
                settings=WorkbookConfigSettings(
                    track_changes=True,
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workbooks"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WorkbookResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, workbook_id: WorkbookId) -> WorkbookResponse:
        """
        Returns a single workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook to return
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.workbooks.get(
            workbook_id="us_wb_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WorkbookResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, workbook_id: WorkbookId) -> Success:
        """
        Deletes a workbook and all of its record data permanently

        Parameters:
            - workbook_id: WorkbookId. ID of workbook to delete
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.workbooks.delete(
            workbook_id="us_wb_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}"),
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

    async def update(self, workbook_id: WorkbookId, *, request: WorkbookUpdate) -> WorkbookResponse:
        """
        Updates a workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook to update

            - request: WorkbookUpdate.
        ---
        from flatfile import Action, ActionMode, WorkbookUpdate
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.workbooks.update(
            workbook_id="us_wb_YOUR_ID",
            request=WorkbookUpdate(
                name="My Updated Workbook",
                labels=["my-new-label"],
                actions=[
                    Action(
                        operation="submitAction",
                        mode=ActionMode.FOREGROUND,
                        label="Submit Changes",
                        description="Submit data to webhook.site",
                        primary=True,
                    )
                ],
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WorkbookResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(Errors, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_workbook_commits(
        self, workbook_id: WorkbookId, *, completed: typing.Optional[bool] = None
    ) -> ListCommitsResponse:
        """
        Returns the commits for a workbook

        Parameters:
            - workbook_id: WorkbookId. ID of workbook

            - completed: typing.Optional[bool]. If true, only return commits that have been completed. If false, only return commits that have not been completed. If not provided, return all commits.
        ---
        from flatfile.client import AsyncFlatfile

        client = AsyncFlatfile(
            x_disable_hooks="YOUR_X_DISABLE_HOOKS",
            token="YOUR_TOKEN",
        )
        await client.workbooks.get_workbook_commits(
            workbook_id="us_wb_YOUR_ID",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"workbooks/{workbook_id}/commits"),
            params=remove_none_from_dict({"completed": completed}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListCommitsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
