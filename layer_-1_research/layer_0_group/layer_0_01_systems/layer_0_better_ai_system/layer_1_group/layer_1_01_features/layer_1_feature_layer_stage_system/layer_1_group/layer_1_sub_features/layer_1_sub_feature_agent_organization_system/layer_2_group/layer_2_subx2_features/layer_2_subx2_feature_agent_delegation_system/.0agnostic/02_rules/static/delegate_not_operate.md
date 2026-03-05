---
resource_id: "36263aaa-2412-4a5e-a967-ae2a4aefeb1e"
resource_type: "rule"
resource_name: "delegate_not_operate"
---
# Delegate, Not Operate Rule

**Type**: Static (always applies)
**Inherits from**: `.0agnostic/02_rules/static/MANAGER_DELEGATION_RULE.md`

<!-- section_id: "3bd7c8fa-d333-4547-ad21-fc765980314e" -->
## Rule

Entity managers MUST delegate operational work to stage agents. Managers MUST NOT carry stage-level methodology, procedures, or domain-specific detail.

<!-- section_id: "18f0be9b-d244-438e-888e-9c01a288a5cd" -->
## What Managers Do
- Read `0INDEX.md` for the rolled-up view
- Read stage reports for status updates
- Decide which stage needs work next
- Spawn stage agents with task descriptions and directory pointers

<!-- section_id: "5b8da231-9690-460d-9446-fa3885cf6fa5" -->
## What Managers Do NOT Do
- Carry methodology for any stage (that's in each stage's `0AGNOSTIC.md`)
- Do stage-level work directly (spawn a stage agent instead)
- Make stage-internal decisions (stage agents handle their own scope)

<!-- section_id: "93c84bbd-b94b-4c00-b2df-0c599801cbc2" -->
## Instantiation for agent_delegation_system

This entity manages two child domains (memory + multi-agent). The entity manager:
- Reads stage reports and child entity dashboards
- Delegates to stage agents OR to child entity managers
- Does not carry context chain architecture (that's memory_system's domain)
- Does not carry orchestration patterns (that's multi_agent_system's domain)
