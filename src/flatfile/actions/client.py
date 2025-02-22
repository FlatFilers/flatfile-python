# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..commons.types.space_id import SpaceId
from ..commons.types.action_mode import ActionMode
from ..commons.types.action_message import ActionMessage
from ..commons.types.action_schedule import ActionSchedule
from ..commons.types.input_form import InputForm
from ..commons.types.action_constraint import ActionConstraint
from ..commons.types.action_mount import ActionMount
from ..commons.types.guide import Guide
from ..commons.types.guardrail import Guardrail
from ..core.request_options import RequestOptions
from .types.api_action_response import ApiActionResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.api_action_configs import ApiActionConfigs
from .types.api_actions_response import ApiActionsResponse
from ..commons.types.action_id import ActionId
from ..core.jsonable_encoder import jsonable_encoder
from ..commons.types.success import Success
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        space_id: SpaceId,
        target_id: str,
        label: str,
        slug: typing.Optional[str] = OMIT,
        operation: typing.Optional[str] = OMIT,
        mode: typing.Optional[ActionMode] = OMIT,
        tooltip: typing.Optional[str] = OMIT,
        messages: typing.Optional[typing.Sequence[ActionMessage]] = OMIT,
        type: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ActionSchedule] = OMIT,
        primary: typing.Optional[bool] = OMIT,
        confirm: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        require_all_valid: typing.Optional[bool] = OMIT,
        require_selection: typing.Optional[bool] = OMIT,
        input_form: typing.Optional[InputForm] = OMIT,
        constraints: typing.Optional[typing.Sequence[ActionConstraint]] = OMIT,
        mount: typing.Optional[ActionMount] = OMIT,
        guide: typing.Optional[Guide] = OMIT,
        guardrail: typing.Optional[Guardrail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiActionResponse:
        """
        Parameters
        ----------
        space_id : SpaceId
            The Space ID for which to create the Action.

        target_id : str

        label : str
            The text on the Button itself

        slug : typing.Optional[str]
            **This is deprecated. Use `operation` instead.**

        operation : typing.Optional[str]
            This will become the job operation that is triggered

        mode : typing.Optional[ActionMode]
            Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete

        tooltip : typing.Optional[str]
            A tooltip that appears when hovering the action button

        messages : typing.Optional[typing.Sequence[ActionMessage]]

        type : typing.Optional[str]
            **This is deprecated.**

        description : typing.Optional[str]
            The text that appears in the dialog after the action is clicked.

        schedule : typing.Optional[ActionSchedule]
            Determines if the action should happen on a regular cadence.

        primary : typing.Optional[bool]
            A primary action will be more visibly present, whether in Sheet or Workbook.

        confirm : typing.Optional[bool]
            Whether to show a modal to confirm the action

        icon : typing.Optional[str]
            Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.

        require_all_valid : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        require_selection : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        input_form : typing.Optional[InputForm]
            Adds an input form for this action after it is clicked.

        constraints : typing.Optional[typing.Sequence[ActionConstraint]]
            A limitation or restriction on the action.

        mount : typing.Optional[ActionMount]

        guide : typing.Optional[Guide]

        guardrail : typing.Optional[Guardrail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.actions.create(
            space_id="spaceId",
            target_id="targetId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions",
            method="POST",
            params={
                "spaceId": space_id,
            },
            json={
                "targetId": target_id,
                "label": label,
                "slug": slug,
                "operation": operation,
                "mode": mode,
                "tooltip": tooltip,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ActionMessage], direction="write"
                ),
                "type": type,
                "description": description,
                "schedule": schedule,
                "primary": primary,
                "confirm": confirm,
                "icon": icon,
                "requireAllValid": require_all_valid,
                "requireSelection": require_selection,
                "inputForm": convert_and_respect_annotation_metadata(
                    object_=input_form, annotation=InputForm, direction="write"
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=typing.Sequence[ActionConstraint], direction="write"
                ),
                "mount": convert_and_respect_annotation_metadata(
                    object_=mount, annotation=ActionMount, direction="write"
                ),
                "guide": convert_and_respect_annotation_metadata(object_=guide, annotation=Guide, direction="write"),
                "guardrail": convert_and_respect_annotation_metadata(
                    object_=guardrail, annotation=Guardrail, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionResponse,
                    parse_obj_as(
                        type_=ApiActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def bulk_create(
        self, *, space_id: SpaceId, request: ApiActionConfigs, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiActionsResponse:
        """
        Parameters
        ----------
        space_id : SpaceId
            The Space ID for which to create the Actions.

        request : ApiActionConfigs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionsResponse

        Examples
        --------
        from flatfile import Flatfile
        from flatfile.commons import ApiActionConfig

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.actions.bulk_create(
            space_id="spaceId",
            request=[
                ApiActionConfig(
                    target_id="targetId",
                ),
                ApiActionConfig(
                    target_id="targetId",
                ),
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions/bulk",
            method="POST",
            params={
                "spaceId": space_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ApiActionConfigs, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionsResponse,
                    parse_obj_as(
                        type_=ApiActionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all(
        self, *, space_id: SpaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiActionsResponse:
        """
        Parameters
        ----------
        space_id : SpaceId
            The Space ID for which to get the Actions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionsResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.actions.get_all(
            space_id="spaceId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions",
            method="GET",
            params={
                "spaceId": space_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionsResponse,
                    parse_obj_as(
                        type_=ApiActionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, action_id: ActionId, *, request_options: typing.Optional[RequestOptions] = None) -> ApiActionResponse:
        """
        Parameters
        ----------
        action_id : ActionId
            The id of the action to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.actions.get(
            action_id="actionId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"actions/{jsonable_encoder(action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionResponse,
                    parse_obj_as(
                        type_=ApiActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        action_id: ActionId,
        *,
        label: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        operation: typing.Optional[str] = OMIT,
        mode: typing.Optional[ActionMode] = OMIT,
        tooltip: typing.Optional[str] = OMIT,
        messages: typing.Optional[typing.Sequence[ActionMessage]] = OMIT,
        type: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ActionSchedule] = OMIT,
        primary: typing.Optional[bool] = OMIT,
        confirm: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        require_all_valid: typing.Optional[bool] = OMIT,
        require_selection: typing.Optional[bool] = OMIT,
        input_form: typing.Optional[InputForm] = OMIT,
        constraints: typing.Optional[typing.Sequence[ActionConstraint]] = OMIT,
        mount: typing.Optional[ActionMount] = OMIT,
        guide: typing.Optional[Guide] = OMIT,
        guardrail: typing.Optional[Guardrail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiActionResponse:
        """
        Parameters
        ----------
        action_id : ActionId
            The id of the action to patch

        label : typing.Optional[str]

        slug : typing.Optional[str]
            **This is deprecated. Use `operation` instead.**

        operation : typing.Optional[str]
            This will become the job operation that is triggered

        mode : typing.Optional[ActionMode]
            Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete

        tooltip : typing.Optional[str]
            A tooltip that appears when hovering the action button

        messages : typing.Optional[typing.Sequence[ActionMessage]]

        type : typing.Optional[str]
            **This is deprecated.**

        description : typing.Optional[str]
            The text that appears in the dialog after the action is clicked.

        schedule : typing.Optional[ActionSchedule]
            Determines if the action should happen on a regular cadence.

        primary : typing.Optional[bool]
            A primary action will be more visibly present, whether in Sheet or Workbook.

        confirm : typing.Optional[bool]
            Whether to show a modal to confirm the action

        icon : typing.Optional[str]
            Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.

        require_all_valid : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        require_selection : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        input_form : typing.Optional[InputForm]
            Adds an input form for this action after it is clicked.

        constraints : typing.Optional[typing.Sequence[ActionConstraint]]
            A limitation or restriction on the action.

        mount : typing.Optional[ActionMount]

        guide : typing.Optional[Guide]

        guardrail : typing.Optional[Guardrail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.actions.update(
            action_id="actionId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"actions/{jsonable_encoder(action_id)}",
            method="PATCH",
            json={
                "label": label,
                "slug": slug,
                "operation": operation,
                "mode": mode,
                "tooltip": tooltip,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ActionMessage], direction="write"
                ),
                "type": type,
                "description": description,
                "schedule": schedule,
                "primary": primary,
                "confirm": confirm,
                "icon": icon,
                "requireAllValid": require_all_valid,
                "requireSelection": require_selection,
                "inputForm": convert_and_respect_annotation_metadata(
                    object_=input_form, annotation=InputForm, direction="write"
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=typing.Sequence[ActionConstraint], direction="write"
                ),
                "mount": convert_and_respect_annotation_metadata(
                    object_=mount, annotation=ActionMount, direction="write"
                ),
                "guide": convert_and_respect_annotation_metadata(object_=guide, annotation=Guide, direction="write"),
                "guardrail": convert_and_respect_annotation_metadata(
                    object_=guardrail, annotation=Guardrail, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionResponse,
                    parse_obj_as(
                        type_=ApiActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, action_id: ActionId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Parameters
        ----------
        action_id : ActionId
            The id of the action to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.actions.delete(
            action_id="actionId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"actions/{jsonable_encoder(action_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Success,
                    parse_obj_as(
                        type_=Success,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        space_id: SpaceId,
        target_id: str,
        label: str,
        slug: typing.Optional[str] = OMIT,
        operation: typing.Optional[str] = OMIT,
        mode: typing.Optional[ActionMode] = OMIT,
        tooltip: typing.Optional[str] = OMIT,
        messages: typing.Optional[typing.Sequence[ActionMessage]] = OMIT,
        type: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ActionSchedule] = OMIT,
        primary: typing.Optional[bool] = OMIT,
        confirm: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        require_all_valid: typing.Optional[bool] = OMIT,
        require_selection: typing.Optional[bool] = OMIT,
        input_form: typing.Optional[InputForm] = OMIT,
        constraints: typing.Optional[typing.Sequence[ActionConstraint]] = OMIT,
        mount: typing.Optional[ActionMount] = OMIT,
        guide: typing.Optional[Guide] = OMIT,
        guardrail: typing.Optional[Guardrail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiActionResponse:
        """
        Parameters
        ----------
        space_id : SpaceId
            The Space ID for which to create the Action.

        target_id : str

        label : str
            The text on the Button itself

        slug : typing.Optional[str]
            **This is deprecated. Use `operation` instead.**

        operation : typing.Optional[str]
            This will become the job operation that is triggered

        mode : typing.Optional[ActionMode]
            Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete

        tooltip : typing.Optional[str]
            A tooltip that appears when hovering the action button

        messages : typing.Optional[typing.Sequence[ActionMessage]]

        type : typing.Optional[str]
            **This is deprecated.**

        description : typing.Optional[str]
            The text that appears in the dialog after the action is clicked.

        schedule : typing.Optional[ActionSchedule]
            Determines if the action should happen on a regular cadence.

        primary : typing.Optional[bool]
            A primary action will be more visibly present, whether in Sheet or Workbook.

        confirm : typing.Optional[bool]
            Whether to show a modal to confirm the action

        icon : typing.Optional[str]
            Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.

        require_all_valid : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        require_selection : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        input_form : typing.Optional[InputForm]
            Adds an input form for this action after it is clicked.

        constraints : typing.Optional[typing.Sequence[ActionConstraint]]
            A limitation or restriction on the action.

        mount : typing.Optional[ActionMount]

        guide : typing.Optional[Guide]

        guardrail : typing.Optional[Guardrail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.create(
                space_id="spaceId",
                target_id="targetId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions",
            method="POST",
            params={
                "spaceId": space_id,
            },
            json={
                "targetId": target_id,
                "label": label,
                "slug": slug,
                "operation": operation,
                "mode": mode,
                "tooltip": tooltip,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ActionMessage], direction="write"
                ),
                "type": type,
                "description": description,
                "schedule": schedule,
                "primary": primary,
                "confirm": confirm,
                "icon": icon,
                "requireAllValid": require_all_valid,
                "requireSelection": require_selection,
                "inputForm": convert_and_respect_annotation_metadata(
                    object_=input_form, annotation=InputForm, direction="write"
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=typing.Sequence[ActionConstraint], direction="write"
                ),
                "mount": convert_and_respect_annotation_metadata(
                    object_=mount, annotation=ActionMount, direction="write"
                ),
                "guide": convert_and_respect_annotation_metadata(object_=guide, annotation=Guide, direction="write"),
                "guardrail": convert_and_respect_annotation_metadata(
                    object_=guardrail, annotation=Guardrail, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionResponse,
                    parse_obj_as(
                        type_=ApiActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def bulk_create(
        self, *, space_id: SpaceId, request: ApiActionConfigs, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiActionsResponse:
        """
        Parameters
        ----------
        space_id : SpaceId
            The Space ID for which to create the Actions.

        request : ApiActionConfigs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionsResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile
        from flatfile.commons import ApiActionConfig

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.bulk_create(
                space_id="spaceId",
                request=[
                    ApiActionConfig(
                        target_id="targetId",
                    ),
                    ApiActionConfig(
                        target_id="targetId",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions/bulk",
            method="POST",
            params={
                "spaceId": space_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ApiActionConfigs, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionsResponse,
                    parse_obj_as(
                        type_=ApiActionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all(
        self, *, space_id: SpaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiActionsResponse:
        """
        Parameters
        ----------
        space_id : SpaceId
            The Space ID for which to get the Actions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionsResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.get_all(
                space_id="spaceId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions",
            method="GET",
            params={
                "spaceId": space_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionsResponse,
                    parse_obj_as(
                        type_=ApiActionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, action_id: ActionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiActionResponse:
        """
        Parameters
        ----------
        action_id : ActionId
            The id of the action to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.get(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"actions/{jsonable_encoder(action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionResponse,
                    parse_obj_as(
                        type_=ApiActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        action_id: ActionId,
        *,
        label: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        operation: typing.Optional[str] = OMIT,
        mode: typing.Optional[ActionMode] = OMIT,
        tooltip: typing.Optional[str] = OMIT,
        messages: typing.Optional[typing.Sequence[ActionMessage]] = OMIT,
        type: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ActionSchedule] = OMIT,
        primary: typing.Optional[bool] = OMIT,
        confirm: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        require_all_valid: typing.Optional[bool] = OMIT,
        require_selection: typing.Optional[bool] = OMIT,
        input_form: typing.Optional[InputForm] = OMIT,
        constraints: typing.Optional[typing.Sequence[ActionConstraint]] = OMIT,
        mount: typing.Optional[ActionMount] = OMIT,
        guide: typing.Optional[Guide] = OMIT,
        guardrail: typing.Optional[Guardrail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiActionResponse:
        """
        Parameters
        ----------
        action_id : ActionId
            The id of the action to patch

        label : typing.Optional[str]

        slug : typing.Optional[str]
            **This is deprecated. Use `operation` instead.**

        operation : typing.Optional[str]
            This will become the job operation that is triggered

        mode : typing.Optional[ActionMode]
            Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete

        tooltip : typing.Optional[str]
            A tooltip that appears when hovering the action button

        messages : typing.Optional[typing.Sequence[ActionMessage]]

        type : typing.Optional[str]
            **This is deprecated.**

        description : typing.Optional[str]
            The text that appears in the dialog after the action is clicked.

        schedule : typing.Optional[ActionSchedule]
            Determines if the action should happen on a regular cadence.

        primary : typing.Optional[bool]
            A primary action will be more visibly present, whether in Sheet or Workbook.

        confirm : typing.Optional[bool]
            Whether to show a modal to confirm the action

        icon : typing.Optional[str]
            Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.

        require_all_valid : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        require_selection : typing.Optional[bool]
            **This is deprecated. Use `constraints` instead.**

        input_form : typing.Optional[InputForm]
            Adds an input form for this action after it is clicked.

        constraints : typing.Optional[typing.Sequence[ActionConstraint]]
            A limitation or restriction on the action.

        mount : typing.Optional[ActionMount]

        guide : typing.Optional[Guide]

        guardrail : typing.Optional[Guardrail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiActionResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.update(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"actions/{jsonable_encoder(action_id)}",
            method="PATCH",
            json={
                "label": label,
                "slug": slug,
                "operation": operation,
                "mode": mode,
                "tooltip": tooltip,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ActionMessage], direction="write"
                ),
                "type": type,
                "description": description,
                "schedule": schedule,
                "primary": primary,
                "confirm": confirm,
                "icon": icon,
                "requireAllValid": require_all_valid,
                "requireSelection": require_selection,
                "inputForm": convert_and_respect_annotation_metadata(
                    object_=input_form, annotation=InputForm, direction="write"
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=typing.Sequence[ActionConstraint], direction="write"
                ),
                "mount": convert_and_respect_annotation_metadata(
                    object_=mount, annotation=ActionMount, direction="write"
                ),
                "guide": convert_and_respect_annotation_metadata(object_=guide, annotation=Guide, direction="write"),
                "guardrail": convert_and_respect_annotation_metadata(
                    object_=guardrail, annotation=Guardrail, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApiActionResponse,
                    parse_obj_as(
                        type_=ApiActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, action_id: ActionId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Parameters
        ----------
        action_id : ActionId
            The id of the action to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.delete(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"actions/{jsonable_encoder(action_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Success,
                    parse_obj_as(
                        type_=Success,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
