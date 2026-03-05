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
### Root Cause

1. Services failed during login (due to inotify exhaustion or portal issues)
2. Systemd gave up after 5 restart attempts
3. Services configured to only start via GNOME session, not manually
4. Manual starts work but nothing restarts them if they die

<!-- section_id: "88aa64cd-8bd7-4368-85d4-be5f2dbbbebf" -->
### Error Evidence

```
× org.gnome.SettingsDaemon.MediaKeys.service
  Active: failed (Result: exit-code)
  "Start request repeated too quickly"
  "Failed with result 'exit-code'"
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
ExecStart=/bin/bash -c 'pgrep -x gsd-media-keys || DISPLAY=:0 /usr/libexec/gsd-media-keys & pgrep -x gsd-power || DISPLAY=:0 /usr/libexec/gsd-power &'

[Install]
WantedBy=default.target
```

> **IMPORTANT**: Do NOT use `RemainAfterExit=yes` — it causes the timer to think the service is still "active" and never re-trigger. The service must complete (become inactive) each run so the timer fires again.
>
> **IMPORTANT**: `DISPLAY=:0` must be set both in `Environment=` AND inline on the exec commands. Without it, the daemons fail with "Cannot open display:" because systemd services don't inherit the X11 display variable.

**~/.config/systemd/user/gsd-keepalive.timer**
```ini
[Unit]
Description=Check GNOME Settings Daemons every minute

[Timer]
OnBootSec=30
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

Log out and log back in after the underlying issues (inotify, portals) are resolved. This allows GNOME session to properly start all services. After a fresh login, the keepalive timer becomes a safety net rather than a necessity.

<!-- section_id: "3254b793-d966-4c9e-a39a-70be3d88668e" -->
## Related Issues

- inotify_exhaustion (resolved)
- Portal service failures (resolved via mask + relogin)
- gnome-shell stale grabs after sleep (see ubuntu_desktop knowledge: gnome_architecture.md)
