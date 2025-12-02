# layer_0 (Layer 0) – Operational Overlay

This overlay maps existing universal content into the Layer/Stage system without moving files. Each slot links to current sources. Use these paths when loading context.

## Slots (0.x, inside `0.01_sub_layers/`)
- 0.01_basic_prompts_throughout → `./0.01_sub_layers/0.01_basic_prompts_throughout/0_basic_prompts_throughout/`
- 0.02_software_engineering_knowledge_system → `./0.01_sub_layers/0.02_software_engineering_knowledge_system/software_engineering_knowledge_system/`
- 0.03_universal_principles → `../SYSTEM_OVERVIEW.md`, `../USAGE_GUIDE.md` (kept at root for now)
- 0.04_universal_rules → `./0.01_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/`
- 0.05_os_setup → `./0.01_sub_layers/0.05_os_setup/trickle_down_0.5_setup/`
- 0.06_coding_app_setup → (add coding IDE/editor setup here if/when available)
- 0.07_apps_browsers_extensions_setup → (add general app/browser/extension setup here)
- 0.08_ai_apps_tools_setup → (use 0.10 path below until split)
- 0.09_ai_models → (document approved models and usage guidance here)
- 0.10_universal_tools → `./0.01_sub_layers/0.10_universal_tools/trickle_down_0.75_universal_tools/`
- 0.99_stages → stage folders + status for this layer

## How to use
- Load context via these mapped paths; do not move existing files.
- Add new docs inside these slots as needed; keep pointers updated.
- Track stage status in `0.99_stages/status_universal.json`.
