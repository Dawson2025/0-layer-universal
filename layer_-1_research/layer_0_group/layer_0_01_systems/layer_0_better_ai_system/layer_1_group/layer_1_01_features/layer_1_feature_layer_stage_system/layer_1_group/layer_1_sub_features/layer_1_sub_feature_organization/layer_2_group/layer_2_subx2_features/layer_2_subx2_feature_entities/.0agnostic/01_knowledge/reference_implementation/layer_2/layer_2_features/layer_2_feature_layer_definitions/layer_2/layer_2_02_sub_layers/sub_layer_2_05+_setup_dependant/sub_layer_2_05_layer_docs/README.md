---
resource_id: "04c9799b-0bf5-4387-b1bf-dc5f11f1f9c2"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Layer Documentation

This directory contains the formal documentation for the Layer-Stage Framework's layer system.

<!-- section_id: "c24569aa-d49f-4084-8800-14f63d388c00" -->
## Documents

| File | Description |
|------|-------------|
| `layer_numbering.md` | Rules for assigning layer numbers |
| `entity_types.md` | Definitions of projects, features, components |
| `nesting_rules.md` | How entities contain other entities |
| `depth_markers.md` | Sub-layer depth notation system |

<!-- section_id: "cde9ec74-9a31-4443-b0e8-bb95065ccd34" -->
## Quick Reference

<!-- section_id: "cae4289b-4720-4e0c-842f-448f765a6b86" -->
### Layer Numbers
- Layer 0 = Universal root
- Layer N+1 = Children of Layer N

<!-- section_id: "f7399326-0d0e-42a5-b3c6-8410b9cd7fa5" -->
### Entity Types
- Projects = Major work efforts
- Features = Functional units
- Components = Reusable pieces

<!-- section_id: "8182b59c-1c99-4680-a2f6-437cf180f354" -->
### Nesting
- `layer_N/` = Entity's internals
- `layer_N+1/` = Entity's children
