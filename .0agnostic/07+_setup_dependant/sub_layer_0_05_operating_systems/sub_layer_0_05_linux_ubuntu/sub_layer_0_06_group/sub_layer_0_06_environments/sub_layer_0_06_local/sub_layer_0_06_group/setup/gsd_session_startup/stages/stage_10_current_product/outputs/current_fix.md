---
resource_id: "f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c"
resource_type: "output"
resource_name: "current_fix"
---

# GSD Session Startup — Current Fix

## Status: Active (post-reboot verified 2026-03-07)

## Problem

After every reboot, gsd-media-keys and gsd-power crash 5 times in <1 second with "Cannot open display:" and permanently fail. This causes:
- ~5 min dead zone for custom keybindings (Ctrl+Alt+S speak-selection)
- Brightness keys broken until manual restart
- Brightness OSD not appearing

## Root Causes

1. **DISPLAY not imported**: Unity desktop doesn't import DISPLAY into systemd user environment before gnome-session activates gsd services
2. **GDK_BACKEND=wayland**: `nvidia-wayland.conf` in environment.d sets GDK_BACKEND=wayland globally, causing gsd (GDK-based) to try Wayland instead of X11

## Solution (Four-Layer Defense)

### Layer 1: environment.d DISPLAY Import
**File**: `~/.config/environment.d/10-display.conf`
```ini
DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
```
Processed at systemd user manager startup, before any service.

### Layer 1b: Global GDK_BACKEND Override (Cycle 3)
**File**: `~/.config/environment.d/zz-x11-session.conf`
```ini
GDK_BACKEND=x11
```
Overrides `nvidia-wayland.conf`'s `GDK_BACKEND=wayland` for ALL systemd user services. Sorts after nvidia-wayland.conf alphabetically (z > n). Fixes all D-Bus-activated GDK apps (gsd services, portals, Nautilus, Settings, Terminal, OBS).

### Layer 2: Service Drop-ins (DISPLAY + GDK_BACKEND)
**GSD services**:
- `~/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf`
- `~/.config/systemd/user/org.gnome.SettingsDaemon.Power.service.d/display.conf`

```ini
[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/dawson/.Xauthority
Environment=GDK_BACKEND=x11
```

**Portal/Terminal services** (defense-in-depth, also have GDK_BACKEND=x11):
- `~/.config/systemd/user/xdg-desktop-portal-gnome.service.d/override.conf`
- `~/.config/systemd/user/xdg-desktop-portal-gtk.service.d/override.conf`
- `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf`
- `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf`

### Layer 3: Safety Nets
- **display-ready.service**: `ExecStartPost` imports runtime DISPLAY after X11 confirmed ready
- **gsd-keepalive.service**: Uses `reset-failed` + `restart .target` for all 5 gsd services (MediaKeys, Power, Color, Keyboard, Wacom)
- **gsd-keepalive.timer**: OnBootSec=10 (reduced from 60)

## Files Changed

### Cycle 1-2 (2026-03-06)

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

### Cycle 3 (2026-03-07)

| File | Action |
|------|--------|
| `~/.config/environment.d/zz-x11-session.conf` | Created (global GDK_BACKEND=x11 override) |
| `~/.config/systemd/user/gsd-keepalive.service` | Updated (added Color, Keyboard, Wacom to monitor list) |
| `~/.config/systemd/user/xdg-desktop-portal-gnome.service.d/override.conf` | Updated (added GDK_BACKEND=x11) |
| `~/.config/systemd/user/xdg-desktop-portal-gtk.service.d/override.conf` | Updated (added GDK_BACKEND=x11) |
| `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf` | Updated (added GDK_BACKEND=x11) |
| `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf` | Updated (added GDK_BACKEND=x11) |

## Verification

### Pre-reboot (2026-03-06): PASSED
- MediaKeys + Power active via systemd targets
- 1 process each (no duplicates)
- Journal clean (no "Cannot open display:" after fix)

### Post-reboot (2026-03-07): PASSED
- MediaKeys + Power started cleanly at boot (zero "Cannot open display:" errors)
- All 5 gsd services active after Cycle 3 fix (Color, Keyboard, Wacom added)
- xdg-desktop-portal-gnome active
- No duplicate processes
- `systemctl --user show-environment | grep GDK_BACKEND` → `x11`
- Functional tests: pending user verification (Ctrl+Alt+S, brightness)
- Toolbar apps: FAILED this session (gnome-shell process env still has GDK_BACKEND=wayland from boot). Will fix on next reboot — gnome-shell will inherit GDK_BACKEND=x11 from environment.d at startup.

### Known Limitation: Mid-Session Fix

The `zz-x11-session.conf` fix updates the systemd user manager environment, but does NOT change the environment of already-running processes like gnome-shell. Apps launched by clicking toolbar icons are forked from gnome-shell, so they inherit gnome-shell's stale `GDK_BACKEND=wayland`. This is resolved by rebooting (or `gnome-shell --replace`).
