---
resource_id: "d5be89e2-4014-4f82-a74e-5f21d9456914"
resource_type: "document"
resource_name: "IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE"
---
# FULL IMPLEMENTATION PLAN: Layer-Stage System Restructure

**Created:** 2026-01-15
**Status:** Planning
**Purpose:** Complete restructure of the layer-stage system to implement new architecture

---

<!-- section_id: "5c0ce8b9-8c7e-4161-8dfc-bd756bca2ef1" -->
## Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        IMPLEMENTATION PHASES                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  Phase 1: Preparation & Backup                                              │
│  Phase 2: Rename Root Repository                                            │
│  Phase 3: Create Tool-Specific Files at Root                                │
│  Phase 4: Create layer_0/ Structure (Universal Internals)                   │
│  Phase 5: Create layer_1/ Structure (Children Grouping)                     │
│  Phase 6: Create layer_1_feature_layer_stage_system                         │
│  Phase 7: Create layer_2 Features (within layer-stage system)               │
│  Phase 8: Apply Naming Conventions Throughout                               │
│  Phase 9: Create Specific/ Nested Structure Templates                       │
│  Phase 10: Add Stage-Level Tool Configs                                     │
│  Phase 11: Update Documentation & References                                │
│  Phase 12: Verification & Testing                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "2d8bca71-a806-4fb3-94f5-38a12fccba1a" -->
## Target Architecture Summary

<!-- section_id: "ca594f70-c563-4657-93db-68e3248f85e4" -->
### Root Structure (Everything Nested Under Layer 0)

```
0_layer_universal/                                    # ROOT - Claude Code runs from here
│
│ ═══════════════════════════════════════════════════════════════════════════
│ TOOL-SPECIFIC AT ROOT
│ ═══════════════════════════════════════════════════════════════════════════
├── CLAUDE.md
├── .claude/
│   ├── settings.json
│   ├── commands/
│   ├── agents/
│   └── skills/
├── .mcp.json
├── .cursorrules
├── AGENTS.md
├── GEMINI.md
│
│ ═══════════════════════════════════════════════════════════════════════════
│ LAYER 0 INTERNALS
│ ═══════════════════════════════════════════════════════════════════════════
├── layer_0/
│   ├── layer_0_00_ai_manager_system/
│   │   ├── agnostic/
│   │   └── specific/os/...
│   ├── layer_0_01_manager_handoff_documents/
│   ├── layer_0_02_sub_layers/
│   └── layer_0_99_stages/
│
│ ═══════════════════════════════════════════════════════════════════════════
│ LAYER 1 CHILDREN
│ ═══════════════════════════════════════════════════════════════════════════
└── layer_1/
    ├── layer_1_projects/
    ├── layer_1_features/
    │   └── layer_1_feature_layer_stage_system/       # THE FRAMEWORK AS A FEATURE
    └── layer_1_components/
```

<!-- section_id: "7a2821b4-c1b2-4418-8dd3-d1404ffb106f" -->
### AI Manager Hierarchy (Nested Specificity)

```
layer_N_00_ai_manager_system/
├── agnostic/                                 # TOOL-AGNOSTIC SOURCE
│   ├── init_prompt.md
│   ├── context_gathering_rules.md
│   ├── handoff_schema.md
│   └── layer_navigation.md
│
└── specific/                                 # NESTED TOOL-SPECIFIC
    └── os/
        ├── wsl/
        │   └── environment/
        │       ├── local/
        │       │   └── coding_app/
        │       │       ├── cursor_ide/
        │       │       │   └── ai_app/
        │       │       │       ├── claude_code_cli/
        │       │       │       ├── codex_cli/
        │       │       │       ├── gemini_cli/
        │       │       │       └── cursor_agent/
        │       │       ├── vscode/
        │       │       ├── jetbrains/
        │       │       ├── rstudio/
        │       │       └── terminal/
        │       └── cloud/
        │           ├── aws/
        │           ├── gcp/
        │           └── azure/
        ├── linux_ubuntu/
        ├── macos/
        └── windows/
```

---

<!-- section_id: "69ab3ada-fe78-465e-9509-e7c4793244c5" -->
## PHASE 1: Preparation & Backup

<!-- section_id: "09833275-a25d-44e1-a0e8-8852d7c53083" -->
### 1.1 Create Backup
```bash
# Backup current state
cd /home/dawson/dawson-workspace/code
cp -r 0_layer_universal 0_layer_universal_backup_$(date +%Y%m%d_%H%M%S)
```

<!-- section_id: "12106509-374f-4f23-9ff8-375e5cc3623c" -->
### 1.2 Document Current State
```bash
# Generate current structure snapshot
find 0_layer_universal -type d > current_structure_$(date +%Y%m%d).txt
```

<!-- section_id: "df8e6066-de94-47b1-9a8f-adbf5ff23c86" -->
### 1.3 Commit Current State
```bash
cd 0_layer_universal
git add -A
git commit -m "Pre-restructure snapshot: $(date +%Y-%m-%d)"
git push
```

---

<!-- section_id: "700448ca-dda3-4d82-81c5-d9f8da03ae6b" -->
## PHASE 2: Rename Root Repository

<!-- section_id: "9e89f08d-964a-4dff-adc2-6e8585e1db73" -->
### 2.1 Rename Directory
```
BEFORE: /home/dawson/dawson-workspace/code/0_layer_universal/
AFTER:  /home/dawson/dawson-workspace/code/0_layer_universal/
```

```bash
cd /home/dawson/dawson-workspace/code
mv 0_layer_universal 0_layer_universal
```

<!-- section_id: "d349e2d0-1ef0-4e32-8987-de5ce7b419fb" -->
### 2.2 Flatten 0_context
```
BEFORE: 0_layer_universal/0_context/
AFTER:  0_layer_universal/  (contents moved up)
```

```bash
cd 0_layer_universal
mv 0_context/* .
rmdir 0_context
```

---

<!-- section_id: "9f0aee9c-05d9-4c8c-9f4a-ea7c491f77da" -->
## PHASE 3: Create Tool-Specific Files at Root

<!-- section_id: "bec725c0-8605-4efe-8150-5a9f909ab4df" -->
### 3.1 Directory Structure
```
0_layer_universal/
├── CLAUDE.md                              # CREATE
├── .claude/                               # CREATE
│   ├── settings.json
│   ├── commands/
│   │   ├── layer-status.md
│   │   ├── gather-context.md
│   │   ├── stage-advance.md
│   │   └── create-entity.md
│   ├── agents/
│   │   ├── layer-manager.md
│   │   ├── stage-manager.md
│   │   └── context-gatherer.md
│   └── skills/
│       ├── context-gathering/
│       │   └── SKILL.md
│       ├── handoff-creation/
│       │   └── SKILL.md
│       ├── stage-navigation/
│       │   └── SKILL.md
│       └── entity-creation/
│           └── SKILL.md
├── .mcp.json                              # CREATE
├── .cursorrules                           # CREATE
├── AGENTS.md                              # CREATE (OpenAI Codex)
└── GEMINI.md                              # CREATE (Gemini CLI)
```

<!-- section_id: "09568298-9759-4c2b-8b34-49a925da24fc" -->
### 3.2 CLAUDE.md Content Template
```markdown
# 0_layer_universal

## Overview
This is the universal root of the Layer-Stage Framework. All projects, features,
and components are nested under this structure.

## Layer-Stage Framework
- **Layers**: Hierarchical depth (Layer 0 = universal, Layer 1+ = projects/features)
- **Stages**: Workflow phases (01-instructions through 09-archives)
- **Entities**: Projects, features, components - each follows the entity pattern

## Context Gathering Rules
- Vertical chain (ancestors + descendants) is always relevant
- Horizontal siblings only when task-relevant
- Use /gather-context to understand current location

## Commands Available
- `/layer-status` - Show current layer position and status
- `/gather-context` - Gather relevant context from layer hierarchy
- `/stage-advance` - Move to next stage in workflow
- `/create-entity` - Create new project/feature/component

## Structure
- `layer_0/` - Universal framework internals
- `layer_1/` - Projects, features, components nested here
```

<!-- section_id: "1df2bdc6-a758-45d0-a2fe-cffd384b0052" -->
### 3.3 Files to Create

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Universal context for Claude Code |
| `.claude/settings.json` | Claude Code settings |
| `.claude/commands/*.md` | Slash commands |
| `.claude/agents/*.md` | Subagent definitions |
| `.claude/skills/*/SKILL.md` | Model-invoked skills |
| `.mcp.json` | MCP server configuration |
| `.cursorrules` | Cursor IDE rules |
| `AGENTS.md` | OpenAI Codex configuration |
| `GEMINI.md` | Gemini CLI configuration |

---

<!-- section_id: "6540b7af-4e98-4807-8dfa-d9f710214738" -->
## PHASE 4: Create layer_0/ Structure

<!-- section_id: "6fa4e91d-c86c-4ba7-b58e-8982680ade40" -->
### 4.1 Create Grouping Directory
```bash
mkdir -p 0_layer_universal/layer_0
```

<!-- section_id: "b2b7bf58-de56-4d67-8e65-eab24150f266" -->
### 4.2 Move & Rename Universal Internals
```
MOVE & RENAME:
layer_0/0.00_ai_manager_system/     → layer_0/layer_0_00_ai_manager_system/
layer_0/0.01_manager_handoff_documents/ → layer_0/layer_0_01_manager_handoff_documents/
layer_0/0.02_sub_layers/            → layer_0/layer_0_02_sub_layers/
layer_0/layer_0_99_stages/                → layer_0/layer_0_99_stages/
```

<!-- section_id: "f39f1a95-b114-4885-b20d-90cd1e11df51" -->
### 4.3 Create Agnostic/Specific Structure in AI Manager
```
layer_0/layer_0_00_ai_manager_system/
├── agnostic/                                  # CREATE
│   ├── init_prompt.md                         # Universal init prompt
│   ├── context_gathering_rules.md
│   ├── handoff_schema.md
│   └── layer_navigation.md
│
└── specific/                                  # CREATE (template structure)
    └── os/
        ├── wsl/
        │   └── environment/
        │       ├── local/
        │       │   └── coding_app/
        │       │       ├── cursor_ide/
        │       │       │   └── ai_app/
        │       │       │       ├── claude_code_cli/
        │       │       │       ├── codex_cli/
        │       │       │       ├── gemini_cli/
        │       │       │       └── cursor_agent/
        │       │       ├── vscode/
        │       │       │   └── ai_app/...
        │       │       ├── jetbrains/
        │       │       ├── rstudio/
        │       │       └── terminal/
        │       │           └── ai_app/...
        │       └── cloud/
        │           ├── aws/
        │           ├── gcp/
        │           └── azure/
        ├── linux_ubuntu/
        │   └── environment/...
        ├── macos/
        │   └── environment/...
        └── windows/
            └── environment/...
```

<!-- section_id: "a1fada0e-9d56-46e8-a1c0-928277ea4bed" -->
### 4.4 Rename Sub-layers
```
RENAME:
sub_layer_0_01_* → sub_layer_0_01_*
sub_layer_0_02_* → sub_layer_0_02_*
...etc
```

<!-- section_id: "bef18abd-e16f-48ba-8042-2c47891138b1" -->
### 4.5 Rename Stages
```
RENAME:
stage_0_01_* → stage_0_01_*
stage_0_02_* → stage_0_02_*
...etc
```

<!-- section_id: "f7a26afb-f3e6-455b-999e-48c80ad4085b" -->
### 4.6 Final layer_0/ Structure
```
layer_0/
├── layer_0_00_ai_manager_system/
│   ├── agnostic/
│   │   ├── init_prompt.md
│   │   ├── context_gathering_rules.md
│   │   ├── handoff_schema.md
│   │   └── layer_navigation.md
│   └── specific/
│       └── os/wsl/environment/local/coding_app/terminal/ai_app/claude_code_cli/
│
├── layer_0_01_manager_handoff_documents/
│   ├── layer_0_00_to_universal/
│   │   ├── incoming.json
│   │   └── outgoing.json
│   └── layer_0_01_to_specific/
│       ├── incoming.json
│       └── outgoing.json
│
├── layer_0_02_sub_layers/
│   ├── sub_layer_0_01_knowledge_system/
│   ├── sub_layer_0_01_knowledge_system/
│   ├── sub_layer_0_03_principles/
│   ├── sub_layer_0_02_rules/
│   └── sub_layer_0_05+_setup_dependant/
│
└── layer_0_99_stages/
    ├── stage_0_03_instructions/
    ├── stage_0_04_planning/
    ├── stage_0_05_design/
    ├── stage_0_06_development/
    ├── stage_0_07_testing/
    ├── stage_0_08_criticism/
    ├── stage_0_09_fixing/
    ├── stage_0_10_current_product/
    ├── stage_0_11_archives/
    └── status_0.json
```

---

<!-- section_id: "085b5b58-1d95-43b6-abea-99658b9a6c74" -->
## PHASE 5: Create layer_1/ Structure

<!-- section_id: "d395115d-48f0-44bf-9021-d574a9d3025a" -->
### 5.1 Create Grouping Directory
```bash
mkdir -p 0_layer_universal/layer_1/layer_1_projects
mkdir -p 0_layer_universal/layer_1/layer_1_features
mkdir -p 0_layer_universal/layer_1/layer_1_components
```

<!-- section_id: "92584afc-bfec-4587-8607-915f3ac12a97" -->
### 5.2 Move Existing Content
```
MOVE:
layer_1_project/     → layer_1/layer_1_projects/layer_1_project_default/
layer_2_features/    → (will be restructured in Phase 6)
layer_3_components/  → (will be restructured in Phase 6)
```

<!-- section_id: "37ccde08-dce4-4dcb-b2c5-6589cb2d2b35" -->
### 5.3 Final layer_1/ Structure
```
layer_1/
├── layer_1_projects/
│   ├── layer_1_project_school/              # Future: submodule to 1_school
│   ├── layer_1_project_work/                # Future: submodule
│   └── layer_1_project_personal/            # Future: submodule
│
├── layer_1_features/
│   └── layer_1_feature_layer_stage_system/  # Created in Phase 6
│
└── layer_1_components/
```

---

<!-- section_id: "d807b2d5-b510-479e-b78d-5a302eda51a5" -->
## PHASE 6: Create layer_1_feature_layer_stage_system

<!-- section_id: "5ac574f8-27a9-4240-94c5-2cfd268b6137" -->
### 6.1 Create Feature Directory
```bash
mkdir -p layer_1/layer_1_features/layer_1_feature_layer_stage_system
```

<!-- section_id: "4e63e49d-6506-48de-a25b-9aa2c8a69638" -->
### 6.2 Create Tool-Specific at Feature Root
```
layer_1_feature_layer_stage_system/
├── CLAUDE.md
├── .claude/
│   ├── commands/
│   ├── agents/
│   └── skills/
```

<!-- section_id: "75ecb490-31da-4e4c-883b-d4615ffcf38b" -->
### 6.3 Create layer_1/ (Feature's Internals)
```
layer_1_feature_layer_stage_system/layer_1/
├── layer_1_00_ai_manager_system/
│   ├── agnostic/
│   │   └── init_prompt.md                    # How to work on the framework
│   └── specific/
│       └── os/...
│
├── layer_1_01_manager_handoff_documents/
│
├── layer_1_02_sub_layers/
│   ├── sub_layer_1_01_prompts/
│   ├── sub_layer_1_02_knowledge_system/
│   ├── sub_layer_1_03_principles/
│   ├── sub_layer_1_04_rules/
│   └── sub_layer_1_05+_setup_dependant/
│       ├── sub_layer_1_05_framework_docs/    # MOVE from layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers
│       │   ├── FLEXIBLE_LAYERING_SYSTEM.md
│       │   ├── EXTENDING_THE_FRAMEWORK.md
│       │   ├── WORKFLOW_FEATURE_PATTERN.md
│       │   ├── FEATURE_TYPE_DECISION_GUIDE.md
│       │   └── UNIVERSAL_SYSTEM_EVALUATION.md
│       ├── sub_layer_1_06_templates/         # MOVE templates
│       │   ├── 0_universal_template/
│       │   ├── 1_project_template/
│       │   ├── 2_feature_template/
│       │   └── 3_component_template/
│       └── sub_layer_1_07_scripts/
│           └── create_workflow_feature.sh
│
└── layer_1_99_stages/
    ├── stage_1_01_instructions/
    ├── stage_1_02_planning/
    ├── stage_1_03_design/
    ├── stage_1_04_development/
    ├── stage_1_05_testing/
    ├── stage_1_06_criticism/
    ├── stage_1_07_fixing/
    ├── stage_1_08_current_product/           # MOVE from layer_1/layer_1_features/layer_1_feature_layer_stage_system
    │   ├── setup/
    │   │   ├── instantiation_guide.md
    │   │   ├── project_creation_checklist.md
    │   │   ├── feature_creation_checklist.md
    │   │   └── component_creation_checklist.md
    │   └── changes/
    │       ├── verify_paths.sh
    │       ├── restructuring_migration_protocol.md
    │       └── traversal_update_protocol.md
    ├── stage_1_09_archives/
    └── status.json
```

<!-- section_id: "47ad0613-9a10-4421-941e-0d0f10b6e038" -->
### 6.4 Create layer_2/ (Feature's Children)
```
layer_1_feature_layer_stage_system/layer_2/
├── layer_2_subx1_projects/
├── layer_2_features/                         # Created in Phase 7
└── layer_2_components/
```

---

<!-- section_id: "69482106-3b34-43f7-ac1e-15513f705f5f" -->
## PHASE 7: Create layer_2 Features (Within Layer-Stage System)

<!-- section_id: "4f09c367-2d32-4d7d-9997-6fdf2b8ba137" -->
### 7.1 Features to Create
```
layer_1_feature_layer_stage_system/layer_2/layer_2_features/
│
├── layer_2_feature_stage_definitions/        # Defines the 9 stages
│   ├── CLAUDE.md
│   ├── layer_2/
│   │   ├── layer_2_00_ai_manager_system/
│   │   ├── layer_2_02_sub_layers/
│   │   │   └── sub_layer_2_05+_setup_dependant/
│   │   │       └── sub_layer_2_05_stage_docs/
│   │   │           ├── stage_00_request_gathering.md
│   │   │           ├── stage_01_instructions.md
│   │   │           ├── stage_02_planning.md
│   │   │           ├── stage_03_design.md
│   │   │           ├── stage_04_development.md
│   │   │           ├── stage_05_testing.md
│   │   │           ├── stage_06_criticism.md
│   │   │           ├── stage_07_fixing.md
│   │   │           ├── stage_08_current_product.md
│   │   │           └── stage_09_archives.md
│   │   └── layer_2_99_stages/
│   └── layer_3/
│
├── layer_2_feature_layer_definitions/        # Defines layer numbering, nesting
│   ├── CLAUDE.md
│   ├── layer_2/
│   │   └── layer_2_02_sub_layers/
│   │       └── sub_layer_2_05+_setup_dependant/
│   │           └── sub_layer_2_05_layer_docs/
│   │               ├── layer_numbering.md
│   │               ├── entity_types.md       # projects, features, components
│   │               ├── nesting_rules.md
│   │               └── depth_markers.md      # sub*N pattern
│   └── layer_3/
│
├── layer_2_feature_context_gathering/        # How AI gathers context
│   ├── CLAUDE.md
│   ├── layer_2/
│   │   └── layer_2_02_sub_layers/
│   │       └── sub_layer_2_05+_setup_dependant/
│   │           └── sub_layer_2_05_context_docs/
│   │               ├── vertical_chain_rules.md
│   │               ├── horizontal_sibling_rules.md
│   │               ├── task_source_identification.md
│   │               └── init_prompt_chain.md
│   └── layer_3/
│
├── layer_2_feature_handoff_system/           # Handoff schemas, to/from
│   ├── CLAUDE.md
│   ├── layer_2/
│   │   └── layer_2_02_sub_layers/
│   │       └── sub_layer_2_05+_setup_dependant/
│   │           └── sub_layer_2_05_handoff_docs/
│   │               ├── handoff_schema.md
│   │               ├── to_universal_pattern.md
│   │               ├── to_specific_pattern.md
│   │               └── stage_handoffs.md
│   └── layer_3/
│
└── layer_2_feature_ai_manager_hierarchy/     # AI manager/worker system
    ├── CLAUDE.md
    ├── layer_2/
    │   ├── layer_2_00_ai_manager_system/
    │   ├── layer_2_02_sub_layers/
    │   │   └── sub_layer_2_05+_setup_dependant/
    │   │       ├── sub_layer_2_05_pattern_docs/
    │   │       │   ├── agnostic_source_pattern.md
    │   │       │   ├── specific_nesting_pattern.md  # os→env→app→ai
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

---

<!-- section_id: "a5d6fa3c-4d26-41f9-a698-8f14f20afa00" -->
## PHASE 8: Apply Naming Conventions Throughout

<!-- section_id: "cb19a2da-7dee-4d53-b841-4fbe0249a8f1" -->
### 8.1 Rename All Directories
```
PATTERN CHANGES:
0.00_* → layer_0_00_*
0.01_* → layer_0_01_*
0.02_* → layer_0_02_*
0.99_* → layer_0_99_*

sub_layer_0_01_* → sub_layer_0_01_*
sub_layer_0_02_* → sub_layer_0_02_*

stage_0_01_* → stage_0_01_*
stage_0_02_* → stage_0_02_*

(Apply same pattern at all layer depths)
```

<!-- section_id: "c611942e-036f-422a-a051-279cd336be54" -->
### 8.2 Rename Status Files
```
status.json → status_N.json (where N = layer number)
```

<!-- section_id: "e81080f8-fa8d-4259-9649-9ddb167debd8" -->
### 8.3 Update All Internal References
- Update all markdown files that reference old paths
- Update all scripts that use old naming
- Update handoff documents

---

<!-- section_id: "7867d069-0799-44e8-999d-f4e7016f14aa" -->
## PHASE 9: Create Specific/ Nested Structure Templates

<!-- section_id: "a05ba5c2-dc34-413c-af7c-6bfadd1229b5" -->
### 9.1 Create Template Script
```bash
#!/bin/bash
# create_specific_structure.sh

create_ai_apps() {
    local base=$1
    mkdir -p "$base/claude_code_cli"
    mkdir -p "$base/codex_cli"
    mkdir -p "$base/gemini_cli"
    mkdir -p "$base/cursor_agent"
}

create_coding_apps() {
    local base=$1
    for app in cursor_ide vscode jetbrains rstudio terminal; do
        mkdir -p "$base/$app/ai_app"
        create_ai_apps "$base/$app/ai_app"
    done
}

create_environments() {
    local base=$1
    mkdir -p "$base/local/coding_app"
    create_coding_apps "$base/local/coding_app"

    for cloud in aws gcp azure; do
        mkdir -p "$base/cloud/$cloud/coding_app"
        create_coding_apps "$base/cloud/$cloud/coding_app"
    done
}

create_os_structure() {
    local base=$1
    for os in wsl linux_ubuntu macos windows; do
        mkdir -p "$base/$os/environment"
        create_environments "$base/$os/environment"
    done
}

# Usage: create_os_structure "/path/to/specific/os"
```

---

<!-- section_id: "98fa12e3-b2da-41c6-8965-24a233bb8316" -->
## PHASE 10: Add Stage-Level Tool Configs

<!-- section_id: "d30a9e96-5267-4de6-b6ec-223ee79c3502" -->
### 10.1 For Each Stage, Create:
```
stage_N_XX_<name>/
├── CLAUDE.md                                  # Stage-specific context
├── .claude/
│   ├── commands/                              # Stage-specific commands
│   ├── agents/                                # Stage-specific agents
│   └── skills/                                # Stage-specific skills
├── docs/
├── hand_off_documents/
│   ├── from_previous_stage.json
│   └── to_next_stage.json
└── work/
```

<!-- section_id: "f4f44d36-4eaf-4cef-9c1d-b6a340bd2eeb" -->
### 10.2 Stage-Specific CLAUDE.md Template
```markdown
# Stage N.XX: <Stage Name>

## Purpose
<Stage purpose from stage_definitions>

## Entry Criteria
- <What must be true to enter this stage>

## Exit Criteria
- <What must be true to exit this stage>

## Tasks
- <Typical tasks for this stage>

## Handoffs
- **From Previous**: <What you receive>
- **To Next**: <What you produce>
```

---

<!-- section_id: "f2c0bbc2-ae7f-45b4-8f8b-51649c225403" -->
## PHASE 11: Update Documentation & References

<!-- section_id: "221692e2-7845-476c-83e4-bb286bc8d69f" -->
### 11.1 Files to Update
- `MASTER_DOCUMENTATION_INDEX.md`
- `SYSTEM_OVERVIEW.md`
- `README.md` (root and all entity READMEs)
- `USAGE_GUIDE.md`
- All framework docs in `sub_layer_1_05_framework_docs/`

<!-- section_id: "3026057f-fbb8-4609-9e9c-8c58227fd679" -->
### 11.2 Update verify_paths.sh
```bash
# Update all path references to new structure
```

<!-- section_id: "628c5ac2-b16c-4a0d-bc66-9530c0a89246" -->
### 11.3 Create Migration Guide
```markdown
# Migration Guide: Old → New Structure

## Path Mappings
| Old Path | New Path |
|----------|----------|
| layer_1/layer_1_features/layer_1_feature_layer_stage_system/ | layer_1/layer_1_features/layer_1_feature_layer_stage_system/ |
| layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/ | .../layer_1_02_sub_layers/sub_layer_1_05+_setup_dependant/ |
| layer_0/ | layer_0/ |
| -1_research/ | .../layer_2_features/layer_2_feature_ai_manager_hierarchy/ |
```

---

<!-- section_id: "2c420177-0ad2-4a8b-bc61-0efda7d13253" -->
## PHASE 12: Verification & Testing

<!-- section_id: "eedcf2f8-f487-4d9c-abb3-a0742a9fee29" -->
### 12.1 Run Verification Script
```bash
# Updated verify_paths.sh with new paths
./verify_paths.sh
```

<!-- section_id: "7af84cc4-5e78-4d4f-9991-87281b8da0f2" -->
### 12.2 Test Claude Code Discovery
```bash
# From different locations, verify CLAUDE.md inheritance works
cd 0_layer_universal
claude
# Verify all skills/commands/agents are available

cd layer_1/layer_1_features/layer_1_feature_layer_stage_system
claude
# Verify inherited + local configs work
```

<!-- section_id: "c5ff8f8d-459c-42df-ad4b-f7aa572bd6a2" -->
### 12.3 Verification Checklist
- [ ] All directories follow new naming (`layer_N_XX_*`)
- [ ] All entities have CLAUDE.md and .claude/
- [ ] Agnostic/specific structure exists in all ai_manager_systems
- [ ] All stages have stage-level configs
- [ ] All handoff documents follow schema
- [ ] All sub_layers follow 01-05+ pattern
- [ ] No stale references to old paths
- [ ] Git status is clean

---

<!-- section_id: "4bce2afa-e8ed-4829-8024-d1b49d543ae4" -->
## SUBAGENT EXECUTION STRATEGY

<!-- section_id: "3a04725b-f3ad-474e-964d-c64fda30f333" -->
### Overview
Each phase should be executed by dedicated subagents to maximize efficiency and enable parallel execution where possible.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SUBAGENT EXECUTION ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐                                                            │
│  │   MANAGER   │  Orchestrates all subagents, tracks progress               │
│  │   (Main)    │  Makes decisions when phases complete                      │
│  └──────┬──────┘                                                            │
│         │                                                                   │
│    ┌────┴────┬────────┬────────┬────────┬────────┬────────┐                │
│    │         │        │        │        │        │        │                │
│    ▼         ▼        ▼        ▼        ▼        ▼        ▼                │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐            │
│ │Prep  │ │Root  │ │Tools │ │Layer0│ │Layer1│ │LSS   │ │Verify│            │
│ │Agent │ │Agent │ │Agent │ │Agent │ │Agent │ │Agent │ │Agent │            │
│ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "8da79561-cfb2-4d4c-aab6-c0c0c67a5955" -->
### Subagent Assignments

| Phase | Subagent Name | Type | Description |
|-------|--------------|------|-------------|
| 1 | `prep-backup-agent` | Bash | Create backups, document current state, git commit |
| 2 | `root-restructure-agent` | Bash | Rename root, flatten 0_context |
| 3 | `tool-files-agent` | general-purpose | Create CLAUDE.md, .claude/, .cursorrules, etc. |
| 4 | `layer0-structure-agent` | general-purpose | Create layer_0/ with all internals |
| 5 | `layer1-structure-agent` | general-purpose | Create layer_1/ groupings |
| 6 | `lss-feature-agent` | general-purpose | Create layer_1_feature_layer_stage_system |
| 7a | `stage-defs-agent` | general-purpose | Create layer_2_feature_stage_definitions |
| 7b | `layer-defs-agent` | general-purpose | Create layer_2_feature_layer_definitions |
| 7c | `context-gather-agent` | general-purpose | Create layer_2_feature_context_gathering |
| 7d | `handoff-sys-agent` | general-purpose | Create layer_2_feature_handoff_system |
| 7e | `ai-manager-agent` | general-purpose | Create layer_2_feature_ai_manager_hierarchy |
| 8 | `naming-convention-agent` | Bash | Rename all directories to new convention |
| 9 | `specific-template-agent` | Bash | Create nested specific/ structures |
| 10 | `stage-configs-agent` | general-purpose | Add stage-level tool configs |
| 11 | `docs-update-agent` | general-purpose | Update all documentation |
| 12 | `verify-agent` | Bash | Run verification, test Claude Code |

<!-- section_id: "ac011aae-a309-47ee-ad28-4971c7f455e5" -->
### Parallel Execution Batches

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PARALLEL BATCH 1: Sequential Foundation (must complete in order)           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phase 1 (prep) ──► Phase 2 (root)                                         │
│  [SEQUENTIAL - dependencies between phases]                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  PARALLEL BATCH 2: Tool Files + Structure (can run in parallel)             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐            │
│  │ Phase 3        │    │ Phase 4        │    │ Phase 5        │            │
│  │ (Tool Files)   │    │ (layer_0)      │    │ (layer_1)      │            │
│  └────────────────┘    └────────────────┘    └────────────────┘            │
│  [PARALLEL - no dependencies between these phases]                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  PARALLEL BATCH 3: Layer-Stage System Feature                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phase 6 (create layer_1_feature_layer_stage_system)                        │
│  [SEQUENTIAL - must complete before Phase 7]                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  PARALLEL BATCH 4: Layer 2 Features (all 5 can run in parallel)             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐│
│  │ Phase 7a   │ │ Phase 7b   │ │ Phase 7c   │ │ Phase 7d   │ │ Phase 7e   ││
│  │ stage_defs │ │ layer_defs │ │ context    │ │ handoff    │ │ ai_manager ││
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘│
│  [PARALLEL - no dependencies between features]                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  PARALLEL BATCH 5: Cleanup & Convention (can run in parallel)               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐            │
│  │ Phase 8        │    │ Phase 9        │    │ Phase 10       │            │
│  │ (Naming)       │    │ (Specific/)    │    │ (Stage Configs)│            │
│  └────────────────┘    └────────────────┘    └────────────────┘            │
│  [PARALLEL - operate on different parts of the structure]                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  PARALLEL BATCH 6: Documentation + Verification (sequential)                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phase 11 (docs) ──► Phase 12 (verify)                                     │
│  [SEQUENTIAL - verify depends on docs being updated]                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "36eac8b2-6911-41ad-8a14-cefb5b19bd34" -->
### Subagent Prompts

#### Phase 1: prep-backup-agent
```
You are the Preparation & Backup Agent.

Tasks:
1. Create backup: cp -r 0_layer_universal 0_layer_universal_backup_$(date +%Y%m%d)
2. Document current structure: find 0_layer_universal -type d > current_structure.txt
3. Git commit: git add -A && git commit -m "Pre-restructure snapshot"

Report: List of backup files created, git commit hash
```

#### Phase 2: root-restructure-agent
```
You are the Root Restructure Agent.

Tasks:
1. Rename directory: mv 0_layer_universal 0_layer_universal
2. Flatten 0_context: mv 0_layer_universal/0_context/* 0_layer_universal/ && rmdir 0_layer_universal/0_context

Constraints:
- Preserve git history
- Do not lose any files

Report: Before/after directory listing
```

#### Phase 3: tool-files-agent
```
You are the Tool Files Agent.

Tasks:
1. Create CLAUDE.md at root with universal context
2. Create .claude/ folder with:
   - settings.json
   - commands/ (layer-status.md, gather-context.md, stage-advance.md, create-entity.md)
   - agents/ (layer-manager.md, stage-manager.md, context-gatherer.md)
   - skills/ (context-gathering/, handoff-creation/, stage-navigation/, entity-creation/)
3. Create .cursorrules
4. Create AGENTS.md
5. Create GEMINI.md
6. Create .mcp.json

Report: List of files created with line counts
```

#### Phase 7 (all features - parallel)
```
You are the [Feature Name] Agent.

Tasks:
1. Create layer_2_feature_[name]/ directory structure
2. Create CLAUDE.md for feature
3. Create layer_2/ (internals) with:
   - layer_2_00_ai_manager_system/ (agnostic/ and specific/)
   - layer_2_02_sub_layers/ with setup_dependant content
   - layer_2_99_stages/
4. Create layer_3/ (children) with empty groupings
5. Populate feature-specific documentation

Report: Directory tree of created feature
```

---

<!-- section_id: "430c1f6a-8654-409c-bfb2-c115b0f8a1aa" -->
## PHASE EXECUTION ORDER (WITH SUBAGENTS)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EXECUTION TIMELINE WITH SUBAGENTS                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BATCH 1 (Sequential)                                                       │
│  ════════════════════                                                       │
│  Phase 1 [prep-backup-agent] ──► Phase 2 [root-restructure-agent]          │
│                                                                             │
│                              ↓                                              │
│  BATCH 2 (Parallel)                                                         │
│  ══════════════════                                                         │
│  ┌─────────────────┬──────────────────┬─────────────────┐                  │
│  │ Phase 3         │ Phase 4          │ Phase 5         │                  │
│  │ [tool-files]    │ [layer0-struct]  │ [layer1-struct] │                  │
│  └─────────────────┴──────────────────┴─────────────────┘                  │
│                                                                             │
│                              ↓                                              │
│  BATCH 3 (Sequential)                                                       │
│  ════════════════════                                                       │
│  Phase 6 [lss-feature-agent]                                               │
│                                                                             │
│                              ↓                                              │
│  BATCH 4 (Parallel - 5 subagents)                                          │
│  ════════════════════════════════                                          │
│  ┌───────────┬───────────┬───────────┬───────────┬───────────┐            │
│  │ 7a        │ 7b        │ 7c        │ 7d        │ 7e        │            │
│  │ [stage]   │ [layer]   │ [context] │ [handoff] │ [ai-mgr]  │            │
│  └───────────┴───────────┴───────────┴───────────┴───────────┘            │
│                                                                             │
│                              ↓                                              │
│  BATCH 5 (Parallel)                                                         │
│  ══════════════════                                                         │
│  ┌─────────────────┬──────────────────┬─────────────────┐                  │
│  │ Phase 8         │ Phase 9          │ Phase 10        │                  │
│  │ [naming-conv]   │ [specific-tmpl]  │ [stage-configs] │                  │
│  └─────────────────┴──────────────────┴─────────────────┘                  │
│                                                                             │
│                              ↓                                              │
│  BATCH 6 (Sequential)                                                       │
│  ════════════════════                                                       │
│  Phase 11 [docs-update-agent] ──► Phase 12 [verify-agent]                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "b5af99e3-5019-43a6-8d63-2fc543703c03" -->
### Total Subagent Count
- **Batch 1**: 2 sequential
- **Batch 2**: 3 parallel
- **Batch 3**: 1 sequential
- **Batch 4**: 5 parallel
- **Batch 5**: 3 parallel
- **Batch 6**: 2 sequential

**Maximum Parallelism**: 5 subagents (Batch 4)
**Total Unique Subagents**: 16

---

<!-- section_id: "fba5c291-0685-4356-8785-6c69139e6f91" -->
## SUMMARY: What Gets Created/Moved

| Action | Count |
|--------|-------|
| **Directories renamed** | ~50+ |
| **New directories created** | ~100+ |
| **CLAUDE.md files created** | ~20+ |
| **.claude/ folders created** | ~20+ |
| **Documentation files updated** | ~30+ |
| **New feature folders** | 5 (stage_defs, layer_defs, context, handoff, ai_manager) |

---

<!-- section_id: "08e8fa73-7686-4faf-8694-afad28a9d578" -->
## Key Architectural Decisions

<!-- section_id: "de5e2830-0dc3-4789-881c-91a70e1fda08" -->
### 1. Everything Nested Under Layer 0
- Enables Claude Code's hierarchical CLAUDE.md discovery
- Universal skills/commands/agents inherited everywhere
- Single root for all projects

<!-- section_id: "2fa7599a-9f23-470c-8136-b24aa49f654a" -->
### 2. Layer-Stage System as a Feature
- The framework itself follows its own pattern
- Has its own stages for development
- Has child features for each major concept

<!-- section_id: "94833c9e-c360-482e-bf25-3e6bea3b63ee" -->
### 3. Agnostic → Specific Pattern
- Tool-agnostic init_prompt.md is the source of truth
- Tool-specific files (CLAUDE.md, .cursorrules, etc.) generated from it
- Nested specificity: os → environment → coding_app → ai_app

<!-- section_id: "9f17114b-8938-415c-be98-879e1e0af6ca" -->
### 4. AI Manager Hierarchy as a Feature
- Defines the agnostic/specific pattern
- Contains templates for each AI tool
- Implemented at every entity's layer_N_00_ai_manager_system/

---

<!-- section_id: "7d2fdfb6-e993-4a20-9153-a174bf91893a" -->
## Files to Delete After Migration

```
DELETE (after content moved):
- layer_1/layer_1_features/layer_1_feature_layer_stage_system/           # Merged into layer_1_feature_layer_stage_system
- layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/        # Moved to sub_layer_1_05_framework_docs
- layer_0/                 # Restructured into layer_0/
- -1_research/                       # Moved to layer_2_feature_ai_manager_hierarchy
- layer_1_project/                   # Restructured
- layer_2_features/                  # Restructured
- layer_3_components/                # Restructured
```

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_04_planning/IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.md`

**Last Updated:** 2026-01-15

**Status:** Ready for execution
