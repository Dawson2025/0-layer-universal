---
resource_id: "05ded9c0-0ceb-4dc7-9a5c-dfc28fc05903"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# Layer-Stage System Knowledge

<!-- section_id: "a6407669-8043-446b-a1df-bd77ca07f4b5" -->
## Purpose

This folder documents the core layer-stage framework - how layers, sub-layers, stages, and sub-stages work together.

---

<!-- section_id: "20f36e66-3b28-4dc6-84d2-7a555d4f8692" -->
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

<!-- section_id: "b89d07f6-7bb7-462c-a811-227ac95c9cee" -->
## Reading Order

<!-- section_id: "3541059a-c913-42c9-b2a8-a11707690818" -->
### For New Users
1. `OVERVIEW.md` - Get the big picture
2. `LAYERS_EXPLAINED.md` - Understand layers
3. `STAGES_EXPLAINED.md` - Understand stages
4. `SUB_LAYERS_EXPLAINED.md` - Understand sub-layers

<!-- section_id: "70358a69-1467-48ef-a3c2-4e9052a3de79" -->
### For Creating Entry Points
1. `SUB_LAYERS_AS_ENTRY_POINTS.md` - How sub-layers can be agent entry points
2. `NESTED_DEPTH_NAMING.md` - How to name nested structures
3. `SUB_STAGES_EXPLAINED.md` - How to create sub-stages

<!-- section_id: "843b0727-2375-44cc-9cb7-d62a13d0dafb" -->
### For Naming Decisions
1. `NESTED_DEPTH_NAMING.md` - subxN conventions
2. `GROUP_VS_HIERARCHY.md` - Folder suffixes

---

<!-- section_id: "aab78873-41ff-491f-9c67-8999b6b0a1ac" -->
## Quick Reference

<!-- section_id: "d4df85a5-d4fa-43ae-bd9f-ec0bb961810f" -->
### Layer Numbers
| Layer | Scope |
|-------|-------|
| 0 | Universal (all projects) |
| 1 | Project |
| 2 | Feature |
| 3+ | Component |
| -1 | Research |

<!-- section_id: "8c8deb27-1734-4683-b167-46a0b9b4e12d" -->
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

<!-- section_id: "2b1d32f6-8cc1-4246-a344-fff405f22ebf" -->
### Depth Naming
| Depth | Prefix |
|-------|--------|
| 1 | `sub_layer_` / `sub_stage_` |
| 2 | `subx2_layer_` / `subx2_stage_` |
| 3 | `subx3_layer_` / `subx3_stage_` |
| N | `subx{N}_layer_` / `subx{N}_stage_` |

---

<!-- section_id: "8a6d4cd6-6f12-486d-ab5a-4f313749da52" -->
## Related Knowledge

- [../AI_CONTEXT_FLOW_ARCHITECTURE.md](../AI_CONTEXT_FLOW_ARCHITECTURE.md) - How context flows through the system
- [../naming_conventions/](../naming_conventions/) - All naming conventions
- [../entity_lifecycle/](../entity_lifecycle/) - Creating and maintaining entities

---

*Core framework documentation*
