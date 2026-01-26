# Version: Tree of Needs

## Current Version

**1.4.0** (2026-01-26)

Converted to DAG structure. `multimodal` now shared between 01_capable and 05_engaging (belongs to both).

---

## Versioning Policy

The Tree of Needs uses [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH
```

### MAJOR version (X.0.0)
Incremented when:
- Root need fundamentally changes
- Branch structure is reorganized
- Needs are merged or split in breaking ways
- Backward-incompatible changes to requirement format

### MINOR version (0.X.0)
Incremented when:
- New branch added
- New need added to existing branch
- Significant new requirements added to existing needs
- New meta documents added

### PATCH version (0.0.X)
Incremented when:
- Clarifications to existing requirements
- Typo fixes
- Acceptance criteria refined
- Documentation improvements
- Dependency map updates

---

## Per-Need Versioning

Each `requirements.md` file also has its own version:

```markdown
**Version**: 1.0.0
```

Need versions are independent of the tree version:
- A need can be at v2.3.1 while tree is at v1.5.0
- Update need version when that specific need changes
- Use same MAJOR.MINOR.PATCH rules

---

## Compatibility

### Forward Compatibility
New versions should:
- Not remove needs without deprecation period
- Not rename needs without redirect/alias
- Not change requirement IDs once assigned

### Backward Compatibility
Old implementations should:
- Still satisfy core requirements of newer versions
- Get warnings for deprecated patterns
- Have migration path documented

---

## Release Process

1. Make changes to needs/structure
2. Update CHANGELOG.md with changes
3. Bump version in this file
4. Bump versions in affected requirements.md files
5. Update DEPENDENCIES.md if structure changed
6. Tag the commit with version number (optional)

---

## Version Comparison

To check if implementation satisfies a version:

```
Tree version required: 1.2.0
Implementation version: 1.3.1

1.3.1 >= 1.2.0 → Compatible ✓
```

Minor and patch increases are backward compatible.
Major increases may require migration.
