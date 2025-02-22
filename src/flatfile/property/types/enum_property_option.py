# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class EnumPropertyOption(UniversalBaseModel):
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A visual label for this option
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description for this option
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional color to assign this option
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    A reference pointer to a previously registered icon
    """

    meta: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    An arbitrary JSON object to be associated with this option and made available to hooks
    """

    value: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The value or ID of this option. This value will be sent in egress. The type is a string | integer | boolean.
    """

    alternative_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="alternativeNames")
    ] = pydantic.Field(default=None)
    """
    Alternative names to match this enum option to
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The order of this option in the list. SortBy must be set to `ordinal` to use this.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
