# Agent Scope vs Delegation Decisions

## Overview

When an AI agent needs work done in other layers, stages, or sub-layers, it must decide:

1. **Expand Scope** - Do the work itself by loading additional context
2. **Delegate** - Spawn other agents at those entry points via CLI tools

This document provides decision criteria for making this choice efficiently.

---

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

## Decision Matrix

### When to EXPAND SCOPE (Work Yourself)

| Condition | Why Expand |
|-----------|------------|
| **Small task** in other layer/stage | Overhead of delegation > task effort |
| **Tightly coupled work** | Need continuous context between parts |
| **Sequential dependency** | Each step needs previous step's output |
| **Quick lookup** | Just reading a file or checking a rule |
| **Same domain knowledge** | Your current expertise applies |
| **1-2 additional layers** | Manageable context expansion |

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

## Efficiency Factors to Consider

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

## How to Delegate via CLI

### Spawning an Agent at Another Entry Point

```bash
# Navigate to target entry point
cd /path/to/layer_N/entry_point/

# Spawn agent with task
claude --task "Description of what to do" \
       --handoff-in ./hand_off_documents/incoming/task.md \
       --handoff-out ./hand_off_documents/outgoing/result.md
```

### Using Task Tool for Delegation

```
Task tool parameters:
- subagent_type: "general-purpose" or specialized
- prompt: Clear task description
- Entry point context will load automatically
```

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

## Agent Coordination Patterns

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

### Pattern 2: Chain (Sequential Delegation)

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│   YOU   │ ──▶ │ Agent A │ ──▶ │ Agent B │ ──▶ │ Agent C │
└─────────┘     └─────────┘     └─────────┘     └─────────┘

Use when: Each agent's output feeds the next
```

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

## Scope Expansion Checklist

Before expanding your scope:

- [ ] Will adding this context keep me under 70% context usage?
- [ ] Do I have the domain knowledge for this area?
- [ ] Is the work tightly coupled with my current task?
- [ ] Are the critical rules similar/compatible?
- [ ] Can I complete this without losing track of my main task?

If all YES → Expand scope safely

---

## Delegation Checklist

Before delegating:

- [ ] Is the task clearly defined and self-contained?
- [ ] Have I written a clear handoff document?
- [ ] Is the target entry point appropriate for this task?
- [ ] Do I know where to receive the result?
- [ ] Can I continue other work while waiting?

If all YES → Delegate efficiently

---

## Examples

### Example 1: Small Scope Expansion

```
Current: Working in layer_1_project/stage_06_development/

Need: Check a universal rule in layer_0

Decision: EXPAND SCOPE
- Reason: Quick lookup, minimal context addition
- Action: Read layer_0/.../sub_layer_0_04_rules/rule.md
- Continue with expanded knowledge
```

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
