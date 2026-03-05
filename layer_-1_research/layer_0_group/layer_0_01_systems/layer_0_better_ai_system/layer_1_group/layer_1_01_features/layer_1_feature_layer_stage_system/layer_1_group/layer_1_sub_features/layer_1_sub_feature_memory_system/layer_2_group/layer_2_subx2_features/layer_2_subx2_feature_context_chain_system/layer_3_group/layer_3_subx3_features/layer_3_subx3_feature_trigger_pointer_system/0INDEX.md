---
resource_id: "03886084-b94c-44e8-af91-ce5733c3bc82"
resource_type: "index
document"
resource_name: "0INDEX"
---
# 0INDEX.md - Trigger Pointer System

## Current State

**Phase**: active | **Last Updated**: 2026-03-02

## Stage Status

| # | Stage | Status | Key Outputs |
|---|-------|--------|-------------|
| 00 | Registry | scaffolded | |
| 01 | Request Gathering | active | Tree of needs for pointer system |
| 02 | Research | scaffolded | |
| 03 | Instructions | scaffolded | |
| 04 | Design | active | Pointer sync protocol (promoted to root .0agnostic/) |
| 05 | Planning | scaffolded | |
| 06 | Development | active | pointer-sync.sh, pointer-edit-guard.sh (promoted to root .0agnostic/) |
| 07 | Testing | scaffolded | |
| 08 | Criticism | scaffolded | |
| 09 | Fixing | scaffolded | |
| 10 | Current Product | active | pointer-sync.sh is working in production |
| 11 | Archives | scaffolded | |

## Production Artifacts

These have been promoted to root `.0agnostic/` and are in active use:

- `pointer-sync.sh` — finds pointers via YAML frontmatter, resolves canonical paths, auto-updates relative paths
- `pointer_sync_protocol.md` — step-by-step usage guide
- `pointer_sync_knowledge.md` — system overview and design decisions
- `pointer_sync_rule.md` — always-apply rule for pointer format
- `pointer-edit-guard.sh` — Claude Code hook for edit-time reminders
- Integration with `agnostic-sync.sh` — validates pointers at end of sync

## Open Items

- [ ] Expand tree of needs with more requirements
- [ ] Add testing stage outputs (automated test suite for pointer-sync.sh)
- [ ] Research additional trigger mechanisms (git hooks, filesystem watchers)
- [ ] Design pointer dependency graph (pointers that point to other pointers)
