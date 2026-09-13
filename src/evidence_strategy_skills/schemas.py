"""Structural evidence checks; no source retrieval or semantic truth assessment."""

from datetime import date
from enum import StrEnum
from typing import Annotated, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

NonEmptyText = Annotated[str, Field(min_length=1, pattern=r"\S")]


class ClaimStatus(StrEnum):
    SUPPORTED = "supported"
    INFERRED = "inferred"
    UNRESOLVED = "unresolved"
    CONFLICTED = "conflicted"


class EvidenceClaim(BaseModel):
    """A scoped assertion with supporting premises and material counterevidence."""

    model_config = ConfigDict(extra="forbid")

    text: NonEmptyText
    status: ClaimStatus
    source_refs: list[NonEmptyText] = Field(default_factory=list)
    contradiction_refs: list[NonEmptyText] = Field(default_factory=list)
    rationale: NonEmptyText | None = None

    @model_validator(mode="after")
    def check_evidence_requirements(self) -> Self:
        for refs in (self.source_refs, self.contradiction_refs):
            if len(refs) != len(set(refs)):
                raise ValueError("Reference lists must not contain duplicate IDs")
        if set(self.source_refs) & set(self.contradiction_refs):
            raise ValueError("Use distinct passage IDs for support and counterevidence")
        if self.status in (ClaimStatus.SUPPORTED, ClaimStatus.INFERRED) and not self.source_refs:
            raise ValueError("Supported and inferred claims require supporting source references")
        if self.status is not ClaimStatus.SUPPORTED and self.rationale is None:
            raise ValueError("Inferred, unresolved, and conflicted claims require a rationale")
        if self.status is ClaimStatus.CONFLICTED:
            if not self.contradiction_refs:
                raise ValueError("Conflicted claims require counterevidence references")
        elif self.contradiction_refs:
            raise ValueError("Material counterevidence requires conflicted status")
        return self


class EvidenceSource(BaseModel):
    """One retained passage/observation; repeated origins are not independent sources."""

    model_config = ConfigDict(extra="forbid")

    id: NonEmptyText
    locator: NonEmptyText
    title: NonEmptyText
    source_type: Literal["scholarly", "official", "market", "community", "runtime", "synthetic"]
    published_at: NonEmptyText | None
    retrieved_at: date
    excerpt: NonEmptyText
    excerpt_kind: Literal["quote", "paraphrase"]
    context: NonEmptyText
    limitations: NonEmptyText


class EvidencePacket(BaseModel):
    """Resolve claim references within a packet without evaluating their meaning."""

    model_config = ConfigDict(extra="forbid")

    sources: list[EvidenceSource]
    claims: list[EvidenceClaim] = Field(min_length=1)

    @model_validator(mode="after")
    def check_source_references(self) -> Self:
        source_ids = [source.id for source in self.sources]
        known = set(source_ids)
        if len(known) != len(source_ids):
            raise ValueError("Source IDs must be unique within a packet")
        for claim in self.claims:
            missing = (set(claim.source_refs) | set(claim.contradiction_refs)) - known
            if missing:
                raise ValueError(f"Unknown source references: {', '.join(sorted(missing))}")
        return self
