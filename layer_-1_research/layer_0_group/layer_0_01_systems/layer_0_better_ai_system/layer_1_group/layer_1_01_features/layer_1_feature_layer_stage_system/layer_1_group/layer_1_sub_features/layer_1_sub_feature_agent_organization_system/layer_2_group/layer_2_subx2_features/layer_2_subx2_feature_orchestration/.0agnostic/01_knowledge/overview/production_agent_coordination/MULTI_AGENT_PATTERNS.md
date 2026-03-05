---
resource_id: "d466ec37-5f9a-4e76-be38-b28a69da8b77"
resource_type: "knowledge"
resource_name: "MULTI_AGENT_PATTERNS"
---
# Multi-Agent Coordination Patterns

<!-- section_id: "1e94ffc0-8f90-4410-9167-868aa91de5a1" -->
## Overview

This document describes patterns for coordinating multiple AI agents working across layers, stages, and sub-layers. Choose the right pattern based on task structure, dependencies, and efficiency requirements.

---

<!-- section_id: "1f178e5c-48f2-4253-bd52-6ca8a85196f0" -->
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

<!-- section_id: "f2d335b3-d65a-4b9b-9e82-748b8067e760" -->
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

<!-- section_id: "f5566e47-81db-4d80-b1ff-39c6b18c3025" -->
### Implementation

```bash
# Coordinator spawns workers
cd /layer_1/feature_a/ && claude --task "Build feature A" &
cd /layer_1/feature_b/ && claude --task "Build feature B" &
cd /layer_1/feature_c/ && claude --task "Build feature C" &

# Wait for all to complete, then collect results
```

---

<!-- section_id: "f030796e-c3e6-47b4-a66e-d6a423c96c3e" -->
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

<!-- section_id: "c3ba15e8-e257-49e1-8a1f-54aeb8836c47" -->
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

<!-- section_id: "cdac624a-72a5-4651-b3ad-fc81e90c82ab" -->
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

<!-- section_id: "e6c93d36-bd78-417e-98f4-ac1981a53bbe" -->
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

<!-- section_id: "fce53c52-591c-49bf-85d9-70f496a889de" -->
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

<!-- section_id: "633bd1c6-10d3-46f5-b60b-81f562d18e33" -->
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

<!-- section_id: "706f340f-c8ca-478e-bc5e-40f7052329d9" -->
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

<!-- section_id: "398cbcab-9788-4162-b2fb-4f8f53f5e4b7" -->
## Anti-Patterns to Avoid

<!-- section_id: "02ab9027-d1c7-4dc2-8592-8b2bc86af8f4" -->
### 1. Over-Delegation
```
BAD: Delegating tiny tasks that are faster to do yourself
     Context switching overhead > task effort
```

<!-- section_id: "4d57571c-f147-4396-851f-4fc813e57175" -->
### 2. Under-Delegation
```
BAD: Doing everything yourself until context window explodes
     Should have delegated earlier
```

<!-- section_id: "1ba83630-a70c-4242-9b36-19b1508008cc" -->
### 3. Circular Delegation
```
BAD: Agent A delegates to B, B delegates to C, C delegates to A
     No one does the actual work
```

<!-- section_id: "5a89fca4-762f-4a87-9d4f-10fd4324ffcf" -->
### 4. Lost Handoffs
```
BAD: Results go to wrong location, coordinator never receives them
     Always verify handoff paths
```

<!-- section_id: "e411c3e1-3f8e-41f8-b70a-46979143a22b" -->
### 5. Infinite Feedback
```
BAD: Feedback loop with no clear acceptance criteria
     Define exit conditions before starting
```

---

*See SCOPE_VS_DELEGATION.md for individual decision criteria*
*See HANDOFF_PROTOCOLS.md for communication details*
