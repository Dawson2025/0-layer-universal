# Layer Documentation

This directory contains the formal documentation for the Layer-Stage Framework's layer system.

## Documents

| File | Description |
|------|-------------|
| `layer_numbering.md` | Rules for assigning layer numbers |
| `entity_types.md` | Definitions of projects, features, components |
| `nesting_rules.md` | How entities contain other entities |
| `depth_markers.md` | Sub-layer depth notation system |

## Quick Reference

### Layer Numbers
- Layer 0 = Universal root
- Layer N+1 = Children of Layer N

### Entity Types
- Projects = Major work efforts
- Features = Functional units
- Components = Reusable pieces

### Nesting
- `layer_N/` = Entity's internals
- `layer_N+1/` = Entity's children
