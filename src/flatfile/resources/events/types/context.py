# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.account_id import AccountId
from ...commons.types.commit_id import CommitId
from ...commons.types.document_id import DocumentId
from ...commons.types.environment_id import EnvironmentId
from ...commons.types.event_id import EventId
from ...commons.types.file_id import FileId
from ...commons.types.job_id import JobId
from ...commons.types.program_id import ProgramId
from ...commons.types.sheet_id import SheetId
from ...commons.types.snapshot_id import SnapshotId
from ...commons.types.space_id import SpaceId
from ...commons.types.version_id import VersionId
from ...commons.types.workbook_id import WorkbookId
from .action_name import ActionName
from .event_context_slugs import EventContextSlugs
from .sheet_slug import SheetSlug

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Context(pydantic.BaseModel):
    """
    The context of the event
    ---
    from flatfile import Context

    Context(
        account_id="us_acc_YOUR_ID",
        actor_id="us_key_SOME_KEY",
        environment_id="us_env_YOUR_ID",
        space_id="us_sp_YOUR_ID",
        workbook_id="us_wb_YOUR_ID",
    )
    """

    namespaces: typing.Optional[typing.List[str]] = pydantic.Field(description="The namespaces of the event")
    slugs: typing.Optional[EventContextSlugs] = pydantic.Field(description="The slugs of related resources")
    action_name: typing.Optional[ActionName] = pydantic.Field(alias="actionName")
    account_id: AccountId = pydantic.Field(alias="accountId")
    environment_id: EnvironmentId = pydantic.Field(alias="environmentId")
    space_id: typing.Optional[SpaceId] = pydantic.Field(alias="spaceId")
    workbook_id: typing.Optional[WorkbookId] = pydantic.Field(alias="workbookId")
    sheet_id: typing.Optional[SheetId] = pydantic.Field(alias="sheetId")
    sheet_slug: typing.Optional[SheetSlug] = pydantic.Field(alias="sheetSlug")
    snapshot_id: typing.Optional[SnapshotId] = pydantic.Field(alias="snapshotId")
    version_id: typing.Optional[VersionId] = pydantic.Field(
        alias="versionId", description="Deprecated, use `commitId` instead."
    )
    commit_id: typing.Optional[CommitId] = pydantic.Field(alias="commitId")
    job_id: typing.Optional[JobId] = pydantic.Field(alias="jobId")
    program_id: typing.Optional[ProgramId] = pydantic.Field(alias="programId")
    file_id: typing.Optional[FileId] = pydantic.Field(alias="fileId")
    document_id: typing.Optional[DocumentId] = pydantic.Field(alias="documentId")
    preceding_event_id: typing.Optional[EventId] = pydantic.Field(alias="precedingEventId")
    actor_id: typing.Optional[str] = pydantic.Field(alias="actorId", description="Can be a UserId, GuestId, or AgentId")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
