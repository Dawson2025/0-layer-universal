---
resource_id: "6ccc2e31-9242-438e-97ab-b5e29a3421b0"
resource_type: "document"
resource_name: "INSTRUCTIONS_LAYER_STAGE_SYSTEM_INTERNAL_STRUCTURE"
---
# INSTRUCTIONS: Layer-Stage System Internal Structure

**Created:** 2026-01-15
**Status:** Instructions Complete
**Purpose:** Define the internal layers, features, and components OF the layer-stage system itself

---

<!-- section_id: "caf5b917-7432-4661-b6c7-75923dfc3f6e" -->
## 1. Overview

The layer-stage system is not just a folder of definitions - it is an **entity** that follows its own pattern. It has:
- Its own `layer_1/` (internals)
- Its own `layer_2/` (children - features, components)
- Its own stages for development
- Its own sub-layers for organization

---

<!-- section_id: "78610a38-5d2c-462b-8e2f-42361d1936b3" -->
## 2. Layer-Stage System as a Feature

The layer-stage system becomes `layer_1_feature_layer_stage_system` nested under the universal root:

```
0_layer_universal/
└── layer_1/
    └── layer_1_features/
        └── layer_1_feature_layer_stage_system/       # THE FRAMEWORK ITSELF
```

---

<!-- section_id: "10cd61b9-40f4-4998-a561-715e3c4176b1" -->
## 3. Internal Structure Diagram

```
layer_1_feature_layer_stage_system/
│
│ ═══════════════════════════════════════════════════════════════════════════
│ TOOL-SPECIFIC AT ENTITY ROOT
│ ═══════════════════════════════════════════════════════════════════════════
├── CLAUDE.md                                         # Framework context
├── .claude/
│   ├── settings.json
│   ├── commands/
│   │   ├── create-entity.md                          # /create-entity
│   │   ├── validate-structure.md                     # /validate-structure
│   │   └── migrate-entity.md                         # /migrate-entity
│   ├── agents/
│   │   ├── framework-developer.md
│   │   └── structure-validator.md
│   └── skills/
│       ├── entity-creation/
│       │   └── SKILL.md
│       ├── structure-validation/
│       │   └── SKILL.md
│       └── naming-convention/
│           └── SKILL.md
├── .cursorrules
├── AGENTS.md
├── GEMINI.md
│
│ ═══════════════════════════════════════════════════════════════════════════
│ LAYER 1 INTERNALS (Framework's Own Stuff)
│ ═══════════════════════════════════════════════════════════════════════════
├── layer_1/
│   │
│   ├── layer_1_00_ai_manager_system/
│   │   ├── agnostic/
│   │   │   ├── init_prompt.md                        # How to work on the framework
│   │   │   ├── framework_development_rules.md
│   │   │   └── contribution_guidelines.md
│   │   └── specific/
│   │       └── os/
│   │           └── [nested specificity...]
│   │
│   ├── layer_1_01_manager_handoff_documents/
│   │   ├── layer_1_00_to_universal/
│   │   │   ├── incoming.json
│   │   │   └── outgoing.json
│   │   └── layer_1_01_to_specific/
│   │       ├── incoming.json
│   │       └── outgoing.json
│   │
│   ├── layer_1_02_sub_layers/
│   │   ├── sub_layer_1_01_prompts/
│   │   │   └── framework_prompts.md
│   │   ├── sub_layer_1_02_knowledge_system/
│   │   │   ├── layer_concepts.md
│   │   │   ├── stage_concepts.md
│   │   │   └── entity_concepts.md
│   │   ├── sub_layer_1_03_principles/
│   │   │   ├── nesting_principle.md
│   │   │   ├── inheritance_principle.md
│   │   │   └── separation_principle.md
│   │   ├── sub_layer_1_04_rules/
│   │   │   ├── naming_rules.md
│   │   │   ├── numbering_rules.md
│   │   │   └── structure_rules.md
│   │   └── sub_layer_1_05+_setup_dependant/
│   │       │
│   │       ├── sub_layer_1_05_framework_docs/        # FROM layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers
│   │       │   ├── FLEXIBLE_LAYERING_SYSTEM.md
│   │       │   ├── EXTENDING_THE_FRAMEWORK.md
│   │       │   ├── WORKFLOW_FEATURE_PATTERN.md
│   │       │   ├── FEATURE_TYPE_DECISION_GUIDE.md
│   │       │   ├── UNIVERSAL_SYSTEM_EVALUATION.md
│   │       │   └── CLASSROOM_WORKFLOW_STRATEGIES.md
│   │       │
│   │       ├── sub_layer_1_06_templates/             # FROM layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers
│   │       │   ├── 0_universal_template/
│   │       │   ├── 1_project_template/
│   │       │   ├── 2_sub_project_template/
│   │       │   ├── 2_feature_template/
│   │       │   └── 3_component_template/
│   │       │
│   │       └── sub_layer_1_07_scripts/
│   │           ├── create_workflow_feature.sh
│   │           ├── create_entity.sh
│   │           ├── validate_structure.sh
│   │           └── migrate_naming.sh
│   │
│   └── layer_1_99_stages/                            # Framework's OWN stages
│       ├── stage_1_00_request_gathering/
│       ├── stage_1_01_instructions/
│       │   └── hand_off_documents/
│       │       ├── INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md
│       │       └── INSTRUCTIONS_LAYER_STAGE_SYSTEM_INTERNAL_STRUCTURE.md
│       ├── stage_1_02_planning/
│       │   └── hand_off_documents/
│       │       └── IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.md
│       ├── stage_1_03_design/
│       ├── stage_1_04_development/
│       ├── stage_1_05_testing/
│       ├── stage_1_06_criticism/
│       ├── stage_1_07_fixing/
│       ├── stage_1_08_current_product/
│       │   ├── setup/
│       │   │   ├── instantiation_guide.md
│       │   │   ├── project_creation_checklist.md
│       │   │   ├── feature_creation_checklist.md
│       │   │   └── component_creation_checklist.md
│       │   └── changes/
│       │       ├── verify_paths.sh
│       │       ├── restructuring_migration_protocol.md
│       │       └── traversal_update_protocol.md
│       ├── stage_1_09_archives/
│       └── status.json
│
│ ═══════════════════════════════════════════════════════════════════════════
│ LAYER 2 CHILDREN (Framework's Features & Components)
│ ═══════════════════════════════════════════════════════════════════════════
└── layer_2/
    ├── layer_2_subx1_projects/                       # Sub-projects (if any)
    │
    ├── layer_2_features/                             # FEATURES OF THE FRAMEWORK
    │   │
    │   ├── layer_2_feature_stage_definitions/
    │   ├── layer_2_feature_layer_definitions/
    │   ├── layer_2_feature_context_gathering/
    │   ├── layer_2_feature_handoff_system/
    │   └── layer_2_feature_ai_manager_hierarchy/
    │
    └── layer_2_components/                           # COMPONENTS OF THE FRAMEWORK
        ├── layer_2_component_stage_template/
        ├── layer_2_component_layer_template/
        └── layer_2_component_entity_template/
```

---

<!-- section_id: "e4f39e1b-c364-4043-900c-5e5557b7d57e" -->
## 4. Layer 2 Features (Children of Layer-Stage System)

<!-- section_id: "219ac3f7-ec6b-409f-98f7-268ac6c9dbe9" -->
### 4.1 layer_2_feature_stage_definitions

**Purpose:** Defines the 9 stages and their workflow

```
layer_2_feature_stage_definitions/
├── CLAUDE.md
├── layer_2/
│   ├── layer_2_00_ai_manager_system/
│   │   └── agnostic/
│   │       └── init_prompt.md
│   ├── layer_2_02_sub_layers/
│   │   └── sub_layer_2_05+_setup_dependant/
│   │       └── sub_layer_2_05_stage_docs/
│   │           ├── stage_00_request_gathering.md
│   │           ├── stage_01_instructions.md
│   │           ├── stage_02_planning.md
│   │           ├── stage_03_design.md
│   │           ├── stage_04_development.md
│   │           ├── stage_05_testing.md
│   │           ├── stage_06_criticism.md
│   │           ├── stage_07_fixing.md
│   │           ├── stage_08_current_product.md
│   │           └── stage_09_archives.md
│   └── layer_2_99_stages/
└── layer_3/
    └── layer_3_components/
        ├── layer_3_component_stage_00_template/
        ├── layer_3_component_stage_01_template/
        └── ...
```

**Defines:**
- Stage purposes and objectives
- Entry/exit criteria for each stage
- Stage-to-stage handoff requirements
- Stage numbering conventions

---

<!-- section_id: "86936d7e-b41a-41fb-8745-23aca0fd3f64" -->
### 4.2 layer_2_feature_layer_definitions

**Purpose:** Defines layer numbering, nesting, and entity types

```
layer_2_feature_layer_definitions/
├── CLAUDE.md
├── layer_2/
│   └── layer_2_02_sub_layers/
│       └── sub_layer_2_05+_setup_dependant/
│           └── sub_layer_2_05_layer_docs/
│               ├── layer_numbering.md
│               ├── entity_types.md
│               ├── nesting_rules.md
│               ├── depth_markers.md
│               └── layer_grouping.md
└── layer_3/
    └── layer_3_components/
        ├── layer_3_component_project_definition/
        ├── layer_3_component_feature_definition/
        └── layer_3_component_component_definition/
```

**Defines:**
- Layer numbering system (0, 1, 2, 3...)
- Entity types (projects, features, components)
- Nesting rules (layer_N/ vs layer_N+1/)
- Depth markers (sub*N pattern)
- Layer grouping conventions

---

<!-- section_id: "62362f58-7d2a-4b1e-bf00-87ae02277b0f" -->
### 4.3 layer_2_feature_context_gathering

**Purpose:** Defines how AI gathers relevant context

```
layer_2_feature_context_gathering/
├── CLAUDE.md
├── layer_2/
│   └── layer_2_02_sub_layers/
│       └── sub_layer_2_05+_setup_dependant/
│           └── sub_layer_2_05_context_docs/
│               ├── vertical_chain_rules.md
│               ├── horizontal_sibling_rules.md
│               ├── task_source_identification.md
│               ├── init_prompt_chain.md
│               └── claude_code_discovery.md
└── layer_3/
    └── layer_3_components/
        ├── layer_3_component_vertical_gatherer/
        └── layer_3_component_horizontal_filter/
```

**Defines:**
- Vertical chain (ancestors + descendants) - always relevant
- Horizontal siblings - only when task-relevant
- Task sources: current request, status.json, todo lists
- Init prompt chain traversal
- Claude Code's hierarchical CLAUDE.md discovery

---

<!-- section_id: "a28cb3a1-de9e-4563-8469-003783c32e56" -->
### 4.4 layer_2_feature_handoff_system

**Purpose:** Defines handoff schemas and patterns

```
layer_2_feature_handoff_system/
├── CLAUDE.md
├── layer_2/
│   └── layer_2_02_sub_layers/
│       └── sub_layer_2_05+_setup_dependant/
│           └── sub_layer_2_05_handoff_docs/
│               ├── handoff_schema.md
│               ├── to_universal_pattern.md
│               ├── to_specific_pattern.md
│               ├── stage_handoffs.md
│               └── layer_handoffs.md
└── layer_3/
    └── layer_3_components/
        ├── layer_3_component_incoming_handler/
        └── layer_3_component_outgoing_handler/
```

**Defines:**
- Handoff JSON schema
- `to_universal/` pattern (handoffs UP to parent)
- `to_specific/` pattern (handoffs DOWN to children)
- Stage-to-stage handoffs
- Layer-to-layer handoffs
- incoming.json / outgoing.json structure

---

<!-- section_id: "98eb7487-3202-44d7-8d4c-89908aa27667" -->
### 4.5 layer_2_feature_ai_manager_hierarchy

**Purpose:** Defines the agnostic/specific pattern and tool configurations

```
layer_2_feature_ai_manager_hierarchy/
├── CLAUDE.md
├── layer_2/
│   ├── layer_2_00_ai_manager_system/
│   │   └── agnostic/
│   │       └── init_prompt.md
│   ├── layer_2_02_sub_layers/
│   │   └── sub_layer_2_05+_setup_dependant/
│   │       ├── sub_layer_2_05_pattern_docs/
│   │       │   ├── agnostic_source_pattern.md
│   │       │   ├── specific_nesting_pattern.md
│   │       │   └── tool_config_patterns.md
│   │       └── sub_layer_2_06_templates/
│   │           ├── agnostic_template/
│   │           │   ├── init_prompt_template.md
│   │           │   └── context_rules_template.md
│   │           └── specific_template/
│   │               └── os/
│   │                   └── [os]/
│   │                       └── environment/
│   │                           └── [env]/
│   │                               └── coding_app/
│   │                                   └── [app]/
│   │                                       └── ai_app/
│   │                                           └── [ai]/
│   └── layer_2_99_stages/
│
└── layer_3/
    └── layer_3_components/
        ├── layer_3_component_claude_code_config/
        │   ├── CLAUDE_md_template.md
        │   ├── claude_folder_structure.md
        │   ├── commands_guide.md
        │   ├── agents_guide.md
        │   └── skills_guide.md
        ├── layer_3_component_cursor_config/
        │   └── cursorrules_template.md
        ├── layer_3_component_codex_config/
        │   └── AGENTS_md_template.md
        └── layer_3_component_gemini_config/
            └── GEMINI_md_template.md
```

**Defines:**
- Agnostic source pattern (tool-independent)
- Specific nesting pattern (os → environment → coding_app → ai_app)
- Tool configuration patterns for each AI tool
- Templates for creating agnostic and specific sections

---

<!-- section_id: "7acf1387-fa27-4fad-868f-fa1e7c620ea6" -->
## 5. Sub-Layer Pattern

The sub-layers within the layer-stage system follow the universal pattern:

| Sub-Layer | Purpose |
|-----------|---------|
| `sub_layer_N_01_prompts/` | Prompts for working on this entity |
| `sub_layer_N_02_knowledge_system/` | Knowledge/concepts for this entity |
| `sub_layer_N_03_principles/` | Guiding principles |
| `sub_layer_N_04_rules/` | Enforced rules |
| `sub_layer_N_05+_setup_dependant/` | Expandable: docs, templates, scripts, etc. |

The `05+` indicates this can expand:
- `sub_layer_N_05_framework_docs/`
- `sub_layer_N_06_templates/`
- `sub_layer_N_07_scripts/`
- `sub_layer_N_08_...` (as needed)

---

<!-- section_id: "4f0d81f8-86de-4be3-a937-8568f4bee19b" -->
## 6. Context Gathering Rules

These were defined earlier in our discussion:

<!-- section_id: "04f05297-1268-4031-8d5b-99e17878e514" -->
### 6.1 Vertical Chain (Always Relevant)
```
Ancestors + Descendants = Always in context

Parent Layer
    ↓
Current Entity  ← YOU ARE HERE
    ↓
Child Entities
```

<!-- section_id: "f72c8231-9abb-44ca-a318-9dc8de631a05" -->
### 6.2 Horizontal Siblings (Conditionally Relevant)
```
Only relevant when:
1. Sibling is related to current entity
   AND
2. The relationship is relevant to the current task

Tasks come from:
- Current user request
- status.json (in_progress items)
- Todo lists (pending items)
```

<!-- section_id: "62e1d10f-e0d9-49db-8cd5-bb21d717bae2" -->
### 6.3 Init Prompt Chain
```
Universal init_prompt.md
        ↓
    Layer 1 init_prompt.md
        ↓
    Layer 2 init_prompt.md
        ↓
    ... (current location)

Each init_prompt references:
- UP: Parent's init_prompt
- DOWN: Children's init_prompts (when relevant)
```

---

<!-- section_id: "9ffe8786-47de-4a56-adda-bb720ac43c23" -->
## 7. Mapping: Current → New Locations

| Current Location | New Location |
|-----------------|--------------|
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/` | `layer_1_feature_layer_stage_system/` |
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/` | `.../layer_1/layer_1_99_stages/` |
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_10_current_product/setup/` | `.../stage_1_08_current_product/setup/` |
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_10_current_product/changes/` | `.../stage_1_08_current_product/changes/` |
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` | `.../layer_1/layer_1_02_sub_layers/sub_layer_1_05+_setup_dependant/` |
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/*.md` | `.../sub_layer_1_05_framework_docs/` |
| `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/*_template/` | `.../sub_layer_1_06_templates/` |
| `-1_research/ai_manager_hierarchy_system/` | `.../layer_2/layer_2_features/layer_2_feature_ai_manager_hierarchy/` |

---

<!-- section_id: "751af440-46f4-4d81-8490-5e7226dd6917" -->
## 8. Feature Responsibilities Summary

| Feature | Defines | Implemented At |
|---------|---------|----------------|
| **stage_definitions** | The 9 stages (00-09) | Every entity's `layer_N_99_stages/` |
| **layer_definitions** | Layer numbering, nesting | Every entity's structure |
| **context_gathering** | How AI gathers context | AI behavior when navigating |
| **handoff_system** | Handoff schemas | Every entity's `layer_N_01_manager_handoff_documents/` |
| **ai_manager_hierarchy** | Agnostic/specific pattern | Every entity's `layer_N_00_ai_manager_system/` |

---

<!-- section_id: "da1a4e1b-bdf4-4cc7-a55e-71e71f5a472b" -->
## 9. Success Criteria

- [ ] Layer-stage system exists as `layer_1_feature_layer_stage_system`
- [ ] Has its own `layer_1/` with proper internals
- [ ] Has its own `layer_2/` with 5 features
- [ ] Each feature follows the entity pattern
- [ ] Sub-layers follow 01-05+ pattern
- [ ] All documentation moved to appropriate sub-layers
- [ ] All templates moved to `sub_layer_1_06_templates/`
- [ ] Research moved to `layer_2_feature_ai_manager_hierarchy/`

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_03_instructions/hand_off_documents/INSTRUCTIONS_LAYER_STAGE_SYSTEM_INTERNAL_STRUCTURE.md`

**Last Updated:** 2026-01-15

**Related Documents:**
- `INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md` (overall restructure instructions)
- `../../stage_0_04_planning/hand_off_documents/IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.md` (implementation plan)
