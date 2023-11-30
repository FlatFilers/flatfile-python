# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.sheet_id import SheetId
from ...commons.types.workbook_id import WorkbookId
from ...records.types.record_counts import RecordCounts
from .sheet_config import SheetConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Sheet(pydantic.BaseModel):
    """
    A place to store tabular data
    ---
    import datetime

    from flatfile import Property_String, RecordCounts, Sheet, SheetConfig

    Sheet(
        id="us_sh_YOUR_ID",
        workbook_id="us_wb_YOUR_ID",
        name="Contacts",
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
        count_records=RecordCounts(
            valid=1000,
            error=0,
            total=1000,
        ),
        locked_by="Example0",
        updated_at=datetime.datetime.fromisoformat(
            "2021-08-31 18:00:00+00:00",
        ),
        created_at=datetime.datetime.fromisoformat(
            "2021-08-31 18:00:00+00:00",
        ),
    )
    """

    id: SheetId = pydantic.Field(description="The ID of the Sheet.")
    workbook_id: WorkbookId = pydantic.Field(alias="workbookId", description="The ID of the Workbook.")
    name: str = pydantic.Field(description="The name of the Sheet.")
    config: SheetConfig = pydantic.Field(description="Describes shape of data as well as behavior")
    count_records: typing.Optional[RecordCounts] = pydantic.Field(
        alias="countRecords", description="The amount of records in the Sheet."
    )
    namespace: typing.Optional[str] = pydantic.Field(description="The scoped namespace of the Sheet.")
    locked_by: typing.Optional[str] = pydantic.Field(alias="lockedBy", description="The actor who locked the Sheet.")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt", description="Date the sheet was last updated")
    created_at: dt.datetime = pydantic.Field(alias="createdAt", description="Date the sheet was created")
    locked_at: typing.Optional[dt.datetime] = pydantic.Field(
        alias="lockedAt", description="The time the Sheet was locked."
    )

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
