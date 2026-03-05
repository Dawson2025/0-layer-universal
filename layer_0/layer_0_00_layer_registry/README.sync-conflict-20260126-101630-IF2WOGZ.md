---
resource_id: "9b76951c-952b-4b79-ad0d-606a1bf0277e"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-101630-IF2WOGZ"
---
# Layer Registry

This directory contains the registry and metadata for layer internal structure.

<!-- section_id: "e8c65b3f-7f9e-4760-bc34-12b0d5cc4a3b" -->
## Purpose

Defines the standard components that exist within each layer:

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Metadata for this layer |
| 01 | ai_manager_system | AI agent configuration |
| 02 | manager_handoff_documents | Session transitions |
| 03 | sub_layers | Knowledge, prompts, rules, setup |
| 99 | stages | Workflow stages (01-11) |

<!-- section_id: "d6282103-06ce-4948-bcdb-efbd90231b35" -->
## Files

- `layer_registry.yaml` - Complete registry definition

<!-- section_id: "7c5a9f4f-9b8c-49f0-88f0-23f832253ac4" -->
## Usage

When creating a new layer (project, feature, component), use this structure:

```
layer_N_entity_name/
├── CLAUDE.md
├── layer_1/
│   ├── layer_1_00_layer_registry/
│   ├── layer_1_01_ai_manager_system/
│   ├── layer_1_02_manager_handoff_documents/
│   ├── layer_1_03_sub_layers/
│   └── layer_1_99_stages/
└── layer_2/layer_2_features/
```
