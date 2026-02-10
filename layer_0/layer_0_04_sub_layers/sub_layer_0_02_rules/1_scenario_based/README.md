# 1_scenario_based

## Purpose

Rules in this folder are important and universal, but apply in **specific scenarios** rather than every API request. They should be **referenced** in CLAUDE.md files but not fully included, to save space.

## Rules

| File | When to Apply |
|------|---------------|
| `safety_governance.md` | Security decisions, permission escalations, sensitive operations |
| `AI_DOCUMENTATION_PROTOCOL.md` | Creating/organizing documentation, choosing where to put content |
| `LAYER_CONTEXT_HEADER_PROTOCOL.md` | Creating new files that need layer/stage headers |
| `sequential_development_methodology.md` | Multi-step development tasks, planning workflows |
| `CROSS_OS_COMPATIBILITY_RULES.md` | Writing code/scripts that must work across OS platforms |

## Usage

CLAUDE.md files should reference these rules like:

```markdown
## Scenario-Based Rules

For specific scenarios, read the full rules:
- Security decisions: `sub_layer_0_02_rules/1_scenario_based/safety_governance.md`
- Documentation: `sub_layer_0_02_rules/1_scenario_based/AI_DOCUMENTATION_PROTOCOL.md`
- File headers: `sub_layer_0_02_rules/1_scenario_based/LAYER_CONTEXT_HEADER_PROTOCOL.md`
```

## Why "Scenario Based"

These rules:
1. Are too detailed to include in every system prompt
2. Only apply when specific types of work are being done
3. Can be read on-demand when the scenario arises
