# Context Agents Architecture

**Purpose**: Document how context agents execute and persist state, including how we extend AALang's base design.

**Reference**: [AALang-Gab](https://github.com/yenrab/AALang-Gab) - The upstream specification

---

## Executive Summary

Our context agents use a **hybrid execution model** where the AI reads JSON-LD definitions at runtime and follows them. We extend AALang's session-only state with **cross-session persistence** via `context_state.json`.

| Aspect | AALang Base | Our Extension |
|--------|-------------|---------------|
| Execution Model | Hybrid (LLM interprets JSON-LD) | Same |
| State Persistence | Session-only | Cross-session via file |
| State Actors | Conversation-scoped | File-persisted |

---

## Part 1: Execution Model

### What AALang Says

From the [AALang-Gab repository](https://github.com/yenrab/AALang-Gab):

> "AALang is a programming language designed specifically for **LLM agent consumption and execution**"

Key characteristics:

1. **Declarative Foundation**: Uses JSON-LD graph format to define structure
2. **LLM-Native Interpretation**: Agents execute "entirely within the LLM" - no external runtime needed
3. **Bounded Non-Determinism**: Structure guides behavior, but flexibility exists within bounds

### Our Implementation: Option C (Hybrid)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  HYBRID EXECUTION MODEL                                                          │
└─────────────────────────────────────────────────────────────────────────────────┘

    JSON-LD Definitions                    AI Runtime (Claude)
    ═══════════════════                    ════════════════════

    context_loading_agent.jsonld  ──────▶  AI reads definition
           │                                      │
           │ Defines:                             │ Understands:
           │ • 4 phases                           │ • "I should follow this workflow"
           │ • State actors                       │ • "I should track these states"
           │ • Transitions                        │ • "I should check confidence"
           │ • Confidence thresholds              │
           │                                      │
           ▼                                      ▼
    context_state_actors.jsonld   ──────▶  AI tracks state mentally
           │                                      │
           │ Defines:                             │ Does:
           │ • What to track                      │ • Records loaded files
           │ • How to calculate                   │ • Calculates confidence
           │ • Thresholds                         │ • Updates navigation
           │                                      │
           ▼                                      ▼
    context_modes.jsonld          ──────▶  AI follows mode sequence
                                                  │
                                                  │ Executes:
                                                  │ • Phase 1: Loading
                                                  │ • Phase 2: Validation
                                                  │ • Phase 3: Propagation
                                                  │ • Phase 4: Delivery
```

### Why Hybrid?

We evaluated three options:

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A: Purely Declarative | JSON-LD just informs behavior | Simple | No structure |
| B: Active Runtime | Custom interpreter executes JSON-LD | Deterministic | Complex to build |
| **C: Hybrid** | AI reads and interprets JSON-LD | Practical, leverages AI | Requires AI understanding |

**Decision: Option C** because:
- Leverages Claude's ability to read structured data
- No external runtime needed
- JSON-LD provides clear contracts
- Aligns with AALang's original design

### How It Works in Practice

1. **Session starts** → Claude Code loads CLAUDE.md chain
2. **CLAUDE.md contains** → `@agent ctx:ContextLoadingAgent` reference
3. **AI reads** → `context_loading_agent.jsonld` definition
4. **AI understands** → "I should follow this 4-phase workflow"
5. **AI executes** → Loads context, validates, propagates, delivers
6. **AI tracks state** → Mentally or in `context_state.json`

---

## Part 2: State Persistence

### What AALang Says

From the AALang-Gab repository:

> "All actors are **stateful**" and "maintain its own isolated context and state"

However, this state is **conversation-scoped**:

> Distinguishes "Actor statefulness" (within conversation) from "Persona session consistency" (behavior consistency across sessions)

**AALang does NOT specify cross-session persistence.**

### Our Extension: Cross-Session Persistence

We extend AALang with file-based persistence:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  STATE PERSISTENCE MODEL                                                         │
└─────────────────────────────────────────────────────────────────────────────────┘

    SESSION 1                              SESSION 2
    ═════════                              ═════════

    ┌─────────────────┐                    ┌─────────────────┐
    │ AI tracks state │                    │ AI reads state  │
    │ mentally        │                    │ from file       │
    └────────┬────────┘                    └────────┬────────┘
             │                                      │
             │ On session end                       │ On session start
             │ (or periodically)                    │
             ▼                                      ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                   context_state.json                         │
    │  ─────────────────────────────────────────────────────────   │
    │  {                                                           │
    │    "lastUpdated": "2026-02-05T17:55:00Z",                    │
    │    "contextLoadingState": { ... },                           │
    │    "contextConfidenceState": { "overallConfidence": 1.0 },   │
    │    "navigationState": { "currentLayer": 0, ... },            │
    │    "debugContextState": { "debugMode": false }               │
    │  }                                                           │
    └─────────────────────────────────────────────────────────────┘
```

### Why Cross-Session?

| Scenario | Session-Only | Cross-Session |
|----------|--------------|---------------|
| Resume work next day | Must re-identify everything | Knows where you were |
| Context already loaded | Must reload | Can skip redundant loads |
| Debug issues | No history | Can see what was loaded |
| Multi-session workflows | Each starts fresh | Continuity maintained |

### State File Location

```
0_layer_universal/.claude/context_state.json
```

### State Structure

```json
{
  "lastUpdated": "ISO timestamp",
  "sessionId": "unique session identifier",

  "contextLoadingState": {
    "loadedFiles": [{ "path": "...", "layer": 0, "lines": 222 }],
    "claudeMdChain": ["~/.claude/CLAUDE.md", ...],
    "rulesLoaded": true,
    "protocolsLoaded": true,
    "overrides": []
  },

  "contextConfidenceState": {
    "layerIdentified": 1.0,
    "stageIdentified": 1.0,
    "rulesAwareness": 1.0,
    "inheritanceResolved": 1.0,
    "requiredContextLoaded": 1.0,
    "overallConfidence": 1.0
  },

  "navigationState": {
    "currentLayer": 0,
    "currentStage": null,
    "path": "/home/.../0_layer_universal",
    "inheritanceChain": ["layer_0"]
  },

  "debugContextState": {
    "debugMode": false,
    "verboseLoading": false
  }
}
```

---

## Part 3: Comparison with AALang Base

### What We Keep from AALang

| AALang Concept | Our Implementation |
|----------------|-------------------|
| JSON-LD format | ✓ Used for all agent definitions |
| State actors | ✓ 4 state actors defined |
| Mode-based workflow | ✓ 4 phases (Loading → Validation → Propagation → Delivery) |
| Confidence thresholds | ✓ >= 0.8 before work |
| Bounded non-determinism | ✓ Structure guides, flexibility within |
| LLM-native execution | ✓ AI interprets definitions |

### What We Extend

| Extension | Why |
|-----------|-----|
| Cross-session persistence | Layer-stage spans multiple sessions |
| Layer inheritance model | Specific to our hierarchy |
| CLAUDE.md integration | Hooks into Claude Code's loading |
| File-based state | Enables session continuity |

### What We Don't Use (Yet)

| AALang Feature | Status | Reason |
|----------------|--------|--------|
| GAB compiler | Not used | We write JSON-LD directly |
| Persona deliberation | Not used | Single agent model currently |
| Message passing between actors | Simplified | State actors are read by one agent |

---

## Part 4: Design Decisions Log

### Decision 1: Execution Model

**Date**: 2026-02-05
**Decision**: Hybrid (Option C)
**Rationale**: Aligns with AALang design, leverages AI capabilities, no external runtime needed
**Alternatives Rejected**:
- Pure declarative (too loose)
- Active runtime (too complex)

### Decision 2: State Persistence

**Date**: 2026-02-05
**Decision**: Cross-session via file
**Rationale**: Layer-stage workflows span multiple sessions; need continuity
**Extension of**: AALang's session-only model
**Implementation**: `.claude/context_state.json`

### Decision 3: Layer Inheritance

**Date**: 2026-02-05
**Decision**: Higher layers can override lower layers
**Rationale**: Standard inheritance pattern; projects need to customize universal rules
**Implementation**: `@override` marker, precedence rules

---

## Part 5: Future Considerations

### Potential Enhancements

1. **GAB Compiler Integration**: Use GAB to generate agent definitions from natural language
2. **Multi-Agent Deliberation**: Multiple personas discussing context conflicts
3. **State Sync**: Sync state across devices via Syncthing
4. **State Versioning**: Track state changes over time

### Open Questions

1. **State Cleanup**: When to clear stale state?
2. **State Migration**: How to handle schema changes?
3. **Conflict Resolution**: What if state file conflicts with reality?

---

## References

- **AALang-Gab Upstream**: https://github.com/yenrab/AALang-Gab
- **Our Fork**: https://github.com/Dawson2025/AALang-Gab (branch: dawson)
- **Context Loading Protocol**: `../sub_layer_0_05_protocols/context_loading_protocol.md`
- **Priority Rules**: `../sub_layer_0_04_rules/context_priority_rules.md`
- **State File**: `../../.claude/context_state.json`

---

*Document created: 2026-02-05*
*Based on AALang-Gab analysis and implementation decisions*
