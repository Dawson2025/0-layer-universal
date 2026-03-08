---
resource_id: "d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a"
resource_type: "output"
resource_name: "post_reboot_test"
---

# GSD Session Startup — Post-Reboot Test Results

**Date**: 2026-03-07
**Boot time**: ~21:16 MST
**Test time**: ~21:25-21:35 MST
**Reboot**: Clean reboot (previous session 2026-03-06)

## Cycle 2 Tests (MediaKeys + Power per-service drop-ins)

### T7: Clean Boot — PASS
```
$ journalctl --user -b -u org.gnome.SettingsDaemon.MediaKeys --no-pager
Mar 07 21:16:58 systemd: Starting org.gnome.SettingsDaemon.MediaKeys.service
Mar 07 21:16:58 systemd: Started org.gnome.SettingsDaemon.MediaKeys.service
Mar 07 21:16:58 gsd-media-keys: Failed to grab accelerator for keybinding settings:volume-mute
Mar 07 21:16:58 gsd-media-keys: Failed to grab accelerator for keybinding settings:volume-up (etc.)

$ journalctl --user -b -u org.gnome.SettingsDaemon.Power --no-pager
Mar 07 21:16:58 systemd: Starting org.gnome.SettingsDaemon.Power.service
Mar 07 21:16:58 systemd: Started org.gnome.SettingsDaemon.Power.service
```
**Zero "Cannot open display:" errors.** Clean start on first attempt.
Note: "Failed to grab accelerator" for volume/brightness keys is expected — Unity/GNOME Shell handles those natively.

### T8: Service Active Within 30s — PASS
```
MediaKeys: active
Power: active
```
Both active immediately at boot (21:16:58).

### T10: No Duplicates Post-Reboot — PASS
```
gsd-media-keys count: 1
gsd-power count: 1
```

## Cycle 3 Findings (Broader GDK_BACKEND Impact)

### T11: Other GSD Services — FAILED (before Cycle 3 fix)
The following services crashed at boot with the same 5-crash pattern:
```
$ systemctl --user --failed (at boot, before fix)
org.gnome.SettingsDaemon.Color.service    - failed
org.gnome.SettingsDaemon.Keyboard.service - failed
org.gnome.SettingsDaemon.Wacom.service    - failed
xdg-desktop-portal-gnome.service         - failed (SEGV)
```

**Root cause**: Same as Cycle 2 — `nvidia-wayland.conf` sets `GDK_BACKEND=wayland` globally. Cycle 2 only created per-service drop-ins for MediaKeys and Power, not for Color/Keyboard/Wacom.

### T11: Other GSD Services — PASS (after Cycle 3 fix)
After applying global `GDK_BACKEND=x11` via `zz-x11-session.conf` + `systemctl --user set-environment GDK_BACKEND=x11` + reset-failed + restart:
```
org.gnome.SettingsDaemon.MediaKeys: active
org.gnome.SettingsDaemon.Power: active
org.gnome.SettingsDaemon.Color: active
org.gnome.SettingsDaemon.Keyboard: active
org.gnome.SettingsDaemon.Wacom: active
xdg-desktop-portal-gnome: active
```

### T12: Toolbar App Launching — PENDING
User must verify: Nautilus, Settings, Terminal, OBS launch from toolbar after Cycle 3 fix.

### T13: Global GDK_BACKEND Verification — PASS
```
$ systemctl --user show-environment | grep GDK_BACKEND
GDK_BACKEND=x11
```

### T9: Functional Post-Reboot — PENDING
- Ctrl+Alt+S: User should test
- Brightness keys: User should test
- Brightness OSD: User should test

## Summary

| Test | Status | Notes |
|------|--------|-------|
| T7: Clean Boot (journals) | PASS | No "Cannot open display:" for MediaKeys/Power |
| T8: Services Active <30s | PASS | Both active at 21:16:58 |
| T9: Functional | PENDING | User to test keybindings/brightness |
| T10: No Duplicates | PASS | 1 process each |
| T11: Other GSD services | PASS (after fix) | Color/Keyboard/Wacom now active via global GDK_BACKEND fix |
| T12: Toolbar apps | PENDING | User to test Nautilus/Settings/Terminal from toolbar |
| T13: Global GDK_BACKEND | PASS | systemd user env shows x11 |

## Key Discovery: Cycle 3

The Cycle 2 approach of per-service drop-ins was insufficient. The `GDK_BACKEND=wayland` setting from `nvidia-wayland.conf` affects ALL D-Bus-activated GDK apps — not just the two gsd services we fixed. This includes:
- Other gsd services (Color, Keyboard, Wacom)
- Desktop portals (xdg-desktop-portal-gnome)
- D-Bus-activated apps (Nautilus, Settings, Terminal) launched from toolbar

The fix: `~/.config/environment.d/zz-x11-session.conf` with `GDK_BACKEND=x11` overrides `nvidia-wayland.conf` globally for ALL systemd user services.
