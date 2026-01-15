# Feature Layer Template (2.x, zero-padded)

Use this to scaffold any feature-level context. Depends on universal (0.x) and project (1.x) layers.

**This template implements Layer 2 (Feature) of the [Ideal AI Manager Hierarchy System](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md).**

The Feature layer inherits Universal (L0) and Project (L1) constraints and adds feature-specific logic and invariants. For architectural details, see:
- [`architecture.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md) – Feature-level responsibilities and decomposition
- [`parallel_execution.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md) – Parallelizing feature work across components

## Directory Structure

```
2_feature_template/
├── layer_2/                              # Layer 2 grouping folder
│   ├── layer_2_00_ai_manager_system/     # Manager docs/configs
│   ├── layer_2_01_manager_handoff_documents/
│   │   ├── 2.00_to_universal/
│   │   └── 2.01_to_specific/
│   ├── layer_2_02_sub_layers/            # Sub-layer slots
│   └── layer_2_99_stages/                # Stage folders
├── layer_3/                              # Layer 3 grouping folder (sibling)
│   ├── layer_3_sub_features/
│   └── layer_3_sub_components/
└── README.md
```

## Manager + Handoff (layer_2/)
- layer_2_00_ai_manager_system: feature manager docs/configs.
- layer_2_01_manager_handoff_documents: `2.00_to_universal/` and `2.01_to_specific/` for up/downstream handoffs.

## Slots (stored under `layer_2/layer_2_02_sub_layers/` as `sub_layer_2.xx_*`)
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
- sub_layer_2.11_feature_tools: scripts/migrations/backfills specific to this feature.
- sub_layer_2.12_feature_agent_setup: feature-specific agent configuration with model fallbacks (depends on 2.08, 2.09, 2.10, 2.11).

## Feature AI Setup Dependency Chain (2.08–2.12)

The slots 2.08–2.12 form a dependency chain for feature-level AI agent setup:
- **2.08** → **2.09**: Feature MCP servers are configured within feature AI apps/tools
- **2.09** → **2.10**: Feature models may be accessed via MCP servers
- **2.10** → **2.11**: Feature tools provide capabilities that agents can use
- **2.11** → **2.12**: Feature agents require tools (including feature tools) to function
- **2.12** depends on all four: agents run in feature apps (2.08), use feature MCP servers (2.09), require feature models (2.10), and use feature tools (2.11)

Configure these in order when setting up feature-specific AI environments.

## Nested Content Directories (layer_3/)

**Same-Type Nesting Rule:** The "sub" prefix applies when nesting the same type. Since a feature inside a feature is same-type nesting, sub-features and sub-components here DO use the "sub" prefix.

- layer_3/layer_3_sub_features/: Sub-features within this feature (feature→feature = same-type, uses "sub")
- layer_3/layer_3_sub_components/: Sub-components within this feature (in feature context, uses "sub")

## Stages (layer_2/layer_2_99_stages/, folders named `stage_2.xx_*`)
- stage_2.00_request_gathering
- stage_2.01_instructions
- stage_2.02_planning
- stage_2.03_design
- stage_2.04_implementation
- stage_2.05_testing
- stage_2.06_criticism
- stage_2.07_fixing
- stage_2.08_archiving

Copy, rename to your feature, and populate each slot.
