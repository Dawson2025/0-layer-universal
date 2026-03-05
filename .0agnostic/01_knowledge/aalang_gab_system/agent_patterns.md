---
resource_id: "e6c8d6f4-ffa1-4145-85e4-52260351478c"
resource_type: "knowledge"
resource_name: "agent_patterns"
---
# Common Agent Patterns

<!-- section_id: "6a084f7c-262d-42c4-b308-84849bcce464" -->
## Overview

AALang defines reusable patterns for structuring agents. Each pattern specifies a mode count, actor count, and typical use case. The two primary patterns used in our system are:

1. **4-mode-13-actor** — for focused, single-purpose agents
2. **5-mode-15-actor** — for orchestration and coordination agents

---

<!-- section_id: "fb68c6ef-961d-4d8c-b79c-7492ab213b7a" -->
## Pattern 1: 4-mode-13-actor

**Used by**: GAB compiler, Context Loading Agent

<!-- section_id: "248b328d-7502-48cd-8093-2fc0d09e4e6e" -->
### Structure

- **4 Modes**: Each with 2 mode actors (Senior + Junior persona pair) = 8 mode actors
- **5 State Actors**: Persist across all modes = 5 state actors
- **Total**: 8 + 5 = 13 actors

<!-- section_id: "aaccc46a-9923-4993-8f52-c3771f9d2a5d" -->
### GAB's 4 Modes

| Mode | Purpose | Senior | Junior |
|------|---------|--------|--------|
| Clarification | Understand requirements | Identifies gaps | Asks questions |
| Discussion | Explore design space | Evaluates options | Proposes approaches |
| Formalization | Create formal spec | Validates completeness | Writes spec |
| Generation | Produce output | Reviews quality | Generates JSON-LD |

<!-- section_id: "5a4e03e9-3333-4650-8b97-f4f4762f306d" -->
### Context Loading Agent's 4 Modes

| Mode | Purpose | Threshold | Senior | Junior |
|------|---------|-----------|--------|--------|
| Loading | Find & parse CLAUDE.md files | 0.6 | Validates file discovery | Reads files |
| Validation | Identify layer/stage position | 0.8 | Confirms positioning | Extracts metadata |
| Propagation | Resolve inheritance & overrides | — | Validates override rules | Applies inheritance |
| Delivery | Confirm ready, persist state | — | Final validation | Persists to state file |

<!-- section_id: "2736eba6-3e34-4af4-a497-b828d49073f3" -->
### When to Use This Pattern

- Agent has a **single, focused purpose**
- Work flows through **clear sequential phases**
- Each phase has **distinct entry/exit criteria**
- Agent operates **independently** (not coordinating other agents)

---

<!-- section_id: "185cca9f-4581-48c7-ae0e-249ad201945b" -->
## Pattern 2: 5-mode-15-actor

**Used by**: Layer 0 Orchestrator, Project-level Orchestrators

<!-- section_id: "0fe74b78-381d-40ab-ac56-11ef91552854" -->
### Structure

- **5 Modes**: Each with 2 mode actors (Senior + Junior) = 10 mode actors
- **5 State Actors**: Persist across all modes = 5 state actors
- **Total**: 10 + 5 = 15 actors

<!-- section_id: "83933160-d70e-4268-8614-2c26dd049bb0" -->
### Orchestrator's 5 Modes

| Mode | Purpose | Senior | Junior |
|------|---------|--------|--------|
| Receive | Parse incoming request | Validates request | Extracts task details |
| Delegation | Assign work to agents | Plans assignments | Creates task specs |
| Monitoring | Track agent progress | Evaluates progress | Checks status |
| Aggregation | Collect & merge results | Validates completeness | Merges outputs |
| Report | Deliver final result | Reviews quality | Formats report |

<!-- section_id: "f071118f-60f7-48d5-a4ab-e6e233d3b454" -->
### When to Use This Pattern

- Agent **coordinates other agents** (orchestrator role)
- Work involves **delegation and monitoring**
- Results come from **multiple sources** that need aggregation
- Agent must **track child agent status**

---

<!-- section_id: "69f5becf-0021-4fbf-ade8-a3e6f7087425" -->
## State Actors Across Patterns

<!-- section_id: "5de51e8b-78fa-49d6-8056-f802686ae4bd" -->
### Standard 5 State Actors (Both Patterns)

| State Actor | 4-mode Use | 5-mode Use |
|-------------|-----------|-----------|
| Product/Context Name | What's being built | What request is being processed |
| Understanding Indicators | Task comprehension | Request comprehension |
| Satisfaction Indicators | Output quality | Delegation quality |
| Debug Mode | Debug logging control | Debug logging control |
| Decision Log | Design decisions | Coordination decisions |

<!-- section_id: "e27b8854-2c5d-45b7-9165-384e4fe6b64c" -->
### Pattern-Specific State Actors

The 5-mode orchestrator pattern often replaces or adds state actors:

| State Actor | Purpose |
|-------------|---------|
| `ChildRegistryStateActor` | Tracks spawned agents |
| `TaskStateActor` | Tracks delegated tasks |
| `ResourceBudgetStateActor` | Monitors resource consumption |
| `LayerStateActor` | Current position in layer hierarchy |

---

<!-- section_id: "428bdfa2-dc61-4743-8579-a08f409b74e2" -->
## Inheritance Between Patterns

Project-level orchestrators **inherit** from the layer 0 orchestrator using `"extends"`:

```
Layer 0 Orchestrator (universal)
├── Defines the 5-mode-15-actor template
├── Standard state actors
├── Universal safeguards (max recursion, circuit breaker)
│
└── Project Orchestrator (inherits)
    ├── Uses "extends": "layer_0_orchestrator" for each mode
    ├── Adds project-specific context (ProjectContextStateActor)
    ├── Scopes operations to project boundaries
    └── Escalates cross-project work to parent
```

This means project-level orchestrators get all the universal behavior (safeguards, patterns, communication) while adding project-specific context and constraints.

---

<!-- section_id: "ae867311-8413-41e5-83e4-f21c374491ab" -->
## Safeguards in Orchestrator Patterns

The 5-mode orchestrator includes built-in safeguards:

| Safeguard | Limit | Purpose |
|-----------|-------|---------|
| Max recursion depth | 5 | Prevents infinite delegation chains |
| No identical re-delegation | — | Prevents stuck loops |
| Max concurrent agents | 3 | Prevents resource exhaustion |
| Circuit breaker | 3 failures | Trips breaker per agent type after 3 consecutive failures |
| Must use hand_off_documents | — | All communication through file-based IPC |

---

<!-- section_id: "69f95d24-8f65-4c7b-9df2-a049459d5df7" -->
## Choosing a Pattern

```
Is the agent coordinating other agents?
├── YES → 5-mode-15-actor (orchestrator pattern)
└── NO → Continue

Does it have a clear linear pipeline?
├── YES → 4-mode-13-actor (pipeline pattern)
└── NO → Continue

Is it something else entirely?
└── Use GAB to design a custom pattern
    (GAB can produce any mode/actor count)
```

---

<!-- section_id: "75d4cc72-e4fb-4848-afc2-1b278d1b3aef" -->
## Custom Patterns

GAB can produce agents with any number of modes and actors. The 4-mode and 5-mode patterns are common templates, but the system supports arbitrary configurations. When creating a new agent via GAB, the Discussion mode will explore which pattern best fits the requirements.

---

*Knowledge area: aalang_gab_system/agent_patterns*
*Last updated: 2026-02-07*
