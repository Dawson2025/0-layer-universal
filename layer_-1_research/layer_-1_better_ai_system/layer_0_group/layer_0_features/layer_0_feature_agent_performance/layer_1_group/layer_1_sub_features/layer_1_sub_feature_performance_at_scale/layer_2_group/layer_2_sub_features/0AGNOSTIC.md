# Layer 2 Sub-Features Registry

## Identity

| Field | Value |
|-------|-------|
| Name | Layer 2 Sub Features |
| Type | Sub-Features Registry |
| Layer | 2 |
| Parent | `../ (layer_1_sub_feature_performance_at_scale)` |

## Description

Container for layer 2 sub_features within **layer_1_sub_feature_performance_at_scale**.

## Children


- layer_2_sub_feature_agent_hierarchy
- layer_2_sub_feature_automation
- layer_2_sub_feature_orchestration

## Conventions

- Child naming: `layer_2_{type}_{name}`
- Each child follows canonical entity structure (`@imports/entity_structure.md`)

## Triggers

| Situation | Action |
|-----------|--------|
| Creating new child | Load `@imports/entity_structure.md`, use `/entity-creation` skill |
