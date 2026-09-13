# P1 — Methodology Foundation

Status: COMPLETE — P1 written-methodology gate. Started/completed 2026-09-13.
Baseline: `04ab8d8`. Created under `active/` and archived under `completed/`
after verification, following AGENTS.md. No empirical usefulness gate is claimed.

## Objective and boundary

Answer the P1 gate: how will we know whether a skill improved behavior?
Establish evidence, source, evaluation, skill design, portability, and security
contracts for the first experiments. No production skills, evaluator, runtime
adapters, distribution infrastructure, or expansion of empty scaffolds.

## Inspection and baseline

- Read AGENTS.md, ROADMAP.md, ARCHITECTURE.md, docs/index.md, all six relevant
  standard placeholders, the four PROPOSED skill placeholders, schema, test,
  validator, and project tooling. No existing active plans or eval definitions.
- Working tree clean on `main`; one scaffold commit, also local `origin/main`.
- Existing verification ran before edits: Ruff lint and format (22 files), mypy
  (2 source files), pytest (1 passed), repository validator, and diff whitespace
  check all passed. Initial uv attempts could not write its cache under the
  sandbox; the authorized rerun succeeded.
- P0 still says IN PROGRESS and includes CI; no workflow exists. P1 does not
  silently mark P0 complete or add CI outside its methodology scope.

## Work sequence

1. Research current official runtime/specification guidance and primary
   methodology/strategy sources; keep citations next to supported conclusions.
2. Resolve claim-state ambiguity, minimal provenance, social observation units,
   and explicit limitations. Define the documentary contract before code.
3. Define paired baseline/treatment comparisons, separate activation studies,
   bounded validity mitigations, outcome rules, and minimum metadata.
4. Write the six standards; make only necessary architecture corrections and
   small schema/validation changes that expose methodological mistakes.
5. Run focused then full verification, inspect the full diff, assess every P1
   gate topic, preserve unresolved risks, and archive this plan when complete.

## Acceptance evidence

- Every P1 topic in ROADMAP.md maps to a concrete standard and reviewable rule.
- Study design can report no improvement, regression, or an inconclusive result.
- Schema checks cannot be mistaken for empirical skill effectiveness.
- Research distinguishes documented runtime behavior from tested behavior;
  numerical study-design choices are project decisions, not research findings.
- All four skills remain PROPOSED; no model benchmark is claimed to have run.

## Decisions and results

1. Retained the four state names and existing lowercase serialization, but made
   them scoped review summaries. CONFLICTED now includes a counterexample without
   requiring an affirmative evidential camp. A rationale carries inference and
   material conflict instead of implying that the labels are a confidence scale.
2. Replaced the claim-only scaffold's insufficient provenance with two small
   additional models: EvidenceSource and EvidencePacket. Support and opposition
   resolve to retained passages; original excerpt whitespace survives parsing.
   EvidenceClaim now rejects missing premises/rationales and silently misspelled
   fields. Existing valid construction remains tested. No production consumers
   were found; previously accepted incomplete records can now fail validation.
3. Removed analytical inference from the architecture's source categories; it
   is reasoning over evidence. Added an explicitly synthetic source type so
   fixture observations cannot be mistaken for collected user evidence.
4. Defined separate explicit-effectiveness, activation and end-to-end questions.
   Fixed packets and fresh isolated sessions come first. A conditional loaded
   subset cannot replace all-assigned-attempt analysis. Native load evidence is
   distinguished from a request or a content-injection proxy.
5. Defined a bounded pilot with frozen task cards, held-out handling, repeats,
   dimension-specific grading, costs, all-attempt retention and explicit
   positive/negative/inconclusive decisions. The numeric screen is a conservative
   project rule, not power analysis or a validated measurement instrument.
6. Established source-specific research policy, social episode annotations,
   untrusted-input handling and minimal artifact retention. A dated public issue
   illustrates attribution limits; it is not a market study or benchmark result.
7. Documented current Agent Skills, OpenAI/Codex and Claude Code conventions.
   OpenAI's root plugin manifest and legacy Codex fallback are distribution
   details, separate from portable skill content. No adapter or plugin was built.

## P1 gate coverage

| Roadmap topic | Concrete contract |
| --- | --- |
| Evidence semantics | evidence-standard.md: state meanings, precedence and scope |
| Source hierarchy | source-policy.md: claim-specific source choices and theory boundaries |
| Provenance | evidence-standard.md: minimum packet; schemas.py: reference checks |
| Conflicting evidence | evidence-standard.md: counterevidence and reconciliation rules |
| Inference boundaries | evidence-standard.md: premise/rationale requirement and missing-premise behavior |
| Social evidence limitations | evidence-standard.md: reported episode, selection log and forbidden population claims |
| Deterministic versus rubric evaluation | evaluation-standard.md: four result classes, grader provenance and denominator rules |
| Experiment metadata | evaluation-standard.md: minimum experiment record with field-purpose mapping |
| Baseline/treatment isolation | evaluation-standard.md: common inputs, clean sessions and explicit package differences |
| Activation versus effectiveness | evaluation-standard.md: three separate studies and verified load observations |
| Model/runtime drift | evaluation-standard.md: paired schedule, exposed versions and residual unknowns |
| Evaluator independence | evaluation-standard.md: blinding, source anchors, calibration, human review and role overlap |
| Benchmark contamination | evaluation-standard.md: grouped splits, exposure history and catalog isolation |
| Held-out strategy | evaluation-standard.md: sealed assessment, one assessment per candidate and retirement after feedback |

The standards also cover progressive disclosure, maturity evidence, runtime
portability and security. No separate design document was needed.

## Files changed

- Six requested standards: evidence-standard.md, source-policy.md,
  evaluation-standard.md, skill-design.md, portability.md, security-standard.md.
- docs/index.md links those standards; ARCHITECTURE.md incorporates the material
  evidence/activation/metadata corrections; ROADMAP.md records the P1 gate and
  corrects unqualified deterministic activation wording.
- src/evidence_strategy_skills/schemas.py and tests/test_evidence.py make the
  minimal structural evidence boundary executable.
- This execution plan, created active and archived on completion.

AGENTS.md, dependency files, validator, flagship placeholders and empty
architecture scaffolds were not expanded. No P2 runner was implemented.

## Verification and review

| Command | Baseline | Final implementation |
| --- | --- | --- |
| `uv run ruff check .` | Passed | Passed |
| `uv run ruff format --check .` | Passed, 22 files | Passed, 23 files |
| `uv run mypy src` | Passed, 2 source files | Passed, 2 source files |
| `uv run pytest` | 1 passed | 31 passed |
| `uv run python scripts/validate_repo.py` | repository structure: OK | repository structure: OK |
| `git diff --check` | Passed | Passed |

Focused evidence tests ran before the full suite: initially 30 passed, then 31
after adding verbatim whitespace preservation. An intermediate Ruff check found
one overlong test signature; it was corrected and both lint/format checks passed.
uv required authorized access to its cache because the default sandbox mounted
that location read-only. No failed verification was counted as passed.

Inspected the full diff in concern-specific groups and reviewed the final
schema/wording follow-ups. The tests assert structural behavior; one deliberately
overclaimed but structurally valid packet demonstrates that these checks do not
certify entailment or authentic evidence. No runtime comparison, model grading,
human grading, statistical result or production skill outcome was generated.

## Remaining risks and next task

- This pass's author also designed the protocol and schema tests; the methodology
  has not had an independent adversarial or human research review.
- Claim summarization, assertion segmentation and decision usefulness remain
  judgment-heavy. The default pilot's task count and screening threshold need
  critique and later evidence, not an interpretation as statistical power.
- Hidden prompts, hosted-model drift, stylistic judge cues, prior benchmark
  exposure and small purposive task samples cannot be fully controlled in V0.
- Live source revisions, access and retention restrictions limit exact replay;
  current portability entries are documented behavior, not runtime test results.
- The project thesis remains untested. P0's missing CI remains a separate
  scaffold gap; this pass does not certify P0 as complete.

P1 should be considered complete against its written gate. The single next task
is the roadmap's adversarial methodology review: challenge the state rule,
baseline isolation, pilot decision thresholds, grading validity and metadata
sufficiency before P2 implementation. Recommended model/effort: GPT-6 Astra,
`xhigh`, in a fresh review conversation. This is an engineering allocation
recommendation, not a measured model comparison or independent human validation.
