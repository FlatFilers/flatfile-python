# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
import typing_extensions
from ...core.serialization import FieldMetadata
from .input_config import InputConfig
from .input_constraint import InputConstraint
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class InputField(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Unique key for a Field.
    """

    label: str = pydantic.Field()
    """
    Visible name of a Field.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brief description below the name of the Field.
    """

    type: str = pydantic.Field()
    """
    Field Types inform the user interface how to sort and display data.
    """

    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Optional[typing.Any]], FieldMetadata(alias="defaultValue")
    ] = pydantic.Field(default=None)
    """
    Default value for a Field.
    """

    config: typing.Optional[InputConfig] = pydantic.Field(default=None)
    """
    Additional configuration for enum Fields.
    """

    constraints: typing.Optional[typing.List[InputConstraint]] = pydantic.Field(default=None)
    """
    Indicate additional validations that will be applied to the Field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
