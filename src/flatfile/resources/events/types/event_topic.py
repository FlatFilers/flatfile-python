# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EventTopic(str, enum.Enum):
    """
    The topic of the event
    ---
    from flatfile import EventTopic

    EventTopic.WORKBOOK_UPDATED
    """

    AGENT_CREATED = "agent:created"
    AGENT_UPDATED = "agent:updated"
    AGENT_DELETED = "agent:deleted"
    SPACE_CREATED = "space:created"
    SPACE_UPDATED = "space:updated"
    SPACE_DELETED = "space:deleted"
    DOCUMENT_CREATED = "document:created"
    DOCUMENT_UPDATED = "document:updated"
    DOCUMENT_DELETED = "document:deleted"
    WORKBOOK_CREATED = "workbook:created"
    WORKBOOK_UPDATED = "workbook:updated"
    WORKBOOK_DELETED = "workbook:deleted"
    SHEET_CREATED = "sheet:created"
    SHEET_UPDATED = "sheet:updated"
    SHEET_DELETED = "sheet:deleted"
    SNAPSHOT_CREATED = "snapshot:created"
    RECORDS_CREATED = "records:created"
    RECORDS_UPDATED = "records:updated"
    RECORDS_DELETED = "records:deleted"
    FILE_CREATED = "file:created"
    FILE_UPDATED = "file:updated"
    FILE_DELETED = "file:deleted"
    JOB_CREATED = "job:created"
    JOB_UPDATED = "job:updated"
    JOB_DELETED = "job:deleted"
    JOB_COMPLETED = "job:completed"
    JOB_READY = "job:ready"
    JOB_SCHEDULED = "job:scheduled"
    JOB_OUTCOME_ACKNOWLEDGED = "job:outcome-acknowledged"
    JOB_PARTS_COMPLETED = "job:parts-completed"
    JOB_FAILED = "job:failed"
    COMMIT_CREATED = "commit:created"
    COMMIT_UPDATED = "commit:updated"
    COMMIT_COMPLETED = "commit:completed"
    LAYER_CREATED = "layer:created"

    def visit(
        self,
        agent_created: typing.Callable[[], T_Result],
        agent_updated: typing.Callable[[], T_Result],
        agent_deleted: typing.Callable[[], T_Result],
        space_created: typing.Callable[[], T_Result],
        space_updated: typing.Callable[[], T_Result],
        space_deleted: typing.Callable[[], T_Result],
        document_created: typing.Callable[[], T_Result],
        document_updated: typing.Callable[[], T_Result],
        document_deleted: typing.Callable[[], T_Result],
        workbook_created: typing.Callable[[], T_Result],
        workbook_updated: typing.Callable[[], T_Result],
        workbook_deleted: typing.Callable[[], T_Result],
        sheet_created: typing.Callable[[], T_Result],
        sheet_updated: typing.Callable[[], T_Result],
        sheet_deleted: typing.Callable[[], T_Result],
        snapshot_created: typing.Callable[[], T_Result],
        records_created: typing.Callable[[], T_Result],
        records_updated: typing.Callable[[], T_Result],
        records_deleted: typing.Callable[[], T_Result],
        file_created: typing.Callable[[], T_Result],
        file_updated: typing.Callable[[], T_Result],
        file_deleted: typing.Callable[[], T_Result],
        job_created: typing.Callable[[], T_Result],
        job_updated: typing.Callable[[], T_Result],
        job_deleted: typing.Callable[[], T_Result],
        job_completed: typing.Callable[[], T_Result],
        job_ready: typing.Callable[[], T_Result],
        job_scheduled: typing.Callable[[], T_Result],
        job_outcome_acknowledged: typing.Callable[[], T_Result],
        job_parts_completed: typing.Callable[[], T_Result],
        job_failed: typing.Callable[[], T_Result],
        commit_created: typing.Callable[[], T_Result],
        commit_updated: typing.Callable[[], T_Result],
        commit_completed: typing.Callable[[], T_Result],
        layer_created: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventTopic.AGENT_CREATED:
            return agent_created()
        if self is EventTopic.AGENT_UPDATED:
            return agent_updated()
        if self is EventTopic.AGENT_DELETED:
            return agent_deleted()
        if self is EventTopic.SPACE_CREATED:
            return space_created()
        if self is EventTopic.SPACE_UPDATED:
            return space_updated()
        if self is EventTopic.SPACE_DELETED:
            return space_deleted()
        if self is EventTopic.DOCUMENT_CREATED:
            return document_created()
        if self is EventTopic.DOCUMENT_UPDATED:
            return document_updated()
        if self is EventTopic.DOCUMENT_DELETED:
            return document_deleted()
        if self is EventTopic.WORKBOOK_CREATED:
            return workbook_created()
        if self is EventTopic.WORKBOOK_UPDATED:
            return workbook_updated()
        if self is EventTopic.WORKBOOK_DELETED:
            return workbook_deleted()
        if self is EventTopic.SHEET_CREATED:
            return sheet_created()
        if self is EventTopic.SHEET_UPDATED:
            return sheet_updated()
        if self is EventTopic.SHEET_DELETED:
            return sheet_deleted()
        if self is EventTopic.SNAPSHOT_CREATED:
            return snapshot_created()
        if self is EventTopic.RECORDS_CREATED:
            return records_created()
        if self is EventTopic.RECORDS_UPDATED:
            return records_updated()
        if self is EventTopic.RECORDS_DELETED:
            return records_deleted()
        if self is EventTopic.FILE_CREATED:
            return file_created()
        if self is EventTopic.FILE_UPDATED:
            return file_updated()
        if self is EventTopic.FILE_DELETED:
            return file_deleted()
        if self is EventTopic.JOB_CREATED:
            return job_created()
        if self is EventTopic.JOB_UPDATED:
            return job_updated()
        if self is EventTopic.JOB_DELETED:
            return job_deleted()
        if self is EventTopic.JOB_COMPLETED:
            return job_completed()
        if self is EventTopic.JOB_READY:
            return job_ready()
        if self is EventTopic.JOB_SCHEDULED:
            return job_scheduled()
        if self is EventTopic.JOB_OUTCOME_ACKNOWLEDGED:
            return job_outcome_acknowledged()
        if self is EventTopic.JOB_PARTS_COMPLETED:
            return job_parts_completed()
        if self is EventTopic.JOB_FAILED:
            return job_failed()
        if self is EventTopic.COMMIT_CREATED:
            return commit_created()
        if self is EventTopic.COMMIT_UPDATED:
            return commit_updated()
        if self is EventTopic.COMMIT_COMPLETED:
            return commit_completed()
        if self is EventTopic.LAYER_CREATED:
            return layer_created()
