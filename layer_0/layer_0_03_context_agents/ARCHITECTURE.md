---
resource_id: "18412aaf-3281-4530-a978-bb2d022d9a53"
resource_type: "document"
resource_name: "ARCHITECTURE"
---
# Context Agents Architecture

**Purpose**: Document how context agents execute and persist state, including how we extend AALang's base design.

**Reference**: [AALang-Gab](https://github.com/yenrab/AALang-Gab) - The upstream specification

---

<!-- section_id: "f3026dfb-6110-4dfe-baf2-7f4f76d09e18" -->
## Executive Summary

Our context agents use the **full AALang/GAB 4-mode-13-actor pattern** in a single comprehensive JSON-LD file (`context_loading.gab.jsonld`). We extend AALang's session-only state with **cross-session persistence** via `context_state.json`.

| Aspect | AALang Base | Our Implementation |
|--------|-------------|-------------------|
| File Organization | Single comprehensive file | ✓ Same (`context_loading.gab.jsonld`) |
| Execution Model | Hybrid (LLM interprets JSON-LD) | ✓ Same |
| Actor Pattern | 4-mode-13-actor | ✓ Same (4 modes, 8 personas, 5 state actors) |
| Persona Deliberation | Senior/Junior pairs per mode | ✓ Same |
| Prohibitions | Severity levels (absolute/critical/standard) | ✓ Same |
| State Persistence | Session-only | **Extended**: Cross-session via file |
| Team Lead | User as team lead | ✓ Same |

---

<!-- section_id: "9c28e1e2-c36a-482d-8302-8272f93a80ab" -->
## Part 1: File Organization

<!-- section_id: "1d8644dc-9dd5-445a-b6bb-d6a85b63625c" -->
### Why One File?

AALang is designed for **LLM agent consumption**. After analyzing `gab.jsonld` (40,878 tokens in ONE file), we learned that a single comprehensive file is more efficient for AI:

| Single File | Multiple Files |
|-------------|----------------|
| 1 read, everything available | Multiple reads, stitching together |
| All @id references resolvable immediately | Must load referenced files to see connections |
| Complete picture at once | Partial views, must reconstruct |
| 1 tool call | 10-30 tool calls |

<!-- section_id: "043cdc12-6569-4e17-b691-0e41ecc627bd" -->
### Our Implementation

```
sub_layer_0_01_context_agents/
├── context_loading.gab.jsonld    ← ONE comprehensive file (57KB)
├── ARCHITECTURE.md               ← This document
└── README.md                     ← Overview and usage
```

The single `context_loading.gab.jsonld` contains:
- **@context**: Namespace definitions
- **prohibitions**: Top-level prohibitions with severity levels
- **@graph**: Array containing ALL nodes:
  - ExecutionInstructions (mode switching)
  - ContextLoadingAgent (main agent definition)
  - 4 Modes (Loading, Validation, Propagation, Delivery)
  - 8 Actors (2 per mode)
  - 8 Personas (Senior/Junior pairs)
  - 5 State Actors with State Personas
  - Message Interface
  - Isolated States per mode
  - User/Team Lead definition
  - Features (DebugCommands, CrossSessionPersistence)
  - Specifications (LayerInheritanceModel, ConfidenceCalculation)

---

<!-- section_id: "dbd5ac9f-8655-4d0d-91b0-b1d79ec52611" -->
## Part 2: The 4-Mode-13-Actor Pattern

<!-- section_id: "dab783cd-3e27-45a0-8b46-a49f3ba2a5c7" -->
### Pattern Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  CONTEXT LOADING AGENT: 4-mode-13-actor pattern                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

MODES (4):                          PERSONAS (8 mode + 5 state = 13 total):
├── LoadingMode (Phase 1)           ├── LoadingPersona1 (Senior) + LoadingPersona2 (Junior)
├── ValidationMode (Phase 2)        ├── ValidationPersona1 (Senior) + ValidationPersona2 (Junior)
├── PropagationMode (Phase 3)       ├── PropagationPersona1 (Senior) + PropagationPersona2 (Junior)
└── DeliveryMode (Phase 4)          └── DeliveryPersona1 (Senior) + DeliveryPersona2 (Junior)

STATE ACTORS (5):
├── ContextLoadingStateActor → ContextLoadingStatePersona
├── ContextConfidenceStateActor → ContextConfidenceStatePersona
├── NavigationStateActor → NavigationStatePersona
├── DebugContextStateActor → DebugContextStatePersona
└── LayerInheritanceStateActor → LayerInheritanceStatePersona
```

<!-- section_id: "919cb508-9266-44fd-a9ce-11e0cc557ecb" -->
### Senior/Junior Persona Pattern

Each mode has a Senior and Junior persona that work together:

| Role | Characteristics | Responsibilities |
|------|-----------------|------------------|
| **Senior** | Experienced, methodical, systematic | Lead the work, make decisions, calculate scores |
| **Junior** | Detail-oriented, questioning, edge-case finder | Assist, verify, challenge assumptions, catch errors |

This follows the GAB pattern where personas deliberate and verify each other's work.

<!-- section_id: "aa196008-d2ac-4e72-82e3-4fe6b7eb1591" -->
### Mode Transitions

```
LoadingMode ──(confidence >= 0.6)──▶ ValidationMode ──(confidence >= 0.8)──▶ PropagationMode
                                                                                    │
                                                      (inheritance resolved)        │
                                                                                    ▼
                                                                             DeliveryMode
                                                                                    │
                                                              (ready indicators met)│
                                                                                    ▼
                                                                            READY FOR WORK
```

---

<!-- section_id: "cb998d59-8ba3-433e-8402-86e8105424af" -->
## Part 3: Execution Model

<!-- section_id: "f55be750-cfeb-42b7-997e-16e149e23219" -->
### How It Works

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  HYBRID EXECUTION MODEL                                                          │
└─────────────────────────────────────────────────────────────────────────────────┘

    context_loading.gab.jsonld                AI Runtime (Claude)
    ═══════════════════════════               ════════════════════

    ┌─────────────────────────┐
    │ ONE comprehensive file  │ ──────────▶  AI reads entire definition
    │ containing:             │                     │
    │ • ExecutionInstructions │                     │ Understands:
    │ • Agent definition      │                     │ • "Switch to execution mode"
    │ • 4 modes               │                     │ • "Follow 4-phase workflow"
    │ • 13 actors/personas    │                     │ • "Track state via actors"
    │ • Prohibitions          │                     │ • "Check confidence thresholds"
    │ • Inheritance model     │                     │ • "Persist state to file"
    └─────────────────────────┘                     │
                                                    ▼
                                            AI executes as the agent
```

<!-- section_id: "d7347627-c1ad-412d-994b-bb4fb75c631b" -->
### Execution Flow

1. **Session starts** → Claude Code loads CLAUDE.md chain
2. **CLAUDE.md contains** → `@agent ctx:ContextLoadingAgent` reference
3. **AI reads** → `context_loading.gab.jsonld` (one read, complete definition)
4. **AI switches mode** → From assistant to execution mode (per ExecutionInstructions)
5. **AI executes** → Runs 4 phases with Senior/Junior persona deliberation
6. **AI persists state** → Saves to `context_state.json` for cross-session continuity

---

<!-- section_id: "293c9973-af00-4528-bfac-e2b583046543" -->
## Part 4: State Persistence (Our Extension)

<!-- section_id: "d4f6ed8d-a041-49bd-aed6-8238a002eacf" -->
### What AALang Says

From the AALang-Gab repository:

> "All actors are **stateful**" and "maintain its own isolated context and state"

However, this state is **conversation-scoped**. AALang does NOT specify cross-session persistence.

<!-- section_id: "200a17f7-c9d3-44e0-a064-e75e73f25541" -->
### Our Extension: Cross-Session Persistence

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  STATE PERSISTENCE MODEL                                                         │
└─────────────────────────────────────────────────────────────────────────────────┘

    SESSION 1                              SESSION 2
    ═════════                              ═════════

    ┌─────────────────┐                    ┌─────────────────┐
    │ AI tracks state │                    │ AI reads state  │
    │ via personas    │                    │ from file       │
    └────────┬────────┘                    └────────┬────────┘
             │                                      │
             │ On Delivery Mode completion          │ On session start
             │                                      │
             ▼                                      ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                   .claude/context_state.json                 │
    └─────────────────────────────────────────────────────────────┘
```

<!-- section_id: "6251bc85-eb2f-4be3-b12b-4d40c78ed73c" -->
### State File Location

```
0_layer_universal/.claude/context_state.json
```

---

<!-- section_id: "3a385f0f-a755-4156-b724-5803c89ff6d7" -->
## Part 5: What We Use from AALang/GAB

| AALang/GAB Feature | Our Implementation |
|--------------------|-------------------|
| **Single JSON-LD file** | ✓ `context_loading.gab.jsonld` |
| **4-mode-N-actor pattern** | ✓ 4 modes, 13 actors |
| **Senior/Junior persona pairs** | ✓ Per mode deliberation |
| **State actors** | ✓ 5 state actors with personas |
| **Message interface** | ✓ Inter-persona communication |
| **Isolated state per mode** | ✓ Mode-private context |
| **Prohibitions with severity** | ✓ absolute/critical/standard |
| **Confidence thresholds** | ✓ 0.6 for loading, 0.8 for work |
| **Team Lead (user)** | ✓ Override authority |
| **ExecutionInstructions** | ✓ Mode switching on load |
| **Debug mode** | ✓ Toggleable visibility |

---

<!-- section_id: "c4845930-8955-474d-9456-864017201ac9" -->
## Part 6: What We Extend Beyond AALang

| Extension | Description | Why |
|-----------|-------------|-----|
| **Cross-session persistence** | State saved to file | Layer-stage workflows span sessions |
| **Layer inheritance model** | Higher layers can override lower | Projects need to customize universal rules |
| **Safety rule protection** | Absolute-severity rules require approval | Security governance |
| **Automatic execution** | Runs on session start without user prompt | Context loading should be transparent |

---

<!-- section_id: "89e7ee42-a1e8-465e-a79c-863337cc8fd4" -->
## Part 7: Design Decisions Log

<!-- section_id: "dd406a23-6cfe-4da9-a9ca-c1602ad0294c" -->
### Decision 1: Single File (Following GAB Pattern)

**Date**: 2026-02-06
**Decision**: Consolidate to one comprehensive JSON-LD file
**Rationale**: AALang is designed for LLM consumption; single file is more efficient
**Evidence**: `gab.jsonld` is 40,878 tokens in ONE file
**Previous Approach**: Multiple files (rejected as less efficient for AI)

<!-- section_id: "b098ec8b-cd89-474d-b8c8-ffc241091d49" -->
### Decision 2: Full 4-Mode-13-Actor Pattern

**Date**: 2026-02-06
**Decision**: Implement full GAB pattern with Senior/Junior persona pairs
**Rationale**: User requested all AALang/GAB features
**Previous Approach**: Simplified single-agent model (replaced)

<!-- section_id: "c9e7a47b-9fe3-45ea-bb07-946746132ee1" -->
### Decision 3: Cross-Session Persistence

**Date**: 2026-02-05
**Decision**: Extend AALang with file-based state persistence
**Rationale**: Layer-stage workflows span multiple sessions
**Extension of**: AALang's session-only model
**Implementation**: `.claude/context_state.json`

<!-- section_id: "b058716c-9f93-4011-9f58-9c328f1eae82" -->
### Decision 4: Layer Inheritance with Safety Protection

**Date**: 2026-02-05
**Decision**: Higher layers can override lower, except absolute-severity rules
**Rationale**: Flexibility with safety; projects customize but can't bypass security
**Implementation**: `@override` marker, severity levels, user approval for absolute

---

<!-- section_id: "2c8296c4-3976-4b12-bfa0-04437c46364b" -->
## Part 8: Future Considerations

<!-- section_id: "582696c8-6549-45a9-912b-95917a970880" -->
### Potential Enhancements

1. **GAB Compiler Integration**: Use GAB to generate new context agents from natural language
2. **State Sync**: Sync state across devices via Syncthing
3. **State Versioning**: Track state changes over time
4. **Inter-Agent Communication**: Context agent communicating with other AALang agents

<!-- section_id: "9a8bf7f9-68d4-409a-85c8-8dfec0e034aa" -->
### Open Questions

1. **State Cleanup**: When to clear stale state?
2. **State Migration**: How to handle schema changes?
3. **Conflict Resolution**: What if state file conflicts with actual file system?

---

<!-- section_id: "4b6d3a72-03d4-4063-b32f-13fa2df61d0a" -->
## References

- **AALang-Gab Upstream**: https://github.com/yenrab/AALang-Gab
- **Our Fork**: https://github.com/Dawson2025/AALang-Gab (branch: dawson)
- **Context Loading Protocol**: `../layer_0_04_sub_layers/sub_layer_0_03_protocols/context_loading_protocol.md`
- **Priority Rules**: `../layer_0_04_sub_layers/sub_layer_0_02_rules/context_priority_rules.md`
- **State File**: `../../.claude/context_state.json`
- **GAB Specification**: `../sub_layer_0_01_ai_system/gab.jsonld` (pattern source)

---

*Document created: 2026-02-05*
*Updated: 2026-02-06 - Consolidated to single file following GAB pattern*
*Based on AALang-Gab analysis and implementation decisions*

---

*Created using AALang and Gab*
