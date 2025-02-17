# This file was auto-generated by Fern from our API Definition.

from .write_secret import WriteSecret
from ...commons.types.secret_id import SecretId
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Secret(WriteSecret):
    """
    The value of a secret

    Examples
    --------
    from flatfile.secrets import Secret

    Secret(
        id="us_sec_YOUR_ID",
        name="My Secret",
        value="Sup3r$ecret\\/alue!",
        environment_id="us_env_YOUR_ID",
        space_id="us_sp_YOUR_ID",
        actor_id="us_usr_YOUR_ID",
    )
    """

    id: SecretId = pydantic.Field()
    """
    The ID of the secret.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
