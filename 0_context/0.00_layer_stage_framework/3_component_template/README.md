# Component Layer Template (3.x, zero-padded)

Use this to scaffold any component-level context. Depends on universal (0.x), project (1.x), and feature (2.x) layers.

## Slots
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

## Stages (3.99)
0.01 instructions → 0.02 planning → 0.03 design → 0.04 development → 0.05 testing → 0.06 criticism → 0.07 fixing → 0.08 archives.

Copy, rename to your component, and populate each slot.
