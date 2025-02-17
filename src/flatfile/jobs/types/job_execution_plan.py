# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .edge import Edge
from ...core.serialization import FieldMetadata
from .source_field import SourceField
from .destination_field import DestinationField
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class JobExecutionPlan(UniversalBaseModel):
    """
    The execution plan for a job, for example, for a map job, the execution plan is the mapping of the source sheet to the destination sheet.

    Examples
    --------
    from flatfile.jobs import Edge, JobExecutionPlan, Metadata
    from flatfile.property import Property_String

    JobExecutionPlan(
        field_mapping=[
            Edge(
                source_field=Property_String(
                    key="firstName",
                ),
                destination_field=Property_String(
                    key="firstName",
                    label="First Name",
                ),
                preview=["John", "Suzy", "Joe"],
                metadata=Metadata(
                    certainty="absolute",
                    confidence=1.0,
                    source="exact",
                ),
            ),
            Edge(
                source_field=Property_String(
                    key="lastName",
                ),
                destination_field=Property_String(
                    key="lastName",
                    label="Last Name",
                ),
                preview=["Smith", "Que", "Montana"],
                metadata=Metadata(
                    certainty="absolute",
                    confidence=1.0,
                    source="exact",
                ),
            ),
        ],
        unmapped_source_fields=[],
        unmapped_destination_fields=[],
    )
    """

    field_mapping: typing_extensions.Annotated[typing.List[Edge], FieldMetadata(alias="fieldMapping")]
    unmapped_source_fields: typing_extensions.Annotated[
        typing.List[SourceField], FieldMetadata(alias="unmappedSourceFields")
    ]
    unmapped_destination_fields: typing_extensions.Annotated[
        typing.List[DestinationField], FieldMetadata(alias="unmappedDestinationFields")
    ]
    program_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="programId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
