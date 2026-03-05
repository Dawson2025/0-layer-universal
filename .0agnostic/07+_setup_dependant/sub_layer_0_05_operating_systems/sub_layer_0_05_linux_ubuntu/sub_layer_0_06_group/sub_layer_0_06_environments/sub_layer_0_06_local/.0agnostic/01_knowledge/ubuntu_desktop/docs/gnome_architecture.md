---
resource_id: "afcaad7e-60f8-46b2-87a0-7682c5ad1161"
resource_type: "knowledge"
resource_name: "gnome_architecture"
---
# Ubuntu Desktop Architecture (GNOME-based)

<!-- section_id: "ff21fe1c-d075-4d8d-9147-2e40f682bfa0" -->
## Overview

Ubuntu's default desktop is based on GNOME Shell with Ubuntu-specific customizations.

<!-- section_id: "41b6f2b0-117a-45a8-bc50-756b38c05de1" -->
## Core Components

<!-- section_id: "b0996c2b-3353-4ab2-b99f-dd107f901919" -->
### GNOME Shell (`gnome-shell`)
- The main desktop compositor and UI
- Handles window management, panels, notifications
- Provides built-in portal (`org.gnome.Shell.Portal`)

<!-- section_id: "e40d14e2-7c62-4772-8928-effa70dbd276" -->
### GNOME Session (`gnome-session-binary`)
- Manages desktop session lifecycle
- Starts and monitors settings daemons
- Provides `org.gnome.SessionManager` D-Bus service
- **Critical**: Many services depend on this being available

<!-- section_id: "2508c9a7-eaa2-4471-a018-637b516e65c1" -->
### Display Manager (`lightdm` or `gdm3`)
- Handles login screen
- Starts the user session
- Sets up initial environment

<!-- section_id: "045be278-b43c-43c5-b00c-e4a29da55c4e" -->
## GNOME Shell 46 Native Media Key Handling

**Critical**: On GNOME Shell 46, the compositor handles standard media keys (volume, brightness, media controls) NATIVELY via mutter's built-in keybinding system. This means:

- gsd-media-keys "Failed to grab accelerator" warnings for standard keys are **HARMLESS**
- gnome-shell already owns these grabs via `org.gnome.Shell.GrabAccelerator` D-Bus API
- gsd-media-keys IS still needed for **custom keybindings** (e.g., `org.gnome.settings-daemon.plugins.media-keys.custom-keybindings`)

<!-- section_id: "efcb17e6-0b79-4caf-a627-48c39cbc0720" -->
### GrabAccelerator D-Bus API

gnome-shell exposes `org.gnome.Shell.GrabAccelerator` at `/org/gnome/Shell`. gsd-media-keys calls this to register key grabs. Standard media keys are pre-grabbed by gnome-shell itself.

<!-- section_id: "ffb64460-1c37-4bbd-af8f-b7854ce8f400" -->
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

<!-- section_id: "3729a007-e7b1-4edb-968b-739dd15e4e95" -->
### Dependencies
All gsd-* daemons require:
1. D-Bus session bus
2. `org.gnome.SessionManager` (for registration)
3. Display access (`DISPLAY` environment variable)

<!-- section_id: "97f2932a-47e0-40a6-a068-79edebf9e21e" -->
## XDG Desktop Portals

Portals provide sandboxed access to desktop features:

| Portal | Purpose |
|--------|---------|
| `xdg-desktop-portal` | Main coordinator |
| `xdg-desktop-portal-gtk` | GTK file dialogs, settings |
| `xdg-desktop-portal-gnome` | GNOME-specific features |

<!-- section_id: "4fb97905-09da-4a46-8342-198d7e4e926e" -->
### Portal Dependencies
- D-Bus session bus
- Display access
- PipeWire (for screen sharing)

<!-- section_id: "7a3039a2-99aa-48b5-9e63-1fd5266c95b0" -->
## Session Startup Flow

```
lightdm/gdm3
    └── gnome-session-binary --session=ubuntu
        ├── gnome-shell
        ├── xdg-desktop-portal*
        └── gsd-* daemons (started on demand)
```

<!-- section_id: "74bf53a9-eb53-4a28-810e-be9e8113c558" -->
## Post-Sleep / Post-Wake Issues

After suspend/resume, gnome-shell's internal accelerator grab table can become corrupted (stale state). Symptoms:
- Volume/brightness buttons stop working
- Custom keybindings stop responding
- gsd-media-keys restart still gets "Failed to grab accelerator" even after process restart
- The keepalive timer restarts gsd-* processes but CANNOT fix stale gnome-shell grabs

<!-- section_id: "25b79c4b-849f-4fcc-b65e-8a73252d464d" -->
### Recovery Protocol

1. **`gnome-shell --replace`** (X11 only): Restarts gnome-shell, clears stale grabs, preserves windows. **WARNING**: Kills Cursor/Electron apps that depend on the compositor. Safest to save work first.
2. **Log out and back in**: Cleanest option, restarts entire session.
3. **Verify after recovery**: `xdotool key XF86AudioRaiseVolume` then check `pactl get-sink-volume @DEFAULT_SINK@` to confirm volume changes.

<!-- section_id: "b68b50a7-c043-49f1-ae9d-e8934de2456d" -->
## Common Failure Modes

1. **Missing SessionManager**: gsd-* daemons can't register
2. **Portal crashes**: File dialogs, app launching broken
3. **Display access**: Services can't connect to X11/Wayland
4. **D-Bus issues**: Inter-process communication fails
5. **Inotify exhaustion**: Services fail to start, systemd gives up
6. **Stale gnome-shell grabs**: After sleep/wake, shell's grab table corrupted (see Post-Sleep section above)

<!-- section_id: "3d6be459-9476-4613-9ea3-673f437895be" -->
## Settings Daemon Recovery

<!-- section_id: "71cac11b-403f-4be5-935f-00390e0051fd" -->
### Why They Don't Auto-Restart

gsd-* services are configured with `RefuseManualStart=true`:
- Can only be started by gnome-session
- Systemd gives up after 5 rapid restart failures
- Manual `/usr/libexec/gsd-*` runs work but aren't managed

<!-- section_id: "bb1851b9-952d-4c8e-8822-9d57ce744c70" -->
### Recovery Options

1. **Log out and back in** - Cleanest, lets gnome-session restart everything
2. **Manual restart** - `DISPLAY=:0 /usr/libexec/gsd-media-keys &`
3. **Keepalive timer** - Periodic check and restart (see gsd_keepalive_fix.md)

<!-- section_id: "98ed29db-5758-4634-811c-c0df06802a32" -->
### Symptoms of Failed gsd-*

| Daemon | Symptom |
|--------|---------|
| `gsd-media-keys` | Volume buttons don't work |
| `gsd-power` | Brightness buttons don't work |
| `gsd-keyboard` | Keyboard shortcuts broken |

<!-- section_id: "b0596ac0-e421-4fee-8c7d-74deb1d74360" -->
## Related Documentation
- [Linux Fundamentals](../../linux_fundamentals/docs/)
- [System Services](../../system_services/docs/)
- [Audio Stack](../../audio/docs/)
