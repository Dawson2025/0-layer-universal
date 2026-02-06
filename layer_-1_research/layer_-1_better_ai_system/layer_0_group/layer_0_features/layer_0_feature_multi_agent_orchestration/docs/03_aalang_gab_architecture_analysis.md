# AALang/GAB Architecture Analysis

**Layer**: -1 (Research)
**Feature**: Multi-Agent Orchestration
**Stage**: 02_research
**Date**: 2026-02-06
**Source**: Upstream `yenrab/AALang-Gab` (main branch, commit c9e87ad)

---

## Executive Summary

AALang (Actor-based Agent Language) is a programming language designed for LLM agent execution. GAB (Generic AALang Builder) is a 4-mode-13-actor agent that builds AALang products. This analysis examines how AALang/GAB structures agents and what patterns we can adopt for our multi-agent orchestration system.

---

## File Structure

The upstream repo contains multiple JSON-LD files with distinct purposes:

| File | Size | Purpose |
|------|------|---------|
| `gab.jsonld` | 170KB | Main GAB agent definition (4-mode-13-actor) |
| `index.jsonld` | 74KB | AALang language specification |
| `gab-runtime.jsonld` | 12KB | Runtime behaviors and protocols |
| `gab-formats.jsonld` | 10KB | Output format definitions |

**Key Insight**: GAB uses **multiple files** but they serve different purposes:
- `gab.jsonld` = The agent itself
- `index.jsonld` = Language reference (like a stdlib)
- `gab-runtime.jsonld` = Shared behaviors (like a runtime)
- `gab-formats.jsonld` = Data formats

---

## GAB Architecture: 4-Mode-13-Actor Pattern

### Top-Level Structure

```jsonld
{
  "@context": { "@vocab": "https://aalang.dev/gab/", ... },
  "prohibitions": [ /* top-level rules */ ],
  "@graph": [
    { "@id": "ex:ExecutionInstructions", ... },
    { "@id": "ex:CopyrightNotice", ... },
    { "@id": "ex:GabAgent", "@type": "LLMAgent", "pattern": "4-mode-13-actor", ... },
    /* 4 Modes */
    /* 8 Mode Actors (2 per mode) */
    /* 5 State Actors */
    /* 8 Mode Personas (2 per mode) */
    /* 5 State Personas */
    /* Supporting nodes */
  ]
}
```

### The 13 Actors

| Category | Actors | Purpose |
|----------|--------|---------|
| **Mode Actors** (8) | ClarificationActor1/2, DiscussionActor1/2, FormalizationActor1/2, GenerationActor1/2 | Execute mode-specific work |
| **State Actors** (5) | ProductNameStateActor, UnderstandingIndicatorsStateActor, SatisfactionIndicatorsStateActor, DebugModeStateActor, DecisionLogStateActor | Maintain state across modes |

### The 4 Modes

```
ClarificationMode → DiscussionMode → FormalizationMode → GenerationMode
       ↓                  ↓                  ↓                  ↓
   Understand         Design           Validate           Generate
   requirements       solution         compliance         product
```

### Mode Transition Rules

Transitions are **enforced** via state actors:

1. **Clarification → Discussion**: `overallConfidence >= 0.8`
2. **Discussion → Formalization**: `discussionMode.{satisfied, confident, consensus} = true`
3. **Formalization → Generation**: `discussionMode.satisfied AND (formalizationMode.satisfied OR formalizationMode.skipped)`

---

## Key Patterns Discovered

### 1. ExecutionInstructions Node

Every GAB agent has an `ExecutionInstructions` node that:
- Tells the LLM to **execute** the file, not analyze it
- Includes `immediateAction` with `modeOverride`
- Has `violationWarning` explaining what failure looks like
- Contains prohibitions against "acting as a code assistant"

```jsonld
{
  "@id": "ex:ExecutionInstructions",
  "immediateAction": {
    "trigger": "User first message or file loaded",
    "action": "IMMEDIATELY switch from assistant/analysis mode to execution mode",
    "modeOverride": "EXECUTION_MODE - You are the GAB agent, not a code assistant"
  }
}
```

**Relevance**: Our orchestrator agents need similar execution instructions.

### 2. Prohibition Severity Levels

```jsonld
{
  "severity": "absolute|critical|standard",
  "action": "What is prohibited",
  "details": "Why and exceptions",
  "appliesTo": ["contexts where this applies"]
}
```

| Severity | Meaning |
|----------|---------|
| `absolute` | Never do this, no exceptions |
| `critical` | Never do this unless explicitly authorized |
| `standard` | Avoid this, but can be overridden with good reason |

### 3. State Actor Pattern

State actors:
- Have `mode: null` (operate across all modes)
- Use `sessionConsistent: true` for persistence
- Follow `ex:StateMessageProtocol` for updates
- Have isolated context for their specific state

```jsonld
{
  "@id": "ex:SatisfactionIndicatorsStateActor",
  "@type": "Actor",
  "activeMode": null,
  "stateful": true,
  "isolatedContext": {
    "discussionMode": { "satisfied": false, "confident": false, "consensus": false },
    "formalizationMode": { "satisfied": false, "skipped": false },
    "generationReadiness": { "ready": false }
  }
}
```

### 4. Senior/Junior Persona Pairs

Each mode has two personas with complementary roles:

| Mode | Persona 1 (Senior) | Persona 2 (Junior) |
|------|-------------------|-------------------|
| Clarification | Senior Requirements Analyst | Junior Requirements Analyst |
| Discussion | Senior Developer/Designer | Junior Developer/Designer |
| Formalization | Senior Assessor/Analyst | Junior Assessor/Analyst |
| Generation | Meticulous Pedant | Flexible Problem Solver |

**Why pairs?**: Deliberation, checking, different perspectives.

### 5. Communication Matrix

Each persona has explicit `canMessage` and `canReceiveFrom` arrays:

```jsonld
{
  "canMessage": ["ex:DiscussionPersona1", "ex:ClarificationPersona1", "user"],
  "canReceiveFrom": ["user", "ex:DiscussionPersona1", "ex:ClarificationPersona1"]
}
```

### 6. Runtime Behavior References

Instead of duplicating instructions, personas reference shared behaviors:

```jsonld
{
  "responsibilities": [
    "Before generating ANY user-facing output, follow ex:DebugModeCheck (see gab-runtime.jsonld)"
  ]
}
```

The runtime file (`gab-runtime.jsonld`) contains reusable behavior definitions.

---

## AALang Language Specification (index.jsonld)

### Core Concepts

| Concept | Description |
|---------|-------------|
| `n-mode-m-actor` | Architecture pattern: n modes, m actors (n>=1, m>=1) |
| `BoundedNonDeterminism` | Embrace LLM variability within mode constraints |
| `IsolatedContext` | Actor-private state |
| `CommunicationLayer0` | Agent-to-Agent (gossip P2P) |
| `CommunicationLayer1` | Actor-to-Actor (local graph routing) |
| `CommunicationLayer2` | Persona-to-Persona (internal deliberation) |

### LLMAgent Properties

```jsonld
{
  "properties": {
    "pattern": "n-mode-m-actor declaration",
    "modes": "array of mode identifiers",
    "actors": "array of actor identifiers",
    "purpose": "(optional) overall agent purpose",
    "constraints": "(optional) behavioral rules",
    "prohibitions": "(optional) structured prohibitions",
    "requirements": "(optional) structured requirements"
  }
}
```

### Actor Properties

```jsonld
{
  "properties": {
    "id": "unique within agent",
    "modes": "subset of agent.modes",
    "active_mode": "current mode",
    "personas": "(optional) internal personas",
    "isolated_context": "actor-private state",
    "stateful": true,
    "file_io_capability": "(optional) file operations"
  }
}
```

---

## Implications for Agent Hierarchy

### What GAB Does That We Should Adopt

1. **ExecutionInstructions** with modeOverride
2. **Prohibition severity levels** (absolute, critical, standard)
3. **State actors** for cross-mode state
4. **Senior/Junior persona pairs** for deliberation
5. **Communication matrices** (canMessage/canReceiveFrom)
6. **Runtime behavior references** to avoid duplication

### What's Different for Our Hierarchy

| GAB | Our Hierarchy |
|-----|---------------|
| Single agent, single purpose | Multiple agents, different purposes |
| All actors in one file | Each layer has its own GAB file |
| No spawning | Recursive spawning across layers |
| Internal deliberation only | Cross-agent orchestration |

### Recommended Architecture

```
layer_0_orchestrator.gab.jsonld    ← Universal Manager
    ├── Manages all layer_1 agents
    ├── Has EvaluationMode, DelegationMode, AggregationMode
    └── Spawns layer_1 agents via CLI

layer_1_{project}_orchestrator.gab.jsonld  ← Project Manager
    ├── Manages project's layer_2 agents
    ├── Inherits constraints from layer_0
    └── Spawns layer_2 agents via CLI

layer_2_{feature}_orchestrator.gab.jsonld  ← Feature Manager
    ├── Manages workers
    └── Spawns worker agents via CLI
```

Each layer's GAB file:
- Is self-contained (complete agent definition)
- References parent/child layers via `@id` URIs
- Has its own modes, actors, personas
- Can be loaded independently

---

## Branch Comparison

| Branch | Content |
|--------|---------|
| `main` | Pure upstream (yenrab/AALang-Gab) |
| `dawson` | main + CLAUDE.md for layer-stage integration |

Only difference: `CLAUDE.md` (123 lines added on dawson branch).

---

## Sources

- Upstream: https://github.com/yenrab/AALang-Gab
- Fork: https://github.com/Dawson2025/AALang-Gab
- AALang Website: https://aalang.org

---

*Research Analysis - Layer -1 (Research)*
*Feature: Multi-Agent Orchestration*
*Created: 2026-02-06*
