# Evidence Strategy Skills — Roadmap

## Mission

Evidence Strategy Skills is an open repository of evidence-backed, model-portable Agent Skills for business, product, and competitive strategy.

The project does **not** exist to teach language models common business frameworks they already know.

It exists to improve how agents:

* acquire and preserve evidence;
* distinguish sourced claims from inference;
* identify customer jobs and pain;
* reason about competitive structure;
* challenge strategic assumptions;
* handle contradictory or insufficient evidence;
* produce decision-ready recommendations;
* calibrate uncertainty;
* behave across different model and agent runtimes.

The governing thesis is:

> A useful skill should measurably improve agent behavior, not merely add vocabulary.

---

# Product Thesis

Most strategy-oriented AI workflows still resemble:

```text
user question
↓
framework prompt
↓
model prior knowledge
↓
professional-looking analysis
```

Evidence Strategy Skills should instead move toward:

```text
decision
↓
research requirements
↓
source acquisition
↓
evidence normalization
↓
structured analysis
↓
appropriate strategy frameworks
↓
adversarial challenge
↓
calibrated recommendation
↓
evaluation
```

Frameworks are analytical components.

The product is the **decision workflow**.

---

# Research Hypotheses

This project is explicitly testing hypotheses rather than assuming them.

## H1 — Skills can improve strategic reasoning

Procedural Agent Skills can measurably improve representative business-strategy tasks relative to the same model operating without the skill.

## H2 — Evidence-first workflows reduce unsupported claims

Requiring explicit evidence acquisition and provenance reduces unsupported strategic assertions and premature certainty.

## H3 — Meaningful skill logic can remain portable

A useful portion of a strategy skill can remain portable across multiple agent runtimes without maintaining separate copies of the business logic.

## H4 — Runtime differences can be isolated

A meaningful portion of model/runtime variation can be represented through capability observations, adapters, and evaluation rather than duplicated skills.

## H5 — Decision-oriented skills outperform framework wrappers

Skills centered on real user jobs such as market entry, customer discovery, or strategy stress-testing should provide more value than thin wrappers around named frameworks such as SWOT, Porter, or VRIO.

## H6 — Social evidence can improve opportunity discovery

Public customer and developer discourse can contribute useful qualitative evidence when provenance, selection bias, context, and inference boundaries are preserved.

## H7 — Some proposed skills will not be useful

Strong models may already perform some proposed workflows well enough that the skill provides little or no meaningful improvement.

Negative results are valid project results.

These hypotheses may be rejected.

The architecture must not make them true by definition.

---

# Core Principles

## 1. Evidence before framework

Do not begin with:

```text
Porter
JTBD
VRIO
SWOT
```

and search for conclusions to populate.

Prefer:

```text
decision
↓
required evidence
↓
observed evidence
↓
appropriate analytical lens
↓
interpretation
```

Frameworks organize reasoning.

They do not manufacture truth.

---

## 2. Jobs before frameworks

Skills should correspond primarily to real user jobs and strategic decisions.

Prefer:

```text
market-sentiment-research
customer-job-discovery
market-entry
strategy-red-team
moat-audit
strategic-positioning
```

over:

```text
porter-five-forces
jtbd
vrio
swot
bcg-matrix
```

Named frameworks belong primarily in references and analytical procedures.

---

## 3. Evidence status must not overclaim truth

The initial evidence vocabulary should distinguish:

```text
SUPPORTED
INFERRED
UNRESOLVED
CONFLICTED
```

These labels describe the relationship between a claim and available evidence.

`SUPPORTED` does **not** mean:

> objectively proven true.

A source can support a claim while being:

* incomplete;
* biased;
* outdated;
* mistaken;
* self-interested;
* contradicted elsewhere.

Evidence provenance must remain available.

---

## 4. Do not create fake quantitative rigor

Useful observations may include:

* recurrence;
* intensity;
* workaround behavior;
* switching behavior;
* economic cost;
* time cost;
* source diversity.

These must not automatically become an arbitrary composite score.

For example:

```text
pain_score = 8.73
```

is not inherently more rigorous than a structured qualitative assessment.

Numerical scoring should only be introduced when:

* its inputs are meaningfully measurable;
* its semantics are clear;
* its limitations are documented;
* evaluation demonstrates that it adds value.

---

## 5. Measure improvement

A production skill should eventually have representative tests for:

* positive activation;
* negative activation;
* behavior after explicit invocation;
* no-skill baseline;
* adversarial inputs;
* insufficient evidence;
* conflicting evidence;
* failure behavior.

A skill is not mature because its prose looks sophisticated.

---

## 6. Separate activation from skill effectiveness

These are different questions:

```text
Should the runtime invoke this skill?
```

and:

```text
Does the skill help when invoked?
```

Activation depends on:

* skill metadata and description;
* user wording;
* model;
* runtime/harness;
* other installed skills;
* available context.

Behavioral usefulness depends on the skill once it is active.

Evaluation must not collapse both into one score.

---

## 7. Social sentiment is qualitative evidence

Public discourse can support claims such as:

```text
users are reporting this problem
this workaround appears repeatedly
some users express switching behavior
this complaint exists across multiple communities
```

It cannot, without defensible sampling, establish claims such as:

```text
30% of developers experience this problem
this represents the overall market
users will pay $X
the total addressable market is Y
```

Therefore:

```text
social complaint frequency
≠
population prevalence
```

and:

```text
expressed frustration
≠
willingness to pay
```

---

## 8. Preserve provenance

Research outputs should retain enough information to answer:

```text
Where did this claim come from?
When was the source produced?
What kind of source is it?
What exactly does it support?
Does another source contradict it?
```

The project should prefer transparent evidence over polished unsupported synthesis.

---

## 9. Portable core, runtime-aware evaluation

The repository should follow the open Agent Skills model where practical.

Core business logic should remain portable.

Runtime-specific behavior belongs primarily in:

* capability observations;
* adapters where genuinely necessary;
* distribution metadata;
* evaluation configuration.

Avoid maintaining:

```text
market-entry-codex
market-entry-claude
market-entry-gemini
```

unless reproducible evidence demonstrates that separate implementations are justified.

---

## 10. Progressive disclosure

Keep `SKILL.md` focused.

Detailed:

* scholarly research;
* source methodology;
* analytical frameworks;
* examples;
* schemas;
* evaluation guidance;

should live in references or other supporting files when appropriate.

Deterministic operations belong in scripts.

Do not convert every reference into instructions permanently loaded into context.

---

## 11. Security is part of correctness

Skills and supporting scripts must not conceal:

* downloads;
* credential access;
* destructive filesystem behavior;
* secret exfiltration;
* arbitrary remote execution;
* opaque dependencies;
* unnecessary network access.

Scripts should be inspectable.

Capabilities should be proportional to the job.

---

## 12. Empty scaffolding is not implementation scope

The repository contains directories representing likely architectural concerns.

Their existence does **not** imply that agents should populate or abstract them immediately.

Do not fill:

```text
frameworks/
profiles/
registry/
evals/
```

merely because those directories exist.

Implement only what the current phase requires.

---

# Source Hierarchy

Different claims require different evidence.

A general preference hierarchy is:

1. original scholarly publication;
2. authoritative university or research institution;
3. official company/product documentation for claims about that company/product;
4. primary public records and datasets;
5. high-quality practitioner research;
6. reputable secondary analysis;
7. direct user/community evidence;
8. analytical inference.

This is not an absolute ranking.

A Reddit thread may be the correct primary evidence for:

> users in this community are reporting X.

It is not the correct primary evidence for:

> X occurs in 40% of the total market.

Evidence types must be matched to claims.

---

# Evaluation Classes

Not every evaluation should be forced into the same scoring mechanism.

## Deterministic assertions

Examples:

* required field exists;
* source reference exists;
* citation format is valid;
* output conforms to schema;
* runtime recorded metadata;
* a complete runtime trace records whether skill instructions loaded.

## Empirical observations

Examples:

* token usage;
* execution time;
* tool calls;
* activation frequency;
* source count;
* source diversity;
* observed runtime failures.

## Rubric-based judgments

Examples:

* analytical correctness;
* usefulness;
* strategic coherence;
* handling of contradictory evidence;
* recommendation quality;
* uncertainty calibration.

Rubric judgments must identify who or what performed the judgment.

Do not represent rubric scores as deterministic truth.

---

# Evaluation Independence

Avoid circular evaluation where possible.

A weak experiment would be:

```text
Astra writes skill
↓
Astra writes benchmark
↓
Astra writes rubric
↓
Astra grades itself
↓
skill wins
```

V0 does not require academic-grade independent experimentation.

It does require transparency.

Results should distinguish:

```text
deterministic result
model-graded result
human-reviewed result
empirical observation
```

Later evaluation should introduce stronger separation where justified.

---

# Reproducibility Metadata

Benchmark results should eventually preserve enough metadata to interpret them later.

Candidate metadata includes:

```yaml
git_commit:
skill:
skill_version:
runtime:
model:
model_version:
reasoning_effort:
date:
tool_access:
web_access:
installed_skills:
baseline_configuration:
evaluation_configuration:
```

Do not assume the schema is complete.

The evaluation foundation phase should finalize the minimum required form.

A benchmark number without its environment is not considered durable evidence.

---

# Environmental Contamination

A baseline model may already receive:

* repository instructions;
* other skills;
* plugins;
* MCP tools;
* runtime defaults;
* system policies;
* hidden harness behavior.

Therefore:

```text
bare model
```

must never be used casually when the environment is not actually bare.

Experiments should document relevant environmental context.

The goal is comparison between controlled configurations, not marketing language.

---

# Architecture

```text
research evidence
       │
       ▼
evidence representation
       │
       ▼
decision-oriented skill
       │
       ├── research protocol
       ├── scholarly references
       ├── structured schemas
       └── deterministic helpers
       │
       ▼
strategy analysis
       │
       ▼
challenge / falsification
       │
       ▼
decision artifact
       │
       ▼
evaluation
       │
       ├── activation
       ├── effectiveness
       ├── evidence fidelity
       ├── calibration
       ├── cost
       └── runtime variance
```

---

# Repository Architecture

```text
evidence-strategy-skills/
│
├── AGENTS.md
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── pyproject.toml
├── uv.lock
│
├── docs/
│   ├── index.md
│   ├── philosophy.md
│   ├── evidence-standard.md
│   ├── source-policy.md
│   ├── skill-design.md
│   ├── evaluation-standard.md
│   ├── portability.md
│   ├── security-standard.md
│   │
│   ├── research/
│   │   ├── index.md
│   │   ├── strategy-literature.md
│   │   ├── agent-skills-market.md
│   │   └── social-pain-map.md
│   │
│   ├── design-docs/
│   │   └── index.md
│   │
│   └── exec-plans/
│       ├── active/
│       └── completed/
│
├── skills/
│   ├── market-sentiment-research/
│   ├── customer-job-discovery/
│   ├── market-entry/
│   └── strategy-red-team/
│
├── frameworks/
│   ├── porter/
│   ├── jtbd/
│   ├── resource-based-view/
│   ├── dynamic-capabilities/
│   ├── value-chain/
│   └── positioning/
│
├── profiles/
│
├── evals/
│   ├── activation/
│   ├── behavioral/
│   ├── evidence/
│   ├── adversarial/
│   ├── fixtures/
│   └── results/
│
├── src/
│   └── evidence_strategy_skills/
│
├── scripts/
│
├── tests/
│
├── registry/
│
└── .github/
    └── workflows/
```

This topology is a map of likely concerns.

It is not permission to implement every component immediately.

---

# Skill Contract

A mature skill may eventually resemble:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── methodology.md
│   ├── evidence.md
│   └── frameworks.md
├── scripts/
├── assets/
└── evals/
    ├── activation.yaml
    └── behavior.yaml
```

Only `SKILL.md` should be assumed by default.

Additional resources require justification.

---

# Skill Maturity Lifecycle

Skills move through explicit maturity states.

## PROPOSED

A concrete user job and rationale have been identified.

No production behavior is implied.

## EXPERIMENTAL

An implementation exists and can be exercised.

Its usefulness is not yet established.

## EVALUATED

Representative baseline comparisons exist and known limitations have been documented.

This does not imply universal model/runtime support.

## STABLE

Behavior is sufficiently repeatable across declared supported environments for the project to recommend normal use.

## REJECTED

Testing suggests the skill does not provide enough value to justify maintenance, complexity, cost, or activation risk.

Rejected skills are valid research outcomes.

## DEPRECATED

The skill was previously supported but should no longer be used for new work.

---

# Skill Kill Criteria

A proposed or experimental skill should not advance toward stable status if:

* strong base models perform equivalently without it;
* it primarily restates knowledge the model already uses effectively;
* claimed improvements cannot be reproduced;
* gains are too small relative to context, token, latency, or maintenance cost;
* triggering creates unacceptable false activations;
* correct activation requires excessive vendor-specific behavior;
* evidence requirements cannot be satisfied reliably;
* the workflow creates false confidence;
* its outputs cannot be evaluated meaningfully;
* a simpler repository instruction or reference would achieve the same result.

The repository should optimize for:

```text
validated useful behaviors
```

not:

```text
number of skills
```

---

# Phase P0 — Repository Foundation

**Status: IN PROGRESS**

Objectives:

* initialize deterministic Python environment;
* establish concise `AGENTS.md`;
* establish `ROADMAP.md`;
* establish architectural boundaries;
* establish structured documentation;
* establish CI;
* create only minimal evidence schema;
* create initial skill placeholders;
* establish repository validation;
* push a clean baseline to GitHub.

Do not implement production versions of the four flagship skills.

### Gate

A fresh coding agent should be able to determine:

* project mission;
* project hypotheses;
* architecture;
* authoritative documents;
* verification commands;
* security boundaries;
* current phase;
* next bounded task;

without requiring a large external handoff.

---

# Phase P1 — Methodology Foundation

**Status: COMPLETE — written methodology gate, 2026-09-13**

Evidence and limitations: [completed P1 plan](docs/exec-plans/completed/P1-methodology-foundation.md).
The usefulness thesis remains untested. Next is the adversarial methodology
review in the Immediate Sequence; P2 remains NOT STARTED.

Purpose:

Determine what it would mean to claim that a strategy skill is useful.

Research and formalize:

* evidence semantics;
* source hierarchy;
* provenance;
* conflicting evidence;
* inference boundaries;
* social evidence limitations;
* deterministic vs rubric evaluation;
* experiment metadata;
* baseline/treatment isolation;
* activation vs effectiveness;
* model/runtime drift;
* evaluator independence;
* benchmark contamination;
* held-out evaluation strategy.

This phase should be primarily research and design.

Avoid large implementation.

### Gate

The repository has a defensible written answer to:

> How will we know whether a skill improved behavior?

---

# Phase P2 — Minimal Evaluation Harness

**Status: NOT STARTED**

Build the smallest system capable of comparing:

```text
configuration A
vs
configuration B
```

For example:

```text
same model without skill
vs
same model with explicit skill invocation
```

Initial dimensions may include:

* activation precision;
* activation recall;
* task success;
* evidence fidelity;
* unsupported-claim rate;
* analytical correctness;
* uncertainty handling;
* actionability;
* token usage;
* runtime;
* cross-runtime variance.

Not every dimension must be numeric.

Preserve raw observations separately from summaries.

### Gate

At least one deliberately small test workflow demonstrates that the harness can expose a behavioral difference or a lack of one without fabricating certainty.

---

# Phase P3 — Market Sentiment Research

**Status: NOT STARTED**

First flagship skill:

```text
market-sentiment-research
```

Purpose:

Turn messy public discourse into structured qualitative evidence.

Potential sources may include:

* GitHub issues and discussions;
* Reddit;
* Hacker News;
* public product forums;
* public reviews;
* issue trackers;
* public community discussions;
* authoritative documentation feedback channels.

The skill should preserve:

* source;
* date;
* relevant context;
* reported pain;
* user circumstance;
* product/runtime;
* workaround;
* recurrence signal;
* intensity signal;
* switching behavior;
* economic/time-cost evidence;
* contradictory examples;
* inference boundaries.

Avoid reducing discourse to generic positive/negative sentiment.

Avoid inferring market prevalence from convenience samples.

### Initial Dogfood Experiment

Use the skill to research the Agent Skills ecosystem itself.

Compare its output against the same model performing the research without the skill.

### Gate

The project has its first defensible skill-versus-baseline experiment.

After this gate, architectural work should be driven primarily by observed needs from real experiments.

---

# Phase P4 — Customer Job Discovery

**Status: NOT STARTED**

Second flagship skill:

```text
customer-job-discovery
```

Input:

structured customer or market evidence.

Output may include:

* circumstance;
* desired progress;
* functional dimensions;
* social dimensions where supported;
* emotional dimensions where supported;
* current solution;
* competing alternatives;
* friction;
* workaround;
* evidence status;
* unresolved questions.

The skill must derive customer jobs from evidence.

It must not manufacture fictional personas to make the analysis look complete.

### Gate

Representative tasks demonstrate useful improvement over the selected baseline configuration.

---

# Phase P5 — Market Entry

**Status: NOT STARTED**

Third flagship skill:

```text
market-entry
```

Potential analytical components include:

* market definition;
* customer jobs;
* substitutes;
* competitive rivalry;
* buyer concentration;
* supplier dependencies;
* switching costs;
* entry barriers;
* regulation;
* competitive positioning;
* market change;
* unresolved assumptions.

Porter's Five Forces may be used where appropriate.

The framework is not the product.

Expected decision orientation:

```text
ENTER
DO NOT ENTER
VALIDATE FIRST
```

with evidence and uncertainty exposed.

### Gate

The skill demonstrates better evidence-grounded decision reasoning than the defined baseline on representative cases.

---

# Phase P6 — Strategy Red Team

**Status: NOT STARTED**

Fourth flagship skill:

```text
strategy-red-team
```

Purpose:

Attack strategic reasoning rather than improve its presentation.

Look for:

* unsupported assumptions;
* contradictory evidence;
* selection bias;
* confirmation bias;
* weak market definition;
* missing substitutes;
* category errors;
* fake moats;
* unjustified willingness-to-pay assumptions;
* hidden dependencies;
* non-falsifiable claims;
* premature certainty;
* framework misuse.

The skill should be capable of rejecting conclusions produced by other strategy workflows.

### Gate

It finds meaningful flaws that a strong baseline model or first-pass strategy workflow misses often enough to justify its cost.

---

# Phase P7 — Cross-Runtime Evaluation

**Status: NOT STARTED**

Initial environments:

```text
Codex / OpenAI
Claude Code
```

Do not expand prematurely.

Only after useful behavior is established should the project consider:

```text
Gemini CLI
Cursor
other Agent Skills-compatible environments
```

Evaluate separately:

* explicit skill effectiveness;
* automatic activation;
* runtime/tool differences;
* token/context effects;
* failure behavior;
* model-specific variance.

### Gate

At least one flagship skill demonstrates useful behavior in more than one declared runtime, or the project documents a reproducible reason portability fails.

Both outcomes are valuable.

---

# Phase P8 — Strategy Library Expansion

**Status: NOT STARTED**

Only begin after the first flagship skills and evaluation methodology survive real experiments.

Candidate skills include:

```text
competitive-dynamics
strategic-positioning
moat-audit
pricing-and-value-capture
business-model-stress-test
growth-bet-evaluator
strategy-coherence-audit
noncustomer-opportunity
strategy-synthesis
```

Each candidate begins with:

```text
user job
↓
why the base model is insufficient
↓
required evidence
↓
baseline tasks
↓
failure cases
↓
implementation
↓
evaluation
```

Not:

```text
interesting framework
↓
write SKILL.md
```

---

# Phase P9 — Distribution

**Status: NOT STARTED**

Support distribution only after useful behavior is established.

Potential targets include:

* open Agent Skills-compatible installation;
* Codex-compatible packaging;
* other runtime-specific packaging as justified.

The portable skill contract should remain authoritative.

Distribution adapters must not silently fork business logic.

---

# Phase P10 — Public Registry and Benchmarks

**Status: NOT STARTED**

Publish a trustworthy skill catalog containing, where available:

* skill version;
* maturity state;
* supported runtimes;
* evaluation coverage;
* activation observations;
* behavioral observations;
* evidence-quality observations;
* cost observations;
* known limitations;
* security status;
* relevant benchmark metadata.

Avoid leaderboard theater.

Raw evidence should remain inspectable where practical.

---

# Execution Planning

`ROADMAP.md` describes:

> where the project is going and what gates control progression.

It is **not** the detailed implementation plan for every task.

Active work belongs under:

```text
docs/exec-plans/active/
```

Example:

```text
docs/exec-plans/active/P1-methodology-foundation.md
```

When completed, move it to:

```text
docs/exec-plans/completed/
```

The hierarchy is:

```text
AGENTS.md
    operating rules

ROADMAP.md
    strategic direction and gates

ARCHITECTURE.md
    durable boundaries

docs/*
    concern-specific standards

docs/exec-plans/active/*
    bounded current implementation
```

---

# Immediate Sequence

The intended near-term sequence is:

```text
P0 repository foundation
↓
principal-engineer methodology review
↓
P1 evidence/evaluation methodology
↓
adversarial methodology review
↓
P2 minimal evaluator
↓
audit evaluator for false rigor
↓
P3 market-sentiment-research
↓
first real baseline experiment
↓
decide whether the thesis survives contact with data
```

After the first real experiment, avoid further architecture work unless observed evidence justifies it.

---

# Non-Goals

The project should not become:

* an MBA glossary;
* a prompt dump;
* a collection of hundreds of thin skills;
* a generic research agent;
* a generic scraping platform;
* a market-data warehouse;
* a vector-database project without demonstrated need;
* a benchmark leaderboard without methodological rigor;
* a model-specific prompt graveyard;
* a framework inheritance hierarchy;
* an autonomous SaaS platform before the core research thesis is validated.

Do not introduce:

* API servers;
* web applications;
* databases;
* distributed systems;
* elaborate plugin infrastructure;

unless a demonstrated project requirement justifies them.

---

# V0 Success Condition

V0 succeeds when the repository can defensibly demonstrate:

> On representative strategy tasks, at least one flagship skill produces meaningfully better evidence-grounded behavior than the same model/runtime under a controlled baseline configuration, with raw evidence, evaluation method, costs, limitations, and reproducibility metadata preserved.

A stronger subsequent result is:

> Useful portions of that improvement reproduce across more than one agent runtime.

Until those claims are supported, repository size, skill count, stars, and framework coverage are secondary metrics.
