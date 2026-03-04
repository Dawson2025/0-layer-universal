# Codex CLI Context Contract

## Purpose

Define how this entity projects agnostic context into Codex-consumable artifacts.

## Canonical Mapping

- Source of truth: `0AGNOSTIC.md`
- Sync engine: `.0agnostic/agnostic-sync.sh`
- Codex context target: `AGENTS.md`
- Codex merge input: `.1merge/.1codex_merge/`

## Discovery Temperatures

### Hot context

Always available at session start:
- `AGENTS.md`

### Warm context

Loaded when the task enters this entity tree:
- `0INDEX.md`
- `layer_2_group/layer_2_99_stages/stage_2_07_testing/outputs/stage_report.md`

### Cold context

Loaded on demand:
- `.0agnostic/01_knowledge/`
- `.0agnostic/02_rules/`
- `.0agnostic/03_protocols/`
- `.0agnostic/05_skills/`

## Merge Contract

For Codex-specific projection:
- `1_overrides/tool_boilerplate.md` replaces default AGENTS boilerplate.
- `2_additions/tool_additions.md` appends Codex-only guidance.

Requirements:
- Codex merge content must appear in `AGENTS.md` after sync.
- Codex merge content must not leak into `CLAUDE.md`.

## Trigger Contract

If a request mentions one or more of the following, Codex should escalate to cold context:
- `context chain`
- `0agnostic`
- `agnostic-sync`
- `chain-validate`
- `avenue-check`
- `parent chain`

## Validation Contract

Minimum passing checks:
- `.1codex_merge` has non-scaffolded content.
- `test_codex_projection.sh` passes.
- `test_codex_discovery_chain.sh` passes.

## Non-Goals

This contract does not define Claude-specific hooks, `.claude/rules/`, or Claude-only skill injection behavior.
