---
resource_id: "94b64730-beb9-4e7f-a9a4-0baf82756bc9"
resource_type: "knowledge"
resource_name: "mode_actor_pattern"
---
# Mode-Actor Pattern

## Overview

The Mode-Actor pattern is the core execution model in AALang. Every AALang agent is structured as a sequence of **modes**, each containing **actors** with **personas**, plus **state actors** that persist across all modes.

---

## Components

### Modes

Modes are sequential execution phases. An agent progresses through modes one at a time. Each mode has:

- **Purpose**: What this phase accomplishes
- **Entry Gate**: Conditions that must be true to enter (confidence thresholds)
- **Exit Gate**: Conditions that must be true to leave (satisfaction indicators)
- **Mode Actors**: The actors that execute within this mode
- **Isolated State**: Private state invisible to other modes

Transition between modes is governed by **confidence thresholds** — numeric values (0.0-1.0) that indicate readiness to proceed. This is semantic execution, not traditional control flow.

### Actors

Actors are the **core reasoning units** — the primary building blocks of AALang's n-mode-m-actor architecture:

- **All actors are stateful** — each maintains its own isolated context and state
- **Actors operate in modes** — they switch between behavioral modes with distinct constraints
- **Actors communicate via message passing** — structured messages between actors (same or different agents)
- **Actors are required** — every AALang agent must have at least one actor

### Personas (Optional Internal Reasoning Patterns)

Personas are **optional library patterns** that actors employ for internal deliberation:

- **Contained within actors** — not separate entities
- **Selectively employed** — actors choose when to use structured deliberation
- **Enable multi-perspective reasoning** — multiple personas within an actor can debate and reach consensus

> **Important practical note** (from professor's README): While personas are technically optional, in practice many implementations use a pattern where actors are stateful containers and personas provide actionable capabilities (responsibilities, messaging, session consistency). Actors without personas may be non-functional in this pattern.

Each mode typically uses two actors with a **Senior/Junior persona pair**:

| Role | Responsibility | Thinking Style |
|------|---------------|----------------|
| **Senior Persona** | Strategic thinking, validation, oversight | "Does this make sense? Is it complete? What's missing?" |
| **Junior Persona** | Execution, implementation, detailed work | "How do I build this? What are the specifics?" |

This dual-persona approach creates an internal review loop — the Junior executes, the Senior validates.

### Definition Adoption (Key Execution Model)

From the professor's `aalang-actor-execution-mechanics.md`:

> LLMs don't create separate actor instances — they **adopt definitions dynamically**. The LLM reads the actor definition and BECOMES that actor through definition adoption. There is no simulation layer.

This means:
- The JSON-LD definition is read as context-setting text
- The LLM's natural language comprehension interprets the structure
- State is maintained in the conversation context window
- **Semantic message filtering** replaces polling — the LLM attends to relevant state through natural language understanding

### State Actors

State actors persist across ALL modes. They maintain information that every mode needs access to:

| State Actor | Purpose |
|-------------|---------|
| `ProductNameStateActor` | Tracks what is being built (the product identity) |
| `UnderstandingIndicatorsStateActor` | Tracks comprehension of user requirements |
| `SatisfactionIndicatorsStateActor` | Tracks whether current output meets quality bars |
| `DebugModeStateActor` | Controls debug output (on/off, detail level) |
| `DecisionLogStateActor` | Records all decisions made (for audit trail) |

State actors have their own personas that define how they interpret and update their state.

### Personas

Every actor (mode or state) has a persona definition that includes:

- **Name**: Identity of the persona
- **Role**: What they do
- **Responsibilities**: Specific duties
- **Thinking patterns**: How they approach problems
- **Output format**: What they produce

---

## Mode Transition Mechanics

```
Mode 1                          Mode 2
┌─────────────────────┐        ┌─────────────────────┐
│                     │        │                     │
│  Senior validates   │        │  Senior validates   │
│  Junior executes    │        │  Junior executes    │
│                     │        │                     │
│  confidence >= 0.7  │───────►│  confidence >= 0.8  │───►...
│  (exit threshold)   │        │  (exit threshold)   │
│                     │        │                     │
└─────────────────────┘        └─────────────────────┘
         │                              │
         ▼                              ▼
┌─────────────────────────────────────────────────────┐
│  State Actors (accessible from ALL modes)           │
│  ProductName | Understanding | Satisfaction | Debug │
└─────────────────────────────────────────────────────┘
```

### Confidence Thresholds

Each mode defines a minimum confidence level to proceed. Confidence is calculated from multiple indicators:

- Understanding of the task
- Completeness of gathered information
- Quality of produced artifacts
- User satisfaction signals

If confidence is below threshold, the mode continues executing (loops) until sufficient confidence is reached.

### Satisfaction Indicators

Satisfaction indicators are distinct from confidence — they track whether the user/system is satisfied with what has been produced, not whether the agent understands the task. Both must be met for mode transition.

---

## Isolated State

Each mode has private state that is invisible to other modes. This prevents information leakage between phases and keeps each mode focused on its specific task.

Only state actors bridge across modes — everything else is mode-local.

---

## Message Passing

Communication in AALang happens at three levels:

### 1. Agent-to-Agent (P2P Gossip)
- Between separate agent instances
- Used for multi-agent orchestration
- Mediated through hand-off documents or message queues

### 2. Actor-to-Actor (Local Routing)
- Within a single agent, between actors in the same mode
- Senior ↔ Junior communication
- Mode actors ↔ State actors

### 3. Persona-to-Persona (Internal Reasoning)
- Within a single actor
- The Senior persona's internal deliberation
- The Junior persona's execution reasoning

---

## Execution in the LLM Context Window

AALang executes within the LLM's context window. This means:

- **State = messages**: All state is represented as messages in the conversation history
- **Semantic filtering replaces polling**: Instead of checking state repeatedly, the LLM attends to relevant state through semantic understanding
- **No external runtime**: No database, no server — everything lives in the context window
- **Conversation IS the program**: The structured conversation IS the executing program

This is fundamentally different from traditional programming where programs run on hardware. AALang programs run on attention mechanisms.

---

*Knowledge area: aalang_gab_system/mode_actor_pattern*
*Last updated: 2026-02-07*
