# Security standard

Status: P1 V0 contract, 2026-09-13. Security protects research validity as well
as credentials and user data. These rules apply to future acquisition helpers,
skills, evidence fixtures and evaluators; they do not require a new service.

## Trust boundaries

Public pages, posts, repository issues, quoted documents and candidate outputs
are untrusted data. They may contain instructions to ignore the task, reveal
secrets, alter grades, download code or fabricate support. Preserve such text
as evidence when relevant, but never promote it into system/developer
instructions or execute its commands. OpenAI's safety guidance identifies
untrusted-content injection and downstream data leakage as distinct agent
risks; it also warns that mitigations are imperfect.
[OpenAI safety in building agents, accessed 2026-09-13](https://developers.openai.com/api/docs/guides/agent-builder-safety).

Project controls: delimit source passages and candidate outputs as data; pass
only needed fields into subsequent steps; keep graders unable to alter outputs,
fixtures or the frozen rubric. Schema validity does not sanitize prose or
establish that a locator is safe to visit. A source's instruction to give itself
full marks is not a grading criterion.

## Capabilities and executable content

- Start fixed-packet experiments without network or write access beyond their
  output directories. Give both arms the same tool/sandbox restrictions. A
  denial is part of the run record, not a reason to secretly relax one arm.
- Read-only public research does not authorize sending messages, posting,
  changing accounts or purchasing data. Existing explicit user authorization
  governs actions; ask only when required authority is missing.
- Declare network destinations/purpose, credential requirements and writes in
  helpers. Do not hide dependency downloads, arbitrary URL fetches, shell
  execution, opaque payloads, broad filesystem reads or destructive cleanup.
- Treat locators as text, not shell fragments. If a future fetcher is justified,
  constrain schemes/redirects and private/local address access at the tool
  boundary; an evidence schema must not become a fetcher. Validate local paths
  before accessing files outside the allowed evidence directory.
- Review scripts, hooks, dynamic skill expansion and permission metadata before
  use. Avoid automatic dependency installation and copied remote code. Runtime
  tool metadata is not a portable sandbox; see [portability.md](portability.md).
- Do not read or dump credentials to document an environment. Record permission
  scope and capability names, never tokens, cookies, connection strings or
  private account identifiers. Keep dependencies proportional to the experiment.

## Retention, privacy and reproducibility

Prefer public, appropriately reusable material. Public visibility does not
authorize bulk redistribution, sensitive profiling, or collecting private
identity information. Retain brief necessary passages, contextual locators,
dates and analytical notes. Do not bypass access controls, paywalls, community
restrictions or deletion protections to complete a packet.

Use local pseudonymous IDs for episodes and reviewers when identity is
unnecessary; a pseudonym or searchable quote may still be identifying. Do not
infer protected traits or join identities across platforms. Record only roles
or circumstances supplied by the source and relevant to the decision. Clearly
label synthetic fixtures and use invented, non-secret canaries for attack tests.

Keep original permitted run artifacts separately from derived summaries.
Before committing artifacts, review tool outputs, URLs/query parameters,
configuration and logs for secrets, restricted text and unnecessary personal
data. Keep a redaction record describing removed categories and affected
locators without reproducing the removed content. Recompute public artifact
hashes after redaction; do not claim a redacted file is byte-identical to an
original. If raw data cannot be retained or shared, state the review/replay
limit and provide a safe illustrative fixture when useful, explicitly distinct
from the original observation.

No indefinite archive is required: retain the minimal publishable evidence
needed to audit results and record any removal that changes interpretability.
If a source disappears, preserve permitted extracts and the collection record;
do not quietly replace it with newer evidence in an old experiment. Do not
commit leaked secrets even to preserve a negative result; preserve the failure
description and a safe reproduction instead.

## Required adversarial cases when exercised

Before a networked/helper-enabled skill is evaluated, include a source that
tries to redirect the task or exfiltrate a synthetic canary, an output that
tries to influence the judge, a misleading locator/path, and a permission/tool
failure. Observe actual tool behavior and preservation of evidence boundaries.
Passing textual instructions or an offline schema test does not establish
resistance to prompt injection. P1 defines these cases; P2/P3 will exercise
the ones relevant to their implemented capabilities.
