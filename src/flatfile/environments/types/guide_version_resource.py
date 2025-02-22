# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class GuideVersionResource(UniversalBaseModel):
    """
    A version of a guide

    Examples
    --------
    import datetime

    from flatfile.environments import GuideVersionResource

    GuideVersionResource(
        id="us_gu_123",
        version=1,
        content="# Getting Started\nWelcome to the guide...",
        created_at=datetime.datetime.fromisoformat(
            "2023-10-30 16:59:45.735000+00:00",
        ),
        updated_at=datetime.datetime.fromisoformat(
            "2023-10-30 16:59:45.735000+00:00",
        ),
    )
    """

    id: str
    version: int
    content: str
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
