---
resource_id: "e680182f-e6ab-4d44-9e52-b785df953a44"
resource_type: "document"
resource_name: "agnostic"
---
# 0_layer_universal - Agnostic Context

## Purpose

Tool-agnostic context for any AI assistant working in the layer-stage system.

## Framework Overview

This is the **Layer-Stage Framework** - a hierarchical system for organizing AI-assisted work.

### Layers

| Layer | Purpose | Scope |
|-------|---------|-------|
| 0 | Universal | Rules, prompts, knowledge that apply to ALL |
| 1 | Projects | Specific projects, features, components |
| -1 | Research | Experimental projects, research |

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

### Sub-layers (Content Types)

| # | Sub-layer | Purpose |
|---|-----------|---------|
| 00 | registry | Metadata |
| 01 | prompts | Init prompts |
| 02 | knowledge | Domain knowledge |
| 03 | principles | Guiding principles |
| 04 | rules | Constraints |
| 05+ | setup | OS/tool config |

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

## Key Patterns

### Container-as-Manager
Every folder with a context file (CLAUDE.md, agnostic.md) is a "manager" of its contents.

### Four-Directional Handoffs
```
hand_off_documents/
├── incoming/from_above/    Tasks from parent
├── incoming/from_below/    Results from children
├── outgoing/to_above/      Results to parent
└── outgoing/to_below/      Tasks to children
```

### Position 00 = Registry
Position 00 in any container holds only data (no manager behavior).

## On Session Start

1. Identify target layer and stage
2. Read context files walking up the tree
3. Check hand_off_documents for pending work
4. Execute or delegate as appropriate
