---
resource_id: "2f7029b6-089c-4959-bf48-25e0f2db958a"
resource_type: "readme
output"
resource_name: "README"
---
# Branch 01: Pointer Format

**Core Question**: How are pointer files structured?

<!-- section_id: "c0cdcfda-dc2e-48c1-aed7-e78fc1957851" -->
## Description

Pointer files need a standardized format that is both machine-readable (for `pointer-sync.sh`) and human-readable (for agents and developers). This branch defines the YAML frontmatter schema and body conventions.

<!-- section_id: "e0731703-d4b7-4a5a-a576-163e7da0c9d4" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| need_01_frontmatter_standard | What fields are required? | `pointer_to`, `canonical_entity`, optional `canonical_stage` + `canonical_subpath` |
| need_02_body_convention | What goes in the body? | `> **Canonical location**:` line, description, "do not duplicate" footer |

<!-- section_id: "18112a92-06d7-4364-8e74-3ee743c1b53b" -->
## Key Insight

The frontmatter uses **logical identifiers** (entity names) instead of hardcoded paths. This makes pointers resilient to directory moves — only the entity itself needs to keep its name.
