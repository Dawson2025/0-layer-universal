---
resource_id: "4d165905-148a-4091-90e0-df1ed9e21580"
resource_type: "document"
resource_name: "INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE"
---
# INSTRUCTIONS: Layer-Stage System Restructure

**Created:** 2026-01-15
**Status:** Instructions Complete
**Next Stage:** Planning (stage_0_04_planning)

---

<!-- section_id: "57bb98a1-38ec-42f5-8a67-dee985cbcc5e" -->
## 1. Objective

Restructure the entire layer-stage system to:
1. Nest all layers under layer 0 (universal root)
2. Implement Claude Code and other AI tool configurations at every level
3. Create a tool-agnostic core with tool-specific implementations
4. Make the layer-stage system itself a feature that follows its own pattern

---

<!-- section_id: "2c6bc1c0-2837-4b49-925d-738d53dfd5f9" -->
## 2. Requirements

<!-- section_id: "4bb027ac-0d72-43e4-8dce-731d7d4dee83" -->
### 2.1 Root Structure Requirements

- **R1**: Rename `0_layer_universal` to `0_layer_universal`
- **R2**: Flatten `0_context/` so contents are at root
- **R3**: All projects, features, components must be nested under layer 0
- **R4**: Root must have tool-specific files (CLAUDE.md, .claude/, .cursorrules, etc.)

<!-- section_id: "94fdfd2f-8c3e-4384-9e3f-ebc539296188" -->
### 2.2 Layer Grouping Requirements

- **R5**: Each entity must have `layer_N/` for its own internals
- **R6**: Each entity must have `layer_N+1/` for its children
- **R7**: Children grouped into `layer_N+1_projects/`, `layer_N+1_features/`, `layer_N+1_components/`

<!-- section_id: "7cf1dadc-bfb4-49c6-a267-f64644ec9f84" -->
### 2.3 Naming Convention Requirements

- **R8**: Change from `0.00_name` to `layer_0_00_name` pattern
- **R9**: Change from `sub_layer_0_01_name` to `sub_layer_0_01_name` pattern
- **R10**: Change from `stage_0_01_name` to `stage_0_01_name` pattern
- **R11**: Status files renamed to `status_N.json` where N = layer number

<!-- section_id: "a16a5999-de4c-42e5-9f5a-4097a38ccc67" -->
### 2.4 AI Manager System Requirements

- **R12**: Every entity must have `layer_N_00_ai_manager_system/`
- **R13**: AI manager system must have `agnostic/` folder (tool-agnostic source)
- **R14**: AI manager system must have `specific/` folder (tool-specific implementations)
- **R15**: Specific folder must nest: `os/ → environment/ → coding_app/ → ai_app/`

<!-- section_id: "1adaced9-92f7-4c43-868e-91804beba4ba" -->
### 2.5 Tool-Specific Requirements

- **R16**: Every entity must have `CLAUDE.md` at its root
- **R17**: Every entity must have `.claude/` folder with commands/, agents/, skills/
- **R18**: Every entity must have `.cursorrules` for Cursor IDE
- **R19**: Every entity must have `AGENTS.md` for OpenAI Codex
- **R20**: Every entity must have `GEMINI.md` for Gemini CLI
- **R21**: Tool-specific files are generated from/reference agnostic source

<!-- section_id: "79cf543c-a5b1-4ea1-9043-7d5484f42251" -->
### 2.6 Layer-Stage System as Feature Requirements

- **R22**: The layer-stage system must be a feature under `layer_1/layer_1_features/`
- **R23**: It must have its own `layer_1/` (internals) and `layer_2/` (children)
- **R24**: It must have child features for each major concept:
  - Stage definitions
  - Layer definitions
  - Context gathering
  - Handoff system
  - AI manager hierarchy

<!-- section_id: "52fb855e-b0dd-4295-baf4-e82597da27a7" -->
### 2.7 Sub-Layer Requirements

- **R25**: Sub-layers must follow pattern: 01_prompts, 02_knowledge_system, 03_principles, 04_rules, 05+_setup_dependant
- **R26**: 05+ indicates expandable sub-layers (05, 06, 07, etc.)

<!-- section_id: "0e610f4f-7332-4a88-a0eb-9de0f676af09" -->
### 2.8 Stage Requirements

- **R27**: Each stage must have its own `CLAUDE.md` and `.claude/` folder
- **R28**: Stages: 00_request_gathering, 01_instructions, 02_planning, 03_design, 04_development, 05_testing, 06_criticism, 07_fixing, 08_current_product, 09_archives

<!-- section_id: "007b4831-e4ca-4b6b-9162-48b33cc6446d" -->
### 2.9 Inheritance Requirements

- **R29**: Claude Code must discover and merge CLAUDE.md files from parent to child
- **R30**: Universal skills/commands/agents must be available everywhere
- **R31**: Child entities can override or extend parent configurations

---

<!-- section_id: "23c353fc-1901-460a-aa36-4c9b1ea990be" -->
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

<!-- section_id: "cdf0e9f2-259c-4b07-84c0-c51a75c45b74" -->
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

<!-- section_id: "16bcdf2d-e13e-42e2-a7bf-1302ed564d5d" -->
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

<!-- section_id: "efd2bb56-af82-4473-ad94-a411f25da224" -->
## 6. Key Concepts

<!-- section_id: "f995daca-6356-4a7b-b960-175772d6e90b" -->
### 6.1 Agnostic vs Specific

| Agnostic | Specific |
|----------|----------|
| Tool-independent | Tool-dependent |
| `init_prompt.md` | `CLAUDE.md`, `.cursorrules`, etc. |
| Universal rules | Tool-specific implementations |
| Source of truth | Generated from agnostic |

<!-- section_id: "9c8aaa63-9e4a-4c68-bedd-332eaa0ef577" -->
### 6.2 Vertical vs Horizontal Context

| Vertical Chain | Horizontal Siblings |
|----------------|---------------------|
| Always relevant | Only when task-relevant |
| Ancestors + descendants | Same-level entities |
| Inherited automatically | Checked conditionally |

<!-- section_id: "6f747cfb-bd7e-45de-b58b-4d72790d741b" -->
### 6.3 Layer-Stage System Features

| Feature | Defines |
|---------|---------|
| `stage_definitions` | The 9 stages (00-09) |
| `layer_definitions` | Layer numbering, nesting, entity types |
| `context_gathering` | How AI gathers relevant context |
| `handoff_system` | Handoff schemas, to/from patterns |
| `ai_manager_hierarchy` | Agnostic/specific pattern, tool configs |

---

<!-- section_id: "74f54ff2-f90f-43e2-a106-0a3293cb286e" -->
## 7. Constraints

- **C1**: Must maintain git history where possible
- **C2**: Must not break existing functionality during migration
- **C3**: Must be executable in phases (can stop/resume)
- **C4**: Must create backup before any destructive operations
- **C5**: Must update all documentation references

---

<!-- section_id: "983d51a4-e497-490e-913e-82317a8832bd" -->
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

<!-- section_id: "62649a15-873d-4d5c-9dd4-58fd9befed8c" -->
## 9. Handoff to Planning

This document defines WHAT needs to be done.
The planning stage (`stage_0_04_planning`) defines HOW to do it.

**Planning Document:** `IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.md`

---

<!-- section_id: "117a4cee-4a39-4549-8bdb-7969f9fae9e2" -->
## 10. References

<!-- section_id: "1eae90e4-4935-4252-a7e4-4b877d816f92" -->
### Current Locations (Before Restructure)
- `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/`
- `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/`
- `0_layer_universal/0_context/layer_0/`
- `0_layer_universal/0_context/-1_research/`

<!-- section_id: "8d757379-5645-42bf-abaa-4fb9f759ac05" -->
### Research Reference
- `-1_research/-1.01_things_researched/ai_manager_hierarchy_system/`

<!-- section_id: "0631af4d-511b-4525-a351-b59de9d835e1" -->
### Claude Code Documentation
- Skills: `~/.claude/skills/` and `.claude/skills/`
- Commands: `.claude/commands/`
- Agents: `.claude/agents/`
- CLAUDE.md: Hierarchical discovery from parent to child

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_03_instructions/hand_off_documents/INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md`

**Last Updated:** 2026-01-15

**Status:** Instructions Complete → Ready for Planning
