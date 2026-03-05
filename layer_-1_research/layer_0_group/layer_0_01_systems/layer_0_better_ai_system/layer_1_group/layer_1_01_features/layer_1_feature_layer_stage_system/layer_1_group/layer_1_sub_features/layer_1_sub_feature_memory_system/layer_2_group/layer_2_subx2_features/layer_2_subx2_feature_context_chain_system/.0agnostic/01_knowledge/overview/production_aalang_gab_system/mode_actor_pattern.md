---
resource_id: "94b64730-beb9-4e7f-a9a4-0baf82756bc9"
resource_type: "knowledge"
resource_name: "mode_actor_pattern"
---
# Mode-Actor Pattern

<!-- section_id: "1c230318-0d94-4ec3-a072-2e9109b3ce35" -->
## Overview

The Mode-Actor pattern is the core execution model in AALang. Every AALang agent is structured as a sequence of **modes**, each containing **actors** with **personas**, plus **state actors** that persist across all modes.

---

<!-- section_id: "e9a014df-f1d7-42fd-beb4-cc1d288dc050" -->
## Components

<!-- section_id: "981a56ab-7dcd-4461-8ac7-707029baeb5d" -->
### Modes

Modes are sequential execution phases. An agent progresses through modes one at a time. Each mode has:

- **Purpose**: What this phase accomplishes
- **Entry Gate**: Conditions that must be true to enter (confidence thresholds)
- **Exit Gate**: Conditions that must be true to leave (satisfaction indicators)
- **Mode Actors**: The actors that execute within this mode
- **Isolated State**: Private state invisible to other modes

Transition between modes is governed by **confidence thresholds** — numeric values (0.0-1.0) that indicate readiness to proceed. This is semantic execution, not traditional control flow.

<!-- section_id: "55596fb2-653b-491e-a9fc-c3660ede25b8" -->
### Actors

Actors are the **core reasoning units** — the primary building blocks of AALang's n-mode-m-actor architecture:

- **All actors are stateful** — each maintains its own isolated context and state
- **Actors operate in modes** — they switch between behavioral modes with distinct constraints
- **Actors communicate via message passing** — structured messages between actors (same or different agents)
- **Actors are required** — every AALang agent must have at least one actor

<!-- section_id: "e19f12ed-a79d-4139-9520-0fe5a23750b5" -->
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

<!-- section_id: "2ebadcf5-79f4-47c1-9f30-78bb52235265" -->
### Definition Adoption (Key Execution Model)

From the professor's `aalang-actor-execution-mechanics.md`:

> LLMs don't create separate actor instances — they **adopt definitions dynamically**. The LLM reads the actor definition and BECOMES that actor through definition adoption. There is no simulation layer.

This means:
- The JSON-LD definition is read as context-setting text
- The LLM's natural language comprehension interprets the structure
- State is maintained in the conversation context window
- **Semantic message filtering** replaces polling — the LLM attends to relevant state through natural language understanding

<!-- section_id: "1d6dfa2c-9377-4beb-866b-ca7c6387932d" -->
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

<!-- section_id: "7c83e0e4-3799-4a49-8994-b4669fa2d437" -->
### Personas

Every actor (mode or state) has a persona definition that includes:

- **Name**: Identity of the persona
- **Role**: What they do
- **Responsibilities**: Specific duties
- **Thinking patterns**: How they approach problems
- **Output format**: What they produce

---

<!-- section_id: "d7d112af-e8da-4aef-a223-93cd241a47bb" -->
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

<!-- section_id: "405e7f73-30f6-41fa-a23e-1c397ff51413" -->
### Confidence Thresholds

Each mode defines a minimum confidence level to proceed. Confidence is calculated from multiple indicators:

- Understanding of the task
- Completeness of gathered information
- Quality of produced artifacts
- User satisfaction signals

If confidence is below threshold, the mode continues executing (loops) until sufficient confidence is reached.

<!-- section_id: "626415f8-cd61-4250-be69-d1abe14c29f1" -->
### Satisfaction Indicators

Satisfaction indicators are distinct from confidence — they track whether the user/system is satisfied with what has been produced, not whether the agent understands the task. Both must be met for mode transition.

---

<!-- section_id: "04cd6b42-e69c-463c-85f4-c54ad017a0a6" -->
## Isolated State

Each mode has private state that is invisible to other modes. This prevents information leakage between phases and keeps each mode focused on its specific task.

Only state actors bridge across modes — everything else is mode-local.

---

<!-- section_id: "c8ec3a56-2487-44a3-b96f-c49b520225c2" -->
## Message Passing

Communication in AALang happens at three levels:

<!-- section_id: "ee5b4316-35db-49c8-823c-d5dabcca993b" -->
### 1. Agent-to-Agent (P2P Gossip)
- Between separate agent instances
- Used for multi-agent orchestration
- Mediated through hand-off documents or message queues

<!-- section_id: "6b4e6b13-17cd-4ff7-be37-cda7152b081b" -->
### 2. Actor-to-Actor (Local Routing)
- Within a single agent, between actors in the same mode
- Senior ↔ Junior communication
- Mode actors ↔ State actors

<!-- section_id: "20d16ea1-32d9-4f2c-9c3f-e2c76692c524" -->
### 3. Persona-to-Persona (Internal Reasoning)
- Within a single actor
- The Senior persona's internal deliberation
- The Junior persona's execution reasoning

---

<!-- section_id: "565e539a-c153-4c54-a547-5122e955ea9b" -->
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
