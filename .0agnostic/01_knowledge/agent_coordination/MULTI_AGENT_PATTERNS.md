---
resource_id: "bc8d6fe8-e0b2-42e7-ac43-102d10bd3cad"
resource_type: "knowledge"
resource_name: "MULTI_AGENT_PATTERNS"
---
# Multi-Agent Coordination Patterns

<!-- section_id: "ad7abee6-3385-4bd8-a33d-cc95a7484fe9" -->
## Overview

This document describes patterns for coordinating multiple AI agents working across layers, stages, and sub-layers. Choose the right pattern based on task structure, dependencies, and efficiency requirements.

---

<!-- section_id: "a397556f-e66f-4302-80bd-7ea9b6c4b403" -->
## Pattern Selection Guide

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PATTERN SELECTION FLOWCHART                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  What is the task structure?                                                │
│           │                                                                 │
│           ├──▶ Single task, single location ──▶ NO PATTERN (do it yourself)│
│           │                                                                 │
│           ├──▶ Multiple independent tasks ──▶ PARALLEL WORKERS             │
│           │                                                                 │
│           ├──▶ Sequential dependent tasks ──▶ PIPELINE                     │
│           │                                                                 │
│           ├──▶ One controller, many workers ──▶ HUB AND SPOKE              │
│           │                                                                 │
│           ├──▶ Complex with mixed dependencies ──▶ HIERARCHICAL             │
│           │                                                                 │
│           └──▶ Needs iteration/feedback ──▶ FEEDBACK LOOP                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "b1d38cd7-b660-46a2-8cd6-2f1d4ef0a5f6" -->
## Pattern 1: Parallel Workers

**When to use**: Multiple independent tasks that can run simultaneously.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARALLEL WORKERS PATTERN                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                      ┌─────────────┐                                        │
│                      │ COORDINATOR │                                        │
│                      │  (you)      │                                        │
│                      └──────┬──────┘                                        │
│                             │                                               │
│            ┌────────────────┼────────────────┐                              │
│            │ spawn          │ spawn          │ spawn                        │
│            ▼                ▼                ▼                              │
│      ┌──────────┐    ┌──────────┐    ┌──────────┐                          │
│      │ Worker A │    │ Worker B │    │ Worker C │                          │
│      │ (layer_1)│    │ (layer_2)│    │ (stage_7)│                          │
│      └────┬─────┘    └────┬─────┘    └────┬─────┘                          │
│           │               │               │                                 │
│           │ result        │ result        │ result                          │
│           └───────────────┼───────────────┘                                 │
│                           ▼                                                 │
│                      ┌─────────────┐                                        │
│                      │ COORDINATOR │                                        │
│                      │ (aggregate) │                                        │
│                      └─────────────┘                                        │
│                                                                             │
│  EFFICIENCY:                                                                │
│  ✓ Maximum parallelism                                                      │
│  ✓ No waiting between tasks                                                 │
│  ✗ All results must be collected before proceeding                         │
│                                                                             │
│  BEST FOR:                                                                  │
│  - Running tests across multiple modules                                    │
│  - Updating documentation in multiple locations                             │
│  - Parallel feature development                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "a0f4817c-d421-47ad-b4e6-9eb0ccc5c273" -->
### Implementation

```bash
# Coordinator spawns workers
cd /layer_1/feature_a/ && claude --task "Build feature A" &
cd /layer_1/feature_b/ && claude --task "Build feature B" &
cd /layer_1/feature_c/ && claude --task "Build feature C" &

# Wait for all to complete, then collect results
```

---

<!-- section_id: "bfe79a09-acaa-4760-b4f8-f6383c76c07e" -->
## Pattern 2: Pipeline

**When to use**: Sequential tasks where each depends on the previous.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PIPELINE PATTERN                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐              │
│  │ Stage 1 │ ──▶ │ Stage 2 │ ──▶ │ Stage 3 │ ──▶ │ Stage 4 │              │
│  │ (design)│     │ (build) │     │ (test)  │     │ (deploy)│              │
│  └─────────┘     └─────────┘     └─────────┘     └─────────┘              │
│       │               │               │               │                     │
│       ▼               ▼               ▼               ▼                     │
│   [design]        [code]          [results]      [deployed]                │
│   handoff         handoff         handoff        handoff                   │
│                                                                             │
│  FLOW:                                                                      │
│  1. Stage 1 agent completes, creates handoff for Stage 2                   │
│  2. Stage 2 agent receives, works, creates handoff for Stage 3             │
│  3. Continue until pipeline complete                                        │
│                                                                             │
│  EFFICIENCY:                                                                │
│  ✓ Clear progression and handoffs                                           │
│  ✓ Each stage has focused context                                           │
│  ✗ Sequential - no parallelism                                              │
│  ✗ Blocked if any stage fails                                               │
│                                                                             │
│  BEST FOR:                                                                  │
│  - Standard development workflow (design → build → test → deploy)          │
│  - Data processing pipelines                                                │
│  - Approval workflows                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "9e6bb1ba-97d0-40cf-b01e-21f977375a0d" -->
## Pattern 3: Hub and Spoke

**When to use**: Central coordinator needs results from multiple specialized agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HUB AND SPOKE PATTERN                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                           ┌─────────┐                                       │
│               ┌───────────│   HUB   │───────────┐                          │
│               │           │  (you)  │           │                          │
│               │           └────┬────┘           │                          │
│               │                │                │                          │
│               ▼                ▼                ▼                          │
│         ┌──────────┐    ┌──────────┐    ┌──────────┐                      │
│         │ Spoke A  │    │ Spoke B  │    │ Spoke C  │                      │
│         │(research)│    │ (impl)   │    │ (test)   │                      │
│         └────┬─────┘    └────┬─────┘    └────┬─────┘                      │
│              │               │               │                             │
│              └───────────────┼───────────────┘                             │
│                              │ all report back to hub                      │
│                              ▼                                              │
│                         ┌─────────┐                                        │
│                         │   HUB   │                                        │
│                         │(decides)│                                        │
│                         └─────────┘                                        │
│                                                                             │
│  THE HUB:                                                                   │
│  - Maintains overall context and goals                                      │
│  - Assigns tasks to spokes                                                  │
│  - Collects and integrates results                                          │
│  - Makes final decisions                                                    │
│                                                                             │
│  SPOKES:                                                                    │
│  - Specialized agents at specific entry points                              │
│  - Execute focused tasks                                                    │
│  - Report results back to hub                                               │
│                                                                             │
│  EFFICIENCY:                                                                │
│  ✓ Centralized coordination                                                 │
│  ✓ Specialized expertise per spoke                                          │
│  ✓ Hub maintains unified vision                                             │
│  ✗ Hub can become bottleneck                                                │
│                                                                             │
│  BEST FOR:                                                                  │
│  - Feature development needing multiple specialists                         │
│  - Research with parallel exploration                                       │
│  - Code review across multiple components                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "9928b936-abd7-4d90-9a70-22d784b34507" -->
## Pattern 4: Hierarchical

**When to use**: Complex tasks with nested sub-tasks at multiple levels.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HIERARCHICAL PATTERN                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                         ┌─────────────┐                                     │
│                         │   ROOT      │ (layer_0)                          │
│                         │ COORDINATOR │                                     │
│                         └──────┬──────┘                                     │
│                                │                                            │
│               ┌────────────────┼────────────────┐                          │
│               ▼                ▼                ▼                          │
│         ┌──────────┐    ┌──────────┐    ┌──────────┐                      │
│         │ Project A│    │ Project B│    │ Project C│ (layer_1)            │
│         │ COORD    │    │ COORD    │    │ COORD    │                      │
│         └────┬─────┘    └────┬─────┘    └────┬─────┘                      │
│              │               │               │                             │
│         ┌────┴────┐     ┌────┴────┐     ┌────┴────┐                       │
│         ▼         ▼     ▼         ▼     ▼         ▼                       │
│     ┌──────┐ ┌──────┐ ...                                                 │
│     │Feat 1│ │Feat 2│                              (layer_2)              │
│     │Worker│ │Worker│                                                      │
│     └──────┘ └──────┘                                                      │
│                                                                             │
│  STRUCTURE:                                                                 │
│  - Each level coordinates the level below                                   │
│  - Matches the layer hierarchy naturally                                    │
│  - Results bubble up, tasks flow down                                       │
│                                                                             │
│  COMMUNICATION:                                                             │
│  - DOWN: Tasks via hand_off_documents/outgoing/to_below/                   │
│  - UP: Results via hand_off_documents/outgoing/to_above/                   │
│                                                                             │
│  EFFICIENCY:                                                                │
│  ✓ Scales well for large projects                                           │
│  ✓ Natural decomposition of work                                            │
│  ✓ Each coordinator has focused scope                                       │
│  ✗ More communication overhead                                              │
│  ✗ Deeper hierarchy = more latency                                          │
│                                                                             │
│  BEST FOR:                                                                  │
│  - Large projects with many components                                      │
│  - Organizations with clear layer structure                                 │
│  - Work that maps naturally to layer hierarchy                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "819a760e-651d-402f-8f7e-7bcea79740bc" -->
## Pattern 5: Feedback Loop

**When to use**: Iterative tasks requiring review and revision.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FEEDBACK LOOP PATTERN                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│         ┌─────────────────────────────────────────────────────┐            │
│         │                                                     │            │
│         ▼                                                     │            │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │            │
│  │   CREATOR    │ ──▶│   REVIEWER   │ ──▶│   DECIDER    │────┘            │
│  │  (stage_06)  │    │  (stage_08)  │    │  (stage_09)  │                 │
│  └──────────────┘    └──────────────┘    └──────────────┘                 │
│         ▲                                        │                         │
│         │                                        │                         │
│         │         ┌──────────────┐               │                         │
│         └─────────│   REVISER    │◀──────────────┘                         │
│      (if needed)  │  (stage_09)  │  (feedback)                             │
│                   └──────────────┘                                         │
│                                                                             │
│  FLOW:                                                                      │
│  1. Creator produces initial work                                           │
│  2. Reviewer evaluates and provides feedback                                │
│  3. Decider determines: Accept or Revise                                    │
│  4. If Revise: Feedback goes to Creator/Reviser                            │
│  5. Loop until Accepted                                                     │
│                                                                             │
│  ROLES:                                                                     │
│  - Creator: Fresh perspective, may be different agent each iteration       │
│  - Reviewer: Consistent standards, same agent preferred                     │
│  - Decider: May be same as Reviewer or separate                            │
│  - Reviser: May be Creator or specialized agent                            │
│                                                                             │
│  EFFICIENCY:                                                                │
│  ✓ Quality assurance built-in                                               │
│  ✓ Catches issues early                                                     │
│  ✗ Multiple iterations increase time                                        │
│  ✗ Need clear acceptance criteria to avoid infinite loops                  │
│                                                                             │
│  BEST FOR:                                                                  │
│  - Code review workflows                                                    │
│  - Document review and approval                                             │
│  - Design iteration                                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "67b4f0b4-9c08-43dd-9ef8-b1be1fdaf7c7" -->
## Pattern 6: Map-Reduce

**When to use**: Same task on many items, then aggregate results.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MAP-REDUCE PATTERN                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                      ┌─────────────┐                                        │
│                      │ COORDINATOR │                                        │
│                      │ (splitter)  │                                        │
│                      └──────┬──────┘                                        │
│                             │ MAP                                           │
│         ┌───────────────────┼───────────────────┐                          │
│         │                   │                   │                          │
│         ▼                   ▼                   ▼                          │
│   ┌──────────┐        ┌──────────┐        ┌──────────┐                    │
│   │ Worker 1 │        │ Worker 2 │        │ Worker N │                    │
│   │(item 1-3)│        │(item 4-6)│        │(item ...)│                    │
│   └────┬─────┘        └────┬─────┘        └────┬─────┘                    │
│        │                   │                   │                          │
│        │ partial           │ partial           │ partial                   │
│        │ result            │ result            │ result                    │
│        │                   │                   │                          │
│        └───────────────────┼───────────────────┘                          │
│                            │ REDUCE                                        │
│                            ▼                                               │
│                      ┌─────────────┐                                       │
│                      │ COORDINATOR │                                       │
│                      │ (aggregator)│                                       │
│                      └─────────────┘                                       │
│                                                                             │
│  MAP PHASE:                                                                 │
│  - Split work into chunks                                                   │
│  - Each worker processes their chunk                                        │
│  - Workers run in parallel                                                  │
│                                                                             │
│  REDUCE PHASE:                                                              │
│  - Collect all partial results                                              │
│  - Aggregate into final result                                              │
│                                                                             │
│  BEST FOR:                                                                  │
│  - Processing many files                                                    │
│  - Batch operations across components                                       │
│  - Analysis tasks that can be parallelized                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "ca312348-0bb9-4d50-b3a5-f90e25058c26" -->
## Choosing the Right Pattern

| Task Characteristics | Recommended Pattern |
|---------------------|---------------------|
| Independent tasks, no ordering | Parallel Workers |
| Clear sequential steps | Pipeline |
| Need centralized control | Hub and Spoke |
| Complex nested structure | Hierarchical |
| Quality requires iteration | Feedback Loop |
| Same task on many items | Map-Reduce |

---

<!-- section_id: "5e3f2b79-0068-4896-a34a-59ccddd80031" -->
## Combining Patterns

Patterns can be combined for complex scenarios:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMBINED PATTERN EXAMPLE                                  │
│                    (Hub-Spoke + Pipeline + Feedback)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                         ┌─────────────┐                                     │
│                         │     HUB     │                                     │
│                         └──────┬──────┘                                     │
│                                │                                            │
│         ┌──────────────────────┼──────────────────────┐                    │
│         │ pipeline             │ parallel             │ pipeline           │
│         ▼                      ▼                      ▼                    │
│   ┌──────────┐          ┌──────────┐          ┌──────────┐               │
│   │ Research │          │  Build   │          │ Research │               │
│   └────┬─────┘          │ Workers  │          └────┬─────┘               │
│        │                └────┬─────┘               │                      │
│        ▼                     │                     ▼                      │
│   ┌──────────┐               │               ┌──────────┐               │
│   │  Design  │               │               │  Design  │               │
│   └────┬─────┘               │               └────┬─────┘               │
│        │                     │                    │                      │
│        └─────────────────────┼────────────────────┘                      │
│                              │                                            │
│                              ▼                                            │
│                         ┌─────────────┐                                   │
│                         │   REVIEW    │◀────┐ feedback                   │
│                         │   (hub)     │─────┘ loop                       │
│                         └─────────────┘                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "9b7a3753-a2e2-4f80-aa46-b62c59c5cd44" -->
## Anti-Patterns to Avoid

<!-- section_id: "57a1cdf8-9c89-432e-87e2-8e4e3762c4f8" -->
### 1. Over-Delegation
```
BAD: Delegating tiny tasks that are faster to do yourself
     Context switching overhead > task effort
```

<!-- section_id: "13737ad5-cf6d-4f77-846d-e194d5ba0b6f" -->
### 2. Under-Delegation
```
BAD: Doing everything yourself until context window explodes
     Should have delegated earlier
```

<!-- section_id: "a7188cd9-64d7-4a31-a4ec-cc71aca87ebc" -->
### 3. Circular Delegation
```
BAD: Agent A delegates to B, B delegates to C, C delegates to A
     No one does the actual work
```

<!-- section_id: "8ce5fc4e-c693-4242-bd07-ee6590b5bc92" -->
### 4. Lost Handoffs
```
BAD: Results go to wrong location, coordinator never receives them
     Always verify handoff paths
```

<!-- section_id: "d0dadc83-8adc-4f07-a684-31d4356f4a21" -->
### 5. Infinite Feedback
```
BAD: Feedback loop with no clear acceptance criteria
     Define exit conditions before starting
```

---

*See SCOPE_VS_DELEGATION.md for individual decision criteria*
*See HANDOFF_PROTOCOLS.md for communication details*
