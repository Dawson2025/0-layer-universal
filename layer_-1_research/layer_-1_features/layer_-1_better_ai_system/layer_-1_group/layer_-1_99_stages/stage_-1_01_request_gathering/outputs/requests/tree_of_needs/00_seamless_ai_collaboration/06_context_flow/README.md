# Branch: 06_context_flow

## Why This Branch Exists

AI agents suffer from "amnesia" - they start fresh each session without memory of previous work. Even within a session, they may not have the right context loaded to do their job effectively.

This branch addresses the need for **context to flow properly** to agents so they:
1. Don't forget what happened before
2. Have the right information at the right time
3. Can find deeper details when needed

---

## The Problem

```
Session 1: Agent learns project structure, makes decisions, documents work
Session 2: Agent starts fresh - knows nothing from Session 1
           Has to re-read everything or makes inconsistent decisions
```

**Current Pain Points:**
- Agent reads CLAUDE.md but doesn't know what happened yesterday
- Agent doesn't know which files contain which context
- Entry point files are either too sparse (agent misses info) or too verbose (context overflow)
- No clear path from "I'm here" to "I need to know X"

---

## The Solution Vision

```
Entry Point (CLAUDE.md / index.jsonld)
├── Identity: Who am I? What's my role?
├── Critical Rules: What must I always do?
├── Triggers: When do I load what?
└── Pointers: Where do I go for more?
    │
    ├── Static Context (stable, rarely changes)
    │   ├── Rules → sub_layer_0_04_rules/
    │   ├── Knowledge → sub_layer_0_02_knowledge/
    │   └── Principles → sub_layer_0_03_principles/
    │
    └── Dynamic Context (changes frequently)
        ├── Current State → status.json
        ├── Recent Sessions → episodic/
        ├── Active Work → stage outputs
        └── Handoffs → hand_off_documents/
```

---

## Needs in This Branch

| Need | Purpose |
|------|---------|
| need_01_no_amnesia | Agent remembers/can recover previous session context |
| need_02_context_propagation_works | Context flows through hierarchy correctly |
| need_03_static_context_available | Stable info (rules, knowledge) is accessible |
| need_04_dynamic_context_available | Changing info (state, sessions) is accessible |
| need_05_entry_points_right_detail | Entry files have enough to direct, not overwhelm |
| need_06_navigation_to_deeper_details | Agent can find more info when needed |

---

## Success Criteria

- [ ] Agent can resume work from previous session without user re-explaining
- [ ] Agent knows where to find rules without reading entire codebase
- [ ] Agent can check current project state quickly
- [ ] Entry point files fit in ~500 tokens but enable full navigation
- [ ] Agent can drill down to specifics via clear links

---

## Related Branches

- `01_capable/need_01_persistent_knowledge` - Related: knowledge persistence
- `01_capable/need_02_scalable_context` - Related: context scaling
- `02_continuous/need_02_session_resilient` - Related: session continuity
- `02_continuous/need_08_universal_context_discovery` - Related: context discovery

---

## Version

- **Created**: 2026-02-04
- **Status**: Active
