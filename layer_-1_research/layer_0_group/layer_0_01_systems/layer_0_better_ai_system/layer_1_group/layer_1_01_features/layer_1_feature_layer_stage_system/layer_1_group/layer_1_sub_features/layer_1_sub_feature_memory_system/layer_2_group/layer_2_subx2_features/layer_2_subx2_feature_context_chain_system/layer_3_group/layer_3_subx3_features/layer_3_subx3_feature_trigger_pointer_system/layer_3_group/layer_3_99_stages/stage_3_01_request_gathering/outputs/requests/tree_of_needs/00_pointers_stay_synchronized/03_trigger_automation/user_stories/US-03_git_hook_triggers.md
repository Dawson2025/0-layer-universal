---
resource_id: "89f5e618-51a5-4063-b6f4-c13f73055e83"
resource_type: "output"
resource_name: "US-03_git_hook_triggers"
---
# US-03: Git Hook Triggers Pointer Sync

<!-- section_id: "bdb9d98e-be64-4e29-8295-ad5b84bd73bf" -->
## User Story

As a developer using git for version control,
I want pointer-sync.sh to run automatically on git operations (pre-commit or post-commit),
so that stale pointers are caught before they propagate to the remote repository.

<!-- section_id: "82b9089c-5083-48fa-9a2e-cf13b2c7dbe8" -->
## Acceptance Criteria

1. A git pre-commit hook runs `pointer-sync.sh --validate`
2. If any pointer is broken or stale, the commit is blocked with a clear error message
3. The hook can be installed via a setup script or git template
4. The hook runs quickly (< 2 seconds for typical repos)

<!-- section_id: "00debf5c-c241-481f-ab8c-69eaf985ae0a" -->
## Integration with Existing Hooks

The editing tool's notification system already triggers warnings when pointer files are edited. The git hook provides a second safety net at commit time.

> **Design note**: The specific notification mechanism (e.g., Claude Code PostToolUse hooks, Cursor rules, VS Code file watchers) is documented in stage 04 design outputs.

<!-- section_id: "5f72e2f5-6f90-4166-b1f7-33929ddfb7fa" -->
## Status

REQ-02 (git_integration) defines the requirement. This user story captures the developer experience.
