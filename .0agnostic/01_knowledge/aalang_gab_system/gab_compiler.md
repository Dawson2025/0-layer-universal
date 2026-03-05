---
resource_id: "84ab93ab-e8b4-41a7-b05b-0594e9057409"
resource_type: "knowledge"
resource_name: "gab_compiler"
---
# GAB Compiler — How It Works

<!-- section_id: "dcb9be6a-3841-4983-b4eb-4353916af9d0" -->
## Overview

GAB (Generic AALang Builder) is the "compiler" for AALang. It takes natural language descriptions of desired agent behavior and produces structured AALang agent definitions in JSON-LD format.

GAB itself is an AALang agent — a **4-mode-13-actor** agent that follows the Mode-Actor pattern it produces.

**Source**: `layer_0/layer_0_01_ai_manager_system/professor/gab.jsonld`

---

<!-- section_id: "51f888e9-c1d9-4dc9-a0b1-207cf221420d" -->
## The 4-Mode Pipeline

GAB processes agent creation through four sequential modes:

```
User's natural language description
         │
         ▼
┌─────────────────────────┐
│  MODE 1: Clarification  │  "What exactly do you want?"
│  Threshold: 0.7         │
│  Senior: ClarifyBot     │  Strategic: identifies gaps in understanding
│  Junior: QuestionBot    │  Execution: asks specific clarifying questions
└────────────┬────────────┘
             │ confidence >= 0.7
             ▼
┌─────────────────────────┐
│  MODE 2: Discussion     │  "Let's explore the design space"
│  Threshold: 0.8         │
│  Senior: DesignBot      │  Strategic: evaluates design options
│  Junior: ExploreBot     │  Execution: proposes concrete approaches
└────────────┬────────────┘
             │ confidence >= 0.8
             ▼
┌─────────────────────────┐
│  MODE 3: Formalization  │  "Here's the formal specification"
│  Threshold: 0.9         │
│  Senior: SpecBot        │  Strategic: validates completeness
│  Junior: FormalizerBot  │  Execution: writes formal spec
└────────────┬────────────┘
             │ confidence >= 0.9
             ▼
┌─────────────────────────┐
│  MODE 4: Generation     │  "Producing the AALang output"
│  MANDATORY (no skip)    │
│  Senior: QualityBot     │  Strategic: reviews output quality
│  Junior: GeneratorBot   │  Execution: produces JSON-LD
└─────────────────────────┘
         │
         ▼
   AALang agent definition (JSON-LD)
```

---

<!-- section_id: "5a10a774-7e89-4684-a038-83ebc39f0276" -->
## Mode Details

<!-- section_id: "a1624e19-b372-4b0e-a716-cce3549d2a2c" -->
### Mode 1: Clarification

**Purpose**: Understand what the user wants to build.

The Clarification mode asks targeted questions to fill gaps in the user's description. The Senior persona (ClarifyBot) identifies what information is missing, while the Junior persona (QuestionBot) formulates and asks the questions.

**Exit condition**: Confidence >= 0.7 that the requirements are understood.

**Key behaviors**:
- Asks about the agent's purpose, users, constraints
- Identifies ambiguities in the description
- Does NOT propose solutions yet — purely requirements gathering

<!-- section_id: "3a28fc7d-f330-4e83-a08a-ea4d4646861a" -->
### Mode 2: Discussion

**Purpose**: Explore design options and converge on an approach.

The Discussion mode explores how to structure the agent. The Senior persona (DesignBot) evaluates trade-offs, while the Junior persona (ExploreBot) proposes concrete options.

**Exit condition**: Confidence >= 0.8 that the design approach is solid.

**Key behaviors**:
- Proposes mode structures (how many modes, what each does)
- Discusses actor/persona assignments
- Identifies state that needs to persist across modes
- Converges on a pattern (4-mode, 5-mode, custom)

<!-- section_id: "46723723-b86f-4eca-ae7e-e6d07c497c1e" -->
### Mode 3: Formalization

**Purpose**: Create a precise formal specification before generating code.

The Formalization mode writes out the complete specification. The Senior persona (SpecBot) validates completeness, while the Junior persona (FormalizerBot) writes the formal spec.

**Exit condition**: Confidence >= 0.9 that the spec is complete and correct.

**Key behaviors**:
- Defines every mode, actor, persona, state actor
- Specifies transition conditions and thresholds
- Documents message interfaces
- Creates work artifact definitions

<!-- section_id: "8e6325cf-f79b-46ae-9541-b4ed5c83af09" -->
### Mode 4: Generation (MANDATORY)

**Purpose**: Produce the final AALang agent definition in JSON-LD.

This mode is **mandatory** — it cannot be skipped even if the user seems satisfied with the spec. The Senior persona (QualityBot) reviews the output against the specification, while the Junior persona (GeneratorBot) produces the JSON-LD.

**Key behaviors**:
- Generates valid JSON-LD structure
- Follows AALang grammar and semantics from the language specification
- Includes all required fields (modes, actors, personas, state, messages)
- Runs quality checklist before finalizing

---

<!-- section_id: "9cb4d887-e5e8-4920-890b-fb7b16c1edf1" -->
## State Actors (Persist Across All 4 Modes)

| State Actor | Tracks |
|-------------|--------|
| `ProductNameStateActor` | The name of the agent being created |
| `UnderstandingIndicatorsStateActor` | How well the requirements are understood |
| `SatisfactionIndicatorsStateActor` | Quality metrics for the generated output |
| `DebugModeStateActor` | Whether debug logging is on (controlled by user) |
| `DecisionLogStateActor` | All design decisions made during the process |

---

<!-- section_id: "3701d8e5-4023-4957-a3a8-baa2618a0136" -->
## Built-in Protocols

GAB includes several protocols that govern execution:

<!-- section_id: "fa1fd9ec-623a-4d58-acaa-12db386ecea4" -->
### Clarification Protocol
- How to ask questions effectively
- When to stop asking and move forward
- How to handle contradictory requirements

<!-- section_id: "294c49da-4f1b-4d50-9c80-513fc9064dd4" -->
### Debug Protocol
- User can toggle debug mode on/off
- When on: shows internal reasoning, decision rationale, state transitions
- When off: clean user-facing output only

<!-- section_id: "037701c1-89a8-4f8a-be2b-6ad00b837224" -->
### NonAALang Detection Protocol
- If the user asks for something that ISN'T an AALang agent
- GAB recognizes this and redirects appropriately
- Prevents misuse of the compiler for non-agent tasks

<!-- section_id: "e9d4eaae-4e9c-4c36-8875-d3a57f8d2e6a" -->
### Quality Checklist
- Run before finalizing Generation mode output
- Validates completeness of the produced agent definition
- Ensures all required JSON-LD fields are present

---

<!-- section_id: "66b4bae4-46e2-47b2-a76d-4186ee62698a" -->
## User's Role

In GAB's model, the user is the "Team Lead":
- GAB asks questions; the user answers
- GAB proposes options; the user decides
- The user can toggle debug mode, request changes, redirect
- GAB cannot proceed past certain gates without user input

---

<!-- section_id: "d900e98a-93cc-4849-965e-ab9caa36b4e8" -->
## Output Format

GAB produces a `.gab.jsonld` file containing:

```
{
  "@context": { ... },
  "@type": "AALangAgent",
  "name": "AgentName",
  "pattern": "N-mode-M-actor",
  "executionInstructions": { ... },
  "modes": [ ... ],
  "stateActors": [ ... ],
  "messageInterface": { ... },
  "protocols": [ ... ]
}
```

The output is a complete, self-contained agent definition that can be loaded into an LLM context window for execution.

---

<!-- section_id: "4d522fa2-fd1b-4760-975d-3043461c65ee" -->
## Development Workflow (Post-Generation)

After GAB generates the initial product, there's a structured refinement cycle (from `gab-development-workflow.md`):

```
GAB 4-Mode Workflow (creates initial product)
         │
         ▼
    Load Actors
         │
         ▼
    Self-Check Actors ◄──────────┐
    (each reports issues)        │
         │                       │
         ▼                       │
    Unload Actors                │
         │                       │
    Issues found? ───Yes────► Modify using GAB
         │
         No
         │
         ▼
    All-But-Actors Self-Check
    (modes, protocols, files)
         │
    Issues found? ───Yes────► Modify using GAB → (back to Load Actors)
         │
         No (zero issues)
         │
         ▼
    System-Level Test
         │
    Stable? ───No────► Modify using GAB → (back to Load Actors)
         │
        Yes
         │
         ▼
    Product Ready
```

<!-- section_id: "6a00dfe2-5c22-4527-95c6-78f9ce1e133f" -->
### User Commands for Development

| Command | Action |
|---------|--------|
| `load actors` | Load all actors from .jsonld into GAB environment |
| `unload actors` | Return to builder-only mode |
| `self-check actors` | Have loaded actors analyze their own instructions |
| `undo` | Undo most recent decision |
| `rollback to [N]` | Roll back to decision number N |
| `show decisions` | View complete decision history |
| `skip formalization` | Authorize skipping Formalization Mode |

<!-- section_id: "a1200562-1e88-4296-8aef-8d4521d6353a" -->
### Self-Check Actors

GAB has built-in quality assurance via self-check actors. They analyze agent definitions for:
- **Vagueness** — terms like "reasonable" or "appropriate" that need specifics
- **Missing instructions** — actions that aren't explicitly stated
- **Inconsistencies** — contradictions between sections
- **Logic errors** — conditions that can't be met

<!-- section_id: "b7ebaf6a-1507-41a0-84bc-485f0071a9ab" -->
### AATest Testing Framework

GAB includes a companion testing tool (AATest) that follows the same 4-mode-13-actor pattern:

1. **Test Need Evaluation** — analyzes product, identifies test gaps
2. **Test Generation** — creates test files (3 types: MessageResponse, MessageFlow, AgentWorkflow)
3. **Test Execution** — runs tests within LLM context using definition adoption
4. **Test Result Reporting** — generates comprehensive reports

Test results for GAB itself: **138 tests, 100% pass rate, 100% coverage** on all metrics (actors, modes, workflows, message paths, state transitions).

---

<!-- section_id: "643e0b55-1baa-40a6-ba68-76d3bf01abda" -->
## Tested Platforms

From the professor's README:

**Generation** (using GAB):
- Cursor (Agent Mode, Auto)

**Execution** (running AALang products):
- Ollama (GUI via @context, HTTP server via system prompt)
- LM Studio (GUI and HTTP server via system prompt)
- Cursor (Agent Mode: Auto, composer1, claude-4.5-sonnet-thinking, grok-code-fast-1, gemini-3-pro-preview)

> **Note**: "Stateful AALang tools created by GAB need significant context windows to not lose the instructions and states." — professor's README

---

*Knowledge area: aalang_gab_system/gab_compiler*
*Last updated: 2026-02-07*
