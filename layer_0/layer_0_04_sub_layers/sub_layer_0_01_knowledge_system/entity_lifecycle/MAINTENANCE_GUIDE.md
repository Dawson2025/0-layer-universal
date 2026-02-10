# Entity Maintenance Guide

## Overview

This guide covers how to maintain, update, and manage entities over time.

## Routine Maintenance Tasks

### 1. Keeping Indexes Updated

**When**: After adding/removing content

**What to update**:
- `0INDEX.md` - Add/remove entries
- Parent's `0INDEX.md` - If entity visibility changed
- Registry files - If structure changed

**Example**:
```markdown
# In 0INDEX.md, update the Contents table:
| Item | Description | Location |
|------|-------------|----------|
| new_feature | Added 2026-02-03 | `layer_2_features/layer_2_feature_new/` |
```

### 2. Syncing Tool Files

**When**: After modifying 0AGNOSTIC.md

**How**:
```bash
# From entity root
bash .0agnostic/hooks/scripts/agnostic-sync.sh all
```

**What gets updated**:
- CLAUDE.md
- .cursorrules
- GEMINI.md
- AGENTS.md
- .github/copilot-instructions.md
- .aider.conf.yml

### 3. Stage Progression

**When**: Work moves to next phase

**What to do**:
1. Move outputs to completed stage's `outputs/`
2. Update stage's status in any tracking files
3. Create handoff document for next stage
4. Update 0INDEX.md with stage status

### 4. Episodic Memory Updates

**When**: After significant work sessions

**What to create**:
```
.0agnostic/episodic/sessions/session_YYYY-MM-DD_<topic>.md
.0agnostic/episodic/changes/YYYY-MM-DD_changes.md
```

**Session file template**:
```markdown
# Session: YYYY-MM-DD - <Topic>

## Summary
<What was accomplished>

## Key Decisions
- ...

## Next Steps
- ...
```

---

## Structural Updates

### Adding New Sub-Layers

1. Create directory: `sub_layer_N_XX_<name>/`
2. Create 0INDEX.md inside
3. Update parent's sub_layers 0INDEX.md
4. If contains nested sub-layers, use `_hierarchy` suffix

### Adding New Stages

1. Create directory: `stage_N_XX_<name>/`
2. Create outputs/ structure
3. Create hand_off_documents/ structure
4. Update stages registry (if exists)
5. Update 0INDEX.md

### Renaming Entities

1. **Update all references first**:
   - Parent's 0INDEX.md
   - Any CLAUDE.md files that reference it
   - Any hardcoded paths in scripts

2. **Rename the directory**

3. **Update internal references**:
   - 0AGNOSTIC.md identity
   - 0INDEX.md
   - Regenerate tool files

### Moving Entities

1. **Check for dependencies** - What references this entity?
2. **Update parent pointers** in 0AGNOSTIC.md
3. **Move the directory**
4. **Update all references** to new path
5. **Regenerate tool files**

---

## Content Updates

### Updating Rules

1. Edit rule file in `sub_layer_N_04_rules/`
2. If rule is critical, add to CLAUDE.md directly
3. Update any affected documentation

### Updating Knowledge

1. Edit/add files in `sub_layer_N_02_knowledge_system/`
2. Update 0INDEX.md if structure changed
3. Consider if knowledge should be in universal layer_0

### Updating Prompts

1. Edit files in `sub_layer_N_01_knowledge_system/`
2. Regenerate tool files if knowledge is included in 0AGNOSTIC.md

---

## Proposal Lifecycle

### Advancing Proposals Through Stages

```
Draft → Experimental → Testing → Rollout → Active
```

**To advance a proposal**:

1. **Complete current staging level** (all relevant stages 01-11)
2. **Move proposal file** to next staging level
3. **Update 0INDEX.md** in proposals/
4. **Reset stage progress** for new level

**Example**:
```bash
# Move from experimental to testing
mv proposals/staging/stage_experimental/stage_10_current_product/proposal_v1.md \
   proposals/staging/stage_testing/stage_01_request_gathering/
```

### Archiving Proposals

**When**: Proposal is superseded or abandoned

1. Move to `proposals/archived/`
2. Add superseded_by or abandoned note
3. Update 0INDEX.md

---

## Health Checks

### Periodic Verification

Run these checks periodically:

1. **Broken references**:
   ```bash
   grep -r "layer_.*_group" --include="*.md" | grep -v "exists"
   ```

2. **Missing indexes**:
   ```bash
   find . -type d -name "layer_*" ! -exec test -f {}/0INDEX.md \; -print
   ```

3. **Orphaned tool files**:
   ```bash
   # CLAUDE.md without matching 0AGNOSTIC.md
   find . -name "CLAUDE.md" -exec dirname {} \; | while read d; do
     [ ! -f "$d/0AGNOSTIC.md" ] && echo "Orphan: $d/CLAUDE.md"
   done
   ```

4. **Stale episodic files**:
   ```bash
   find . -path "*episodic/sessions/*" -mtime +30
   ```

### Cleanup Tasks

- Remove empty directories
- Archive old session files
- Consolidate duplicate documentation
- Update outdated references

---

## Version Control Integration

### Commit Messages for Maintenance

Use these prefixes:
- `[AI Context]` - Changes to CLAUDE.md, 0AGNOSTIC.md, etc.
- `[Structure]` - Directory restructuring
- `[Docs]` - Documentation updates
- `[Cleanup]` - Maintenance and cleanup

### What to Commit Together

- 0AGNOSTIC.md + all generated tool files
- Entity move + all reference updates
- New entity + parent index update

---

*See ARCHIVAL_GUIDE.md for end-of-life entity management*
