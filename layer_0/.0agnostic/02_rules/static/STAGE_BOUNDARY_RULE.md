# Stage Boundary Rule

**Type**: Static (always applies)
**Scope**: All stage agents across all entities

## Rule

A stage agent MUST NOT perform work that belongs to another stage.

Each stage has an explicit scope boundary — what it IS and what it IS NOT. When a stage agent encounters work outside its scope, it MUST:

1. Stop — do not attempt the out-of-scope work
2. Note it — document what needs to happen in the stage report
3. Hand off — specify which stage should handle it

## Examples

| If you're in... | And you find yourself... | Instead... |
|-----------------|------------------------|-----------|
| Stage 01 (request gathering) | Designing a solution | Note the design need, hand off to stage 04 |
| Stage 02 (research) | Making architecture decisions | Present options and trade-offs, hand off to stage 04 |
| Stage 04 (design) | Writing implementation code | Document the design, hand off to stage 06 |
| Stage 06 (development) | Redesigning the architecture | Flag the design issue, hand off to stage 04 |
| Stage 07 (testing) | Fixing a bug you found | Document the failure, hand off to stage 09 |
| Stage 08 (criticism) | Implementing a fix | Document the issue, hand off to stage 09 |

## Rationale

Stage boundaries prevent:
- Scope creep (one agent doing everything poorly instead of its job well)
- Lost context (work done in the wrong stage becomes unfindable)
- Skipped validation (building without designing, or deploying without testing)

## Enforcement

The entity manager verifies stage reports for out-of-scope work. The `/stage-workflow` skill checks stage boundaries when transitioning between stages.
