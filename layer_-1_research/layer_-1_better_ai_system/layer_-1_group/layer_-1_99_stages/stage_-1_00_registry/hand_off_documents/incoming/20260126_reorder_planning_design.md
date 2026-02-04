# Task: Reorder Planning and Design Stages

**Date**: 2026-01-26
**Requested By**: User (via conversation)
**Priority**: MEDIUM

## Description

Move the **planning** stage to come AFTER the **design** stage in the workflow.

### Current Order
```
03_instructions → 04_planning → 05_design → 06_development
```

### Desired Order
```
03_instructions → 04_design → 05_planning → 06_development
```

## Rationale

You can't accurately plan implementation tasks until you understand the technical design:

1. **Design reveals complexity** - Only after designing do you know what's actually involved
2. **Planning before design = replanning** - Plans made before design often need revision
3. **Similar to "spike" pattern** - Explore (design) before committing (planning)
4. **For AI work**: Can't estimate tasks until you see the shape of the solution

## Scope

This change affects the `better_ai_system` research project:
- Path: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/`

## Acceptance Criteria

- [ ] Stage directories renamed:
  - `stage_-1_04_planning` → `stage_-1_05_planning`
  - `stage_-1_05_design` → `stage_-1_04_design`
- [ ] All CLAUDE.md files updated with new stage numbers
- [ ] All handoff documents updated (from/to references)
- [ ] Stage manager's authoritative list updated
- [ ] No stale references remain (verified with grep)
- [ ] Change documented in `outputs/change_log.md`

## Files Likely Affected

1. `stage_-1_00_stage_manager/CLAUDE.md` - Authoritative list
2. `stage_-1_04_planning/` → rename and update internals
3. `stage_-1_05_design/` → rename and update internals
4. Any skills/references mentioning these stages
5. Project-level documentation

## Notes

- Use the reorder procedure in `references/reorder_procedure.md`
- Use temp directory names to avoid collision during rename
- Verify with grep after all changes
