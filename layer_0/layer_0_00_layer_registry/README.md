---
resource_id: "542e9c9d-e604-4df1-b615-e8f8bdf3137e"
resource_type: "readme
document"
resource_name: "README"
---
# Layer Registry

This directory contains the registry and metadata for layer internal structure.

<!-- section_id: "80e3e363-a434-44f9-8dfa-783c0aad27b4" -->
## Purpose

Defines the standard components that exist within each layer:

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Metadata for this layer |
| 01 | ai_manager_system | AI agent configuration |
| 02 | manager_handoff_documents | Session transitions |
| 03 | sub_layers | Knowledge, prompts, rules, setup |
| 99 | stages | Workflow stages (01-11) |

<!-- section_id: "85c9671a-7d21-44c5-859c-e74f1895c444" -->
## Files

- `layer_registry.yaml` - Complete registry definition

<!-- section_id: "57ad700c-4394-498d-8c99-a6fa21e110f5" -->
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
