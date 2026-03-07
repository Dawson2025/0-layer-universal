---
resource_id: "2f3a4b5c-6d7e-4f8a-9b0c-1d2e3f4a5b6c"
resource_type: "output"
resource_name: "REQ-02_placeholder_syntax"
---
# REQ-02: Placeholder Syntax in Source Files

**Need**: [UUID-Based Reference Resolution](../README.md)

<!-- section_id: "3a4b5c6d-7e8f-4a9b-0c1d-2e3f4a5b6c7d" -->
## Requirements

- **MUST** define a placeholder syntax for UUID references in 0AGNOSTIC.md source files: `{{resolve:UUID}}`
- **MUST** be unambiguous — cannot be confused with markdown, YAML, or shell syntax
- **MUST** support full UUIDs: `{{resolve:08a4e9bc-8cc1-457e-b966-0a912ae6dff7}}`
- **SHOULD** support short prefixes: `{{resolve:08a4e9bc}}`
- **MUST** be resolvable by `agnostic-sync.sh` during generation — replaced with current path in generated output
- **MUST** be human-scannable — a reader can see it's a UUID reference even without tooling
- **MUST** survive markdown rendering without breaking (not interpreted as markdown syntax)
- **MUST NOT** break existing markdown parsers, linters, or renderers
- **SHOULD** be searchable via grep: `grep -r '{{resolve:' .` finds all UUID references
- **MUST** include both the UUID and a human-readable label in documentation tables:
  ```markdown
  | pointer-sync.sh | `{{resolve:08a4e9bc}}` | resource_id: `08a4e9bc-...` |
  ```
