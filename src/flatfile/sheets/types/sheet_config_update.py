# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from .sheet_access import SheetAccess
from ...property.types.property import Property
from ...commons.types.action import Action
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class SheetConfigUpdate(UniversalBaseModel):
    """
    Changes to make to an existing sheet config
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of your Sheet as it will appear to your end users.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A sentence or two describing the purpose of your Sheet.
    """

    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for your Sheet. **Required when updating a Workbook.**
    """

    readonly: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether or not this sheet is read only. Read only sheets are not editable by end users.
    """

    allow_additional_fields: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowAdditionalFields")
    ] = pydantic.Field(default=None)
    """
    Allow end users to add fields during mapping.
    """

    mapping_confidence_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="mappingConfidenceThreshold")
    ] = pydantic.Field(default=None)
    """
    The minimum confidence required to automatically map a field
    """

    access: typing.Optional[typing.List[SheetAccess]] = pydantic.Field(default=None)
    """
    Control Sheet-level access for all users.
    """

    fields: typing.Optional[typing.List[Property]] = pydantic.Field(default=None)
    """
    Where you define your Sheet’s data schema.
    """

    actions: typing.Optional[typing.List[Action]] = pydantic.Field(default=None)
    """
    An array of actions that end users can perform on this Sheet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
