# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .cell_config import CellConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RecordConfig(pydantic.BaseModel):
    """
    Configuration of a record or specific fields in the record
    ---
    from flatfile import CellConfig, RecordConfig

    RecordConfig(
        readonly=True,
        fields={
            "foo": CellConfig(
                readonly=True,
            ),
            "bar": CellConfig(
                readonly=True,
            ),
        },
    )
    """

    readonly: typing.Optional[bool] = None
    fields: typing.Optional[typing.Dict[str, CellConfig]] = None

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
