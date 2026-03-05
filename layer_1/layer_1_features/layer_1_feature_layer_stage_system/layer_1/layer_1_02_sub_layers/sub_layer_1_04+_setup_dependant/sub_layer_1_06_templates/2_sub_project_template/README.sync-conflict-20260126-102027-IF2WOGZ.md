---
resource_id: "95b5c46f-e398-4f53-9907-6502d8f56fad"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102027-IF2WOGZ"
---
# Sub-Project Layer Template (2.x, zero-padded)

Use this to scaffold any sub-project within a parent project. Sub-projects are nested projects that warrant their own scope, lifecycle, and potentially their own Git repository (submodule).

**This template implements Layer 2 (Sub-Project) of the Layer + Stage Framework.**

The Sub-Project layer inherits Project (L1) constraints and adds sub-project-specific context. For architectural details, see:
- [`architecture.md`](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md) – Layer inheritance and sub-project responsibilities
- [`FLEXIBLE_LAYERING_SYSTEM.md`](../FLEXIBLE_LAYERING_SYSTEM.md) – Flexible nesting patterns

<!-- section_id: "9531326d-93f3-45dc-b8f0-0dbe3747366a" -->
## When to Use a Sub-Project

Use this template when you have a nested project that:
- Has its own distinct scope and lifecycle
- Warrants its own Git repository (as a submodule of the parent)
- Contains multiple features/components of its own
- Examples: Individual classes within a school project, microservices within a monorepo

<!-- section_id: "cc2d806d-2301-42e4-86fe-7d4d3f79efba" -->
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

<!-- section_id: "63c4c4b1-7c92-47ca-8c31-04225e2d9967" -->
## Manager + Handoff (layer_2/)
- layer_2_00_ai_manager_system: sub-project-level manager docs/configs.
- layer_2_01_manager_handoff_documents: `2.00_to_universal/` and `2.01_to_specific/` for up/downstream handoffs.

<!-- section_id: "aff37e3d-23f6-45a3-8122-4f086e9255da" -->
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

<!-- section_id: "840d9d85-0a40-412c-8a4d-dcbdd0aa33df" -->
## Nested Content Directories (layer_3/)

**Same-Type Nesting Rule:** The "sub" prefix only applies to same-type nesting. Since a feature inside a sub_project is a different type (not project→project), features and components here do NOT use the "sub" prefix.

- layer_3/layer_3_subx2_projects/: Nested subx2-projects within this sub-project (project→project = same-type)
- layer_3/layer_3_features/: Features within this sub-project (project→feature = different type, NO "sub")
- layer_3/layer_3_components/: Components within this sub-project (project→component = different type, NO "sub")

<!-- section_id: "6016dfe0-338b-4dc1-ac6a-fbfabbc728bc" -->
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
