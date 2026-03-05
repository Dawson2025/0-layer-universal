---
resource_id: "832cec4d-5b30-4cb8-b1f1-cff5ad024b4d"
resource_type: "document"
resource_name: "agnostic"
---
# layer_0 - Agnostic Context

<!-- section_id: "62c72c90-bb40-4626-9a18-af99c5a02301" -->
## Purpose

Tool-agnostic context for the universal layer.

<!-- section_id: "0ce806aa-f2d5-49e1-b291-813be312c85e" -->
## Scope

Layer 0 contains content that applies to ALL other layers:
- Universal rules
- Universal prompts
- Universal knowledge
- Universal principles
- Universal setup patterns

<!-- section_id: "fabb220b-7d81-4817-9fb8-a909619a55f6" -->
## Structure

```
layer_0/
├── layer_0_00_layer_registry/    Layer metadata
├── layer_0_01_ai_manager_system/ AI manager configs
│   ├── agnostic/                 Tool-agnostic prompts
│   └── specific/                 Tool-specific configs
├── layer_0_02_manager_handoff_documents/
├── layer_0_04_sub_layers/        Universal content types
│   ├── sub_layer_0_01_knowledge_system/  (incl. principles/)
│   ├── sub_layer_0_02_rules/             (static/ + dynamic/)
│   ├── sub_layer_0_03_protocols/
│   └── sub_layer_0_04+_setup_dependant/
└── layer_0_99_stages/            Universal stage templates
```

<!-- section_id: "b812667b-d510-42e2-89c7-422e8d5c93a0" -->
## Key Content

| Location | Content |
|----------|---------|
| `sub_layer_0_01_knowledge_system/` | Domain knowledge (incl. principles/) |
| `sub_layer_0_02_rules/` | Universal rules (static/ always-on, dynamic/ trigger-based) |
| `sub_layer_0_03_protocols/` | Session init, context protocols |
| `layer_0_99_stages/` | Stage workflow templates |

<!-- section_id: "2c19a323-bb42-446a-9747-73154dfc6b94" -->
## Inheritance

All other layers inherit from layer_0:
- Layer 1 projects inherit layer_0 rules
- Layer -1 research inherits layer_0 rules
- Nested layers inherit from their parents + layer_0
