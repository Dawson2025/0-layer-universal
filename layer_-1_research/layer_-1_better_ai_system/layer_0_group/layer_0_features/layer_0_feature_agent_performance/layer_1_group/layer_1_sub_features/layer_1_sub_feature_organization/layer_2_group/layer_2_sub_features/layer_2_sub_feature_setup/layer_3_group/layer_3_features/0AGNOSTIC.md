# Layer 3 Features Registry

## Identity

| Field | Value |
|-------|-------|
| Name | Layer 3 Features |
| Type | Features Registry |
| Layer | 3 |
| Parent | `../ (layer_2_sub_feature_setup)` |

## Description

Container for layer 3 features within **layer_2_sub_feature_setup**.

## Children


- layer_3_feature_multi_os_system

## Conventions

- Child naming: `layer_3_{type}_{name}`
- Each child follows canonical entity structure (`@imports/entity_structure.md`)

## Triggers

| Situation | Action |
|-----------|--------|
| Creating new child | Load `@imports/entity_structure.md`, use `/entity-creation` skill |
