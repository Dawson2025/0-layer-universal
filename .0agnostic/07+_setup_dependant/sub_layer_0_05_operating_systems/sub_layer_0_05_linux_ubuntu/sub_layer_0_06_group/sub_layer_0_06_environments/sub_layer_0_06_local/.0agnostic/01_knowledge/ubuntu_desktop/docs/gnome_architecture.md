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

## GNOME Shell 46 Native Media Key Handling

**Critical**: On GNOME Shell 46, the compositor handles standard media keys (volume, brightness, media controls) NATIVELY via mutter's built-in keybinding system. This means:

- gsd-media-keys "Failed to grab accelerator" warnings for standard keys are **HARMLESS**
- gnome-shell already owns these grabs via `org.gnome.Shell.GrabAccelerator` D-Bus API
- gsd-media-keys IS still needed for **custom keybindings** (e.g., `org.gnome.settings-daemon.plugins.media-keys.custom-keybindings`)

### GrabAccelerator D-Bus API

gnome-shell exposes `org.gnome.Shell.GrabAccelerator` at `/org/gnome/Shell`. gsd-media-keys calls this to register key grabs. Standard media keys are pre-grabbed by gnome-shell itself.

## Settings Daemons (gsd-*)

Located in `/usr/libexec/gsd-*`, these handle various desktop functions:

| Daemon | Function | Shell 46 Note |
|--------|----------|---------------|
| `gsd-media-keys` | Custom keybindings | Standard keys handled by Shell natively |
| `gsd-power` | Power management, lid switch | Brightness handled by Shell natively |
| `gsd-keyboard` | Keyboard settings, layouts | |
| `gsd-color` | Display color profiles | |
| `gsd-xsettings` | X11 settings synchronization | |
| `gsd-housekeeping` | Disk space monitoring, cleanup | |

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

## Post-Sleep / Post-Wake Issues

After suspend/resume, gnome-shell's internal accelerator grab table can become corrupted (stale state). Symptoms:
- Volume/brightness buttons stop working
- Custom keybindings stop responding
- gsd-media-keys restart still gets "Failed to grab accelerator" even after process restart
- The keepalive timer restarts gsd-* processes but CANNOT fix stale gnome-shell grabs

### Recovery Protocol

1. **`gnome-shell --replace`** (X11 only): Restarts gnome-shell, clears stale grabs, preserves windows. **WARNING**: Kills Cursor/Electron apps that depend on the compositor. Safest to save work first.
2. **Log out and back in**: Cleanest option, restarts entire session.
3. **Verify after recovery**: `xdotool key XF86AudioRaiseVolume` then check `pactl get-sink-volume @DEFAULT_SINK@` to confirm volume changes.

## Common Failure Modes

1. **Missing SessionManager**: gsd-* daemons can't register
2. **Portal crashes**: File dialogs, app launching broken
3. **Display access**: Services can't connect to X11/Wayland
4. **D-Bus issues**: Inter-process communication fails
5. **Inotify exhaustion**: Services fail to start, systemd gives up
6. **Stale gnome-shell grabs**: After sleep/wake, shell's grab table corrupted (see Post-Sleep section above)

## Settings Daemon Recovery

### Why They Don't Auto-Restart

gsd-* services are configured with `RefuseManualStart=true`:
- Can only be started by gnome-session
- Systemd gives up after 5 rapid restart failures
- Manual `/usr/libexec/gsd-*` runs work but aren't managed

### Recovery Options

1. **Log out and back in** - Cleanest, lets gnome-session restart everything
2. **Manual restart** - `DISPLAY=:0 /usr/libexec/gsd-media-keys &`
3. **Keepalive timer** - Periodic check and restart (see gsd_keepalive_fix.md)

### Symptoms of Failed gsd-*

| Daemon | Symptom |
|--------|---------|
| `gsd-media-keys` | Volume buttons don't work |
| `gsd-power` | Brightness buttons don't work |
| `gsd-keyboard` | Keyboard shortcuts broken |

## Related Documentation
- [Linux Fundamentals](../../linux_fundamentals/docs/)
- [System Services](../../system_services/docs/)
- [Audio Stack](../../audio/docs/)
