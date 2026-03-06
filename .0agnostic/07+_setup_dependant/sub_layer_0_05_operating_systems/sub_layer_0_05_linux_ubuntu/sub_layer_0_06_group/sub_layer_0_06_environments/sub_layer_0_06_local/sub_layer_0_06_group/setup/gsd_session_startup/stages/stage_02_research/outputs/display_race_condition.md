---
resource_id: "4961c5aa-4266-46df-ad0d-fac5d072b7d1"
resource_type: "output"
resource_name: "display_race_condition"
---
# DISPLAY Race Condition — Root Cause Analysis

**Date**: 2026-03-06
**Method**: Post-reboot journal analysis + manual daemon testing

<!-- section_id: "69f5a671-e44c-49e3-94ee-98bcfd302518" -->
## Summary

Unity desktop (`XDG_CURRENT_DESKTOP=Unity`) doesn't import `DISPLAY` into the systemd user environment before GNOME session triggers gsd-media-keys and gsd-power. This causes 5 rapid "Cannot open display:" crashes in <1 second, after which systemd permanently gives up on the services.

<!-- section_id: "23cdce01-ba3d-4fb7-856f-97b2409d4be5" -->
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

<!-- section_id: "fc6f4842-425a-4126-aa61-9d7b98948f1a" -->
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

<!-- section_id: "86a0a653-7e4e-4720-a890-e2186ba8107d" -->
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

<!-- section_id: "d8886a42-112b-41b2-98e5-91e81b5bac06" -->
## Current Band-Aid Stack

| Layer | Mechanism | What It Does | Limitation |
|-------|-----------|-------------|------------|
| 1 | `gsd-keepalive.timer` | Polls every 60s, restarts dead daemons | ~5 min dead zone; D-Bus name conflict prevents restart |
| 2 | `wait-for-display.sh` | ExecStartPre — waits for X11 before starting | Only helps keepalive, not GNOME's own service |
| 3 | `Environment=DISPLAY=:0` | Hardcoded in keepalive service | Fragile; doesn't fix GNOME's service |
| 4 | Inline `DISPLAY=:0` on ExecStart | Redundant env setting | Same fragility |

<!-- section_id: "9e3928f8-c867-4aa6-bcce-8a4bed17f189" -->
## Proper Fix Direction

Import `DISPLAY` and `XAUTHORITY` into the systemd user environment **before** gsd services start. Options:

1. **systemd drop-in override** — make gsd services depend on a readiness target that waits for DISPLAY
2. **Session autostart script** — `.desktop` file that runs `systemctl --user import-environment DISPLAY XAUTHORITY` early
3. **systemd user environment generator** — export DISPLAY from display manager's perspective

See `../stage_04_design/outputs/pre_testing/solution_overview.md` for detailed solution designs.

<!-- section_id: "27d1c63f-04c6-475e-a64a-7277bb0fc1fd" -->
## Functional Impact (observed 2026-03-06)

| Feature | Status After Reboot | Root Cause |
|---------|-------------------|------------|
| Ctrl+Alt+S speak-selection | Broken for ~5 min, then works | gsd-media-keys dead, keepalive eventually restarts it |
| Volume keys | Working immediately | Uses custom `volume-control.sh`, NOT gsd-media-keys |
| Brightness keys | Broken permanently | gsd-power dead, brightness OSD not appearing |
| Kokoro TTS server | Working | Separate systemd service, not affected |
| PipeWire audio | Working | Not affected by gsd failures |
