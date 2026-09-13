# Skill design

Status: P1 V0 contract, 2026-09-13. All four flagship skills remain PROPOSED.
This standard defines implementation gates; it is not their implementation.

## A skill must earn its procedure

Begin with the decision the user needs, a hypothesized baseline failure, the
evidence needed to address it, and an acceptance card independent of the skill's
prose. Include a case where no skill is needed and one where evidence is
insufficient. Establish how a good baseline could tie or beat the treatment.
Only then write the smallest intervention worth comparing.

For the first sentiment skill, the hypothesized value is preserving situated
pain, workarounds, contradictions and inference boundaries. Whether it improves
those behaviors is unresolved. Framework recall and the number of headings or
source links are not success criteria. A simpler checklist/reference remains a
plausible alternative and should be tested if a package shows gains.

## Primary instructions versus supporting resources

The portable format is defined in [portability.md](portability.md). Keep the
primary instructions short enough to inspect as a procedure. They should state:

- The user job, when to use it, and concrete exclusions/neighboring jobs.
- Required inputs and capabilities, what to do when they are unavailable, and
  the decision artifact the user receives.
- Evidence acquisition/inspection steps, how to retain source relationships,
  and when to distinguish support, inference, unresolved questions, and conflict.
- A stopping rule and failure behavior that preserve limitations rather than
  filling missing evidence with model priors.
- A targeted check for alternative explanations or contrary evidence before
  recommending an action.
- Links to the specific references/helpers needed at each step and the
  conditions under which they should be loaded.

Long methodology, scholarly background, source catalogs, extended examples and
rubrics belong in focused supporting files. Include a script only for repeated
deterministic work or a necessary capability; document its inputs, outputs,
dependencies, side effects and failure modes. No helper needs to execute merely
because a directory exists. Keep evaluator rubrics and held-out answers out of
the distributed skill and generation workspace.

Before any installable release, bundle required procedural references so a copy
outside this repository resolves them. Do not make external parent paths or
this repository's AGENTS.md an undocumented runtime dependency. Preserve
reference provenance and licensing; bundle only what is permitted and needed.

## Activation is part of the public interface

Descriptions identify a task boundary, not advertise general intelligence.
Front-load the actual user job and include exclusions where they prevent
confusion. Do not tune descriptions solely against copied trigger phrases.
Maintain natural positive, neighboring negative, ambiguous, and adversarial
activation cases separately from explicit-invocation behavior cases.

Changing a description, dependency, reference, example or runtime metadata can
change behavior even when the main procedure is unchanged. Version the package
as evaluated, not just SKILL.md. Record runtime controls separately; the
portable instructions should not depend on a vendor's command-expansion,
permission-grant, or subagent semantics.

## Maturity evidence

| State | Evidence required before using the label |
| --- | --- |
| PROPOSED | Concrete job, rationale and testable hypothesis; placeholders qualify only as proposals |
| EXPERIMENTAL | Exercisable bounded procedure, inspectable dependencies, documented failures and baseline protocol |
| EVALUATED | Representative declared comparison completed with raw results, grading class, costs and limitations; can include mixed or negative results |
| STABLE | Fresh-case replication, acceptable activation/cost/failure behavior and security review across the environments actually claimed |
| REJECTED | Preserved evidence or explicit maintenance decision explaining why the procedure does not justify its cost or risk |
| DEPRECATED | Prior supported scope and replacement/removal rationale recorded |

No pass count automatically advances maturity. EVALUATED does not mean it won;
a positive small pilot does not establish STABLE. A negative result may warrant
revision or rejection, and a tie may favor the simpler baseline. P1's written
methodology does not change any skill's maturity.

## Review before an experiment

Check whether the instructions actually change an observable behavior; whether
their evidence requirements are attainable with declared capabilities; whether
they encourage overclaiming or unnecessary actions; and whether the baseline
receives a fair task. Use [evidence-standard.md](evidence-standard.md),
[evaluation-standard.md](evaluation-standard.md), and
[security-standard.md](security-standard.md) on demand. Do not inject all of
these authoring standards into every production skill invocation.
