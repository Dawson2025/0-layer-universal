---
resource_id: "8b5d1937-1e8d-42b3-97b6-5f693235e867"
resource_type: "knowledge"
resource_name: "ARCHITECTURE"
---
# Context Agents Architecture

**Purpose**: Document how context agents execute and persist state, including how we extend AALang's base design.

**Reference**: [AALang-Gab](https://github.com/yenrab/AALang-Gab) - The upstream specification

---

<!-- section_id: "0f5e10a9-2f56-454a-8856-4f02dd2aaa23" -->
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

<!-- section_id: "283288d5-8b64-492a-8803-4d9a4dd05093" -->
## Part 1: File Organization

<!-- section_id: "73fed1f2-1944-4633-8418-01ad7a592398" -->
### Why One File?

AALang is designed for **LLM agent consumption**. After analyzing `gab.jsonld` (40,878 tokens in ONE file), we learned that a single comprehensive file is more efficient for AI:

| Single File | Multiple Files |
|-------------|----------------|
| 1 read, everything available | Multiple reads, stitching together |
| All @id references resolvable immediately | Must load referenced files to see connections |
| Complete picture at once | Partial views, must reconstruct |
| 1 tool call | 10-30 tool calls |

<!-- section_id: "3bdce87f-0605-411b-9e86-881a2b956dc8" -->
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

<!-- section_id: "142f6c89-e435-4841-9865-5745e1cb493f" -->
## Part 2: The 4-Mode-13-Actor Pattern

<!-- section_id: "9c0b3c02-0671-49b5-b70a-fff2881e73ac" -->
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

<!-- section_id: "60aa14bc-50f6-437f-9f31-2657eda49038" -->
### Senior/Junior Persona Pattern

Each mode has a Senior and Junior persona that work together:

| Role | Characteristics | Responsibilities |
|------|-----------------|------------------|
| **Senior** | Experienced, methodical, systematic | Lead the work, make decisions, calculate scores |
| **Junior** | Detail-oriented, questioning, edge-case finder | Assist, verify, challenge assumptions, catch errors |

This follows the GAB pattern where personas deliberate and verify each other's work.

<!-- section_id: "c6ebd166-a332-45eb-8a75-174afb5c2c6c" -->
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

<!-- section_id: "0053fd35-bd33-4cd6-85e6-2194ac61e123" -->
## Part 3: Execution Model

<!-- section_id: "6801d257-d78e-45c4-a02a-7d8e984a6b40" -->
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

<!-- section_id: "02083020-ff01-42ec-a1ae-3a55a21e5aaa" -->
### Execution Flow

1. **Session starts** → Claude Code loads CLAUDE.md chain
2. **CLAUDE.md contains** → `@agent ctx:ContextLoadingAgent` reference
3. **AI reads** → `context_loading.gab.jsonld` (one read, complete definition)
4. **AI switches mode** → From assistant to execution mode (per ExecutionInstructions)
5. **AI executes** → Runs 4 phases with Senior/Junior persona deliberation
6. **AI persists state** → Saves to `context_state.json` for cross-session continuity

---

<!-- section_id: "80398d44-1677-4005-a65e-2b57a4c00d45" -->
## Part 4: State Persistence (Our Extension)

<!-- section_id: "d1195000-3526-4cff-9e92-ca78436afada" -->
### What AALang Says

From the AALang-Gab repository:

> "All actors are **stateful**" and "maintain its own isolated context and state"

However, this state is **conversation-scoped**. AALang does NOT specify cross-session persistence.

<!-- section_id: "d2527ea2-80ca-4a09-a2e3-da8d77e54614" -->
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

<!-- section_id: "446ea8e5-4a48-4a9e-8026-74b473245abe" -->
### State File Location

```
0_layer_universal/.claude/context_state.json
```

---

<!-- section_id: "292cc37c-f4dc-487e-9471-6b0c37239ffd" -->
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

<!-- section_id: "66f1f889-1d7c-43e2-a253-200129794db0" -->
## Part 6: What We Extend Beyond AALang

| Extension | Description | Why |
|-----------|-------------|-----|
| **Cross-session persistence** | State saved to file | Layer-stage workflows span sessions |
| **Layer inheritance model** | Higher layers can override lower | Projects need to customize universal rules |
| **Safety rule protection** | Absolute-severity rules require approval | Security governance |
| **Automatic execution** | Runs on session start without user prompt | Context loading should be transparent |

---

<!-- section_id: "aa8cbc1d-6d19-46db-849f-dbd5453fb94b" -->
## Part 7: Design Decisions Log

<!-- section_id: "5caa2685-a83b-4926-8843-9b035fb65800" -->
### Decision 1: Single File (Following GAB Pattern)

**Date**: 2026-02-06
**Decision**: Consolidate to one comprehensive JSON-LD file
**Rationale**: AALang is designed for LLM consumption; single file is more efficient
**Evidence**: `gab.jsonld` is 40,878 tokens in ONE file
**Previous Approach**: Multiple files (rejected as less efficient for AI)

<!-- section_id: "7ac2c2aa-2187-4bbd-b3d1-e8219b869b55" -->
### Decision 2: Full 4-Mode-13-Actor Pattern

**Date**: 2026-02-06
**Decision**: Implement full GAB pattern with Senior/Junior persona pairs
**Rationale**: User requested all AALang/GAB features
**Previous Approach**: Simplified single-agent model (replaced)

<!-- section_id: "30bcf706-5b9a-4720-8dfb-38af3354666e" -->
### Decision 3: Cross-Session Persistence

**Date**: 2026-02-05
**Decision**: Extend AALang with file-based state persistence
**Rationale**: Layer-stage workflows span multiple sessions
**Extension of**: AALang's session-only model
**Implementation**: `.claude/context_state.json`

<!-- section_id: "1b9e9ba4-ed0e-41b4-b5f6-0e9f738e5b2b" -->
### Decision 4: Layer Inheritance with Safety Protection

**Date**: 2026-02-05
**Decision**: Higher layers can override lower, except absolute-severity rules
**Rationale**: Flexibility with safety; projects customize but can't bypass security
**Implementation**: `@override` marker, severity levels, user approval for absolute

---

<!-- section_id: "1f28189d-88de-49d7-bc71-0126d875dd13" -->
## Part 8: Future Considerations

<!-- section_id: "a30fb72b-33b9-4223-9cec-af1942369933" -->
### Potential Enhancements

1. **GAB Compiler Integration**: Use GAB to generate new context agents from natural language
2. **State Sync**: Sync state across devices via Syncthing
3. **State Versioning**: Track state changes over time
4. **Inter-Agent Communication**: Context agent communicating with other AALang agents

<!-- section_id: "e5ac8ee5-0384-4c7e-90d3-1793916ee37b" -->
### Open Questions

1. **State Cleanup**: When to clear stale state?
2. **State Migration**: How to handle schema changes?
3. **Conflict Resolution**: What if state file conflicts with actual file system?

---

<!-- section_id: "d3353633-4304-498e-962b-872ae6f51c0a" -->
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
