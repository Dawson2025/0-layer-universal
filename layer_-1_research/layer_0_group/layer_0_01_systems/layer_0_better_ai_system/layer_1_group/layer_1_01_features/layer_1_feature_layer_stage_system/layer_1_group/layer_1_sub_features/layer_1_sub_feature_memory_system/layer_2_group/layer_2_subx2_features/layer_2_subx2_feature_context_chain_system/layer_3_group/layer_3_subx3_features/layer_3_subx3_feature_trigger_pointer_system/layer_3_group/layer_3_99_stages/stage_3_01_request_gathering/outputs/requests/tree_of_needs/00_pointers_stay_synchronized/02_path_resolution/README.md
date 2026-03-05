---
resource_id: "065f6299-baea-45a1-9d7f-6a45cbe2be24"
resource_type: "readme
output"
resource_name: "README"
---
# Branch 02: Path Resolution

**Core Question**: How are canonical paths found?

<!-- section_id: "223061d2-3485-4dee-83e0-8b9c866533e6" -->
## Description

The pointer-sync script must dynamically locate canonical targets. This branch defines the resolution algorithm: searching by entity name, navigating to stages, and computing portable relative paths.

<!-- section_id: "a16559ce-d19b-47eb-ad45-8e8ea8d5c1fe" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| need_01_entity_search | How do we find entity directories? | `find` by name under 0_layer_universal, handle ambiguity |
| need_02_relative_path_compute | How do we compute relative paths? | Python `os.path.relpath` for reliability, handle symlinks |

<!-- section_id: "3404e6cd-c0bc-4c74-9288-dc338504fb29" -->
## Key Insight

Resolution is **entity-relative**, not path-relative. We search for the entity directory by name, so pointers survive when intermediate parent directories are renamed. Only the leaf entity directory name must stay stable.
