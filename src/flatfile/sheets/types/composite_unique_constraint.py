# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
import typing_extensions
from ...core.serialization import FieldMetadata
from .composite_unique_constraint_strategy import CompositeUniqueConstraintStrategy
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CompositeUniqueConstraint(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the constraint
    """

    fields: typing.List[str] = pydantic.Field()
    """
    The fields that must be unique together
    """

    required_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="requiredFields")
    ] = pydantic.Field(default=None)
    """
    Fields that, when empty, will cause this unique constraint to be ignored
    """

    strategy: CompositeUniqueConstraintStrategy

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
