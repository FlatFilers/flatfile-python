# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .generic_event import GenericEvent


class Event_AgentCreated(GenericEvent):
    topic: typing_extensions.Literal["agent:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_AgentUpdated(GenericEvent):
    topic: typing_extensions.Literal["agent:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_AgentDeleted(GenericEvent):
    topic: typing_extensions.Literal["agent:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SpaceCreated(GenericEvent):
    topic: typing_extensions.Literal["space:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SpaceUpdated(GenericEvent):
    topic: typing_extensions.Literal["space:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SpaceDeleted(GenericEvent):
    topic: typing_extensions.Literal["space:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SpaceExpired(GenericEvent):
    topic: typing_extensions.Literal["space:expired"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DocumentCreated(GenericEvent):
    topic: typing_extensions.Literal["document:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DocumentUpdated(GenericEvent):
    topic: typing_extensions.Literal["document:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_DocumentDeleted(GenericEvent):
    topic: typing_extensions.Literal["document:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_WorkbookCreated(GenericEvent):
    topic: typing_extensions.Literal["workbook:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_WorkbookUpdated(GenericEvent):
    topic: typing_extensions.Literal["workbook:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_WorkbookDeleted(GenericEvent):
    topic: typing_extensions.Literal["workbook:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_WorkbookExpired(GenericEvent):
    topic: typing_extensions.Literal["workbook:expired"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SheetCreated(GenericEvent):
    topic: typing_extensions.Literal["sheet:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SheetUpdated(GenericEvent):
    topic: typing_extensions.Literal["sheet:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SheetDeleted(GenericEvent):
    topic: typing_extensions.Literal["sheet:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_SnapshotCreated(GenericEvent):
    topic: typing_extensions.Literal["snapshot:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_RecordsCreated(GenericEvent):
    topic: typing_extensions.Literal["records:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_RecordsUpdated(GenericEvent):
    topic: typing_extensions.Literal["records:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_RecordsDeleted(GenericEvent):
    topic: typing_extensions.Literal["records:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_FileCreated(GenericEvent):
    topic: typing_extensions.Literal["file:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_FileUpdated(GenericEvent):
    topic: typing_extensions.Literal["file:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_FileDeleted(GenericEvent):
    topic: typing_extensions.Literal["file:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_FileExpired(GenericEvent):
    topic: typing_extensions.Literal["file:expired"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobCreated(GenericEvent):
    topic: typing_extensions.Literal["job:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobUpdated(GenericEvent):
    topic: typing_extensions.Literal["job:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobDeleted(GenericEvent):
    topic: typing_extensions.Literal["job:deleted"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobFailed(GenericEvent):
    topic: typing_extensions.Literal["job:failed"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobCompleted(GenericEvent):
    topic: typing_extensions.Literal["job:completed"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobReady(GenericEvent):
    topic: typing_extensions.Literal["job:ready"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobScheduled(GenericEvent):
    topic: typing_extensions.Literal["job:scheduled"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobOutcomeAcknowledged(GenericEvent):
    topic: typing_extensions.Literal["job:outcome-acknowledged"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_JobPartsCompleted(GenericEvent):
    topic: typing_extensions.Literal["job:parts-completed"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_CommitCreated(GenericEvent):
    topic: typing_extensions.Literal["commit:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_CommitUpdated(GenericEvent):
    topic: typing_extensions.Literal["commit:updated"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_CommitCompleted(GenericEvent):
    topic: typing_extensions.Literal["commit:completed"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class Event_LayerCreated(GenericEvent):
    topic: typing_extensions.Literal["layer:created"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


"""
import datetime

from flatfile import Context, Domain, Event_WorkbookUpdated, Origin

Event_WorkbookUpdated(
    topic="workbook:updated",
    id="us_evt_YOUR_ID",
    created_at=datetime.datetime.fromisoformat(
        "2023-11-07 20:46:04.300000+00:00",
    ),
    payload={"recordsAdded": 100},
    domain=Domain.WORKBOOK,
    context=Context(
        account_id="us_acc_YOUR_ID",
        actor_id="us_key_SOME_KEY",
        environment_id="us_env_YOUR_ID",
        space_id="us_sp_YOUR_ID",
        workbook_id="us_wb_YOUR_ID",
    ),
    callback_url="",
    data_url="",
    namespaces=["workbook"],
    origin=Origin(
        id="us_wb_YOUR_ID",
    ),
)
"""
Event = typing.Union[
    Event_AgentCreated,
    Event_AgentUpdated,
    Event_AgentDeleted,
    Event_SpaceCreated,
    Event_SpaceUpdated,
    Event_SpaceDeleted,
    Event_SpaceExpired,
    Event_DocumentCreated,
    Event_DocumentUpdated,
    Event_DocumentDeleted,
    Event_WorkbookCreated,
    Event_WorkbookUpdated,
    Event_WorkbookDeleted,
    Event_WorkbookExpired,
    Event_SheetCreated,
    Event_SheetUpdated,
    Event_SheetDeleted,
    Event_SnapshotCreated,
    Event_RecordsCreated,
    Event_RecordsUpdated,
    Event_RecordsDeleted,
    Event_FileCreated,
    Event_FileUpdated,
    Event_FileDeleted,
    Event_FileExpired,
    Event_JobCreated,
    Event_JobUpdated,
    Event_JobDeleted,
    Event_JobFailed,
    Event_JobCompleted,
    Event_JobReady,
    Event_JobScheduled,
    Event_JobOutcomeAcknowledged,
    Event_JobPartsCompleted,
    Event_CommitCreated,
    Event_CommitUpdated,
    Event_CommitCompleted,
    Event_LayerCreated,
]
