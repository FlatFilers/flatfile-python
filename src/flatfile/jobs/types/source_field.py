# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...property.types.property import Property
from ...core.serialization import FieldMetadata
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class SourceField(UniversalBaseModel):
    source_field: typing_extensions.Annotated[Property, FieldMetadata(alias="sourceField")] = pydantic.Field()
    """
    The description of the source field
    """

    preview: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of preview values of the data in the source field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
