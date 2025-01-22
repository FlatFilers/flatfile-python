# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PromptTypeEnum(str, enum.Enum):
    AI_ASSIST = "AI_ASSIST"
    CONSTRAINT_GENERATION = "CONSTRAINT_GENERATION"

    def visit(
        self, ai_assist: typing.Callable[[], T_Result], constraint_generation: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PromptTypeEnum.AI_ASSIST:
            return ai_assist()
        if self is PromptTypeEnum.CONSTRAINT_GENERATION:
            return constraint_generation()
