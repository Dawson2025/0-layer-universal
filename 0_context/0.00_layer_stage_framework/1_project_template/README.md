# Project Layer Template (1.x, zero-padded)

Use this to scaffold any project-level context. Mirrors the universal 0.x stack but specialized for a single project.

## Slots (stored under `1.01_sub_layers/` as `sub_layer_1.xx_*`)
- sub_layer_1.01_basic_prompts: project init + what-to-do-next prompts.
- sub_layer_1.02_project_se_knowledge: SE/domain knowledge this project relies on.
- sub_layer_1.03_project_principles: project-specific design/UX/security principles.
- sub_layer_1.04_project_rules: hard rules (branching, testing, compliance).
- sub_layer_1.05_project_os: OS targets/requirements for dev/prod.
- sub_layer_1.06_project_env_repo_layout: local/remote env details; repo layout/monorepo notes.
- sub_layer_1.07_project_architecture: stack (FE/BE/Data/Auth/Storage/Integrations) + diagrams.
- sub_layer_1.08_project_coding_app_setup: IDE/run/debug configs for this project.
- sub_layer_1.09_project_apps_browsers_tools: dashboards, admin panels, monitoring tools.
- sub_layer_1.10_project_ai_app_tool_usage: approved AI tools/agents and scopes.
- sub_layer_1.11_project_model_usage: approved models for this project and their uses.
- sub_layer_1.12_project_tools: project-specific scripts/CLIs/migrations.
- 1.99_stages: stage folders and status template.

## Stages (1.99, stored under `1.99_stages/`, folders named `stage_1.xx_*`)
stage_1.01_instructions → stage_1.02_planning → stage_1.03_design → stage_1.04_development → stage_1.05_testing → stage_1.06_criticism → stage_1.07_fixing → stage_1.08_archives.

Copy, rename to your project, and populate each slot.
