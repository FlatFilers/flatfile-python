# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .snapshot import Snapshot

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SnapshotsResponse(pydantic.BaseModel):
    """
    import datetime

    from flatfile import (
        Snapshot,
        SnapshotsResponse,
        SnapshotSummary,
        SummarySection,
    )

    SnapshotsResponse(
        data=[
            Snapshot(
                id="us_ss_YOUR_ID",
                sheet_id="us_sh_YOUR_ID",
                label="My snapshot",
                summary=SnapshotSummary(
                    created_since=SummarySection(
                        total=0,
                    ),
                    updated_since=SummarySection(
                        total=5,
                        by_field={"lastName": 5},
                    ),
                    deleted_since=SummarySection(
                        total=5,
                        by_field={"firstName": 1},
                    ),
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2023-01-01 00:00:00+00:00",
                ),
                created_by="us_usr_YOUR_ID",
            )
        ],
    )
    """

    data: typing.List[Snapshot]

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
