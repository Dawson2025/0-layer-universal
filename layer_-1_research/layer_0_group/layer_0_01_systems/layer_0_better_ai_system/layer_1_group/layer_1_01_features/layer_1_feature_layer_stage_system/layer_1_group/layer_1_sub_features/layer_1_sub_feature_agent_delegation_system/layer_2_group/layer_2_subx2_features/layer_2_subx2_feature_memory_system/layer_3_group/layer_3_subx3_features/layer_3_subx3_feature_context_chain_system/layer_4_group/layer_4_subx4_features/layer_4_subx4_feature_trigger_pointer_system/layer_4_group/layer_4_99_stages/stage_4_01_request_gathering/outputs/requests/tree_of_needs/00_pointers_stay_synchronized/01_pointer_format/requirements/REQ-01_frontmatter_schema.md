# REQ-01: Frontmatter Schema

**Need**: [Pointer Format](../README.md)

## Requirements

- **MUST** start with `---` YAML frontmatter delimiters
- **MUST** include `pointer_to:` field (human-readable logical ID)
- **MUST** include `canonical_entity:` field (directory name used by `find`)
- **MAY** include `canonical_stage:` field (stage directory within entity)
- **MAY** include `canonical_subpath:` field (path within stage/entity)
- **MUST** be parseable by `sed` and `grep` (no complex YAML features)
- **MUST** tolerate both Unix and Windows line endings
