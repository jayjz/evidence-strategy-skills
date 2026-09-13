from datetime import date

import pytest
from pydantic import ValidationError

from evidence_strategy_skills.schemas import (
    ClaimStatus,
    EvidenceClaim,
    EvidencePacket,
    EvidenceSource,
)


def test_supported_claim_preserves_source_references() -> None:
    claim = EvidenceClaim(
        text="Observed behavior is supported by source evidence.",
        status=ClaimStatus.SUPPORTED,
        source_refs=["source-1"],
    )

    assert claim.status is ClaimStatus.SUPPORTED
    assert claim.source_refs == ["source-1"]


def source(source_id: str = "source-1") -> EvidenceSource:
    return EvidenceSource(
        id=source_id,
        locator="synthetic:episode-1#report",
        title="Invented report for schema testing",
        source_type="synthetic",
        published_at=None,
        retrieved_at=date(2026, 9, 13),
        excerpt="The reporter describes repeating a manual setup step.",
        excerpt_kind="paraphrase",
        context="A synthetic single-reporter episode, not collected user evidence.",
        limitations="Does not establish real-world behavior, recurrence, or prevalence.",
    )


def test_packet_round_trip_preserves_attribution_and_inference_boundary() -> None:
    packet = EvidencePacket(
        sources=[source()],
        claims=[
            EvidenceClaim(
                text="In the synthetic episode, the reporter describes a manual setup step.",
                status=ClaimStatus.SUPPORTED,
                source_refs=["source-1"],
            ),
            EvidenceClaim(
                text="The setup step may interrupt the reporter's workflow.",
                status=ClaimStatus.INFERRED,
                source_refs=["source-1"],
                rationale="Assumes setup happens during active work; timing is not reported.",
            ),
        ],
    )
    serialized = packet.model_dump_json()
    assert EvidencePacket.model_validate_json(serialized) == packet
    assert '"status":"supported"' in serialized
    assert packet.sources[0].published_at is None
    assert packet.sources[0].excerpt_kind == "paraphrase"


def test_verbatim_passage_whitespace_is_not_silently_normalized() -> None:
    record = source().model_dump()
    record["excerpt"] = "  indented synthetic code or quoted text\n"
    record["excerpt_kind"] = "quote"
    retained = EvidenceSource.model_validate(record)
    restored = EvidenceSource.model_validate_json(retained.model_dump_json())
    assert restored.excerpt == record["excerpt"]


@pytest.mark.parametrize("status", [ClaimStatus.SUPPORTED, ClaimStatus.INFERRED])
def test_sourced_states_cannot_be_asserted_without_premises(status: ClaimStatus) -> None:
    with pytest.raises(ValidationError, match="require supporting source"):
        EvidenceClaim(text="Some claim", status=status, rationale="A plausible story alone.")


@pytest.mark.parametrize(
    "status", [ClaimStatus.INFERRED, ClaimStatus.UNRESOLVED, ClaimStatus.CONFLICTED]
)
def test_qualified_states_require_an_explanation(status: ClaimStatus) -> None:
    with pytest.raises(ValidationError, match="require a rationale"):
        EvidenceClaim(text="Some claim", status=status, source_refs=["source-1"])


def test_missing_evidence_is_representable_without_a_fake_source() -> None:
    packet = EvidencePacket(
        sources=[],
        claims=[
            EvidenceClaim(
                text="Whether users would pay for automation remains unknown.",
                status=ClaimStatus.UNRESOLVED,
                rationale="No purchase evidence; investigate an appropriately scoped paid trial.",
            )
        ],
    )
    assert packet.claims[0].source_refs == []


def test_counterexample_does_not_require_fabricating_an_opposing_camp() -> None:
    packet = EvidencePacket(
        sources=[source()],
        claims=[
            EvidenceClaim(
                text="No episode in the synthetic packet involves manual setup.",
                status=ClaimStatus.CONFLICTED,
                contradiction_refs=["source-1"],
                rationale="The retained episode is a counterexample to this universal claim.",
            )
        ],
    )
    assert packet.claims[0].source_refs == []
    assert packet.claims[0].contradiction_refs == ["source-1"]


def test_conflict_requires_retained_counterevidence() -> None:
    with pytest.raises(ValidationError, match="require counterevidence"):
        EvidenceClaim(
            text="Some claim",
            status=ClaimStatus.CONFLICTED,
            source_refs=["source-1"],
            rationale="Disagreement asserted without an opposing record.",
        )


@pytest.mark.parametrize("status", [ClaimStatus.SUPPORTED, ClaimStatus.INFERRED])
def test_material_counterevidence_cannot_hide_under_an_affirmative_label(
    status: ClaimStatus,
) -> None:
    with pytest.raises(ValidationError, match="requires conflicted status"):
        EvidenceClaim(
            text="Some claim",
            status=status,
            source_refs=["source-1"],
            contradiction_refs=["source-2"],
            rationale="A material contradiction exists.",
        )


@pytest.mark.parametrize("relationship", ["support", "counterevidence"])
def test_packet_rejects_dangling_references_for_both_relationships(relationship: str) -> None:
    claim = EvidenceClaim(
        text="Some claim",
        status=ClaimStatus.CONFLICTED,
        source_refs=["missing" if relationship == "support" else "source-1"],
        contradiction_refs=["missing" if relationship == "counterevidence" else "source-2"],
        rationale="Sources disagree in the same scope.",
    )
    with pytest.raises(ValidationError, match="Unknown source references: missing"):
        EvidencePacket(sources=[source(), source("source-2")], claims=[claim])


def test_duplicate_source_ids_cannot_make_resolution_ambiguous() -> None:
    with pytest.raises(ValidationError, match="Source IDs must be unique"):
        EvidencePacket(
            sources=[source(), source()],
            claims=[EvidenceClaim(text="Report", status="supported", source_refs=["source-1"])],
        )


def test_repeated_origins_are_allowed_but_not_asserted_independent() -> None:
    packet = EvidencePacket(
        sources=[source(), source("source-2")],
        claims=[
            EvidenceClaim(
                text="The synthetic source reports manual setup.",
                status=ClaimStatus.SUPPORTED,
                source_refs=["source-1", "source-2"],
            )
        ],
    )
    assert packet.sources[0].locator == packet.sources[1].locator


@pytest.mark.parametrize(
    ("support", "opposition", "message"),
    [
        (["source-1", "source-1"], ["source-2"], "duplicate IDs"),
        (["source-1"], ["source-2", "source-2"], "duplicate IDs"),
        (["source-1"], ["source-1"], "distinct passage IDs"),
    ],
)
def test_relationships_cannot_double_count_a_passage(
    support: list[str], opposition: list[str], message: str
) -> None:
    with pytest.raises(ValidationError, match=message):
        EvidenceClaim(
            text="Some claim",
            status=ClaimStatus.CONFLICTED,
            source_refs=support,
            contradiction_refs=opposition,
            rationale="Compare the passages.",
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("id", " "),
        ("locator", ""),
        ("excerpt", "\n"),
        ("context", ""),
        ("limitations", ""),
        ("published_at", ""),
        ("source_type", "inference"),
        ("excerpt_kind", "summary-or-quote"),
        ("retrieved_at", "not-a-date"),
    ],
)
def test_source_rejects_missing_or_ambiguous_provenance(field: str, value: str) -> None:
    record = source().model_dump()
    record[field] = value
    with pytest.raises(ValidationError):
        EvidenceSource.model_validate(record)


def test_misspelled_counterevidence_field_cannot_be_silently_discarded() -> None:
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        EvidenceClaim.model_validate(
            {
                "text": "Some claim",
                "status": "supported",
                "source_refs": ["source-1"],
                "contradictions_refs": ["source-2"],
            }
        )


def test_valid_structure_does_not_certify_entailment_or_source_authenticity() -> None:
    # Deliberately overclaimed: semantic review must reject this, not a URL/schema check.
    packet = EvidencePacket(
        sources=[source()],
        claims=[
            EvidenceClaim(
                text="Every real customer will pay for automation.",
                status=ClaimStatus.SUPPORTED,
                source_refs=["source-1"],
            )
        ],
    )
    assert packet.claims[0].status is ClaimStatus.SUPPORTED
