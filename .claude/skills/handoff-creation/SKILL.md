---
name: handoff-creation
description: "Create structured handoff documents to preserve session context across agent transitions. Use at the end of a work session, when transitioning between agents, or when context must survive a session boundary."
---

# Handoff Creation Skill

## WHEN to Use
- **End of any non-trivial work session** — the agent is about to stop and context will be lost
- When transitioning work to a different agent (orchestrator spawning children, etc.)
- When the user says "save progress," "create a handoff," or "wrap up"
- When a complex task is partially complete and will continue in the next session
- When spawned as a child agent completing a subtask — report results to parent

## WHEN NOT to Use
- Quick tasks that are fully completed (nothing to hand off)
- The user explicitly says not to create a handoff
- You're in the middle of active work (handoffs are for session boundaries)

## Handoff Document Contents

1. **Current status summary** — what state is the work in?
2. **Work completed this session** — what was accomplished?
3. **Pending tasks** — what still needs to be done?
4. **Decisions made** — what was decided and why?
5. **Open questions** — what needs clarification?
6. **Next steps** — what should the next agent do first?

## Steps

1. Review session activity (what was done)
2. **Check agent context**: Read the `.integration.md` for your role (matching the `.gab.jsonld`) to understand handoff expectations
3. Identify key accomplishments and remaining work
4. Note any blockers or issues
5. Create structured handoff document following the format above
6. Save to appropriate hand_off_documents/ location:
   - Results to parent: `hand_off_documents/outgoing/to_above/`
   - Tasks to children: `hand_off_documents/outgoing/to_below/`

## AALang Reference

The orchestrator's ReportMode handles structured handoff creation.
See: `layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`

The hand_off_documents/ directory uses four-directional communication:
- `incoming/from_above/` — tasks from parent/user
- `incoming/from_below/` — results from child agents
- `outgoing/to_above/` — results to parent/user
- `outgoing/to_below/` — tasks to child agents
