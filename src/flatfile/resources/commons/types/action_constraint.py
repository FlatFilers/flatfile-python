# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .action_constraint_has_all_valid import ActionConstraintHasAllValid
from .action_constraint_has_column_enabled import ActionConstraintHasColumnEnabled
from .action_constraint_has_data import ActionConstraintHasData
from .action_constraint_has_selection import ActionConstraintHasSelection


class ActionConstraint_HasAllValid(ActionConstraintHasAllValid):
    type: typing.Literal["hasAllValid"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionConstraint_HasSelection(ActionConstraintHasSelection):
    type: typing.Literal["hasSelection"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionConstraint_HasData(ActionConstraintHasData):
    type: typing.Literal["hasData"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionConstraint_HasColumnEnabled(ActionConstraintHasColumnEnabled):
    type: typing.Literal["hasColumnEnabled"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ActionConstraint = typing.Union[
    ActionConstraint_HasAllValid,
    ActionConstraint_HasSelection,
    ActionConstraint_HasData,
    ActionConstraint_HasColumnEnabled,
]
