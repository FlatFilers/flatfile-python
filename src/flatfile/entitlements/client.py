# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from .types.list_entitlements_response import ListEntitlementsResponse
from ..core.pydantic_utilities import parse_obj_as
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.types.errors import Errors
from ..commons.errors.not_found_error import NotFoundError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper


class EntitlementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, resource_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEntitlementsResponse:
        """
        Returns all entitlements matching a filter for resourceId

        Parameters
        ----------
        resource_id : str
            The associated Resource ID for the entitlements.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEntitlementsResponse

        Examples
        --------
        from flatfile import Flatfile

        client = Flatfile(
            token="YOUR_TOKEN",
        )
        client.entitlements.list(
            resource_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "entitlements",
            method="GET",
            params={
                "resourceId": resource_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListEntitlementsResponse,
                    parse_obj_as(
                        type_=ListEntitlementsResponse,  # type: ignore
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


class AsyncEntitlementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, resource_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEntitlementsResponse:
        """
        Returns all entitlements matching a filter for resourceId

        Parameters
        ----------
        resource_id : str
            The associated Resource ID for the entitlements.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEntitlementsResponse

        Examples
        --------
        import asyncio

        from flatfile import AsyncFlatfile

        client = AsyncFlatfile(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entitlements.list(
                resource_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entitlements",
            method="GET",
            params={
                "resourceId": resource_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListEntitlementsResponse,
                    parse_obj_as(
                        type_=ListEntitlementsResponse,  # type: ignore
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
