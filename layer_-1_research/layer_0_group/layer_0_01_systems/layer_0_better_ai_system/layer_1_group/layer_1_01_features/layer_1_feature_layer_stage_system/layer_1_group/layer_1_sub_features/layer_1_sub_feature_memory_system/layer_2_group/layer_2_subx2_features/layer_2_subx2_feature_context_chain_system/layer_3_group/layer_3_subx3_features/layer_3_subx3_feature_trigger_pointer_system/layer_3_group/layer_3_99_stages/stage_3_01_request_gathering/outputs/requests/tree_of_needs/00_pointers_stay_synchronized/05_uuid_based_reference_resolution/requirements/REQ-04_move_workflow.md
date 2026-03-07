---
resource_id: "6d7e8f9a-0b1c-4d2e-3f4a-5b6c7d8e9f0a"
resource_type: "output"
resource_name: "REQ-04_move_workflow"
---
# REQ-04: Trivial Move Workflow

**Need**: [UUID-Based Reference Resolution](../README.md)

<!-- section_id: "7e8f9a0b-1c2d-4e3f-4a5b-6c7d8e9f0a1b" -->
## Requirements

- **MUST** reduce the move workflow to: `mv` → `pointer-sync.sh --rebuild-index` → commit
- **MUST NOT** require manual grep-and-replace across documentation files after a move
- **MUST NOT** require manual updates to script-to-script call paths after a move
- **MUST NOT** require manual updates to git hook paths after a move
- **MUST NOT** require manual updates to 0AGNOSTIC.md resource tables after a move (UUID references stay valid)
- **SHOULD** auto-rebuild the UUID index via git hooks (post-checkout, post-merge) so even the manual `rebuild-index` step is eliminated for common operations
- **SHOULD** provide a pre-commit hook that validates all UUID references resolve to existing paths, catching broken references before they're committed
- **MUST** support moving: individual files, directories, entities (entire subtrees), stages
- **MUST** support renaming: files, directories, entities
- **MUST** handle the bootstrapping problem: the `resolve-uuid` function itself is found via `git rev-parse --show-toplevel` (the one hardcoded path in the system)
