# Feature Layer Template (2.x)

Use this to scaffold any feature-level context. Depends on universal (0.x) and project (1.x) layers.

## Slots
- 2.00_basic_prompts: feature init + what-to-do-next.
- 2.10_feature_knowledge: domain/UX/business knowledge specific to this feature.
- 2.20_feature_principles: local design/perf/security principles.
- 2.30_feature_rules: must/never rules, data constraints.
- 2.40_feature_os: platform/browser/runtime specifics (if any).
- 2.45_feature_env_layout: where the feature lives, services/modules it touches, env/config needs.
- 2.50_feature_architecture: FE/BE/data/API shape for this feature.
- 2.55_feature_coding_app_setup: run/debug configs, scripts for this feature.
- 2.60_feature_apps_tools: dashboards/monitoring/admin relevant to this feature.
- 2.70_feature_ai_app_tool_usage: feature-level AI workflows.
- 2.80_feature_model_usage: models wired into this feature (if any).
- 2.90_feature_tools: scripts/migrations/backfills specific to this feature.
- 2.99_stages: stage folders and status template.

## Stages (2.99)
0.0 instructions → 0.1 planning → 0.2 design → 0.3 development → 0.4 testing → 0.5 criticism → 0.6 fixing → 0.7 archives.

Copy, rename to your feature, and populate each slot.
