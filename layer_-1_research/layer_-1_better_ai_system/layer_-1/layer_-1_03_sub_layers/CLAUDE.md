# layer_-1_03_sub_layers

## Role

**Sub_layers Manager** - Manages sub_layers for the better_ai_system research project.

## Responsibilities

- Manage project-specific prompts, knowledge, principles, rules, and setup
- Delegate tasks to appropriate sub_layer
- Aggregate results from sub_layers
- Handle escalations from sub_layers
- Maintain sub_layer registry

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from layer_-1
2. Check `hand_off_documents/incoming/from_below/` for results/escalations from sub_layers
3. Process pending work or delegate to appropriate sub_layer

## Children (Project Sub_layers)

| Number | Name | Purpose |
|--------|------|---------|
| 00 | sub_layer_registry | Sub_layer definitions and metadata (data only) |
| 01 | prompts | Project-specific prompts |
| 02 | knowledge_system | Project-specific knowledge |
| 03 | principles | Project-specific principles |
| 04 | rules | Project-specific rules |
| 05+ | setup_dependant | Project-specific setup |

## Navigation

- **Parent**: `../` (layer_-1 of better_ai_system)
- **Registry**: `sub_layer_-1_00_sub_layer_registry/`
