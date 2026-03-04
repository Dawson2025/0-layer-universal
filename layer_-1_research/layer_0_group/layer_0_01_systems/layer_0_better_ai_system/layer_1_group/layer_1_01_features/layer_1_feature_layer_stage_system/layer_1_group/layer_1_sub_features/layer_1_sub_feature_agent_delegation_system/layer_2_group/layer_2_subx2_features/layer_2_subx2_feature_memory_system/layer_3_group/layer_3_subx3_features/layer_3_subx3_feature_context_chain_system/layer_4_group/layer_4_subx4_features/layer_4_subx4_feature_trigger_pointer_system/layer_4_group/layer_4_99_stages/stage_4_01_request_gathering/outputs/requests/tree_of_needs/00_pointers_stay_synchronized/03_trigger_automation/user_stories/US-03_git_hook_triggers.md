# US-03: Git Hook Triggers Pointer Sync

## User Story

As a developer using git for version control,
I want pointer-sync.sh to run automatically on git operations (pre-commit or post-commit),
so that stale pointers are caught before they propagate to the remote repository.

## Acceptance Criteria

1. A git pre-commit hook runs `pointer-sync.sh --validate`
2. If any pointer is broken or stale, the commit is blocked with a clear error message
3. The hook can be installed via a setup script or git template
4. The hook runs quickly (< 2 seconds for typical repos)

## Integration with Existing Hooks

The Claude Code PostToolUse hook (`pointer-edit-guard.sh`) already triggers warnings when pointer files are edited. The git hook provides a second safety net at commit time.

## Status

REQ-02 (git_integration) defines the requirement. This user story captures the developer experience.
