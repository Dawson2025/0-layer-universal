---
resource_id: "2e0c3f2b-5383-46ae-a49b-920c82ce5898"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_fix"
---
# Fix: XDG Portal / GNOME Apps Not Opening

<!-- section_id: "7b2d09d1-c5f6-4c27-a76e-67c742f4c4fc" -->
## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

<!-- section_id: "42571acd-5c06-4a5e-932b-bf18ea953814" -->
## Date
2026-01-28

<!-- section_id: "eec90fac-cad0-4806-ae79-b379f97c92d8" -->
## Fixes Applied

<!-- section_id: "9abed779-f18b-4664-8079-999ee4c8154b" -->
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

<!-- section_id: "44c760cc-7569-451b-bbe3-2686839f358c" -->
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

<!-- section_id: "ec0b0b37-3097-46fc-97af-f03dc81f27e5" -->
### Fix 3: Manual Service Start (Immediate)

For immediate fix without reboot:
```bash
# Start terminal server
DISPLAY=:0 /usr/libexec/gnome-terminal-server &

# Start portals
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gtk &
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal &
```

<!-- section_id: "73318aa4-7d5b-4c44-abe8-7323ac28e16f" -->
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

<!-- section_id: "78cc5f87-6701-47e2-9a13-cf8f4374ac34" -->
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

<!-- section_id: "2008fcfa-4d31-4e1d-a8e6-1dd77e5751f2" -->
### Apply Changes
```bash
systemctl --user daemon-reload
```

<!-- section_id: "1932b729-1016-4019-8f32-398264d1e31c" -->
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

<!-- section_id: "f3d522f1-7bc7-42e1-b8fe-0b7bacfb19eb" -->
## Verification
```bash
# Check apps open
nautilus ~
gnome-terminal

# Check services
pgrep -f gnome-terminal-server
pgrep -f xdg-desktop-portal
```

<!-- section_id: "dac8163e-23a2-4c44-a58c-4811bf37b29c" -->
## Result
- Files app: Working
- Terminal app: Working (via D-Bus override)
