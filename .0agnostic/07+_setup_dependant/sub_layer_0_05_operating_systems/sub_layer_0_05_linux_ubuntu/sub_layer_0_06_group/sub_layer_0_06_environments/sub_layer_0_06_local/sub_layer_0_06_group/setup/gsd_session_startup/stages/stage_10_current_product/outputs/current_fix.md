---
resource_id: "f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c"
resource_type: "output"
resource_name: "current_fix"
---

# GSD Session Startup — Current Fix

## Status: Active (pre-reboot verified, post-reboot pending)

## Problem

After every reboot, gsd-media-keys and gsd-power crash 5 times in <1 second with "Cannot open display:" and permanently fail. This causes:
- ~5 min dead zone for custom keybindings (Ctrl+Alt+S speak-selection)
- Brightness keys broken until manual restart
- Brightness OSD not appearing

## Root Causes

1. **DISPLAY not imported**: Unity desktop doesn't import DISPLAY into systemd user environment before gnome-session activates gsd services
2. **GDK_BACKEND=wayland**: `nvidia-wayland.conf` in environment.d sets GDK_BACKEND=wayland globally, causing gsd (GDK-based) to try Wayland instead of X11

## Solution (Three-Layer Defense)

### Layer 1: environment.d DISPLAY Import
**File**: `~/.config/environment.d/10-display.conf`
```ini
DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
```
Processed at systemd user manager startup, before any service.

### Layer 2: Service Drop-ins (DISPLAY + GDK_BACKEND)
**Files**:
- `~/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf`
- `~/.config/systemd/user/org.gnome.SettingsDaemon.Power.service.d/display.conf`

```ini
[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/dawson/.Xauthority
Environment=GDK_BACKEND=x11
```

### Layer 3: Safety Nets
- **display-ready.service**: `ExecStartPost` imports runtime DISPLAY after X11 confirmed ready
- **gsd-keepalive.service**: Uses `reset-failed` + `restart .target` (proper systemd, no raw spawning)
- **gsd-keepalive.timer**: OnBootSec=10 (reduced from 60)

## Files Changed

| File | Action |
|------|--------|
| `~/.config/environment.d/10-display.conf` | Created |
| `~/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf` | Created |
| `~/.config/systemd/user/org.gnome.SettingsDaemon.Power.service.d/display.conf` | Created |
| `~/.config/systemd/user/display-ready.service` | Modified (added ExecStartPost) |
| `~/.config/systemd/user/gsd-keepalive.service` | Rewritten (proper systemd restart) |
| `~/.config/systemd/user/gsd-keepalive.timer` | Modified (OnBootSec 60→10) |
| `~/.config/systemd/user/gsd-keepalive-v2.service` | Deleted (unused) |
| `~/.config/systemd/user/gnome-session-binary.service.d/override.conf` | Deleted (referenced disabled target) |

## Verification

### Pre-reboot (2026-03-06): PASSED
- Both services active via systemd targets
- 1 process each (no duplicates)
- Journal clean (no "Cannot open display:" after fix)

### Post-reboot: PENDING
- Requires reboot to confirm environment.d + drop-ins work at boot time
