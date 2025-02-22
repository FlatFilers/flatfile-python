# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...commons.types.pagination import Pagination
from .detailed_agent_log import DetailedAgentLog
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GetDetailedAgentLogsResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from flatfile.agents import DetailedAgentLog, GetDetailedAgentLogsResponse
    from flatfile.commons import Pagination

    GetDetailedAgentLogsResponse(
        pagination=Pagination(
            current_page=3,
            page_count=50,
            total_count=100,
        ),
        data=[
            DetailedAgentLog(
                event_id="us_evt_YOUR_ID",
                success=True,
                created_at=datetime.datetime.fromisoformat(
                    "2022-09-18 00:19:57.007000+00:00",
                ),
                completed_at=datetime.datetime.fromisoformat(
                    "2022-09-18 00:20:04.007000+00:00",
                ),
                duration=500,
                topic="space:created",
                context={},
                log="SUCCESS",
            )
        ],
    )
    """

    pagination: typing.Optional[Pagination] = None
    data: typing.List[DetailedAgentLog]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
