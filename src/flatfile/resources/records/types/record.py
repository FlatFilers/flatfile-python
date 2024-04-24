# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .record_base import RecordBase
from .record_data import RecordData


class Record(RecordBase):
    """
    A single row of data in a Sheet
    ---
    from flatfile import CellValue, Record, RecordConfig

    Record(
        id="us_rc_YOUR_ID",
        version_id="us_vr_YOUR_ID",
        commit_id="us_vr_YOUR_ID",
        values={
            "firstName": CellValue(
                messages=[],
                valid=True,
            ),
            "lastName": CellValue(
                messages=[],
                valid=True,
            ),
            "email": CellValue(
                messages=[],
                valid=True,
            ),
        },
        valid=True,
        metadata={},
        config=RecordConfig(),
    )
    """

    values: RecordData

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
