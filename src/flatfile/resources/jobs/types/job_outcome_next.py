# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .job_outcome_next_download import JobOutcomeNextDownload
from .job_outcome_next_id import JobOutcomeNextId
from .job_outcome_next_snapshot import JobOutcomeNextSnapshot
from .job_outcome_next_url import JobOutcomeNextUrl
from .job_outcome_next_wait import JobOutcomeNextWait


class JobOutcomeNext_Id(JobOutcomeNextId):
    type: typing_extensions.Literal["id"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class JobOutcomeNext_Url(JobOutcomeNextUrl):
    type: typing_extensions.Literal["url"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class JobOutcomeNext_Download(JobOutcomeNextDownload):
    type: typing_extensions.Literal["download"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class JobOutcomeNext_Wait(JobOutcomeNextWait):
    type: typing_extensions.Literal["wait"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class JobOutcomeNext_Snapshot(JobOutcomeNextSnapshot):
    type: typing_extensions.Literal["snapshot"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


"""
from flatfile import JobOutcomeNext_Id

JobOutcomeNext_Id(
    type="id",
    id="us_jb_YOUR_ID",
)
"""
JobOutcomeNext = typing.Union[
    JobOutcomeNext_Id, JobOutcomeNext_Url, JobOutcomeNext_Download, JobOutcomeNext_Wait, JobOutcomeNext_Snapshot
]
