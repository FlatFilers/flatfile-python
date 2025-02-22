# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .guide_version_resource import GuideVersionResource
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GuideCreateRequest(UniversalBaseModel):
    """
    Create a guide

    Examples
    --------
    from flatfile.environments import GuideCreateRequest

    GuideCreateRequest(
        description="Getting started guide",
        title="Data import made easy",
        slug="getting-started",
        environment_id="commons.EnvironmentId",
        versions=[],
        blocks=[],
        metadata={"category": "onboarding"},
    )
    """

    description: str
    title: str
    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    slug: str
    versions: typing.List[GuideVersionResource]
    blocks: typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]
    environment_id: typing_extensions.Annotated[str, FieldMetadata(alias="environmentId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
