---
resource_id: "857cdf7a-6e59-4bf9-8082-36e68aa4aebf"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Agent Coordination Knowledge

<!-- section_id: "c3f6dd04-4626-475c-a42b-a16c8d8c7340" -->
## Purpose

This folder documents how AI agents coordinate work across layers, stages, and sub-layers - including when to expand scope versus delegate to other agents.

---

<!-- section_id: "340aa56f-1ca1-4e3a-a18c-cb7dde61dfb7" -->
## Contents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| [SCOPE_VS_DELEGATION.md](SCOPE_VS_DELEGATION.md) | When to do work yourself vs spawn agents | Before working across layers/stages |
| [HANDOFF_PROTOCOLS.md](HANDOFF_PROTOCOLS.md) | How to communicate between agents | When delegating or receiving delegation |
| [MULTI_AGENT_PATTERNS.md](MULTI_AGENT_PATTERNS.md) | Coordination patterns for complex work | Planning multi-agent tasks |

---

<!-- section_id: "86a39984-c8f7-4eba-8803-def03694eeb6" -->
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

<!-- section_id: "524839ee-1335-4901-9c22-b5701451a64f" -->
## Key Concepts

<!-- section_id: "45b89729-81ec-45f5-a65a-af6c44bd71c3" -->
### Scope Expansion
- Load additional layer/stage context yourself
- Maintain continuity and full context
- Best for: small tasks, tightly coupled work, sequential dependencies

<!-- section_id: "76f5ee20-2715-413d-a656-e0441277a93e" -->
### Delegation
- Spawn agents at other entry points via CLI
- Communicate via handoff documents
- Best for: large tasks, parallel work, specialized domains

<!-- section_id: "ec8eb55f-a6cf-4364-a7ce-55a13d840b73" -->
### Entry Points
Every layer, stage, sub-layer, or sub-stage with a CLAUDE.md can be an agent entry point.

---

<!-- section_id: "b79f0c9e-52e1-4245-9608-2ac129df61ec" -->
## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows
- [../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md](../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md) - Sub-layer entry points
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and managing entities

---

*Agent coordination documentation*
