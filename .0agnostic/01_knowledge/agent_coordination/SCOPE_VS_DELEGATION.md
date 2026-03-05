---
resource_id: "1dd9c5f3-4a13-49a8-b2bc-8731a104aaee"
resource_type: "knowledge"
resource_name: "SCOPE_VS_DELEGATION"
---
# Agent Scope vs Delegation Decisions

<!-- section_id: "b28d3f97-6bcb-48fe-9496-411d57eb2020" -->
## Overview

When an AI agent needs work done in other layers, stages, or sub-layers, it must decide:

1. **Expand Scope** - Do the work itself by loading additional context
2. **Delegate** - Spawn other agents at those entry points via CLI tools

This document provides decision criteria for making this choice efficiently.

---

<!-- section_id: "831d53ad-00b6-49e3-829e-dbef5f2150e7" -->
## The Core Trade-off

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCOPE vs DELEGATION TRADE-OFF                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EXPAND SCOPE (Do it yourself)                                              │
│  ─────────────────────────────                                              │
│  ✓ No communication overhead                                                │
│  ✓ Full context continuity                                                  │
│  ✓ Simpler coordination                                                     │
│  ✗ Context window fills up                                                  │
│  ✗ May lack specialized knowledge                                           │
│  ✗ Sequential processing only                                               │
│                                                                             │
│  DELEGATE (Spawn other agents)                                              │
│  ─────────────────────────────                                              │
│  ✓ Parallel processing possible                                             │
│  ✓ Specialized agents per entry point                                       │
│  ✓ Fresh context windows                                                    │
│  ✗ Communication overhead (handoffs)                                        │
│  ✗ Coordination complexity                                                  │
│  ✗ Context may be lost between agents                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "ae5d3cd3-86d4-4fa3-8686-8077715cf6a1" -->
## Decision Matrix

<!-- section_id: "0f6ff6a2-b8b1-47a2-a2d4-c5907107db4a" -->
### When to EXPAND SCOPE (Work Yourself)

| Condition | Why Expand |
|-----------|------------|
| **Small task** in other layer/stage | Overhead of delegation > task effort |
| **Tightly coupled work** | Need continuous context between parts |
| **Sequential dependency** | Each step needs previous step's output |
| **Quick lookup** | Just reading a file or checking a rule |
| **Same domain knowledge** | Your current expertise applies |
| **1-2 additional layers** | Manageable context expansion |

<!-- section_id: "803b76e3-88c2-4400-be6f-61b117d27747" -->
### When to DELEGATE (Spawn Agents)

| Condition | Why Delegate |
|-----------|--------------|
| **Large independent tasks** | Can run in parallel |
| **Specialized domain** | Other entry point has specific expertise |
| **Deep layer/stage nesting** | Would overload your context |
| **Different critical rules** | Specialized agent knows local rules |
| **Long-running task** | Don't block your current work |
| **3+ additional layers** | Too much context to manage |

---

<!-- section_id: "521bc799-e7c4-4747-8787-07529dd4a95d" -->
## Decision Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCOPE vs DELEGATION DECISION FLOW                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Need work in another layer/stage/sub-layer?                                │
│                     │                                                       │
│                     ▼                                                       │
│  ┌─────────────────────────────────────┐                                   │
│  │ Is the task small and quick?        │                                   │
│  │ (< 5 minutes, simple lookup/edit)   │                                   │
│  └─────────────────┬───────────────────┘                                   │
│           YES      │      NO                                                │
│            │       │       │                                                │
│            ▼       │       ▼                                                │
│     EXPAND SCOPE   │  ┌─────────────────────────────────────┐              │
│                    │  │ Does it require specialized context │              │
│                    │  │ I don't have?                       │              │
│                    │  └─────────────────┬───────────────────┘              │
│                    │          YES       │      NO                           │
│                    │           │        │       │                           │
│                    │           ▼        │       ▼                           │
│                    │      DELEGATE      │  ┌─────────────────────────────┐ │
│                    │                    │  │ Can tasks run in parallel?  │ │
│                    │                    │  └─────────────────┬───────────┘ │
│                    │                    │          YES       │      NO     │
│                    │                    │           │        │       │     │
│                    │                    │           ▼        │       ▼     │
│                    │                    │      DELEGATE      │  ┌─────────┐│
│                    │                    │                    │  │ How many││
│                    │                    │                    │  │ layers? ││
│                    │                    │                    │  └────┬────┘│
│                    │                    │                    │   1-2 │ 3+  │
│                    │                    │                    │    │  │  │  │
│                    │                    │                    │    ▼  │  ▼  │
│                    │                    │              EXPAND SCOPE  DELEGATE│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "9fd4d2f9-c997-45f7-8f80-113cc1651068" -->
## Efficiency Factors to Consider

<!-- section_id: "2416482f-88ab-4cb8-b8c2-9020801944b8" -->
### 1. Context Window Cost

```
Your current context usage: [estimate %]

Adding layer context:
  - CLAUDE.md: ~50-200 lines
  - Critical rules: ~20-50 lines
  - Domain knowledge: varies (100-1000+ lines)

If (current_usage + new_context) > 70%:
  → Consider DELEGATE

If (current_usage + new_context) < 50%:
  → EXPAND SCOPE is safe
```

<!-- section_id: "9d7a65f7-2cb7-4b14-ae64-b54f751ed568" -->
### 2. Task Dependency Graph

```
Independent tasks:          → DELEGATE (parallel)
┌───┐  ┌───┐  ┌───┐
│ A │  │ B │  │ C │
└───┘  └───┘  └───┘

Sequential tasks:           → EXPAND SCOPE (continuity)
┌───┐ → ┌───┐ → ┌───┐
│ A │   │ B │   │ C │
└───┘   └───┘   └───┘

Mixed:                      → EXPAND for chain, DELEGATE for independent
┌───┐ → ┌───┐     ┌───┐
│ A │   │ B │     │ D │  (D is independent)
└───┘   └───┘     └───┘
          │
          ▼
        ┌───┐
        │ C │
        └───┘
```

<!-- section_id: "3b81bc07-3d2f-4766-b1d1-22ec4e3e46a2" -->
### 3. Specialization Benefit

```
Same domain (you know it):         → EXPAND SCOPE
┌─────────────────────────────┐
│ Your expertise: Python API   │
│ Task: Python API changes     │  → Do it yourself
└─────────────────────────────┘

Different domain (specialized):    → DELEGATE
┌─────────────────────────────┐
│ Your expertise: Python API   │
│ Task: Kubernetes deployment  │  → Delegate to K8s specialist
└─────────────────────────────┘
```

<!-- section_id: "8ff24b9e-d325-4160-b55e-1c45d9b3a687" -->
### 4. Communication Overhead

```
Simple output (file, result):      → DELEGATE is cheap
Complex state transfer:            → EXPAND SCOPE is cheaper

Handoff document complexity:
  - Simple: < 50 lines → delegation OK
  - Medium: 50-200 lines → consider expanding
  - Complex: 200+ lines → definitely expand
```

---

<!-- section_id: "d3b81b21-685b-4fe8-ab67-d6d7b64b228c" -->
## How to Delegate via CLI

<!-- section_id: "3bcf39f3-ab58-4b37-a304-1108e24f1852" -->
### Spawning an Agent at Another Entry Point

```bash
# Navigate to target entry point
cd /path/to/layer_N/entry_point/

# Spawn agent with task
claude --task "Description of what to do" \
       --handoff-in ./hand_off_documents/incoming/task.md \
       --handoff-out ./hand_off_documents/outgoing/result.md
```

<!-- section_id: "19d9599b-acd4-424b-a0d7-0b4a334be07c" -->
### Using Task Tool for Delegation

```
Task tool parameters:
- subagent_type: "general-purpose" or specialized
- prompt: Clear task description
- Entry point context will load automatically
```

<!-- section_id: "e4ade3d8-eec9-486e-992e-b439d56ab941" -->
### Handoff Document for Delegation

```markdown
# Task Handoff

## From
- Agent: [your identity]
- Entry point: [your location]
- Session: [timestamp]

## Task
[Clear description of what needs to be done]

## Context Provided
[Any context the delegated agent needs]

## Expected Output
[What should come back]

## Constraints
[Any rules or limitations]

## Return To
[Path for result handoff document]
```

---

<!-- section_id: "c817d3b7-7726-4597-a4e7-a2860f2062a9" -->
## Agent Coordination Patterns

<!-- section_id: "173e38fb-40e6-47dc-8406-13779493045f" -->
### Pattern 1: Hub and Spoke (You Coordinate)

```
                    ┌─────────┐
                    │   YOU   │
                    │ (Hub)   │
                    └────┬────┘
           ┌─────────────┼─────────────┐
           │             │             │
           ▼             ▼             ▼
      ┌─────────┐   ┌─────────┐   ┌─────────┐
      │ Agent A │   │ Agent B │   │ Agent C │
      │(layer_1)│   │(layer_2)│   │(stage_6)│
      └─────────┘   └─────────┘   └─────────┘

Use when: You need to coordinate results from multiple agents
```

<!-- section_id: "864540dc-351a-42ac-a791-d0617fdc0687" -->
### Pattern 2: Chain (Sequential Delegation)

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│   YOU   │ ──▶ │ Agent A │ ──▶ │ Agent B │ ──▶ │ Agent C │
└─────────┘     └─────────┘     └─────────┘     └─────────┘

Use when: Each agent's output feeds the next
```

<!-- section_id: "82a26ab7-f4f0-4638-81f7-5d674f46c515" -->
### Pattern 3: Expand Then Delegate

```
┌─────────────────────────────────────┐
│              YOU                     │
│  (expanded scope for core work)     │
│                                     │
│  ┌──────────────────────────────┐  │
│  │ Layer 0 + Layer 1 context    │  │
│  │ (doing main implementation)  │  │
│  └──────────────────────────────┘  │
└─────────────────┬───────────────────┘
                  │
        ┌─────────┼─────────┐
        │ delegate         │ delegate
        ▼                  ▼
   ┌─────────┐        ┌─────────┐
   │ Agent A │        │ Agent B │
   │ (tests) │        │ (docs)  │
   └─────────┘        └─────────┘

Use when: Core work needs unified context, side tasks are independent
```

---

<!-- section_id: "43002927-3fbe-4c6c-b286-a527f9fa486d" -->
## Scope Expansion Checklist

Before expanding your scope:

- [ ] Will adding this context keep me under 70% context usage?
- [ ] Do I have the domain knowledge for this area?
- [ ] Is the work tightly coupled with my current task?
- [ ] Are the critical rules similar/compatible?
- [ ] Can I complete this without losing track of my main task?

If all YES → Expand scope safely

---

<!-- section_id: "2455b491-4efd-49f0-b2d3-7dd989c03bfc" -->
## Delegation Checklist

Before delegating:

- [ ] Is the task clearly defined and self-contained?
- [ ] Have I written a clear handoff document?
- [ ] Is the target entry point appropriate for this task?
- [ ] Do I know where to receive the result?
- [ ] Can I continue other work while waiting?

If all YES → Delegate efficiently

---

<!-- section_id: "a5c60544-2c64-4fb3-8078-6d60dac14f01" -->
## Examples

<!-- section_id: "653c3b0e-eba2-4662-80e3-1abc0d742343" -->
### Example 1: Small Scope Expansion

```
Current: Working in layer_1_project/stage_06_development/

Need: Check a universal rule in layer_0

Decision: EXPAND SCOPE
- Reason: Quick lookup, minimal context addition
- Action: Read layer_0/.../sub_layer_0_02_rules/rule.md
- Continue with expanded knowledge
```

<!-- section_id: "c60774f4-c070-49a6-8b49-1f941efb2cdc" -->
### Example 2: Delegation for Parallel Work

```
Current: Working in layer_1_project/

Need:
- Run tests in stage_07_testing/
- Update docs in stage_10_current_product/
- Fix linting in stage_09_fixing/

Decision: DELEGATE all three
- Reason: Independent tasks, can run in parallel
- Action: Spawn 3 agents at each stage entry point
- Collect results via handoff documents
```

<!-- section_id: "6bd9b663-56a9-4bb9-880e-6d3dc52bc9d5" -->
### Example 3: Mixed Strategy

```
Current: Working on feature in layer_2_feature_auth/

Need:
- Implement core logic (sequential, complex)
- Write tests (independent)
- Update project README (independent)

Decision:
- EXPAND SCOPE for core logic (needs continuity)
- DELEGATE tests to stage_07 agent
- DELEGATE README to layer_1 agent
```

---

<!-- section_id: "a6f6e26b-ed47-4763-8186-643d1e5eea1e" -->
## Self-Assessment Questions

When facing work in other layers/stages, ask:

1. **How big is this task?** (minutes vs hours)
2. **How specialized is the domain?** (general vs expert)
3. **How coupled is it to my current work?** (tight vs loose)
4. **Can it run in parallel?** (independent vs dependent)
5. **How deep is the layer/stage nesting?** (1-2 vs 3+)
6. **How much context would I need to add?** (small vs large)

---

*See AI_CONTEXT_FLOW_ARCHITECTURE.md for context cascade details*
*See ../entity_lifecycle/INSTANTIATION_GUIDE.md for spawning agents*
