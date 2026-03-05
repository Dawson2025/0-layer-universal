---
resource_id: "3250c79a-0022-4586-947b-59fd9c90a73d"
resource_type: "readme
document"
resource_name: "README"
---
# Sub-Project Layer Template (2.x, zero-padded)

Use this to scaffold any sub-project within a parent project. Sub-projects are nested projects that warrant their own scope, lifecycle, and potentially their own Git repository (submodule).

**This template implements Layer 2 (Sub-Project) of the Layer + Stage Framework.**

The Sub-Project layer inherits Project (L1) constraints and adds sub-project-specific context. For architectural details, see:
- [`architecture.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md) – Layer inheritance and sub-project responsibilities
- [`FLEXIBLE_LAYERING_SYSTEM.md`](../FLEXIBLE_LAYERING_SYSTEM.md) – Flexible nesting patterns

<!-- section_id: "3f72de70-8b32-4b43-8810-8ccac0de2668" -->
## When to Use a Sub-Project

Use this template when you have a nested project that:
- Has its own distinct scope and lifecycle
- Warrants its own Git repository (as a submodule of the parent)
- Contains multiple features/components of its own
- Examples: Individual classes within a school project, microservices within a monorepo

<!-- section_id: "148230b6-5731-4839-a533-37442fb000c3" -->
## Directory Structure

```
2_sub_project_template/
├── layer_2/                              # Layer 2 grouping folder
│   ├── layer_2_00_ai_manager_system/     # Manager docs/configs
│   ├── layer_2_01_manager_handoff_documents/
│   │   ├── 2.00_to_universal/
│   │   └── 2.01_to_specific/
│   ├── layer_2_02_sub_layers/            # Sub-layer slots
│   └── layer_2_99_stages/                # Stage folders
├── layer_3/                              # Layer 3 grouping folder (sibling)
│   ├── layer_3_subx2_projects/
│   ├── layer_3_features/
│   └── layer_3_components/
└── README.md
```

<!-- section_id: "dfbb1116-8cec-422a-8f42-6804e9d2182a" -->
## Manager + Handoff (layer_2/)
- layer_2_00_ai_manager_system: sub-project-level manager docs/configs.
- layer_2_01_manager_handoff_documents: `2.00_to_universal/` and `2.01_to_specific/` for up/downstream handoffs.

<!-- section_id: "bbd7c9db-1470-49f8-862a-bf20acfb9972" -->
## Slots (stored under `layer_2/layer_2_02_sub_layers/` as `sub_layer_2.xx_*`)
- sub_layer_2.01_basic_prompts: sub-project init + what-to-do-next prompts.
- sub_layer_2.02_sub_project_se_knowledge: SE/domain knowledge this sub-project relies on.
- sub_layer_2.03_sub_project_principles: sub-project-specific design/UX/security principles.
- sub_layer_2.04_sub_project_rules: hard rules (branching, testing, compliance).
- sub_layer_2.05_sub_project_os_setup: OS targets/requirements for dev/prod.
- sub_layer_2.06_sub_project_coding_app_setup: IDE/run/debug configs for this sub-project.
- sub_layer_2.07_sub_project_apps_browsers_extensions_setup: dashboards, admin panels, monitoring tools, browser extensions.
- sub_layer_2.08_sub_project_ai_apps_tools_setup: sub-project-specific AI apps/tools configuration.
- sub_layer_2.09_sub_project_mcp_servers_and_tools_setup: sub-project-specific MCP server setup (depends on 2.08).
- sub_layer_2.10_sub_project_ai_models: approved models for this sub-project and their uses.
- sub_layer_2.11_sub_project_tools: sub-project-specific scripts/CLIs/migrations.
- sub_layer_2.12_sub_project_agent_setup: sub-project-specific agent configuration with model fallbacks.

<!-- section_id: "09122d45-9e59-4772-b62d-f552a69b8f30" -->
## Nested Content Directories (layer_3/)

**Same-Type Nesting Rule:** The "sub" prefix only applies to same-type nesting. Since a feature inside a sub_project is a different type (not project→project), features and components here do NOT use the "sub" prefix.

- layer_3/layer_3_subx2_projects/: Nested subx2-projects within this sub-project (project→project = same-type)
- layer_3/layer_3_features/: Features within this sub-project (project→feature = different type, NO "sub")
- layer_3/layer_3_components/: Components within this sub-project (project→component = different type, NO "sub")

<!-- section_id: "e6aece19-d76c-4ada-a888-e373abd0336d" -->
## Stages (layer_2/layer_2_99_stages/, folders named `stage_2.xx_*`)
- stage_2.00_request_gathering
- stage_2.01_instructions
- stage_2.02_planning
- stage_2.03_design
- stage_2.04_development
- stage_2.05_testing
- stage_2.06_criticism
- stage_2.07_fixing
- stage_2.09_archives

Copy, rename to `layer_2_sub_project_<name>`, and populate each slot.
