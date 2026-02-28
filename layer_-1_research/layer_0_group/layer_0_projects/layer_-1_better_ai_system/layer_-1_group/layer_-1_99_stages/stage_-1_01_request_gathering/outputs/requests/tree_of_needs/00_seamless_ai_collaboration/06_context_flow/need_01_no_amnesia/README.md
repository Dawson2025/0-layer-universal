# Need: No Amnesia

## Parent Branch
`06_context_flow`

---

## Problem Statement

AI agents start each session with a blank slate. They have no memory of:
- Previous sessions and what was accomplished
- Decisions made and why
- Current project state
- Recent user preferences or patterns

This forces users to re-explain context every session, leads to inconsistent decisions, and wastes time re-discovering what the agent should already "know."

---

## What We Need

Agents should be able to **recover context from previous sessions** so they can:
1. Know what work was done recently
2. Understand decisions made and their rationale
3. Pick up where the last session left off
4. Maintain consistency across sessions

---

## Solution Approaches

### Approach 1: Episodic Memory Files
```
outputs/episodic/
├── index.md                    ← What to read first
├── 2026-02-03_session.md       ← Session summaries
├── 2026-02-04_session.md
└── decisions/
    └── 2026-02-03_architecture_decision.md
```

Agent reads `index.md` on session start → knows recent sessions exist → can read relevant ones.

### Approach 2: Status File
```json
// status.json
{
  "lastSession": "2026-02-04T10:30:00Z",
  "currentStage": "06_development",
  "activeWork": "implementing JSON-LD navigation",
  "recentDecisions": ["chose JSON-LD over YAML", "prototype first approach"],
  "nextSteps": ["test prototype", "validate links"]
}
```

Agent reads `status.json` on session start → instant context.

### Approach 3: Handoff Documents
```
hand_off_documents/
├── incoming/from_above/        ← What user wants
└── outgoing/to_above/
    └── latest_handoff.md       ← Summary of where we are
```

Each session ends with a handoff → next session reads it.

---

## Success Criteria

- [ ] Agent can answer "what did we do last session?" without user input
- [ ] Agent makes decisions consistent with previous sessions
- [ ] Agent doesn't re-ask questions that were already answered
- [ ] Recovery time < 30 seconds (read 1-2 files)

---

## Related Needs

- `need_04_dynamic_context_available` - How dynamic state is stored
- `02_continuous/need_02_session_resilient` - Session continuity

---

## Status

- **Priority**: High
- **Complexity**: Medium
- **Dependencies**: Need a standard format for session summaries
