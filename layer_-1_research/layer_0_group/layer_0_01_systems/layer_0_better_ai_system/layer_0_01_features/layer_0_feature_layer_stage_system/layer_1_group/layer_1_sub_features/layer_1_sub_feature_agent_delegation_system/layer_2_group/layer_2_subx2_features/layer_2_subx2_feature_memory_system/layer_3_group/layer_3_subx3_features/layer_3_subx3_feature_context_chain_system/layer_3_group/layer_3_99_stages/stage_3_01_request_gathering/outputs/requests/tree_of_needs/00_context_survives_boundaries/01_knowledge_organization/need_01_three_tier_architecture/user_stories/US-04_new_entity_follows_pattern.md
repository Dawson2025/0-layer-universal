# US-04: New entity follows the pattern

**Need**: [Three-Tier Architecture](../README.md)

---

**As a** user creating a new entity (project, feature, sub-feature),
**I want** a knowledge file template so every entity's knowledge is structured the same way,
**So that** the AI can navigate any entity's knowledge without learning a new layout each time.

### What Happens

1. User creates a new entity and tells the AI to set up its knowledge structure
2. AI uses the knowledge file template to create consistent knowledge files
3. New entity's knowledge files have the same sections (summary, references, version) as every other entity
4. Any AI session entering the new entity can load its knowledge using the same pattern

### Acceptance Criteria

- Knowledge file template exists with required sections (summary, references, version)
- All new entities use the template; no one-off formats
- Template is referenced from entity creation tooling
