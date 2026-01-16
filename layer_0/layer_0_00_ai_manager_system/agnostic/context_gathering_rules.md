# Context Gathering Rules

## Overview
This document defines the rules for gathering context in the Layer-Stage Framework.

## Vertical Chain (Always Required)
The vertical chain consists of ancestors and descendants:
- **Ancestors**: All layers above the current position (toward Layer 0)
- **Descendants**: All layers below the current position (toward leaf nodes)

The vertical chain is ALWAYS relevant and should be gathered automatically.

## Horizontal Context (Task-Relevant)
Siblings at the same layer level are only gathered when:
- The task explicitly references them
- Cross-feature dependencies exist
- Shared components are being modified

## Context Priority
1. Current layer's init_prompt.md
2. Current layer's stage-specific context
3. Ancestor init_prompt.md chain (up to Layer 0)
4. Descendant context (if working on parent task)
5. Sibling context (only when task-relevant)

## File Reading Order
1. `layer_N_00_ai_manager_system/agnostic/init_prompt.md`
2. `layer_N_00_ai_manager_system/specific/` (environment-specific config)
3. `layer_N_01_manager_handoff_documents/` (handoff context)
4. `layer_N_02_sub_layers/` (relevant sub-layer content)
5. `layer_N_99_stages/` (current stage context)

## Skip Conditions
- Do NOT gather archived stages (stage_N.09_archives)
- Do NOT gather sibling layers unless explicitly needed
- Do NOT recursively read all files - use init_prompts as entry points
