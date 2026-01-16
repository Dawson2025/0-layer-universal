# layer_0 (Layer 0) – Operational Overlay

This overlay maps existing universal content into the Layer/Stage system without moving files. Each slot links to current sources. Use these paths when loading context.

## Manager and handoff
- 0.00_ai_manager_system → `./0.00_ai_manager_system/` (manager docs/configs)
- 0.01_manager_handoff_documents → `./0.01_manager_handoff_documents/` with `0.00_to_universal/` and `0.01_to_specific/`

## Slots (0.x, inside `0.02_sub_layers/`)
- 0.01_basic_prompts_throughout → `./0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/`
- 0.02_software_engineering_knowledge_system → `./0.02_sub_layers/sub_layer_0_02_software_engineering_knowledge_system/software_engineering_knowledge_system/`
- 0.03_universal_principles → `../SYSTEM_OVERVIEW.md`, `../USAGE_GUIDE.md` (kept at root for now)
- 0.04_universal_rules → `./0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/`
- 0.05_os_setup → `./0.02_sub_layers/sub_layer_0.05_os_setup/trickle_down_0.5_setup/`
- 0.06_environment_setup → `./0.02_sub_layers/sub_layer_0.06_environment_setup/trickle_down_0.5_setup/` (Git/GitHub auth, cross-app environment rules)
- 0.07_coding_app_setup → (coding IDE/editor setup)
- 0.08_apps_browsers_extensions_setup → (general apps, browsers, extensions)
- 0.09_ai_apps_tools_setup → (AI clients/CLIs and integrations setup)
- 0.10_mcp_servers_and_tools_setup → `./0.02_sub_layers/sub_layer_0.10_mcp_servers_and_tools_setup/`
- 0.11_ai_models → `./0.02_sub_layers/sub_layer_0.11_ai_models/` (approved models and usage guidance)
- 0.12_universal_tools → `./0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/`
- 0.13_agent_setup → `./0.02_sub_layers/sub_layer_0.13_agent_setup/trickle_down_0.75_universal_tools/0_instruction_docs/` (agent configuration, model fallbacks, MCP integration, tool access)
- 0.99_stages → stage folders + status for this layer

## How to use
- Load context via these mapped paths; do not move existing files.
- Add new docs inside these slots as needed; keep pointers updated.
- Track stage status in `0.99_stages/status_universal.json`.
