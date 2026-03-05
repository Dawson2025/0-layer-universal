---
resource_id: "ec7fbc06-b321-4a65-826e-0f6f8bb7aa05"
resource_type: "output"
resource_name: "US-01_auto_sync_on_move"
---
# US-01: Auto-Sync After Directory Move

**Need**: [Trigger Automation](../README.md)

---

**As a** developer who moved a parent directory,
**I want** the pointer system to automatically notice that something changed and update all pointer paths,
**So that** all pointers remain valid without me manually running anything or having an AI agent manually update everything.

### What Happens

1. Developer renames or moves a directory (e.g., via file manager, `git mv`, or IDE refactor)
2. A trigger fires automatically (git hook, Claude Code hook, or filesystem watcher)
3. The trigger invokes `pointer-sync.sh` without any manual intervention
4. Script finds all pointer files, resolves canonical paths by entity name search
5. Any stale paths are updated to reflect the new directory structure
6. Developer sees a summary log of what was updated (or a "nothing changed" confirmation)

### Acceptance Criteria

- No manual invocation required — sync happens automatically on structural changes
- All pointer paths are correct after a directory rename/move
- Developer receives a summary of updated pointers (not silent)
- AI agents do NOT need to manually fix pointer paths after their own file operations
- `pointer-sync.sh --validate` exits 0 after automatic sync completes
- System degrades gracefully if hooks are unavailable (validation still works manually)
