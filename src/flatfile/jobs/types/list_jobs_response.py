# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...commons.types.pagination import Pagination
from .job import Job
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ListJobsResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from flatfile.commons import Pagination
    from flatfile.jobs import (
        EmptyObject,
        Job,
        JobSubject_Resource,
        ListJobsResponse,
    )

    ListJobsResponse(
        pagination=Pagination(
            current_page=3,
            page_count=50,
            total_count=100,
        ),
        data=[
            Job(
                id="us_jb_YOUR_ID",
                created_at=datetime.datetime.fromisoformat(
                    "2023-10-30 20:04:28.556000+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2023-10-30 20:04:32.075000+00:00",
                ),
                started_at=datetime.datetime.fromisoformat(
                    "2023-10-30 20:04:29.453000+00:00",
                ),
                finished_at=datetime.datetime.fromisoformat(
                    "2023-10-30 20:04:32.074000+00:00",
                ),
                environment_id="us_env_YOUR_ID",
                type="workbook",
                operation="submitAction",
                source="us_wb_YOUR_ID",
                destination="us_wb_YOUR_ID",
                config=EmptyObject(),
                trigger="immediate",
                status="complete",
                progress=100,
                file_id="us_fl_YOUR_ID",
                mode="foreground",
                input={},
                subject=JobSubject_Resource(
                    id="us_wb_YOUR_ID",
                ),
                outcome={
                    "message": "Data was successfully submitted to Webhook.site. Go check it out at https://example.site/example."
                },
                info="Starting job to submit action to webhook.site",
                managed=True,
            )
        ],
    )
    """

    pagination: typing.Optional[Pagination] = None
    data: typing.List[Job]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
