# Extension Guide: Tree of Needs

How to extend the Tree of Needs structure while maintaining consistency.

---

## Adding a New Need to an Existing Branch

When a new need fits within an existing branch (01_capable, 02_continuous, 03_trustworthy, 04_observable):

### 1. Create the Need Folder
```bash
mkdir -p tree_of_needs/00_seamless_ai_collaboration/XX_branch/need_NN_name/
```

Naming convention:
- `need_NN_` where NN is the next sequential number in that branch
- Name should be a single descriptive adjective or noun (e.g., `discoverable`, `bounded`)

### 2. Create requirements.md
Use this template:

```markdown
# Need: [Name]

**Branch**: [link to parent branch](../)
**Question**: "[Single question this need answers]"
**Version**: 1.0.0

---

## Definition

[2-3 sentences explaining what this need means]
- [Key aspect 1]
- [Key aspect 2]
- [Key aspect 3]

---

## Why This Matters

- [Reason 1]
- [Reason 2]
- [Reason 3]
- [Reason 4]

---

## Requirements

### [Category Name] (from request_XX)
- MUST [requirement]
- MUST [requirement]
- SHOULD [requirement]

---

## Acceptance Criteria

- [ ] [Measurable criterion]
- [ ] [Measurable criterion]

---

## Integrated From

- request_XX: REQ-XX-FNN
```

### 3. Update Branch README
Add the new need to the Child Needs table in the branch README.

### 4. Update Root README
Add the need to the Branch Structure diagram.

### 5. Update Dependencies
Add any dependencies to `_meta/DEPENDENCIES.md`.

### 6. Log the Change
Add entry to `_meta/CHANGELOG.md`.

---

## Adding a New Branch

When requirements don't fit any existing branch, a new branch may be needed.

### Before Creating a New Branch

Ask these questions:
1. Does this truly represent a fundamentally different concern?
2. Could it be a sub-need of an existing branch instead?
3. Does it have at least 2-3 distinct needs that would go under it?
4. Is it orthogonal to existing branches (not overlapping)?

### If a New Branch is Justified

1. **Create branch folder**: `XX_branchname/` (next sequential number)
2. **Create branch README** with:
   - Core Question
   - Description
   - Child Needs table
   - Key Insight
3. **Create at least 2 needs** under the branch
4. **Update root README** to add the new branch
5. **Update `_meta/DEPENDENCIES.md`** with any cross-branch dependencies
6. **Log in `_meta/CHANGELOG.md`**

---

## Adding Cross-Cutting Concerns

Some requirements span multiple branches. Handle these by:

### Option 1: Primary + References
- Place the need in its primary branch
- Add cross-references in related branches' READMEs
- Document in `_meta/DEPENDENCIES.md`

### Option 2: Shared Requirements Section
- If a requirement applies to multiple needs, document it once
- Reference it from each need's requirements.md
- Use: "See also: [other_need](../path/to/other_need/)"

---

## Deprecating a Need

When a need becomes obsolete:

1. **Don't delete** - move to `_deprecated/` folder
2. **Add deprecation notice** at top of requirements.md:
   ```markdown
   > **DEPRECATED**: This need has been superseded by [new_need](path).
   > Kept for historical reference. See CHANGELOG for details.
   ```
3. **Update references** pointing to this need
4. **Log in CHANGELOG**

---

## Version Numbering

Requirements use semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Fundamental change to what the need means
- **MINOR**: New requirements added, existing unchanged
- **PATCH**: Clarifications, typo fixes, acceptance criteria updates

Update version in requirements.md header when making changes.

---

## Checklist for Any Extension

- [ ] Follows naming conventions
- [ ] Has all required sections
- [ ] Parent README updated
- [ ] Root README updated (if structure changed)
- [ ] Dependencies documented
- [ ] CHANGELOG updated
- [ ] Version number set/updated
