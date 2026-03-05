---
resource_id: "6769eead-b1ed-41c6-86ff-8f94ab94d000"
resource_type: "knowledge"
resource_name: "01_current_system_analysis"
---
# Current Layer-Stage System Analysis

## Date: 2026-01-25
## Source: Reference Implementation Analysis

---

## 1. Architecture Overview

The current Layer-Stage Framework (v4.0) implements an N-layer hierarchical system with 11 workflow stages.

### Core Components

| Component | Purpose |
|-----------|---------|
| **Layers** | Hierarchical depth (L0 = universal, L1+ = nested entities) |
| **Stages** | 11 workflow phases (00-10 in reference, 01-11 in v3.0) |
| **Entities** | Projects, features, components following entity pattern |
| **Handoffs** | JSON/Markdown documents passing state between agents |
| **Registries** | Centralized metadata at position 00 |

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

## 2. Stage System

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

### Updated Stage Numbering (v3.0)

| # | Stage | Change |
|---|-------|--------|
| 00 | stage_registry | NEW - Registry position |
| 01 | request_gathering | Shifted +1 |
| 02 | research | Shifted +1 |
| ... | ... | ... |
| 10 | current_product | Shifted +1 |
| 11 | archives | Shifted +1 |

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

## 3. Layer System

### Layer Numbering Rules

1. **Layer 0** = Universal root
2. **Layer N** = Entities use `layer_N_XX_name` internally
3. **Layer N+1** = Children of Layer N entities
4. Infinite nesting supported

### Layer Internal Components

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Layer metadata (NEW) |
| 01 | ai_manager_system | Agent configurations |
| 02 | manager_handoff_documents | Inter-layer communication |
| 03 | sub_layers | Content slots |
| 99 | stages | Workflow stages |

### Sub-Layer Content Slots

| Position | Slot | Typical Content |
|----------|------|-----------------|
| 01 | prompts | Visual notes, diagrams |
| 02 | knowledge_system | Documentation, overview, things_learned |
| 03 | principles | Guiding principles |
| 04 | rules | Constraints and rules |
| 05+ | setup_dependant | OS/environment-specific content |

---

## 4. Context Gathering

### Vertical Chain (Always Relevant)
- **Ancestors**: All `init_prompt.md` files up to Layer 0
- **Descendants**: All `status_*.json` files down

### Horizontal Siblings (Task-Dependent)
- Include if related to current entity
- Include if relationship is task-relevant

### Task Sources (Priority Order)
1. Current user request (highest)
2. `status.json` (in_progress tasks)
3. Handoff documents
4. Todo lists (lowest)

---

## 5. Agnostic/Specific Pattern

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

### Purpose
- Agnostic = Source of truth, tool-independent
- Specific = Implementation details per environment

---

## 6. Handoff System

### Two Types

1. **Layer Handoffs** (`layer_N_01_manager_handoff_documents/`)
   - `layer_N_00_to_universal/` - Reports to parent
   - `layer_N_01_to_specific/` - Communicates to children

2. **Stage Handoffs** (`stage_N_XX_name/hand_off_documents/`)
   - `from_previous_stage.json` - Input
   - `to_next_stage.json` - Output

### Pattern
- Keep handoffs **concise**
- Reference `outputs/` folder for artifacts
- Don't duplicate content inline

---

## 7. Entity Types

### Three Core Types
1. **Project** - Top-level work unit
2. **Feature** - Functional capability
3. **Component** - Reusable building block

### Same-Type Nesting Rule

| Parent | Child | Uses "sub" Prefix? |
|--------|-------|--------------------|
| Project | Project | YES → `sub_project` |
| Project | Feature | NO |
| Project | Component | NO |
| Feature | Feature | YES → `sub_feature` |
| Feature | Component | YES → `sub_component` |
| Component | Component | YES → `sub_component` |

### Depth Markers
- Level 1: `sub_*`
- Level 2: `subx2_*`
- Level 3: `subx3_*`
- etc.

---

## 8. Key Strengths Identified

1. **Flexible N-Layer Architecture** - Unlimited nesting depth
2. **Clear Separation** - Entity internals vs nested content
3. **Tool-Agnostic Core** - Portable across AI tools
4. **Comprehensive Documentation** - Well-documented patterns
5. **Status Tracking** - JSON metadata at every level
6. **Workflow Stages** - Systematic progression
7. **Context Rules** - Clear gathering strategy

---

## 9. Pain Points Identified

1. **Naming Inconsistency** - Mixed dot/underscore notation
2. **Stage Numbering Confusion** - Multiple versions (00-10 vs 01-11)
3. **Relative Layer Numbers** - L-1 research context handling unclear
4. **Deep Nesting Paths** - Very long file paths
5. **Documentation Drift** - Some docs reference old patterns
6. **Registry Integration** - Not consistently implemented

---

## Next Steps

See `02_inconsistencies_found.md` for detailed inconsistency analysis.
See `03_improvement_proposals.md` for proposed changes.
