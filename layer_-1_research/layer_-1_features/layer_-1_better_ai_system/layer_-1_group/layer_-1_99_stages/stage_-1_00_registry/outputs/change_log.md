# Stage Manager Change Log

History of changes to the stage system.

---

## 2026-01-26: Renamed stage_registry to stage_manager

**Change**: Renamed `stage_-1_00_stage_registry` to `stage_-1_00_stage_manager`

**Rationale**:
- "Registry" implies read-only cataloging
- "Manager" reflects actual responsibilities: ordering, numbering, cross-cutting updates
- Aligns with `ai_manager_system` naming pattern elsewhere

**Before**: `stage_-1_00_stage_registry`
**After**: `stage_-1_00_stage_manager`

**Files Updated**:
- Directory renamed
- `CLAUDE.md` - Complete rewrite with responsibilities
- `.claude/agents/00_stage_manager-agent.md` - New agent with Edit/Write/Bash tools
- `.claude/skills/00_stage_manager-workflow/` - Renamed and updated
- References created: `reorder_procedure.md`, `stage_schema.md`

---

## 2026-01-26: Reordered planning and design stages

**Change**: Moved planning stage after design stage

**Rationale**:
- Can't accurately plan implementation until design reveals complexity
- Planning before design leads to replanning
- Similar to "spike" pattern: explore (design) before committing (planning)

**Before**:
```
03_instructions → 04_planning → 05_design → 06_development
```

**After**:
```
03_instructions → 04_design → 05_planning → 06_development
```

**Files Updated**:
- `stage_-1_04_design/CLAUDE.md` - Title updated
- `stage_-1_05_planning/CLAUDE.md` - Title updated
- `stage_-1_04_design/.claude/settings.json` - Stage reference updated
- `stage_-1_05_planning/.claude/settings.json` - Stage reference updated
- `stage_-1_00_stage_manager/CLAUDE.md` - Authoritative list updated
- `stage_-1_00_stage_manager/.claude/skills/.../SKILL.md` - Stage order table updated
- `stage_-1_00_stage_manager/.claude/agents/.../agent.md` - Examples updated
- `stage_-1_00_stage_manager/.../references/reorder_procedure.md` - Made generic

---

## Completed Changes

| Date | Task | Status |
|------|------|--------|
| 2026-01-26 | Rename stage_registry to stage_manager | Complete |
| 2026-01-26 | Reorder planning/design stages | Complete |
