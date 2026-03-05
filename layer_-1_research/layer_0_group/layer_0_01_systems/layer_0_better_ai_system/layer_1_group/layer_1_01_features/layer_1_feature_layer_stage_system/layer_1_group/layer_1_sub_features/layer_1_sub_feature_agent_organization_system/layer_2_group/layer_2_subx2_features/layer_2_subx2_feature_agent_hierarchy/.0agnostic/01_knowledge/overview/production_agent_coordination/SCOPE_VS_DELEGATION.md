---
resource_id: "b1a514d3-bc7c-471c-953e-3d3ecb431ddf"
resource_type: "knowledge"
resource_name: "SCOPE_VS_DELEGATION"
---
# Agent Scope vs Delegation Decisions

<!-- section_id: "d6cd54f6-7670-4c81-a2ff-87316c54f304" -->
## Overview

When an AI agent needs work done in other layers, stages, or sub-layers, it must decide:

1. **Expand Scope** - Do the work itself by loading additional context
2. **Delegate** - Spawn other agents at those entry points via CLI tools

This document provides decision criteria for making this choice efficiently.

---

<!-- section_id: "32c9ec6f-4623-4cc4-bbab-c60ceb1d7880" -->
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

<!-- section_id: "d2e415be-dd03-47c9-81c6-52075d744cd0" -->
## Decision Matrix

<!-- section_id: "b62fe02c-a4ca-46c7-9597-d442f4a8c7b2" -->
### When to EXPAND SCOPE (Work Yourself)

| Condition | Why Expand |
|-----------|------------|
| **Small task** in other layer/stage | Overhead of delegation > task effort |
| **Tightly coupled work** | Need continuous context between parts |
| **Sequential dependency** | Each step needs previous step's output |
| **Quick lookup** | Just reading a file or checking a rule |
| **Same domain knowledge** | Your current expertise applies |
| **1-2 additional layers** | Manageable context expansion |

<!-- section_id: "c6ad0c42-096e-4c4e-8230-60ee7cbce331" -->
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

<!-- section_id: "e8a106c4-6407-439a-b566-d3e21c84bdb3" -->
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

<!-- section_id: "91f3e6b3-e92c-4b0a-b9e8-7cd601dfdfe6" -->
## Efficiency Factors to Consider

<!-- section_id: "d6f52362-9aa8-4d0b-bf28-706c7ab3c5f9" -->
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

<!-- section_id: "d15ce9c7-2eac-4a94-aefb-d946ba1342ba" -->
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

<!-- section_id: "7d000858-6255-4f29-bd20-b1d2c190742b" -->
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

<!-- section_id: "6b0b3120-c301-48fd-a83c-6dcaf0c8bef9" -->
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

<!-- section_id: "8e7dc097-52e7-4751-9699-c450ed347d39" -->
## How to Delegate via CLI

<!-- section_id: "7250354a-cad8-4b9b-9c75-a4060f978145" -->
### Spawning an Agent at Another Entry Point

```bash
# Navigate to target entry point
cd /path/to/layer_N/entry_point/

# Spawn agent with task
claude --task "Description of what to do" \
       --handoff-in ./hand_off_documents/incoming/task.md \
       --handoff-out ./hand_off_documents/outgoing/result.md
```

<!-- section_id: "5e9d3c8b-5aea-4025-a2e6-d19baee3f7f5" -->
### Using Task Tool for Delegation

```
Task tool parameters:
- subagent_type: "general-purpose" or specialized
- prompt: Clear task description
- Entry point context will load automatically
```

<!-- section_id: "7a7adcb3-b431-44c6-aed3-e7072315486f" -->
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

<!-- section_id: "62a30761-9847-430a-9b3e-9b3d37579911" -->
## Agent Coordination Patterns

<!-- section_id: "c8a21d81-7b88-4d80-aeb2-e8ab47226caa" -->
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

<!-- section_id: "71c1fb6b-026d-4853-a966-6c770fafd3f3" -->
### Pattern 2: Chain (Sequential Delegation)

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│   YOU   │ ──▶ │ Agent A │ ──▶ │ Agent B │ ──▶ │ Agent C │
└─────────┘     └─────────┘     └─────────┘     └─────────┘

Use when: Each agent's output feeds the next
```

<!-- section_id: "e2f92527-daaf-4399-90ea-62c3791420c6" -->
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

<!-- section_id: "cadbff87-4d6f-454c-9504-60f0149f46b6" -->
## Scope Expansion Checklist

Before expanding your scope:

- [ ] Will adding this context keep me under 70% context usage?
- [ ] Do I have the domain knowledge for this area?
- [ ] Is the work tightly coupled with my current task?
- [ ] Are the critical rules similar/compatible?
- [ ] Can I complete this without losing track of my main task?

If all YES → Expand scope safely

---

<!-- section_id: "511dfb4a-bf51-4d16-9214-589ae91f48f2" -->
## Delegation Checklist

Before delegating:

- [ ] Is the task clearly defined and self-contained?
- [ ] Have I written a clear handoff document?
- [ ] Is the target entry point appropriate for this task?
- [ ] Do I know where to receive the result?
- [ ] Can I continue other work while waiting?

If all YES → Delegate efficiently

---

<!-- section_id: "b011d304-4d03-4c45-9e24-19ef60b52abc" -->
## Examples

<!-- section_id: "9f5339e5-3f95-4b9e-95cc-22698231e600" -->
### Example 1: Small Scope Expansion

```
Current: Working in layer_2_project/stage_06_development/

Need: Check a universal rule in layer_0

Decision: EXPAND SCOPE
- Reason: Quick lookup, minimal context addition
- Action: Read layer_0/.../sub_layer_0_04_rules/rule.md
- Continue with expanded knowledge
```

<!-- section_id: "8a27da14-640f-4071-8772-6e84823c6a0f" -->
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

<!-- section_id: "982db75d-5058-498e-b37b-24f83b04d66c" -->
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

<!-- section_id: "39426306-0884-41d8-a8e4-ed50060ce014" -->
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
