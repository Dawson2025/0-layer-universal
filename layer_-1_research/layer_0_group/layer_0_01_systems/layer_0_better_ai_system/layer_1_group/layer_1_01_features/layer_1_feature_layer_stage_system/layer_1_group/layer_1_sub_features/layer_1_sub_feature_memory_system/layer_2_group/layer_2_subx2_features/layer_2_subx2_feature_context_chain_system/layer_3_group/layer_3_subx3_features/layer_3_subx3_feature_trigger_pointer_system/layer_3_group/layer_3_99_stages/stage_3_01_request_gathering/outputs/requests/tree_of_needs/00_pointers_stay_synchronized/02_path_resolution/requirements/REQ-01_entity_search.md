---
resource_id: "6bc2da16-8fdd-44eb-b7c0-9ee783a3ca5a"
resource_type: "output"
resource_name: "REQ-01_entity_search"
---
# REQ-01: Entity Search Algorithm

**Need**: [Path Resolution](../README.md)

<!-- section_id: "d823aad4-3042-4de9-b79f-e8b69190868c" -->
## Requirements

- **MUST** locate entity directories by name; implementation may use filesystem search, indexing, or other mechanisms
- **MUST** handle case where multiple directories match (resolve deterministically)
- **MUST** report BROKEN if entity not found
- **MUST** optionally navigate to a stage within the entity (`canonical_stage`)
- **MUST** optionally append a subpath within the stage (`canonical_subpath`)
- **MUST** verify the final resolved path exists before updating
- **MUST** compute relative path from pointer file's directory to canonical target
- **MUST** tolerate both Unix and Windows line endings in pointer files

> **Design note**: The specific search mechanism (e.g., `find`, UUID index lookup, TSV grep) is documented in stage 04 design outputs.
