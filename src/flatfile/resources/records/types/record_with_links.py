# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.record_id import RecordId
from .record_config import RecordConfig
from .record_data_with_links import RecordDataWithLinks
from .validation_message import ValidationMessage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RecordWithLinks(pydantic.BaseModel):
    """
    A single row of data in a Sheet, including links to related rows
    ---
    import datetime

    from flatfile import CellValueWithLinks, RecordConfig, RecordWithLinks

    RecordWithLinks(
        id="us_rc_YOUR_ID",
        values={
            "firstName": CellValueWithLinks(
                messages=[],
                valid=True,
                updated_at=datetime.datetime.fromisoformat(
                    "2023-11-20 16:59:40.286000+00:00",
                ),
            ),
            "lastName": CellValueWithLinks(
                messages=[],
                valid=True,
                updated_at=datetime.datetime.fromisoformat(
                    "2023-11-20 16:59:40.286000+00:00",
                ),
            ),
            "email": CellValueWithLinks(
                messages=[],
                valid=True,
                updated_at=datetime.datetime.fromisoformat(
                    "2023-11-20 16:59:40.286000+00:00",
                ),
            ),
        },
        valid=True,
        metadata={},
        config=RecordConfig(),
    )
    """

    id: RecordId
    values: RecordDataWithLinks
    valid: typing.Optional[bool] = None
    messages: typing.Optional[typing.List[ValidationMessage]] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    config: typing.Optional[RecordConfig] = None

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
