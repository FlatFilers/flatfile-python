# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.action import Action

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DocumentConfig(pydantic.BaseModel):
    """
    from flatfile import Action, ActionMode, DocumentConfig

    DocumentConfig(
        title="My Document 1",
        body="My information",
        actions=[
            Action(
                operation="submitAction",
                mode=ActionMode.FOREGROUND,
                label="Submit",
                description="Submit data to webhook.site",
                primary=True,
            )
        ],
    )
    """

    title: str
    body: str
    treatments: typing.Optional[typing.List[str]] = pydantic.Field(
        description="Certain treatments will cause your Document to look or behave differently."
    )
    actions: typing.Optional[typing.List[Action]]

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
