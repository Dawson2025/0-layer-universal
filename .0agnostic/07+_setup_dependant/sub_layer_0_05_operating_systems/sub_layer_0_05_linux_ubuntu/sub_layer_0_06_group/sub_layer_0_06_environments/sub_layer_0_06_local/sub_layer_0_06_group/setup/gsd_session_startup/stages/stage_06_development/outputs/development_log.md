---
resource_id: "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d"
resource_type: "output"
resource_name: "development_log"
---

# GSD Session Startup — Development Log

## Date: 2026-03-06

### Implementation Summary

Implemented three-layer defense against the DISPLAY race condition, plus discovered a secondary root cause (GDK_BACKEND conflict).

### Root Causes Identified

**Primary (known)**: DISPLAY not in systemd user environment at boot. Unity doesn't call `systemctl --user import-environment DISPLAY` before gnome-session triggers gsd services.

**Secondary (discovered during testing)**: `~/.config/environment.d/nvidia-wayland.conf` sets `GDK_BACKEND=wayland` globally in the systemd user environment. Since the actual desktop runs X11 (not Wayland), gsd services launched by systemd try to connect to a non-existent Wayland display and fail with "Cannot open display:". Manual shell launches work because the login session overrides `GDK_BACKEND=x11`.

### Files Created

| File | Purpose |
|------|---------|
| `~/.config/environment.d/10-display.conf` | DISPLAY=:0 and XAUTHORITY for systemd services |
| `~/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf` | Service drop-in: DISPLAY + GDK_BACKEND=x11 |
| `~/.config/systemd/user/org.gnome.SettingsDaemon.Power.service.d/display.conf` | Service drop-in: DISPLAY + GDK_BACKEND=x11 |

### Files Modified

| File | Change |
|------|--------|
| `~/.config/systemd/user/display-ready.service` | Added ExecStartPost to import DISPLAY into systemd env |
| `~/.config/systemd/user/gsd-keepalive.service` | Rewritten: uses reset-failed + restart .target instead of pgrep/spawn |
| `~/.config/systemd/user/gsd-keepalive.timer` | Changed OnBootSec from 60 to 10 |

### Files Deleted

| File | Reason |
|------|--------|
| `~/.config/systemd/user/gsd-keepalive-v2.service` | Unused alternative |
| `~/.config/systemd/user/gnome-session-binary.service.d/override.conf` | Referenced disabled target |

### Testing Discovery

During pre-reboot testing, the initial environment.d + keepalive approach failed. Even with `DISPLAY=:0` explicitly set via `Environment=` directive in service drop-ins, gsd-media-keys still reported "Cannot open display:". Investigation revealed:

1. A transient systemd service running `env` showed `GDK_BACKEND=wayland` inherited from `nvidia-wayland.conf`
2. gsd-media-keys uses GDK which respects `GDK_BACKEND` — with `wayland` set, it ignores `$DISPLAY` and tries Wayland
3. Adding `GDK_BACKEND=x11` to the service drop-in resolved the issue immediately
4. Both services now start and run correctly via systemd targets

### Verification Results (Pre-Reboot)

- `systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service` → **active**
- `systemctl --user is-active org.gnome.SettingsDaemon.Power.service` → **active**
- `pgrep -c gsd-media-keys` → **1** (no duplicates)
- `pgrep -c gsd-power` → **1** (no duplicates)

### Pending: Post-Reboot Test

The environment.d config and service drop-ins will be tested after reboot to confirm they work at boot time (not just mid-session).
