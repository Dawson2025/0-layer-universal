# Skill: Tree of Needs Status

Check the current status and coverage of the Tree of Needs.

## Trigger
- `/tree-of-needs-status`
- When asked about requirements status
- When asked about Tree of Needs coverage

## Actions

### 1. Read Current Version
Read `outputs/requests/tree_of_needs/_meta/VERSION.md` to get current version.

### 2. Count Structure
Count:
- Total branches (should be 4)
- Total needs per branch (should be 3 each)
- Total requirements.md files

### 3. Check Completeness
For each need, verify:
- [ ] requirements.md exists
- [ ] Has Definition section
- [ ] Has Requirements section with MUST/SHOULD
- [ ] Has Acceptance Criteria
- [ ] Has "Integrated From" section

### 4. Report Status

Output format:
```
## Tree of Needs Status

**Version**: X.Y.Z
**Last Updated**: [from CHANGELOG]

### Coverage

| Branch | Needs | Complete | Missing |
|--------|-------|----------|---------|
| 01_capable | 3 | 3 | 0 |
| 02_continuous | 3 | 3 | 0 |
| 03_trustworthy | 3 | 3 | 0 |
| 04_observable | 3 | 3 | 0 |

### Completeness Checks

| Check | Status |
|-------|--------|
| All needs have requirements.md | ✓ |
| All needs have acceptance criteria | ✓ |
| Dependencies documented | ✓ |
| Changelog up to date | ✓ |

### Issues Found
- [List any issues]

### Recent Changes
- [From CHANGELOG.md]
```

## Files to Read
- `outputs/requests/tree_of_needs/_meta/VERSION.md`
- `outputs/requests/tree_of_needs/_meta/CHANGELOG.md`
- `outputs/requests/tree_of_needs/00_seamless_ai_collaboration/*/need_*/requirements.md`

## Output
Summary of Tree of Needs status with any issues highlighted.
