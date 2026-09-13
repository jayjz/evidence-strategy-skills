# Portability

Status: P1 documentation review, checked 2026-09-13. No runtime compatibility
experiment was performed. Documentation URLs can change; recheck before P2/P7
tests or P9 distribution. Documented support is not observed effectiveness.

## Contract and runtime boundary

The portable unit remains `skills/<name>/SKILL.md` and the local resources it
actually requires. Repository layout is authoring layout, not a promise that
every runtime discovers a top-level `skills/` directory automatically.

The current Agent Skills specification requires YAML `name` and `description`
followed by Markdown. Names match the directory, use lowercase letters/digits
and single hyphens, and are 1–64 characters; descriptions are nonempty and at
most 1,024 characters. Optional license, compatibility, and string-valued
metadata are available. `allowed-tools` is experimental with implementation
variation. The specification recommends progressive loading of metadata,
instructions, then resources; under 500 lines is guidance, not a usefulness
criterion. [Agent Skills specification](https://agentskills.io/specification).

Project policy: use the common format and plain instructions. Describe a
capability such as public-source search, local passage inspection, or structured
artifact writing without making vendor tool names part of the business logic.
An unavailable capability must produce a scoped limitation or evidence request,
never fabricated research. Do not promise permission enforcement from metadata.

## Current documented conventions

| Concern | Codex/OpenAI | Claude Code |
| --- | --- | --- |
| Local discovery | Codex scans repository `.agents/skills` from working directory toward repository root, plus user/admin/system locations | Project `.claude/skills` and personal `~/.claude/skills`, with additional managed/plugin scopes |
| Invocation | CLI/IDE support explicit `$skill` selection and implicit description matching | Explicit `/skill-name` and automatic selection |
| Runtime additions | Optional `agents/openai.yaml` for presentation, dependencies and `allow_implicit_invocation`; false retains explicit invocation | `disable-model-invocation: true` removes automatic use and description context; `user-invocable: false` removes manual invocation |
| Context | Initial metadata may be shortened or omitted when the catalog exceeds its budget; full instructions load on selection | Skill instructions persist after loading; automatic and explicit controls affect what is initially exposed |
| Execution | Actual available tools/permissions depend on the host and configuration | `allowed-tools` grants specified tool permissions for the invoking turn; it does not restrict all available tools. `context: fork` and dynamic command expansion add runtime behavior |

Sources for the table: [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)
and [Claude Code skills](https://code.claude.com/docs/en/skills). Claude accepts
some frontmatter omissions that the open specification does not; this project
keeps the stricter common contract. These facts require runtime-specific test
configuration, not copies of the strategy procedure.

Codex also discovers layered AGENTS.md instructions. An experiment must record
the visible instruction chain and isolate the baseline from this repository's
methodology. [OpenAI custom instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
The same isolation principle applies to other hosts' persistent instructions,
memory, plugins, and catalogs. Inspect the actual environment rather than
inferring it from the target skill's installation setting.

## Plugins are a separate distribution concern

Current OpenAI packaging guidance uses root `plugin.json` for the portable
Agent Plugins package, with OpenAI settings in `extensions.com.openai`. The
older `.codex-plugin/plugin.json` remains a fallback; the documented creator
still scaffolds that compatibility layout. Root `mcp.json` and legacy
`.mcp.json` are not interchangeable by renaming. This is a plugin contract,
distinct from the Agent Skills contract. P1 creates neither manifest.
[OpenAI Package your plugin](https://developers.openai.com/plugins/build/plugins).

Distribution can introduce MCP servers, hooks, permissions and other context,
so a plugin-installed treatment can differ from an instruction-only skill.
Record those differences rather than attributing their combined effect to the
portable procedure. Never install a marketplace or fork skill logic just to
make a documentation checklist look complete.

## Later portability observation protocol

When a useful workflow warrants runtime testing:

1. Freeze the same portable package/content digest. Record any packaging overlay
   separately, including invocation syntax, paths and permission changes.
2. Confirm resource resolution from an installed standalone copy. Existing
   PROPOSED placeholders refer to `../../ROADMAP.md`; that authoring reference
   does not establish a self-contained installable skill.
3. Test explicit loading, then behavior on identical fixed packets using the
   [evaluation contract](evaluation-standard.md). Test automatic activation in a
   separate declared catalog. Preserve load evidence and missing telemetry.
4. Record capability as documented, observed working, observed failing, or
   unknown, with runtime version, date, task and trace. These are observation
   labels for the report, not a new profile framework.
5. Describe the tested model/runtime combination. Comparing Codex/OpenAI with
   Claude Code/Claude changes both model and runtime; differences cannot be
   attributed to runtime alone. Equal tool names also do not imply equivalent
   implementations or search results.

Format portability, capability compatibility, activation reliability, and
behavioral usefulness are four distinct claims. A shared file format establishes
only the first. Add a small adapter only for a demonstrated mismatch, and retain
one authoritative procedural core unless evidence justifies a documented fork.
