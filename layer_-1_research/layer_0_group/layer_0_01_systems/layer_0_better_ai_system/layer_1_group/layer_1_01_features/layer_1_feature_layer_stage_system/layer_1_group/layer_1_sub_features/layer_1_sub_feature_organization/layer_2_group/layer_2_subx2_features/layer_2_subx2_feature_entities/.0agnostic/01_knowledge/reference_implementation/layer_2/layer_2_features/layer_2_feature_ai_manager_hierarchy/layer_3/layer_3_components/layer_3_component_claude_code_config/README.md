---
resource_id: "cc6f8924-208c-4723-b501-c35e5721e2da"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Claude Code Config Component

<!-- section_id: "609de141-8dd1-4d96-9f91-423a38d7e0dd" -->
## Purpose
Defines patterns for Claude Code CLI configuration.

<!-- section_id: "0677a77d-6637-4c9b-b714-cc41ca08ad70" -->
## Files at Entity Root
- `CLAUDE.md` - Primary configuration file
- `.claude/` - Optional configuration folder

<!-- section_id: "a58b46df-d4d3-4030-a80d-707510271e21" -->
## CLAUDE.md Pattern
```markdown
# [Entity Name]

## Purpose
[Brief description]

## Key Files
- [Important files to reference]

## Instructions
- [Entity-specific instructions]
```

<!-- section_id: "c2ec3b74-30df-49d2-8bc2-278a4eeebe5f" -->
## .claude/ Folder
Optional folder for additional Claude Code configuration:
- `settings.json` - Tool settings
- `commands/` - Custom commands
