---
paths: layer_0/**
---

# Universal Layer Context

## Required Reading

When working in layer_0 (universal) directories:
1. Find the `.gab.jsonld` for your role (e.g., `layer_0_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name, e.g., `layer_0_orchestrator.integration.md`)
3. For precise mode constraints, query the `.gab.jsonld` via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
4. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Understanding location | `/context-gathering` | First action — identify sub-layer, purpose |
| Working through stages | `/stage-workflow` | When following stage_0_* directories |
| Creating new sub-layers | `/entity-creation` | When extending layer_0 structure |
| Session transitions | `/handoff-creation` | Preserve context for next session |

## Episodic Memory

- **Session start**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **Session end**: After significant work, update `.0agnostic/episodic_memory/index.md` in the working layer, then run `tools/episodic-sync.sh` to sync to auto-memory

## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` is the source — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

## Universal Layer Rules

- Layer 0 content applies to ALL projects — changes here affect everything
- Sub-layers are organized by type:
  - `sub_layer_0_01_knowledge_system/` — Domain knowledge (includes `principles/`)
  - `sub_layer_0_02_rules/` — Mandatory rules (`static/` + `dynamic/`) — READ FIRST
  - `sub_layer_0_03_protocols/` — Standard protocols
  - `sub_layer_0_04+_setup_dependant/` — OS/tool/environment-specific content
- Always check `sub_layer_0_02_rules/` before making changes
- Universal rules cannot be overridden without explicit approval
