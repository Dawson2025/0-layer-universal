# layer_0 - Agnostic Context

## Purpose

Tool-agnostic context for the universal layer.

## Scope

Layer 0 contains content that applies to ALL other layers:
- Universal rules
- Universal prompts
- Universal knowledge
- Universal principles
- Universal setup patterns

## Structure

```
layer_0/
├── layer_0_00_layer_registry/    Layer metadata
├── layer_0_01_ai_manager_system/ AI manager configs
│   ├── agnostic/                 Tool-agnostic prompts
│   └── specific/                 Tool-specific configs
├── layer_0_02_manager_handoff_documents/
├── layer_0_03_sub_layers/        Universal content types
│   ├── sub_layer_0_01_prompts/
│   ├── sub_layer_0_02_knowledge_system/
│   ├── sub_layer_0_03_principles/
│   ├── sub_layer_0_04_rules/
│   └── sub_layer_0_05+_setup_dependant/
└── layer_0_99_stages/            Universal stage templates
```

## Key Content

| Location | Content |
|----------|---------|
| `sub_layer_0_01_prompts/` | Session initialization |
| `sub_layer_0_04_rules/` | Universal rules (modification protocol, commit rule, safety) |
| `sub_layer_0_03_principles/` | Guiding principles |
| `layer_0_99_stages/` | Stage workflow templates |

## Inheritance

All other layers inherit from layer_0:
- Layer 1 projects inherit layer_0 rules
- Layer -1 research inherits layer_0 rules
- Nested layers inherit from their parents + layer_0
