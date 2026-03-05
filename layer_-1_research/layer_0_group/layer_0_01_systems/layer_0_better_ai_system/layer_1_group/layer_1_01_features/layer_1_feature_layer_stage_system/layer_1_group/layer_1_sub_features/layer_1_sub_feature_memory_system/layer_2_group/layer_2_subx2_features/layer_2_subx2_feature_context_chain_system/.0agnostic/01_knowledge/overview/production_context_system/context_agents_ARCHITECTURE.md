---
resource_id: "648e8b66-1628-43cf-a4d8-9500f4541f10"
resource_type: "knowledge"
resource_name: "context_agents_ARCHITECTURE"
---
# Context Agents Architecture

**Purpose**: Document how context agents execute and persist state, including how we extend AALang's base design.

**Reference**: [AALang-Gab](https://github.com/yenrab/AALang-Gab) - The upstream specification

---

<!-- section_id: "58d7ab63-0919-44f6-aa80-d8caa9e9f808" -->
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

<!-- section_id: "728dd41c-0d13-4964-808c-9f154358aca2" -->
## Part 1: File Organization

<!-- section_id: "e62c1b44-e93a-4692-a0b9-6deed4a95bb2" -->
### Why One File?

AALang is designed for **LLM agent consumption**. After analyzing `gab.jsonld` (40,878 tokens in ONE file), we learned that a single comprehensive file is more efficient for AI:

| Single File | Multiple Files |
|-------------|----------------|
| 1 read, everything available | Multiple reads, stitching together |
| All @id references resolvable immediately | Must load referenced files to see connections |
| Complete picture at once | Partial views, must reconstruct |
| 1 tool call | 10-30 tool calls |

<!-- section_id: "77eed3ec-e2a3-41f4-817c-d6f4785e2298" -->
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

<!-- section_id: "f94f3334-5140-4417-a04f-1544fc908858" -->
## Part 2: The 4-Mode-13-Actor Pattern

<!-- section_id: "2c34e34d-8a26-4823-9688-c162499ca6f2" -->
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

<!-- section_id: "f08d0a92-0aa9-4b24-96fc-c9931fdf1ded" -->
### Senior/Junior Persona Pattern

Each mode has a Senior and Junior persona that work together:

| Role | Characteristics | Responsibilities |
|------|-----------------|------------------|
| **Senior** | Experienced, methodical, systematic | Lead the work, make decisions, calculate scores |
| **Junior** | Detail-oriented, questioning, edge-case finder | Assist, verify, challenge assumptions, catch errors |

This follows the GAB pattern where personas deliberate and verify each other's work.

<!-- section_id: "1ed99eec-c1da-4818-9100-805c4076931a" -->
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

<!-- section_id: "373dcaa4-643d-46c0-9d89-15e24106b1bc" -->
## Part 3: Execution Model

<!-- section_id: "8ed7e731-badb-4e6a-a7cd-1617c02da004" -->
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

<!-- section_id: "853bcce2-71a1-4a3c-b947-4cbb58fce837" -->
### Execution Flow

1. **Session starts** → Claude Code loads CLAUDE.md chain
2. **CLAUDE.md contains** → `@agent ctx:ContextLoadingAgent` reference
3. **AI reads** → `context_loading.gab.jsonld` (one read, complete definition)
4. **AI switches mode** → From assistant to execution mode (per ExecutionInstructions)
5. **AI executes** → Runs 4 phases with Senior/Junior persona deliberation
6. **AI persists state** → Saves to `context_state.json` for cross-session continuity

---

<!-- section_id: "4b21f150-1907-4e88-bb87-d2ee69b0a846" -->
## Part 4: State Persistence (Our Extension)

<!-- section_id: "053a1cd3-57a6-4c13-a17c-6862c5055e9e" -->
### What AALang Says

From the AALang-Gab repository:

> "All actors are **stateful**" and "maintain its own isolated context and state"

However, this state is **conversation-scoped**. AALang does NOT specify cross-session persistence.

<!-- section_id: "5f433ab9-9add-4fb1-be9a-96ec06986729" -->
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

<!-- section_id: "e2c2e68e-404f-4b1b-bd87-cfa6934020a4" -->
### State File Location

```
0_layer_universal/.claude/context_state.json
```

---

<!-- section_id: "7279f07b-b4d4-42d8-9bed-98088ce12f43" -->
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

<!-- section_id: "16163ead-a80d-4a98-9cda-b1303d983f8c" -->
## Part 6: What We Extend Beyond AALang

| Extension | Description | Why |
|-----------|-------------|-----|
| **Cross-session persistence** | State saved to file | Layer-stage workflows span sessions |
| **Layer inheritance model** | Higher layers can override lower | Projects need to customize universal rules |
| **Safety rule protection** | Absolute-severity rules require approval | Security governance |
| **Automatic execution** | Runs on session start without user prompt | Context loading should be transparent |

---

<!-- section_id: "213e0897-cb90-4314-94af-40d5dacaac60" -->
## Part 7: Design Decisions Log

<!-- section_id: "b9672919-faf4-41ce-bf28-7f2257f2b6d2" -->
### Decision 1: Single File (Following GAB Pattern)

**Date**: 2026-02-06
**Decision**: Consolidate to one comprehensive JSON-LD file
**Rationale**: AALang is designed for LLM consumption; single file is more efficient
**Evidence**: `gab.jsonld` is 40,878 tokens in ONE file
**Previous Approach**: Multiple files (rejected as less efficient for AI)

<!-- section_id: "9dac92cb-6659-441c-8a60-c8f3c6887640" -->
### Decision 2: Full 4-Mode-13-Actor Pattern

**Date**: 2026-02-06
**Decision**: Implement full GAB pattern with Senior/Junior persona pairs
**Rationale**: User requested all AALang/GAB features
**Previous Approach**: Simplified single-agent model (replaced)

<!-- section_id: "bb318d0a-2d18-4121-8e38-2428015b3f9e" -->
### Decision 3: Cross-Session Persistence

**Date**: 2026-02-05
**Decision**: Extend AALang with file-based state persistence
**Rationale**: Layer-stage workflows span multiple sessions
**Extension of**: AALang's session-only model
**Implementation**: `.claude/context_state.json`

<!-- section_id: "96786118-176b-4f7e-9234-8656def2aa43" -->
### Decision 4: Layer Inheritance with Safety Protection

**Date**: 2026-02-05
**Decision**: Higher layers can override lower, except absolute-severity rules
**Rationale**: Flexibility with safety; projects customize but can't bypass security
**Implementation**: `@override` marker, severity levels, user approval for absolute

---

<!-- section_id: "4d42f416-c820-4898-88c3-78e3641a7e99" -->
## Part 8: Future Considerations

<!-- section_id: "9a99ab4a-f819-4e64-bd94-9084b5ccda20" -->
### Potential Enhancements

1. **GAB Compiler Integration**: Use GAB to generate new context agents from natural language
2. **State Sync**: Sync state across devices via Syncthing
3. **State Versioning**: Track state changes over time
4. **Inter-Agent Communication**: Context agent communicating with other AALang agents

<!-- section_id: "805d4d08-b6bf-4f37-9c09-1acbcc7d83b0" -->
### Open Questions

1. **State Cleanup**: When to clear stale state?
2. **State Migration**: How to handle schema changes?
3. **Conflict Resolution**: What if state file conflicts with actual file system?

---

<!-- section_id: "aa76a810-1827-421d-be50-89bdb396358f" -->
## References

- **AALang-Gab Upstream**: https://github.com/yenrab/AALang-Gab
- **Our Fork**: https://github.com/Dawson2025/AALang-Gab (branch: dawson)
- **Context Loading Protocol**: `../sub_layer_0_05_protocols/context_loading_protocol.md`
- **Priority Rules**: `../sub_layer_0_04_rules/context_priority_rules.md`
- **State File**: `../../.claude/context_state.json`
- **GAB Specification**: `../sub_layer_0_01_ai_system/gab.jsonld` (pattern source)

---

*Document created: 2026-02-05*
*Updated: 2026-02-06 - Consolidated to single file following GAB pattern*
*Based on AALang-Gab analysis and implementation decisions*

---

*Created using AALang and Gab*
