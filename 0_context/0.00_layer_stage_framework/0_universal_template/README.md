# Universal Layer Template (0.x)

Use this when defining the universal layer for any ecosystem.

## Manager + handoff
- 0.00_ai_manager_system: manager docs/configs.
- 0.01_manager_handoff_documents: `0.00_to_universal/` and `0.01_to_specific/` for cross-layer handoffs.

## Slots (stored under `0.02_sub_layers/` as `sub_layer_0.xx_*`)
- sub_layer_0.01_basic_prompts_throughout: session init, what-to-do-next, core prompts.
- sub_layer_0.02_software_engineering_knowledge_system: general SE knowledge map.
- sub_layer_0.03_universal_principles: philosophies, values.
- sub_layer_0.04_universal_rules: hard constraints (git, terminal, security).
- sub_layer_0.05_os_setup: OS-specific setup (macOS/Linux/Windows).
- sub_layer_0.06_coding_app_setup: IDE/editor configuration.
- sub_layer_0.07_apps_browsers_extensions_setup: general apps, browsers, extensions.
- sub_layer_0.08_ai_apps_tools_setup: AI clients/CLIs and integrations.
- sub_layer_0.09_mcp_servers_and_tools_setup: MCP server setup and configuration (depends on 0.08).
- sub_layer_0.10_ai_models: approved models and usage guidance.
- sub_layer_0.11_agent_setup: agent configuration with model fallbacks and MCP integration (depends on 0.08, 0.09, 0.10).
- sub_layer_0.12_universal_tools: cross-project scripts/utilities.
- 0.99_stages: stage folders and status template.

## AI Setup Dependency Chain (0.08–0.11)

The slots 0.08–0.11 form a critical dependency chain for AI agent setup:
- **0.08** → **0.09**: MCP servers are configured within AI apps/tools
- **0.09** → **0.10**: Models may be accessed via MCP servers
- **0.10** → **0.11**: Agents require models to function
- **0.11** depends on all three: agents run in apps (0.08), use MCP servers (0.09), and require models (0.10)

Configure these in order when setting up a new AI environment.

## Stages (0.99, folders named `stage_0.xx_*`)
- stage_0.01_instructions
- stage_0.02_planning
- stage_0.03_design
- stage_0.04_development
- stage_0.05_testing
- stage_0.06_criticism
- stage_0.07_fixing
- stage_0.08_archives

Copy this template, rename for your universal context, and populate per slot.
