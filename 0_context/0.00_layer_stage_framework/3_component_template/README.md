# Component Layer Template (3.x, zero-padded)

Use this to scaffold any component-level context. Depends on universal (0.x), project (1.x), and feature (2.x) layers.

## Slots (stored under `3.01_sub_layers/`)
- 3.01_basic_prompts: component init + what-to-do-next.
- 3.02_component_knowledge: what this component does; contracts/invariants.
- 3.03_component_principles: micro-principles (purity, idempotency, perf goals).
- 3.04_component_rules: strict requirements (logging, validation, error handling).
- 3.05_component_os: only if OS/platform-specific.
- 3.06_component_env_layout: exact paths/deps/config this component needs.
- 3.07_component_architecture: internal structure/data flow/interfaces.
- 3.08_component_coding_app_setup: run/debug/test configs for this component.
- 3.09_component_apps_tools: dashboards/tools relevant to this component.
- 3.10_component_ai_app_tool_usage: component-level AI calls/workflows.
- 3.11_component_model_usage: models wired into this component (if any).
- 3.12_component_tools: helper scripts/utilities for this component.
- 3.99_stages: stage folders and status template.

## Stages (3.99, stored under `3.99_stages/`, folders named `stage_3.xx_*`)
stage_3.01_instructions → stage_3.02_planning → stage_3.03_design → stage_3.04_development → stage_3.05_testing → stage_3.06_criticism → stage_3.07_fixing → stage_3.08_archives.

Copy, rename to your component, and populate each slot.
