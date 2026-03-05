---
resource_id: "d41825a9-0070-43bd-8790-f4f549e750df"
resource_type: "document"
resource_name: "layer_navigation"
---
# Layer Navigation

<!-- section_id: "73c2bec7-942e-4083-9e00-1c1d316e5b8b" -->
## Overview
This document explains how to navigate the Layer-Stage Framework structure.

<!-- section_id: "48313cb3-3287-4065-a35c-494d77fa605d" -->
## Layer Hierarchy
```
Layer 0 (Universal)
  +-- Layer 1 (Projects)
        +-- Layer 2 (Features)
              +-- Layer 3 (Components)
                    +-- Layer 4+ (Sub-components)
```

<!-- section_id: "0515394d-3a81-4c89-a42e-40c6ea86af8c" -->
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
  |     +-- sub_layer_N_01_knowledge_system/
  |     +-- sub_layer_N_02_rules/
  |     +-- sub_layer_N_04+_setup_dependant/
  +-- layer_N_99_stages/
        +-- status_N.json
```

<!-- section_id: "1c9dc533-287a-45e3-b47a-be2645f9464d" -->
## Navigation Commands
- `/layer-status`: Show current position in hierarchy
- `/layer-up`: Move to parent layer
- `/layer-down <child>`: Move to child layer
- `/layer-root`: Return to Layer 0

<!-- section_id: "0e754613-3dd3-4bd8-8a36-6137c5a20b89" -->
## Finding Context
1. Identify your current layer position
2. Read the init_prompt.md chain from current to Layer 0
3. Check stage status to determine workflow phase
4. Gather relevant sub-layer content based on task

<!-- section_id: "a0216046-76cf-40ce-a9d1-e65122df6cad" -->
## Cross-Layer References
When referencing content in other layers:
- Use absolute paths from repository root
- Prefer symlinks or references over duplication
- Document dependencies in handoff documents
