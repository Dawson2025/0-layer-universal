# REQ-01: Entity Search Algorithm

**Need**: [Path Resolution](../README.md)

## Requirements

- **MUST** find entity directories by name using `find ... -type d -name "$canonical_entity" -path "*/layer_*"`
- **MUST** handle case where multiple directories match (use first match)
- **MUST** report BROKEN if entity not found
- **MUST** optionally navigate to a stage within the entity (`canonical_stage`)
- **MUST** optionally append a subpath within the stage (`canonical_subpath`)
- **MUST** verify the final resolved path exists before updating
- **MUST** compute relative path from pointer file's directory to canonical target
- **MUST** tolerate both Unix and Windows line endings in pointer files
