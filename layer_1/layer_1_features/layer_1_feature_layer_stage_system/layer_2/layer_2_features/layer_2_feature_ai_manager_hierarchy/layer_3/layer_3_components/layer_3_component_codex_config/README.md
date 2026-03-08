---
resource_id: "6247e1a0-f0eb-4dd3-b432-03da5c1e592e"
resource_type: "readme_document"
resource_name: "README"
---
# Codex Config Component

<!-- section_id: "2d3137e7-e0a7-4f1c-b0c0-b752cf7a1b07" -->
## Purpose
Defines patterns for OpenAI Codex CLI configuration.

<!-- section_id: "375c07a5-c86d-4122-b05d-77596bf5ec14" -->
## Files at Entity Root
- `AGENTS.md` - Primary configuration file

<!-- section_id: "8d9f4457-0398-465a-a94a-20efc76baa24" -->
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

<!-- section_id: "6a6359fc-664e-4307-b3b1-eb97391098e9" -->
## Integration
Codex CLI reads `AGENTS.md` for agent configuration.
