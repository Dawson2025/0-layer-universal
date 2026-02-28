# Need: Dynamic Context Available

## Parent Branch
`06_context_flow`

---

## Problem Statement

Dynamic context (current state, recent work, active decisions) changes frequently and agents need it to:
- Know what's currently happening
- Continue interrupted work
- Make consistent decisions
- Understand recent history

**Current Issues:**
- No standard place for "current state"
- Session history scattered or non-existent
- Active work not tracked
- Decisions not recorded

---

## What We Need

**Dynamic context** should be:
1. **Current** - Reflects actual state right now
2. **Accessible** - Easy to find and read
3. **Structured** - Machine-readable, not just prose
4. **Maintained** - Updated as work progresses

---

## Dynamic Context Types

| Type | What It Is | Update Frequency | Format |
|------|------------|------------------|--------|
| **Current State** | What stage, what work | Every session | `status.json` |
| **Session History** | What happened when | Per session | `episodic/*.md` |
| **Active Decisions** | Recent choices made | As decided | `decisions/*.md` |
| **Handoffs** | Transition summaries | Session boundaries | `hand_off_documents/` |
| **Work In Progress** | Uncommitted changes | Continuously | Stage outputs |

---

## Solution: Dynamic Context Structure

```
entity/
├── status.json                     ← Current state (machine-readable)
├── outputs/
│   └── episodic/
│       ├── index.md                ← Session history index
│       ├── 2026-02-04_session.md   ← Today's session
│       └── decisions/
│           └── 2026-02-04_*.md     ← Recent decisions
└── hand_off_documents/
    └── latest_handoff.md           ← Most recent handoff
```

### status.json Schema

```json
{
  "currentStage": "06_development",
  "lastModified": "2026-02-04T10:30:00Z",
  "lastSession": {
    "date": "2026-02-04",
    "summary": "Implemented JSON-LD prototype",
    "file": "outputs/episodic/2026-02-04_session.md"
  },
  "activeWork": {
    "description": "Testing JSON-LD navigation",
    "blockers": [],
    "nextSteps": ["validate links", "agent walkthrough"]
  },
  "recentDecisions": [
    {
      "date": "2026-02-03",
      "decision": "Use JSON-LD for navigation",
      "rationale": "Machine-readable, linked data standard"
    }
  ]
}
```

---

## Access Pattern

```json
// In index.jsonld
"nav:dynamicContext": {
  "status": "status.json",
  "episodic": "outputs/episodic/",
  "handoffs": "hand_off_documents/"
},

"trigger:onSessionStart": [
  {"action": "read", "target": "status.json", "purpose": "Current state"},
  {"action": "read", "target": "outputs/episodic/index.md", "purpose": "Recent history"}
]
```

---

## Success Criteria

- [ ] Agent can answer "what's the current state?" from status.json
- [ ] Agent can find what happened in the last 3 sessions
- [ ] Decisions are recorded with rationale
- [ ] Handoffs enable smooth session transitions

---

## Related Needs

- `need_01_no_amnesia` - Why we need session history
- `need_03_static_context_available` - Counterpart: stable context

---

## Status

- **Priority**: High
- **Complexity**: Medium
- **Current State**: Some structures exist (episodic/, hand_off_documents/), needs status.json
