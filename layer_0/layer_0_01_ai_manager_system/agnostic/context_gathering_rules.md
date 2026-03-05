---
resource_id: "14988064-1fb8-442d-b8ed-8b5a23c581c7"
resource_type: "document"
resource_name: "context_gathering_rules"
---
# Context Gathering Rules

<!-- section_id: "5385ce25-e7d0-4ed4-af29-006b949e4c50" -->
## Overview
This document defines the rules for gathering context in the Layer-Stage Framework.

<!-- section_id: "e9b42cf9-0a80-4690-abc3-c8365d45bc75" -->
## Vertical Chain (Always Required)
The vertical chain consists of ancestors and descendants:
- **Ancestors**: All layers above the current position (toward Layer 0)
- **Descendants**: All layers below the current position (toward leaf nodes)

The vertical chain is ALWAYS relevant and should be gathered automatically.

<!-- section_id: "ffe208c2-899d-49ac-9893-6960dc0826ad" -->
## Horizontal Context (Task-Relevant)
Siblings at the same layer level are only gathered when:
- The task explicitly references them
- Cross-feature dependencies exist
- Shared components are being modified

<!-- section_id: "088ac4a7-d15e-48e5-a486-2f0ccc4b0cec" -->
## Context Priority
1. Current layer's init_prompt.md
2. Current layer's stage-specific context
3. Ancestor init_prompt.md chain (up to Layer 0)
4. Descendant context (if working on parent task)
5. Sibling context (only when task-relevant)

<!-- section_id: "29796d1a-ad4d-4e0f-b5ef-f250a0a4574c" -->
## File Reading Order
1. `layer_N_00_ai_manager_system/agnostic/init_prompt.md`
2. `layer_N_00_ai_manager_system/specific/` (environment-specific config)
3. `layer_N_01_manager_handoff_documents/` (handoff context)
4. `layer_N_02_sub_layers/` (relevant sub-layer content)
5. `layer_N_99_stages/` (current stage context)

<!-- section_id: "d323c502-befb-44a8-bc37-f4e49ab2f29a" -->
## Skip Conditions
- Do NOT gather archived stages (stage_N.09_archives)
- Do NOT gather sibling layers unless explicitly needed
- Do NOT recursively read all files - use init_prompts as entry points
