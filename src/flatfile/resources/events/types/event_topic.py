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
    SPACE_ARCHIVED = "space:archived"
    SPACE_UNARCHIVED = "space:unarchived"
    SPACE_EXPIRED = "space:expired"
    SPACE_GUEST_ADDED = "space:guestAdded"
    SPACE_GUEST_REMOVED = "space:guestRemoved"
    DOCUMENT_CREATED = "document:created"
    DOCUMENT_UPDATED = "document:updated"
    DOCUMENT_DELETED = "document:deleted"
    WORKBOOK_CREATED = "workbook:created"
    WORKBOOK_UPDATED = "workbook:updated"
    WORKBOOK_DELETED = "workbook:deleted"
    WORKBOOK_EXPIRED = "workbook:expired"
    SHEET_CREATED = "sheet:created"
    SHEET_UPDATED = "sheet:updated"
    SHEET_DELETED = "sheet:deleted"
    SHEET_COUNTS_UPDATED = "sheet:counts-updated"
    SNAPSHOT_CREATED = "snapshot:created"
    RECORDS_CREATED = "records:created"
    RECORDS_UPDATED = "records:updated"
    RECORDS_DELETED = "records:deleted"
    FILE_CREATED = "file:created"
    FILE_UPDATED = "file:updated"
    FILE_DELETED = "file:deleted"
    FILE_EXPIRED = "file:expired"
    JOB_CREATED = "job:created"
    JOB_UPDATED = "job:updated"
    JOB_DELETED = "job:deleted"
    JOB_COMPLETED = "job:completed"
    JOB_READY = "job:ready"
    JOB_SCHEDULED = "job:scheduled"
    JOB_OUTCOME_ACKNOWLEDGED = "job:outcome-acknowledged"
    JOB_PARTS_COMPLETED = "job:parts-completed"
    JOB_FAILED = "job:failed"
    PROGRAM_CREATED = "program:created"
    PROGRAM_UPDATED = "program:updated"
    COMMIT_CREATED = "commit:created"
    COMMIT_UPDATED = "commit:updated"
    COMMIT_COMPLETED = "commit:completed"
    LAYER_CREATED = "layer:created"
    SECRET_CREATED = "secret:created"
    SECRET_UPDATED = "secret:updated"
    SECRET_DELETED = "secret:deleted"
    CRON_5_MINUTES = "cron:5-minutes"
    CRON_HOURLY = "cron:hourly"
    CRON_DAILY = "cron:daily"
    CRON_WEEKLY = "cron:weekly"
    ENVIRONMENT_CREATED = "environment:created"
    ENVIRONMENT_UPDATED = "environment:updated"
    ENVIRONMENT_DELETED = "environment:deleted"
    ACTION_CREATED = "action:created"
    ACTION_UPDATED = "action:updated"
    ACTION_DELETED = "action:deleted"
    DATA_CLIP_CREATED = "data-clip:created"
    DATA_CLIP_UPDATED = "data-clip:updated"
    DATA_CLIP_DELETED = "data-clip:deleted"
    DATA_CLIP_COLLABORATOR_UPDATED = "data-clip:collaborator-updated"
    DATA_CLIP_RESOLUTIONS_CREATED = "data-clip:resolutions-created"
    DATA_CLIP_RESOLUTIONS_UPDATED = "data-clip:resolutions-updated"
    DATA_CLIP_RESOLUTIONS_REFRESHED = "data-clip:resolutions-refreshed"

    def visit(
        self,
        agent_created: typing.Callable[[], T_Result],
        agent_updated: typing.Callable[[], T_Result],
        agent_deleted: typing.Callable[[], T_Result],
        space_created: typing.Callable[[], T_Result],
        space_updated: typing.Callable[[], T_Result],
        space_deleted: typing.Callable[[], T_Result],
        space_archived: typing.Callable[[], T_Result],
        space_unarchived: typing.Callable[[], T_Result],
        space_expired: typing.Callable[[], T_Result],
        space_guest_added: typing.Callable[[], T_Result],
        space_guest_removed: typing.Callable[[], T_Result],
        document_created: typing.Callable[[], T_Result],
        document_updated: typing.Callable[[], T_Result],
        document_deleted: typing.Callable[[], T_Result],
        workbook_created: typing.Callable[[], T_Result],
        workbook_updated: typing.Callable[[], T_Result],
        workbook_deleted: typing.Callable[[], T_Result],
        workbook_expired: typing.Callable[[], T_Result],
        sheet_created: typing.Callable[[], T_Result],
        sheet_updated: typing.Callable[[], T_Result],
        sheet_deleted: typing.Callable[[], T_Result],
        sheet_counts_updated: typing.Callable[[], T_Result],
        snapshot_created: typing.Callable[[], T_Result],
        records_created: typing.Callable[[], T_Result],
        records_updated: typing.Callable[[], T_Result],
        records_deleted: typing.Callable[[], T_Result],
        file_created: typing.Callable[[], T_Result],
        file_updated: typing.Callable[[], T_Result],
        file_deleted: typing.Callable[[], T_Result],
        file_expired: typing.Callable[[], T_Result],
        job_created: typing.Callable[[], T_Result],
        job_updated: typing.Callable[[], T_Result],
        job_deleted: typing.Callable[[], T_Result],
        job_completed: typing.Callable[[], T_Result],
        job_ready: typing.Callable[[], T_Result],
        job_scheduled: typing.Callable[[], T_Result],
        job_outcome_acknowledged: typing.Callable[[], T_Result],
        job_parts_completed: typing.Callable[[], T_Result],
        job_failed: typing.Callable[[], T_Result],
        program_created: typing.Callable[[], T_Result],
        program_updated: typing.Callable[[], T_Result],
        commit_created: typing.Callable[[], T_Result],
        commit_updated: typing.Callable[[], T_Result],
        commit_completed: typing.Callable[[], T_Result],
        layer_created: typing.Callable[[], T_Result],
        secret_created: typing.Callable[[], T_Result],
        secret_updated: typing.Callable[[], T_Result],
        secret_deleted: typing.Callable[[], T_Result],
        cron_5_minutes: typing.Callable[[], T_Result],
        cron_hourly: typing.Callable[[], T_Result],
        cron_daily: typing.Callable[[], T_Result],
        cron_weekly: typing.Callable[[], T_Result],
        environment_created: typing.Callable[[], T_Result],
        environment_updated: typing.Callable[[], T_Result],
        environment_deleted: typing.Callable[[], T_Result],
        action_created: typing.Callable[[], T_Result],
        action_updated: typing.Callable[[], T_Result],
        action_deleted: typing.Callable[[], T_Result],
        data_clip_created: typing.Callable[[], T_Result],
        data_clip_updated: typing.Callable[[], T_Result],
        data_clip_deleted: typing.Callable[[], T_Result],
        data_clip_collaborator_updated: typing.Callable[[], T_Result],
        data_clip_resolutions_created: typing.Callable[[], T_Result],
        data_clip_resolutions_updated: typing.Callable[[], T_Result],
        data_clip_resolutions_refreshed: typing.Callable[[], T_Result],
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
        if self is EventTopic.SPACE_ARCHIVED:
            return space_archived()
        if self is EventTopic.SPACE_UNARCHIVED:
            return space_unarchived()
        if self is EventTopic.SPACE_EXPIRED:
            return space_expired()
        if self is EventTopic.SPACE_GUEST_ADDED:
            return space_guest_added()
        if self is EventTopic.SPACE_GUEST_REMOVED:
            return space_guest_removed()
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
        if self is EventTopic.WORKBOOK_EXPIRED:
            return workbook_expired()
        if self is EventTopic.SHEET_CREATED:
            return sheet_created()
        if self is EventTopic.SHEET_UPDATED:
            return sheet_updated()
        if self is EventTopic.SHEET_DELETED:
            return sheet_deleted()
        if self is EventTopic.SHEET_COUNTS_UPDATED:
            return sheet_counts_updated()
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
        if self is EventTopic.FILE_EXPIRED:
            return file_expired()
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
        if self is EventTopic.PROGRAM_CREATED:
            return program_created()
        if self is EventTopic.PROGRAM_UPDATED:
            return program_updated()
        if self is EventTopic.COMMIT_CREATED:
            return commit_created()
        if self is EventTopic.COMMIT_UPDATED:
            return commit_updated()
        if self is EventTopic.COMMIT_COMPLETED:
            return commit_completed()
        if self is EventTopic.LAYER_CREATED:
            return layer_created()
        if self is EventTopic.SECRET_CREATED:
            return secret_created()
        if self is EventTopic.SECRET_UPDATED:
            return secret_updated()
        if self is EventTopic.SECRET_DELETED:
            return secret_deleted()
        if self is EventTopic.CRON_5_MINUTES:
            return cron_5_minutes()
        if self is EventTopic.CRON_HOURLY:
            return cron_hourly()
        if self is EventTopic.CRON_DAILY:
            return cron_daily()
        if self is EventTopic.CRON_WEEKLY:
            return cron_weekly()
        if self is EventTopic.ENVIRONMENT_CREATED:
            return environment_created()
        if self is EventTopic.ENVIRONMENT_UPDATED:
            return environment_updated()
        if self is EventTopic.ENVIRONMENT_DELETED:
            return environment_deleted()
        if self is EventTopic.ACTION_CREATED:
            return action_created()
        if self is EventTopic.ACTION_UPDATED:
            return action_updated()
        if self is EventTopic.ACTION_DELETED:
            return action_deleted()
        if self is EventTopic.DATA_CLIP_CREATED:
            return data_clip_created()
        if self is EventTopic.DATA_CLIP_UPDATED:
            return data_clip_updated()
        if self is EventTopic.DATA_CLIP_DELETED:
            return data_clip_deleted()
        if self is EventTopic.DATA_CLIP_COLLABORATOR_UPDATED:
            return data_clip_collaborator_updated()
        if self is EventTopic.DATA_CLIP_RESOLUTIONS_CREATED:
            return data_clip_resolutions_created()
        if self is EventTopic.DATA_CLIP_RESOLUTIONS_UPDATED:
            return data_clip_resolutions_updated()
        if self is EventTopic.DATA_CLIP_RESOLUTIONS_REFRESHED:
            return data_clip_resolutions_refreshed()
