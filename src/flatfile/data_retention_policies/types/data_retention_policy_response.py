# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .data_retention_policy import DataRetentionPolicy
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class DataRetentionPolicyResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from flatfile.data_retention_policies import (
        DataRetentionPolicy,
        DataRetentionPolicyResponse,
    )

    DataRetentionPolicyResponse(
        data=DataRetentionPolicy(
            id="us_drp_YOUR_ID",
            environment_id="us_env_YOUR_ID",
            created_at=datetime.datetime.fromisoformat(
                "2023-11-15 19:31:33.015000+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2023-11-15 19:31:33.015000+00:00",
            ),
            type="lastActivity",
            period=5,
        ),
    )
    """

    data: DataRetentionPolicy

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
