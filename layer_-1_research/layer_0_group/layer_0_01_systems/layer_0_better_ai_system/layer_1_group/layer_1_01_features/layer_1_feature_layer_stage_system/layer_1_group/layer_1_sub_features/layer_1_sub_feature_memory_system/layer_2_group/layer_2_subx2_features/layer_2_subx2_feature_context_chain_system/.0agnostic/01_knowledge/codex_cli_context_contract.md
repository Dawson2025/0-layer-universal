---
resource_id: "a0c6a818-34d0-4f48-9a14-b3139c096dc7"
resource_type: "knowledge"
resource_name: "codex_cli_context_contract"
---
# Codex CLI Context Contract

<!-- section_id: "f3a472a9-6195-4f99-9eac-f3f60403a1ec" -->
## Purpose

Define how this entity projects agnostic context into Codex-consumable artifacts.

<!-- section_id: "afcaa567-eeb5-4274-85f5-3e58065ab0fb" -->
## Canonical Mapping

- Source of truth: `0AGNOSTIC.md`
- Sync engine: `.0agnostic/agnostic-sync.sh`
- Codex context target: `AGENTS.md`
- Codex merge input: `.1merge/.1codex_merge/`

<!-- section_id: "bca51b3a-96cc-4013-a7a8-1b8032dc22ee" -->
## Discovery Temperatures

<!-- section_id: "06199c77-1dc2-4fc9-be79-4532681295e3" -->
### Hot context

Always available at session start:
- `AGENTS.md`

<!-- section_id: "0909da98-0780-4f05-9921-7b3dc85ca316" -->
### Warm context

Loaded when the task enters this entity tree:
- `0INDEX.md`
- `layer_2_group/layer_2_99_stages/stage_2_07_testing/outputs/stage_report.md`

<!-- section_id: "65064706-ca91-47eb-8ea4-ea53b13f9d3d" -->
### Cold context

Loaded on demand:
- `.0agnostic/01_knowledge/`
- `.0agnostic/02_rules/`
- `.0agnostic/03_protocols/`
- `.0agnostic/05_skills/`

<!-- section_id: "c20bc822-a007-468b-a225-15392ba3dec9" -->
## Merge Contract

For Codex-specific projection:
- `1_overrides/tool_boilerplate.md` replaces default AGENTS boilerplate.
- `2_additions/tool_additions.md` appends Codex-only guidance.

Requirements:
- Codex merge content must appear in `AGENTS.md` after sync.
- Codex merge content must not leak into `CLAUDE.md`.

<!-- section_id: "7ee4b6c8-f7bd-4d4e-ba4c-0a2b3b2e672e" -->
## Trigger Contract

If a request mentions one or more of the following, Codex should escalate to cold context:
- `context chain`
- `0agnostic`
- `agnostic-sync`
- `chain-validate`
- `avenue-check`
- `parent chain`

<!-- section_id: "67931467-e2fe-4851-b3df-67c3509603db" -->
## Validation Contract

Minimum passing checks:
- `.1codex_merge` has non-scaffolded content.
- `test_codex_projection.sh` passes.
- `test_codex_discovery_chain.sh` passes.

<!-- section_id: "139aec5e-33c4-4cb7-94e7-39f9e617669a" -->
## Non-Goals

This contract does not define Claude-specific hooks, `.claude/rules/`, or Claude-only skill injection behavior.
