# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Pagination(UniversalBaseModel):
    """
    pagination info

    Examples
    --------
    from flatfile.commons import Pagination

    Pagination(
        current_page=3,
        page_count=50,
        total_count=100,
    )
    """

    current_page: typing_extensions.Annotated[int, FieldMetadata(alias="currentPage")] = pydantic.Field()
    """
    current page of results
    """

    page_count: typing_extensions.Annotated[int, FieldMetadata(alias="pageCount")] = pydantic.Field()
    """
    total number of pages of results
    """

    total_count: typing_extensions.Annotated[int, FieldMetadata(alias="totalCount")] = pydantic.Field()
    """
    total available results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
