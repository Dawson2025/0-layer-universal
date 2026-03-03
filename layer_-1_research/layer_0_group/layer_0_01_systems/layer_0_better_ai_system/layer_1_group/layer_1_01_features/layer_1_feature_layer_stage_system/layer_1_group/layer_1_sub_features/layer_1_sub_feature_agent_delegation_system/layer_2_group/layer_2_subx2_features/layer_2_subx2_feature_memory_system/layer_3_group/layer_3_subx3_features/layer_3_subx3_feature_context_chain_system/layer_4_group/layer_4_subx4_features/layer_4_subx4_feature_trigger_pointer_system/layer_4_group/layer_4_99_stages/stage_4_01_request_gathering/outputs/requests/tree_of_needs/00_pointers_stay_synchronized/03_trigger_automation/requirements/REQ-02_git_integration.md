# REQ-02: Git Integration Triggers

**Need**: [Trigger Automation](../README.md)

## Requirements

- **SHOULD** provide a git post-commit hook that detects directory renames/moves
- **SHOULD** automatically run `pointer-sync.sh` when git detects file path changes
- **MUST** detect when `git mv` operations affect directories containing pointer targets
- **SHOULD** integrate with `agnostic-sync.sh` so pointer validation runs as part of the sync chain
- **MUST NOT** prevent git operations from completing if pointer-sync fails
- **MAY** provide a pre-push hook that validates all pointers before allowing push
