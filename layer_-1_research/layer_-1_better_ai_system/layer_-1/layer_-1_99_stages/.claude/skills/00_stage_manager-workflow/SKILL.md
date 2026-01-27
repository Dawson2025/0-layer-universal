---
name: 00_stage_manager-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# Stage Manager Workflow Skill

## When to Use

- When reordering stages (e.g., moving planning after design)
- When adding or removing stages
- When renumbering stages
- When updating stage definitions
- When ensuring cross-cutting consistency

## Current Stage Order

| # | Stage | Purpose |
|---|-------|---------|
| 00 | stage_manager | Meta: manages stages |
| 01 | request_gathering | Collect requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints |
| 04 | design | Architecture decisions |
| 05 | planning | Break into subtasks |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical |

## Workflow: Reorder Stages

### 1. Understand the Change
```
Example: Reordering stages

Current: 03_instructions → 04_design → 05_planning → 06_development
(Design now comes before planning)
```

### 2. Find All References
```bash
# Find all files referencing affected stages
grep -rl "stage_-1_04" .
grep -rl "stage_-1_05" .
grep -rl "planning" . --include="*.md"
grep -rl "design" . --include="*.md"
```

### 3. Rename Directories
```bash
# Use temp name to avoid collision when swapping
mv stage_-1_XX_old stage_-1_XX_old_TEMP
mv stage_-1_YY_new stage_-1_XX_new
mv stage_-1_XX_old_TEMP stage_-1_YY_old
```

### 4. Update All References

Files to check:
- [ ] `CLAUDE.md` in stage_manager (authoritative list)
- [ ] Each affected stage's `CLAUDE.md`
- [ ] `hand_off_documents/` in affected stages
- [ ] `outputs/overview/` documents
- [ ] Any skills referencing stage numbers
- [ ] Parent project `CLAUDE.md`

### 5. Verify No Stale References
```bash
# Should return nothing after updates (except task docs)
grep -r "OLD_STAGE_NAME" .
```

### 6. Document the Change
Create `outputs/change_log.md` entry:
```markdown
## YYYY-MM-DD: Reordered planning and design

**Change**: Moved planning after design
**Rationale**: Can't accurately plan until design reveals complexity
**Before**: instructions → planning → design
**After**: instructions → design → planning
**Files Updated**: [list]
```

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Authoritative stage definitions |
| `outputs/stage_registry.md` | Detailed documentation |
| `outputs/change_log.md` | History of changes |
| `hand_off_documents/incoming/` | Tasks to process |
| `hand_off_documents/outgoing/` | Completed task reports |

## References

For detailed procedures, read:
- `references/reorder_procedure.md` - Step-by-step reorder guide
- `references/stage_schema.md` - Stage directory structure
