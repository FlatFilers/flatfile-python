# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobOutcomeTrigger(str, enum.Enum):
    """
    Whether a job outcome's effect should be triggered automatically
    """

    MANUAL = "manual"
    AUTOMATIC = "automatic"
    AUTOMATIC_SILENT = "automatic_silent"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        automatic: typing.Callable[[], T_Result],
        automatic_silent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobOutcomeTrigger.MANUAL:
            return manual()
        if self is JobOutcomeTrigger.AUTOMATIC:
            return automatic()
        if self is JobOutcomeTrigger.AUTOMATIC_SILENT:
            return automatic_silent()
