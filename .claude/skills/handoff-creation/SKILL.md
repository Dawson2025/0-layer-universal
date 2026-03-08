---
resource_id: "4e72fb64-a33d-4649-a3a1-fceb8fcc667e"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: handoff-creation
description: "Create structured handoff documents to preserve session context across agent transitions. Use at the end of a work session, when transitioning between agents, or when context must survive a session boundary."
---

# Handoff Creation Skill

<!-- section_id: "6598aa23-9eee-44ff-b989-588a06ca1fbf" -->
## WHEN to Use
- **End of any non-trivial work session** — the agent is about to stop and context will be lost
- When transitioning work to a different agent (orchestrator spawning children, etc.)
- When the user says "save progress," "create a handoff," or "wrap up"
- When a complex task is partially complete and will continue in the next session
- When spawned as a child agent completing a subtask — report results to parent

<!-- section_id: "0c24f425-b92d-42e9-bd17-6c6a96809b07" -->
## WHEN NOT to Use
- Quick tasks that are fully completed (nothing to hand off)
- The user explicitly says not to create a handoff
- You're in the middle of active work (handoffs are for session boundaries)

<!-- section_id: "c9df8063-2bc4-4bd6-b8ae-cf51784ee73c" -->
## Handoff Document Contents

1. **Current status summary** — what state is the work in?
2. **Work completed this session** — what was accomplished?
3. **Pending tasks** — what still needs to be done?
4. **Decisions made** — what was decided and why?
5. **Open questions** — what needs clarification?
6. **Next steps** — what should the next agent do first?

<!-- section_id: "8ad23638-42b4-4f2a-b190-d2f9d82d9fe9" -->
## Steps

1. Review session activity (what was done)
2. **Check agent context**: Read the `.integration.md` for your role (matching the `.gab.jsonld`) to understand handoff expectations
3. Identify key accomplishments and remaining work
4. Note any blockers or issues
5. Create structured handoff document following the format above
6. Save to appropriate hand_off_documents/ location:
   - Results to parent: `hand_off_documents/outgoing/to_above/`
   - Tasks to children: `hand_off_documents/outgoing/to_below/`

<!-- section_id: "fdbb931d-421c-4328-a54f-a7fa94bc2ba0" -->
## Agnostic System

When creating handoff documents:
- If `0AGNOSTIC.md` exists in the working directory, note it as the source of truth in the handoff
- If `.0agnostic/` exists, mention available on-demand resources
- If context was modified during the session, note whether `agnostic-sync.sh` was run
- If `.1merge/` exists, note any tool-specific override state

<!-- section_id: "54c079c9-636a-4cf3-97f1-1ca086933b29" -->
## AALang Reference

The orchestrator's ReportMode handles structured handoff creation.
See: `layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`

The hand_off_documents/ directory uses four-directional communication:
- `incoming/from_above/` — tasks from parent/user
- `incoming/from_below/` — results from child agents
- `outgoing/to_above/` — results to parent/user
- `outgoing/to_below/` — tasks to child agents
