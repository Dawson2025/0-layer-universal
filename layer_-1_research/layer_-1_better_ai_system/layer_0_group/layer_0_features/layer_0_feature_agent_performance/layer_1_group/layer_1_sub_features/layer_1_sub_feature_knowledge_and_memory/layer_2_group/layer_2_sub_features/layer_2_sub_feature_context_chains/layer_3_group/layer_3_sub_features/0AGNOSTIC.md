# Layer 3 Sub-Features Registry

## Identity

| Field | Value |
|-------|-------|
| Name | Layer 3 Sub Features |
| Type | Sub-Features Registry |
| Layer | 3 |
| Parent | `../ (layer_2_sub_feature_context_chains)` |

## Description

Container for layer 3 sub_features within **layer_2_sub_feature_context_chains**.

## Children


- layer_3_sub_feature_chain_visualization
- layer_3_sub_feature_context_loading
- layer_3_sub_feature_tool_agnostic

## Conventions

- Child naming: `layer_3_{type}_{name}`
- Each child follows canonical entity structure (`@imports/entity_structure.md`)

## Triggers

| Situation | Action |
|-----------|--------|
| Creating new child | Load `@imports/entity_structure.md`, use `/entity-creation` skill |
