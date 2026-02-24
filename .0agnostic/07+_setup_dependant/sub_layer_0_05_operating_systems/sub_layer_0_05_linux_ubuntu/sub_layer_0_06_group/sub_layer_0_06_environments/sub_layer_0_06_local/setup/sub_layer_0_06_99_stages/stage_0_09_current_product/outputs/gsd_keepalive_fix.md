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

## Long-term Fix

Log out and log back in after the underlying issues (inotify, portals) are resolved. This allows GNOME session to properly start all services. After a fresh login, the keepalive timer becomes a safety net rather than a necessity.

## Related Issues

- inotify_exhaustion (resolved)
- Portal service failures (resolved via mask + relogin)
