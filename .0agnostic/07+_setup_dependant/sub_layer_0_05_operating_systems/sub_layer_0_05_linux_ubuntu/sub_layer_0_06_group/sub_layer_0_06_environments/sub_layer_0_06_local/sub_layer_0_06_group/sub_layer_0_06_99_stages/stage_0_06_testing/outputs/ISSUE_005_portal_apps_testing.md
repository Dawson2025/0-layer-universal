---
resource_id: "5d34df75-3eb6-4845-82e3-be36f462c822"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_testing"
---
# Testing: XDG Portal / GNOME Apps Not Opening

## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

## Date
2026-01-28

## Symptoms Reported
- Files app (Nautilus) would not open
- Terminal app (gnome-terminal) would not open
- Apps launched but no window appeared

## Test Performed

### 1. Check User Journal for Errors
```bash
journalctl --user -p err -n 50 --no-pager
```

**Results:**
- `xdg-desktop-portal-gnome.service` - Failed with SEGFAULT (signal 11)
- `xdg-desktop-portal-gtk.service` - "cannot open display: :0"
- `gnome-terminal-server.service` - "Cannot open display:"
- `xdg-desktop-portal.service` - Timeout waiting for portal implementations

### 2. Check Portal Service Status
```bash
systemctl --user status xdg-desktop-portal-gnome.service
```

**Results:**
```
Active: failed (Result: core-dump)
Process: ExecStart=/usr/libexec/xdg-desktop-portal-gnome (code=dumped, signal=SEGV)
```

### 3. Check Terminal Server Status
```bash
systemctl --user status gnome-terminal-server.service
```

**Results:**
```
Active: failed (Result: exit-code)
gnome-terminal-server: Failed to parse arguments: Cannot open display:
```

### 4. Manual Launch Test
```bash
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gnome &
```

**Result:** Process started and stayed running when DISPLAY was set manually.

## Root Causes Identified

1. **xdg-desktop-portal-gnome**: Crashing with SEGFAULT when started by systemd
2. **xdg-desktop-portal-gtk**: Missing DISPLAY environment variable
3. **gnome-terminal-server**: Missing DISPLAY environment variable
4. **All services**: Systemd user services don't inherit session DISPLAY variable

## Conclusion
Multiple XDG desktop portal services are failing due to:
1. A bug causing GNOME portal to crash
2. Missing DISPLAY environment variable in systemd service context

These services are required for GNOME apps to function properly.
