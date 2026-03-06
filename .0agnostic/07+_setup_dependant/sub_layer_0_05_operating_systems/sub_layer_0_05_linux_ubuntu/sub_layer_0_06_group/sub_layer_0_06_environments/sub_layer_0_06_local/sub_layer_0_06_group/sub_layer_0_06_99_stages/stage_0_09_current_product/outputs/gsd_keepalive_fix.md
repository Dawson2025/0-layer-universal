---
resource_id: "5509c4f6-4668-4d98-bc75-002d3559ec78"
resource_type: "output"
resource_name: "gsd_keepalive_fix"
---
# GSD Keepalive Service Fix

<!-- section_id: "eaca8696-22bf-4c17-98e7-d32c9c3646ab" -->
## Problem

GNOME Settings Daemons (`gsd-media-keys`, `gsd-power`) repeatedly failing, causing:
- Volume buttons not working
- Brightness buttons not working

<!-- section_id: "2a3eed74-3292-4ffe-84e4-d4aef95b32d2" -->
### Root Cause: DISPLAY Race Condition

**Single root cause**: Unity desktop doesn't import `DISPLAY` into the systemd user environment before GNOME session triggers gsd-media-keys and gsd-power.

**Timeline (every boot)**:
1. `09:08:20.000` — systemd user session starts (reaches default.target in 141ms)
2. `09:08:20.141` — GNOME session triggers gsd-media-keys, gsd-power
3. `09:08:21` — gsd-media-keys: `Cannot open display:` — crashes
4. 5 crashes in <1 second — systemd enters permanent `failed` state
5. `09:08:2?` — Display manager finally exports `DISPLAY=:0` ... too late

**Why Unity is different**: On stock GNOME, `gnome-session` calls `systemctl --user import-environment DISPLAY` before activating gsd targets. Unity (`XDG_CURRENT_DESKTOP=Unity`) uses GNOME components but has a different session startup sequence — it doesn't import `DISPLAY` into systemd fast enough.

**The keepalive system is a band-aid**:
- Band-aid 1: `gsd-keepalive.timer` — polls every 60s, restarts dead daemons
- Band-aid 2: `wait-for-display.sh` — waits for X11 before starting
- Band-aid 3: `Environment=DISPLAY=:0` — hardcoded fallback in service
- Still broken: ~5 min dead zone, multi-instance spawning, silent errors

**Proper fix**: Import DISPLAY into systemd user env before gsd services start (e.g., systemd drop-in override or session startup script running `systemctl --user import-environment DISPLAY XAUTHORITY` early in the login sequence).

> **NOTE**: This problem is being tracked in a dedicated entity. See `../../../setup/gsd_session_startup/` for the full requirements tree, design, and testing.

<!-- section_id: "88aa64cd-8bd7-4368-85d4-be5f2dbbbebf" -->
### Error Evidence

Journal output from 2026-03-06 reboot:
```
gsd-media-keys: Cannot open display:
gsd-media-keys: Cannot open display:
gsd-media-keys: Cannot open display:
gsd-media-keys: Cannot open display:
gsd-media-keys: Cannot open display:
× org.gnome.SettingsDaemon.MediaKeys.service
  Active: failed (Result: exit-code)
  "Start request repeated too quickly"
  "Failed with result 'exit-code'"
```

gsd-media-keys D-Bus dependency failure (brightness keys → gsd-power):
```
media-keys-plugin-WARNING: Failed to set new screen percentage:
  GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown:
  The name org.gnome.SettingsDaemon.Power was not provided by any .service files
```

<!-- section_id: "71512a44-d982-4580-9882-338b246b8977" -->
## Solution

Created a keepalive timer that checks every 60 seconds and restarts dead daemons.

<!-- section_id: "a7bf8c86-baa8-4706-b8a2-51e1eeb23539" -->
### Files Created

**~/.config/systemd/user/gsd-keepalive.service**
```ini
[Unit]
Description=Keep GNOME Settings Daemons alive
After=graphical-session.target

[Service]
Type=oneshot
Environment=DISPLAY=:0
Environment=XAUTHORITY=%h/.Xauthority
# Wait for display to be ready dynamically before attempting to start daemons
ExecStartPre=/home/dawson/.local/bin/wait-for-display.sh
# Start/restart daemons - attempt manual start as fallback
ExecStart=/bin/bash -c 'pgrep -x gsd-media-keys > /dev/null || DISPLAY=:0 XAUTHORITY=%h/.Xauthority /usr/libexec/gsd-media-keys 2>/dev/null & pgrep -x gsd-power > /dev/null || DISPLAY=:0 XAUTHORITY=%h/.Xauthority /usr/libexec/gsd-power 2>/dev/null &'

[Install]
WantedBy=default.target
```

> **IMPORTANT**: Do NOT use `RemainAfterExit=yes` — it causes the timer to think the service is still "active" and never re-trigger. The service must complete (become inactive) each run so the timer fires again.
>
> **IMPORTANT**: `DISPLAY=:0` must be set both in `Environment=` AND inline on the exec commands. Without it, the daemons fail with "Cannot open display:" because systemd services don't inherit the X11 display variable.

**~/.local/bin/wait-for-display.sh** (ExecStartPre dependency)
- Polls every 2s (up to 120s) for: DISPLAY set, X11 socket exists, XAUTHORITY accessible, gnome-shell running
- Exits 0 when all conditions met, exits 1 on timeout

**~/.config/systemd/user/gsd-keepalive.timer**
```ini
[Unit]
Description=Check GNOME Settings Daemons every minute

[Timer]
OnBootSec=60
OnUnitActiveSec=60

[Install]
WantedBy=timers.target
```

<!-- section_id: "66e00fa6-81c7-4b79-adf9-0db21d6b8c60" -->
### Commands to Apply

```bash
# Reload systemd
systemctl --user daemon-reload

# Enable and start timer
systemctl --user enable --now gsd-keepalive.timer

# Verify
systemctl --user status gsd-keepalive.timer
```

<!-- section_id: "f89243ea-5817-40ab-bbbe-b5dafd6e0ff8" -->
## Verification

```bash
# Check timer is active
systemctl --user list-timers | grep gsd

# Check daemons are running
pgrep -a gsd-media-keys
pgrep -a gsd-power

# Test volume/brightness buttons
```

<!-- section_id: "20654ec1-e65c-47a8-92d9-0d1a6dac1e71" -->
## Known Limitation: Stale GNOME Shell Grabs

The keepalive timer successfully restarts gsd-media-keys and gsd-power processes. However, if gnome-shell's internal accelerator grab table is stale (common after suspend/resume), the restarted daemons still get "Failed to grab accelerator" for standard media keys.

**Why**: GNOME Shell 46 handles standard media keys (volume, brightness) natively. The "Failed to grab accelerator" messages are actually harmless for standard keys — gnome-shell already owns them. gsd-media-keys IS still needed for custom keybindings (e.g., Ctrl+Alt+S for speak-selection).

**When keepalive is NOT enough**: If gnome-shell itself has stale state (post-sleep), even custom keybindings may not work. In this case:
1. `gnome-shell --replace` on X11 (WARNING: kills Cursor/Electron apps)
2. Or log out and back in

<!-- section_id: "9893c362-614f-432f-8b16-a9b0fbe8a1c2" -->
## Long-term Fix

Import `DISPLAY` and `XAUTHORITY` into the systemd user environment early in the Unity session startup, before GNOME triggers gsd services. This is the proper fix — it eliminates the race condition instead of working around it. See `../../../setup/gsd_session_startup/` for investigation and implementation of the proper fix.

Current workaround: the keepalive timer provides eventual recovery (~5 min delay). A fresh logout/login also works because it restarts the full GNOME session.

<!-- section_id: "e1f7a2b3-4c5d-6e7f-8a9b-0c1d2e3f4a5b" -->
## Reboot Test Results (2026-03-06)

Fresh reboot test to verify keepalive reliability.

### Timeline

| Time | Event |
|------|-------|
| 09:08:20 | System boot, kokoro-tts.service starts, gsd-keepalive.timer starts |
| 09:08:22 | GNOME's `org.gnome.SettingsDaemon.MediaKeys.service` crashes 5 times → enters **permanent failure** |
| 09:09:06 | First keepalive run — display check passes, ExecStart runs, reports "Finished" |
| 09:09–09:13 | Keepalive fires every 60s, always succeeds, but **gsd-media-keys is NOT running** |
| ~09:14 | Manual keepalive trigger → gsd-media-keys finally stays alive (3 instances spawned) |

### Findings

1. **GNOME session service fails every boot**: `org.gnome.SettingsDaemon.MediaKeys.service` crashes 5 times during login and enters permanent `failed` state. This happens every reboot — it's not a one-time issue.

2. **Keepalive fires but daemons die silently**: The keepalive ExecStart runs, pgrep correctly finds gsd-media-keys dead, starts a new one — but the process exits immediately. The `2>/dev/null` hides the error. This repeats for ~5 minutes.

3. **Likely cause — D-Bus name conflict**: The crashed GNOME service may still hold the D-Bus name `org.gnome.SettingsDaemon.MediaKeys`. The keepalive's new process can't register the same name and exits. Once the D-Bus name times out/releases, the next attempt succeeds.

4. **Multi-instance spawning**: No duplicate prevention. When the daemon finally stays alive, subsequent keepalive runs can spawn additional instances (observed 3 concurrent processes). The `pgrep` check should prevent this, but there's a race window between pgrep and process startup.

5. **gsd-power never starts**: The keepalive attempts to start it every 60s but it never comes up. Not critical for TTS but affects power management features.

### Post-Reboot Functional Status

| Feature | Status | Notes |
|---------|--------|-------|
| Ctrl+Alt+S speak-selection | Working | After ~5 min dead zone |
| Volume keys (custom script) | Working | Uses custom volume-control.sh, not gsd-media-keys |
| Brightness keys | **NOT working** | gsd-power not running; brightness OSD not appearing |
| Kokoro TTS server | Working | systemd service auto-started, GPU healthy |
| Audio stack (PipeWire) | Working | paplay functional |

<!-- section_id: "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e" -->
## Open Bugs

1. **~5 min dead zone after boot**: Custom keybindings don't work for ~5 minutes after every reboot. Root cause: D-Bus name conflict between GNOME's failed service and keepalive's restart attempt. Potential fix: reset the GNOME systemd service first (`systemctl --user reset-failed org.gnome.SettingsDaemon.MediaKeys.service`) before starting a new process.

2. **Multi-instance spawning**: Race condition between pgrep check and process startup can produce duplicate gsd-media-keys processes. Potential fix: use a PID file or `flock` for mutual exclusion.

3. **gsd-power not starting**: Keepalive tries every 60s but gsd-power never stays alive. Needs investigation — may be same D-Bus conflict, or missing dependency.

4. **Silent error suppression**: `2>/dev/null` in ExecStart hides all startup errors. Should log to journal instead for debugging.

5. **Brightness keys/OSD broken**: Brightness hardware keys don't work and the GNOME brightness OSD doesn't appear in the top corner. Likely caused by gsd-power not running.

<!-- section_id: "3254b793-d966-4c9e-a39a-70be3d88668e" -->
## Related Issues

- inotify_exhaustion (resolved)
- Portal service failures (resolved via mask + relogin)
- gnome-shell stale grabs after sleep (see ubuntu_desktop knowledge: gnome_architecture.md)
