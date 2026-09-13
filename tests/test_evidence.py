from evidence_strategy_skills.schemas import ClaimStatus, EvidenceClaim


def test_supported_claim_preserves_source_references() -> None:
    claim = EvidenceClaim(
        text="Observed behavior is supported by source evidence.",
        status=ClaimStatus.SUPPORTED,
        source_refs=["source-1"],
    )

    assert claim.status is ClaimStatus.SUPPORTED
    assert claim.source_refs == ["source-1"]
