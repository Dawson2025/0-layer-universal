---
resource_id: "1acb88c9-b5d5-4659-96de-8cadb43fcb2d"
resource_type: "document"
resource_name: "INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.sync-conflict-20260126-035814-IF2WOGZ"
---
# INSTRUCTIONS: Layer-Stage System Restructure

**Created:** 2026-01-15
**Status:** Instructions Complete
**Next Stage:** Planning (stage_0_04_planning)

---

<!-- section_id: "f2077c87-d841-4295-96c0-07c240aaf61b" -->
## 1. Objective

Restructure the entire layer-stage system to:
1. Nest all layers under layer 0 (universal root)
2. Implement Claude Code and other AI tool configurations at every level
3. Create a tool-agnostic core with tool-specific implementations
4. Make the layer-stage system itself a feature that follows its own pattern

---

<!-- section_id: "7d237e15-819c-4992-a510-dfc1be4b3722" -->
## 2. Requirements

<!-- section_id: "b4040b4a-5acf-4373-9363-f889ceba8577" -->
### 2.1 Root Structure Requirements

- **R1**: Rename `0_layer_universal` to `0_layer_universal`
- **R2**: Flatten `0_context/` so contents are at root
- **R3**: All projects, features, components must be nested under layer 0
- **R4**: Root must have tool-specific files (CLAUDE.md, .claude/, .cursorrules, etc.)

<!-- section_id: "7e0bfcc0-e6b3-4334-a0ba-ee5565d3ff6f" -->
### 2.2 Layer Grouping Requirements

- **R5**: Each entity must have `layer_N/` for its own internals
- **R6**: Each entity must have `layer_N+1/` for its children
- **R7**: Children grouped into `layer_N+1_projects/`, `layer_N+1_features/`, `layer_N+1_components/`

<!-- section_id: "690bf97d-cbf0-4091-9f1a-16119a9e694f" -->
### 2.3 Naming Convention Requirements

- **R8**: Change from `0.00_name` to `layer_0_00_name` pattern
- **R9**: Change from `sub_layer_0_01_name` to `sub_layer_0_01_name` pattern
- **R10**: Change from `stage_0_01_name` to `stage_0_01_name` pattern
- **R11**: Status files renamed to `status_N.json` where N = layer number

<!-- section_id: "40c7ec81-c92f-44db-89b2-b84899adaf33" -->
### 2.4 AI Manager System Requirements

- **R12**: Every entity must have `layer_N_00_ai_manager_system/`
- **R13**: AI manager system must have `agnostic/` folder (tool-agnostic source)
- **R14**: AI manager system must have `specific/` folder (tool-specific implementations)
- **R15**: Specific folder must nest: `os/ → environment/ → coding_app/ → ai_app/`

<!-- section_id: "b0f1b473-2dab-4977-b1e4-1ae175f3bf10" -->
### 2.5 Tool-Specific Requirements

- **R16**: Every entity must have `CLAUDE.md` at its root
- **R17**: Every entity must have `.claude/` folder with commands/, agents/, skills/
- **R18**: Every entity must have `.cursorrules` for Cursor IDE
- **R19**: Every entity must have `AGENTS.md` for OpenAI Codex
- **R20**: Every entity must have `GEMINI.md` for Gemini CLI
- **R21**: Tool-specific files are generated from/reference agnostic source

<!-- section_id: "4172e1da-a75f-4852-bf59-3469ed3582ef" -->
### 2.6 Layer-Stage System as Feature Requirements

- **R22**: The layer-stage system must be a feature under `layer_1/layer_1_features/`
- **R23**: It must have its own `layer_1/` (internals) and `layer_2/` (children)
- **R24**: It must have child features for each major concept:
  - Stage definitions
  - Layer definitions
  - Context gathering
  - Handoff system
  - AI manager hierarchy

<!-- section_id: "77432c3c-438e-43d9-8cc4-0f579d86b1df" -->
### 2.7 Sub-Layer Requirements

- **R25**: Sub-layers must follow pattern: 01_prompts, 02_knowledge_system, 03_principles, 04_rules, 05+_setup_dependant
- **R26**: 05+ indicates expandable sub-layers (05, 06, 07, etc.)

<!-- section_id: "c1f0517f-0d6b-46ce-b589-b5797218098a" -->
### 2.8 Stage Requirements

- **R27**: Each stage must have its own `CLAUDE.md` and `.claude/` folder
- **R28**: Stages: 00_request_gathering, 01_instructions, 02_planning, 03_design, 04_development, 05_testing, 06_criticism, 07_fixing, 08_current_product, 09_archives

<!-- section_id: "14c82508-5757-46e9-910c-9f76f0388fa4" -->
### 2.9 Inheritance Requirements

- **R29**: Claude Code must discover and merge CLAUDE.md files from parent to child
- **R30**: Universal skills/commands/agents must be available everywhere
- **R31**: Child entities can override or extend parent configurations

---

<!-- section_id: "9ecb5d3d-6ee6-47ac-9b2e-4b03ad286e75" -->
## 3. Specific/ Nested Structure

The `specific/` folder uses nested specificity:

```
specific/
└── os/                              # Level 1: Operating System
    ├── wsl/
    ├── linux_ubuntu/
    ├── macos/
    └── windows/
        └── environment/             # Level 2: Environment
            ├── local/
            └── cloud/
                ├── aws/
                ├── gcp/
                └── azure/
                    └── coding_app/  # Level 3: Coding Application
                        ├── cursor_ide/
                        ├── vscode/
                        ├── jetbrains/
                        ├── rstudio/
                        └── terminal/
                            └── ai_app/  # Level 4: AI Application
                                ├── claude_code_cli/
                                ├── codex_cli/
                                ├── gemini_cli/
                                └── cursor_agent/
```

---

<!-- section_id: "a6195705-1164-4ad9-a89e-6536362e89a2" -->
## 4. Entity Pattern

Every entity (project, feature, component) follows this pattern:

```
layer_N_<type>_<name>/
│
├── CLAUDE.md                        # Tool-specific at root
├── .claude/
│   ├── settings.json
│   ├── commands/
│   ├── agents/
│   └── skills/
├── .cursorrules
├── AGENTS.md
├── GEMINI.md
├── .mcp.json
│
├── layer_N/                         # This entity's internals
│   ├── layer_N_00_ai_manager_system/
│   │   ├── agnostic/
│   │   └── specific/
│   ├── layer_N_01_manager_handoff_documents/
│   ├── layer_N_02_sub_layers/
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   ├── sub_layer_N_03_principles/
│   │   ├── sub_layer_N_04_rules/
│   │   └── sub_layer_N_05+_setup_dependant/
│   └── layer_N_99_stages/
│
└── layer_N+1/                       # This entity's children
    ├── layer_N+1_sub*N_projects/
    ├── layer_N+1_features/
    └── layer_N+1_components/
```

---

<!-- section_id: "9fcfb503-7864-4637-b9c8-217349e67bae" -->
## 5. Target Root Structure

```
0_layer_universal/                   # ROOT
│
├── CLAUDE.md
├── .claude/
│   ├── commands/
│   ├── agents/
│   └── skills/
├── .cursorrules
├── AGENTS.md
├── GEMINI.md
├── .mcp.json
│
├── layer_0/                         # Universal internals
│   ├── layer_0_00_ai_manager_system/
│   │   ├── agnostic/
│   │   └── specific/
│   ├── layer_0_01_manager_handoff_documents/
│   ├── layer_0_02_sub_layers/
│   └── layer_0_99_stages/
│
└── layer_1/                         # Universal's children
    ├── layer_1_projects/
    │   ├── layer_1_project_school/
    │   ├── layer_1_project_work/
    │   └── layer_1_project_personal/
    │
    ├── layer_1_features/
    │   └── layer_1_feature_layer_stage_system/  # THE FRAMEWORK
    │       ├── CLAUDE.md
    │       ├── layer_1/             # Framework's internals
    │       │   ├── layer_1_02_sub_layers/
    │       │   │   └── sub_layer_1_05+_setup_dependant/
    │       │   │       ├── sub_layer_1_05_framework_docs/
    │       │   │       ├── sub_layer_1_06_templates/
    │       │   │       └── sub_layer_1_07_scripts/
    │       │   └── layer_1_99_stages/
    │       │       └── stage_1_08_current_product/
    │       │           ├── setup/
    │       │           └── changes/
    │       └── layer_2/             # Framework's children
    │           └── layer_2_features/
    │               ├── layer_2_feature_stage_definitions/
    │               ├── layer_2_feature_layer_definitions/
    │               ├── layer_2_feature_context_gathering/
    │               ├── layer_2_feature_handoff_system/
    │               └── layer_2_feature_ai_manager_hierarchy/
    │
    └── layer_1_components/
```

---

<!-- section_id: "309f8cbc-611d-43f6-9df1-4c8a0d5765ff" -->
## 6. Key Concepts

<!-- section_id: "933f52d7-8522-4755-a09a-03b52c9933bb" -->
### 6.1 Agnostic vs Specific

| Agnostic | Specific |
|----------|----------|
| Tool-independent | Tool-dependent |
| `init_prompt.md` | `CLAUDE.md`, `.cursorrules`, etc. |
| Universal rules | Tool-specific implementations |
| Source of truth | Generated from agnostic |

<!-- section_id: "b093d050-5db5-4d90-9d9a-31a75f137416" -->
### 6.2 Vertical vs Horizontal Context

| Vertical Chain | Horizontal Siblings |
|----------------|---------------------|
| Always relevant | Only when task-relevant |
| Ancestors + descendants | Same-level entities |
| Inherited automatically | Checked conditionally |

<!-- section_id: "f4a3476c-44e9-4e89-ab0f-3e4c24fcd244" -->
### 6.3 Layer-Stage System Features

| Feature | Defines |
|---------|---------|
| `stage_definitions` | The 9 stages (00-09) |
| `layer_definitions` | Layer numbering, nesting, entity types |
| `context_gathering` | How AI gathers relevant context |
| `handoff_system` | Handoff schemas, to/from patterns |
| `ai_manager_hierarchy` | Agnostic/specific pattern, tool configs |

---

<!-- section_id: "e5ce8d88-be7d-44a4-a9bb-acf34e291871" -->
## 7. Constraints

- **C1**: Must maintain git history where possible
- **C2**: Must not break existing functionality during migration
- **C3**: Must be executable in phases (can stop/resume)
- **C4**: Must create backup before any destructive operations
- **C5**: Must update all documentation references

---

<!-- section_id: "e7a8a899-afc2-48de-a96e-6a916a496d7b" -->
## 8. Success Criteria

- [ ] All entities follow the entity pattern
- [ ] All directories use new naming convention
- [ ] All entities have tool-specific files at root
- [ ] All ai_manager_systems have agnostic/ and specific/
- [ ] Layer-stage system exists as a feature with child features
- [ ] Claude Code inheritance works (test from multiple locations)
- [ ] All documentation references updated
- [ ] No stale paths remain
- [ ] Git history preserved

---

<!-- section_id: "b32adf90-71f7-4aeb-8de4-7e439503784b" -->
## 9. Handoff to Planning

This document defines WHAT needs to be done.
The planning stage (`stage_0_04_planning`) defines HOW to do it.

**Planning Document:** `IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.md`

---

<!-- section_id: "c0133836-a993-492d-b7fa-06750fade480" -->
## 10. References

<!-- section_id: "fd030b9c-8bbf-424c-bdf4-9137805932e9" -->
### Current Locations (Before Restructure)
- `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/`
- `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/`
- `0_layer_universal/0_context/layer_0/`
- `0_layer_universal/0_context/-1_research/`

<!-- section_id: "1b16f9ac-dfeb-4999-9ff4-1f2f18c838bb" -->
### Research Reference
- `-1_research/-1.01_things_researched/ai_manager_hierarchy_system/`

<!-- section_id: "dcf9122c-b5f7-4bcc-8437-a3fec393c2ba" -->
### Claude Code Documentation
- Skills: `~/.claude/skills/` and `.claude/skills/`
- Commands: `.claude/commands/`
- Agents: `.claude/agents/`
- CLAUDE.md: Hierarchical discovery from parent to child

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_03_instructions/hand_off_documents/INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md`

**Last Updated:** 2026-01-15

**Status:** Instructions Complete → Ready for Planning
