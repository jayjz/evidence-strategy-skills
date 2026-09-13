# Architecture

## Purpose

Evidence Strategy Skills is an applied research and engineering repository for determining whether reusable Agent Skills can improve evidence-grounded strategic reasoning across AI agent runtimes.

The architecture exists to support that experiment.

It is not intended to become a generalized business-intelligence platform.

---

# Core Pipeline

The conceptual workflow is:

```text
user decision / research job
        │
        ▼
research requirements
        │
        ▼
evidence acquisition
        │
        ▼
evidence representation
        │
        ▼
decision-oriented skill
        │
        ├── research protocol
        ├── relevant framework references
        ├── structured schemas
        └── deterministic helpers
        │
        ▼
analysis
        │
        ▼
challenge / falsification
        │
        ▼
decision artifact
        │
        ▼
evaluation
```

Not every skill must implement every stage.

The architecture represents separation of concerns, not a mandatory orchestration engine.

---

# Primary Boundaries

## 1. Skills

Location:

```text
skills/
```

A skill contains reusable procedural knowledge for a concrete user job or strategic decision.

Examples:

```text
market-sentiment-research
customer-job-discovery
market-entry
strategy-red-team
```

Skills should primarily answer:

> What procedure helps an agent perform this job better?

A skill should not exist merely because a named business framework exists.

---

## 2. Framework References

Location:

```text
frameworks/
```

Frameworks contain reusable research and reference material for analytical lenses such as:

* Porter;
* Jobs to Be Done;
* resource-based view;
* dynamic capabilities;
* value chain;
* strategic positioning.

Their presence does not imply standalone skills.

Initially, framework material should remain primarily documentary.

Avoid executable abstraction layers until repeated real implementation needs justify them.

---

## 3. Evidence Representation

Location:

```text
src/evidence_strategy_skills/
```

The evidence layer represents only what is required to preserve and evaluate research claims.

P1 claim summary states:

```text
SUPPORTED
INFERRED
UNRESOLVED
CONFLICTED
```

The evidence layer preserves enough provenance to distinguish:

```text
claim
source
source type
relevant context
support relationship
conflict relationship
inference boundary
```

The project should avoid becoming a generalized knowledge graph.

Complexity must be justified by observed skill requirements.

---

## 4. Evaluation

Location:

```text
evals/
```

The evaluation layer determines whether skills improve behavior.

It should support comparisons such as:

```text
configuration A
vs
configuration B
```

including:

```text
same runtime/model without skill
vs
same runtime/model with skill
```

where the environment is sufficiently controlled and documented.

Evaluation must distinguish:

### Activation

Did the runtime invoke the skill appropriately?

### Effectiveness

Did the skill improve behavior after invocation?

These are separate experimental concerns.

---

## 5. Runtime Capability Profiles

Location:

```text
profiles/
```

Profiles describe observed or documented capabilities of agent runtimes.

Examples may eventually include:

* tool access;
* shell execution;
* filesystem behavior;
* web research;
* explicit skill invocation;
* automatic skill activation;
* subagent support;
* structured output support;
* context behavior.

Profiles must be based on:

* authoritative documentation; and/or
* reproducible observation.

Do not populate profile data from assumption.

Profiles must not duplicate core business logic.

---

## 6. Repository Knowledge

Location:

```text
docs/
```

Repository knowledge is split by purpose.

```text
AGENTS.md
    agent operating rules

ROADMAP.md
    project direction, hypotheses, phases, gates

ARCHITECTURE.md
    durable boundaries and conceptual structure

docs/*.md
    concern-specific standards

docs/design-docs/
    deeper architectural decisions where necessary

docs/exec-plans/active/
    bounded current work

docs/exec-plans/completed/
    preserved implementation history
```

This structure exists to minimize repeated context and large handoff prompts.

---

# Evidence Model

The P1 evidence model stays small: an `EvidencePacket` contains source passages
and claims. A scoped claim might resemble:

```yaml
text: One reporter described a skill-loading failure in their stated environment.
status: supported
source_refs:
  - source-001
contradiction_refs: []
```

The source record retains origin/locator, dates, a short quote or paraphrase,
context and limitations. Claims refer separately to support and counterevidence;
inferred, unresolved and conflicted claims require a rationale. Scope and
attribution belong in claim text. Packet validation checks reference resolution,
not truth, entailment, source independence or the adequacy of a research design.
The exact contract is in [docs/evidence-standard.md](docs/evidence-standard.md).
Social episode annotations and experiment metadata remain documentary until a
real workflow needs executable validation. No general provenance graph is needed.

---

# Evidence Semantics

The states are review summaries, not truth values or an ordinal confidence scale.
`SUPPORTED` means:

> retained evidence directly supports this scoped claim, with no reviewed material counterevidence left unaddressed.

It does not mean:

> the claim is conclusively true.

`INFERRED` means:

> the conclusion goes beyond directly observed evidence but follows from stated reasoning.

`UNRESOLVED` means:

> available evidence is insufficient for a defensible conclusion.

`CONFLICTED` means:

> material counterevidence challenges the claim, or relevant accounts remain incompatible after checking scope, time and definitions.

Conflict does not require equal support for two sides. It takes precedence over
an inference label; the rationale preserves the inference and the contradiction.
Missing essential premises make a claim UNRESOLVED. See the evidence standard
for the state decision rule and treatment of refuted universal claims.

---

# Source Types

The architecture should eventually distinguish at least conceptually between:

```text
scholarly/framework evidence
official product/company evidence
market evidence
customer/community evidence
empirical runtime evidence
synthetic test material
```

Different source types answer different questions.

No universal source ranking should substitute for claim-specific judgment.
Analytical inference is a claim operation over evidence, not an independent
source category.

---

# Social Research Boundary

Public discourse is useful for identifying:

* observed pain;
* language users employ;
* workarounds;
* repeated complaints;
* circumstances;
* switching signals;
* contradictions.

It does not automatically establish:

* representative market prevalence;
* causality;
* willingness to pay;
* market size.

Any future social-research pipeline must preserve this distinction.

---

# Evaluation Architecture

Evaluation results may contain multiple kinds of evidence.

## Deterministic assertions

Examples:

```text
required field exists
citation present
schema valid
trace records verified skill loading
```

## Empirical observations

Examples:

```text
token usage
execution time
tool calls
sources gathered
runtime failure
```

## Rubric judgments

Examples:

```text
strategic coherence
analytical correctness
usefulness
uncertainty handling
```

The system must preserve which class produced a result.

Do not collapse all judgments into a single pseudo-objective score.

---

# Reproducibility Boundary

P1 defines the minimum documentary record in
[docs/evaluation-standard.md](docs/evaluation-standard.md#minimum-experiment-record):
frozen protocol and inputs, actual code/skill revision, model/runtime and visible
configuration, tool/catalog access, paired attempt identity, raw outputs/traces,
usage, load evidence, and grading provenance. Unknown host details remain
explicitly unknown. P2 will encode only what its bounded demonstration consumes.

Activation requests, verified loading, and effectiveness are distinct. Begin
with fresh isolated baseline/treatment sessions over identical fixed evidence;
do not expose the baseline to this repository's methodology through instructions
or installed skills. Live acquisition and cross-runtime behavior are separate
comparisons, with their own confounds and limits.

---

# Portability

The preferred architecture is:

```text
portable skill core
        +
runtime capability observations
        +
evaluation evidence
        +
small adapters where justified
```

rather than:

```text
Codex copy
Claude copy
Gemini copy
Cursor copy
```

Portability is a research hypothesis, not an invariant.

If evidence shows meaningful runtime-specific implementations are required, document the reason before introducing duplication.

---

# Progressive Disclosure

Skill instructions should be small enough to avoid unnecessary context consumption.

Prefer:

```text
SKILL.md
    core procedure

references/
    deeper methodology and research

scripts/
    deterministic helpers

assets/
    reusable non-instruction resources

evals/
    skill-local evaluation definitions
```

Avoid loading entire scholarly or research libraries into every invocation.

---

# Dependency Direction

Prefer conceptual dependency flow such as:

```text
framework references
        ↓
skill

evidence schemas
        ↓
skill/evaluation

skill outputs
        ↓
evaluation
```

Avoid coupling:

```text
evaluation
→ modifying skill behavior during the same run

runtime profile
→ duplicating skill business logic

framework directory
→ owning application orchestration
```

---

# Complexity Rule

Architecture must be driven by demonstrated need.

Do not introduce:

* framework class hierarchies;
* plugin abstraction layers;
* database persistence;
* vector databases;
* web servers;
* queues;
* distributed execution;
* event buses;
* generalized crawling systems;

until a real experiment requires them.

The smallest system capable of falsifying the current hypothesis is preferred.

---

# Initial Flagship Skills

The initial research set is intentionally limited to:

```text
market-sentiment-research
customer-job-discovery
market-entry
strategy-red-team
```

These provide a useful sequence:

```text
observe real problems
↓
understand customer progress
↓
evaluate strategic opportunity
↓
attack the resulting reasoning
```

They should not all be implemented simultaneously.

Each should earn expansion through evaluation.

---

# Initial Experiment Strategy

The first important vertical slice is expected to become:

```text
market-sentiment-research
        ↓
Agent Skills ecosystem research task
        ↓
no-skill baseline
        vs
skill-assisted configuration
        ↓
raw results
        ↓
evaluation
        ↓
methodological review
```

This experiment should drive later architecture.

After it exists, new abstractions should generally respond to observed limitations rather than speculative future scale.

---

# Security Boundary

Skills and helper code must avoid hidden authority.

Do not conceal:

* credential access;
* network downloads;
* executable remote payloads;
* destructive operations;
* filesystem access unrelated to the job.

Prefer:

```text
transparent instructions
inspectable scripts
minimal dependencies
minimal permissions
explicit network behavior
```

Security review is part of skill maturity.

---

# Non-Goals

The architecture is not intended to become:

* an autonomous consulting company;
* a generic business-research platform;
* a massive prompt marketplace;
* a strategy-framework API;
* a general knowledge graph;
* a social-data warehouse;
* a web-scraping service;
* an eval leaderboard optimized for vanity metrics.

The architecture exists to answer:

> Can carefully designed, evidence-backed Agent Skills measurably improve strategic reasoning across modern AI agent environments?
