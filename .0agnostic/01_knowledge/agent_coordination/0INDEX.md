---
resource_id: "857cdf7a-6e59-4bf9-8082-36e68aa4aebf"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Agent Coordination Knowledge

## Purpose

This folder documents how AI agents coordinate work across layers, stages, and sub-layers - including when to expand scope versus delegate to other agents.

---

## Contents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| [SCOPE_VS_DELEGATION.md](SCOPE_VS_DELEGATION.md) | When to do work yourself vs spawn agents | Before working across layers/stages |
| [HANDOFF_PROTOCOLS.md](HANDOFF_PROTOCOLS.md) | How to communicate between agents | When delegating or receiving delegation |
| [MULTI_AGENT_PATTERNS.md](MULTI_AGENT_PATTERNS.md) | Coordination patterns for complex work | Planning multi-agent tasks |

---

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

## Key Concepts

### Scope Expansion
- Load additional layer/stage context yourself
- Maintain continuity and full context
- Best for: small tasks, tightly coupled work, sequential dependencies

### Delegation
- Spawn agents at other entry points via CLI
- Communicate via handoff documents
- Best for: large tasks, parallel work, specialized domains

### Entry Points
Every layer, stage, sub-layer, or sub-stage with a CLAUDE.md can be an agent entry point.

---

## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows
- [../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md](../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md) - Sub-layer entry points
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and managing entities

---

*Agent coordination documentation*
