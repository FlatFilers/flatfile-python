# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...commons.types.commit_id import CommitId
import typing_extensions
from ...commons.types.sheet_id import SheetId
from ...core.serialization import FieldMetadata
import pydantic
import typing
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Commit(UniversalBaseModel):
    """
    A commit version

    Examples
    --------
    import datetime

    from flatfile.commits import Commit

    Commit(
        id="us_vr_YOUR_ID",
        sheet_id="us_sh_YOUR_ID",
        created_by="us_usr_YOUR_ID",
        created_at=datetime.datetime.fromisoformat(
            "2019-08-24 14:15:22+00:00",
        ),
    )
    """

    id: CommitId
    sheet_id: typing_extensions.Annotated[SheetId, FieldMetadata(alias="sheetId")]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy")] = pydantic.Field()
    """
    The actor (user or system) who created the commit
    """

    completed_by: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="completedBy")] = (
        pydantic.Field(default=None)
    )
    """
    The actor (user or system) who completed the commit
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    The time the commit was created
    """

    completed_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="completedAt")] = (
        pydantic.Field(default=None)
    )
    """
    The time the commit was acknowledged
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
