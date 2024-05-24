# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SheetUpdateRequest(pydantic.BaseModel):
    """
    Changes to make to an existing sheet
    ---
    from flatfile import SheetUpdateRequest

    SheetUpdateRequest(
        name="New Sheet Name",
        metadata={"rowHeaders": [6]},
    )
    """

    name: typing.Optional[str] = pydantic.Field(default=None, description="The name of the Sheet.")
    slug: typing.Optional[str] = pydantic.Field(default=None, description="The slug of the Sheet.")
    metadata: typing.Optional[typing.Any] = pydantic.Field(
        default=None, description="Useful for any contextual metadata regarding the sheet. Store any valid json"
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
        json_encoders = {dt.datetime: serialize_datetime}
