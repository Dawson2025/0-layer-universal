# layer_0

## Role

**Layer Manager** - Universal layer that applies to ALL other layers.

## Responsibilities

- Manage universal sub_layers (prompts, knowledge, principles, rules, setup)
- Manage universal stages (workflow templates)
- Receive tasks from Root Manager via `hand_off_documents/incoming/from_above/`
- Delegate to sub_layers or stages as appropriate
- Aggregate results and report via `hand_off_documents/outgoing/to_above/`
- Handle escalations from sub_layers and stages

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from root
2. Check `hand_off_documents/incoming/from_below/` for results/escalations
3. Process pending work or await delegation

## Children

| Child | Purpose |
|-------|---------|
| `layer_0_00_layer_registry/` | Registry data (layer metadata) |
| `layer_0_01_ai_manager_system/` | AI manager configurations |
| `layer_0_02_manager_handoff_documents/` | Legacy handoff documents |
| `layer_0_03_sub_layers/` | Universal sub_layers (prompts, knowledge, principles, rules, setup) |
| `layer_0_99_stages/` | Universal stages (workflow templates) |

## Navigation

- **Parent**: `../` (0_layer_universal - Root Manager)
- **Registry**: `layer_0_00_layer_registry/`
- **Sub_layers**: `layer_0_03_sub_layers/`
- **Stages**: `layer_0_99_stages/`

## Key Locations

| Content | Path |
|---------|------|
| Universal rules | `layer_0_03_sub_layers/sub_layer_0_04_rules/` |
| Init prompts | `layer_0_03_sub_layers/sub_layer_0_01_prompts/` |
| Principles | `layer_0_03_sub_layers/sub_layer_0_03_principles/` |
| Knowledge | `layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/` |
