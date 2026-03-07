---
resource_id: "6b7c8d9e-0f1a-4b2c-3d4e-5f6a7b8c9d0e"
resource_type: "output"
resource_name: "US-03_script_calls_by_uuid"
---
# US-03: Script Calls Other Scripts by UUID

**Need**: [UUID-Based Reference Resolution](../README.md)

---

**As a** shell script (e.g., agnostic-sync.sh) that needs to call another script (e.g., pointer-sync.sh),
**I want** to reference the other script by its UUID instead of a hardcoded relative or absolute path,
**So that** either script can be moved to a different directory without breaking the cross-script call.

<!-- section_id: "7c8d9e0f-1a2b-4c3d-4e5f-6a7b8c9d0e1f" -->
### What Happens

1. `agnostic-sync.sh` needs to call `pointer-sync.sh` for validation
2. Instead of: `bash "$ROOT/.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh" --validate`
3. It runs: `bash "$(resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)" --validate`
4. `resolve-uuid` finds the repo root via `git rev-parse --show-toplevel`, loads `.uuid-index.json`, looks up the UUID, returns the current path
5. The script executes at whatever path it currently lives at

**What this enables:**
- Moving `pointer-sync.sh` to a new directory doesn't break `agnostic-sync.sh`
- Moving `agnostic-sync.sh` doesn't break its calls to other scripts
- No need to update `SCRIPT_DIR` or `ROOT` path computations after moves
- Same-directory scripts can still use `$SCRIPT_DIR/` for efficiency (they're in the same `tools/` directory)

<!-- section_id: "8d9e0f1a-2b3c-4d4e-5f6a-7b8c9d0e1f2a" -->
### Acceptance Criteria

- `agnostic-sync.sh` calls `pointer-sync.sh` via UUID resolution instead of hardcoded path
- Git hooks call scripts via UUID resolution instead of hardcoded path
- Resolution adds <10ms overhead per call
- Scripts that are in the same `tools/` directory can still use `$SCRIPT_DIR/` for same-directory calls (optimization, not requirement)
- Moving any script to a new location + rebuilding index = all cross-script calls continue working
