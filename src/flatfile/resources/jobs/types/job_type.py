# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobType(str, enum.Enum):
    """
    The type of job
    """

    FILE = "file"
    WORKBOOK = "workbook"
    SHEET = "sheet"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        workbook: typing.Callable[[], T_Result],
        sheet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobType.FILE:
            return file()
        if self is JobType.WORKBOOK:
            return workbook()
        if self is JobType.SHEET:
            return sheet()