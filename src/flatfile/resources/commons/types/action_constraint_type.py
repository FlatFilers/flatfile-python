# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActionConstraintType(str, enum.Enum):
    HAS_ALL_VALID = "hasAllValid"
    HAS_SELECTION = "hasSelection"
    HAS_DATA = "hasData"

    def visit(
        self,
        has_all_valid: typing.Callable[[], T_Result],
        has_selection: typing.Callable[[], T_Result],
        has_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionConstraintType.HAS_ALL_VALID:
            return has_all_valid()
        if self is ActionConstraintType.HAS_SELECTION:
            return has_selection()
        if self is ActionConstraintType.HAS_DATA:
            return has_data()
