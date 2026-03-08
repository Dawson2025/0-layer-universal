---
resource_id: "ab7984ae-e0d9-49be-8753-c97d0e3a8f4b"
resource_type: "output"
resource_name: "US-01_directory_moves"
---
# US-01: Directory Moves, Automatic Pointer Updates

**Need**: [Path Resolution](../README.md)

---

**As a** developer who moved a parent directory,
**I want** the pointer system to automatically detect that something changed and update all pointer paths,
**So that** all pointers remain valid without me manually updating paths or requiring an AI agent to manually update everything.

<!-- section_id: "bdff8cbc-3be3-4529-aba5-5ad07a075439" -->
### What Happens

1. Developer reorganizes directory structure (e.g., renames intermediate directory)
2. The system automatically detects the structural change (via hooks, git triggers, or filesystem watchers)
3. System searches for each referenced entity by name (not by old path)
4. System finds entities at their new locations
5. System computes new relative paths from each pointer to its target
6. All affected pointer files' `> **Canonical location**:` lines are updated automatically
7. Developer is notified of what changed (summary log)

<!-- section_id: "74610c77-5cd0-48af-8a16-14f8fdcc106f" -->
### Acceptance Criteria

- Pointer resolves correctly after parent directory is renamed — no manual intervention needed
- Detection happens without manual developer intervention
- `pointer-sync.sh --validate` exits 0 after automatic sync
- Old relative paths are replaced with new computed paths
- Developer receives a summary of which pointers were updated
- AI agents editing files do NOT need to manually fix pointer paths — the system handles it
