# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .job_plan import JobPlan

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class JobPlanResponse(pydantic.BaseModel):
    """
    import datetime

    from flatfile import (
        Certainty,
        Edge,
        Job,
        JobExecutionPlan,
        JobMode,
        JobPlan,
        JobPlanResponse,
        JobStatus,
        JobSubject_Resource,
        JobType,
        Metadata,
        Property_String,
        Trigger,
    )

    JobPlanResponse(
        data=JobPlan(
            job=Job(
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
                type=JobType.WORKBOOK,
                operation="submitAction",
                source="us_wb_YOUR_ID",
                destination="us_wb_YOUR_ID",
                trigger=Trigger.IMMEDIATE,
                status=JobStatus.COMPLETE,
                progress=100,
                file_id="us_fl_YOUR_ID",
                mode=JobMode.FOREGROUND,
                input={},
                subject=JobSubject_Resource(
                    type="resource",
                    id="us_wb_YOUR_ID",
                ),
                outcome={
                    "message": "Data was successfully submitted to Webhook.site. Go check it out at https://example.site/example."
                },
                info="Starting job to submit action to webhook.site",
                managed=True,
            ),
            plan=JobExecutionPlan(
                field_mapping=[
                    Edge(
                        source_field=Property_String(
                            type="string",
                            key="firstName",
                        ),
                        destination_field=Property_String(
                            type="string",
                            key="firstName",
                            label="First Name",
                        ),
                        preview=["John", "Suzy", "Joe"],
                        metadata=Metadata(
                            certainty=Certainty.ABSOLUTE,
                            confidence=1.0,
                            source="exact",
                        ),
                    ),
                    Edge(
                        source_field=Property_String(
                            type="string",
                            key="lastName",
                        ),
                        destination_field=Property_String(
                            type="string",
                            key="lastName",
                            label="Last Name",
                        ),
                        preview=["Smith", "Que", "Montana"],
                        metadata=Metadata(
                            certainty=Certainty.ABSOLUTE,
                            confidence=1.0,
                            source="exact",
                        ),
                    ),
                ],
                unmapped_source_fields=[],
                unmapped_destination_fields=[],
            ),
        ),
    )
    """

    data: JobPlan

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
