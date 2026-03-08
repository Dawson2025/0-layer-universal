# OpenAI Context

---
resource_id: "c40951ce-b9a2-4c62-b5d1-7578710436aa"
resource_type: "agnostic_document"
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

This entity governs the **pointer synchronization system** — all tooling and design for keeping pointer files in sync with their canonical targets. The tools live in organized protocol directories under `.0agnostic/03_protocols/` (pointer_sync_protocol, uuid_assignment_protocol, agnostic_sync_protocol). Each script has a stable UUID (`resource_id`) that survives renames and moves — the path is convenience, the UUID is truth.

<!-- section_id: "a77c8da4-37e8-4685-93e8-ad32d96b8c96" -->
### Production Artifacts (organized by protocol in .0agnostic/03_protocols/)

Scripts are organized into three protocol directories. Each script has a stable `resource_id` (UUID) so references survive path changes.

| Artifact | Protocol | Path | resource_id |
|----------|----------|------|-------------|
| `pointer-sync.sh` | pointer_sync | `.0agnostic/03_protocols/pointer_sync_protocol/tools/` | `08a4e9bc-8cc1-457e-b966-0a912ae6dff7` |
| `entity-find.sh` | pointer_sync | `.0agnostic/03_protocols/pointer_sync_protocol/tools/` | `f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7` |
| `create-resource-indexes.sh` | pointer_sync | `.0agnostic/03_protocols/pointer_sync_protocol/tools/` | `9f294247-a227-4bf1-8a51-bdee7555115c` |
| `migrate-pointers.sh` | pointer_sync | `.0agnostic/03_protocols/pointer_sync_protocol/tools/` | `7505b140-8772-43f1-abe5-996847e68657` |
| `assign-entity-uuids.sh` | uuid_assignment | `.0agnostic/03_protocols/uuid_assignment_protocol/tools/` | `92ab3def-22d7-48cd-91be-6744c3466240` |
| `assign-file-uuids.sh` | uuid_assignment | `.0agnostic/03_protocols/uuid_assignment_protocol/tools/` | `68c9cfcc-9915-47f6-be3a-2c75fbd7ef7e` |
| `assign-dir-uuids.sh` | uuid_assignment | `.0agnostic/03_protocols/uuid_assignment_protocol/tools/` | `c7d8e9f0-1a2b-4c3d-e4f5-6a7b8c9d0e1f` |
| `assign-section-uuids.sh` | uuid_assignment | `.0agnostic/03_protocols/uuid_assignment_protocol/tools/` | `d8e9f0a1-2b3c-4d5e-f6a7-8b9c0d1e2f3a` |
| `create-stage-indexes.sh` | uuid_assignment | `.0agnostic/03_protocols/uuid_assignment_protocol/tools/` | `bcac347f-f4e3-4047-8171-ed9a20022624` |
| `agnostic-sync.sh` | agnostic_sync | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/` | `781698fa-f580-4606-80e4-dc73fb30e3f7` |
| `agnostic-diagram-generator.sh` | agnostic_sync | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/` | `44f8f145-6ab5-44c0-8538-887e7c652052` |
| `user-level-sync.sh` | agnostic_sync | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/` | `5e3e7995-23d1-42e6-9a11-de1515e6367f` |

**Non-script artifacts**:

| Artifact | Path | Purpose |
|----------|------|---------|
| `.entity-lookup.tsv` | `.entity-lookup.tsv` | Flat entity index (generated) |
| Protocol | `.0agnostic/03_protocols/pointer_sync_protocol/pointer_sync_protocol.md` | Usage guide |
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

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
