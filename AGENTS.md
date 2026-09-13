# AGENTS.md

## Mission

Evidence Strategy Skills builds evidence-backed, model-portable Agent Skills for real business and product strategy decisions.

The project measures whether skills improve agent behavior rather than assuming that well-written prompts are useful.

## Read First

Before substantial work, inspect:

1. `ROADMAP.md`
2. `ARCHITECTURE.md`
3. `docs/index.md`
4. the relevant active execution plan, if one exists
5. the relevant skill's `SKILL.md`
6. relevant tests and evals

Do not load every reference document unless the task requires it.

## Source of Truth

Use this precedence when sources conflict:

1. tests and executable validation for current implemented behavior;
2. `ROADMAP.md` for project direction and phase gates;
3. `ARCHITECTURE.md` for durable system boundaries;
4. concern-specific documents under `docs/`;
5. active execution plan for the bounded current task;
6. skill-local documentation.

If documentation and implementation conflict, identify the conflict explicitly.

Do not silently redefine the project.

## Core Invariants

* Evidence before framework.
* Skills represent user jobs and decisions, not merely named frameworks.
* Separate sourced support from inference, unresolved questions, and conflicting evidence.
* Social evidence does not by itself establish market prevalence or willingness to pay.
* Do not fabricate citations, benchmark results, user sentiment, experiments, or test outcomes.
* Keep portable skill logic separate from runtime-specific adaptations where practical.
* Prefer progressive disclosure over large `SKILL.md` files.
* Preserve negative evaluation results.
* Do not weaken tests or evaluation criteria to make a skill appear successful.
* Do not proliferate skills before the flagship methodology is validated.
* Empty scaffold directories do not imply implementation work is required.

## Evidence Language

Initial claim states are:

```text
SUPPORTED
INFERRED
UNRESOLVED
CONFLICTED
```

`SUPPORTED` means available evidence supports a claim.

It does not mean the claim has been proven objectively true.

Do not introduce numerical confidence or composite scoring without explicit methodological justification.

## Skill Design

Use the open Agent Skills structure where practical.

Minimum:

```text
skills/<name>/SKILL.md
```

Additional resources may include:

```text
agents/
references/
scripts/
assets/
evals/
```

Add them only when justified.

Keep:

* scholarly background;
* long methodology;
* extensive examples;
* source catalogs;

out of the primary skill instructions when they can be loaded on demand.

Do not create standalone framework skills merely because a framework exists.

## Evaluation

Always distinguish:

```text
activation behavior
```

from:

```text
skill effectiveness after invocation
```

Evaluation results should identify whether they are:

* deterministic assertions;
* empirical observations;
* model-graded judgments;
* human-reviewed judgments.

Do not present rubric judgments as objective measurements.

When comparing configurations, preserve enough information to understand:

* model/runtime;
* skill version;
* repository commit;
* tool access;
* relevant installed skills;
* reasoning configuration where available;
* benchmark/evaluation configuration.

## Development Workflow

Use:

```text
inspect
→ understand
→ plan
→ smallest justified change
→ focused verification
→ broader verification
→ inspect diff
→ report evidence
```

Before modifying substantial code:

```bash
git status --short --branch
git log -5 --oneline --decorate
```

Search before assuming something does not exist.

Understand callers, tests, invariants, and failure behavior before rewriting components.

## Execution Plans

For substantial work, create or update a bounded plan under:

```text
docs/exec-plans/active/
```

Do not turn `ROADMAP.md` into a detailed task log.

When a plan is complete, move it to:

```text
docs/exec-plans/completed/
```

Do not maintain multiple competing active plans for the same workstream without a clear reason.

## Scope Discipline

Prefer the smallest architecture capable of testing the current hypothesis.

Do not introduce prematurely:

* APIs;
* web applications;
* databases;
* queues;
* vector stores;
* distributed evaluators;
* generalized framework engines;
* plugin marketplaces;
* elaborate runtime adapters.

Do not create abstractions solely because future code might use them.

Evidence of repetition should precede abstraction.

## Frameworks

Framework references may live under `frameworks/`.

Treat them primarily as research/reference material.

Do not create object-oriented framework hierarchies or executable framework abstractions unless repeated implementation requirements justify them.

Frameworks organize evidence.

They do not generate evidence.

## Testing and Verification

Use the repository's current tooling.

Typical verification:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run python scripts/validate_repo.py
git diff --check
```

Use `uv run python`, not a system `python` alias.

Run focused tests before broader verification when appropriate.

Do not claim a command passed unless it actually ran successfully.

If verification cannot run, state exactly why.

## Git Safety

Do not casually use destructive commands such as:

```bash
git reset --hard
git clean -fd
git checkout -- .
git restore .
```

Preserve existing work.

Assume another human or agent may have made valid changes in the current tree.

Inspect before overwriting.

## Research Standards

For canonical business-strategy concepts, prefer:

1. original scholarly publications;
2. authoritative university or research-institution sources;
3. strong primary sources;
4. high-quality secondary sources.

For product/runtime behavior, prefer current official documentation and reproducible tests.

For customer/community pain, direct community evidence is useful but must retain its limitations.

Never convert convenience-sample sentiment into population statistics without defensible evidence.

## Security

Never commit:

* API keys;
* passwords;
* private keys;
* access tokens;
* wallet secrets;
* private credentials;
* unnecessary personal information;
* restricted scraped data.

Scripts must not conceal:

* remote downloads;
* credential reads;
* destructive filesystem actions;
* arbitrary network behavior;
* opaque executable payloads.

Dependencies and capabilities should be proportional to demonstrated project needs.

## Skill Maturity

Skills may be:

```text
PROPOSED
EXPERIMENTAL
EVALUATED
STABLE
REJECTED
DEPRECATED
```

A rejected skill is a valid research result.

Do not retain a skill merely to increase catalog size.

## Completion Standard

Do not report work as complete because files exist.

Report:

1. what changed;
2. why it changed;
3. tests and verification actually run;
4. observed results;
5. remaining risks or assumptions;
6. the smallest justified next step.

Optimize for verifiable improvement, not apparent productivity.
