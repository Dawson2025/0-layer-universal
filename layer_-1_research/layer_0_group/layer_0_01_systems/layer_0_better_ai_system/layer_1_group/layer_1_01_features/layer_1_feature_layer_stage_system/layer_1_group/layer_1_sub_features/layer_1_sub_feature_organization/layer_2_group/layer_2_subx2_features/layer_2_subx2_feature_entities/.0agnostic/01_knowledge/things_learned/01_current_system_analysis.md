---
resource_id: "6769eead-b1ed-41c6-86ff-8f94ab94d000"
resource_type: "knowledge"
resource_name: "01_current_system_analysis"
---
# Current Layer-Stage System Analysis

<!-- section_id: "b848369f-20fc-42fb-b497-f3378d046a08" -->
## Date: 2026-01-25
<!-- section_id: "892cd531-cd2b-4adb-aaf0-fa00b609be00" -->
## Source: Reference Implementation Analysis

---

<!-- section_id: "ba042cd5-6c4c-45b7-8735-43099d88aa51" -->
## 1. Architecture Overview

The current Layer-Stage Framework (v4.0) implements an N-layer hierarchical system with 11 workflow stages.

<!-- section_id: "41fce9eb-f560-4779-81fe-0c682dad7b49" -->
### Core Components

| Component | Purpose |
|-----------|---------|
| **Layers** | Hierarchical depth (L0 = universal, L1+ = nested entities) |
| **Stages** | 11 workflow phases (00-10 in reference, 01-11 in v3.0) |
| **Entities** | Projects, features, components following entity pattern |
| **Handoffs** | JSON/Markdown documents passing state between agents |
| **Registries** | Centralized metadata at position 00 |

<!-- section_id: "a33302da-b3d8-4113-95ed-15c3d88f183c" -->
### Two-Folder Structure

Every entity has sibling folders:
```
layer_N_entity_name/
├── layer_N/          # Entity's internals
│   ├── layer_N_00_ai_manager_system/
│   ├── layer_N_01_manager_handoff_documents/
│   ├── layer_N_02_sub_layers/
│   └── layer_N_99_stages/
└── layer_N+1/        # Nested content (children)
    ├── layer_N+1_features/
    ├── layer_N+1_sub_projects/
    └── layer_N+1_components/
```

---

<!-- section_id: "6c4ff431-5dd3-44cc-b412-657d025f7d9a" -->
## 2. Stage System

<!-- section_id: "bdcf7dc0-24de-4fd9-bf5b-85294779e2c7" -->
### Current Stage Definitions (Reference Implementation)

| # | Stage | Purpose |
|---|-------|---------|
| 00 | request_gathering | Initial requirements collection |
| 01 | research | Problem space exploration |
| 02 | instructions | Task definition |
| 03 | planning | Implementation planning |
| 04 | design | Solution architecture |
| 05 | development | Implementation |
| 06 | testing | Verification |
| 07 | criticism | Review and critique |
| 08 | fixing | Issue resolution |
| 09 | current_product | Working version |
| 10 | archives | Historical records |

<!-- section_id: "184ae15c-5d74-4c8f-8175-5013a377487b" -->
### Updated Stage Numbering (v3.0)

| # | Stage | Change |
|---|-------|--------|
| 00 | stage_registry | NEW - Registry position |
| 01 | request_gathering | Shifted +1 |
| 02 | research | Shifted +1 |
| ... | ... | ... |
| 10 | current_product | Shifted +1 |
| 11 | archives | Shifted +1 |

<!-- section_id: "f5b42131-621e-4685-82d2-0faeb7880405" -->
### Stage Structure Pattern

Each stage contains:
```
stage_N_XX_name/
├── CLAUDE.md              # Stage documentation
├── .claude/               # Claude Code integration
│   ├── settings.json
│   ├── agents/
│   ├── commands/
│   ├── skills/
│   ├── hooks/
│   └── scripts/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes
└── outputs/               # Stage artifacts
```

---

<!-- section_id: "772a1470-bb15-460f-8d14-c053b73c6047" -->
## 3. Layer System

<!-- section_id: "c42f4ca6-fcaf-4f47-bb0d-9b552b3d4d02" -->
### Layer Numbering Rules

1. **Layer 0** = Universal root
2. **Layer N** = Entities use `layer_N_XX_name` internally
3. **Layer N+1** = Children of Layer N entities
4. Infinite nesting supported

<!-- section_id: "c82d4ad4-c3d7-49c3-8f7d-05a153bfa4b6" -->
### Layer Internal Components

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Layer metadata (NEW) |
| 01 | ai_manager_system | Agent configurations |
| 02 | manager_handoff_documents | Inter-layer communication |
| 03 | sub_layers | Content slots |
| 99 | stages | Workflow stages |

<!-- section_id: "98379861-9300-4012-bc2b-8fcc79d97cc1" -->
### Sub-Layer Content Slots

| Position | Slot | Typical Content |
|----------|------|-----------------|
| 01 | prompts | Visual notes, diagrams |
| 02 | knowledge_system | Documentation, overview, things_learned |
| 03 | principles | Guiding principles |
| 04 | rules | Constraints and rules |
| 05+ | setup_dependant | OS/environment-specific content |

---

<!-- section_id: "08927d1c-7794-472b-8880-1717592d6017" -->
## 4. Context Gathering

<!-- section_id: "d693cfaf-b714-46a2-a8d2-8b6f08728111" -->
### Vertical Chain (Always Relevant)
- **Ancestors**: All `init_prompt.md` files up to Layer 0
- **Descendants**: All `status_*.json` files down

<!-- section_id: "cf307737-6e30-4243-8819-19f47a0cd383" -->
### Horizontal Siblings (Task-Dependent)
- Include if related to current entity
- Include if relationship is task-relevant

<!-- section_id: "bde19b35-9f1e-4563-88a5-b73e5c005a77" -->
### Task Sources (Priority Order)
1. Current user request (highest)
2. `status.json` (in_progress tasks)
3. Handoff documents
4. Todo lists (lowest)

---

<!-- section_id: "dfb6858d-0ec4-4709-962e-f1cdce15bc8e" -->
## 5. Agnostic/Specific Pattern

<!-- section_id: "17e5a375-125e-464f-98d2-558a848ed73e" -->
### Structure
```
layer_N_00_ai_manager_system/
├── agnostic/              # Tool-independent source
│   ├── init_prompt.md
│   ├── context_gathering_rules.md
│   └── layer_navigation.md
└── specific/              # Tool-specific configs
    └── os/
        └── {wsl|linux|macos|windows}/
            └── environment/
                └── {local|cloud}/
                    └── coding_app/
                        └── {cursor|vscode|terminal}/
                            └── ai_app/
                                └── {claude|codex|gemini}/
```

<!-- section_id: "8a2693d3-3508-43bd-be60-d19db26a9fe5" -->
### Purpose
- Agnostic = Source of truth, tool-independent
- Specific = Implementation details per environment

---

<!-- section_id: "6672f139-62a5-4fe0-88a8-498d76523871" -->
## 6. Handoff System

<!-- section_id: "7202ad2d-44f5-4245-a194-f7628ff1a20d" -->
### Two Types

1. **Layer Handoffs** (`layer_N_01_manager_handoff_documents/`)
   - `layer_N_00_to_universal/` - Reports to parent
   - `layer_N_01_to_specific/` - Communicates to children

2. **Stage Handoffs** (`stage_N_XX_name/hand_off_documents/`)
   - `from_previous_stage.json` - Input
   - `to_next_stage.json` - Output

<!-- section_id: "9a2132d8-40b2-4368-9f7c-aaa41352ecb1" -->
### Pattern
- Keep handoffs **concise**
- Reference `outputs/` folder for artifacts
- Don't duplicate content inline

---

<!-- section_id: "9b244c24-5d49-4494-96c2-4cee407ce361" -->
## 7. Entity Types

<!-- section_id: "1e10f261-ce0b-4eb4-984d-d4a099f3ace4" -->
### Three Core Types
1. **Project** - Top-level work unit
2. **Feature** - Functional capability
3. **Component** - Reusable building block

<!-- section_id: "e4063ca1-e108-42e0-bf52-b42ef6c23827" -->
### Same-Type Nesting Rule

| Parent | Child | Uses "sub" Prefix? |
|--------|-------|--------------------|
| Project | Project | YES → `sub_project` |
| Project | Feature | NO |
| Project | Component | NO |
| Feature | Feature | YES → `sub_feature` |
| Feature | Component | YES → `sub_component` |
| Component | Component | YES → `sub_component` |

<!-- section_id: "5111c316-cb48-4af4-99cc-67016c788307" -->
### Depth Markers
- Level 1: `sub_*`
- Level 2: `subx2_*`
- Level 3: `subx3_*`
- etc.

---

<!-- section_id: "dc00e938-b1ac-4af9-82a1-9860489eb9f0" -->
## 8. Key Strengths Identified

1. **Flexible N-Layer Architecture** - Unlimited nesting depth
2. **Clear Separation** - Entity internals vs nested content
3. **Tool-Agnostic Core** - Portable across AI tools
4. **Comprehensive Documentation** - Well-documented patterns
5. **Status Tracking** - JSON metadata at every level
6. **Workflow Stages** - Systematic progression
7. **Context Rules** - Clear gathering strategy

---

<!-- section_id: "1635795c-3db3-4200-adbc-049f46bfdd7b" -->
## 9. Pain Points Identified

1. **Naming Inconsistency** - Mixed dot/underscore notation
2. **Stage Numbering Confusion** - Multiple versions (00-10 vs 01-11)
3. **Relative Layer Numbers** - L-1 research context handling unclear
4. **Deep Nesting Paths** - Very long file paths
5. **Documentation Drift** - Some docs reference old patterns
6. **Registry Integration** - Not consistently implemented

---

<!-- section_id: "4d0019b6-f8e9-4ab4-9135-d4d8d3166b93" -->
## Next Steps

See `02_inconsistencies_found.md` for detailed inconsistency analysis.
See `03_improvement_proposals.md` for proposed changes.
