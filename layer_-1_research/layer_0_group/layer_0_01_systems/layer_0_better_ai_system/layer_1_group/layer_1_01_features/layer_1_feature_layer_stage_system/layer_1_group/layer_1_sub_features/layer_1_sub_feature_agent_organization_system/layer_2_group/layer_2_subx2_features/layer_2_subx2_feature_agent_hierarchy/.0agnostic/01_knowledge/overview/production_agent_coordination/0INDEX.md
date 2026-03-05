---
resource_id: "6c8256a6-a859-41af-ada8-d0b3c56cff80"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Agent Coordination Knowledge

<!-- section_id: "426ed82e-ca7e-4a09-9ac5-3175a6789f93" -->
## Purpose

This folder documents how AI agents coordinate work across layers, stages, and sub-layers - including when to expand scope versus delegate to other agents.

---

<!-- section_id: "1f55091d-d242-4843-aa3a-47c7d609d57c" -->
## Contents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| [SCOPE_VS_DELEGATION.md](SCOPE_VS_DELEGATION.md) | When to do work yourself vs spawn agents | Before working across layers/stages |
| [HANDOFF_PROTOCOLS.md](HANDOFF_PROTOCOLS.md) | How to communicate between agents | When delegating or receiving delegation |
| [MULTI_AGENT_PATTERNS.md](MULTI_AGENT_PATTERNS.md) | Coordination patterns for complex work | Planning multi-agent tasks |

---

<!-- section_id: "fed4c552-3816-4d07-95bb-edec4ec1bebc" -->
## Quick Decision Guide

```
Need work in another layer/stage?
          │
          ▼
    ┌─────────────┐
    │ Small task? │──YES──▶ EXPAND SCOPE (do it yourself)
    └──────┬──────┘
           │ NO
           ▼
    ┌─────────────────┐
    │ Specialized     │──YES──▶ DELEGATE to specialist agent
    │ domain needed?  │
    └──────┬──────────┘
           │ NO
           ▼
    ┌─────────────────┐
    │ Can run in      │──YES──▶ DELEGATE (parallel execution)
    │ parallel?       │
    └──────┬──────────┘
           │ NO
           ▼
    ┌─────────────────┐
    │ 3+ layers deep? │──YES──▶ DELEGATE (context limit)
    └──────┬──────────┘
           │ NO
           ▼
    EXPAND SCOPE (manageable)
```

---

<!-- section_id: "f4b4e7b8-0735-4810-8653-ff629fe46313" -->
## Key Concepts

<!-- section_id: "21711106-88b5-465e-8a87-1885120cea25" -->
### Scope Expansion
- Load additional layer/stage context yourself
- Maintain continuity and full context
- Best for: small tasks, tightly coupled work, sequential dependencies

<!-- section_id: "54e8df4d-066d-43a9-906c-199633b78359" -->
### Delegation
- Spawn agents at other entry points via CLI
- Communicate via handoff documents
- Best for: large tasks, parallel work, specialized domains

<!-- section_id: "220beaf5-641a-4339-b170-1be92c2295a3" -->
### Entry Points
Every layer, stage, sub-layer, or sub-stage with a CLAUDE.md can be an agent entry point.

---

<!-- section_id: "6fd2bc5c-0539-496b-b078-78092709cd8a" -->
## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows
- [../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md](../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md) - Sub-layer entry points
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and managing entities

---

*Agent coordination documentation*
