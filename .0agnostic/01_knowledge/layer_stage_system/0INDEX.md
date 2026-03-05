---
resource_id: "e0c64f2c-f43b-4819-8871-eff7a6c1ec2d"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Layer-Stage System Knowledge

## Purpose

This folder documents the core layer-stage framework - how layers, sub-layers, stages, and sub-stages work together.

---

## Contents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| [OVERVIEW.md](OVERVIEW.md) | High-level system overview | **Start here** |
| [LAYERS_EXPLAINED.md](LAYERS_EXPLAINED.md) | Layer numbers, relationships | Understanding layer structure |
| [STAGES_EXPLAINED.md](STAGES_EXPLAINED.md) | Stage numbers, workflow | Understanding stage workflow |
| [SUB_LAYERS_EXPLAINED.md](SUB_LAYERS_EXPLAINED.md) | Sub-layer types and purposes | Understanding sub-layer organization |
| [SUB_LAYERS_AS_ENTRY_POINTS.md](SUB_LAYERS_AS_ENTRY_POINTS.md) | Sub-layers as agent entry points | Making sub-layers navigable by agents |
| [NESTED_DEPTH_NAMING.md](NESTED_DEPTH_NAMING.md) | subxN naming convention | Naming nested sub-layers/sub-stages |
| [SUB_STAGES_EXPLAINED.md](SUB_STAGES_EXPLAINED.md) | Sub-stages within stages | Breaking stages into finer phases |
| [GROUP_VS_HIERARCHY.md](GROUP_VS_HIERARCHY.md) | `_group` vs `_hierarchy` suffixes | Choosing correct folder suffix |

---

## Reading Order

### For New Users
1. `OVERVIEW.md` - Get the big picture
2. `LAYERS_EXPLAINED.md` - Understand layers
3. `STAGES_EXPLAINED.md` - Understand stages
4. `SUB_LAYERS_EXPLAINED.md` - Understand sub-layers

### For Creating Entry Points
1. `SUB_LAYERS_AS_ENTRY_POINTS.md` - How sub-layers can be agent entry points
2. `NESTED_DEPTH_NAMING.md` - How to name nested structures
3. `SUB_STAGES_EXPLAINED.md` - How to create sub-stages

### For Naming Decisions
1. `NESTED_DEPTH_NAMING.md` - subxN conventions
2. `GROUP_VS_HIERARCHY.md` - Folder suffixes

---

## Quick Reference

### Layer Numbers
| Layer | Scope |
|-------|-------|
| 0 | Universal (all projects) |
| 1 | Project |
| 2 | Feature |
| 3+ | Component |
| -1 | Research |

### Stage Numbers
| Stage | Phase |
|-------|-------|
| 01 | Request gathering |
| 02 | Research |
| 03 | Instructions |
| 04 | Planning |
| 05 | Design |
| 06 | Development |
| 07 | Testing |
| 08 | Criticism |
| 09 | Fixing |
| 10 | Current product |
| 11 | Archives |

### Depth Naming
| Depth | Prefix |
|-------|--------|
| 1 | `sub_layer_` / `sub_stage_` |
| 2 | `subx2_layer_` / `subx2_stage_` |
| 3 | `subx3_layer_` / `subx3_stage_` |
| N | `subx{N}_layer_` / `subx{N}_stage_` |

---

## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows through the system
- [../naming_conventions/](../naming_conventions/) - All naming conventions
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and maintaining entities

---

*Core framework documentation*
