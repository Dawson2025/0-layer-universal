# Layer Navigation

## Overview
This document explains how to navigate the Layer-Stage Framework structure.

## Layer Hierarchy
```
Layer 0 (Universal)
  +-- Layer 1 (Projects)
        +-- Layer 2 (Features)
              +-- Layer 3 (Components)
                    +-- Layer 4+ (Sub-components)
```

## Directory Structure Pattern
Each layer follows this pattern:
```
layer_N/
  +-- layer_N_00_ai_manager_system/
  |     +-- agnostic/           # Universal config for this layer
  |     +-- specific/           # Environment-specific config
  +-- layer_N_01_manager_handoff_documents/
  |     +-- layer_N_00_to_universal/
  |     +-- layer_N_01_to_specific/
  +-- layer_N_02_sub_layers/
  |     +-- sub_layer_N_01_prompts/
  |     +-- sub_layer_N_02_knowledge_system/
  |     +-- sub_layer_N_03_principles/
  |     +-- sub_layer_N_04_rules/
  |     +-- sub_layer_N_05+_setup_dependant/
  +-- layer_N_99_stages/
        +-- status_N.json
```

## Navigation Commands
- `/layer-status`: Show current position in hierarchy
- `/layer-up`: Move to parent layer
- `/layer-down <child>`: Move to child layer
- `/layer-root`: Return to Layer 0

## Finding Context
1. Identify your current layer position
2. Read the init_prompt.md chain from current to Layer 0
3. Check stage status to determine workflow phase
4. Gather relevant sub-layer content based on task

## Cross-Layer References
When referencing content in other layers:
- Use absolute paths from repository root
- Prefer symlinks or references over duplication
- Document dependencies in handoff documents
