# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...property.types.property import Property
from ...core.serialization import FieldMetadata
import pydantic
import typing
from .enum_details import EnumDetails
from .metadata import Metadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Edge(UniversalBaseModel):
    source_field: typing_extensions.Annotated[Property, FieldMetadata(alias="sourceField")] = pydantic.Field()
    """
    The description of the source field
    """

    destination_field: typing_extensions.Annotated[Property, FieldMetadata(alias="destinationField")] = pydantic.Field()
    """
    The description of the destination field
    """

    preview: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of preview values of the data in the destination field
    """

    enum_details: typing_extensions.Annotated[typing.Optional[EnumDetails], FieldMetadata(alias="enumDetails")] = (
        pydantic.Field(default=None)
    )
    """
    Only available if one or more of the destination fields is of type enum. Provides category mapping.
    """

    metadata: typing.Optional[Metadata] = pydantic.Field(default=None)
    """
    Metadata about the edge
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
