# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Certainty(str, enum.Enum):
    ABSOLUTE = "absolute"
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"

    def visit(
        self,
        absolute: typing.Callable[[], T_Result],
        strong: typing.Callable[[], T_Result],
        moderate: typing.Callable[[], T_Result],
        weak: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Certainty.ABSOLUTE:
            return absolute()
        if self is Certainty.STRONG:
            return strong()
        if self is Certainty.MODERATE:
            return moderate()
        if self is Certainty.WEAK:
            return weak()