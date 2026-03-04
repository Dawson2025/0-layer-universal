# OpenAI Context


## Identity
You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: Trigger Pointer System.
- **Role**: Trigger-based pointer synchronization system — automated detection and resolution of stale pointer files across the layer-stage hierarchy
- **Scope**: Pointer file format (YAML frontmatter), path resolution algorithm, sync scripts (pointer-sync.sh), hook-based triggers (pointer-edit-guard.sh), validation, protocol
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_context_chain_system)
- **Children**: None (leaf entity)

## Key Behaviors

### What This Entity Owns

This entity governs the **pointer synchronization system** — all tooling and design for keeping pointer files in sync with their canonical targets. The actual tools live at root `.0agnostic/` (production location), but this entity owns the stages for their ongoing development.

### Production Artifacts (at root .0agnostic/)

| Artifact | Root Location | Purpose |
|----------|---------------|---------|
| `pointer-sync.sh` | `.0agnostic/pointer-sync.sh` | Main sync script |
| Protocol | `.0agnostic/03_protocols/pointer_sync_protocol.md` | Usage guide |
| Knowledge | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` | System overview |
| Rule | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` | Format requirements |
| Hook | `.0agnostic/06_.../08_hooks/scripts/pointer-edit-guard.sh` | Edit-time trigger |

### Connection to Parent

The trigger pointer system is a subset of the context chain system. Pointers ARE part of the three-tier knowledge architecture (Pointer -> Distilled -> Full). This entity handles the automation of that first tier.

## Triggers
Load this context when:
- User mentions: pointer sync, trigger pointer, auto-update pointers, stale pointers, pointer validation
- Working on: pointer-sync.sh improvements, new hook triggers, pointer format changes, path resolution bugs
- Entering: `layer_3_subx3_feature_trigger_pointer_system/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_3_group/layer_3_99_stages/` |

## Resources

### Knowledge

| Topic | Path | Content |
|-------|------|---------|
| Trigger Pointer System | `.0agnostic/01_knowledge/trigger_pointer_system/trigger_pointer_knowledge.md` | Architecture, components, design decisions, trigger mechanisms |

### Rules

| Rule | Type | Path |
|------|------|------|
| Pointer File Convention | Static | `.0agnostic/02_rules/static/pointer_file_convention/pointer_file_convention.md` |
| Auto-Trigger Pointer Sync | Dynamic | `.0agnostic/02_rules/dynamic/auto_trigger_rule/auto_trigger_rule.md` |

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
