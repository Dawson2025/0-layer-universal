# Common Agent Patterns

## Overview

AALang defines reusable patterns for structuring agents. Each pattern specifies a mode count, actor count, and typical use case. The two primary patterns used in our system are:

1. **4-mode-13-actor** — for focused, single-purpose agents
2. **5-mode-15-actor** — for orchestration and coordination agents

---

## Pattern 1: 4-mode-13-actor

**Used by**: GAB compiler, Context Loading Agent

### Structure

- **4 Modes**: Each with 2 mode actors (Senior + Junior persona pair) = 8 mode actors
- **5 State Actors**: Persist across all modes = 5 state actors
- **Total**: 8 + 5 = 13 actors

### GAB's 4 Modes

| Mode | Purpose | Senior | Junior |
|------|---------|--------|--------|
| Clarification | Understand requirements | Identifies gaps | Asks questions |
| Discussion | Explore design space | Evaluates options | Proposes approaches |
| Formalization | Create formal spec | Validates completeness | Writes spec |
| Generation | Produce output | Reviews quality | Generates JSON-LD |

### Context Loading Agent's 4 Modes

| Mode | Purpose | Threshold | Senior | Junior |
|------|---------|-----------|--------|--------|
| Loading | Find & parse CLAUDE.md files | 0.6 | Validates file discovery | Reads files |
| Validation | Identify layer/stage position | 0.8 | Confirms positioning | Extracts metadata |
| Propagation | Resolve inheritance & overrides | — | Validates override rules | Applies inheritance |
| Delivery | Confirm ready, persist state | — | Final validation | Persists to state file |

### When to Use This Pattern

- Agent has a **single, focused purpose**
- Work flows through **clear sequential phases**
- Each phase has **distinct entry/exit criteria**
- Agent operates **independently** (not coordinating other agents)

---

## Pattern 2: 5-mode-15-actor

**Used by**: Layer 0 Orchestrator, Project-level Orchestrators

### Structure

- **5 Modes**: Each with 2 mode actors (Senior + Junior) = 10 mode actors
- **5 State Actors**: Persist across all modes = 5 state actors
- **Total**: 10 + 5 = 15 actors

### Orchestrator's 5 Modes

| Mode | Purpose | Senior | Junior |
|------|---------|--------|--------|
| Receive | Parse incoming request | Validates request | Extracts task details |
| Delegation | Assign work to agents | Plans assignments | Creates task specs |
| Monitoring | Track agent progress | Evaluates progress | Checks status |
| Aggregation | Collect & merge results | Validates completeness | Merges outputs |
| Report | Deliver final result | Reviews quality | Formats report |

### When to Use This Pattern

- Agent **coordinates other agents** (orchestrator role)
- Work involves **delegation and monitoring**
- Results come from **multiple sources** that need aggregation
- Agent must **track child agent status**

---

## State Actors Across Patterns

### Standard 5 State Actors (Both Patterns)

| State Actor | 4-mode Use | 5-mode Use |
|-------------|-----------|-----------|
| Product/Context Name | What's being built | What request is being processed |
| Understanding Indicators | Task comprehension | Request comprehension |
| Satisfaction Indicators | Output quality | Delegation quality |
| Debug Mode | Debug logging control | Debug logging control |
| Decision Log | Design decisions | Coordination decisions |

### Pattern-Specific State Actors

The 5-mode orchestrator pattern often replaces or adds state actors:

| State Actor | Purpose |
|-------------|---------|
| `ChildRegistryStateActor` | Tracks spawned agents |
| `TaskStateActor` | Tracks delegated tasks |
| `ResourceBudgetStateActor` | Monitors resource consumption |
| `LayerStateActor` | Current position in layer hierarchy |

---

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

## Custom Patterns

GAB can produce agents with any number of modes and actors. The 4-mode and 5-mode patterns are common templates, but the system supports arbitrary configurations. When creating a new agent via GAB, the Discussion mode will explore which pattern best fits the requirements.

---

*Knowledge area: aalang_gab_system/agent_patterns*
*Last updated: 2026-02-07*
