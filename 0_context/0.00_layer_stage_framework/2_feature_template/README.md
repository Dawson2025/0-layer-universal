# Feature Layer Template (2.x, zero-padded)

Use this to scaffold any feature-level context. Depends on universal (0.x) and project (1.x) layers.

## Slots (stored under `2.01_sub_layers/`)
- 2.01_basic_prompts: feature init + what-to-do-next.
- 2.02_feature_knowledge: domain/UX/business knowledge specific to this feature.
- 2.03_feature_principles: local design/perf/security principles.
- 2.04_feature_rules: must/never rules, data constraints.
- 2.05_feature_os: platform/browser/runtime specifics (if any).
- 2.06_feature_env_layout: where the feature lives, services/modules it touches, env/config needs.
- 2.07_feature_architecture: FE/BE/data/API shape for this feature.
- 2.08_feature_coding_app_setup: run/debug configs, scripts for this feature.
- 2.09_feature_apps_tools: dashboards/monitoring/admin relevant to this feature.
- 2.10_feature_ai_app_tool_usage: feature-level AI workflows.
- 2.11_feature_model_usage: models wired into this feature (if any).
- 2.12_feature_tools: scripts/migrations/backfills specific to this feature.
- 2.99_stages: stage folders and status template.

## Stages (2.99, stored under `2.99_stages/`, folders named `stage_2.xx_*`)
stage_2.01_instructions → stage_2.02_planning → stage_2.03_design → stage_2.04_development → stage_2.05_testing → stage_2.06_criticism → stage_2.07_fixing → stage_2.08_archives.

Copy, rename to your feature, and populate each slot.
