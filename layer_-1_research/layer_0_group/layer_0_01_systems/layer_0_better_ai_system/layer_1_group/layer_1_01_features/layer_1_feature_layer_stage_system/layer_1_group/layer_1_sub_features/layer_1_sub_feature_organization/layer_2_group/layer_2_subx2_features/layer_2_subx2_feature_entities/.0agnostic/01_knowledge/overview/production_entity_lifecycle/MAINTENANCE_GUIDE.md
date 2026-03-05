---
resource_id: "561ac377-1f3f-481d-9bff-b302b81a0df5"
resource_type: "knowledge"
resource_name: "MAINTENANCE_GUIDE"
---
# Entity Maintenance Guide

<!-- section_id: "4c364584-99fc-4069-96a8-04117e5f988b" -->
## Overview

This guide covers how to maintain, update, and manage entities over time.

<!-- section_id: "710964a0-535a-4f2d-bd22-9575f8783a29" -->
## Routine Maintenance Tasks

<!-- section_id: "47a67d7b-93c8-4ee2-900e-1d392c472abf" -->
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

<!-- section_id: "b82d4a04-8f6b-4e6b-807d-af00d2196423" -->
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

<!-- section_id: "12700f47-e301-4270-ac94-514b62f99e18" -->
### 3. Stage Progression

**When**: Work moves to next phase

**What to do**:
1. Move outputs to completed stage's `outputs/`
2. Update stage's status in any tracking files
3. Create handoff document for next stage
4. Update 0INDEX.md with stage status

<!-- section_id: "6992db28-0a7f-48fd-942a-67ebd5a782ab" -->
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

<!-- section_id: "962d0d58-cdf0-4847-a22a-80a4b8131e1f" -->
## Structural Updates

<!-- section_id: "20ce6578-239a-416d-9002-84edecd92ca1" -->
### Adding New Sub-Layers

1. Create directory: `sub_layer_N_XX_<name>/`
2. Create 0INDEX.md inside
3. Update parent's sub_layers 0INDEX.md
4. If contains nested sub-layers, use `_hierarchy` suffix

<!-- section_id: "7938106f-aef5-49fe-b636-4a33cc751a3b" -->
### Adding New Stages

1. Create directory: `stage_N_XX_<name>/`
2. Create outputs/ structure
3. Create hand_off_documents/ structure
4. Update stages registry (if exists)
5. Update 0INDEX.md

<!-- section_id: "45626f76-2bf1-46c1-8c4e-d7294535aa4c" -->
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

<!-- section_id: "35c62af0-16a9-4cbb-a344-56c0c61b5197" -->
### Moving Entities

1. **Check for dependencies** - What references this entity?
2. **Update parent pointers** in 0AGNOSTIC.md
3. **Move the directory**
4. **Update all references** to new path
5. **Regenerate tool files**

---

<!-- section_id: "d3a2d2d3-1e96-47e7-a99a-e0277ca735d6" -->
## Content Updates

<!-- section_id: "baf18d59-42c8-4fa6-be2e-8781c7149cba" -->
### Updating Rules

1. Edit rule file in `sub_layer_N_04_rules/`
2. If rule is critical, add to CLAUDE.md directly
3. Update any affected documentation

<!-- section_id: "a1ed4d6d-ca4a-49cc-b246-d035a73f712d" -->
### Updating Knowledge

1. Edit/add files in `sub_layer_N_02_knowledge_system/`
2. Update 0INDEX.md if structure changed
3. Consider if knowledge should be in universal layer_0

<!-- section_id: "a3ac0f98-37fd-48e5-bdda-2e4ad907e38c" -->
### Updating Prompts

1. Edit files in `sub_layer_N_01_prompts/`
2. Regenerate tool files if prompts are included in 0AGNOSTIC.md

---

<!-- section_id: "cee85e79-67b1-4a36-a4f5-e5dbf40713b0" -->
## Proposal Lifecycle

<!-- section_id: "e3d8445f-dff3-41f7-9fd9-f8f2f60cfb13" -->
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

<!-- section_id: "3047d490-487d-44a3-955c-b44b1e42905b" -->
### Archiving Proposals

**When**: Proposal is superseded or abandoned

1. Move to `proposals/archived/`
2. Add superseded_by or abandoned note
3. Update 0INDEX.md

---

<!-- section_id: "fa6eed41-8767-4a9b-9e04-d12a54a01706" -->
## Health Checks

<!-- section_id: "e92a3be5-dff3-4f22-8299-8a392a00ee58" -->
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

<!-- section_id: "5e0d6938-6d73-41b6-9704-4a892a4dceb0" -->
### Cleanup Tasks

- Remove empty directories
- Archive old session files
- Consolidate duplicate documentation
- Update outdated references

---

<!-- section_id: "b1261bf2-6384-4abb-a2af-e7b52e1afdff" -->
## Version Control Integration

<!-- section_id: "9bb4ff55-7f24-4ca5-8b47-e75d83299b46" -->
### Commit Messages for Maintenance

Use these prefixes:
- `[AI Context]` - Changes to CLAUDE.md, 0AGNOSTIC.md, etc.
- `[Structure]` - Directory restructuring
- `[Docs]` - Documentation updates
- `[Cleanup]` - Maintenance and cleanup

<!-- section_id: "659ca74f-ec21-42ff-9616-ba33c03f7b5e" -->
### What to Commit Together

- 0AGNOSTIC.md + all generated tool files
- Entity move + all reference updates
- New entity + parent index update

---

*See ARCHIVAL_GUIDE.md for end-of-life entity management*
