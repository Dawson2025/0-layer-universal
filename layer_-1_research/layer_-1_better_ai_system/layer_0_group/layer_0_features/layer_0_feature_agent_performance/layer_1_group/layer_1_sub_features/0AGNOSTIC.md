# Layer 1 Sub-Features Registry

## Identity

| Field | Value |
|-------|-------|
| Name | Layer 1 Sub Features |
| Type | Sub-Features Registry |
| Layer | 1 |
| Parent | `../ (layer_0_feature_agent_performance)` |

## Description

Container for layer 1 sub_features within **layer_0_feature_agent_performance**.

## Children


- layer_1_sub_feature_aalang
- layer_1_sub_feature_knowledge_and_memory
- layer_1_sub_feature_organization
- layer_1_sub_feature_performance_at_scale
- layer_1_sub_feature_tooling

## Conventions

- Child naming: `layer_1_{type}_{name}`
- Each child follows canonical entity structure (`@imports/entity_structure.md`)

## Triggers

| Situation | Action |
|-----------|--------|
| Creating new child | Load `@imports/entity_structure.md`, use `/entity-creation` skill |
