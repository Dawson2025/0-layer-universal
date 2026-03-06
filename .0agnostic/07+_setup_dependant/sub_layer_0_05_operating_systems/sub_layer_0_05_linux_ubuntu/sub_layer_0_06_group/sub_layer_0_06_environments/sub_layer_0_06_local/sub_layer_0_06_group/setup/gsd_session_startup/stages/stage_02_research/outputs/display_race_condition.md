---
resource_id: "d4e5f6a7-b8c9-0123-defa-345678901234"
resource_type: "output"
resource_name: "display_race_condition"
---
# DISPLAY Race Condition — Root Cause Analysis

**Date**: 2026-03-06
**Method**: Post-reboot journal analysis + manual daemon testing

<!-- section_id: "c9d0e1f2-a3b4-5c6d-7e8f-9a0b1c2d3e4f" -->
## Summary

Unity desktop (`XDG_CURRENT_DESKTOP=Unity`) doesn't import `DISPLAY` into the systemd user environment before GNOME session triggers gsd-media-keys and gsd-power. This causes 5 rapid "Cannot open display:" crashes in <1 second, after which systemd permanently gives up on the services.

<!-- section_id: "d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a" -->
## Timeline (from journal, 2026-03-06 reboot)

```
09:08:20.000  systemd user session starts (reaches default.target in 141ms)
09:08:20.141  GNOME session triggers gsd-media-keys, gsd-power via D-Bus activation
09:08:21      gsd-media-keys: "Cannot open display:" — crashes (attempt 1)
09:08:21      gsd-media-keys: "Cannot open display:" — crashes (attempt 2)
09:08:21      gsd-media-keys: "Cannot open display:" — crashes (attempt 3)
09:08:21      gsd-media-keys: "Cannot open display:" — crashes (attempt 4)
09:08:21      gsd-media-keys: "Cannot open display:" — crashes (attempt 5)
09:08:22      systemd: "Start request repeated too quickly" → PERMANENT FAILURE
              org.gnome.SettingsDaemon.MediaKeys.service → failed state
              (same for gsd-power)
09:08:2?      Display manager finally exports DISPLAY=:0
              ...but it's too late. Services are dead forever.
```

<!-- section_id: "e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b" -->
## Journal Evidence

### gsd-media-keys crashes
```
journalctl --user -u org.gnome.SettingsDaemon.MediaKeys -b
→ "Cannot open display:" (x5, all within 09:08:21)
→ "Start request repeated too quickly"
→ "Failed with result 'exit-code'"
```

### gsd-media-keys accelerator grab failures (after manual restart)
```
media-keys-plugin-WARNING: Failed to grab accelerator for keybinding settings:volume-down
media-keys-plugin-WARNING: Failed to grab accelerator for keybinding settings:volume-up
media-keys-plugin-WARNING: Failed to grab accelerator for keybinding settings:volume-mute
media-keys-plugin-WARNING: Failed to grab accelerator for keybinding settings:screen-brightness-up
media-keys-plugin-WARNING: Failed to grab accelerator for keybinding settings:screen-brightness-down
```
Note: These are harmless — GNOME Shell 46 handles standard media keys natively. gsd-media-keys is needed for custom keybindings only.

### gsd-power D-Bus dependency
```
media-keys-plugin-WARNING: Failed to set new screen percentage:
  GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown:
  The name org.gnome.SettingsDaemon.Power was not provided by any .service files
```
Brightness key presses route through gsd-media-keys → D-Bus call to gsd-power. Since gsd-power is also dead, brightness control fails completely.

<!-- section_id: "f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c" -->
## Why Unity Is Different

On **stock GNOME**, `gnome-session` calls:
```bash
systemctl --user import-environment DISPLAY XAUTHORITY
```
...before activating gsd D-Bus targets. This ensures DISPLAY is in the systemd user environment when services start.

On **Unity** (`XDG_CURRENT_DESKTOP=Unity`):
- Uses GNOME components (gsd-media-keys, gsd-power, gnome-shell)
- Has a different session startup sequence
- Does NOT import DISPLAY into systemd user env before services trigger
- Result: services crash because `DISPLAY` is empty/unset

<!-- section_id: "a3b4c5d6-e7f8-9a0b-1c2d-3e4f5a6b7c8d" -->
## Current Band-Aid Stack

| Layer | Mechanism | What It Does | Limitation |
|-------|-----------|-------------|------------|
| 1 | `gsd-keepalive.timer` | Polls every 60s, restarts dead daemons | ~5 min dead zone; D-Bus name conflict prevents restart |
| 2 | `wait-for-display.sh` | ExecStartPre — waits for X11 before starting | Only helps keepalive, not GNOME's own service |
| 3 | `Environment=DISPLAY=:0` | Hardcoded in keepalive service | Fragile; doesn't fix GNOME's service |
| 4 | Inline `DISPLAY=:0` on ExecStart | Redundant env setting | Same fragility |

<!-- section_id: "b4c5d6e7-f8a9-0b1c-2d3e-4f5a6b7c8d9e" -->
## Proper Fix Direction

Import `DISPLAY` and `XAUTHORITY` into the systemd user environment **before** gsd services start. Options:

1. **systemd drop-in override** — make gsd services depend on a readiness target that waits for DISPLAY
2. **Session autostart script** — `.desktop` file that runs `systemctl --user import-environment DISPLAY XAUTHORITY` early
3. **systemd user environment generator** — export DISPLAY from display manager's perspective

See `../stage_04_design/outputs/pre_testing/solution_overview.md` for detailed solution designs.

<!-- section_id: "c5d6e7f8-a90b-1c2d-3e4f-5a6b7c8d9e0f" -->
## Functional Impact (observed 2026-03-06)

| Feature | Status After Reboot | Root Cause |
|---------|-------------------|------------|
| Ctrl+Alt+S speak-selection | Broken for ~5 min, then works | gsd-media-keys dead, keepalive eventually restarts it |
| Volume keys | Working immediately | Uses custom `volume-control.sh`, NOT gsd-media-keys |
| Brightness keys | Broken permanently | gsd-power dead, brightness OSD not appearing |
| Kokoro TTS server | Working | Separate systemd service, not affected |
| PipeWire audio | Working | Not affected by gsd failures |
