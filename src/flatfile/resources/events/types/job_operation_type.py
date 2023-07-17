# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobOperationType(str, enum.Enum):
    EXTRACT = "EXTRACT"
    MAP = "MAP"

    def visit(self, extract: typing.Callable[[], T_Result], map: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobOperationType.EXTRACT:
            return extract()
        if self is JobOperationType.MAP:
            return map()