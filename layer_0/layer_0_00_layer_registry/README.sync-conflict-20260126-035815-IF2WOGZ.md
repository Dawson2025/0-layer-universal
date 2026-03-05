---
resource_id: "8dd4672a-f9fd-49cc-90c7-c3e82d88bb21"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035815-IF2WOGZ"
---
# Layer Registry

This directory contains the registry and metadata for layer internal structure.

<!-- section_id: "ec88f3f5-e481-4bed-b232-27f63fb5dac3" -->
## Purpose

Defines the standard components that exist within each layer:

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Metadata for this layer |
| 01 | ai_manager_system | AI agent configuration |
| 02 | manager_handoff_documents | Session transitions |
| 03 | sub_layers | Knowledge, prompts, rules, setup |
| 99 | stages | Workflow stages (01-11) |

<!-- section_id: "67715a37-4107-4e93-aec8-9b7afa0233fe" -->
## Files

- `layer_registry.yaml` - Complete registry definition

<!-- section_id: "970de97b-2d82-4581-a96a-575e6752a1a5" -->
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
