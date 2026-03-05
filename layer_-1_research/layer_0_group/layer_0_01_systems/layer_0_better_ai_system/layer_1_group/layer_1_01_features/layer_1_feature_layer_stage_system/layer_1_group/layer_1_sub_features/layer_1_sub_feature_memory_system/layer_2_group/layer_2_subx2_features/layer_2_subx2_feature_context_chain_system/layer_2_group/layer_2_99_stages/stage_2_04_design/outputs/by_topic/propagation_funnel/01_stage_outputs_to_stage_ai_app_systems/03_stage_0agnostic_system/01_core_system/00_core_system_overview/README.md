---
resource_id: "55158857-718b-4c9c-9616-2e59b19f77ac"
resource_type: "readme
output"
resource_name: "README"
---
# Core System (01-05) Overview

## What Is Core System?

The core system is the **unified, canonical source of truth** for all context in the layer-stage hierarchy. It lives in `.0agnostic/` at every entity and stage level, organized into five numbered sections:

- **01_knowledge/** — What we know (principles, documentation, resources)
- **02_rules/** — What constraints apply (static and dynamic rules)
- **03_protocols/** — How we do things (workflows, procedures)
- **04_episodic_memory/** — What we've learned (session history, changes)
- **05_handoff_documents/** — How we communicate (cross-entity messages)

## Why It's the Source of Truth

1. **Single location** — One place for each concept (no duplication)
2. **Unified representation** — Same content, adapted for different contexts
3. **Versioning** — All changes tracked in git history
4. **Cascading** — Content automatically applies to child entities and stages
5. **Navigation** — Pointers in 0AGNOSTIC.md guide agents to relevant content

## How It Gets Used

The core system is **consumed by**:
1. **Setup-Dependent layer** — which adds environment-specific adaptations
2. **Context Avenue Web** — which converts it into avenue-specific formats
3. **.1merge system** — which creates AI app-specific final versions

Each layer uses the core system content but adapts it for its specific purpose.

## Key Files

At every entity and stage level:
- `0AGNOSTIC.md` — Identity, triggers, pointers to .0agnostic/ content
- `.0agnostic/01_knowledge/` — Domain knowledge organized by topic
- `.0agnostic/02_rules/` — Constraints (static/ and dynamic/)
- `.0agnostic/03_protocols/` — Workflows and procedures
- `.0agnostic/04_episodic_memory/` — Session records and changes
- `.0agnostic/05_handoff_documents/` — Cross-entity communication

## Reference

See the numbered subdirectories (01_knowledge, 02_rules, etc.) for documentation of each core section.
