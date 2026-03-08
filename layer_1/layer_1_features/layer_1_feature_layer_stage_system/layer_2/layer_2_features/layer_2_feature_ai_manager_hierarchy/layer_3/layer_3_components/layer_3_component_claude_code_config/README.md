---
resource_id: "5ad7bd18-97bd-4961-bf74-e5b678a0419c"
resource_type: "readme_document"
resource_name: "README"
---
# Claude Code Config Component

<!-- section_id: "41250d0c-deda-486f-9821-32a042384703" -->
## Purpose
Defines patterns for Claude Code CLI configuration.

<!-- section_id: "2ee44dd9-ad2d-449f-b1f4-307751d060cc" -->
## Files at Entity Root
- `CLAUDE.md` - Primary configuration file
- `.claude/` - Optional configuration folder

<!-- section_id: "0785db04-fb5f-4249-b063-9e41544d7840" -->
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

<!-- section_id: "e2163476-7083-4fc5-8a49-c8217623a57b" -->
## .claude/ Folder
Optional folder for additional Claude Code configuration:
- `settings.json` - Tool settings
- `commands/` - Custom commands
