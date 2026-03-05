---
resource_id: "55158857-718b-4c9c-9616-2e59b19f77ac"
resource_type: "readme
output"
resource_name: "README"
---
# Core System (01-05) Overview

<!-- section_id: "489da919-715c-4798-95e4-e6ad6c63392b" -->
## What Is Core System?

The core system is the **unified, canonical source of truth** for all context in the layer-stage hierarchy. It lives in `.0agnostic/` at every entity and stage level, organized into five numbered sections:

- **01_knowledge/** — What we know (principles, documentation, resources)
- **02_rules/** — What constraints apply (static and dynamic rules)
- **03_protocols/** — How we do things (workflows, procedures)
- **04_episodic_memory/** — What we've learned (session history, changes)
- **05_handoff_documents/** — How we communicate (cross-entity messages)

<!-- section_id: "d908b0b7-9f9e-483c-9b81-3a36155812e5" -->
## Why It's the Source of Truth

1. **Single location** — One place for each concept (no duplication)
2. **Unified representation** — Same content, adapted for different contexts
3. **Versioning** — All changes tracked in git history
4. **Cascading** — Content automatically applies to child entities and stages
5. **Navigation** — Pointers in 0AGNOSTIC.md guide agents to relevant content

<!-- section_id: "25132462-8eaa-4479-ab4a-32d41e491f8e" -->
## How It Gets Used

The core system is **consumed by**:
1. **Setup-Dependent layer** — which adds environment-specific adaptations
2. **Context Avenue Web** — which converts it into avenue-specific formats
3. **.1merge system** — which creates AI app-specific final versions

Each layer uses the core system content but adapts it for its specific purpose.

<!-- section_id: "3face5b6-ede0-4937-9f26-fb45851779b1" -->
## Key Files

At every entity and stage level:
- `0AGNOSTIC.md` — Identity, triggers, pointers to .0agnostic/ content
- `.0agnostic/01_knowledge/` — Domain knowledge organized by topic
- `.0agnostic/02_rules/` — Constraints (static/ and dynamic/)
- `.0agnostic/03_protocols/` — Workflows and procedures
- `.0agnostic/04_episodic_memory/` — Session records and changes
- `.0agnostic/05_handoff_documents/` — Cross-entity communication

<!-- section_id: "cd849910-50a4-4ec5-8403-4504670e02e5" -->
## Reference

See the numbered subdirectories (01_knowledge, 02_rules, etc.) for documentation of each core section.
