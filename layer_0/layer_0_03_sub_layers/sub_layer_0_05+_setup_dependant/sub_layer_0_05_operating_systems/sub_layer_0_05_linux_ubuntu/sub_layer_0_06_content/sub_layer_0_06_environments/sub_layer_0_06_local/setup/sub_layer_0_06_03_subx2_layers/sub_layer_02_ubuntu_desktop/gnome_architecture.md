# Ubuntu Desktop Architecture (GNOME-based)

## Overview

Ubuntu's default desktop is based on GNOME Shell with Ubuntu-specific customizations.

## Core Components

### GNOME Shell (`gnome-shell`)
- The main desktop compositor and UI
- Handles window management, panels, notifications
- Provides built-in portal (`org.gnome.Shell.Portal`)

### GNOME Session (`gnome-session-binary`)
- Manages desktop session lifecycle
- Starts and monitors settings daemons
- Provides `org.gnome.SessionManager` D-Bus service
- **Critical**: Many services depend on this being available

### Display Manager (`lightdm` or `gdm3`)
- Handles login screen
- Starts the user session
- Sets up initial environment

## Settings Daemons (gsd-*)

Located in `/usr/libexec/gsd-*`, these handle various desktop functions:

| Daemon | Function |
|--------|----------|
| `gsd-media-keys` | Volume, brightness, media controls |
| `gsd-power` | Power management, brightness |
| `gsd-keyboard` | Keyboard settings, layouts |
| `gsd-color` | Display color profiles |
| `gsd-xsettings` | X11 settings synchronization |
| `gsd-housekeeping` | Disk space monitoring, cleanup |

### Dependencies
All gsd-* daemons require:
1. D-Bus session bus
2. `org.gnome.SessionManager` (for registration)
3. Display access (`DISPLAY` environment variable)

## XDG Desktop Portals

Portals provide sandboxed access to desktop features:

| Portal | Purpose |
|--------|---------|
| `xdg-desktop-portal` | Main coordinator |
| `xdg-desktop-portal-gtk` | GTK file dialogs, settings |
| `xdg-desktop-portal-gnome` | GNOME-specific features |

### Portal Dependencies
- D-Bus session bus
- Display access
- PipeWire (for screen sharing)

## Session Startup Flow

```
lightdm/gdm3
    └── gnome-session-binary --session=ubuntu
        ├── gnome-shell
        ├── xdg-desktop-portal*
        └── gsd-* daemons (started on demand)
```

## Common Failure Modes

1. **Missing SessionManager**: gsd-* daemons can't register
2. **Portal crashes**: File dialogs, app launching broken
3. **Display access**: Services can't connect to X11/Wayland
4. **D-Bus issues**: Inter-process communication fails

## Related Documentation
- [Linux Fundamentals](../sub_layer_01_linux_fundamentals/)
- [System Services](../sub_layer_03_system_services/)
