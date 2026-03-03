# Pointer Sync Rule

**Type**: Static (always applies) | **Scope**: All agents

## Rule

When creating or modifying a pointer file:

1. **MUST** include YAML frontmatter with `pointer_to:` and `canonical_entity:` fields
2. **MUST** include a `> **Canonical location**:` line in the body
3. **MUST** run `pointer-sync.sh --validate` after creation or modification
4. **MUST NOT** hardcode absolute paths in pointer files
5. **MUST NOT** manually compute relative paths — let `pointer-sync.sh` handle it

## Pointer File Template

```markdown
---
pointer_to: logical_id
canonical_entity: entity_directory_name
canonical_stage: stage_N_NN_name        # optional
canonical_subpath: path/within/stage    # optional
---
# [Title] — Pointer

> **Canonical location**: `[AUTO-UPDATED by pointer-sync.sh]`

Brief description of what this points to.

Do not duplicate content here — read the canonical location instead.
```

## When This Rule Applies

- Creating a new pointer file (instead of duplicating content)
- Editing an existing pointer file's frontmatter
- Moving or renaming directories that contain pointer targets
- Running `agnostic-sync.sh` (which includes pointer validation)

## References

- Protocol: `.0agnostic/03_protocols/pointer_sync_protocol.md`
- Knowledge: `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md`
- Script: `.0agnostic/pointer-sync.sh`
