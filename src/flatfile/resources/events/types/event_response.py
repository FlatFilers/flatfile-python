# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .event import Event

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EventResponse(pydantic.BaseModel):
    """
    import datetime

    from flatfile import (
        Context,
        Domain,
        Event_WorkbookUpdated,
        EventResponse,
        Origin,
    )

    EventResponse(
        data=Event_WorkbookUpdated(
            topic="workbook:updated",
            id="us_evt_YOUR_ID",
            created_at=datetime.datetime.fromisoformat(
                "2023-11-07 20:46:04.300000+00:00",
            ),
            payload={"recordsAdded": 100},
            domain=Domain.WORKBOOK,
            context=Context(
                account_id="us_acc_YOUR_ID",
                actor_id="us_key_SOME_KEY",
                environment_id="us_env_YOUR_ID",
                space_id="us_sp_YOUR_ID",
                workbook_id="us_wb_YOUR_ID",
            ),
            callback_url="",
            data_url="",
            namespaces=["workbook"],
            origin=Origin(
                id="us_wb_YOUR_ID",
            ),
        ),
    )
    """

    data: Event

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
