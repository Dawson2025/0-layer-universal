---
resource_id: "8f11590f-7c3f-4457-9c73-2eba2942f644"
resource_type: "readme
document"
resource_name: "README"
---
cl# layer_0 (Layer 0) – Operational Overlay

This overlay maps existing universal content into the Layer/Stage system without moving files. Each slot links to current sources. Use these paths when loading context.

## Manager and handoff
- layer_0_01_ai_manager_system → `./layer_0_01_ai_manager_system/` (manager docs/configs)
- layer_0_02_manager_handoff_documents → `./layer_0_02_manager_handoff_documents/` with `layer_0_00_to_universal/` and `layer_0_01_to_specific/`

## Slots (inside `layer_0_04_sub_layers/`)
- sub_layer_0_01_knowledge_system → `./layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/` (incl. principles/)
- sub_layer_0_02_rules → `./layer_0_04_sub_layers/sub_layer_0_02_rules/` (static/ + dynamic/)
- sub_layer_0_03_protocols → `./layer_0_04_sub_layers/sub_layer_0_03_protocols/`
- sub_layer_0_04+_setup_dependant → `./layer_0_04_sub_layers/sub_layer_0_04+_setup_dependant/` (OS, environments, apps, tools)
- layer_0_99_stages → stage folders + status for this layer

## How to use
- Load context via these mapped paths; do not move existing files.
- Add new docs inside these slots as needed; keep pointers updated.
- Track stage status in `layer_0_99_stages/status.json`.
