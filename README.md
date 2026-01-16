# AI Agent Context System (Layer + Stage Framework)

This repo is the universal context hub for all AI agents. It uses two orthogonal dimensions:

- **Layer System (specificity):** universal → project → feature → component. Each layer has `<N>.00_ai_manager_system/`, `<N>.01_manager_handoff_documents/` (`<N>.00_to_universal/`, `<N>.01_to_specific/`), slots in `<N>.02_sub_layers/sub_layer_<N.xx>_*`, and stages in `<N>.99_stages/`. Numbers are zero‑padded (e.g., 0.01, 1.01).
- **Stage System (chronology):** instructions → planning → design → development → testing → criticism → fixing → archives. Stage folders mirror the layer prefix (e.g., `stage_1.03_design`) and live under `*.99_stages/`, each with `hand_off_documents/` and `ai_agent_system/` drop points.

## Repo layout (top level)
- `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` — templates and README describing how to scaffold new layers and stages.
- `layer_0/` — universal content (0.01–0.10 slots + 0.99 stages).
- `layer_1_project/` — project-level content (1.01–1.12 slots + 1.99 stages).
- `layer_2_features/` — feature-level content (2.01–2.12 slots + 2.99 stages).
- `layer_3_components/` — component-level content (3.01–3.12 slots + 3.99 stages).

Legacy `trickle_down_*` material remains inside `legacy_import/` folders within the appropriate sub_layer directories for reference; new work should use the Layer/Stage paths above.

## Navigation (start here)
1. Read `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`.
2. Read `MASTER_DOCUMENTATION_INDEX.md` and `SYSTEM_OVERVIEW.md` for the map.
3. Load the relevant project/feature/component layers and operate inside their current stage (see `*.99_stages/status*.json`).

## Naming conventions
- Manager & handoff: `<N>.00_ai_manager_system/` and `<N>.01_manager_handoff_documents/<N>.00_to_universal|<N>.01_to_specific/` in each layer.
- Slots: `sub_layer_<N.xx>_*` inside `<layer>/0.02_sub_layers/`, zero‑padded (e.g., `sub_layer_1.05_project_architecture`).
- Stages: `stage_<N.xx>_*` inside `<layer>/*.99_stages/`, zero‑padded (e.g., `stage_2.04_development`). Each stage has `hand_off_documents/` and `ai_agent_system/`.
- Status: per-layer status JSON in `*.99_stages/` using stage keys like `stage_1.03_design`.

## Quick sync rules
- Start every session with `git pull` and `git status` for all repos you will touch.
- End each response by committing and pushing relevant changes, and updating context/docs/stage status.

## Need templates?
Copy from `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` to scaffold a new universal/project/feature/component layer. Templates already include sub_layers, stages, handoff folders, and a status template.
