from enum import StrEnum

from pydantic import BaseModel, Field


class ClaimStatus(StrEnum):
    SUPPORTED = "supported"
    INFERRED = "inferred"
    UNRESOLVED = "unresolved"
    CONFLICTED = "conflicted"


class EvidenceClaim(BaseModel):
    text: str
    status: ClaimStatus
    source_refs: list[str] = Field(default_factory=list)
