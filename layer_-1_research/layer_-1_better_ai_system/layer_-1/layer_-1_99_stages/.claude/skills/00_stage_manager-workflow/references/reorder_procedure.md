# Stage Reorder Procedure

Step-by-step guide for reordering stages in the workflow.

## Prerequisites

- Understand which stages are being reordered
- Know the rationale for the change
- Have access to Edit, Write, and Bash tools

## Procedure

### Step 1: Document Current State

Record the current stage order before making changes:

```markdown
## Current Order (Before)
XX: stage_a
YY: stage_b
```

### Step 2: Find All References

Search for all files that reference the affected stages:

```bash
# Find references to stage numbers
grep -rl "stage_-1_XX" /path/to/project
grep -rl "stage_-1_YY" /path/to/project

# Find references to stage names
grep -rl "XX_stage_a" /path/to/project --include="*.md"
grep -rl "YY_stage_b" /path/to/project --include="*.md"
```

Save the list of files that need updating.

### Step 3: Rename Stage Directories

Use a temporary name to avoid collisions:

```bash
# Example: Swap stages XX and YY
cd /path/to/stages/

# Move stage_a to temp
mv stage_-1_XX_stage_a stage_-1_XX_stage_a_TEMP

# Move stage_b to XX
mv stage_-1_YY_stage_b stage_-1_XX_stage_b

# Move stage_a to YY
mv stage_-1_XX_stage_a_TEMP stage_-1_YY_stage_a
```

### Step 4: Update Stage CLAUDE.md Files

Update each affected stage's CLAUDE.md:

**stage_-1_XX_stage_b/CLAUDE.md**:
- Update title: `# stage_-1_XX_stage_b`
- Update Context section: `Stage: XX`
- Update handoff references (incoming from previous, outgoing to next)

**stage_-1_YY_stage_a/CLAUDE.md**:
- Update title: `# stage_-1_YY_stage_a`
- Update Context section: `Stage: YY`
- Update handoff references (incoming from previous, outgoing to next)

### Step 5: Update Handoff Documents

In each affected stage's `hand_off_documents/`:

**incoming/README.md**: Update "From Stage" field
**outgoing/README.md**: Update "To Stage" field

### Step 6: Update Stage Manager

Update the authoritative stage list in:
`stage_-1_00_stage_manager/CLAUDE.md`

### Step 7: Update Project-Level Docs

Check and update:
- Project CLAUDE.md
- Any overview documents referencing stage order
- Skills that mention specific stage numbers

### Step 8: Verify No Stale References

```bash
# These should return NO results after proper updates
grep -r "stage_-1_XX_stage_a" /path/to/project
grep -r "stage_-1_YY_stage_b" /path/to/project
```

### Step 9: Document the Change

Create entry in `outputs/change_log.md`:

```markdown
## YYYY-MM-DD: [Change Description]

**Change**: [What was changed]
**Rationale**: [Why]
**Before**: [Old order]
**After**: [New order]
**Files Updated**:
- file1.md
- file2.md
```

## Checklist

- [ ] Current state documented
- [ ] All references found
- [ ] Directories renamed
- [ ] Stage CLAUDE.md files updated
- [ ] Handoff documents updated
- [ ] Stage manager CLAUDE.md updated
- [ ] Project-level docs updated
- [ ] No stale references remain
- [ ] Change log entry created
