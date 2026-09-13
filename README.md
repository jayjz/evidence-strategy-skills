# Evidence Strategy Skills

Evidence-backed, evaluated, model-portable Agent Skills for business and product strategy.

## Thesis

A useful skill should measurably improve agent behavior, not merely add vocabulary.

Modern models already know frameworks such as:

* Porter's Five Forces;
* Jobs to Be Done;
* value-chain analysis;
* resource-based strategy;
* positioning;
* dynamic capabilities.

The problem is not simply getting a model to recite those frameworks.

The problem is getting an agent to:

```text
research real evidence
↓
preserve provenance
↓
separate support from inference
↓
apply the right analytical lens
↓
challenge its assumptions
↓
produce a calibrated decision
```

and then proving that the skill actually improved the result.

---

## What This Repository Is Building

Initial flagship skills:

```text
market-sentiment-research
customer-job-discovery
market-entry
strategy-red-team
```

These are intentionally decision-oriented rather than framework-oriented.

Frameworks are reusable analytical components.

They are not automatically standalone skills.

---

## Research Model

The project compares configurations such as:

```text
same model/runtime
without skill
```

against:

```text
same model/runtime
with skill
```

and examines dimensions such as:

* activation behavior;
* task effectiveness;
* evidence fidelity;
* unsupported claims;
* analytical correctness;
* uncertainty handling;
* actionability;
* token usage;
* runtime;
* cross-runtime variance.

Not every dimension is objectively measurable.

Evaluation distinguishes deterministic assertions, empirical observations, and rubric judgments.

---

## Evidence Model

Initial claim states are:

```text
SUPPORTED
INFERRED
UNRESOLVED
CONFLICTED
```

`SUPPORTED` means available evidence supports the claim.

It does not mean the claim has been conclusively proven true.

The project avoids unsupported numerical confidence and composite scoring until methodology demonstrates a reason to use them.

---

## Social Research

Public customer and developer discourse is valuable for discovering:

* pain;
* workarounds;
* recurring complaints;
* user language;
* switching behavior;
* circumstances.

It is not automatically representative of an entire market.

The project explicitly distinguishes:

```text
social evidence
```

from:

```text
market prevalence
```

and:

```text
expressed frustration
```

from:

```text
willingness to pay
```

---

## Skill Lifecycle

Skills may progress through:

```text
PROPOSED
↓
EXPERIMENTAL
↓
EVALUATED
↓
STABLE
```

or become:

```text
REJECTED
DEPRECATED
```

A rejected skill is a valid research result.

The goal is not to maximize skill count.

The goal is to identify reusable procedures that produce meaningful, reproducible behavioral improvement.

---

## Project Structure

```text
.
├── AGENTS.md
├── ROADMAP.md
├── ARCHITECTURE.md
│
├── docs/
│   ├── research/
│   ├── design-docs/
│   └── exec-plans/
│
├── skills/
│   ├── market-sentiment-research/
│   ├── customer-job-discovery/
│   ├── market-entry/
│   └── strategy-red-team/
│
├── frameworks/
├── profiles/
├── evals/
├── src/
├── scripts/
└── tests/
```

See:

* `ROADMAP.md` for project phases and research hypotheses;
* `ARCHITECTURE.md` for system boundaries;
* `AGENTS.md` for repository operating rules;
* `docs/index.md` for deeper documentation.

---

## Development

Requires Python 3.12+ and `uv`.

Install dependencies:

```bash
uv sync
```

Run verification:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run python scripts/validate_repo.py
git diff --check
```

The repository uses a `src/` Python package layout and commits `uv.lock` for reproducible environments.

---

## Development Philosophy

The expected workflow is:

```text
inspect
↓
understand
↓
form hypothesis
↓
make smallest justified change
↓
test
↓
evaluate
↓
inspect diff
↓
report evidence
```

For substantial tasks, use bounded execution plans under:

```text
docs/exec-plans/active/
```

Completed plans move to:

```text
docs/exec-plans/completed/
```

---

## Current Status

The project is in the repository and methodology foundation stage.

The initial skill directories are placeholders.

They are intentionally **not yet production skills**.

The immediate sequence is:

```text
repository foundation
↓
evidence/evaluation methodology
↓
minimal evaluation harness
↓
market-sentiment-research V0
↓
first skill-versus-baseline experiment
```

The project should not expand the skill catalog until the first real experiment tests the core thesis.

---

## Non-Goals

This is not intended to become:

* an MBA glossary;
* a prompt dump;
* hundreds of thin framework skills;
* a generic autonomous research platform;
* a benchmark leaderboard without inspectable evidence;
* a model-specific prompt collection.

A skill must earn its complexity.

If a strong base model performs the job just as well without it, that is evidence that the skill may not need to exist.

---

## Long-Term Goal

The long-term goal is a public repository where a user can determine not just:

> What does this skill claim to do?

but:

> What evidence shows that this skill improves this job, on which runtimes, under what conditions, at what cost, and with what known limitations?
