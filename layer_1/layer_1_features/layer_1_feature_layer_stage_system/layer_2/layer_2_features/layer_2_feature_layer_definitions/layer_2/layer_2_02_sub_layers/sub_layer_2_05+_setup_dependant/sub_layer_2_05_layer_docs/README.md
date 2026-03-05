---
resource_id: "e187581b-b19f-43a1-ba6f-e9397e7e0485"
resource_type: "readme
document"
resource_name: "README"
---
# Layer Documentation

This directory contains the formal documentation for the Layer-Stage Framework's layer system.

<!-- section_id: "00fbdcb3-7fc0-411f-b725-fc5233356ea7" -->
## Documents

| File | Description |
|------|-------------|
| `layer_numbering.md` | Rules for assigning layer numbers |
| `entity_types.md` | Definitions of projects, features, components |
| `nesting_rules.md` | How entities contain other entities |
| `depth_markers.md` | Sub-layer depth notation system |

<!-- section_id: "8e9b8895-4474-42ca-95d1-0029bc54dc50" -->
## Quick Reference

<!-- section_id: "b58c0245-3798-4231-a2ee-ecb68230a02c" -->
### Layer Numbers
- Layer 0 = Universal root
- Layer N+1 = Children of Layer N

<!-- section_id: "3bae201a-46b2-4f90-92ce-8d0e919a7881" -->
### Entity Types
- Projects = Major work efforts
- Features = Functional units
- Components = Reusable pieces

<!-- section_id: "8f7a888b-fcb8-4b58-8859-82801447422a" -->
### Nesting
- `layer_N/` = Entity's internals
- `layer_N+1/` = Entity's children
