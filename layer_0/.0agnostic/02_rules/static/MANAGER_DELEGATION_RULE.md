# Manager Delegation Rule

**Type**: Static (always applies)
**Scope**: All entity managers across all layers

## Rule

Entity managers MUST delegate operational work to stage agents. Managers do NOT carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with the methodology, output format, and success criteria for that stage.

## Manager's Job

1. Read `0INDEX.md` for the rolled-up view of all stages
2. Read stage reports (`stage_XX/outputs/stage_report.md`) for status
3. Decide what needs to happen next
4. Delegate to the appropriate stage agent
5. Maintain the entity-level view of how stages connect

## Manager Does NOT

- Carry the methodology for request gathering (the stage 01 agent knows that)
- Carry the research protocol (the stage 02 agent knows that)
- Carry the design standards (the stage 04 agent knows that)
- Do stage-level work directly — spawn a stage agent instead

## Delegation Pattern

```
Task tool:
  subagent_type: general-purpose
  prompt: "Work on stage_{LL}_{NN}_{name} for the {entity_name}.
           Read 0AGNOSTIC.md in that stage directory for your instructions.
           Read ../../.0agnostic/01_knowledge/ for domain context if needed.
           {specific task description}"
```

## Three-Tier Knowledge

- **Pointers** (0AGNOSTIC.md) — what this entity IS, where things are
- **Distilled** (.0agnostic/01_knowledge/) — domain knowledge, principles, architecture docs
- **Full** (stage outputs) — complete research, design specs, test results

Managers operate at the pointer tier. Stage agents load the distilled tier on demand. Full tier is consumed within stages.

## Rationale

Managers that carry operational detail:
- Overload their context window
- Become bottlenecks (can't delegate effectively)
- Drift from the actual stage state (their knowledge becomes stale)

Stage agents with their own 0AGNOSTIC.md:
- Have fresh, relevant context
- Know exactly what to do and produce
- Can be spawned independently
