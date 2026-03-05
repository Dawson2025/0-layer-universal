---
resource_id: "e680182f-e6ab-4d44-9e52-b785df953a44"
resource_type: "document"
resource_name: "agnostic"
---
# 0_layer_universal - Agnostic Context

<!-- section_id: "77563331-9353-44be-b028-e64c8e11f226" -->
## Purpose

Tool-agnostic context for any AI assistant working in the layer-stage system.

<!-- section_id: "0165e998-6b08-481c-a3e0-8d2bd0cb5728" -->
## Framework Overview

This is the **Layer-Stage Framework** - a hierarchical system for organizing AI-assisted work.

<!-- section_id: "02d0c07b-b44c-40a1-a2a0-fb6ba28d90b5" -->
### Layers

| Layer | Purpose | Scope |
|-------|---------|-------|
| 0 | Universal | Rules, prompts, knowledge that apply to ALL |
| 1 | Projects | Specific projects, features, components |
| -1 | Research | Experimental projects, research |

<!-- section_id: "f5f1bb06-b6fe-48df-906e-1dddce0d2d05" -->
### Stages (Workflow)

| # | Stage | Purpose |
|---|-------|---------|
| 00 | registry | Metadata (data only) |
| 01 | request_gathering | Collect requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints |
| 04 | design | Architecture |
| 05 | planning | Break into tasks |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | History |

<!-- section_id: "86e6a632-4680-4983-88dc-3df4d4c0f060" -->
### Sub-layers (Content Types)

| # | Sub-layer | Purpose |
|---|-----------|---------|
| 00 | registry | Metadata |
| 01 | prompts | Init prompts |
| 02 | knowledge | Domain knowledge |
| 03 | principles | Guiding principles |
| 04 | rules | Constraints |
| 05+ | setup | OS/tool config |

<!-- section_id: "ccf2aa17-d0cd-4893-a2a5-460b94fa0f4c" -->
## Structure

```
0_layer_universal/
├── layer_0/                 Universal layer
│   ├── layer_0_04_sub_layers/
│   └── layer_0_99_stages/
├── layer_1/                 Projects layer
│   ├── layer_1_projects/
│   ├── layer_1_features/
│   └── layer_1_components/
└── layer_-1_research/       Research layer
    └── layer_-1_*/          Research projects
```

<!-- section_id: "da404ec8-5390-4791-ab6d-713ad52758ce" -->
## Key Patterns

<!-- section_id: "1ec4f509-aa9d-4fb8-b8b9-069ffe1f6a01" -->
### Container-as-Manager
Every folder with a context file (CLAUDE.md, agnostic.md) is a "manager" of its contents.

<!-- section_id: "42f95acb-1f4b-464d-ae3e-5f81c26f19bd" -->
### Four-Directional Handoffs
```
hand_off_documents/
├── incoming/from_above/    Tasks from parent
├── incoming/from_below/    Results from children
├── outgoing/to_above/      Results to parent
└── outgoing/to_below/      Tasks to children
```

<!-- section_id: "71794b00-9993-4139-b07f-76060557b946" -->
### Position 00 = Registry
Position 00 in any container holds only data (no manager behavior).

<!-- section_id: "0b68969f-7f61-411c-81a1-6e96bd0b88dd" -->
## On Session Start

1. Identify target layer and stage
2. Read context files walking up the tree
3. Check hand_off_documents for pending work
4. Execute or delegate as appropriate
