# layer_1_school_agent_system_development_projects

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Group Definition ──

## Identity

entity_id: "d7e4ea54-4306-46d0-9cdc-83baf95aa885"

This is a **layer_1_group** (organizational container, NOT a layer). It contains further layering structure for layer_2 feature projects.

- **Role**: Organization container for Layer 1 (Projects)
- **Parent**: `../0AGNOSTIC.md` (layer_0_school_agent_system_development)
- **Layer**: 1 (organizational grouping)
- **Type**: Project organization container
- **Contains**: Multiple numbered grouping containers (01_features, 02_projects, etc.) that organize layer_2+ entities

## Key Behaviors

### NOT a Layer - This is a Container

This `layer_1_group/` is **NOT** a layer entity. It is an organizational container. Therefore:

- ❌ NO `layer_1_99_stages/` — containers don't have workflow stages
- ❌ NO entity-level `0AGNOSTIC.md` identity — this is organizational metadata only
- ✅ YES `layer_1_00_layer_registry/` — registry of how layer_1 is organized
- ✅ YES `layer_1_0X_*` numbered grouping containers — organizational subdirectories

### Grouping Container Structure

This group can contain multiple numbered organizational containers:
- `layer_1_01_features/` — for layer_2 feature entities
- `layer_1_02_projects/` — optional, for layer_2 project entities
- `layer_1_03_components/` — optional, for other organizational purposes
- (etc.)

Each child entity inside these containers is a REAL LAYER with its own stages.

## Triggers

Load this context when:
- Working on feature development within the school agent system
- Creating new layer_2 feature entities
- Organizing project-level work

## Current Status

**Phase**: Initialization | **Last Updated**: 2026-02-28

Layer_1_group structure created with registry and feature grouping container. Ready to receive layer_2 feature entities.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

### Structure Status

- ✅ `layer_1_00_layer_registry/` created — for layer_1 organizational metadata
- ✅ `layer_1_01_features/` created — grouping container for layer_2 feature entities
- ⏳ Child layer_2 feature entities pending creation

### Important Distinction

Each child entity (e.g., `layer_2_feature_authentication/`) that goes inside `layer_1_01_features/` will be:
- A **layer_2 entity** (actual layer, not a container)
- Will have its own `layer_2_group/` with `layer_2_00_layer_registry/` and `layer_2_99_stages/`
- Will have 11 workflow stages (01-11)
- Will contribute its own `0AGNOSTIC.md` defining layer_2 identity

This `layer_1_group/` remains an organizational container — purely structural.

# ── References ──

## Navigation

### Parent
`../0AGNOSTIC.md` — layer_0_school_agent_system_development

### Related Directories
- `layer_1_00_layer_registry/` — Layer 1 registry (metadata about how layer_1 is organized)
- `layer_1_01_features/` — Grouping container for layer_2 feature entities

## Key Locations

| Content | Location |
|---------|----------|
| Group identity | This file (0AGNOSTIC.md) |
| Layer registry | `layer_1_00_layer_registry/0REGISTRY.md` |
| Features organization | `layer_1_01_features/` (holds layer_2 entities) |
| Parent context | `../0AGNOSTIC.md` (layer_0 entity) |

## On Exit

1. Update this 0AGNOSTIC.md if adding/modifying grouping containers
2. When creating child layer_2 entities, ensure they go inside appropriate grouping container
3. Run agnostic-sync.sh at parent entity level if needed
4. Commit changes

---

*This is a tool-agnostic group-level context file. Groups are organizational containers and do NOT have workflow stages.*
