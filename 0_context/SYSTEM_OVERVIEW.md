# System Overview (Layer + Stage)

## Big picture
- **Layer System (specificity):** universal (0) → project (1) → feature (2) → component (3). Lower numbers are prerequisites. Each layer has `<N>.00_ai_manager_system/`, `<N>.01_manager_handoff_documents/<N>.00_to_universal|<N>.01_to_specific/`, slots in `layer_<N>_*/<N>.02_sub_layers/sub_layer_<N.xx>_*`.
- **Stage System (chronology):** instructions → planning → design → development → testing → criticism → fixing → archives. Stages mirror the layer prefix (e.g., `stage_2.04_development`) inside `*.99_stages/`, each with `hand_off_documents/` and `ai_agent_system/`.
- **Status:** per-layer status JSON inside `*.99_stages/` tracks `current_stage` and each stage state (`not_started | in_progress | blocked | done`).

## Layout map (current repo)
```
0_context/
├── 0.00_layer_stage_framework/     # templates + framework README
├── layer_0_universal/               # universal layer (0.xx slots + 0.99 stages)
├── layer_1_project/                 # project layer (1.xx slots + 1.99 stages)
├── layer_2_features/                # feature layer (2.xx slots + 2.99 stages)
└── layer_3_components/              # component layer (3.xx slots + 3.99 stages)
```

Legacy `trickle_down_*` content is preserved under `legacy_import/` within the closest matching sub_layer; do not add new work there.

## How to work in this system
1. **Start in universal:** `layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md` then `MASTER_DOCUMENTATION_INDEX.md`.
2. **Load needed layers:** project (`layer_1_*`), feature (`layer_2_*`), component (`layer_3_*`).
3. **Enter a stage:** use the layer’s `*.99_stages/` directory; read/update `status*.json`; use `hand_off_documents/` and `ai_agent_system/` inside the current stage.
4. **Sync habit:** `git pull` at session start for all repos you will touch; `git commit` + `git push` and update docs/status before ending a response.

## Slot numbers (zero‑padded examples)
- Universal 0.xx (slots): 0.01 basic prompts, 0.02 SE knowledge, 0.03 principles, 0.04 rules, 0.05 OS setup, 0.06 coding app setup, 0.07 apps/browsers/extensions, 0.08 AI apps/tools, 0.09 MCP servers and tools setup, 0.10 AI models, 0.11 agent setup, 0.12 universal tools.
- Project 1.xx mirrors 0.xx with project-specific content (e.g., 1.05 project architecture).
- Feature 2.xx and Component 3.xx mirror the same pattern at finer scope.

## Stage numbers (per layer)
- For layer N: stages are `stage_N.01_instructions`, `stage_N.02_planning`, `stage_N.03_design`, `stage_N.04_development`, `stage_N.05_testing`, `stage_N.06_criticism`, `stage_N.07_fixing`, `stage_N.08_archives` under `N.99_stages/`.

## Why this structure
- Deterministic, git-friendly navigation; no reliance on fuzzy search.
- Clear prerequisites (lower layers first) and clear workflow (stages) for handoffs.
- Ready-made drop points for artifacts (`hand_off_documents/`) and agent configs (`ai_agent_system/`).
