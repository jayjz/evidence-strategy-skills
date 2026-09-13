# Evaluation standard

Status: P1 V0 contract, 2026-09-13. No skill comparison has been run. Numerical
design choices below are bounded project screening rules, not estimated power,
validated thresholds, or claims from the literature. P2 implements a smaller
harness demonstration; P3 supplies the first real skill experiment.

## The claim an experiment may earn

Report whether adding a particular version of a skill changed specified
behaviors for a declared task set, model, runtime, and resource budget. Require
recoverable raw outputs, failures, grading evidence, costs, and a frozen analysis
rule. Vocabulary, number of citations, compliance with the skill's preferred
headings, or an attractive report is insufficient evidence of useful change.

OpenAI recommends task-specific evals, representative and adversarial examples,
and calibration against human judgments. These inform V0's design, but they do
not independently establish that this benchmark measures strategy quality.
[OpenAI evaluation best practices, accessed 2026-09-13](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## Three questions, separate studies

| Study | Comparison/observation | Claim allowed |
| --- | --- | --- |
| Explicit effectiveness | Same model/runtime, task and evidence; target skill absent versus explicitly loaded | Incremental effect of the loaded package under these conditions, conditional on verified delivery |
| Activation | Target installed; naturally worded positive, negative, ambiguous, and adversarial prompts; inspect loading traces | Discovery/invocation behavior in this catalog and context |
| End-to-end usefulness | Skill unavailable versus available for natural discovery, including misses and false activations | Combined installation effect; neither activation nor conditional effectiveness in isolation |

Do explicit effectiveness first. Do not discard invocation failures and then
claim end-to-end success. Delivery failures stay in the run ledger. Report all
assigned attempts and a separate conditional analysis of verified-loaded runs;
if delivery is uncertain, conditional effectiveness is not established.
The conditional subset may select easier cases and cannot replace the analysis
of all assigned attempts.

An explicit request is not proof that instructions entered context. Record the
invocation request separately from observed loading: `loaded`, `not_loaded`, or
`unknown`, with the trace locator and observation method. Only a positive load
event or visible instruction delivery
establishes `loaded`; absence establishes `not_loaded` only with complete load
telemetry. Self-report or distinctive output phrasing is not sufficient.

## Baseline/treatment isolation

1. Freeze the task instructions and evidence packet once. Both arms receive
   identical substantive requests, required decision artifact, and evidence.
   Baseline receives no target skill name, description, body, references, or
   examples. Do not cripple the baseline's normal reasoning or tools.
2. Start fresh sessions in separate clean working directories with matching
   configuration. Do not run the study inside this authoring conversation or
   give the baseline access to this repository's methodology through AGENTS.md,
   search, parent directories, memory, other skills, plugins, or prior outputs.
   Use an isolated experiment workspace, not merely a new Git branch.
3. Keep model identifier/snapshot, runtime build, visible system/developer
   instructions, reasoning and generation settings, tools, permissions, evidence
   order, common output requirements, and resource ceilings equal. Explicitly
   list unavoidable differences. Hidden host instructions are `unknown`, never
   represented as empty or as a known identical prompt.
4. Treatment receives the exact frozen skill package. Prefer native explicit
   invocation with recorded expansion. If unavailable, inject the identical
   body at a documented message role and position and call this an
   **instruction-injection proxy**. It tests content, not native skill loading.
   Record invocation text as part of the treatment difference.
5. Ensure the treatment's added context leaves room for the common evidence and
   output budget. Record truncation/compaction; if source material is displaced,
   the pair cannot support the controlled reasoning claim. Keep the failure in
   the ledger, correct the design, and rerun both arms as a new revision.
6. Run paired attempts near each other, randomizing A/B order within task and
   repetition with a saved schedule. Keep source ordering identical within a
   pair. Never copy the first arm's answer or acquired evidence into the second.

The primary effect includes the skill's extra instructions, context, resource
use, and any bundled knowledge. It does not isolate procedural logic from
information quantity or extra compute. Measure these costs. If improvement
appears, the smallest follow-up is a common-information/reference-only or short
checklist ablation to test whether a simpler intervention suffices. Token-matched
nonsense is not a neutral placebo. Do not require a factorial study in V0.

Use fixed, human-inspectable evidence packets first with web access off for both
arms. This tests extraction and reasoning over supplied evidence, not acquisition.
A later live-web study uses equal access and budgets and preserves actual
queries/results. Divergent retrieval is part of that workflow's effect; changing
search rankings remains a limitation. Do not pool fixed-packet and live-web runs.

## Tasks, separation, and a bounded pilot

Before implementing or tuning a skill, define task families from the user job
and credible failure consequences. Use ordinary tasks a strong baseline might
already solve, not only traps tailored to the procedure. Synthetic examples are
useful diagnostic fixtures but must be labeled and paired later with permissioned
real-world material before claiming external usefulness.

For the first P3 screening study, default to six development cases and six
held-out cases, with three attempts per arm per case. The held-out set should
cover: straightforward extraction; ambiguous circumstances; insufficient
evidence; contradictory or version-dependent reports; duplicated/promotional
material; and a misleading prevalence/payment request or source injection.
Include different domains or circumstances across the split. Similar variants of
one source/thread stay in one split. This is 72 planned generations including
development, not 72 independent tasks. P2's harness smoke demonstration may use
two synthetic cases and fewer attempts and must not claim skill effectiveness.

A human custodian or a separately scoped author without access to the skill
implementation prepares held-out tasks and grading anchors from the job. Freeze
their manifest/hash before development; keep sealed content outside the coding
agent's readable workspace. The implementer may know categories, not prompts,
answers, or held-out feedback. If separation is unavailable, label the run
exploratory and the author exposure explicitly. A file named `heldout` in a
readable checkout does not establish blindness.

Use development cases for rubric calibration and debugging. Open the held-out
set once per frozen candidate/protocol. Once feedback is used to revise the
skill, that set becomes development/regression material. Keep old results and
acquire fresh cases for a new generalization claim. Record every candidate and
test exposure, including failed runs and prompt-only revisions. Publish the
sealed fixtures after the evaluation when rights permit; published cases are
regression tests for subsequent candidates, not perpetually unseen evidence.

Repeated adaptive use of data can invalidate ordinary validation conclusions;
the reusable-holdout literature motivates separating tuning and assessment.
V0 uses a procedural freeze, not differential privacy or the statistical
guarantees of that literature. [Dwork et al., 2015](https://arxiv.org/abs/1411.2664).

## Measures and who produced them

Every result row retains its class, definition, raw input/output locator,
evaluator identity/version when applicable, value or judgment, and explanation.
A number calculated from rubric labels remains based on judgments.

| Class | Examples and permitted interpretation |
| --- | --- |
| `deterministic_assertion` | Schema validity, reference resolution, exact extract match, a trace event matching the runtime's load definition. These check structure or instrumented events, not semantic truth. |
| `empirical_observation` | Recorded tool calls, tokens, time, failures, activation counts. Counting can be deterministic while the underlying observed process is stochastic. |
| `model_graded_judgment` | Entailment, unsupported assertions, handling conflict, actionability, task pass/fail judged by a model. Preserve prompt, model/settings, output, and source-based rationale. |
| `human_reviewed_judgment` | The same semantic questions reviewed by a person; preserve reviewer ID/role, rubric, initial decision, and any adjudication. Human review is fallible. |

For activation, prelabel natural prompts as should-load, should-not-load, or
ambiguous before seeing behavior. Do not write positives by copying the skill
description or inserting its name. Use overlapping skills as declared distractors
where relevant. Include quoted skill names in irrelevant source text as negative
cases. Report TP/FP/FN/TN and unknown telemetry counts, precision
`TP/(TP+FP)` and recall `TP/(TP+FN)` only when denominators are nonzero; use
`undefined` otherwise. Report ambiguous cases and telemetry coverage separately.
Unknowns cannot be silently converted into negatives; incomplete coverage limits
the rates to observed cases. User intent labels are judgments even when trace
matching is deterministic. Explicit invocation tests do not estimate recall.

## Effectiveness rubric and denominators

Before outputs exist, give every task a short answer-independent acceptance
card: required decision, relevant source passages, essential observations,
acceptable interpretations, material counterevidence, unsupported conclusions
to avoid, and consequences of a mistake. Multiple valid answers are allowed.
Both arms receive the same external output requirements; graders do not reward
the treatment for imitating SKILL.md or using exact status words unless the
user's job explicitly needs that serialization.

Default dimensions, kept separate:

- **Evidence fidelity:** Does each material factual assertion match its cited
  passage and scope? Are quotes, source identity, and self-report attribution
  preserved? Record each error with the assertion and passage.
- **Coverage:** Are the predeclared essential observations and contrary cases
  addressed? A shorter answer that avoids all substantive claims is not success.
- **Inference/uncertainty:** Are missing premises, alternatives, and unresolved
  questions exposed? Does a recommendation exceed what the evidence supports?
- **Decision usefulness:** Does the output answer the actual decision or identify
  the specific next evidence/action needed, with its reason? More framework
  terminology alone earns no credit.
- **Cost/failure:** Record total generation/tool usage, elapsed time and errors,
  including unsuccessful attempts. Grading costs are separate from task costs.

For an optional unsupported-claim rate, reviewers segment the complete answer
into distinct externally checkable assertions, separating compound claims and
deduplicating repeats by stated rules. Unsupported means asserted as established
without adequate available support, including misquotation and overgeneralization;
clearly marked hypotheses and conditional recommendations are reviewed under
inference instead. Publish the claim inventory, unsupported numerator, total
checkable denominator, and coverage beside the fraction. Zero assertions gives
`undefined`, not zero error. Report per-task values first; pooling all claims
overweights verbose outputs. This rate is judgment-derived, not objective truth.

Grade each task attempt `pass`, `fail`, or `unjudgeable` against its acceptance
card, with dimension-level reasons. Fabricated sources/quotes, population or
payment claims from convenience samples, suppressing decisive counterevidence,
and following source instructions that redirect the task or disclose protected
data are critical failures for the first sentiment experiment. A valid structure
with any such failure does not pass. Do not convert these dimensions into a weighted
composite score or claim calibrated confidence from status-label frequency.

## Judges and independence

Use a grader outside the generation conversation. Hide arm, skill, and generator
identity; provide the task, evidence, and acceptance card, not the skill's prose.
Prefer a different model family from the author/generator for model grading,
while recognizing that shared training and style preferences remain. If only
one model is available, disclose that and limit conclusions to exploratory
model-graded observations until human review occurs.

LLM-judge research documents position, verbosity, and self-enhancement bias;
reported judge/human agreement on chat benchmarks does not validate strategic
reasoning grades here. [Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
A more recent study also reports style-sensitive judgments and heterogeneous
responses to debiasing. We use its current warning against a universal judge
recipe, not its reported numerical performance as an estimate for this project.
[Soumik, 2026, version 2](https://arxiv.org/abs/2604.23178v2).

Calibrate the rubric on development outputs with human labels before assessment.
For pairwise judgments, present both A/B and B/A order and retain disagreement;
do not reroll until one arm wins. Score individual acceptance criteria before
overall preference. Use identical output length limits, but do not truncate or
rewrite answers to blind them: that could change their meaning. Style may reveal
the arm despite blinding. Include at least one content-equivalent formatting
control during grader calibration; preference there diagnoses the grader, not
the skill. Treat instructions embedded in outputs as untrusted text.

For the small default held-out set, a human reviews all 36 outputs against the
evidence, blinded where feasible; preserve initial model and human decisions
separately. A second reviewer adjudicates decisive disagreements when available.
Otherwise preserve the disputed judgment and show whether it changes the study
conclusion. No human review means no claim of human-reviewed improvement. List
author, task designer, rubric designer, generator, and grader roles and overlaps;
another invocation of the same agent is not independent authorship.

## Analysis and decision before seeing results

Freeze the primary task-pass comparison, guardrails, budgets, repetition count,
stopping rule, and exclusions in the protocol. Three repetitions are a cheap
way to expose some instability, not a guarantee of repeatability. Research on
benchmark variance motivates accounting for variation beyond a single run; its
ML training results do not quantify the variance of our agent experiment.
[Bouthillier et al., 2021](https://arxiv.org/abs/2103.03098).

Default screening rule: a task meets acceptance when at least two of its three
attempts pass; publish all attempts so this summary cannot hide failures.
Promising local evidence requires treatment to turn at least two held-out tasks
from baseline non-acceptance to acceptance, no task to move the opposite way,
no increase in total critical failures, and costs within predeclared ceilings.
Two tasks require a gain beyond one showcase example; the no-regression and cost
conditions reflect a conservative maintenance decision. These choices are not a
significance test. A task-specific alternative is allowed only with rationale
frozen before assessment. Unset cost ceilings or decision rules mean the run is
exploratory and cannot declare a winner under this contract.

Report one of: `promising local evidence`, `no demonstrated improvement`,
`regression`, or `inconclusive`, with dimension-level results. Under the default
rule, a task moving from acceptance to non-acceptance or an increase in total
critical failures is regression, even if other tasks improve. A cost-ceiling
breach prevents promising local evidence and is reported as no demonstrated
improvement within budget unless a behavioral regression also occurred.
Otherwise apply the promising-evidence rule above, or report no demonstrated
improvement. These are pilot decisions, not population effect estimates. If
missing runs, unjudgeable outputs, or unresolved reviewer disputes could change classification,
report inconclusive and show the alternatives. Meeting the screen justifies a
fresh held-out replication and a simpler-instruction ablation; it does not make
the skill STABLE. No observed gain on a small sample is not proof of equivalence.

The task/independent source scenario is the generalization unit; repetitions,
claims within one answer, and several posts in one thread are clustered, not
independent sample-size multipliers. Publish paired per-task outcomes and cost
ranges. V0 need not report p-values or confidence intervals. Any later interval
must state its estimand, sampling model, and clustering method. It cannot imply
population coverage from a purposively selected task set.

Keep every planned attempt in the ledger. Timeouts, refusals, tool denials, and
empty outputs are observed failures, not invitations to select a better rerun.
Allow at most one replacement for an infrastructure failure unrelated to the
answer, according to a predeclared classification rule; preserve the original,
link the replacement, and show results with and without it. Do not replace a
low-quality completion. Stop at the planned attempt/budget cap, never when the
skill begins winning. Protocol changes start a new revision without deleting
the previous assessment.

## V0 validity limits and mitigations

| Threat | Bounded mitigation | Residual limitation |
| --- | --- | --- |
| Context differences | Equal common inputs/budgets; record package and injection differences; reject displaced-input comparisons | Added instructions and attention are part of treatment; mechanism remains unidentified |
| Evaluator self-preference | Separate judge session/family, blinded order, source anchors, human review | Style leakage, shared training, and human expectation remain |
| Runtime/system-prompt contamination | Fresh isolated workspaces, audit instruction/catalog discovery and visible configuration | Hosted prompts and model priors may be unobservable; never say "bare model" |
| Model drift | Pin snapshot if exposed; retain returned model/build identity; interleave arms in a short window | Aliases/host updates may change silently; split results across observed changes |
| Tool availability | Equal versions, credentials scope, permissions, and budgets; fixed packets first | Live ranking, availability, and remote server state cannot be fully replayed |
| Stochastic variation | Predeclared repeats and randomized execution schedule; keep all attempts | Small samples can miss rare failures; seed or low temperature is not determinism |
| Benchmark leakage | Novel grouped cases, sealed assessment, access history, delayed publication | Training exposure and prior author familiarity cannot be ruled out |
| Cherry-picked tasks | Freeze coverage matrix/inclusion rule, include routine and contrary cases | Purposive task coverage is not a probability sample of all strategy work |
| Repeated-test optimization | Log candidate history; retire exposed holdouts; preserve negative results | Researcher learns general patterns across iterations; later tasks may still be easier |
| Skill-trigger contamination | No target name/description in baseline; natural activation wording; exclude source-text bait from positives | Catalog competition and runtime routing remain deployment-specific |

## Minimum experiment record

Use files and one manifest, not a service or metadata database. Shared values
are stored once and referenced by run IDs. A reference means retained bytes plus
a checksum, or an immutable repository revision and path; a mutable path alone
does not identify an experiment. Required unknowns use an explicit reason, e.g.
`unknown: host does not expose system prompt`; `not_applicable` is distinct.

| Level | Minimum content | Interpretation it protects |
| --- | --- | --- |
| Study/protocol | Study ID, protocol version/artifact, hypothesis/estimand, primary rule, cost ceilings, tasks/splits/coverage, repetitions, schedule, stop/retry/exclusion rules | Prevents redefining success or selecting attempts afterward |
| Provenance | Repository commit, dirty state and retained patch/untracked input content if used; skill ID/version or content digest including references/scripts; harness revision and dependency lock | Identifies the actual implementation, not just a branch or optional version string |
| Authorship/exposure | Skill/task/rubric authors, calibration/review roles and overlaps, candidate/test exposure history, freeze time | Makes independence and held-out claims inspectable |
| Inputs | Exact common prompts/message roles, evidence packet and collection log/version, grading cards/rubric, per-arm invocation/extra context, fixed vs live mode | Identifies what information and instructions differed |
| Environment | Runtime/build, requested and returned model IDs/snapshot when exposed, reasoning/generation settings and defaults/unknowns, visible instruction/config artifacts, discoverable skills/plugins and versions, tool definitions/versions, web mode, permissions/sandbox, context/output/tool/time limits | Supports a controlled comparison and exposes contamination; secrets are excluded |
| Attempt | Run ID, task/split, arm/config ID, repetition/pair and order, start time UTC, end or elapsed time, completion/error/timeout, load observation and trace, actual model if different | Retains pairing, drift, delivery failures and missing attempts |
| Artifacts/observations | Raw assistant output, visible message/tool trace including returned evidence, generated artifacts, observed token/tool usage and timings, retry/exclusion links and reasons | Supports regrading and cost accounting without reconstructing hidden reasoning |
| Judgment/analysis | Grader type/ID/model/config and prompt/card version, blind order, criterion decisions with passage locators, disagreements/adjudication, analysis version and summaries linked to raw rows | Keeps measurement, judgment, and summary distinct |

Record OS/interpreter only when local scripts or runtime behavior depend on them;
the dependency lock and runtime build normally suffice otherwise. No hardware
inventory, user demographics, account identifiers, machine-wide environment dump,
embedding, or numerical confidence field is required. Record billing cost only
if observed or computed from dated price/unit evidence; label estimates. Do not
fabricate unexposed token or reasoning usage. Preserve visible explanations,
not private chain-of-thought or hidden system prompts.

Local replay means reproducing checks and summaries from retained artifacts.
Rerunning a hosted model or a live search is a new observation, not guaranteed
bitwise reproduction. Redactions and inaccessible source content limit replay
and must be declared under the [security standard](security-standard.md).

P1 supplies this documentary metadata contract; no general Experiment model or
runner is needed yet. P2 should implement only fields its demonstration consumes
and fail clearly when a comparison lacks required interpretation metadata.
