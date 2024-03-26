# generated by datamodel-codegen:
#   filename:  framework_span_attributes.json
#   timestamp: 2024-02-28T05:09:20+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class FrameworkSpanAttributes(BaseModel):
    langtrace_service_name: str = Field(..., alias='langtrace.service.name')
    langtrace_service_type: str = Field(..., alias='langtrace.service.type')
    langtrace_service_version: str = Field(...,
                                           alias='langtrace.service.version')
    langtrace_version: str = Field(..., alias='langtrace.version')
    langchain_task_name: Optional[str] = Field(
        None, alias='langchain.task.name')
    langchain_inputs: Optional[str] = Field(None, alias='langchain.inputs')
    langchain_outputs: Optional[str] = Field(None, alias='langchain.outputs')
    llamaindex_task_name: Optional[str] = Field(
        None, alias='llamaindex.task.name')
    llamaindex_inputs: Optional[str] = Field(None, alias='llamaindex.inputs')
    llamaindex_outputs: Optional[str] = Field(None, alias='llamaindex.outputs')