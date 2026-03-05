---
resource_id: "15f5846b-03bb-41af-b1d3-5c118a1c4042"
resource_type: "knowledge"
resource_name: "SCOPE_VS_DELEGATION"
---
# Agent Scope vs Delegation Decisions

<!-- section_id: "8875e7eb-7e7e-45a7-944c-926046a49806" -->
## Overview

When an AI agent needs work done in other layers, stages, or sub-layers, it must decide:

1. **Expand Scope** - Do the work itself by loading additional context
2. **Delegate** - Spawn other agents at those entry points via CLI tools

This document provides decision criteria for making this choice efficiently.

---

<!-- section_id: "b2a4462a-bda7-4951-a0b2-eafdc5cea6f0" -->
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

<!-- section_id: "d460a929-0e06-408f-b265-bc3264616a6a" -->
## Decision Matrix

<!-- section_id: "f472e420-540f-466a-8c83-9079eaea46f6" -->
### When to EXPAND SCOPE (Work Yourself)

| Condition | Why Expand |
|-----------|------------|
| **Small task** in other layer/stage | Overhead of delegation > task effort |
| **Tightly coupled work** | Need continuous context between parts |
| **Sequential dependency** | Each step needs previous step's output |
| **Quick lookup** | Just reading a file or checking a rule |
| **Same domain knowledge** | Your current expertise applies |
| **1-2 additional layers** | Manageable context expansion |

<!-- section_id: "020fe956-bd55-4504-a52a-716bd2328a42" -->
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

<!-- section_id: "a08c52e6-725b-47e6-92af-96ad4e7a9572" -->
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

<!-- section_id: "1f1cdcdd-8446-4a37-83f4-72ba402e7186" -->
## Efficiency Factors to Consider

<!-- section_id: "cc8920c2-d62f-470b-8c9d-f3583cb9b0ec" -->
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

<!-- section_id: "992a81ba-1787-4cfe-8d19-38f1a966a8ce" -->
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

<!-- section_id: "b8ed58ad-01d9-4b21-af30-81143285b5fc" -->
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

<!-- section_id: "62eff03c-42c7-44a3-91dd-1816417f3865" -->
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

<!-- section_id: "99be2ab9-2bb2-4af6-a62c-3fa2abce1535" -->
## How to Delegate via CLI

<!-- section_id: "d018ce84-0b9e-4cee-9eda-4dc84ac570f5" -->
### Spawning an Agent at Another Entry Point

```bash
# Navigate to target entry point
cd /path/to/layer_N/entry_point/

# Spawn agent with task
claude --task "Description of what to do" \
       --handoff-in ./hand_off_documents/incoming/task.md \
       --handoff-out ./hand_off_documents/outgoing/result.md
```

<!-- section_id: "a7157e2d-2465-4a63-a3c7-0750df234f86" -->
### Using Task Tool for Delegation

```
Task tool parameters:
- subagent_type: "general-purpose" or specialized
- prompt: Clear task description
- Entry point context will load automatically
```

<!-- section_id: "07091925-8551-4d8d-9652-4bcd6ac581d2" -->
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

<!-- section_id: "c71cf2f8-2e55-40b8-b69c-7daaecb0fb14" -->
## Agent Coordination Patterns

<!-- section_id: "aa7bd504-d54c-475c-ae0b-066b8a31563b" -->
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

<!-- section_id: "fc0dc1a4-08f8-42c9-8718-e20ec4979dd5" -->
### Pattern 2: Chain (Sequential Delegation)

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│   YOU   │ ──▶ │ Agent A │ ──▶ │ Agent B │ ──▶ │ Agent C │
└─────────┘     └─────────┘     └─────────┘     └─────────┘

Use when: Each agent's output feeds the next
```

<!-- section_id: "eb471395-03f0-46f0-b626-fe8465652b58" -->
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

<!-- section_id: "0075a3fa-bffd-4076-b956-74ff7c6851c0" -->
## Scope Expansion Checklist

Before expanding your scope:

- [ ] Will adding this context keep me under 70% context usage?
- [ ] Do I have the domain knowledge for this area?
- [ ] Is the work tightly coupled with my current task?
- [ ] Are the critical rules similar/compatible?
- [ ] Can I complete this without losing track of my main task?

If all YES → Expand scope safely

---

<!-- section_id: "4287ab3f-3df7-4496-adac-e44e2bf33b0e" -->
## Delegation Checklist

Before delegating:

- [ ] Is the task clearly defined and self-contained?
- [ ] Have I written a clear handoff document?
- [ ] Is the target entry point appropriate for this task?
- [ ] Do I know where to receive the result?
- [ ] Can I continue other work while waiting?

If all YES → Delegate efficiently

---

<!-- section_id: "4c25125b-0006-4b94-a4b7-276d6521ce12" -->
## Examples

<!-- section_id: "ab28166b-ac28-47d0-98c7-88e50bea0f16" -->
### Example 1: Small Scope Expansion

```
Current: Working in layer_2_project/stage_06_development/

Need: Check a universal rule in layer_0

Decision: EXPAND SCOPE
- Reason: Quick lookup, minimal context addition
- Action: Read layer_0/.../sub_layer_0_04_rules/rule.md
- Continue with expanded knowledge
```

<!-- section_id: "19cb8111-73bc-4078-8a2b-e5319d4f8d79" -->
### Example 2: Delegation for Parallel Work

```
Current: Working in layer_2_project/

Need:
- Run tests in stage_07_testing/
- Update docs in stage_10_current_product/
- Fix linting in stage_09_fixing/

Decision: DELEGATE all three
- Reason: Independent tasks, can run in parallel
- Action: Spawn 3 agents at each stage entry point
- Collect results via handoff documents
```

<!-- section_id: "a8b3ccab-2cc2-4078-9dac-952e42e91a5c" -->
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

<!-- section_id: "67453f92-fc6c-402a-8524-61df5d8981c4" -->
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
