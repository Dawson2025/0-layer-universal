---
resource_id: "24b87bb5-c981-40b3-94dc-c0b052db0997"
resource_type: "output"
resource_name: "pointer_sync_implementation"
---
# Pointer Sync System — Implementation

> **Canonical location**: Root `.0agnostic/pointer-sync.sh`

The implementation artifacts live at the root `.0agnostic/` level. This pointer connects stage_3_06_development to the canonical script and hook.

## Production Artifacts

| Artifact | Canonical Location |
|----------|-------------------|
| Main script | `.0agnostic/pointer-sync.sh` |
| Claude Code hook | `.0agnostic/06_context_avenue_web/01_file_based/08_hooks/scripts/pointer-edit-guard.sh` |
| Hook registration | `.claude/settings.json` (PostToolUse entry) |
| agnostic-sync integration | `.0agnostic/agnostic-sync.sh` (pointer validation section) |
