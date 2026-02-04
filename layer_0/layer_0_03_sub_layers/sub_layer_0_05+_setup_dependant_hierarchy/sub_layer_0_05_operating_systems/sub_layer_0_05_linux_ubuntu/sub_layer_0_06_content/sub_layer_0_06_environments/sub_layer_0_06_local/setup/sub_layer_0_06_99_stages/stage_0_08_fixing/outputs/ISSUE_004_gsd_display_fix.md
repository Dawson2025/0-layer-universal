# Fix: GSD DISPLAY Environment Variable Issue

## Issue Reference
ISSUE_004 - GSD Daemons Fail After Reboot Due to Missing DISPLAY

## Date
2026-01-26

## Fix Applied

### 1. Immediate Fix (Manual)
Started daemons manually with DISPLAY set:
```bash
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```

### 2. Permanent Fix (Service Update)
Added `Environment=DISPLAY=:0` to the systemd service file.

**File**: `~/.config/systemd/user/gsd-keepalive.service`

**Change Made**:
```diff
 [Service]
 Type=oneshot
 RemainAfterExit=yes
+Environment=DISPLAY=:0
 ExecStart=/bin/bash -c 'pgrep -x gsd-media-keys || /usr/libexec/gsd-media-keys & pgrep -x gsd-power || /usr/libexec/gsd-power &'
```

### 3. Reload Systemd
```bash
systemctl --user daemon-reload
```

## Updated Service File (Complete)
```ini
[Unit]
Description=Keep GNOME Settings Daemons alive
After=graphical-session.target

[Service]
Type=oneshot
RemainAfterExit=yes
Environment=DISPLAY=:0
ExecStart=/bin/bash -c 'pgrep -x gsd-media-keys || /usr/libexec/gsd-media-keys & pgrep -x gsd-power || /usr/libexec/gsd-power &'
ExecStop=/bin/true

[Install]
WantedBy=default.target
```

## Verification
```bash
# Check daemons are running
pgrep -a gsd-media-keys
pgrep -a gsd-power

# Test volume buttons - should work
# Test brightness buttons - should work
```

## Result
- Volume buttons: Working
- Brightness buttons: Working
- Persists after reboot: Yes (with updated service)
