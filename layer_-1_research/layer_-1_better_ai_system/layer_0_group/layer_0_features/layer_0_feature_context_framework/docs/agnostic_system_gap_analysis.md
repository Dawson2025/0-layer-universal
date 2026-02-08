# Agnostic System Gap Analysis — Claude Code Integration

**Layer**: 0 (Universal — Context Framework)
**Date**: 2026-02-08
**Status**: Analysis complete, fixes pending

---

## Problem Statement

The agnostic system (`0AGNOSTIC.md`, `.0agnostic/`, `.1merge/`, `agnostic-sync.sh`) is the infrastructure layer for tool-agnostic context distribution. However, **Claude Code's context chain does not reference or instruct agents to use this system at all.**

This means:
- Agents don't know to edit `0AGNOSTIC.md` instead of `CLAUDE.md`
- Agents don't know `.0agnostic/` contains on-demand resources
- Agents don't know `.1merge/` provides tool-specific overrides
- Agents don't know to run `agnostic-sync.sh` after changes

---

## System Architecture

### What the Agnostic System Does

```
SOURCE (edit these)                  GENERATED (don't edit)
─────────────────                    ─────────────────────
0AGNOSTIC.md          ──┐
                        ├──▶  agnostic-sync.sh  ──▶  CLAUDE.md
.0agnostic/            ─┤                         ──▶  AGENTS.md
  ├── skills/           │                         ──▶  GEMINI.md
  ├── agents/           │                         ──▶  OPENAI.md
  ├── rules/            │                         ──▶  .claude/skills/
  ├── knowledge/        │                         ──▶  .claude/rules/
  └── automation/       │                         ──▶  .cursor/rules/
                        │
.1merge/               ─┘
  ├── .1claude_merge/
  │   ├── 0_synced/      (base from .0agnostic)
  │   ├── 1_overrides/   (Claude-specific overrides)
  │   └── 2_additions/   (Claude-specific additions)
  ├── .1cursor_merge/
  ├── .1copilot_merge/
  ├── .1gemini_merge/
  ├── .1aider_merge/
  └── .1codex_merge/
```

### Three Avenues of Chaining

**Context Chain** (how agents load instructions):

| Avenue | Mechanism | Status |
|--------|-----------|--------|
| CLAUDE.md hierarchy | Root → layer → stage → feature | Working |
| `.claude/rules/` | Path-matched rules files | Working |
| `@imports/` | Session workflow, structure overview | Working |

**Reference Chain** (how agents find resources):

| Avenue | Mechanism | Status |
|--------|-----------|--------|
| AALang/GAB/JSON-LD | `.gab.jsonld` agent definitions | Working (10/11) |
| Integration MDs | `.integration.md` auto-generated summaries | Working (8/8) |
| Skills | `.claude/skills/*/SKILL.md` action triggers | Partial (5/7) |

**Agnostic System** (how context stays tool-agnostic):

| Component | Purpose | Referenced in Chain? |
|-----------|---------|:-------------------:|
| `0AGNOSTIC.md` | Source of truth for context | **NO** |
| `.0agnostic/` | On-demand resources (rules, skills, agents, knowledge) | **NO** |
| `.1merge/` | Tool-specific overrides (3-tier merge) | **NO** |
| `agnostic-sync.sh` | Transforms agnostic → tool-specific | **NO** |

---

## Gap Inventory

### Claude Code Context Chain Entry Points (13 total)

| Entry Point | GAB | Integration | Skills | 0AGNOSTIC | .0agnostic | .1merge | sync.sh |
|-------------|:---:|:----------:|:------:|:---------:|:----------:|:-------:|:-------:|
| `~/.claude/CLAUDE.md` | — | — | — | NO | NO | NO | NO |
| `~/CLAUDE.md` | — | — | — | NO | NO | NO | NO |
| `CLAUDE.md` (root) | YES | YES | NO | NO | NO | NO | NO |
| `rules/universal-layer.md` | YES | YES | YES | NO | NO | NO | NO |
| `rules/aalang-integration.md` | YES | YES | YES | NO | NO | NO | NO |
| `rules/research-context.md` | YES | YES | YES | NO | NO | NO | NO |
| `rules/school-context.md` | YES | YES | YES | NO | NO | NO | NO |
| `rules/development-stages.md` | YES | YES | YES | NO | NO | NO | NO |
| `skills/context-gathering` | YES | YES | — | NO | NO | NO | NO |
| `skills/entity-creation` | NO | NO | — | NO | NO | NO | NO |
| `skills/handoff-creation` | YES | NO | — | NO | NO | NO | NO |
| `skills/stage-workflow` | YES | NO | — | NO | NO | NO | NO |
| `@imports/session_workflow.md` | YES | YES | NO | NO | NO | NO | NO |

**Legend**: YES = referenced, NO = not referenced, — = not applicable

### Score by Avenue

| Avenue | Coverage | Grade |
|--------|----------|-------|
| GAB/JSON-LD | 10/11 (91%) | A |
| Integration MD | 8/8 (100%) | A+ |
| Skills | 5/7 (71%) | C |
| 0AGNOSTIC.md | 0/10 (0%) | F |
| .0agnostic/ | 0/10 (0%) | F |
| .1merge/ | 0/10 (0%) | F |
| agnostic-sync.sh | 0/10 (0%) | F |

---

## Fix Plan

### Tier 1: Critical (Agnostic System — 40 failures)

Every context chain entry point needs to know about the agnostic system. The fix should add:

**For files that agents EDIT** (rules, skills, CLAUDE.md):
```markdown
## Agnostic System
- `0AGNOSTIC.md` is the source of truth — edit this, NOT `CLAUDE.md`
- `.0agnostic/` contains on-demand resources (rules, skills, agents, knowledge)
- After editing 0AGNOSTIC.md, run `agnostic-sync.sh` to regenerate tool-specific files
- `.1merge/` provides tool-specific overrides (3-tier: synced → overrides → additions)
```

**For session workflow** (`@imports/session_workflow.md`):
- Add step: "If modifying context, edit 0AGNOSTIC.md and run agnostic-sync.sh"

**For context-gathering skill**:
- Add step: "Check for 0AGNOSTIC.md and .0agnostic/ in working directory"

### Tier 2: Minor (Skills + CLAUDE.md — 6 failures)

- Add skills references to `@imports/session_workflow.md` and root `CLAUDE.md`
- Add .gab.jsonld/.integration.md references to `entity-creation` and `handoff-creation` skills

### Tier 3: Consistency (layer_0 references — 2 failures)

- `layer_0/0AGNOSTIC.md` needs to mention .0agnostic/ (it probably does but CLAUDE.md doesn't carry it through)
- Root `CLAUDE.md` should reference 0AGNOSTIC.md

---

## Scope of .1merge/

Currently `.1merge/` only exists in the research layer (9 directories). The question of whether to extend it to layer_0 and layer_1 is a separate decision — the context chain should at least explain what it IS so agents encountering it understand the pattern.

---

## Relationship to Other Research

- **Test results**: `layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/claude_code_chain_test_results.md`
- **Agnostic sync design**: `layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/agnostic_sync_system_design.md`
- **Context chain visualization**: `layer_0_feature_context_framework/layer_1_sub_feature_context_visualization/diagrams/current/context_chain/`

---

*This document is part of the context framework research for the better_ai_system project.*
