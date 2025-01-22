# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.guide_id import GuideId
from .guide_version_resource import GuideVersionResource

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GuideResource(pydantic.BaseModel):
    """
    A guide
    ---
    import datetime

    from flatfile import GuideResource

    GuideResource(
        id="us_gu_YOUR_ID",
        description="Getting started guide",
        title="Importing your data",
        slug="getting-started",
        versions=[],
        blocks=[],
        metadata={"category": "onboarding"},
        created_at=datetime.datetime.fromisoformat(
            "2023-10-30 16:59:45.735000+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2023-10-30 16:59:45.735000+00:00",
        ),
    )
    """

    id: GuideId
    description: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    slug: str
    title: str
    versions: typing.List[GuideVersionResource]
    blocks: typing.List[typing.Optional[typing.Dict[str, typing.Any]]]
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

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
