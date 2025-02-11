# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.sheet_id import SheetId
from ...commons.types.snapshot_id import SnapshotId
from ...commons.types.user_id import UserId
from .snapshot_summary import SnapshotSummary

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Snapshot(pydantic.BaseModel):
    """
    import datetime

    from flatfile import (
        Property_String,
        SchemaDiffEnum,
        SheetConfig,
        Snapshot,
        SnapshotSummary,
        SummarySection,
    )

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
            schema_diff={
                "firstName": SchemaDiffEnum.ADDED,
                "lastName": SchemaDiffEnum.REMOVED,
                "email": SchemaDiffEnum.UNCHANGED,
            },
            config=SheetConfig(
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
            ),
        ),
        created_at=datetime.datetime.fromisoformat(
            "2023-01-01 00:00:00+00:00",
        ),
        created_by="us_usr_YOUR_ID",
    )
    """

    id: SnapshotId = pydantic.Field(description="The ID of the Snapshot.")
    sheet_id: SheetId = pydantic.Field(alias="sheetId", description="The ID of the Sheet.")
    label: typing.Optional[str] = pydantic.Field(default=None, description="The title of the Snapshot.")
    summary: typing.Optional[SnapshotSummary] = pydantic.Field(
        default=None,
        description="A summary of the Snapshot. This field is only available on the single get snapshot endpoint. It is not available for the list snapshots endpoint.",
    )
    created_at: dt.datetime = pydantic.Field(alias="createdAt", description="The time the Snapshot was created.")
    created_by: UserId = pydantic.Field(alias="createdBy", description="The actor who created the Snapshot.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
