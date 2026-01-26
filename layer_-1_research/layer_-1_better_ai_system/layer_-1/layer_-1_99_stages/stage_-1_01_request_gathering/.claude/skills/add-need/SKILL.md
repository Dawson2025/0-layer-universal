# Skill: Add Need

Add a new need to the Tree of Needs following the extension guide.

## Trigger
- `/add-need`
- When asked to add a new requirement/need

## Inputs Required
Ask user for:
1. **Branch**: Which of the 4 branches? (01_capable, 02_continuous, 03_trustworthy, 04_observable)
2. **Need Name**: Single descriptive word (adjective or noun)
3. **Question**: What question does this need answer?
4. **Definition**: 2-3 sentence description
5. **Key Requirements**: What must be true? (MUST/SHOULD statements)

## Actions

### 1. Validate Branch
Confirm branch exists and is appropriate for the need.

### 2. Determine Number
Check existing needs in branch, assign next sequential number.

### 3. Create Folder
```bash
mkdir -p tree_of_needs/00_seamless_ai_collaboration/[branch]/need_NN_[name]/
```

### 4. Create requirements.md
Use template from `_meta/EXTENSION_GUIDE.md`:

```markdown
# Need: [Name]

**Branch**: [link to parent](../)
**Question**: "[Question]"
**Version**: 1.0.0

---

## Definition

[Definition provided]
- [Key aspect 1]
- [Key aspect 2]

---

## Why This Matters

- [Reason 1]
- [Reason 2]
- [Reason 3]

---

## Requirements

### [Category]
- MUST [requirement]
- SHOULD [requirement]

---

## Acceptance Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

## Integrated From

- [Source if applicable]
```

### 5. Update Branch README
Add new need to the Child Needs table.

### 6. Update Dependencies
Add entry to `_meta/DEPENDENCIES.md` with:
- What this need depends on
- What depends on this need

### 7. Update Changelog
Add entry to `_meta/CHANGELOG.md`:
```markdown
## [X.Y.0] - YYYY-MM-DD

### Added
- `need_NN_[name]` in [branch] - [brief description]
```

### 8. Bump Version
Update `_meta/VERSION.md` (MINOR version bump for new need).

## Validation Checklist
- [ ] Folder created with correct naming
- [ ] requirements.md has all required sections
- [ ] Branch README updated
- [ ] DEPENDENCIES.md updated
- [ ] CHANGELOG.md updated
- [ ] VERSION.md bumped

## Output
Confirmation of new need creation with links to created files.
