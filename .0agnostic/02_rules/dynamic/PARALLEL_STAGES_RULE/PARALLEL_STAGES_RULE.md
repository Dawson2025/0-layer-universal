---
resource_id: "ab799d8f-fa5d-44d8-9b37-8577c0772465"
resource_type: "rule"
resource_name: "PARALLEL_STAGES_RULE"
---
# Parallel Stages Rule

**Type**: Dynamic (triggered by scenario)
**Trigger**: When stages run concurrently instead of sequentially

## Rule

When stages run in parallel, each stage agent MUST:

1. Operate independently within its own scope
2. Not read outputs from the parallel stage until that stage signals readiness in its stage report
3. Document its own findings independently
4. Merge parallel findings only through the entity manager (not directly between stage agents)

## Common Parallel Patterns

| Parallel Stages | When | How to Merge |
|----------------|------|-------------|
| 01 + 02 (requirements + research) | Requirements inform research, research reveals new requirements | Manager coordinates: new needs from research go back to 01, research questions from 01 go to 02 |
| 06 + 07 (development + testing) | TDD or incremental build-and-test | Manager coordinates: dev produces artifact, testing validates, dev continues |

## Rationale

Parallel stages accelerate work but create coordination complexity. The entity manager serves as the coordination point to prevent conflicts and ensure both stages' outputs are integrated properly.

## Manager Coordination Protocol

When managing parallel stages:
1. Read both stage reports regularly
2. Route discoveries from one stage to the other through explicit handoff notes
3. Wait for both stages to reach a checkpoint before advancing to the next phase
