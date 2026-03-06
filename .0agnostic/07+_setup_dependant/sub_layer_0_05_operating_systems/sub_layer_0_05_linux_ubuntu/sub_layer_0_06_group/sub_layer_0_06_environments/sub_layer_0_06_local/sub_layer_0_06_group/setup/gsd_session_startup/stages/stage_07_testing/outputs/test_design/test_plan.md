---
resource_id: "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e"
resource_type: "output"
resource_name: "test_plan"
---

# GSD Session Startup — Test Plan

## Pre-Reboot Tests (no reboot needed)

### T1: Environment Verification
- `systemctl --user show-environment | grep DISPLAY` → `:0`
- `systemctl --user show-environment | grep XAUTHORITY` → `/home/dawson/.Xauthority`

### T2: Service Drop-in Verification
- `systemctl --user show org.gnome.SettingsDaemon.MediaKeys.service -p Environment` includes `GDK_BACKEND=x11`
- `systemctl --user show org.gnome.SettingsDaemon.Power.service -p Environment` includes `GDK_BACKEND=x11`

### T3: Recovery via systemd (reset-failed + start target)
1. Kill stale raw processes: `pkill -x gsd-media-keys; pkill -x gsd-power`
2. Reset failed: `systemctl --user reset-failed org.gnome.SettingsDaemon.MediaKeys.service`
3. Start target: `systemctl --user start org.gnome.SettingsDaemon.MediaKeys.target`
4. Check active: `systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service` → `active`
5. Repeat for Power

### T4: Process Count
- `pgrep -c gsd-media-keys` → exactly 1
- `pgrep -c gsd-power` → exactly 1

### T5: Functional Tests
- Ctrl+Alt+S (speak-selection) keybinding works
- Brightness keys (Fn+F5/F6) change brightness
- Brightness OSD appears

### T6: Journal Clean
- `journalctl --user -u org.gnome.SettingsDaemon.MediaKeys -n 5 --no-pager` — no recent "Cannot open display:" after fix applied

## Post-Reboot Tests (requires reboot)

### T7: Clean Boot
1. Reboot
2. `journalctl --user -b -u org.gnome.SettingsDaemon.MediaKeys --no-pager` — NO "Cannot open display:" errors
3. `journalctl --user -b -u org.gnome.SettingsDaemon.Power --no-pager` — NO "Cannot open display:" errors

### T8: Service Active Within 30s
- `systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service` → `active`
- `systemctl --user is-active org.gnome.SettingsDaemon.Power.service` → `active`

### T9: Functional Post-Reboot
- Ctrl+Alt+S works immediately (within 30s of desktop)
- Brightness keys work + OSD appears

### T10: No Duplicates Post-Reboot
- `pgrep -c gsd-media-keys` → 1
- `pgrep -c gsd-power` → 1
