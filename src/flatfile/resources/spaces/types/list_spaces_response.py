# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.pagination import Pagination
from .space import Space

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ListSpacesResponse(pydantic.BaseModel):
    """
    List of Space objects
    ---
    import datetime

    from flatfile import (
        GuestAuthenticationEnum,
        ListSpacesResponse,
        Pagination,
        Space,
    )

    ListSpacesResponse(
        pagination=Pagination(
            current_page=3,
            page_count=50,
            total_count=100,
        ),
        data=[
            Space(
                id="us_sp_YOUR_ID",
                name="My First Worbook",
                display_order=1,
                created_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                created_by_user_id="us_usr_YOUR_ID",
                workbooks_count=1,
                files_count=1,
                is_collaborative=True,
                upgraded_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                guest_authentication=[
                    GuestAuthenticationEnum.MAGIC_LINK,
                    GuestAuthenticationEnum.SHARED_LINK,
                ],
                environment_id="us_env_YOUR_ID",
                primary_workbook_id="us_wb_YOUR_ID",
                labels=[],
            )
        ],
    )
    """

    pagination: typing.Optional[Pagination]
    data: typing.List[Space]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
