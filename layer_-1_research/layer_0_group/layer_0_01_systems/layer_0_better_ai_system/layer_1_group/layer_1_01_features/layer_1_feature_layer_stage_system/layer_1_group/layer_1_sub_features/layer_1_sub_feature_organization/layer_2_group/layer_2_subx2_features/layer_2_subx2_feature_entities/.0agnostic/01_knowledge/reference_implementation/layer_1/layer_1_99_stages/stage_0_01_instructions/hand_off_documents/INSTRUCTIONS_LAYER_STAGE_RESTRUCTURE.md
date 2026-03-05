---
resource_id: "f868ae87-46e8-4795-9828-a974a4032a8e"
resource_type: "knowledge"
resource_name: "INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE"
---
# INSTRUCTIONS: Layer-Stage System Restructure

**Created:** 2026-01-15
**Status:** Instructions Complete
**Next Stage:** Planning (stage_0_02_planning)

---

<!-- section_id: "5a1975f8-66d9-4d82-903f-fd00e2db0c3b" -->
## 1. Objective

Restructure the entire layer-stage system to:
1. Nest all layers under layer 0 (universal root)
2. Implement Claude Code and other AI tool configurations at every level
3. Create a tool-agnostic core with tool-specific implementations
4. Make the layer-stage system itself a feature that follows its own pattern

---

<!-- section_id: "15c799d8-184b-4192-ad89-841320df494c" -->
## 2. Requirements

<!-- section_id: "2e239ff5-b136-4392-b2dc-8a32320d7603" -->
### 2.1 Root Structure Requirements

- **R1**: Rename `0_layer_universal` to `0_layer_universal`
- **R2**: Flatten `0_context/` so contents are at root
- **R3**: All projects, features, components must be nested under layer 0
- **R4**: Root must have tool-specific files (CLAUDE.md, .claude/, .cursorrules, etc.)

<!-- section_id: "3da2ecf2-a14b-4a3c-88e5-ca08b5fbd272" -->
### 2.2 Layer Grouping Requirements

- **R5**: Each entity must have `layer_N/` for its own internals
- **R6**: Each entity must have `layer_N+1/` for its children
- **R7**: Children grouped into `layer_N+1_projects/`, `layer_N+1_features/`, `layer_N+1_components/`

<!-- section_id: "d2b170d7-5f7a-4121-9b73-fa9d6601d20e" -->
### 2.3 Naming Convention Requirements

- **R8**: Change from `0.00_name` to `layer_0_00_name` pattern
- **R9**: Change from `sub_layer_0_01_name` to `sub_layer_0_01_name` pattern
- **R10**: Change from `stage_0_01_name` to `stage_0_01_name` pattern
- **R11**: Status files renamed to `status_N.json` where N = layer number

<!-- section_id: "e2cbeffb-e5a3-448e-9ddc-00e171cd4199" -->
### 2.4 AI Manager System Requirements

- **R12**: Every entity must have `layer_N_00_ai_manager_system/`
- **R13**: AI manager system must have `agnostic/` folder (tool-agnostic source)
- **R14**: AI manager system must have `specific/` folder (tool-specific implementations)
- **R15**: Specific folder must nest: `os/ → environment/ → coding_app/ → ai_app/`

<!-- section_id: "c977ab37-dc23-47a4-87fd-e2c51f05f947" -->
### 2.5 Tool-Specific Requirements

- **R16**: Every entity must have `CLAUDE.md` at its root
- **R17**: Every entity must have `.claude/` folder with commands/, agents/, skills/
- **R18**: Every entity must have `.cursorrules` for Cursor IDE
- **R19**: Every entity must have `AGENTS.md` for OpenAI Codex
- **R20**: Every entity must have `GEMINI.md` for Gemini CLI
- **R21**: Tool-specific files are generated from/reference agnostic source

<!-- section_id: "3f5020b2-f422-41eb-adbd-c3f209ec1ff2" -->
### 2.6 Layer-Stage System as Feature Requirements

- **R22**: The layer-stage system must be a feature under `layer_1/layer_1_features/`
- **R23**: It must have its own `layer_1/` (internals) and `layer_2/` (children)
- **R24**: It must have child features for each major concept:
  - Stage definitions
  - Layer definitions
  - Context gathering
  - Handoff system
  - AI manager hierarchy

<!-- section_id: "0ff95380-2c76-425b-b9d6-a6f1f7aa416b" -->
### 2.7 Sub-Layer Requirements

- **R25**: Sub-layers must follow pattern: 01_prompts, 02_knowledge_system, 03_principles, 04_rules, 05+_setup_dependant
- **R26**: 05+ indicates expandable sub-layers (05, 06, 07, etc.)

<!-- section_id: "7b26fd44-2246-4441-9b81-1ea88c08a70c" -->
### 2.8 Stage Requirements

- **R27**: Each stage must have its own `CLAUDE.md` and `.claude/` folder
- **R28**: Stages: 00_request_gathering, 01_instructions, 02_planning, 03_design, 04_development, 05_testing, 06_criticism, 07_fixing, 08_current_product, 09_archives

<!-- section_id: "77780561-4878-4f6a-a877-a645a0cbdde2" -->
### 2.9 Inheritance Requirements

- **R29**: Claude Code must discover and merge CLAUDE.md files from parent to child
- **R30**: Universal skills/commands/agents must be available everywhere
- **R31**: Child entities can override or extend parent configurations

---

<!-- section_id: "961f2b09-3a02-494b-9343-1af5c68bdec6" -->
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

<!-- section_id: "4136d172-0832-46b6-b2ad-41628eede803" -->
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

<!-- section_id: "5aa896a9-4e1b-4f7d-8f3d-faba78629237" -->
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
├── layer_0_group/                         # Universal internals
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

<!-- section_id: "16859b6c-2fb8-426c-8461-0d7bfeea203b" -->
## 6. Key Concepts

<!-- section_id: "73a10958-06dc-4769-a80f-27e93078f231" -->
### 6.1 Agnostic vs Specific

| Agnostic | Specific |
|----------|----------|
| Tool-independent | Tool-dependent |
| `init_prompt.md` | `CLAUDE.md`, `.cursorrules`, etc. |
| Universal rules | Tool-specific implementations |
| Source of truth | Generated from agnostic |

<!-- section_id: "3c84bbfe-a1ff-489e-9898-29f9ceb6c198" -->
### 6.2 Vertical vs Horizontal Context

| Vertical Chain | Horizontal Siblings |
|----------------|---------------------|
| Always relevant | Only when task-relevant |
| Ancestors + descendants | Same-level entities |
| Inherited automatically | Checked conditionally |

<!-- section_id: "3287be72-76b0-45c6-9b6c-41bc86119137" -->
### 6.3 Layer-Stage System Features

| Feature | Defines |
|---------|---------|
| `stage_definitions` | The 9 stages (00-09) |
| `layer_definitions` | Layer numbering, nesting, entity types |
| `context_gathering` | How AI gathers relevant context |
| `handoff_system` | Handoff schemas, to/from patterns |
| `ai_manager_hierarchy` | Agnostic/specific pattern, tool configs |

---

<!-- section_id: "08b22a46-7f5c-4ba8-8644-992c2bbdcffe" -->
## 7. Constraints

- **C1**: Must maintain git history where possible
- **C2**: Must not break existing functionality during migration
- **C3**: Must be executable in phases (can stop/resume)
- **C4**: Must create backup before any destructive operations
- **C5**: Must update all documentation references

---

<!-- section_id: "4313eb1f-8a0d-4995-be7d-6a5e3c8ff96a" -->
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

<!-- section_id: "3c5141bd-54f3-4b9b-8b7a-a55b6d28ad93" -->
## 9. Handoff to Planning

This document defines WHAT needs to be done.
The planning stage (`stage_0_02_planning`) defines HOW to do it.

**Planning Document:** `IMPLEMENTATION_PLAN_LAYER_STAGE_RESTRUCTURE.md`

---

<!-- section_id: "c23a8f87-0192-4fdc-843b-fb931dfabb81" -->
## 10. References

<!-- section_id: "eac25615-d621-48f7-90e7-4dd7cfb54498" -->
### Current Locations (Before Restructure)
- `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/`
- `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/`
- `0_layer_universal/0_context/layer_0_group/`
- `0_layer_universal/0_context/-1_research/`

<!-- section_id: "2f4f4bb2-2f6f-4460-a47c-d2af12a28247" -->
### Research Reference
- `-1_research/-1.01_things_researched/ai_manager_hierarchy_system/`

<!-- section_id: "699bccf6-961d-4d3a-83c4-cdf6173e6847" -->
### Claude Code Documentation
- Skills: `~/.claude/skills/` and `.claude/skills/`
- Commands: `.claude/commands/`
- Agents: `.claude/agents/`
- CLAUDE.md: Hierarchical discovery from parent to child

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_01_instructions/hand_off_documents/INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md`

**Last Updated:** 2026-01-15

**Status:** Instructions Complete → Ready for Planning
