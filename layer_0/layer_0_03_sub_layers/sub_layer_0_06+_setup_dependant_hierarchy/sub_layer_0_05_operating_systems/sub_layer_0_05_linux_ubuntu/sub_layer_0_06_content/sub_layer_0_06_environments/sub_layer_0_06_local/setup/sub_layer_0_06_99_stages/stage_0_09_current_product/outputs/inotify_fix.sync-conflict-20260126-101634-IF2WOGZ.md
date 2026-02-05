# Inotify Limits Fix

## Problem

System entered "degraded" state with multiple failures:
- Volume/brightness keys not working
- Apps failing to open (Files, Terminal)
- xdg-desktop-portal services failing
- "No space left on device" errors in logs (inotify, not disk)

## Root Cause

Inotify watches/instances exhausted due to:
- Cursor IDE (21+ inotify instances)
- Multiple Node.js processes (MCP servers)
- Chrome browser
- Other Electron apps (Vibe Typer, Termius)

Default limits (65,536 watches / 128 instances) insufficient for modern dev environment.

## Solution

### 1. Increase Inotify Limits (Permanent)

```bash
# Create sysctl config
sudo tee /etc/sysctl.d/60-inotify.conf << 'EOF'
fs.inotify.max_user_watches = 1048576
fs.inotify.max_user_instances = 512
EOF

# Apply immediately
sudo sysctl --system

# Verify
cat /proc/sys/fs/inotify/max_user_watches   # Should show: 1048576
cat /proc/sys/fs/inotify/max_user_instances # Should show: 512
```

**This persists across reboots.**

### 2. Restart Desktop Session

After applying inotify fix, a fresh session is needed:

**Option A: Logout/Login (Preferred)**
- Click system menu → Log Out
- At login screen, ensure "Ubuntu" session is selected
- Log back in

**Option B: Reboot**
```bash
sudo reboot
```

### 3. Verify Fix

```bash
# Check system status
systemctl --user is-system-running  # Should show: running

# Check portal services
systemctl --user is-active xdg-desktop-portal xdg-desktop-portal-gtk

# Test functionality
# - Volume keys should work
# - Brightness keys should work
# - Apps should open normally
```

## If Portal Services Still Fail After Reboot

The xdg-desktop-portal-gnome service has a known crash bug. Workaround:

```bash
# Mask the crashing GNOME portal (use GTK portal instead)
systemctl --user mask xdg-desktop-portal-gnome

# Restart remaining portals
systemctl --user restart xdg-desktop-portal-gtk xdg-desktop-portal
```

## If Settings Daemons Not Running

Manually start critical daemons:

```bash
# Start media keys and power (for volume/brightness)
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &

# Start other useful daemons
for daemon in gsd-xsettings gsd-color gsd-keyboard gsd-housekeeping; do
  DISPLAY=:0 /usr/libexec/$daemon &
done
```

## File Locations

| File | Purpose |
|------|---------|
| `/etc/sysctl.d/60-inotify.conf` | Permanent inotify limits |
| `/proc/sys/fs/inotify/max_user_watches` | Current watch limit |
| `/proc/sys/fs/inotify/max_user_instances` | Current instance limit |

## Prevention

To reduce inotify usage:
1. Configure IDE to exclude `node_modules` from watching
2. Close unused Electron apps
3. Consolidate MCP server instances where possible

In VS Code/Cursor settings.json:
```json
{
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/.git/objects/**": true
  }
}
```

## Related Knowledge
- [Inotify Fundamentals](../../sub_layer_0_06_03_subx2_layers/sub_layer_01_linux_fundamentals/inotify.md)
- [GNOME Architecture](../../sub_layer_0_06_03_subx2_layers/sub_layer_02_ubuntu_desktop/gnome_architecture.md)
- [Systemd User Services](../../sub_layer_0_06_03_subx2_layers/sub_layer_03_system_services/systemd_user_services.md)

---
*Fixed: 2026-01-25*
*Environment: Ubuntu 24.04 LTS, GNOME Shell*
