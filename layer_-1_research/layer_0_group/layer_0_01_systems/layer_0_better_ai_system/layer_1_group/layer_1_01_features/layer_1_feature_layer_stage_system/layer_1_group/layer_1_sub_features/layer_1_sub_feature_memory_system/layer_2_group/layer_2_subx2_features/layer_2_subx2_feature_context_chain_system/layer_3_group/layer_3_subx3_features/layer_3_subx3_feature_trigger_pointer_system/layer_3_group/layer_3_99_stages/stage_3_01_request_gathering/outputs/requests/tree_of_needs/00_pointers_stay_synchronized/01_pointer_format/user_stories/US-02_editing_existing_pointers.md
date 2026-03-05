---
resource_id: "755f2426-c4de-44f0-9777-547a61628b13"
resource_type: "output"
resource_name: "US-02_editing_existing_pointers"
---
# US-02: Editing Existing Pointers

<!-- section_id: "67c3c894-e28f-4362-bd30-d02f73ea66a3" -->
## User Story

As a developer maintaining the layer-stage system,
I want to be able to change the `pointer_to` or `canonical_entity` fields of an existing pointer file,
so that I can retarget a pointer to a different canonical location without recreating the file.

<!-- section_id: "f7d3fcd1-3374-4db9-8a03-27ac302608c7" -->
## Acceptance Criteria

1. After editing the `canonical_entity` field to a new valid entity, running `pointer-sync.sh` updates the `> **Canonical location**:` line to reflect the new target
2. After editing the `pointer_to` field (description), the sync still operates correctly
3. Changing `canonical_stage` or `canonical_subpath` also resolves correctly after sync
4. If the new entity doesn't exist, `--validate` reports BROKEN

<!-- section_id: "6d30fd86-e993-409f-b704-c7e83f647b0e" -->
## Test Coverage

- Test 5.1 (stale pointer → updated) validates that changed paths are corrected
- Test 3.1-3.6 (entity resolution) validates that various entity/stage/subpath combinations resolve
