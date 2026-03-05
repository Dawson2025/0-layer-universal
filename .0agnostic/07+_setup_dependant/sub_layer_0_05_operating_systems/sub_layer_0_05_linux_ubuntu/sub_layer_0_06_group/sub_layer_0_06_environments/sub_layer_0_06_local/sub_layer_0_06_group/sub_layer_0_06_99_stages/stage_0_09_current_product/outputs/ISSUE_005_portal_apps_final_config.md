---
resource_id: "f711e94e-3ce1-4f42-a74d-0f7c177b5c0c"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_final_config"
---
# Final Configuration: XDG Portal / GNOME Apps Fix

<!-- section_id: "23ac5188-b37c-437d-9aaf-fcf2d0e70632" -->
## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

<!-- section_id: "c0937423-614d-4867-9386-b2745bb26b28" -->
## Date
2026-01-28

<!-- section_id: "eac300eb-4f32-4c52-84d0-526528f1a065" -->
## Status
**RESOLVED** - Files and Terminal apps now open reliably

---

<!-- section_id: "fcdf072b-cca7-45d7-837b-478b756e8c37" -->
## Problem Solved

GNOME apps (Files, Terminal) would not open due to:
1. xdg-desktop-portal-gnome crashing with SEGFAULT
2. Portal and terminal services lacking DISPLAY environment variable

---

<!-- section_id: "bbb12d24-6c88-4972-aa24-95c1d7603791" -->
## Current Configuration

<!-- section_id: "c163747a-0d1f-4be2-9138-1ccf731adf9e" -->
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

<!-- section_id: "e9f70e54-f3c9-44e5-a88b-299fb28ac491" -->
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

<!-- section_id: "8c03dca9-eeb6-49e7-8b8d-9ad6989fd676" -->
### Systemd Overrides (in `~/.config/systemd/user/`)

| Service | Override File | Content |
|---------|---------------|---------|
| xdg-desktop-portal | xdg-desktop-portal.service.d/override.conf | Environment=DISPLAY=:0 |
| xdg-desktop-portal-gnome | xdg-desktop-portal-gnome.service.d/override.conf | Environment=DISPLAY=:0 |
| xdg-desktop-portal-gtk | xdg-desktop-portal-gtk.service.d/override.conf | Environment=DISPLAY=:0 |
| gnome-terminal-server | gnome-terminal-server.service.d/override.conf | Environment=DISPLAY=:0 |

<!-- section_id: "84032f23-d646-4fc0-b3b6-6bf19e0e1e05" -->
### Autostart Backup
**File**: `~/.config/autostart/fix-portal-services.desktop` + `~/.local/bin/fix-portal-services.sh`

---

<!-- section_id: "8eb5e6e7-440a-4257-a72b-bd9c2debaf47" -->
## Recovery Commands

<!-- section_id: "cc130d89-e820-4d58-9ba7-e518e636eb92" -->
### If Terminal Won't Open
```bash
# Kill and restart terminal server
pkill -9 gnome-terminal-server
DISPLAY=:0 /usr/libexec/gnome-terminal-server &
gnome-terminal
```

<!-- section_id: "39e30917-465f-4258-90ca-9844903be3ce" -->
### If Files Won't Open
```bash
# Kill and restart portals
pkill -9 -f xdg-desktop-portal
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gtk &
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal &
nautilus ~
```

<!-- section_id: "7e79512e-a3f4-4d48-bb95-49da53c1e1fa" -->
### Full Reset
```bash
~/.local/bin/fix-portal-services.sh
```

---

<!-- section_id: "c284e07d-abb8-4d55-b152-faea622310bc" -->
## Known Limitations

1. **GNOME Portal Crash**: The xdg-desktop-portal-gnome package has a bug causing SEGFAULT. Workaround: Use GTK portal instead.
2. **D-Bus vs Systemd**: D-Bus activation doesn't always respect systemd overrides. Workaround: Local D-Bus service files.
3. **First Boot**: May need manual intervention on first boot after kernel update.

---

<!-- section_id: "39327f34-aea4-402c-8d59-42cefabef2f3" -->
## Related Documentation

| Stage | Document |
|-------|----------|
| Testing | `stage_0_06_testing/outputs/ISSUE_005_portal_apps_testing.md` |
| Criticism | `stage_0_07_criticism/outputs/ISSUE_005_portal_apps_criticism.md` |
| Fixing | `stage_0_08_fixing/outputs/ISSUE_005_portal_apps_fix.md` |
