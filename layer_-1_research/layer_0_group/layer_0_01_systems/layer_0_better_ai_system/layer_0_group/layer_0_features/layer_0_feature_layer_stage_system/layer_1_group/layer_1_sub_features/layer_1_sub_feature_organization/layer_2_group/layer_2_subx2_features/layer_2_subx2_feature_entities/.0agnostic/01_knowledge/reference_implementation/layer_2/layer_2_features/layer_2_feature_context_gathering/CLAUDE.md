# layer_2_feature_context_gathering

## Purpose
Defines how AI agents gather relevant context within the Layer-Stage Framework.

## Core Principle
- Vertical chain (ancestors + descendants) = ALWAYS relevant
- Horizontal siblings = ONLY when task-relevant

## Vertical Chain
1. Traverse up to find ancestor init_prompt.md files
2. Traverse down to find descendant status files
3. All are included in context

## Horizontal Siblings
Include when:
1. Sibling is RELATED to current entity (dependencies, references)
2. Relationship is RELEVANT to current task

## Task Sources
1. Current user request (highest priority)
2. status.json (in_progress tasks)
3. Handoff documents
4. Todo lists (lowest priority)

## Documentation
See `layer_2/layer_2_02_sub_layers/sub_layer_2_05+_setup_dependant/sub_layer_2_05_context_docs/`
