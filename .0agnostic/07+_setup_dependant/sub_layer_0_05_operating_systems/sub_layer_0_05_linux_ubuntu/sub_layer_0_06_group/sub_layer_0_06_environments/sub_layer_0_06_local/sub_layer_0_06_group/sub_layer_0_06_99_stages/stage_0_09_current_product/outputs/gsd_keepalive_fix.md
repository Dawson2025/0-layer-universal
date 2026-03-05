---
resource_id: "5509c4f6-4668-4d98-bc75-002d3559ec78"
resource_type: "output"
resource_name: "gsd_keepalive_fix"
---
# GSD Keepalive Service Fix

## Problem

GNOME Settings Daemons (`gsd-media-keys`, `gsd-power`) repeatedly failing, causing:
- Volume buttons not working
- Brightness buttons not working

### Root Cause

1. Services failed during login (due to inotify exhaustion or portal issues)
2. Systemd gave up after 5 restart attempts
3. Services configured to only start via GNOME session, not manually
4. Manual starts work but nothing restarts them if they die

### Error Evidence

```
× org.gnome.SettingsDaemon.MediaKeys.service
  Active: failed (Result: exit-code)
  "Start request repeated too quickly"
  "Failed with result 'exit-code'"
```

## Solution

Created a keepalive timer that checks every 60 seconds and restarts dead daemons.

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

### Commands to Apply

```bash
# Reload systemd
systemctl --user daemon-reload

# Enable and start timer
systemctl --user enable --now gsd-keepalive.timer

# Verify
systemctl --user status gsd-keepalive.timer
```

## Verification

```bash
# Check timer is active
systemctl --user list-timers | grep gsd

# Check daemons are running
pgrep -a gsd-media-keys
pgrep -a gsd-power

# Test volume/brightness buttons
```

## Known Limitation: Stale GNOME Shell Grabs

The keepalive timer successfully restarts gsd-media-keys and gsd-power processes. However, if gnome-shell's internal accelerator grab table is stale (common after suspend/resume), the restarted daemons still get "Failed to grab accelerator" for standard media keys.

**Why**: GNOME Shell 46 handles standard media keys (volume, brightness) natively. The "Failed to grab accelerator" messages are actually harmless for standard keys — gnome-shell already owns them. gsd-media-keys IS still needed for custom keybindings (e.g., Ctrl+Alt+S for speak-selection).

**When keepalive is NOT enough**: If gnome-shell itself has stale state (post-sleep), even custom keybindings may not work. In this case:
1. `gnome-shell --replace` on X11 (WARNING: kills Cursor/Electron apps)
2. Or log out and back in

## Long-term Fix

Log out and log back in after the underlying issues (inotify, portals) are resolved. This allows GNOME session to properly start all services. After a fresh login, the keepalive timer becomes a safety net rather than a necessity.

## Related Issues

- inotify_exhaustion (resolved)
- Portal service failures (resolved via mask + relogin)
- gnome-shell stale grabs after sleep (see ubuntu_desktop knowledge: gnome_architecture.md)
