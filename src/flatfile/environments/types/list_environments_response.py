# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .environment import Environment
from ...commons.types.pagination import Pagination
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ListEnvironmentsResponse(UniversalBaseModel):
    """
    Examples
    --------
    from flatfile.environments import Environment, ListEnvironmentsResponse

    ListEnvironmentsResponse(
        data=[
            Environment(
                id="us_env_YOUR_ID",
                account_id="us_acc_YOUR_ID",
                name="dev",
                is_prod=False,
                guest_authentication=["magic_link"],
                features={},
                metadata={},
                namespaces=["default"],
            )
        ],
    )
    """

    data: typing.List[Environment]
    pagination: typing.Optional[Pagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
