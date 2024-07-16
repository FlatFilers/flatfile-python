# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.pagination import Pagination
from .prompt import Prompt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PromptsResponse(pydantic.BaseModel):
    """
    import datetime

    from flatfile import Pagination, Prompt, PromptsResponse

    PromptsResponse(
        data=[
            Prompt(
                id="us_pr_YOUR_ID",
                created_by_id="us_usr_YOUR_ID",
                account_id="us_acc_YOUR_ID",
                environment_id="us_env_YOUR_ID",
                space_id="us_sp_YOUR_ID",
                prompt="Combine first name and last name into a new column called Full Name",
                created_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
            )
        ],
        pagination=Pagination(
            current_page=3,
            page_count=50,
            total_count=100,
        ),
    )
    """

    pagination: typing.Optional[Pagination] = None
    data: typing.List[Prompt]

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
