# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .constraint import Constraint
from .field_appearance import FieldAppearance
from ...commons.types.action import Action
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class BaseProperty(UniversalBaseModel):
    key: str
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    User friendly field name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the field. Markdown syntax is supported.
    """

    constraints: typing.Optional[typing.List[Constraint]] = pydantic.Field(default=None)
    """
    A list of constraints that should be applied to this field. This is limited to a maximum of 10 constraints and all external and stored constraints must have unique validator values.
    """

    readonly: typing.Optional[bool] = None
    appearance: typing.Optional[FieldAppearance] = None
    actions: typing.Optional[typing.List[Action]] = pydantic.Field(default=None)
    """
    An array of actions that end users can perform on this Column.
    """

    metadata: typing.Optional[typing.Optional[typing.Any]] = pydantic.Field(default=None)
    """
    Useful for any contextual metadata regarding the schema. Store any valid json here.
    """

    treatments: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A unique presentation for a field in the UI.
    """

    alternative_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="alternativeNames")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
