# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...commons.types.pagination import Pagination
from .agent_log import AgentLog
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GetAgentLogsResponse(UniversalBaseModel):
    """
    Examples
    --------
    from flatfile.agents import AgentLog, GetAgentLogsResponse
    from flatfile.commons import Pagination

    GetAgentLogsResponse(
        pagination=Pagination(
            current_page=3,
            page_count=50,
            total_count=100,
        ),
        data=[
            AgentLog(
                event_id="us_evt_YOUR_ID",
                agent_id="us_ag_YOUR_ID",
                success=True,
                created_at="2022-09-18T00:19:57.007Z",
                completed_at="2022-09-18T00:20:04.007Z",
                log="SUCCESS",
            )
        ],
    )
    """

    pagination: typing.Optional[Pagination] = None
    data: typing.Optional[typing.List[AgentLog]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
