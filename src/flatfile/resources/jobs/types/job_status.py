# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobStatus(str, enum.Enum):
    """
    the status of the job
    ---
    from flatfile import JobStatus

    JobStatus.PLANNING
    """

    CREATED = "created"
    PLANNING = "planning"
    SCHEDULED = "scheduled"
    READY = "ready"
    EXECUTING = "executing"
    COMPLETE = "complete"
    FAILED = "failed"
    CANCELED = "canceled"
    WAITING = "waiting"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        planning: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        executing: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        waiting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.CREATED:
            return created()
        if self is JobStatus.PLANNING:
            return planning()
        if self is JobStatus.SCHEDULED:
            return scheduled()
        if self is JobStatus.READY:
            return ready()
        if self is JobStatus.EXECUTING:
            return executing()
        if self is JobStatus.COMPLETE:
            return complete()
        if self is JobStatus.FAILED:
            return failed()
        if self is JobStatus.CANCELED:
            return canceled()
        if self is JobStatus.WAITING:
            return waiting()
