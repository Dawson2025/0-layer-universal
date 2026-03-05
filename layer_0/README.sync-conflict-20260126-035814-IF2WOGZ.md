---
resource_id: "1a859368-ed15-4aa2-bc55-694805e4c1a9"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035814-IF2WOGZ"
---
cl# layer_0 (Layer 0) – Operational Overlay

This overlay maps existing universal content into the Layer/Stage system without moving files. Each slot links to current sources. Use these paths when loading context.

<!-- section_id: "7f02235a-d1f3-4010-a34d-da0776693265" -->
## Manager and handoff
- layer_0_01_ai_manager_system → `./layer_0_01_ai_manager_system/` (manager docs/configs)
- layer_0_02_manager_handoff_documents → `./layer_0_02_manager_handoff_documents/` with `layer_0_00_to_universal/` and `layer_0_01_to_specific/`

<!-- section_id: "2dfc792c-fa0f-41c4-977c-5aa1277199f3" -->
## Slots (inside `layer_0_03_sub_layers/`)
- sub_layer_0_01_prompts → `./layer_0_03_sub_layers/sub_layer_0_01_prompts/`
- sub_layer_0_02_knowledge_system → `./layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/`
- sub_layer_0_03_principles → `./layer_0_03_sub_layers/sub_layer_0_03_principles/`
- sub_layer_0_04_rules → `./layer_0_03_sub_layers/sub_layer_0_04_rules/`
- sub_layer_0_05+_setup_dependant → `./layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant/` (OS, environments, apps, tools, protocols)
- layer_0_99_stages → stage folders + status for this layer

<!-- section_id: "843cf0e6-512d-4c3c-af6c-44f7aa5dacd1" -->
## How to use
- Load context via these mapped paths; do not move existing files.
- Add new docs inside these slots as needed; keep pointers updated.
- Track stage status in `layer_0_99_stages/status.json`.
