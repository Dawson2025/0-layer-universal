---
resource_id: "d4f6e050-33a7-446c-b6ec-9538f4a0b2f4"
resource_type: "rule"
resource_name: "STAGE_REPORT_RULE"
---
# Stage Report Rule

**Type**: Static (always applies)
**Scope**: All stage agents across all entities

<!-- section_id: "3611db4c-2dbf-4b0a-b40f-509773b8a827" -->
## Rule

Every stage agent MUST update `outputs/stage_report.md` before exiting.

<!-- section_id: "17e02ba9-3fb3-40f0-818f-a47e25ed5dcc" -->
## Required Sections

A stage report MUST contain:

1. **Status**: `active` | `scaffolded` | `complete` | `blocked`
2. **Last Updated**: Date of last update
3. **Summary**: 2-3 sentences describing what this stage has done
4. **Key Outputs**: List of primary deliverables with paths
5. **Findings**: Key discoveries or decisions (if applicable)
6. **Open Items**: What remains to be done
7. **Handoff**: Whether ready for next stage, which stage, and what it needs to know

<!-- section_id: "3642b810-3072-4edf-be84-5cf005852046" -->
## Rationale

Stage reports are the primary communication channel between stage agents and the entity manager. The manager reads stage reports to understand status without loading all stage details. Without stage reports, the manager cannot:
- Know what stage to delegate to next
- Understand what was accomplished
- Identify blockers or open questions

<!-- section_id: "412aeb74-a25b-4f83-be0f-f22dfc0fe51f" -->
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
