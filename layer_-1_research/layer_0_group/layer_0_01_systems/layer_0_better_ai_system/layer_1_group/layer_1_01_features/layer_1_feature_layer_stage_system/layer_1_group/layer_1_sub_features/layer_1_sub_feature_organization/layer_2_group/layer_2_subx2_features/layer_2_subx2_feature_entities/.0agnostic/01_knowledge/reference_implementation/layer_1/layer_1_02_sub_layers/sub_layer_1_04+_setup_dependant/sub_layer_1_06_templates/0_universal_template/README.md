---
resource_id: "2888884c-5471-4771-9040-1bef8f1fc508"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Universal Layer Template (0.x)

Use this when defining the universal layer for any ecosystem.

**This template implements Layer 0 (Universal) of the [Ideal AI Manager Hierarchy System](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md).**

The Universal layer defines global rules, tools, and standards that cascade down to all other layers (Project, Feature, Component). For architectural details, see:
- [`architecture.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md) – Layer responsibilities and context stacking
- [`tools_and_context_systems.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md) – Tool specialization at each layer
- [`os_and_quartets.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md) – OS-specific context variants

<!-- section_id: "d0763324-ddd1-481f-ab63-1e5995b83113" -->
## Directory Structure

```
0_universal_template/
├── layer_0_group/                              # Layer 0 grouping folder
│   ├── layer_0_00_ai_manager_system/     # Manager docs/configs
│   ├── layer_0_01_manager_handoff_documents/
│   │   ├── 0.00_to_universal/
│   │   └── 0.01_to_specific/
│   ├── layer_0_02_sub_layers/            # Sub-layer slots
│   └── layer_0_99_stages/                # Stage folders
└── README.md
```

<!-- section_id: "e9f49127-ad76-42b9-91b3-8627eff251f6" -->
## Manager + Handoff (layer_0_group/)
- layer_0_00_ai_manager_system: manager docs/configs.
- layer_0_01_manager_handoff_documents: `0.00_to_universal/` and `0.01_to_specific/` for cross-layer handoffs.

<!-- section_id: "44cafff2-2cb7-4055-814c-6f562f4b43a8" -->
## Slots (stored under `layer_0_group/layer_0_02_sub_layers/` as `sub_layer_0_xx_*`)
- sub_layer_0_01_basic_prompts_throughout: session init, what-to-do-next, core prompts.
- sub_layer_0_02_software_engineering_knowledge_system: general SE knowledge map.
- sub_layer_0_03_universal_principles: philosophies, values.
- sub_layer_0_04_universal_rules: hard constraints (git, terminal, security).
- sub_layer_0_05_os_setup: OS-specific setup (macOS/Linux/Windows).
- sub_layer_0_06_environment_setup: environment-level setup (git/github auth, credentials, shells).
- sub_layer_0_07_coding_app_setup: IDE/editor configuration.
- sub_layer_0_08_apps_browsers_extensions_setup: general apps, browsers, extensions.
- sub_layer_0_09_ai_apps_tools_setup: AI clients/CLIs and integrations.
- sub_layer_0_10_mcp_servers_and_tools_setup: MCP server setup and configuration (depends on 0.09).
- sub_layer_0_11_ai_models: approved models and usage guidance.
- sub_layer_0_12_universal_tools: cross-project scripts/utilities.
- sub_layer_0_13_agent_setup: agent configuration with model fallbacks and MCP integration (depends on 0.09, 0.10, 0.11, 0.12).

<!-- section_id: "cbe02dfc-ef5b-437a-b380-3e9718d04161" -->
## AI Setup Dependency Chain (0.09–0.13)

The slots 0.09–0.13 form a critical dependency chain for AI agent setup:
- **0.09** → **0.10**: MCP servers are configured within AI apps/tools
- **0.10** → **0.11**: Models may be accessed via MCP servers
- **0.11** → **0.12**: Universal tools provide capabilities that agents can use
- **0.12** → **0.13**: Agents require tools (including universal tools) to function
- **0.13** depends on all four: agents run in apps (0.09), use MCP servers (0.10), require models (0.11), and use universal tools (0.12)

Configure these in order when setting up a new AI environment.

<!-- section_id: "22011a5d-851e-44d2-a243-ed0b844def36" -->
## Stages (layer_0_group/layer_0_99_stages/, folders named `stage_0_xx_*`)
- stage_0_00_request_gathering
- stage_0_01_instructions
- stage_0_02_planning
- stage_0_03_design
- stage_0_04_implementation
- stage_0_05_testing
- stage_0_06_criticism
- stage_0_07_fixing
- stage_0_09_archives

Copy this template, rename for your universal context, and populate per slot.
