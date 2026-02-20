# Stage Report Protocol

**Scope**: Universal — applies to all stage agents across all entities

## Purpose

Every stage agent writes a `stage_report.md` in its `outputs/` directory before exiting. The entity manager reads these reports to maintain a rolled-up view of all stages without loading stage-level details.

## When to Write

- After completing any significant work in a stage
- Before handing off to another stage
- When the manager requests a status update

## Location

`outputs/stage_report.md` within the stage directory.

## Format

```markdown
# Stage Report: {NN}_{stage_name}

## Status
{pending | active | blocked | complete}

## Last Updated
{YYYY-MM-DD}

## Summary
{2-3 sentences: what this stage does and where it stands}

## Key Outputs
- `outputs/{path}`: {one-line description}

## Findings
- {Key insight or decision, 1 line each}

## Open Items
- {What's unresolved or needs attention}

## Handoff
- **Ready for next stage**: {yes | no}
- **Next stage**: {NN}_{stage_name}
- **What next stage needs to know**: {1-2 sentences}
```

## Rules

1. Keep it under 30 lines — this is a summary, not a detailed report
2. Use the exact format above so the manager can parse consistently
3. Findings should be conclusions, not process descriptions
4. Open items should be actionable — what specifically needs to happen
5. Update the report, don't append — each write replaces the previous version
6. The manager may update `0INDEX.md` after reading your report

## Related

- **Stage Report Rule**: `../02_rules/static/STAGE_REPORT_RULE.md` — mandates that all agents write stage reports
- **Stage Guides**: `../01_knowledge/layer_stage_system/stage_guides/` — what each stage agent does
