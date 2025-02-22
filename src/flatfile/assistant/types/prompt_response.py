# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .prompt import Prompt
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class PromptResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from flatfile.assistant import Prompt, PromptResponse

    PromptResponse(
        data=Prompt(
            id="us_pr_YOUR_ID",
            created_by_id="us_usr_YOUR_ID",
            account_id="us_acc_YOUR_ID",
            environment_id="us_env_YOUR_ID",
            space_id="us_sp_YOUR_ID",
            prompt_type="AI_ASSIST",
            prompt="Combine first name and last name into a new column called Full Name",
            created_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
    )
    """

    data: Prompt

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
