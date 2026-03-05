---
resource_id: "e2c7fbaf-105d-4203-b962-91a9576ba13a"
resource_type: "document"
resource_name: "init_prompt"
---
# Layer 0: Universal

<!-- section_id: "a0f8ebbd-e682-42e8-9658-8cff6487de26" -->
## Inherited From
- None (this is the root)

<!-- section_id: "883592e7-cc7c-4fa0-8517-bea08a986981" -->
## Purpose
Universal root of the Layer-Stage Framework. All projects, features, and components are nested here.

<!-- section_id: "cdb6612b-0576-41ac-907c-8ffca7045cea" -->
## Context Rules
- This is always in the vertical chain
- All descendants inherit from this
- Universal skills, commands, agents available everywhere

<!-- section_id: "878f21c6-76eb-4c4e-a149-5739ae55564d" -->
## Conventions
- Layer numbering: N_XX_name
- Sub-layers: 01_prompts through 05+_setup_dependant
- Stages: 00_request_gathering through 09_archives

<!-- section_id: "588a204d-f30f-4a14-815c-d64375977abf" -->
## Children
- layer_1/layer_1_projects/ - Project repositories
- layer_1/layer_1_features/ - Universal features
- layer_1/layer_1_components/ - Shared components
