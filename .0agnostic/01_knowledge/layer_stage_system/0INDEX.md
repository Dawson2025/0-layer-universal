---
resource_id: "e0c64f2c-f43b-4819-8871-eff7a6c1ec2d"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Layer-Stage System Knowledge

<!-- section_id: "ce9ab449-92b9-4af9-ab96-239c0047ad9e" -->
## Purpose

This folder documents the core layer-stage framework - how layers, sub-layers, stages, and sub-stages work together.

---

<!-- section_id: "0e6000f7-1a8a-4c5d-9f7c-8f7ea411c196" -->
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

<!-- section_id: "20fc041c-39be-40db-bbf4-ab26af709ba1" -->
## Reading Order

<!-- section_id: "8e5f99b2-b6db-4e8e-a498-05712e93beca" -->
### For New Users
1. `OVERVIEW.md` - Get the big picture
2. `LAYERS_EXPLAINED.md` - Understand layers
3. `STAGES_EXPLAINED.md` - Understand stages
4. `SUB_LAYERS_EXPLAINED.md` - Understand sub-layers

<!-- section_id: "a8764c73-0e1d-4c75-9ead-8c85b5dbfb15" -->
### For Creating Entry Points
1. `SUB_LAYERS_AS_ENTRY_POINTS.md` - How sub-layers can be agent entry points
2. `NESTED_DEPTH_NAMING.md` - How to name nested structures
3. `SUB_STAGES_EXPLAINED.md` - How to create sub-stages

<!-- section_id: "ea2482d8-6d93-48d3-912a-be42aed036fe" -->
### For Naming Decisions
1. `NESTED_DEPTH_NAMING.md` - subxN conventions
2. `GROUP_VS_HIERARCHY.md` - Folder suffixes

---

<!-- section_id: "102f087c-77f9-4c19-9835-0f8bede25eec" -->
## Quick Reference

<!-- section_id: "176e168c-ecfe-4f5f-9373-816d7a016721" -->
### Layer Numbers
| Layer | Scope |
|-------|-------|
| 0 | Universal (all projects) |
| 1 | Project |
| 2 | Feature |
| 3+ | Component |
| -1 | Research |

<!-- section_id: "01b3a6ff-7b12-4101-8169-eda7d70247b9" -->
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

<!-- section_id: "f0085ad9-6953-4f6f-886f-545e61588226" -->
### Depth Naming
| Depth | Prefix |
|-------|--------|
| 1 | `sub_layer_` / `sub_stage_` |
| 2 | `subx2_layer_` / `subx2_stage_` |
| 3 | `subx3_layer_` / `subx3_stage_` |
| N | `subx{N}_layer_` / `subx{N}_stage_` |

---

<!-- section_id: "a42cd713-7496-4b4a-9742-d342ebaf3722" -->
## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows through the system
- [../naming_conventions/](../naming_conventions/) - All naming conventions
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and maintaining entities

---

*Core framework documentation*
