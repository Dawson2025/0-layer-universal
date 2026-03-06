---
resource_id: "b2c3d4e5-f6a7-8901-bcde-f12345678901"
resource_type: "index"
resource_name: "gsd_session_startup_index"
---
# GSD Session Startup — Status Dashboard

<!-- section_id: "e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b" -->
## Current Status

**Phase**: Research & Design (pre-testing)
**Blocking**: ~5 min dead zone after every reboot; brightness keys broken until manual intervention
**Last Updated**: 2026-03-06

## Root Cause Summary

Unity doesn't call `systemctl --user import-environment DISPLAY` before GNOME session activates gsd targets. Result: 5 rapid "Cannot open display:" crashes → permanent systemd failure.

## Stage Progress

| Stage | Status | Notes |
|-------|--------|-------|
| 01 Request Gathering | Done | Requirements tree complete |
| 02 Research | Done | DISPLAY race condition identified |
| 03 Instructions | Empty | |
| 04 Design | In Progress | 3 solutions documented (pre-testing) |
| 05 Planning | Not Started | |
| 06 Development | Not Started | |
| 07 Testing | Not Started | Test subdirs ready |
| 08 Criticism | Not Started | |
| 09 Fixing | Not Started | |
| 10 Current Product | Active | gsd_keepalive_fix.md (workaround) |
| 11 Archives | Empty | |

## Current Workaround

`gsd-keepalive.timer` + `wait-for-display.sh` — polls every 60s and restarts dead daemons. See `stages/stage_10_current_product/outputs/` for pointer.

## Open Bugs (from workaround)

1. ~5 min dead zone after boot (D-Bus name conflict)
2. Multi-instance spawning (race condition in pgrep check)
3. gsd-power not starting (same D-Bus conflict or missing dependency)
4. Silent error suppression (2>/dev/null hides errors)
5. Brightness keys/OSD broken (gsd-power not running)

## Proposed Solutions (Pre-Testing)

1. **gnome-session service startup order override** — systemd drop-in
2. **Post-login autostart hook** — .desktop autostart that imports DISPLAY
3. **Re-login trigger notification** — alert user when services fail

See `stages/stage_04_design/outputs/pre_testing/solution_overview.md` for details.
