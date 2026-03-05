---
resource_id: "f711e94e-3ce1-4f42-a74d-0f7c177b5c0c"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_final_config"
---
# Final Configuration: XDG Portal / GNOME Apps Fix

## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

## Date
2026-01-28

## Status
**RESOLVED** - Files and Terminal apps now open reliably

---

## Problem Solved

GNOME apps (Files, Terminal) would not open due to:
1. xdg-desktop-portal-gnome crashing with SEGFAULT
2. Portal and terminal services lacking DISPLAY environment variable

---

## Current Configuration

### Portal Configuration
**File**: `~/.config/xdg-desktop-portal/portals.conf`
```ini
[preferred]
default=gtk
org.freedesktop.impl.portal.Settings=gtk
org.freedesktop.impl.portal.FileChooser=gtk
org.freedesktop.impl.portal.AppChooser=gtk
org.freedesktop.impl.portal.Print=gtk
org.freedesktop.impl.portal.Screenshot=gtk
```

### D-Bus Service Overrides

**Terminal Server**: `~/.local/share/dbus-1/services/org.gnome.Terminal.service`
```ini
[D-BUS Service]
Name=org.gnome.Terminal
Exec=/bin/sh -c 'DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/gnome-terminal-server'
```

**Portal GTK**: `~/.local/share/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service`
```ini
[D-BUS Service]
Name=org.freedesktop.impl.portal.desktop.gtk
Exec=/bin/sh -c 'DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gtk'
```

### Systemd Overrides (in `~/.config/systemd/user/`)

| Service | Override File | Content |
|---------|---------------|---------|
| xdg-desktop-portal | xdg-desktop-portal.service.d/override.conf | Environment=DISPLAY=:0 |
| xdg-desktop-portal-gnome | xdg-desktop-portal-gnome.service.d/override.conf | Environment=DISPLAY=:0 |
| xdg-desktop-portal-gtk | xdg-desktop-portal-gtk.service.d/override.conf | Environment=DISPLAY=:0 |
| gnome-terminal-server | gnome-terminal-server.service.d/override.conf | Environment=DISPLAY=:0 |

### Autostart Backup
**File**: `~/.config/autostart/fix-portal-services.desktop` + `~/.local/bin/fix-portal-services.sh`

---

## Recovery Commands

### If Terminal Won't Open
```bash
# Kill and restart terminal server
pkill -9 gnome-terminal-server
DISPLAY=:0 /usr/libexec/gnome-terminal-server &
gnome-terminal
```

### If Files Won't Open
```bash
# Kill and restart portals
pkill -9 -f xdg-desktop-portal
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gtk &
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal &
nautilus ~
```

### Full Reset
```bash
~/.local/bin/fix-portal-services.sh
```

---

## Known Limitations

1. **GNOME Portal Crash**: The xdg-desktop-portal-gnome package has a bug causing SEGFAULT. Workaround: Use GTK portal instead.
2. **D-Bus vs Systemd**: D-Bus activation doesn't always respect systemd overrides. Workaround: Local D-Bus service files.
3. **First Boot**: May need manual intervention on first boot after kernel update.

---

## Related Documentation

| Stage | Document |
|-------|----------|
| Testing | `stage_0_06_testing/outputs/ISSUE_005_portal_apps_testing.md` |
| Criticism | `stage_0_07_criticism/outputs/ISSUE_005_portal_apps_criticism.md` |
| Fixing | `stage_0_08_fixing/outputs/ISSUE_005_portal_apps_fix.md` |
