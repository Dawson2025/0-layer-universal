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

### No Other Fixes Needed

The Cycle 1 design changes (environment.d, display-ready ExecStartPost, keepalive rewrite, cleanup) remain unchanged. Only the GDK_BACKEND addition was needed.
