# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .commit import Commit
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class CommitResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from flatfile.commits import Commit, CommitResponse

    CommitResponse(
        data=Commit(
            id="us_vr_YOUR_ID",
            sheet_id="us_sh_YOUR_ID",
            created_by="us_usr_YOUR_ID",
            created_at=datetime.datetime.fromisoformat(
                "2019-08-24 14:15:22+00:00",
            ),
        ),
    )
    """

    data: Commit

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
