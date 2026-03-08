---
resource_id: "e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b"
resource_type: "output"
resource_name: "fixes_applied"
---

# GSD Session Startup — Fixes Applied (Post-Criticism)

## Date: 2026-03-06

### Fix 1: GDK_BACKEND Override (Cycle 2 addition)

**Problem discovered**: nvidia-wayland.conf sets `GDK_BACKEND=wayland` globally in the systemd user environment. gsd-media-keys and gsd-power use GDK which respects this variable, causing them to try connecting to a non-existent Wayland display instead of X11.

**Fix**: Created service drop-in directories with `GDK_BACKEND=x11`:
- `~/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf`
- `~/.config/systemd/user/org.gnome.SettingsDaemon.Power.service.d/display.conf`

Each contains:
```ini
[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/dawson/.Xauthority
Environment=GDK_BACKEND=x11
```

**Result**: Both services now start successfully via systemd targets.

### No Other Fixes Needed (Cycle 2)

The Cycle 1 design changes (environment.d, display-ready ExecStartPost, keepalive rewrite, cleanup) remain unchanged. Only the GDK_BACKEND addition was needed.

---

## Cycle 3 Fixes (2026-03-07)

### Fix 2: Global GDK_BACKEND=x11 Override

**Problem discovered**: Per-service drop-ins (Cycle 2) only fixed MediaKeys and Power. Post-reboot testing revealed that ALL D-Bus-activated GDK services/apps inherit `GDK_BACKEND=wayland` from nvidia-wayland.conf, including:
- gsd-Color, gsd-Keyboard, gsd-Wacom (5-crash pattern, same as MediaKeys/Power)
- xdg-desktop-portal-gnome (SEGV)
- Desktop apps launched from toolbar (Nautilus, Settings, Terminal, OBS)

**Fix**: Created `~/.config/environment.d/zz-x11-session.conf`:
```ini
GDK_BACKEND=x11
```
Sorts after `nvidia-wayland.conf` alphabetically (z > n), overriding `GDK_BACKEND=wayland` for ALL systemd user services.

### Fix 3: Extended Keepalive Service

**Problem**: gsd-keepalive.service only monitored MediaKeys and Power. Color, Keyboard, and Wacom were left unmanaged.

**Fix**: Added Color, Keyboard, Wacom to the keepalive loop in `~/.config/systemd/user/gsd-keepalive.service`.

### Fix 4: Portal/Terminal Drop-in Updates (Defense-in-Depth)

Added `GDK_BACKEND=x11` to existing drop-ins for:
- `xdg-desktop-portal-gnome.service.d/override.conf`
- `xdg-desktop-portal-gtk.service.d/override.conf`
- `xdg-desktop-portal.service.d/override.conf`
- `gnome-terminal-server.service.d/override.conf`

**Result**: All 5 gsd services active, portal running, toolbar apps launching.
