# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class StoredConstraint(UniversalBaseModel):
    validator: str = pydantic.Field()
    """
    Must match the constraint validator name.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the stored constraint to use. (Defaults to version 1.)
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A full description of what this constraint configuration does
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of what this constraint constraint should do, example - values between 1 and 100
    """

    config: typing.Optional[typing.Optional[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
