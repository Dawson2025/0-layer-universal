---
resource_id: "c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f"
resource_type: "output"
resource_name: "pre_reboot_test"
---

# GSD Session Startup — Pre-Reboot Test Results

**Date**: 2026-03-06
**Boot time**: 09:08 MST
**Test time**: ~11:08–11:15 MST

## Test Results

### T1: Environment Verification — PASS
```
$ systemctl --user show-environment | grep DISPLAY
DISPLAY=:0

$ systemctl --user show-environment | grep XAUTHORITY
XAUTHORITY=/home/dawson/.Xauthority
```

### T2: Service Drop-in Verification — PASS
```
$ systemctl --user show org.gnome.SettingsDaemon.MediaKeys.service -p Environment
Environment=DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority GDK_BACKEND=x11

$ systemctl --user show org.gnome.SettingsDaemon.MediaKeys.service -p DropInPaths
DropInPaths=/home/dawson/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf
```

### T3: Recovery via systemd — PASS (on second attempt)

**First attempt (without GDK_BACKEND=x11)**: FAILED
- Reset-failed + restart target → service started but immediately failed
- "Cannot open display:" despite DISPLAY=:0 being set
- Root cause: `GDK_BACKEND=wayland` from nvidia-wayland.conf

**Second attempt (with GDK_BACKEND=x11 in drop-in)**: PASSED
- Reset-failed + start target → both services started successfully
- `systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service` → `active`
- `systemctl --user is-active org.gnome.SettingsDaemon.Power.service` → `active`

### T4: Process Count — PASS
```
$ pgrep -c gsd-media-keys
1
$ pgrep -c gsd-power
1
```

### T5: Functional Tests — PENDING
- Ctrl+Alt+S: User should test manually
- Brightness keys: User should test manually

### T6: Journal Clean — PASS (after fix)
Latest entries show successful start, no "Cannot open display:" after the GDK_BACKEND fix.

## Key Finding: GDK_BACKEND Conflict

The most significant discovery was that `~/.config/environment.d/nvidia-wayland.conf` sets `GDK_BACKEND=wayland` for all systemd user services. This causes gsd-media-keys and gsd-power to try connecting to a Wayland display instead of X11, regardless of whether DISPLAY is set.

**Evidence**:
- Transient service `env` output showed `GDK_BACKEND=wayland` in environment
- Shell had `GDK_BACKEND=x11` (set by login session)
- Adding `GDK_BACKEND=x11` to service drop-ins immediately resolved the issue

This was NOT in the original design. The design document has been updated to reflect this additional fix.

## Post-Reboot Tests — NOT YET RUN
Require reboot. The environment.d + service drop-ins should prevent the initial boot-time failures entirely.

## Conclusion

Pre-reboot tests pass. The fix requires:
1. `~/.config/environment.d/10-display.conf` (DISPLAY + XAUTHORITY)
2. Service drop-ins with `GDK_BACKEND=x11` for both gsd services
3. Rewritten gsd-keepalive as safety net
4. Enhanced display-ready.service for runtime DISPLAY import

The GDK_BACKEND conflict was a hidden second root cause that wasn't visible in the original research because the research tested with shell commands (which had GDK_BACKEND=x11 from the session).
