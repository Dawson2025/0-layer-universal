# Project Layer Template (1.x, zero-padded)

Use this to scaffold any project-level context. Mirrors the universal 0.x stack but specialized for a single project.

## Slots (stored under `1.01_sub_layers/`)
- 1.01_basic_prompts: project init + what-to-do-next prompts.
- 1.02_project_se_knowledge: SE/domain knowledge this project relies on.
- 1.03_project_principles: project-specific design/UX/security principles.
- 1.04_project_rules: hard rules (branching, testing, compliance).
- 1.05_project_os: OS targets/requirements for dev/prod.
- 1.06_project_env_repo_layout: local/remote env details; repo layout/monorepo notes.
- 1.07_project_architecture: stack (FE/BE/Data/Auth/Storage/Integrations) + diagrams.
- 1.08_project_coding_app_setup: IDE/run/debug configs for this project.
- 1.09_project_apps_browsers_tools: dashboards, admin panels, monitoring tools.
- 1.10_project_ai_app_tool_usage: approved AI tools/agents and scopes.
- 1.11_project_model_usage: approved models for this project and their uses.
- 1.12_project_tools: project-specific scripts/CLIs/migrations.
- 1.99_stages: stage folders and status template.

## Stages (1.99, stored under `1.99_stages/`)
1.01 instructions → 1.02 planning → 1.03 design → 1.04 development → 1.05 testing → 1.06 criticism → 1.07 fixing → 1.08 archives.

Copy, rename to your project, and populate each slot.
