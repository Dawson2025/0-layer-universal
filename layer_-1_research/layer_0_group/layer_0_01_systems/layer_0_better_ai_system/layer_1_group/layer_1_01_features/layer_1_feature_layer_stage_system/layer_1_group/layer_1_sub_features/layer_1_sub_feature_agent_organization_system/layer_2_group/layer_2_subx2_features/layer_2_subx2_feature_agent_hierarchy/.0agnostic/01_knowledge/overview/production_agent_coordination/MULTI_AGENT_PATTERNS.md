---
resource_id: "f3f45a8c-a89d-4603-b64c-9c60f8dfd90a"
resource_type: "knowledge"
resource_name: "MULTI_AGENT_PATTERNS"
---
# Multi-Agent Coordination Patterns

<!-- section_id: "a14d3b63-14cf-446b-914b-4b49361c33ca" -->
## Overview

This document describes patterns for coordinating multiple AI agents working across layers, stages, and sub-layers. Choose the right pattern based on task structure, dependencies, and efficiency requirements.

---

<!-- section_id: "f058ec1e-16be-4ad7-8e44-9ef7388f0612" -->
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

<!-- section_id: "4a7575e6-3638-419b-8d7f-6815793f58db" -->
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

<!-- section_id: "789ecbc5-d835-4374-b94d-5a539844faba" -->
### Implementation

```bash
# Coordinator spawns workers
cd /layer_1/feature_a/ && claude --task "Build feature A" &
cd /layer_1/feature_b/ && claude --task "Build feature B" &
cd /layer_1/feature_c/ && claude --task "Build feature C" &

# Wait for all to complete, then collect results
```

---

<!-- section_id: "42bb076c-a208-49eb-bc4a-9fecde9fc5b5" -->
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

<!-- section_id: "98112fa9-f764-4ce3-94bb-5b810cc56557" -->
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

<!-- section_id: "7f4635f4-91de-49d2-b427-c7ea4c81506c" -->
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

<!-- section_id: "d609b03e-723c-4dcc-b81e-165ca176b655" -->
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

<!-- section_id: "aa7437a8-d1f6-4fe9-beec-57eff8aab180" -->
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

<!-- section_id: "059779f7-a05e-4a98-8eaa-dbc9f1ec8e0a" -->
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

<!-- section_id: "d5a5de0f-55ae-4dbc-8dab-d32d8ee2dc81" -->
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

<!-- section_id: "ba5ae9bd-9c39-4e25-9247-134d6d22fed6" -->
## Anti-Patterns to Avoid

<!-- section_id: "8b7fa664-4438-44c7-bad8-15ba62dcc6a7" -->
### 1. Over-Delegation
```
BAD: Delegating tiny tasks that are faster to do yourself
     Context switching overhead > task effort
```

<!-- section_id: "b17986c6-8011-4668-8b89-564f9a443335" -->
### 2. Under-Delegation
```
BAD: Doing everything yourself until context window explodes
     Should have delegated earlier
```

<!-- section_id: "a04a35e4-ba04-49c5-a58f-dbd77dea8386" -->
### 3. Circular Delegation
```
BAD: Agent A delegates to B, B delegates to C, C delegates to A
     No one does the actual work
```

<!-- section_id: "c32bae6e-ebf9-4694-be7c-890a7277f0fb" -->
### 4. Lost Handoffs
```
BAD: Results go to wrong location, coordinator never receives them
     Always verify handoff paths
```

<!-- section_id: "0f9d1eaa-9dfa-4cb4-8bc4-227cf2cb536a" -->
### 5. Infinite Feedback
```
BAD: Feedback loop with no clear acceptance criteria
     Define exit conditions before starting
```

---

*See SCOPE_VS_DELEGATION.md for individual decision criteria*
*See HANDOFF_PROTOCOLS.md for communication details*
