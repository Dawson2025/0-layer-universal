---
resource_id: "01cc122f-c203-4b09-a917-de38c42a0c31"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Agent Coordination Knowledge

<!-- section_id: "776eff4e-9d60-4da0-951a-274b7967a8b7" -->
## Purpose

This folder documents how AI agents coordinate work across layers, stages, and sub-layers - including when to expand scope versus delegate to other agents.

---

<!-- section_id: "9efa8d43-9dd5-4417-83bf-f68126e075d0" -->
## Contents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| [SCOPE_VS_DELEGATION.md](SCOPE_VS_DELEGATION.md) | When to do work yourself vs spawn agents | Before working across layers/stages |
| [HANDOFF_PROTOCOLS.md](HANDOFF_PROTOCOLS.md) | How to communicate between agents | When delegating or receiving delegation |
| [MULTI_AGENT_PATTERNS.md](MULTI_AGENT_PATTERNS.md) | Coordination patterns for complex work | Planning multi-agent tasks |

---

<!-- section_id: "ce855c14-0bfa-4ce8-ac6a-8f2ae71e2e66" -->
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

<!-- section_id: "430c1f0b-3f26-488f-8d8c-29a99738a664" -->
## Key Concepts

<!-- section_id: "e90590ea-c1f4-4695-b4de-0d2b352ef1c3" -->
### Scope Expansion
- Load additional layer/stage context yourself
- Maintain continuity and full context
- Best for: small tasks, tightly coupled work, sequential dependencies

<!-- section_id: "201a7f4c-678a-46b2-a8f1-7e475b65172f" -->
### Delegation
- Spawn agents at other entry points via CLI
- Communicate via handoff documents
- Best for: large tasks, parallel work, specialized domains

<!-- section_id: "816f48d5-6f6a-4c72-bdef-8505950fe7f6" -->
### Entry Points
Every layer, stage, sub-layer, or sub-stage with a CLAUDE.md can be an agent entry point.

---

<!-- section_id: "84ff8bae-5dae-4e99-ba04-f54df87f63ec" -->
## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows
- [../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md](../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md) - Sub-layer entry points
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and managing entities

---

*Agent coordination documentation*
