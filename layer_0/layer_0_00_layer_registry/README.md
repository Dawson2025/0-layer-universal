# Layer Registry

This directory contains the registry and metadata for layer internal structure.

## Purpose

Defines the standard components that exist within each layer:

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Metadata for this layer |
| 01 | ai_manager_system | AI agent configuration |
| 02 | manager_handoff_documents | Session transitions |
| 03 | sub_layers | Knowledge, prompts, rules, setup |
| 99 | stages | Workflow stages (01-11) |

## Files

- `layer_registry.yaml` - Complete registry definition

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
