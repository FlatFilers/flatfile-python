# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .action_mode import ActionMode
from .action_message import ActionMessage
from .action_schedule import ActionSchedule
import typing_extensions
from ...core.serialization import FieldMetadata
from .input_form import InputForm
from .action_constraint import ActionConstraint
from .action_mount import ActionMount
from .guide import Guide
from .guardrail import Guardrail
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ActionWithoutLabel(UniversalBaseModel):
    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    **This is deprecated. Use `operation` instead.**
    """

    operation: typing.Optional[str] = pydantic.Field(default=None)
    """
    This will become the job operation that is triggered
    """

    mode: typing.Optional[ActionMode] = pydantic.Field(default=None)
    """
    Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete
    """

    tooltip: typing.Optional[str] = pydantic.Field(default=None)
    """
    A tooltip that appears when hovering the action button
    """

    messages: typing.Optional[typing.List[ActionMessage]] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    **This is deprecated.**
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text that appears in the dialog after the action is clicked.
    """

    schedule: typing.Optional[ActionSchedule] = pydantic.Field(default=None)
    """
    Determines if the action should happen on a regular cadence.
    """

    primary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A primary action will be more visibly present, whether in Sheet or Workbook.
    """

    confirm: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to show a modal to confirm the action
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.
    """

    require_all_valid: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="requireAllValid")] = (
        pydantic.Field(default=None)
    )
    """
    **This is deprecated. Use `constraints` instead.**
    """

    require_selection: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="requireSelection")] = (
        pydantic.Field(default=None)
    )
    """
    **This is deprecated. Use `constraints` instead.**
    """

    input_form: typing_extensions.Annotated[typing.Optional[InputForm], FieldMetadata(alias="inputForm")] = (
        pydantic.Field(default=None)
    )
    """
    Adds an input form for this action after it is clicked.
    """

    constraints: typing.Optional[typing.List[ActionConstraint]] = pydantic.Field(default=None)
    """
    A limitation or restriction on the action.
    """

    mount: typing.Optional[ActionMount] = None
    guide: typing.Optional[Guide] = None
    guardrail: typing.Optional[Guardrail] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
