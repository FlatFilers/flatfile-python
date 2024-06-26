# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .sheet import Sheet

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ListSheetsResponse(pydantic.BaseModel):
    """
    import datetime

    from flatfile import ListSheetsResponse, Property_String, Sheet, SheetConfig

    ListSheetsResponse(
        data=[
            Sheet(
                id="us_sh_YOUR_ID",
                workbook_id="us_wb_YOUR_ID",
                name="Contacts",
                slug="contacts",
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
                metadata={"rowHeaders": [4]},
                updated_at=datetime.datetime.fromisoformat(
                    "2021-08-31 18:00:00+00:00",
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2021-08-31 18:00:00+00:00",
                ),
            )
        ],
    )
    """

    data: typing.List[Sheet]

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
