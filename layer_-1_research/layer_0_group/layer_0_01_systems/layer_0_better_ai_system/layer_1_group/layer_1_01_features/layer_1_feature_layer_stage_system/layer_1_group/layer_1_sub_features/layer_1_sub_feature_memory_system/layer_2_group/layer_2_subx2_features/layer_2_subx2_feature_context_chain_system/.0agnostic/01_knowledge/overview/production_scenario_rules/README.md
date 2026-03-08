---
resource_id: "2be48daf-c1ad-4fb1-8ee3-4cef5f50d0a0"
resource_type: "readme_knowledge"
resource_name: "README"
---
# 1_scenario_based

<!-- section_id: "2cd59f03-d4ed-4ebf-af3c-2ac481e3915b" -->
## Purpose

Rules in this folder are important and universal, but apply in **specific scenarios** rather than every API request. They should be **referenced** in CLAUDE.md files but not fully included, to save space.

<!-- section_id: "f401d436-bb1d-4383-a682-d1829364211c" -->
## Rules

| File | When to Apply |
|------|---------------|
| `safety_governance.md` | Security decisions, permission escalations, sensitive operations |
| `AI_DOCUMENTATION_PROTOCOL.md` | Creating/organizing documentation, choosing where to put content |
| `LAYER_CONTEXT_HEADER_PROTOCOL.md` | Creating new files that need layer/stage headers |
| `sequential_development_methodology.md` | Multi-step development tasks, planning workflows |
| `CROSS_OS_COMPATIBILITY_RULES.md` | Writing code/scripts that must work across OS platforms |

<!-- section_id: "323c128b-a0f4-4817-9c71-47fc3a70cbed" -->
## Usage

CLAUDE.md files should reference these rules like:

```markdown
## Scenario-Based Rules

For specific scenarios, read the full rules:
- Security decisions: `sub_layer_0_04_rules/1_scenario_based/safety_governance.md`
- Documentation: `sub_layer_0_04_rules/1_scenario_based/AI_DOCUMENTATION_PROTOCOL.md`
- File headers: `sub_layer_0_04_rules/1_scenario_based/LAYER_CONTEXT_HEADER_PROTOCOL.md`
```

<!-- section_id: "f565ea38-b742-4d67-9422-6df8a17406df" -->
## Why "Scenario Based"

These rules:
1. Are too detailed to include in every system prompt
2. Only apply when specific types of work are being done
3. Can be read on-demand when the scenario arises
