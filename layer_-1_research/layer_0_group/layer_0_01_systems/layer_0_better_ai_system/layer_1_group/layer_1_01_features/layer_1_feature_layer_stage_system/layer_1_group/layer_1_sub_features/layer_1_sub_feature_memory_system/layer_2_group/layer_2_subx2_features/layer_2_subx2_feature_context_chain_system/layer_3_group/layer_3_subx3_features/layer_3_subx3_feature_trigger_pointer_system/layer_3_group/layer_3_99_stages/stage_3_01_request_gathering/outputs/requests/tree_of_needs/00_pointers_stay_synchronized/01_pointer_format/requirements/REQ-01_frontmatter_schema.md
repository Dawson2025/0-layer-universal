---
resource_id: "8350765d-5fec-444f-b3fd-a3f5afaa1b29"
resource_type: "output"
resource_name: "REQ-01_frontmatter_schema"
---
# REQ-01: Frontmatter Schema

**Need**: [Pointer Format](../README.md)

<!-- section_id: "6a706613-c023-4a8a-a213-223ddbd56cb5" -->
## Requirements

- **MUST** start with `---` YAML frontmatter delimiters
- **MUST** include `pointer_to:` field (human-readable logical ID)
- **MUST** include `canonical_entity:` field (directory name used by `find`)
- **MAY** include `canonical_stage:` field (stage directory within entity)
- **MAY** include `canonical_subpath:` field (path within stage/entity)
- **MUST** be parseable by `sed` and `grep` (no complex YAML features)
- **MUST** tolerate both Unix and Windows line endings
