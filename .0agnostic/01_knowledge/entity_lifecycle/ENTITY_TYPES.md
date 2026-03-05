---
resource_id: "cd440420-3152-4260-b503-a0628c646019"
resource_type: "knowledge"
resource_name: "ENTITY_TYPES"
---
# Entity Types

<!-- section_id: "cd02736c-2d56-488b-8317-17d38caf3675" -->
## What is an Entity?

An entity is any managed unit in the layer-stage system: projects, features, components, stages, research projects, etc.

**ALL entities follow the canonical structure** defined in:
**[entity_structure.md](../../../06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md)**

That document is the **single source of truth** for:
- Complete directory structure for each type
- File requirements
- Naming conventions
- Mkdir templates
- Agent file specifications

<!-- section_id: "419b4bf4-64c6-4b95-ba2d-065b4fead6db" -->
## Entity Types Overview

| Type | Layer | Purpose | Parent Location |
|------|-------|---------|-----------------|
| Project | 1 | Complete application or system | `layer_1/layer_1_projects/` |
| Feature | 2+ | Distinct capability within project | `<project>/layer_N+1_group/layer_N+1_features/` |
| Component | 3+ | Separable sub-part of feature | `<feature>/layer_N+1_group/layer_N+1_components/` |
| Research Project | -1 | Experimental exploration | `layer_-1_research/` |
| Stage | varies | Workflow phase (01-11) | `<entity>/layer_N_group/layer_N_99_stages/` |

<!-- section_id: "70baf877-087e-45ba-83c7-dd177aaa545b" -->
## Quick Reference

<!-- section_id: "41ea4739-3de6-40be-aec4-83bde5f69856" -->
### 1. Projects (layer_1)

**Purpose**: A complete application, system, or body of work

**Example structure**: See entity_structure.md → Full Entity Structure

**0AGNOSTIC.md identity**: Layer 1 project with children at `layer_2_group/layer_2_features/`

<!-- section_id: "620bfbc5-8378-4c93-83e3-08de291c5fc5" -->
### 2. Features (layer_2+)

**Purpose**: A distinct capability within a project

**Example structure**: See entity_structure.md → Full Entity Structure

**0AGNOSTIC.md identity**: Layer N feature with children at `layer_N+1_group/layer_N+1_components/` (if any)

<!-- section_id: "76482a21-ad02-4dd4-a0bb-52e52976d3a7" -->
### 3. Research Projects (layer_-1)

**Purpose**: Experimental, exploratory work

**Key difference**: Uses `layer_0_group/` for features (not layer_2_group)

**Scope**: Research-only; does not implement in production

**0AGNOSTIC.md includes**: "Research, design, planning only. Does not implement in production."

<!-- section_id: "8896c862-43f4-40c2-beaf-6b80f2c9f984" -->
### 4. Stages (stage_N_XX)

**Purpose**: Workflow phase container

**Creation**: ALL 12 stages created (00-11). Empty stages are valid. Missing stages are NOT.

**Structure**: See entity_structure.md → Stage Structure

**Parent**: Always inside `layer_N_group/layer_N_99_stages/` of their entity

<!-- section_id: "b0300975-7514-4390-8d56-13f80f29bd00" -->
### 5. Setup-Dependant Entities

**Purpose**: Machine/OS/environment-specific configuration

**Location**: Inside `.0agnostic/07+_setup_dependant/`

**Structure exception**:
- No `07+_setup_dependant/` in their `.0agnostic/` (they're already within one)
- Knowledge topics replace old-style sub-layers
- May have internal stages and child entities

**Example**: `sub_layer_0_06_local/` (Ubuntu environment) with internal stages and child entities at `sub_layer_0_07_group/`

<!-- section_id: "8fa35878-b23a-495f-b36a-ba057252a333" -->
## Naming Conventions

| Convention | Rule | Example |
|---|---|---|
| Entity naming | `layer_{N}_{type}_{name}` | `layer_2_feature_assignments` |
| Internal group | **MUST** use `_group` suffix | `layer_7_group/` (NOT `layer_7/`) |
| Children group | **MUST** use `_group` suffix | `layer_8_group/` (NOT `layer_8/`) |
| Episodic memory | **MUST** be `episodic_memory` | NOT `episodic/` |
| Agent files | Dot-separation | `name.gab.jsonld` (NOT `name_gab.jsonld`) |

Children are always layer N+1 of their parent.

<!-- section_id: "3ae1114b-7be7-46ea-9fc0-ef1d3d64c95e" -->
## Key File Requirements

| File | Purpose | Required For |
|------|---------|--------------|
| `0AGNOSTIC.md` | Identity, triggers, pointers (source of truth) | All entities |
| `0INDEX.md` | Contents listing / navigation | All entities |
| `README.md` | Human-readable overview | All entities |
| `CLAUDE.md` etc. | Tool-specific context (auto-generated from 0AGNOSTIC.md) | All entities |
| `.0agnostic/` | Entity-scoped resources (numbered subdirs 01-07+) | All entities |
| `.1merge/` | Tool-specific overrides (6 tools × 3 tiers) | All entities |
| Tool dirs | `.claude/`, `.cursor/`, `.gemini/`, `.codex/`, `.github/` | All entities |
| `layer_N_group/` | Entity internals | All entities |
| `layer_N+1_group/` | Children containers (if entity has children) | Projects & features |
| `layer_N.orchestrator.gab.jsonld` | Entity-level agent orchestrator | All entities |
| `layer_N_99_stages.orchestrator.gab.jsonld` | Stages orchestrator | All entities |

<!-- section_id: "840fb5ba-1ca1-4df9-b3c4-26794efcd583" -->
## Entity Nesting Rules

1. **Projects contain features**: `layer_1` → `layer_2` children in `layer_2_group/layer_2_features/`
2. **Features contain components**: `layer_2` → `layer_3` children in `layer_3_group/layer_3_components/`
3. **Research uses layer_0 for features**: `layer_-1` → `layer_0` children in `layer_0_group/layer_0_features/`
4. **Setup-dependant entities nest by specificity**: OS → Distro → Environment → Local → Apps
5. **Stages don't nest** — they're siblings inside `layer_N_group/layer_N_99_stages/`

<!-- section_id: "b3ea75f1-5f16-4b14-9232-1a5674668020" -->
## Deprecated Patterns

The following patterns are **no longer used**. If found in existing entities, they should be migrated:

| Old Pattern | Replacement |
|-------------|-------------|
| `layer_N_01_ai_manager_system/` | Entity root `0AGNOSTIC.md` (identity lives there now) |
| `layer_N_02_manager_handoff_documents/` | `.0agnostic/05_handoff_documents/` |
| `layer_N_03_sub_layers/` | `.0agnostic/01_knowledge/` (knowledge topics) + `.0agnostic/02_rules/` + `.0agnostic/03_protocols/` |
| `sub_layer_N_XX_knowledge_system/` | `.0agnostic/01_knowledge/` |
| `sub_layer_N_XX_rules/` | `.0agnostic/02_rules/` |
| `sub_layer_N_XX_protocols/` | `.0agnostic/03_protocols/` |
| `sub_layer_N_XX_prompts/` | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` |
| Topic sub-layer directories | `.0agnostic/01_knowledge/[topic]/` (with `principles/`, `docs/`, `resources/`) |

**Migration tool**: `.0agnostic/01_knowledge/layer_stage_system/resources/tools/migrate-sub-layers-to-0agnostic.sh`

---

**PRIMARY SOURCE**: [entity_structure.md](../../../06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md)

**For how to create entities**: [INSTANTIATION_GUIDE.md](./INSTANTIATION_GUIDE.md)
