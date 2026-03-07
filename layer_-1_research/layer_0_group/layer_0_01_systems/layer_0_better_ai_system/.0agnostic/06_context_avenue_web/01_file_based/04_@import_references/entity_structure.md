---
resource_id: "42097639-800c-4e95-a86c-650d54ec8e6e"
resource_type: "knowledge"
resource_name: "entity_structure_bridge"
---
# Entity Structure Compatibility Bridge

This project-local file is a compatibility bridge.

The canonical entity structure file is the root-level universal reference:

`/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`

Use that file as the source of truth.

## Why This Bridge Exists

Older documents inside `better_ai_system` refer to a local `.0agnostic/.../entity_structure.md` path.
Keeping this bridge preserves those references while making the root-level `0_layer_universal` path authoritative.

## If You Are Creating Or Updating Entities

1. Read the root canonical file above.
2. Follow its linked lifecycle docs for templates and maintenance.
3. Treat this local file as informational only, not the source of truth.
