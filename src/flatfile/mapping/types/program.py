# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .mapping_rule_or_config import MappingRuleOrConfig
import pydantic
import typing_extensions
from ...commons.types.family_id import FamilyId
from ...core.serialization import FieldMetadata
import datetime as dt
from ...commons.types.user_id import UserId
from .program_summary import ProgramSummary
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Program(UniversalBaseModel):
    rules: typing.List[MappingRuleOrConfig] = pydantic.Field()
    """
    Mapping rules
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this program was saved, this is the ID of the program
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Namespace of the program
    """

    family_id: typing_extensions.Annotated[typing.Optional[FamilyId], FieldMetadata(alias="familyId")] = pydantic.Field(
        default=None
    )
    """
    Family ID of the program, if it belongs to a family
    """

    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = (
        pydantic.Field(default=None)
    )
    """
    If this program was saved, this is the time it was created
    """

    created_by: typing_extensions.Annotated[typing.Optional[UserId], FieldMetadata(alias="createdBy")] = pydantic.Field(
        default=None
    )
    """
    If this program was saved, this is the user ID of the creator
    """

    source_keys: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="sourceKeys")] = pydantic.Field()
    """
    Source keys
    """

    destination_keys: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="destinationKeys")] = (
        pydantic.Field()
    )
    """
    Destination keys
    """

    summary: typing.Optional[ProgramSummary] = pydantic.Field(default=None)
    """
    Summary of the mapping rules
    """

    access_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="accessToken")] = (
        pydantic.Field(default=None)
    )
    """
    If this program was saved, this token allows you to modify the program
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
