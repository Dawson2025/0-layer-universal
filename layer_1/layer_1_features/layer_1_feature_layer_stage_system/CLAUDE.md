# layer_1_feature_layer_stage_system

## Overview
This feature IS the Layer-Stage Framework itself. It defines the patterns that all other entities follow.

## Purpose
- Define stage workflows (00-09)
- Define layer hierarchy patterns
- Define context gathering rules
- Define handoff system
- Define AI manager hierarchy

## Structure
- `layer_1/` - Framework's internal workings
- `layer_2/` - Child features that define specific concepts

## Child Features (in layer_2/layer_2_features/)
- `layer_2_feature_stage_definitions/` - Defines the 9 stages
- `layer_2_feature_layer_definitions/` - Defines layer numbering and nesting
- `layer_2_feature_context_gathering/` - Defines how AI gathers context
- `layer_2_feature_handoff_system/` - Defines handoff patterns
- `layer_2_feature_ai_manager_hierarchy/` - Defines agnostic/specific pattern

## Commands
- `/framework-status` - Show framework development status
