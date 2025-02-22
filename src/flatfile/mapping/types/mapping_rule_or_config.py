# This file was auto-generated by Fern from our API Definition.

from .mapping_rule_config import MappingRuleConfig
import typing
from ...commons.types.mapping_id import MappingId
import pydantic
import typing_extensions
from ...commons.types.user_id import UserId
from ...core.serialization import FieldMetadata
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class MappingRuleOrConfig(MappingRuleConfig):
    id: typing.Optional[MappingId] = pydantic.Field(default=None)
    """
    ID of the mapping rule
    """

    confidence: typing.Optional[int] = pydantic.Field(default=None)
    """
    Confidence of the mapping rule
    """

    created_by: typing_extensions.Annotated[typing.Optional[UserId], FieldMetadata(alias="createdBy")] = pydantic.Field(
        default=None
    )
    """
    User ID of the creator of the mapping rule
    """

    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = (
        pydantic.Field(default=None)
    )
    """
    Time the mapping rule was created
    """

    updated_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt")] = (
        pydantic.Field(default=None)
    )
    """
    Time the mapping rule was last updated
    """

    deleted_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="deletedAt")] = (
        pydantic.Field(default=None)
    )
    """
    Time the mapping rule was deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
