# Claude Code Context

---
resource_id: "c40951ce-b9a2-4c62-b5d1-7578710436aa"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_3_subx3_feature_trigger_pointer_system

<!-- section_id: "e58b6638-29f0-4a85-a4f9-afb047fa89e0" -->
## Identity

entity_id: "ae555d77-4521-4c1a-add1-ad572fae305c"

You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: Trigger Pointer System.
- **Role**: Trigger-based pointer synchronization system — automated detection and resolution of stale pointer files across the layer-stage hierarchy
- **Scope**: Pointer file format (YAML frontmatter), path resolution algorithm, sync scripts (pointer-sync.sh), hook-based triggers (pointer-edit-guard.sh), validation, protocol
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_context_chain_system)
- **Children**: None (leaf entity)

<!-- section_id: "5ded17a3-7104-4e06-b25c-db03496a1d53" -->
## Key Behaviors

<!-- section_id: "c3eff18b-c425-40b2-a1a3-7a626c531797" -->
### What This Entity Owns

This entity governs the **pointer synchronization system** — all tooling and design for keeping pointer files in sync with their canonical targets. The actual tools live at root `.0agnostic/` (production location), but this entity owns the stages for their ongoing development.

<!-- section_id: "a77c8da4-37e8-4685-93e8-ad32d96b8c96" -->
### Production Artifacts (at root .0agnostic/)

| Artifact | Root Location | Purpose |
|----------|---------------|---------|
| `pointer-sync.sh` | `.0agnostic/pointer-sync.sh` | Main sync script |
| `entity-find.sh` | `.0agnostic/entity-find.sh` | Fast entity lookup (~5ms, no Python) |
| `.entity-lookup.tsv` | `.entity-lookup.tsv` | Flat entity index (generated) |
| Protocol | `.0agnostic/03_protocols/pointer_sync_protocol.md` | Usage guide |
| Knowledge | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` | System overview |
| Rule | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` | Format requirements |
| UUID Rule | `.claude/rules/uuid-identity-system.md` | Agent discoverability |
| Hook | `.0agnostic/06_.../08_hooks/scripts/pointer-edit-guard.sh` | Edit-time trigger |
| UUID Skill | `.0agnostic/06_.../05_skills/uuid-query/SKILL.md` | Agent skill interface |

<!-- section_id: "5f39911f-20d8-4c08-bc76-d46bc6dfe474" -->
### Connection to Parent

The trigger pointer system is a subset of the context chain system. Pointers ARE part of the three-tier knowledge architecture (Pointer -> Distilled -> Full). This entity handles the automation of that first tier.

<!-- section_id: "3c81300d-020e-4d49-9c24-a6ba03a4d61b" -->
## Triggers
Load this context when:
- User mentions: pointer sync, trigger pointer, auto-update pointers, stale pointers, pointer validation, entity-find, entity lookup
- Working on: pointer-sync.sh improvements, entity-find.sh, new hook triggers, pointer format changes, path resolution bugs
- Entering: `layer_3_subx3_feature_trigger_pointer_system/`

<!-- section_id: "0cae297e-ba44-4a29-8d01-15e19023dec9" -->
## Pointers
<!-- section_id: "a049413d-fc6f-46a8-820d-3d473d66c8ef" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_99_stages/` for stage progress

<!-- section_id: "a5548a9d-f75e-43b2-9673-7e865de25497" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_3_group/layer_3_99_stages/` |

<!-- section_id: "35e3d65b-ee29-46a5-808a-6af84386e779" -->
## Resources

<!-- section_id: "bfcd7682-5b72-429c-b6e0-943bf7886f41" -->
### Knowledge

| Topic | Path | Content |
|-------|------|---------|
| Trigger Pointer System | `.0agnostic/01_knowledge/trigger_pointer_system/trigger_pointer_knowledge.md` | Architecture, components, design decisions, trigger mechanisms |

<!-- section_id: "a883efc1-4176-492f-b78a-1c97db74c0d4" -->
### Rules

| Rule | Type | Path |
|------|------|------|
| Pointer File Convention | Static | `.0agnostic/02_rules/static/pointer_file_convention/pointer_file_convention.md` |
| Auto-Trigger Pointer Sync | Dynamic | `.0agnostic/02_rules/dynamic/auto_trigger_rule/auto_trigger_rule.md` |

<!-- section_id: "82c23aa7-7782-4d8e-b2b7-a20b4990e310" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Requirements | `layer_3_group/layer_3_99_stages/stage_3_01_request_gathering/outputs/` |
| Research | `layer_3_group/layer_3_99_stages/stage_3_02_research/outputs/` |
| Design | `layer_3_group/layer_3_99_stages/stage_3_04_design/outputs/` |
| Implementation | `layer_3_group/layer_3_99_stages/stage_3_06_development/outputs/` |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
