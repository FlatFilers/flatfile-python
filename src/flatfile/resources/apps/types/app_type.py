# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AppType(str, enum.Enum):
    PORTAL = "PORTAL"
    PROJECTS = "PROJECTS"
    MAPPING = "MAPPING"
    WORKBOOKS = "WORKBOOKS"
    CUSTOM = "CUSTOM"

    def visit(
        self,
        portal: typing.Callable[[], T_Result],
        projects: typing.Callable[[], T_Result],
        mapping: typing.Callable[[], T_Result],
        workbooks: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppType.PORTAL:
            return portal()
        if self is AppType.PROJECTS:
            return projects()
        if self is AppType.MAPPING:
            return mapping()
        if self is AppType.WORKBOOKS:
            return workbooks()
        if self is AppType.CUSTOM:
            return custom()