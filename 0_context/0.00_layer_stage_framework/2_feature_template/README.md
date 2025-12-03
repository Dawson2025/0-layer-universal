# Feature Layer Template (2.x, zero-padded)

Use this to scaffold any feature-level context. Depends on universal (0.x) and project (1.x) layers.

## Manager + handoff
- 2.00_ai_manager_system: feature manager docs/configs.
- 2.01_manager_handoff_documents: `2.00_to_universal/` and `2.01_to_specific/` for up/downstream handoffs.

## Slots (stored under `2.02_sub_layers/` as `sub_layer_2.xx_*`)
- sub_layer_2.01_basic_prompts: feature init + what-to-do-next.
- sub_layer_2.02_feature_knowledge: domain/UX/business knowledge specific to this feature.
- sub_layer_2.03_feature_principles: local design/perf/security principles.
- sub_layer_2.04_feature_rules: must/never rules, data constraints.
- sub_layer_2.05_feature_os_setup: platform/browser/runtime specifics (if any).
- sub_layer_2.06_feature_coding_app_setup: run/debug configs, scripts for this feature.
- sub_layer_2.07_feature_apps_browsers_extensions_setup: dashboards/monitoring/admin relevant to this feature.
- sub_layer_2.08_feature_ai_apps_tools_setup: feature-level AI apps/tools configuration.
- sub_layer_2.09_feature_mcp_servers_and_tools_setup: feature-specific MCP server setup (depends on 2.08).
- sub_layer_2.10_feature_ai_models: models wired into this feature (if any).
- sub_layer_2.11_feature_agent_setup: feature-specific agent configuration with model fallbacks (depends on 2.08, 2.09, 2.10).
- sub_layer_2.12_feature_tools: scripts/migrations/backfills specific to this feature.
- 2.99_stages: stage folders and status template.

## Feature AI Setup Dependency Chain (2.08–2.11)

The slots 2.08–2.11 form a dependency chain for feature-level AI agent setup:
- **2.08** → **2.09**: Feature MCP servers are configured within feature AI apps/tools
- **2.09** → **2.10**: Feature models may be accessed via MCP servers
- **2.10** → **2.11**: Feature agents require models to function
- **2.11** depends on all three: agents run in feature apps (2.08), use feature MCP servers (2.09), and require feature models (2.10)

Configure these in order when setting up feature-specific AI environments.

## Stages (2.99, stored under `2.99_stages/`, folders named `stage_2.xx_*`)
stage_2.01_instructions → stage_2.02_planning → stage_2.03_design → stage_2.04_development → stage_2.05_testing → stage_2.06_criticism → stage_2.07_fixing → stage_2.08_archives.

Copy, rename to your feature, and populate each slot.
