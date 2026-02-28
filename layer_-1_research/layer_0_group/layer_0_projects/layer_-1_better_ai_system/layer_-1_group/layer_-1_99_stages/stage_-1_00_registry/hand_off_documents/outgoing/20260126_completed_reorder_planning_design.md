# Completed: Reorder Planning and Design Stages

**Date**: 2026-01-26
**Task**: `incoming/20260126_reorder_planning_design.md`
**Status**: Complete

## Changes Made

1. Renamed stage directories:
   - `stage_-1_04_planning` → `stage_-1_05_planning`
   - `stage_-1_05_design` → `stage_-1_04_design`

2. Updated stage CLAUDE.md titles in both directories

3. Updated `.claude/settings.json` in both directories

4. Updated authoritative stage list in `stage_-1_00_stage_manager/CLAUDE.md`

5. Updated skill and agent documentation to reflect new order

6. Made reorder procedure references generic (not specific to this change)

## Files Updated

- `stage_-1_04_design/CLAUDE.md`
- `stage_-1_05_planning/CLAUDE.md`
- `stage_-1_04_design/.claude/settings.json`
- `stage_-1_05_planning/.claude/settings.json`
- `stage_-1_00_stage_manager/CLAUDE.md`
- `stage_-1_00_stage_manager/.claude/skills/00_stage_manager-workflow/SKILL.md`
- `stage_-1_00_stage_manager/.claude/agents/00_stage_manager-agent.md`
- `stage_-1_00_stage_manager/.claude/skills/.../references/reorder_procedure.md`
- `stage_-1_00_stage_manager/outputs/change_log.md`

## Verification

- [x] Stage directories renamed
- [x] All CLAUDE.md files updated with new stage numbers
- [x] Settings.json files updated
- [x] Stage manager's authoritative list updated
- [x] Grep check passed (only task doc and sync-conflict backups remain)
- [x] Change documented in `outputs/change_log.md`

## New Stage Order

| Number | Name | Purpose |
|--------|------|---------|
| 00 | stage_manager | Meta-stage: manages the stage system |
| 01 | request_gathering | Collect and clarify requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints and guidelines |
| **04** | **design** | **Architecture decisions** |
| **05** | **planning** | **Break into subtasks** |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review and critique |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical versions |

## Notes

- Sync-conflict files (Syncthing backups) contain stale references but are not primary files
- Task document `20260126_reorder_planning_design.md` preserved with original content for history
