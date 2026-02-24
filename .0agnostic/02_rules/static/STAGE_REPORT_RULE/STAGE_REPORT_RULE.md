# Stage Report Rule

**Type**: Static (always applies)
**Scope**: All stage agents across all entities

## Rule

Every stage agent MUST update `outputs/stage_report.md` before exiting.

## Required Sections

A stage report MUST contain:

1. **Status**: `active` | `scaffolded` | `complete` | `blocked`
2. **Last Updated**: Date of last update
3. **Summary**: 2-3 sentences describing what this stage has done
4. **Key Outputs**: List of primary deliverables with paths
5. **Findings**: Key discoveries or decisions (if applicable)
6. **Open Items**: What remains to be done
7. **Handoff**: Whether ready for next stage, which stage, and what it needs to know

## Rationale

Stage reports are the primary communication channel between stage agents and the entity manager. The manager reads stage reports to understand status without loading all stage details. Without stage reports, the manager cannot:
- Know what stage to delegate to next
- Understand what was accomplished
- Identify blockers or open questions

## Format

```markdown
# Stage Report: {NN}_{stage_name}

## Status
{active|scaffolded|complete|blocked}

## Last Updated
{YYYY-MM-DD}

## Summary
{2-3 sentences}

## Key Outputs
- `outputs/{path}`: {description}

## Findings
- {finding 1}

## Open Items
- {item 1}

## Handoff
- **Ready for next stage**: {yes|no}
- **Next stage**: {NN}_{name}
- **What next stage needs to know**: {context}
```
