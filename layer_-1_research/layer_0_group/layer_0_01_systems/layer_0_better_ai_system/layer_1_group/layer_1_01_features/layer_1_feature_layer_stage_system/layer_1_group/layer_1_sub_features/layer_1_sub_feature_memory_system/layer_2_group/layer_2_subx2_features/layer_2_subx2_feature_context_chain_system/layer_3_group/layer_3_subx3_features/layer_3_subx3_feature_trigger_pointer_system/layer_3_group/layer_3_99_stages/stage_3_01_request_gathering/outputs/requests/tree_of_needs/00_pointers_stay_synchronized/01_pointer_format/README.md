# Branch 01: Pointer Format

**Core Question**: How are pointer files structured?

## Description

Pointer files need a standardized format that is both machine-readable (for `pointer-sync.sh`) and human-readable (for agents and developers). This branch defines the YAML frontmatter schema and body conventions.

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| need_01_frontmatter_standard | What fields are required? | `pointer_to`, `canonical_entity`, optional `canonical_stage` + `canonical_subpath` |
| need_02_body_convention | What goes in the body? | `> **Canonical location**:` line, description, "do not duplicate" footer |

## Key Insight

The frontmatter uses **logical identifiers** (entity names) instead of hardcoded paths. This makes pointers resilient to directory moves — only the entity itself needs to keep its name.
