# This file was auto-generated by Fern from our API Definition.

from .data_retention_policy_config import DataRetentionPolicyConfig
from ...commons.types.data_retention_policy_id import DataRetentionPolicyId
import typing_extensions
import datetime as dt
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class DataRetentionPolicy(DataRetentionPolicyConfig):
    """
    A data retention policy belonging to an environment

    Examples
    --------
    import datetime

    from flatfile.data_retention_policies import DataRetentionPolicy

    DataRetentionPolicy(
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
    )
    """

    id: DataRetentionPolicyId
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    Date the policy was created
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    Date the policy was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
