---
resource_id: "dc89d261-ed0b-4ff8-9556-8f05a7974b6f"
resource_type: "document"
resource_name: "SYSTEM_OVERVIEW.sync-conflict-20260126-035814-IF2WOGZ"
---
# System Overview (Layer + Stage)

## Big picture
- **Layer System (specificity):** universal (0) → project (1) → feature (2) → component (3). Lower numbers are prerequisites. Each layer has `layer_<N>_01_ai_manager_system/`, `layer_<N>_02_manager_handoff_documents/layer_<N>_00_to_universal|layer_<N>_01_to_specific/`, and sub-layers in `layer_<N>_0X_sub_layers/` (layer 0 uses `layer_0_03_sub_layers/`).
- **Stage System (chronology):** request_gathering → research → instructions → planning → design → development → testing → criticism → fixing → current_product → archives. Stages mirror the layer prefix (e.g., `stage_2_05_design`) inside `layer_<N>_99_stages/`, each with `hand_off_documents/` and `ai_agent_system/`.
- **Status:** per-layer status JSON inside `layer_<N>_99_stages/` tracks `current_stage` and each stage state (`not_started | in_progress | blocked | done`).

## Agent OS Architecture

This layer + stage framework implements the **AI Manager Hierarchy System** - a comprehensive **Agent Operating System** for software development.

### Core Concepts

The Agent OS organizes AI work through:

- **Layers of Abstraction**: L0 (Universal) → L1 (Project) → L2 (Feature) → L3 (Component) → L4+ (Sub-component)
  - Lower layers define constraints that cascade to higher layers
  - Each layer has managers that coordinate work and workers that execute tasks

- **Chronological Stages**: Work moves through a pipeline within each layer
  - request → instructions → planning → design → implementation → testing → criticism → fixing → current_product → archives
  - Each stage reads incoming handoffs, performs work, and writes outgoing handoffs

- **Manager/Worker Pattern**:
  - **Managers** read handoffs, decompose tasks, spawn workers (possibly in parallel), and aggregate results
  - **Workers** read one handoff, execute bounded work, write one handoff, and exit
  - Communication happens through structured **handoff documents** (JSON/Markdown)

- **Tool Specialization**:
  - **Claude Code**: Managers, criticism, complex multi-file work
  - **Codex CLI**: Short, atomic implementation/testing tasks (leaf workers)
  - **Gemini CLI**: Long-running request/instructions/planning and research
  - **Cursor IDE**: Interactive debugging and refactors
  - **Frameworks** (LangGraph, AutoGen, CrewAI): Optional orchestrators

- **Persistent Instructions**: System-level prompts (CLAUDE.md, AGENTS.md, GEMINI.md, .cursor/rules/) cascade from L0 down, keeping instructions sticky without chat history bloat

### Where to Learn More

- **Quick Start**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`](-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md)
- **Detailed Specs**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/`](-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/)
- **Master Index**: [MASTER_DOCUMENTATION_INDEX.md](MASTER_DOCUMENTATION_INDEX.md#-canonical-agent-os-architecture---ai-manager-hierarchy-system)

This Agent OS design is the **canonical architecture** for all AI agent coordination in this repository.

## Layout map (current repo)
```
0_layer_universal/
├── layer_0/                         # universal layer (sub-layers + stages)
├── layer_1/                         # project/feature layers
│   └── layer_1_features/            # framework + feature definitions
└── layer_-1_research/               # research projects
```

Legacy `trickle_down_*` content is preserved under `legacy_import/` within the closest matching sub_layer; do not add new work there.

## How to work in this system
1. **Start in universal:** `layer_0/layer_0_03_sub_layers/sub_layer_0_01_prompts/universal_init_prompt.md` then `MASTER_DOCUMENTATION_INDEX.md`.
2. **Load needed layers:** project (`layer_1_*`), feature (`layer_2_*`), component (`layer_3_*`).
3. **Enter a stage:** use the layer’s `*.99_stages/` directory; read/update `status*.json`; use `hand_off_documents/` and `ai_agent_system/` inside the current stage.
4. **Sync habit:** `git pull` at session start for all repos you will touch; `git commit` + `git push` and update docs/status before ending a response.

## Slot numbers (zero‑padded examples)
- Universal 0.xx (slots): 0.01 basic prompts, 0.02 SE knowledge, 0.03 principles, 0.04 rules, 0.05 OS setup, 0.06 coding app setup, 0.07 apps/browsers/extensions, 0.08 AI apps/tools, 0.09 MCP servers and tools setup, 0.10 AI models, 0.11 universal tools, 0.12 agent setup.
- Project 1.xx mirrors 0.xx with project-specific content (e.g., 1.05 project architecture).
- Feature 2.xx and Component 3.xx mirror the same pattern at finer scope.

## Stage numbers (per layer)
- For layer N: stages are `stage_N_01_request_gathering`, `stage_N_02_research`, `stage_N_03_instructions`, `stage_N_04_planning`, `stage_N_05_design`, `stage_N_06_development`, `stage_N_07_testing`, `stage_N_08_criticism`, `stage_N_09_fixing`, `stage_N_10_current_product`, `stage_N_11_archives` under `layer_N_99_stages/`.

## Why this structure
- Deterministic, git-friendly navigation; no reliance on fuzzy search.
- Clear prerequisites (lower layers first) and clear workflow (stages) for handoffs.
- Ready-made drop points for artifacts (`hand_off_documents/`) and agent configs (`ai_agent_system/`).
