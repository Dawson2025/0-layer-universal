# Component Layer Template (3.x, zero-padded)

Use this to scaffold any component-level context. Depends on universal (0.x), project (1.x), and feature (2.x) layers.

## Manager + handoff
- 3.00_ai_manager_system: component manager docs/configs.
- 3.01_manager_handoff_documents: `3.00_to_universal/` and `3.01_to_specific/` for up/downstream handoffs.

## Slots (stored under `3.02_sub_layers/` as `sub_layer_3.xx_*`)
- sub_layer_3.01_basic_prompts: component init + what-to-do-next.
- sub_layer_3.02_component_knowledge: what this component does; contracts/invariants.
- sub_layer_3.03_component_principles: micro-principles (purity, idempotency, perf goals).
- sub_layer_3.04_component_rules: strict requirements (logging, validation, error handling).
- sub_layer_3.05_component_os_setup: only if OS/platform-specific.
- sub_layer_3.06_component_coding_app_setup: run/debug/test configs for this component.
- sub_layer_3.07_component_apps_browsers_extensions_setup: dashboards/tools relevant to this component.
- sub_layer_3.08_component_ai_apps_tools_setup: component-level AI apps/tools configuration.
- sub_layer_3.09_component_mcp_servers_and_tools_setup: component-specific MCP server setup (depends on 3.08).
- sub_layer_3.10_component_ai_models: models wired into this component (if any).
- sub_layer_3.11_component_agent_setup: component-specific agent configuration with model fallbacks (depends on 3.08, 3.09, 3.10).
- sub_layer_3.12_component_tools: helper scripts/utilities for this component.
- 3.99_stages: stage folders and status template.

## Component AI Setup Dependency Chain (3.08–3.11)

The slots 3.08–3.11 form a dependency chain for component-level AI agent setup:
- **3.08** → **3.09**: Component MCP servers are configured within component AI apps/tools
- **3.09** → **3.10**: Component models may be accessed via MCP servers
- **3.10** → **3.11**: Component agents require models to function
- **3.11** depends on all three: agents run in component apps (3.08), use component MCP servers (3.09), and require component models (3.10)

Configure these in order when setting up component-specific AI environments.

## Stages (3.99, stored under `3.99_stages/`, folders named `stage_3.xx_*`)
stage_3.01_instructions → stage_3.02_planning → stage_3.03_design → stage_3.04_development → stage_3.05_testing → stage_3.06_criticism → stage_3.07_fixing → stage_3.08_archives.

Copy, rename to your component, and populate each slot.
