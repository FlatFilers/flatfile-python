# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .boolean_property import BooleanProperty
from .date_property import DateProperty
from .enum_property import EnumProperty
from .number_property import NumberProperty
from .reference_property import ReferenceProperty
from .string_property import StringProperty


class Property_String(StringProperty):
    type: typing_extensions.Literal["string"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Property_Number(NumberProperty):
    type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Property_Boolean(BooleanProperty):
    type: typing_extensions.Literal["boolean"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Property_Date(DateProperty):
    type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Property_Enum(EnumProperty):
    type: typing_extensions.Literal["enum"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Property_Reference(ReferenceProperty):
    type: typing_extensions.Literal["reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


"""
from flatfile import (
    Constraint_Unique,
    Property_String,
    StringConfig,
    StringConfigOptions,
    UniqueConstraintConfig,
)

Property_String(
    type="string",
    key="code",
    label="Product Code",
    description="Unique identifier defining an individual product.",
    constraints=[
        Constraint_Unique(
            type="unique",
            config=UniqueConstraintConfig(
                case_sensitive=False,
            ),
        )
    ],
    config=StringConfig(
        size=StringConfigOptions.TINY,
    ),
)
"""
Property = typing.Union[
    Property_String, Property_Number, Property_Boolean, Property_Date, Property_Enum, Property_Reference
]
