---
resource_id: "231d48be-ceea-4d8c-9f3d-0c5e302c5d65"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Cursor Config Component

<!-- section_id: "0d839e7f-4148-49de-8b8d-4c4a3a75e467" -->
## Purpose
Defines patterns for Cursor IDE configuration.

<!-- section_id: "b7b6538c-f60a-45f3-a692-8d37f5774642" -->
## Files at Entity Root
- `.cursorrules` - Primary configuration file

<!-- section_id: "8d4c0e76-3eb9-496f-b3c5-d65b5f4b3a29" -->
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

<!-- section_id: "9977c704-7a30-430e-b03d-e19884853640" -->
## Integration
Cursor reads `.cursorrules` for AI context in the current workspace.
