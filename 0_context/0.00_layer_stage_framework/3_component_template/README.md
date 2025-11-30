# Component Layer Template (3.x)

Use this to scaffold any component-level context. Depends on universal (0.x), project (1.x), and feature (2.x) layers.

## Slots
- 3.00_basic_prompts: component init + what-to-do-next.
- 3.10_component_knowledge: what this component does; contracts/invariants.
- 3.20_component_principles: micro-principles (purity, idempotency, perf goals).
- 3.30_component_rules: strict requirements (logging, validation, error handling).
- 3.40_component_os: only if OS/platform-specific.
- 3.45_component_env_layout: exact paths/deps/config this component needs.
- 3.50_component_architecture: internal structure/data flow/interfaces.
- 3.55_component_coding_app_setup: run/debug/test configs for this component.
- 3.60_component_apps_tools: dashboards/tools relevant to this component.
- 3.70_component_ai_app_tool_usage: component-level AI calls/workflows.
- 3.80_component_model_usage: models wired into this component (if any).
- 3.90_component_tools: helper scripts/utilities for this component.
- 3.99_stages: stage folders and status template.

## Stages (3.99)
0.0 instructions → 0.1 planning → 0.2 design → 0.3 development → 0.4 testing → 0.5 criticism → 0.6 fixing → 0.7 archives.

Copy, rename to your component, and populate each slot.
