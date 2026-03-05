---
resource_id: "065f6299-baea-45a1-9d7f-6a45cbe2be24"
resource_type: "readme
output"
resource_name: "README"
---
# Branch 02: Path Resolution

**Core Question**: How are canonical paths found?

## Description

The pointer-sync script must dynamically locate canonical targets. This branch defines the resolution algorithm: searching by entity name, navigating to stages, and computing portable relative paths.

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| need_01_entity_search | How do we find entity directories? | `find` by name under 0_layer_universal, handle ambiguity |
| need_02_relative_path_compute | How do we compute relative paths? | Python `os.path.relpath` for reliability, handle symlinks |

## Key Insight

Resolution is **entity-relative**, not path-relative. We search for the entity directory by name, so pointers survive when intermediate parent directories are renamed. Only the leaf entity directory name must stay stable.
