---
resource_id: "d3432ac2-a6b6-49df-97ec-25b2c1273a0c"
resource_type: "readme_document"
resource_name: "README"
---
# Cursor Config Component

<!-- section_id: "e2420ba2-7864-4352-98b7-ab690260071e" -->
## Purpose
Defines patterns for Cursor IDE configuration.

<!-- section_id: "cefa5d1f-b4bb-4392-919d-bf4882fd664c" -->
## Files at Entity Root
- `.cursorrules` - Primary configuration file

<!-- section_id: "b40d1265-62e9-43fd-a766-f81f187dbb78" -->
## .cursorrules Pattern
```
# [Entity Name] Rules

## Context
[Description of the entity]

## Instructions
- [Rule 1]
- [Rule 2]
- [Rule 3]

## File References
- [Important files]
```

<!-- section_id: "5701c44e-9ffa-4b85-9af4-721808d65309" -->
## Integration
Cursor reads `.cursorrules` for AI context in the current workspace.
