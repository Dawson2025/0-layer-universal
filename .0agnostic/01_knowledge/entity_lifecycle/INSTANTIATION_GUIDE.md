---
resource_id: "8b26f755-ff1e-47d9-9b24-e0204be0411a"
resource_type: "knowledge"
resource_name: "INSTANTIATION_GUIDE"
---
# Entity Instantiation Guide

## Overview

This guide explains how to create new entities in the layer-stage system.

**⚠️ START HERE**: All structural details, templates, and step-by-step instructions come from the CANONICAL SOURCE:

**[entity_structure.md](../../../06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md)**

That document is the **single source of truth** for:
- Complete directory tree structure
- Full mkdir command templates
- Stage creation procedures
- Naming conventions
- Required files and templates
- Post-instantiation checklist
- All workflow details

## Quick Decision Tree

### Creating a... | Goes in... | Layer N
|---|---|---|
| New project | `layer_1/layer_1_projects/` | 1 |
| New feature (inside project) | `<project>/layer_2_group/layer_2_features/` | 2 |
| New component (inside feature) | `<feature>/layer_3_group/layer_3_components/` | 3 |
| New research project | `layer_-1_research/` | -1 |
| New research feature | `<research>/layer_0_group/layer_0_features/` | 0 |

## Key Architectural Pattern

- **`layer_N_group/`** (entity's own internal structure): Contains ONLY `layer_N_00_layer_registry/` + `layer_N_99_stages/`
- **`layer_N+1_group/`** (further layering for children): Contains `layer_N+1_00_layer_registry/` + `layer_N+1_01_features/` + other organizing containers

**⚠️ CRITICAL**: Child-organizing containers (features, projects, components) go INSIDE `layer_N+1_group/`, NEVER inside `layer_N_group/`.

## Instantiation Workflow

1. **Read the canonical source** (link above) for complete instructions
2. **Use mkdir templates** from entity_structure.md
3. **Create all 12 stages** (00-11) — Empty stages are valid, missing stages are NOT
4. **Create required files** (0AGNOSTIC.md, 0INDEX.md, README.md)
5. **Create orchestrators** (copy from sibling entity, adapt names)
6. **Run agnostic-sync.sh** on all 0AGNOSTIC.md files
7. **Validate** with validate-entity.sh

## 0AGNOSTIC.md Template

Each entity needs a 0AGNOSTIC.md defining its identity. Basic structure:

```markdown
# Identity
You are an agent at **Layer N** (Type), **Entity**: <name>.

- **Role**: <role description>
- **Scope**: <what this entity covers>
- **Parent**: `../0AGNOSTIC.md`
- **Children**: `layer_N+1_group/` (contains child organizing containers)

## Triggers
Load this context when:
- User mentions: "<keywords>"
- Working on: <activities>
- Entering: `<path>`
```

**For complete 0AGNOSTIC.md template**: See entity_structure.md → Required Files

## Type-Specific Examples

### Creating a New Project (layer_1)

1. **Location**: `layer_1/layer_1_projects/layer_1_project_<name>/`
2. **Children**: `layer_2_group/layer_2_features/` (feature entities)
3. **0AGNOSTIC.md example**:
```markdown
## Identity
You are an agent at **Layer 1** (Project), **Project**: <name>.
- **Role**: Project Manager
- **Scope**: <project description>
- **Children**: `layer_2_group/layer_2_features/`
```

### Creating a New Feature (layer_2+)

1. **Location**: `<project>/layer_2_group/layer_2_features/layer_2_feature_<name>/`
2. **Children**: `layer_3_group/layer_3_components/` (if any)
3. **0AGNOSTIC.md example**:
```markdown
## Identity
You are an agent at **Layer 2** (Feature), **Feature**: <name>.
- **Role**: Feature Developer
- **Scope**: <feature description>
- **Children**: `layer_3_group/layer_3_components/` (if any)
```

### Creating a New Research Project (layer_-1)

1. **Location**: `layer_-1_research/layer_-1_<name>/`
2. **Key difference**: Uses `layer_0_group/` for features (not layer_2_group)
3. **Scope note**: Research-only — does not implement in production
4. **0AGNOSTIC.md includes**:
```markdown
- **Scope**: Research, design, planning only. Does not implement in production.
```

### Creating a New Stage

1. **Location**: `<entity>/layer_N_group/layer_N_99_stages/stage_N_XX_<name>/`
2. **Complete 12-stage example**: See entity_structure.md → Stage Structure

## Deprecated Patterns

These patterns are **no longer used**. If found, migrate per entity_structure.md:

| Old | Replacement |
|---|---|
| `layer_N_01_ai_manager_system/` | Entity root `0AGNOSTIC.md` |
| `layer_N_02_manager_handoff_documents/` | `.0agnostic/05_handoff_documents/` |
| `layer_N_03_sub_layers/` | `.0agnostic/01_knowledge/` |
| Topic sub-layer directories | `.0agnostic/01_knowledge/[topic]/` |

---

**PRIMARY SOURCE**: [entity_structure.md](../../../06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md)

**For maintenance guidance**: [MAINTENANCE_GUIDE.md](./MAINTENANCE_GUIDE.md)

**For complete post-instantiation checklist**: See entity_structure.md
