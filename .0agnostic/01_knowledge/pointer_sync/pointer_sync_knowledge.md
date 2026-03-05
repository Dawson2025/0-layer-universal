---
resource_id: "e3bf770d-abeb-41d8-a558-87d6e27d605f"
resource_type: "knowledge"
resource_name: "pointer_sync_knowledge"
---
# Pointer Sync System — Knowledge

## What It Is

The pointer sync system keeps pointer files synchronized with their canonical content locations. When directories are moved or renamed, the system detects stale paths and updates them automatically.

## Components

| Component | Location | Purpose |
|-----------|----------|---------|
| `pointer-sync.sh` | `.0agnostic/pointer-sync.sh` | Main sync script — finds, resolves, updates pointers |
| Protocol | `.0agnostic/03_protocols/pointer_sync_protocol.md` | Step-by-step usage guide |
| Rule | `.0agnostic/02_rules/static/pointer_sync_rule/` | Always-apply rule for pointer file format |
| Hook (pointer) | `.0agnostic/06_.../08_hooks/scripts/pointer-edit-guard.sh` | Reminds agents to validate after editing pointers |
| Hook (config) | `.claude/settings.json` | Registers the hook with Claude Code |

## How Pointers Work

Pointer files use **YAML frontmatter** to declare what they point to:

```yaml
---
pointer_to: tree_of_needs_04_data_based
canonical_entity: context_chain_system
canonical_stage: stage_3_01_request_gathering
canonical_subpath: outputs/requests/tree_of_needs/00_context_survives_boundaries/04_data_based_avenue_comparison
---
```

The script uses these fields to:
1. **Find** the entity directory by name (`find ... -name "$canonical_entity"`)
2. **Navigate** to the stage within it (if `canonical_stage` is set)
3. **Append** the subpath (if `canonical_subpath` is set)
4. **Compute** a relative path from the pointer to the canonical location
5. **Update** the `> **Canonical location**:` line in the pointer body

## Relationship to Existing Systems

- **Deduplication pattern**: Pointer files ARE the deduplication mechanism. This system automates their maintenance.
- **agnostic-sync.sh**: Pointer validation runs at the end of agnostic-sync. Broken pointers produce warnings.
- **Claude Code hooks**: The `pointer-edit-guard.sh` hook fires after any Edit/Write on a pointer file, reminding the agent to validate.

## Key Design Decisions

1. **Frontmatter-based identification**: Pointers self-declare via `pointer_to:` field. No external registry needed.
2. **Entity-relative resolution**: Uses `find` to locate entity directories by name. This means pointers survive when parent directories change — only the entity itself needs to keep its name.
3. **Relative paths in body**: The displayed path is relative (not absolute), following existing conventions.
4. **Non-destructive**: The script only modifies the `> **Canonical location**:` line. All other content in the pointer is preserved.
5. **Validation mode**: `--validate` exits non-zero on broken pointers, suitable for CI or pre-commit checks.
