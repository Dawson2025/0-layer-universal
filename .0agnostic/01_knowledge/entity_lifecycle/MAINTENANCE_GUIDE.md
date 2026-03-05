---
resource_id: "dc8264ac-0bdc-4be0-a2fb-066b5e1a7ac0"
resource_type: "knowledge"
resource_name: "MAINTENANCE_GUIDE"
---
# Entity Maintenance Guide

<!-- section_id: "14aa5b55-d53f-4378-a830-4aab47fd9d31" -->
## Overview

This guide covers how to maintain, update, and manage entities over time.

<!-- section_id: "f6f6b6a8-1f2c-4887-b865-3d5f8dc9fcba" -->
## Routine Maintenance Tasks

<!-- section_id: "beedf2c5-c540-4395-ad3b-6c0fa02621c1" -->
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

<!-- section_id: "7c60770c-3a97-4f54-bd68-1f3bfa6de87f" -->
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

<!-- section_id: "767f485e-6485-4a99-94ab-7cf707b20681" -->
### 3. Stage Progression

**When**: Work moves to next phase

**What to do**:
1. Move outputs to completed stage's `outputs/`
2. Update stage's status in any tracking files
3. Create handoff document for next stage
4. Update 0INDEX.md with stage status

<!-- section_id: "0eb5f26c-7871-4b9b-a5f6-5db088c9f8c7" -->
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

<!-- section_id: "10e307b8-9037-42dc-9a17-670f4c233892" -->
## Structural Updates

<!-- section_id: "e17caa1a-57f1-4ed0-bada-875c60f9e313" -->
### Adding New Sub-Layers

1. Create directory: `sub_layer_N_XX_<name>/`
2. Create 0INDEX.md inside
3. Update parent's sub_layers 0INDEX.md
4. If contains nested sub-layers, use `_hierarchy` suffix

<!-- section_id: "8dac8cf7-533c-4141-a614-e0a6cb5e66b1" -->
### Adding New Stages

1. Create directory: `stage_N_XX_<name>/`
2. Create outputs/ structure
3. Create hand_off_documents/ structure
4. Update stages registry (if exists)
5. Update 0INDEX.md

<!-- section_id: "b4ec289a-ecf1-4bb2-a419-d938b41b1e2f" -->
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

<!-- section_id: "41f74dfb-aa36-495f-920d-23b257b0a2a2" -->
### Moving Entities

1. **Check for dependencies** - What references this entity?
2. **Update parent pointers** in 0AGNOSTIC.md
3. **Move the directory**
4. **Update all references** to new path
5. **Regenerate tool files**

---

<!-- section_id: "a21ee056-e513-452a-837c-1688fa181a37" -->
## Content Updates

<!-- section_id: "c6ad2212-1d84-4d7f-b586-54b1e17eb2a5" -->
### Updating Rules

1. Edit rule file in `sub_layer_N_04_rules/`
2. If rule is critical, add to CLAUDE.md directly
3. Update any affected documentation

<!-- section_id: "b688346c-d5cc-4498-8aef-0fef8260bfba" -->
### Updating Knowledge

1. Edit/add files in `sub_layer_N_02_knowledge_system/`
2. Update 0INDEX.md if structure changed
3. Consider if knowledge should be in universal layer_0

<!-- section_id: "9af08552-3875-4496-88da-fe619f20152d" -->
### Updating Prompts

1. Edit files in `sub_layer_N_01_knowledge_system/`
2. Regenerate tool files if knowledge is included in 0AGNOSTIC.md

---

<!-- section_id: "8639fd35-15c5-43bc-b56a-5301fcd44db4" -->
## Proposal Lifecycle

<!-- section_id: "f9b98146-fc0e-4a09-8b58-bd08e4537c20" -->
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

<!-- section_id: "7a39bb41-cf4f-45ab-a85f-94d5ca873316" -->
### Archiving Proposals

**When**: Proposal is superseded or abandoned

1. Move to `proposals/archived/`
2. Add superseded_by or abandoned note
3. Update 0INDEX.md

---

<!-- section_id: "7dad0b3e-7605-4019-b401-2a2229f03262" -->
## Health Checks

<!-- section_id: "ad8ed9e4-8cb0-4fde-a0d6-cc39cd27c1ce" -->
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

<!-- section_id: "c218dc39-7be0-44e2-a132-60be9fbe9ec1" -->
### Cleanup Tasks

- Remove empty directories
- Archive old session files
- Consolidate duplicate documentation
- Update outdated references

---

<!-- section_id: "bbad81a9-b609-48c6-aea1-edfcec185617" -->
## Version Control Integration

<!-- section_id: "f2c2cce9-812a-4a34-8a44-f075e0a6caf4" -->
### Commit Messages for Maintenance

Use these prefixes:
- `[AI Context]` - Changes to CLAUDE.md, 0AGNOSTIC.md, etc.
- `[Structure]` - Directory restructuring
- `[Docs]` - Documentation updates
- `[Cleanup]` - Maintenance and cleanup

<!-- section_id: "9d0ee35b-5bc7-4e5c-a469-e0aac6e78dc6" -->
### What to Commit Together

- 0AGNOSTIC.md + all generated tool files
- Entity move + all reference updates
- New entity + parent index update

---

*See ARCHIVAL_GUIDE.md for end-of-life entity management*
