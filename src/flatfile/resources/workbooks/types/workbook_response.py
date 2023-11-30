# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .workbook import Workbook

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class WorkbookResponse(pydantic.BaseModel):
    """
    import datetime

    from flatfile import (
        Action,
        ActionMode,
        Property_String,
        RecordCounts,
        Sheet,
        SheetConfig,
        Workbook,
        WorkbookConfigSettings,
        WorkbookResponse,
    )

    WorkbookResponse(
        data=Workbook(
            id="us_wb_YOUR_ID",
            name="My First Workbook",
            space_id="us_sp_YOUR_ID",
            environment_id="us_env_YOUR_ID",
            sheets=[
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
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
    )
    """

    data: Workbook

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
