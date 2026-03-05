---
resource_id: "4a137e61-5be8-4c76-8c19-d7b40203e217"
resource_type: "readme
document"
resource_name: "README"
---
# Project Layer Template (1.x, zero-padded)

Use this to scaffold any project-level context. Mirrors the universal 0.x stack but specialized for a single project.

**This template implements Layer 1 (Project) of the [Ideal AI Manager Hierarchy System](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md).**

The Project layer inherits Universal (L0) constraints and adds project-specific architecture, tech stack, and requirements. For architectural details, see:
- [`architecture.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md) – Layer inheritance and project-level responsibilities
- [`tools_and_context_systems.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md) – Tool selection for project managers vs. workers

## Directory Structure

```
1_project_template/
├── layer_1/                              # Layer 1 grouping folder
│   ├── layer_1_00_ai_manager_system/     # Manager docs/configs
│   ├── layer_1_01_manager_handoff_documents/
│   │   ├── 1.00_to_universal/
│   │   └── 1.01_to_specific/
│   ├── layer_1_02_sub_layers/            # Sub-layer slots
│   └── layer_1_99_stages/                # Stage folders
├── layer_2/                              # Layer 2 grouping folder (sibling)
│   ├── layer_2_sub_projects/
│   ├── layer_2_features/
│   └── layer_2_components/
└── README.md
```

## Manager + Handoff (layer_1/)
- layer_1_00_ai_manager_system: project-level manager docs/configs.
- layer_1_01_manager_handoff_documents: `1.00_to_universal/` and `1.01_to_specific/` for up/downstream handoffs.

## Slots (stored under `layer_1/layer_1_02_sub_layers/` as `sub_layer_1.xx_*`)
- sub_layer_1.01_basic_prompts: project init + what-to-do-next prompts.
- sub_layer_1.02_project_se_knowledge: SE/domain knowledge this project relies on.
- sub_layer_1.03_project_principles: project-specific design/UX/security principles.
- sub_layer_1.04_project_rules: hard rules (branching, testing, compliance).
- sub_layer_1.05_project_os_setup: OS targets/requirements for dev/prod.
- sub_layer_1.06_project_coding_app_setup: IDE/run/debug configs for this project.
- sub_layer_1.07_project_apps_browsers_extensions_setup: dashboards, admin panels, monitoring tools, browser extensions.
- sub_layer_1.08_project_ai_apps_tools_setup: project-specific AI apps/tools configuration.
- sub_layer_1.09_project_mcp_servers_and_tools_setup: project-specific MCP server setup (depends on 1.08).
- sub_layer_1.10_project_ai_models: approved models for this project and their uses.
- sub_layer_1.11_project_tools: project-specific scripts/CLIs/migrations.
- sub_layer_1.12_project_agent_setup: project-specific agent configuration with model fallbacks (depends on 1.08, 1.09, 1.10, 1.11).

## Project AI Setup Dependency Chain (1.08–1.12)

The slots 1.08–1.12 form a dependency chain for project-level AI agent setup:
- **1.08** → **1.09**: Project MCP servers are configured within project AI apps/tools
- **1.09** → **1.10**: Project models may be accessed via MCP servers
- **1.10** → **1.11**: Project tools provide capabilities that agents can use
- **1.11** → **1.12**: Project agents require tools (including project tools) to function
- **1.12** depends on all four: agents run in project apps (1.08), use project MCP servers (1.09), require project models (1.10), and use project tools (1.11)

Configure these in order when setting up project-specific AI environments.

## Nested Content Directories (layer_2/)

**Same-Type Nesting Rule:** The "sub" prefix only applies to same-type nesting. Since features and components are different types from projects, they do NOT use the "sub" prefix.

- layer_2/layer_2_sub_projects/: Sub-projects within this project (project→project = same-type, uses "sub")
- layer_2/layer_2_features/: Features within this project (project→feature = different type, NO "sub")
- layer_2/layer_2_components/: Components within this project (project→component = different type, NO "sub")

## Stages (layer_1/layer_1_99_stages/, folders named `stage_1.xx_*`)
- stage_1.00_request_gathering
- stage_1.01_instructions
- stage_1.02_planning
- stage_1.03_design
- stage_1.04_implementation
- stage_1.05_testing
- stage_1.06_criticism
- stage_1.07_fixing
- stage_1.09_archives

Copy, rename to your project, and populate each slot.
