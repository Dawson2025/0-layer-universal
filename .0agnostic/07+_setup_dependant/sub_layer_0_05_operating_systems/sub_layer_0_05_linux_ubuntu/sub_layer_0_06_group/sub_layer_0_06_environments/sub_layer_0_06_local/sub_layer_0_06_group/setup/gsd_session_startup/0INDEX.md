---
resource_id: "5248e0b5-6417-4314-84f8-688f9db8c42e"
resource_type: "index"
resource_name: "gsd_session_startup_index"
---
# GSD Session Startup — Status Dashboard

<!-- section_id: "a89d7885-4767-43e5-929e-5b009f9f6c1f" -->
## Current Status

**Phase**: Fix Applied — services verified, toolbar apps require reboot
**Blocking**: Reboot needed to validate toolbar app launching (gnome-shell has stale GDK_BACKEND)
**Last Updated**: 2026-03-07

## Root Causes

1. **DISPLAY race condition**: Unity doesn't call `systemctl --user import-environment DISPLAY` before GNOME session activates gsd targets → 5 rapid "Cannot open display:" crashes → permanent systemd failure
2. **GDK_BACKEND conflict**: `nvidia-wayland.conf` sets `GDK_BACKEND=wayland` in systemd user environment. ALL GDK services/apps launched via systemd try Wayland instead of X11. Shell sessions override this with `GDK_BACKEND=x11`, hiding the issue from manual testing.
3. **Broader impact (Cycle 3)**: Affects not just gsd-media-keys/gsd-power but ALL D-Bus-activated GDK apps — gsd-Color/Keyboard/Wacom, desktop portals, and toolbar-launched apps (Nautilus, Settings, Terminal, OBS).

## Solution Summary

Four-layer defense:
1. **environment.d DISPLAY**: `10-display.conf` — DISPLAY + XAUTHORITY at user manager startup
2. **environment.d GDK_BACKEND**: `zz-x11-session.conf` — global GDK_BACKEND=x11 override (Cycle 3)
3. **Service drop-ins**: GDK_BACKEND=x11 + DISPLAY for gsd and portal/terminal services
4. **Safety nets**: display-ready.service + gsd-keepalive (all 5 services)

See `stages/stage_10_current_product/outputs/current_fix.md` for full details.

## Stage Progress

| Stage | Status | Key Output |
|-------|--------|------------|
| 01 Request Gathering | Done | `requirements_tree.md` — R1-R6 hierarchy |
| 02 Research | Done | `display_race_condition.md` — DISPLAY race condition identified |
| 03 Instructions | Done | `constraints.md` — system constraints, dependency chain |
| 04 Design | Done | `cycle_1/chosen_solution.md` — three-layer defense |
| 05 Planning | Done | `implementation_plan.md` — 6-step implementation |
| 06 Development | Done | `development_log.md` — files created/modified/deleted |
| 07 Testing | Done | `pre_reboot_test.md` + `post_reboot_test.md` — all automated tests pass |
| 08 Criticism | Done (Cycle 3) | `review.md` — per-service insufficient, global fix needed |
| 09 Fixing | Done (Cycle 3) | `fixes_applied.md` — global GDK_BACKEND + extended keepalive |
| 10 Current Product | Active | `current_fix.md` — four-layer defense |
| 11 Archives | Empty | |

## Pending

- **Reboot**: Required to validate toolbar app launching — gnome-shell's process env has stale `GDK_BACKEND=wayland` from boot (before fix). On next boot, `zz-x11-session.conf` will set `GDK_BACKEND=x11` before gnome-shell starts.
- **Functional test**: After reboot, verify Ctrl+Alt+S, brightness keys, and toolbar app launching
- **Two propagation paths discovered**: D-Bus activation (systemd env → works now) vs gnome-shell fork (process env → needs reboot)
