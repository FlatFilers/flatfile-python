# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class NumberConfig(UniversalBaseModel):
    """
    Examples
    --------
    from flatfile.property import NumberConfig

    NumberConfig(
        decimal_places=2,
    )
    """

    decimal_places: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="decimalPlaces")] = (
        pydantic.Field(default=None)
    )
    """
    Number of decimal places to round data to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
