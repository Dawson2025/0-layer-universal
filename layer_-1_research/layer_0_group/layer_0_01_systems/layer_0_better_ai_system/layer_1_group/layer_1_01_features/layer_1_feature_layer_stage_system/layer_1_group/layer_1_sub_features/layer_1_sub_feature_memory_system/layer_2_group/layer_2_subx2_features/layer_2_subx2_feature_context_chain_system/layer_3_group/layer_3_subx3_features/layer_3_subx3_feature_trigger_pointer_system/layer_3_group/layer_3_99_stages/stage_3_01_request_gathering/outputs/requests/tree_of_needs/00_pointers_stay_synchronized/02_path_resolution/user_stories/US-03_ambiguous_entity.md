---
resource_id: "191360e5-325a-40c8-a653-3fcef9fffece"
resource_type: "output"
resource_name: "US-03_ambiguous_entity"
---
# US-03: Ambiguous Entity Name Resolution

## User Story

As a developer with multiple entities sharing similar names,
I want the pointer sync system to deterministically resolve to one entity,
so that pointer targets are predictable.

## Acceptance Criteria

1. When `find` returns multiple directories matching the entity name, the system uses the first result (`head -1`)
2. The behavior is documented: first-match-wins, ordered by filesystem traversal
3. Future enhancement: if ambiguity is detected, warn the user

## Current Behavior

The script uses `find "$ROOT" -type d -name "$CANONICAL_ENTITY" -path "*/layer_*" | head -1` which selects the first match found by filesystem traversal order. This is deterministic but not user-controllable.

## Open Question

Should the system detect ambiguity (multiple matches) and warn? Currently it silently picks the first match. A `--verbose` flag shows which directory was selected, but there's no explicit ambiguity warning.
