# GAB Compiler — How It Works

## Overview

GAB (Generic AALang Builder) is the "compiler" for AALang. It takes natural language descriptions of desired agent behavior and produces structured AALang agent definitions in JSON-LD format.

GAB itself is an AALang agent — a **4-mode-13-actor** agent that follows the Mode-Actor pattern it produces.

**Source**: `layer_0/layer_0_01_ai_manager_system/professor/gab.jsonld`

---

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

## Mode Details

### Mode 1: Clarification

**Purpose**: Understand what the user wants to build.

The Clarification mode asks targeted questions to fill gaps in the user's description. The Senior persona (ClarifyBot) identifies what information is missing, while the Junior persona (QuestionBot) formulates and asks the questions.

**Exit condition**: Confidence >= 0.7 that the requirements are understood.

**Key behaviors**:
- Asks about the agent's purpose, users, constraints
- Identifies ambiguities in the description
- Does NOT propose solutions yet — purely requirements gathering

### Mode 2: Discussion

**Purpose**: Explore design options and converge on an approach.

The Discussion mode explores how to structure the agent. The Senior persona (DesignBot) evaluates trade-offs, while the Junior persona (ExploreBot) proposes concrete options.

**Exit condition**: Confidence >= 0.8 that the design approach is solid.

**Key behaviors**:
- Proposes mode structures (how many modes, what each does)
- Discusses actor/persona assignments
- Identifies state that needs to persist across modes
- Converges on a pattern (4-mode, 5-mode, custom)

### Mode 3: Formalization

**Purpose**: Create a precise formal specification before generating code.

The Formalization mode writes out the complete specification. The Senior persona (SpecBot) validates completeness, while the Junior persona (FormalizerBot) writes the formal spec.

**Exit condition**: Confidence >= 0.9 that the spec is complete and correct.

**Key behaviors**:
- Defines every mode, actor, persona, state actor
- Specifies transition conditions and thresholds
- Documents message interfaces
- Creates work artifact definitions

### Mode 4: Generation (MANDATORY)

**Purpose**: Produce the final AALang agent definition in JSON-LD.

This mode is **mandatory** — it cannot be skipped even if the user seems satisfied with the spec. The Senior persona (QualityBot) reviews the output against the specification, while the Junior persona (GeneratorBot) produces the JSON-LD.

**Key behaviors**:
- Generates valid JSON-LD structure
- Follows AALang grammar and semantics from the language specification
- Includes all required fields (modes, actors, personas, state, messages)
- Runs quality checklist before finalizing

---

## State Actors (Persist Across All 4 Modes)

| State Actor | Tracks |
|-------------|--------|
| `ProductNameStateActor` | The name of the agent being created |
| `UnderstandingIndicatorsStateActor` | How well the requirements are understood |
| `SatisfactionIndicatorsStateActor` | Quality metrics for the generated output |
| `DebugModeStateActor` | Whether debug logging is on (controlled by user) |
| `DecisionLogStateActor` | All design decisions made during the process |

---

## Built-in Protocols

GAB includes several protocols that govern execution:

### Clarification Protocol
- How to ask questions effectively
- When to stop asking and move forward
- How to handle contradictory requirements

### Debug Protocol
- User can toggle debug mode on/off
- When on: shows internal reasoning, decision rationale, state transitions
- When off: clean user-facing output only

### NonAALang Detection Protocol
- If the user asks for something that ISN'T an AALang agent
- GAB recognizes this and redirects appropriately
- Prevents misuse of the compiler for non-agent tasks

### Quality Checklist
- Run before finalizing Generation mode output
- Validates completeness of the produced agent definition
- Ensures all required JSON-LD fields are present

---

## User's Role

In GAB's model, the user is the "Team Lead":
- GAB asks questions; the user answers
- GAB proposes options; the user decides
- The user can toggle debug mode, request changes, redirect
- GAB cannot proceed past certain gates without user input

---

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

### Self-Check Actors

GAB has built-in quality assurance via self-check actors. They analyze agent definitions for:
- **Vagueness** — terms like "reasonable" or "appropriate" that need specifics
- **Missing instructions** — actions that aren't explicitly stated
- **Inconsistencies** — contradictions between sections
- **Logic errors** — conditions that can't be met

### AATest Testing Framework

GAB includes a companion testing tool (AATest) that follows the same 4-mode-13-actor pattern:

1. **Test Need Evaluation** — analyzes product, identifies test gaps
2. **Test Generation** — creates test files (3 types: MessageResponse, MessageFlow, AgentWorkflow)
3. **Test Execution** — runs tests within LLM context using definition adoption
4. **Test Result Reporting** — generates comprehensive reports

Test results for GAB itself: **138 tests, 100% pass rate, 100% coverage** on all metrics (actors, modes, workflows, message paths, state transitions).

---

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
