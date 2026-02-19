# Delegate, Not Operate Rule

**Type**: Static (always applies)
**Inherits from**: `layer_0/.0agnostic/02_rules/static/MANAGER_DELEGATION_RULE.md`

## Rule

Entity managers MUST delegate operational work to stage agents. Managers MUST NOT carry stage-level methodology, procedures, or domain-specific detail.

## What Managers Do
- Read `0INDEX.md` for the rolled-up view
- Read stage reports for status updates
- Decide which stage needs work next
- Spawn stage agents with task descriptions and directory pointers

## What Managers Do NOT Do
- Carry methodology for any stage (that's in each stage's `0AGNOSTIC.md`)
- Do stage-level work directly (spawn a stage agent instead)
- Make stage-internal decisions (stage agents handle their own scope)

## Instantiation for agent_delegation_system

This entity manages two child domains (memory + multi-agent). The entity manager:
- Reads stage reports and child entity dashboards
- Delegates to stage agents OR to child entity managers
- Does not carry context chain architecture (that's memory_system's domain)
- Does not carry orchestration patterns (that's multi_agent_system's domain)
