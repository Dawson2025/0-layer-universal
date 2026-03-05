---
resource_id: "2e0c3f2b-5383-46ae-a49b-920c82ce5898"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_fix"
---
# Fix: XDG Portal / GNOME Apps Not Opening

## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

## Date
2026-01-28

## Fixes Applied

### Fix 1: Configure Portal to Use GTK Instead of GNOME

Created configuration to bypass the crashing GNOME portal:

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

### Fix 2: Systemd Service Overrides with DISPLAY

Created override files to provide DISPLAY environment variable:

**File**: `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf`
```ini
[Service]
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/home/dawson/.Xauthority"
```

**File**: `~/.config/systemd/user/xdg-desktop-portal-gnome.service.d/override.conf`
```ini
[Service]
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/home/dawson/.Xauthority"
```

**File**: `~/.config/systemd/user/xdg-desktop-portal-gtk.service.d/override.conf`
```ini
[Service]
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/home/dawson/.Xauthority"
```

**File**: `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf`
```ini
[Service]
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/home/dawson/.Xauthority"
```

### Fix 3: Manual Service Start (Immediate)

For immediate fix without reboot:
```bash
# Start terminal server
DISPLAY=:0 /usr/libexec/gnome-terminal-server &

# Start portals
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gtk &
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal &
```

### Fix 4: D-Bus Service Overrides (Most Reliable)

The systemd overrides don't work reliably for D-Bus activated services. Created local D-Bus service files that include DISPLAY:

**File**: `~/.local/share/dbus-1/services/org.gnome.Terminal.service`
```ini
[D-BUS Service]
Name=org.gnome.Terminal
Exec=/bin/sh -c 'DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/gnome-terminal-server'
```

**File**: `~/.local/share/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service`
```ini
[D-BUS Service]
Name=org.freedesktop.impl.portal.desktop.gtk
Exec=/bin/sh -c 'DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gtk'
```

### Fix 5: Autostart Script (Backup)

Created autostart script as backup in case D-Bus activation still fails:

**File**: `~/.config/autostart/fix-portal-services.desktop`
```ini
[Desktop Entry]
Type=Application
Name=Fix Portal Services
Exec=/home/dawson/.local/bin/fix-portal-services.sh
X-GNOME-Autostart-Delay=5
```

**File**: `~/.local/bin/fix-portal-services.sh`
```bash
#!/bin/bash
export DISPLAY=:0
export XAUTHORITY=/home/dawson/.Xauthority
sleep 3
pkill -9 -f xdg-desktop-portal 2>/dev/null
/usr/libexec/xdg-desktop-portal-gtk &
sleep 2
/usr/libexec/xdg-desktop-portal &
sleep 2
/usr/libexec/gnome-terminal-server &
logger "fix-portal-services: Portal and terminal services started"
```

### Apply Changes
```bash
systemctl --user daemon-reload
```

## Files Created/Modified

| File | Action | Purpose |
|------|--------|---------|
| `~/.config/xdg-desktop-portal/portals.conf` | Created | Use GTK portal instead of crashing GNOME portal |
| `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf` | Created | Add DISPLAY to main portal |
| `~/.config/systemd/user/xdg-desktop-portal-gnome.service.d/override.conf` | Created | Add DISPLAY to GNOME portal |
| `~/.config/systemd/user/xdg-desktop-portal-gtk.service.d/override.conf` | Existed | Already had DISPLAY |
| `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf` | Created | Add DISPLAY to terminal server |
| `~/.local/share/dbus-1/services/org.gnome.Terminal.service` | Created | D-Bus activation with DISPLAY |
| `~/.local/share/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service` | Created | D-Bus activation with DISPLAY |
| `~/.config/autostart/fix-portal-services.desktop` | Created | Autostart backup fix |
| `~/.local/bin/fix-portal-services.sh` | Created | Script to start services |

## Verification
```bash
# Check apps open
nautilus ~
gnome-terminal

# Check services
pgrep -f gnome-terminal-server
pgrep -f xdg-desktop-portal
```

## Result
- Files app: Working
- Terminal app: Working (via D-Bus override)
