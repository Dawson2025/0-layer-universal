---
resource_id: "b4302628-9229-4cbe-a1f3-5a506c704543"
resource_type: "document"
resource_name: "IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.sync-conflict-20260126-102107-IF2WOGZ"
---
# FULL IMPLEMENTATION PLAN: Layer-Stage System Restructure

**Created:** 2026-01-15
**Status:** Planning
**Purpose:** Complete restructure of the layer-stage system to implement new architecture

---

<!-- section_id: "da93508b-0ffd-4f88-9fa6-c8fb1faacf35" -->
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

<!-- section_id: "0b89d9e4-59e5-4ac9-bab2-c74c08828cc0" -->
## Target Architecture Summary

<!-- section_id: "6d5eb765-007e-4421-b1cc-b7d664b2b8b2" -->
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

<!-- section_id: "490ccf57-0346-4003-b652-42e78103c046" -->
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

<!-- section_id: "0defb0e8-31d2-41e1-9a18-d4442b8d463f" -->
## PHASE 1: Preparation & Backup

<!-- section_id: "a6f29e38-6c31-4ce3-94f9-09e4623bf0ce" -->
### 1.1 Create Backup
```bash
# Backup current state
cd /home/dawson/dawson-workspace/code
cp -r 0_layer_universal 0_layer_universal_backup_$(date +%Y%m%d_%H%M%S)
```

<!-- section_id: "01b53e15-387e-4ad5-9fc6-27cbb478510b" -->
### 1.2 Document Current State
```bash
# Generate current structure snapshot
find 0_layer_universal -type d > current_structure_$(date +%Y%m%d).txt
```

<!-- section_id: "251b1697-732c-4708-97af-705c6ff462f7" -->
### 1.3 Commit Current State
```bash
cd 0_layer_universal
git add -A
git commit -m "Pre-restructure snapshot: $(date +%Y-%m-%d)"
git push
```

---

<!-- section_id: "7f73a5e7-2797-4c46-86e0-98f9b1e4ed56" -->
## PHASE 2: Rename Root Repository

<!-- section_id: "2f7510b1-76c0-42b3-99d2-b2f151f4d6b5" -->
### 2.1 Rename Directory
```
BEFORE: /home/dawson/dawson-workspace/code/0_layer_universal/
AFTER:  /home/dawson/dawson-workspace/code/0_layer_universal/
```

```bash
cd /home/dawson/dawson-workspace/code
mv 0_layer_universal 0_layer_universal
```

<!-- section_id: "ba067f34-669e-413c-904e-5efeb92123d8" -->
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

<!-- section_id: "a7952023-5307-4251-b455-cc7b1c0a2c46" -->
## PHASE 3: Create Tool-Specific Files at Root

<!-- section_id: "a6817314-f1d2-4110-93cc-df84ac090001" -->
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

<!-- section_id: "ef0a6994-bfcc-4f2e-911d-fe0a6723a9bf" -->
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

<!-- section_id: "f31ed7bb-aa6e-47e8-b6ce-6dd2449af76b" -->
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

<!-- section_id: "cd81ad83-e69d-4448-bff8-b07a424c220b" -->
## PHASE 4: Create layer_0/ Structure

<!-- section_id: "af2d9e24-5723-4255-b4ed-69beb2d4bd70" -->
### 4.1 Create Grouping Directory
```bash
mkdir -p 0_layer_universal/layer_0
```

<!-- section_id: "34fb3428-5634-4e2b-b20b-df9a80d806ae" -->
### 4.2 Move & Rename Universal Internals
```
MOVE & RENAME:
layer_0/0.00_ai_manager_system/     → layer_0/layer_0_00_ai_manager_system/
layer_0/0.01_manager_handoff_documents/ → layer_0/layer_0_01_manager_handoff_documents/
layer_0/0.02_sub_layers/            → layer_0/layer_0_02_sub_layers/
layer_0/layer_0_99_stages/                → layer_0/layer_0_99_stages/
```

<!-- section_id: "d909139f-eed3-43df-8315-649cd5f8ca39" -->
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

<!-- section_id: "9b6be8ee-3e20-4587-a50f-22e403af202b" -->
### 4.4 Rename Sub-layers
```
RENAME:
sub_layer_0_01_* → sub_layer_0_01_*
sub_layer_0_02_* → sub_layer_0_02_*
...etc
```

<!-- section_id: "470f7da5-1b2f-4671-912b-a66c756b67bf" -->
### 4.5 Rename Stages
```
RENAME:
stage_0_01_* → stage_0_01_*
stage_0_02_* → stage_0_02_*
...etc
```

<!-- section_id: "def5f3ec-00fb-4ee4-a0ca-4ade114ce427" -->
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
│   ├── sub_layer_0_01_prompts/
│   ├── sub_layer_0_02_knowledge_system/
│   ├── sub_layer_0_03_principles/
│   ├── sub_layer_0_04_rules/
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

<!-- section_id: "73324773-09b9-429a-b942-c4dc8ee60493" -->
## PHASE 5: Create layer_1/ Structure

<!-- section_id: "adc76e01-de00-4908-9743-2460744428f7" -->
### 5.1 Create Grouping Directory
```bash
mkdir -p 0_layer_universal/layer_1/layer_1_projects
mkdir -p 0_layer_universal/layer_1/layer_1_features
mkdir -p 0_layer_universal/layer_1/layer_1_components
```

<!-- section_id: "5a696937-eb75-4782-8449-902541d12e29" -->
### 5.2 Move Existing Content
```
MOVE:
layer_1_project/     → layer_1/layer_1_projects/layer_1_project_default/
layer_2_features/    → (will be restructured in Phase 6)
layer_3_components/  → (will be restructured in Phase 6)
```

<!-- section_id: "d69ff298-0bba-4ddd-b458-bc5dc546a81d" -->
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

<!-- section_id: "b19c8662-d111-4fdc-943e-14721b06809f" -->
## PHASE 6: Create layer_1_feature_layer_stage_system

<!-- section_id: "1be79911-fc06-4c8e-8a34-5af051d49c60" -->
### 6.1 Create Feature Directory
```bash
mkdir -p layer_1/layer_1_features/layer_1_feature_layer_stage_system
```

<!-- section_id: "cb961a16-b1a8-4732-a2c8-a72868847979" -->
### 6.2 Create Tool-Specific at Feature Root
```
layer_1_feature_layer_stage_system/
├── CLAUDE.md
├── .claude/
│   ├── commands/
│   ├── agents/
│   └── skills/
```

<!-- section_id: "8f2006bf-3f05-47e8-8f4b-48fa679ec793" -->
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

<!-- section_id: "d73707b9-3d3e-470b-b042-d422a38b78cf" -->
### 6.4 Create layer_2/ (Feature's Children)
```
layer_1_feature_layer_stage_system/layer_2/
├── layer_2_subx1_projects/
├── layer_2_features/                         # Created in Phase 7
└── layer_2_components/
```

---

<!-- section_id: "07ff78de-11a4-44e7-a698-8a963baa2d25" -->
## PHASE 7: Create layer_2 Features (Within Layer-Stage System)

<!-- section_id: "c1d97021-8fa9-45a2-8908-dd3c628e6b80" -->
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

<!-- section_id: "463ff742-99be-4163-8d7f-22b1af72079f" -->
## PHASE 8: Apply Naming Conventions Throughout

<!-- section_id: "71b40ea5-a549-4e88-97b6-a1127e3c5645" -->
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

<!-- section_id: "1566de42-1d28-46f0-b7b9-43a557b61f7f" -->
### 8.2 Rename Status Files
```
status.json → status_N.json (where N = layer number)
```

<!-- section_id: "d402f58c-d499-4299-a66c-6fdf4b6147b4" -->
### 8.3 Update All Internal References
- Update all markdown files that reference old paths
- Update all scripts that use old naming
- Update handoff documents

---

<!-- section_id: "a70e151b-ca5e-4504-b1ac-4d493ae3bbc6" -->
## PHASE 9: Create Specific/ Nested Structure Templates

<!-- section_id: "752b8ba5-30d9-45ed-972c-2beeec988ee4" -->
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

<!-- section_id: "dd323dbf-61c7-4b86-905f-b01c98118956" -->
## PHASE 10: Add Stage-Level Tool Configs

<!-- section_id: "8593e89a-689c-4af2-8213-089ed860a20d" -->
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

<!-- section_id: "91ba2090-838f-4f34-b3e0-7cf7b75dc130" -->
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

<!-- section_id: "d0a2aaf9-7a1b-44d5-976f-14c31b529012" -->
## PHASE 11: Update Documentation & References

<!-- section_id: "b10dfb2e-7da7-4a19-a560-3faa3e7beed9" -->
### 11.1 Files to Update
- `MASTER_DOCUMENTATION_INDEX.md`
- `SYSTEM_OVERVIEW.md`
- `README.md` (root and all entity READMEs)
- `USAGE_GUIDE.md`
- All framework docs in `sub_layer_1_05_framework_docs/`

<!-- section_id: "95b07ba6-a2a9-498a-b96e-fe442cab5711" -->
### 11.2 Update verify_paths.sh
```bash
# Update all path references to new structure
```

<!-- section_id: "74ebcdab-a5dc-4dc0-b857-c12fe5797237" -->
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

<!-- section_id: "82e69f83-a83d-4d01-a3ee-072d72501fa7" -->
## PHASE 12: Verification & Testing

<!-- section_id: "edc15070-9f62-48d5-8aa9-006f1174e077" -->
### 12.1 Run Verification Script
```bash
# Updated verify_paths.sh with new paths
./verify_paths.sh
```

<!-- section_id: "8d3ee65c-af33-4efc-8276-ba7bf51808a6" -->
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

<!-- section_id: "15205153-c18c-470c-bad6-c31d5d2c2929" -->
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

<!-- section_id: "cb00b05a-b935-48fb-a4a1-04a42990f751" -->
## SUBAGENT EXECUTION STRATEGY

<!-- section_id: "b46e2c49-3587-49db-b164-4fe5f40298ad" -->
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

<!-- section_id: "0eb16132-cfa4-4fbe-9355-bcb68097e526" -->
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

<!-- section_id: "0af29cc3-ce40-4280-a43c-ea13c886b955" -->
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

<!-- section_id: "938babe2-f1f4-4751-a1ee-0c9e22a9050d" -->
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

<!-- section_id: "5a950650-6f4f-4456-9433-bc7f675f26ad" -->
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

<!-- section_id: "8006bf72-c8ac-4d7c-baa6-3616855e17c2" -->
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

<!-- section_id: "4b16cd65-d1f6-4575-a6b3-6dd42b8dc7fe" -->
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

<!-- section_id: "1f6c3253-7e52-4347-b898-88e98592c953" -->
## Key Architectural Decisions

<!-- section_id: "258c5dd9-e749-45aa-b26b-ad5e36c04c58" -->
### 1. Everything Nested Under Layer 0
- Enables Claude Code's hierarchical CLAUDE.md discovery
- Universal skills/commands/agents inherited everywhere
- Single root for all projects

<!-- section_id: "cf6b6d23-56e9-447a-a6ed-4734f34128a0" -->
### 2. Layer-Stage System as a Feature
- The framework itself follows its own pattern
- Has its own stages for development
- Has child features for each major concept

<!-- section_id: "2d0c2865-0ea6-4fe1-98fb-12e9a681eb9c" -->
### 3. Agnostic → Specific Pattern
- Tool-agnostic init_prompt.md is the source of truth
- Tool-specific files (CLAUDE.md, .cursorrules, etc.) generated from it
- Nested specificity: os → environment → coding_app → ai_app

<!-- section_id: "c0c2c8df-5c72-4e3f-9514-9ece8d653dc8" -->
### 4. AI Manager Hierarchy as a Feature
- Defines the agnostic/specific pattern
- Contains templates for each AI tool
- Implemented at every entity's layer_N_00_ai_manager_system/

---

<!-- section_id: "4e7bdb65-ce82-443b-97af-847679869539" -->
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
