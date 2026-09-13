# Evidence standard

Status: P1 V0 contract, 2026-09-13. These are project design decisions, not
validated findings about skill effectiveness. Applies to the first fixed-packet
experiments and subsequent qualitative market research.

## What must be recoverable

A reviewer must be able to move from a decision-relevant claim to the retained
passage or observation, its origin and context, and the reasoning that connects
them. W3C PROV distinguishes artifacts, their production, and attribution; V0
borrows that separation without implementing its ontology or exchange formats.
[W3C PROV overview, 2013](https://www.w3.org/TR/prov-overview/).

Use a small evidence packet: source records plus claims. A source record is one
retained passage or observation, not necessarily an entire publication. Multiple
passages from one publication may have separate IDs; they are not independent
sources. Research selection and extraction history belongs in the accompanying
research log or experiment manifest, not a knowledge graph.

## Claim states and decision rule

Retain the four names, but make them a **review summary**, not truth values,
probabilities, an ordinal scale, or a complete epistemic taxonomy. Serialized
values remain lowercase, matching the scaffold's `ClaimStatus` enum.

| State | V0 meaning | Required justification |
| --- | --- | --- |
| `SUPPORTED` | Retained evidence directly supports the precisely scoped claim; no reviewed material counterevidence remains unaddressed. | At least one supporting source reference. Attribution and scope must be in the claim text. |
| `INFERRED` | An interpretation extends beyond direct observation, with enough premises to make a qualified argument. | Premise source references and a rationale stating the inferential step and assumptions. |
| `UNRESOLVED` | Evidence needed to answer the question is missing, inaccessible, too weak, or insufficiently scoped. | A rationale naming the missing evidence and what would resolve it. References may be empty. |
| `CONFLICTED` | Material counterevidence challenges the claim, or relevant accounts remain incompatible after checking scope, dates, and definitions. | Counterevidence references and a rationale explaining the conflict and its consequences. Supporting references may be empty. |

Apply in this order: inspect material counterevidence; assess whether the
remaining evidence is sufficient for the claimed scope; distinguish inference
from direct support. A conflict takes precedence over an inference label; retain
the inferential step in its rationale. Missing premises mean UNRESOLVED, not
INFERRED merely because a plausible story can be written.

This changes the scaffold's conflict wording: counterevidence does not require
two equally credible camps or positive support for the original claim. For a
refuted universal claim, preserve it as CONFLICTED with the counterexample and,
where useful, add a separate SUPPORTED narrow correction. Do not call a resolved
false claim merely "uncertain." Superseding a claim must preserve its earlier
version in the research artifact history.

These labels compress two different properties: directness and evidential
adequacy. V0 retains the vocabulary to keep review manageable, while explicit
support/counterevidence links and rationale prevent the label from carrying all
meaning. Add separate axes only if early annotation shows repeatable ambiguity.

## Minimum packet fields

| Record | Fields | Why retained |
| --- | --- | --- |
| Source | `id`, `locator`, `title`, `source_type` | Resolve citations and identify whose evidence is being used. Locator is a direct URL/DOI or a retained local artifact path with a passage/observation locator. |
| Source | `published_at`, `retrieved_at` | Separate the source's date from collection date. Publication date may be null; retain known partial precision as text, never invent a day. |
| Source | `excerpt`, `excerpt_kind`, `context`, `limitations` | Preserve a brief quote or faithful paraphrase, surrounding meaning, and restrictions on what it establishes. |
| Claim | `text`, `status`, `source_refs`, `contradiction_refs`, `rationale` | Recover the assertion, supporting premises, opposing evidence, and interpretation. Rationale is optional only for straightforward SUPPORTED claims. |

Source types: `scholarly`, `official`, `market`, `community`, `runtime`,
`synthetic`. These describe origin/use, not a quality ranking. An inference is
a claim operation, not a source type. A vendor's survey can be `market` with its
sponsorship and recruitment described in context. Synthetic fixtures must never
be counted as observations about real users or products.

Claim text must state relevant population, circumstance, product/version, time,
and attribution; omit dimensions only when immaterial. Split conjunctions whose
parts have different support. Source context includes the publisher or speaker's
role where known, thread or document section, applicable version, and whether
the record is a self-report, measurement, or editorial assertion. Do not infer
private identity or role from a username.

The packet's creator, extraction method, source selection procedure, and packet
revision are recorded once in the research log or
[experiment manifest](evaluation-standard.md#minimum-experiment-record).
Keep quoted text distinct from paraphrase; mark translations and retain the
original short passage when permitted. Search snippets are discovery leads, not
read source evidence. If access fails, log it and narrow the conclusion.

## Review rules

- A source saying X supports "the source reports X"; it may not support X as an
  independently verified event. Vendor documentation establishes documented
  behavior, while a recorded run establishes behavior in that run.
- Inspect the passage for entailment, source interest, scope, age, and alternate
  explanations. A valid URL, quote match, or schema does not perform this review.
- Keep negative and contradictory records even when inconvenient. First check
  whether different versions, dates, tasks, or definitions explain the apparent
  disagreement. Narrow or split the claim if so; document why.
- Do not count copied articles, cross-posts, quotations of one report, or replies
  describing the same incident as independent corroboration. Describe source
  dependence; no universal minimum number of domains establishes truth.
- Absence from a bounded search means "not found in this search." It does not
  establish that a pain, competitor, capability, or market does not exist.
- No automatic confidence score, weighted source score, or average of statuses.
  Review credibility qualitatively against the particular claim.

## Social observation contract

The first unit is a **reported episode in a particular circumstance**. A post
may contain several episodes; several posts may describe one episode. Preserve
this distinction with local observation IDs and group related posts before
describing recurrence. Do not construct cross-platform identity profiles.

Future `market-sentiment-research` must retain these columns in a small table or
document, linked to source IDs. They are documentary fields for now, not new
Python model classes. For each value distinguish directly reported content
from analyst interpretation and use `not reported`, `unclear`, or `not applicable`
instead of treating missing data as zero or false.

| Dimension | Required interpretation boundary |
| --- | --- |
| Source/context | Passage locator, dates, platform/thread, product/runtime/version, author role only if stated, reply context, duplication/related-incident group. |
| Circumstance | Task, trigger, environment, constraints, and desired progress; separate supplied facts from inferred jobs. |
| Pain | Specific obstacle and consequence, not generic positive/negative sentiment. |
| Workaround | What the reporter actually did, versus advice from someone else or an analyst's proposal. |
| Recurrence | Within-reporter frequency and separate independent episodes in the collected corpus; keep the unit and denominator explicit. |
| Intensity | Reported language and behavioral consequences; profanity or upvotes alone are not severity measures. |
| Switching | Distinguish consideration, stated intention, trial, reported completed switch, and directly observed behavior. Preserve destination and obstacles if stated. |
| Time/economic cost | Original units, time window, who estimated or measured it, and whether incurred, projected, or hypothetical. Do not monetize time without a stated assumption. |
| Contradictory cases | Success, acceptable tradeoffs, abandoned workarounds, different circumstances, and evidence against the emerging theme. Link their source IDs. |

The collection log must declare the question, platforms, queries, date/language
limits, ordering or search provider, inclusion/exclusion rules, stopping rule,
retrieval failures, and counts screened/included/deduplicated. Preserve an
exclusion reason per screened record or clearly specified group. Search for
successful and disconfirming cases as well as complaints. AAPOR's disclosure
standard calls for content-analysis units, sampling rules, dates, coding
procedures, and limitations; V0 adapts these reporting principles, not a survey
sampling design. [AAPOR disclosure standards, accessed 2026-09-13](https://aapor.org/standards-and-ethics/disclosure-standards/).

Corpus counts can describe what was collected: "three independently reported
episodes among the twelve included records." They cannot estimate population
prevalence, market size, causality, or willingness to pay. Search rankings,
moderation, access, language, and self-selection leave unknown coverage. A
reported purchase establishes that report in its stated circumstances, not a
demand curve. Interview, usage, purchase, or sampling evidence appropriate to
the decision is the next validation step.

## Worked public-source boundary

On 2026-08-27, a reporter described plugin-hook dependencies disappearing after
cache refresh, with Codex CLI 0.150.0 on Linux and a Bun workaround. The issue
describes a manual dependency install restoring the hook until a later refresh.
This supports "one reporter described this workflow failure," not a verified
current defect across Codex installations. It provides a circumstance, pain,
workaround, and claimed within-workflow recurrence. Intensity beyond the stated
consequence, switching, time cost, and economic cost are not reported in the
passage. Related issue links are leads requiring separate inspection and
deduplication; this single record supplies no contradictory case or independent
recurrence estimate. [Public issue #41177, body/reproduction, accessed 2026-09-13](https://github.com/openai/codex/issues/41177).

This is a source-policy illustration selected during P1, not a market study or
benchmark fixture. No population conclusion follows from it.

## Executable boundary

[schemas.py](../src/evidence_strategy_skills/schemas.py) checks nonempty required
fields, known labels, status-specific reference/rationale requirements, unique
source IDs, and reference resolution inside an `EvidencePacket`. An
`EvidenceClaim` alone cannot check resolution. Packet validation does not fetch
sources, inspect entailment, establish independence, validate study design, or
prove the declared status. Those remain explicit review work.
