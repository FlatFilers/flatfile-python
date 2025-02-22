# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..commons.types.sheet_id import SheetId
from ..core.request_options import RequestOptions
from .types.list_views_response import ListViewsResponse
from ..core.pydantic_utilities import parse_obj_as
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.types.errors import Errors
from ..commons.errors.not_found_error import NotFoundError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.view_config import ViewConfig
from .types.view_response import ViewResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..commons.types.view_id import ViewId
from ..core.jsonable_encoder import jsonable_encoder
from ..commons.types.success import Success
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ViewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        sheet_id: SheetId,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListViewsResponse:
        """
        Returns all views for the sheet

        Parameters
        ----------
        sheet_id : SheetId
            The associated sheet ID of the view.

        page_size : typing.Optional[int]
            Number of prompts to return in a page (default 10)

        page_number : typing.Optional[int]
            Based on pageSize, which page of prompts to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListViewsResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.views.list(
            sheet_id="us_sh_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "views",
            method="GET",
            params={
                "sheetId": sheet_id,
                "pageSize": page_size,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListViewsResponse,
                    parse_obj_as(
                        type_=ListViewsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        sheet_id: SheetId,
        name: str,
        config: ViewConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ViewResponse:
        """
        Add a new view to the space

        Parameters
        ----------
        sheet_id : SheetId

        name : str

        config : ViewConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewResponse

        Examples
        --------
        from flatfile import Flatfile
        from flatfile.views import ViewConfig

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.views.create(
            sheet_id="us_sh_YOUR_ID",
            name="My View",
            config=ViewConfig(
                filter="error",
                filter_field="email",
                q="firstname like %John%",
                sort_field="email",
                sort_direction="asc",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "views",
            method="POST",
            json={
                "sheetId": sheet_id,
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=ViewConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ViewResponse,
                    parse_obj_as(
                        type_=ViewResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, view_id: ViewId, *, request_options: typing.Optional[RequestOptions] = None) -> ViewResponse:
        """
        Returns a single view

        Parameters
        ----------
        view_id : ViewId
            ID of view to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.views.get(
            view_id="us_vi_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"views/{jsonable_encoder(view_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ViewResponse,
                    parse_obj_as(
                        type_=ViewResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        view_id: ViewId,
        *,
        config: ViewConfig,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ViewResponse:
        """
        Updates a single view

        Parameters
        ----------
        view_id : ViewId
            ID of view to update

        config : ViewConfig

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewResponse

        Examples
        --------
        from flatfile import Flatfile
        from flatfile.views import ViewConfig

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.views.update(
            view_id="us_vi_YOUR_ID",
            name="My View",
            config=ViewConfig(
                filter="error",
                filter_field="email",
                q="firstname like %John%",
                sort_field="email",
                sort_direction="asc",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"views/{jsonable_encoder(view_id)}",
            method="PATCH",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=ViewConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ViewResponse,
                    parse_obj_as(
                        type_=ViewResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, view_id: ViewId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Deletes a single view

        Parameters
        ----------
        view_id : ViewId
            ID of view to delete

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
        client.views.delete(
            view_id="us_vi_YOUR_ID",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"views/{jsonable_encoder(view_id)}",
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


class AsyncViewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        sheet_id: SheetId,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListViewsResponse:
        """
        Returns all views for the sheet

        Parameters
        ----------
        sheet_id : SheetId
            The associated sheet ID of the view.

        page_size : typing.Optional[int]
            Number of prompts to return in a page (default 10)

        page_number : typing.Optional[int]
            Based on pageSize, which page of prompts to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListViewsResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.list(
                sheet_id="us_sh_YOUR_ID",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "views",
            method="GET",
            params={
                "sheetId": sheet_id,
                "pageSize": page_size,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListViewsResponse,
                    parse_obj_as(
                        type_=ListViewsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        sheet_id: SheetId,
        name: str,
        config: ViewConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ViewResponse:
        """
        Add a new view to the space

        Parameters
        ----------
        sheet_id : SheetId

        name : str

        config : ViewConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile
        from flatfile.views import ViewConfig

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.create(
                sheet_id="us_sh_YOUR_ID",
                name="My View",
                config=ViewConfig(
                    filter="error",
                    filter_field="email",
                    q="firstname like %John%",
                    sort_field="email",
                    sort_direction="asc",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "views",
            method="POST",
            json={
                "sheetId": sheet_id,
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=ViewConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ViewResponse,
                    parse_obj_as(
                        type_=ViewResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, view_id: ViewId, *, request_options: typing.Optional[RequestOptions] = None) -> ViewResponse:
        """
        Returns a single view

        Parameters
        ----------
        view_id : ViewId
            ID of view to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.get(
                view_id="us_vi_YOUR_ID",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"views/{jsonable_encoder(view_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ViewResponse,
                    parse_obj_as(
                        type_=ViewResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        view_id: ViewId,
        *,
        config: ViewConfig,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ViewResponse:
        """
        Updates a single view

        Parameters
        ----------
        view_id : ViewId
            ID of view to update

        config : ViewConfig

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile
        from flatfile.views import ViewConfig

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.update(
                view_id="us_vi_YOUR_ID",
                name="My View",
                config=ViewConfig(
                    filter="error",
                    filter_field="email",
                    q="firstname like %John%",
                    sort_field="email",
                    sort_direction="asc",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"views/{jsonable_encoder(view_id)}",
            method="PATCH",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=ViewConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ViewResponse,
                    parse_obj_as(
                        type_=ViewResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Errors,
                        parse_obj_as(
                            type_=Errors,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, view_id: ViewId, *, request_options: typing.Optional[RequestOptions] = None) -> Success:
        """
        Deletes a single view

        Parameters
        ----------
        view_id : ViewId
            ID of view to delete

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
            await client.views.delete(
                view_id="us_vi_YOUR_ID",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"views/{jsonable_encoder(view_id)}",
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
