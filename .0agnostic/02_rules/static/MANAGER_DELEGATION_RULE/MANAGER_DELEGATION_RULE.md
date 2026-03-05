---
resource_id: "a4dc8810-883e-487a-b7c4-08e54f0105ba"
resource_type: "rule"
resource_name: "MANAGER_DELEGATION_RULE"
---
# Manager Delegation Rule

**Type**: Static (always applies)
**Scope**: All entity managers across all layers

<!-- section_id: "c909f9e3-68f6-4273-b7c7-0b52b22924ea" -->
## Rule

Entity managers MUST delegate operational work to stage agents. Managers do NOT carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with the methodology, output format, and success criteria for that stage.

<!-- section_id: "4f77c949-bced-4197-8a73-30c0df073f6b" -->
## Manager's Job

1. Read `0INDEX.md` for the rolled-up view of all stages
2. Read stage reports (`stage_XX/outputs/stage_report.md`) for status
3. Decide what needs to happen next
4. Delegate to the appropriate stage agent
5. Maintain the entity-level view of how stages connect

<!-- section_id: "8d704563-639d-4c4c-879d-b3c72883e5a2" -->
## Manager Does NOT

- Carry the methodology for request gathering (the stage 01 agent knows that)
- Carry the research protocol (the stage 02 agent knows that)
- Carry the design standards (the stage 04 agent knows that)
- Do stage-level work directly — spawn a stage agent instead

<!-- section_id: "48d42249-b9fa-4e90-b937-5b6b37ac0218" -->
## Delegation Pattern

```
Task tool:
  subagent_type: general-purpose
  prompt: "Work on stage_{LL}_{NN}_{name} for the {entity_name}.
           Read 0AGNOSTIC.md in that stage directory for your instructions.
           Read ../../.0agnostic/01_knowledge/ for domain context if needed.
           {specific task description}"
```

<!-- section_id: "befddde4-f376-4c18-80ab-2b99b01e22ef" -->
## Three-Tier Knowledge

- **Pointers** (0AGNOSTIC.md) — what this entity IS, where things are
- **Distilled** (.0agnostic/01_knowledge/) — domain knowledge, principles, architecture docs
- **Full** (stage outputs) — complete research, design specs, test results

Managers operate at the pointer tier. Stage agents load the distilled tier on demand. Full tier is consumed within stages.

<!-- section_id: "35af61fc-aa68-4fcb-be10-ea5d0bd265e7" -->
## Rationale

Managers that carry operational detail:
- Overload their context window
- Become bottlenecks (can't delegate effectively)
- Drift from the actual stage state (their knowledge becomes stale)

Stage agents with their own 0AGNOSTIC.md:
- Have fresh, relevant context
- Know exactly what to do and produce
- Can be spawned independently
