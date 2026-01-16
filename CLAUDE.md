# 0_layer_universal

## Overview
This is the universal root of the Layer-Stage Framework. All projects, features, and components are nested under this structure.

## Layer-Stage Framework
- **Layers**: Hierarchical depth (Layer 0 = universal, Layer 1+ = projects/features)
- **Stages**: Workflow phases (00-request_gathering through 09-archives)
- **Entities**: Projects, features, components - each follows the entity pattern

## Context Gathering Rules
- Vertical chain (ancestors + descendants) is always relevant
- Horizontal siblings only when task-relevant
- Read init_prompt chain from layer_0/layer_0_00_ai_manager_system/agnostic/

## Commands Available
- `/layer-status` - Show current layer position and status
- `/gather-context` - Gather relevant context from layer hierarchy
- `/stage-advance` - Move to next stage in workflow
- `/create-entity` - Create new project/feature/component

## Structure
- `layer_0/` - Universal framework internals
- `layer_1/` - Projects, features, components nested here

## Conventions
- Layer numbering: Layer N entities use N_XX internally
- Naming: `layer_N_XX_name` pattern (underscores, not dots)
- Sub-layers: 01_prompts, 02_knowledge_system, 03_principles, 04_rules, 05+_setup_dependant
- Stages: 00-09 (request_gathering through archives)
