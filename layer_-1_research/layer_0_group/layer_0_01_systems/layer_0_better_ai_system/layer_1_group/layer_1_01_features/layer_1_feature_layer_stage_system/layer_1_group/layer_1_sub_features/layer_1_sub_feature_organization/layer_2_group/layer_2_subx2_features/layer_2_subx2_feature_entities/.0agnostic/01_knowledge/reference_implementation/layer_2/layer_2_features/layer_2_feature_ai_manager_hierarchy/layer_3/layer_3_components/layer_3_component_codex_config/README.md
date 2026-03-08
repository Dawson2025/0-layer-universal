---
resource_id: "a5161c8b-0c3b-4148-9d4e-3c36a2faa379"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Codex Config Component

<!-- section_id: "d6ee3083-b896-4746-b72f-d0f8bb652beb" -->
## Purpose
Defines patterns for OpenAI Codex CLI configuration.

<!-- section_id: "2f27af79-ebfb-441b-9721-d50b2fc11d78" -->
## Files at Entity Root
- `AGENTS.md` - Primary configuration file

<!-- section_id: "4e4eaa21-af5f-49ab-99a5-e91035562ee4" -->
## AGENTS.md Pattern
```markdown
# [Entity Name] Agent Configuration

## Role
[Agent role description]

## Capabilities
- [Capability 1]
- [Capability 2]

## Instructions
- [Instruction 1]
- [Instruction 2]

## Context Files
- [Files to reference]
```

<!-- section_id: "aaf188c4-415a-428c-93e0-23a0539f80a4" -->
## Integration
Codex CLI reads `AGENTS.md` for agent configuration.
