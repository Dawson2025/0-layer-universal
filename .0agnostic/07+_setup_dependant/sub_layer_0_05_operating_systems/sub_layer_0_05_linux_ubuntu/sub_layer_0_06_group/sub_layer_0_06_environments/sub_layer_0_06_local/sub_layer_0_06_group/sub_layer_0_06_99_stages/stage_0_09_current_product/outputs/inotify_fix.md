---
resource_id: "6f8047e4-a0e2-4417-8462-244b14dafb2c"
resource_type: "output"
resource_name: "inotify_fix"
---
# Inotify Limits Fix

<!-- section_id: "345228a9-7c95-48b6-93fd-19c18fdd5a8c" -->
## Problem

System entered "degraded" state with multiple failures:
- Volume/brightness keys not working
- Apps failing to open (Files, Terminal)
- xdg-desktop-portal services failing
- "No space left on device" errors in logs (inotify, not disk)

<!-- section_id: "17d1f9a6-467b-4d17-b271-0aa58c36ee21" -->
## Root Cause

Inotify watches/instances exhausted due to:
- Cursor IDE (21+ inotify instances)
- Multiple Node.js processes (MCP servers)
- Chrome browser
- Other Electron apps (Vibe Typer, Termius)

Default limits (65,536 watches / 128 instances) insufficient for modern dev environment.

<!-- section_id: "7218652a-93e2-4a31-9f39-ceef5d7dd361" -->
## Solution

<!-- section_id: "13c9180e-5d89-4f95-88ef-a496edc43bee" -->
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

<!-- section_id: "1bc7aef1-3f82-427f-b62f-c23d3ed90d2c" -->
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

<!-- section_id: "528356d1-6fb8-4b67-8a36-9b96b890fac0" -->
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

<!-- section_id: "67d29295-9764-4cca-8beb-e5aa76fd4ac9" -->
## If Portal Services Still Fail After Reboot

The xdg-desktop-portal-gnome service has a known crash bug. Workaround:

```bash
# Mask the crashing GNOME portal (use GTK portal instead)
systemctl --user mask xdg-desktop-portal-gnome

# Restart remaining portals
systemctl --user restart xdg-desktop-portal-gtk xdg-desktop-portal
```

<!-- section_id: "0481bcc0-0320-417d-b2c7-47fefc65c3f0" -->
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

<!-- section_id: "9a28d218-1cdc-4f4a-95bb-6a4bea129f7d" -->
## File Locations

| File | Purpose |
|------|---------|
| `/etc/sysctl.d/60-inotify.conf` | Permanent inotify limits |
| `/proc/sys/fs/inotify/max_user_watches` | Current watch limit |
| `/proc/sys/fs/inotify/max_user_instances` | Current instance limit |

<!-- section_id: "423cb556-61ee-4f55-840a-f423e63bebf6" -->
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

<!-- section_id: "c2f22c21-a244-491c-8ecf-538bcd90bf3d" -->
## Related Knowledge
- [Inotify Fundamentals](../../sub_layer_0_06_03_subx2_layers/sub_layer_01_linux_fundamentals/inotify.md)
- [GNOME Architecture](../../sub_layer_0_06_03_subx2_layers/sub_layer_02_ubuntu_desktop/gnome_architecture.md)
- [Systemd User Services](../../sub_layer_0_06_03_subx2_layers/sub_layer_03_system_services/systemd_user_services.md)

---
*Fixed: 2026-01-25*
*Environment: Ubuntu 24.04 LTS, GNOME Shell*
