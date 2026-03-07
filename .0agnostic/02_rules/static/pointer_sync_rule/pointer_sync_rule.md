---
resource_id: "431bfad1-8f7d-46c7-857c-0ef13769d6e5"
resource_type: "rule"
resource_name: "pointer_sync_rule"
---
# Pointer Sync Rule

**Type**: Static (always applies) | **Scope**: All agents

<!-- section_id: "5b0f851f-4164-459c-a18c-b1566b0289f8" -->
## Rule

When creating or modifying a pointer file:

1. **MUST** include YAML frontmatter with `pointer_to:` and `canonical_entity:` fields
2. **MUST** include `canonical_entity_id:` with the target entity's UUID
3. **MUST** include `canonical_stage_id:` if `canonical_stage:` is set
4. **MUST** include a `> **Canonical location**:` line in the body
5. **MUST** run `pointer-sync.sh --validate` after creation or modification
6. **MUST NOT** hardcode absolute paths in pointer files
7. **MUST NOT** manually compute relative paths — let `pointer-sync.sh` handle it

<!-- section_id: "d45fbe31-808d-4bde-9e5a-5a7f61fb63e7" -->
## Pointer File Template

```markdown
---
pointer_to: logical_id
canonical_entity: entity_directory_name
canonical_entity_id: "uuid-from-uuid-index"
canonical_stage: stage_N_NN_name        # optional
canonical_stage_id: "uuid-from-stage-index"  # required if canonical_stage is set
canonical_subpath: path/within/stage    # optional
---
# [Title] — Pointer

> **Canonical location**: `[AUTO-UPDATED by pointer-sync.sh]`

Brief description of what this points to.

Do not duplicate content here — read the canonical location instead.
```

<!-- section_id: "3eea5273-36f6-43bd-b5a4-c4433780393f" -->
## When This Rule Applies

- Creating a new pointer file (instead of duplicating content)
- Editing an existing pointer file's frontmatter
- Moving or renaming directories that contain pointer targets
- Running `agnostic-sync.sh` (which includes pointer validation)

<!-- section_id: "a93b9c17-242e-47c3-b20c-0efe11b34036" -->
## References

- Protocol: `.0agnostic/03_protocols/pointer_sync_protocol/pointer_sync_protocol.md`
- Knowledge: `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md`
- Script: `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh`
