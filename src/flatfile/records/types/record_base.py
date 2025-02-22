# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...commons.types.record_id import RecordId
import typing_extensions
import typing
from ...commons.types.version_id import VersionId
from ...core.serialization import FieldMetadata
import pydantic
from ...commons.types.commit_id import CommitId
from .validation_message import ValidationMessage
from .record_config import RecordConfig
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class RecordBase(UniversalBaseModel):
    """
    Examples
    --------
    from flatfile.records import RecordBase

    RecordBase(
        id="us_rc_YOUR_ID",
        version_id="us_vr_YOUR_ID",
        commit_id="us_vr_YOUR_ID",
        valid=True,
        metadata={},
    )
    """

    id: RecordId
    version_id: typing_extensions.Annotated[typing.Optional[VersionId], FieldMetadata(alias="versionId")] = (
        pydantic.Field(default=None)
    )
    """
    Deprecated, use `commitId` instead.
    """

    commit_id: typing_extensions.Annotated[typing.Optional[CommitId], FieldMetadata(alias="commitId")] = None
    valid: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Auto-generated value based on whether the record contains a field with an error message. Cannot be set via the API.
    """

    messages: typing.Optional[typing.List[ValidationMessage]] = pydantic.Field(default=None)
    """
    This record level `messages` property is deprecated and no longer stored or used. Use the `messages` property on the individual cell values instead. This property will be removed in a future release.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    config: typing.Optional[RecordConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
