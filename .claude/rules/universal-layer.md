---
resource_id: "6029951d-37ae-482d-8ae6-209a42341721"
resource_type: "document"
resource_name: "universal-layer"
---
---
paths: layer_0/**
---

# Universal Layer Context

<!-- section_id: "658d64fb-d220-4d8b-adc2-ef64ba2e30bf" -->
## Required Reading

When working in layer_0 (universal) directories:
1. Find the `.gab.jsonld` for your role (e.g., `layer_0_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name, e.g., `layer_0_orchestrator.integration.md`)
3. For precise mode constraints, query the `.gab.jsonld` via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
4. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

<!-- section_id: "54bfafe7-2ca0-4155-bac0-5b59c854c5b6" -->
## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Understanding location | `/context-gathering` | First action — identify sub-layer, purpose |
| Working through stages | `/stage-workflow` | When following stage_0_* directories |
| Creating new sub-layers | `/entity-creation` | When extending layer_0 structure |
| Session transitions | `/handoff-creation` | Preserve context for next session |

<!-- section_id: "6b408044-5316-4cca-91c6-84a30b9e9fa7" -->
## Episodic Memory

- **Session start**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **Session end**: After significant work, update `.0agnostic/episodic_memory/index.md` in the working layer, then run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` to sync to auto-memory

<!-- section_id: "0ccf3661-2d6a-4d9a-a38a-a9dab964d23f" -->
## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` is the source — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

<!-- section_id: "f24ecf5d-5fc5-432e-93de-30602993ac12" -->
## Universal Layer Rules

- Layer 0 content applies to ALL projects — changes here affect everything
- Entity resources live in `.0agnostic/` with numbered directories:
  - `.0agnostic/01_knowledge/` — Domain knowledge (per-topic with `principles/`, `docs/`, `resources/`)
  - `.0agnostic/02_rules/` — Mandatory rules (`static/` + `dynamic/`) — READ FIRST
  - `.0agnostic/03_protocols/` — Standard protocols
  - `.0agnostic/04_episodic_memory/` — Session records (`sessions/`, `changes/`)
  - `.0agnostic/05_handoff_documents/` — Cross-entity communication
  - `.0agnostic/06_context_avenue_web/` — All context avenues (aalang, skills, agents, hooks, etc.)
  - `.0agnostic/07+_setup_dependant/` — OS/tool/environment-specific content
- Always check `.0agnostic/02_rules/` before making changes
- Universal rules cannot be overridden without explicit approval
