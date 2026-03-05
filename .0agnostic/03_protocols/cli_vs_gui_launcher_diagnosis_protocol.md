---
resource_id: "38845c1d-f1f7-417a-bbe2-f80a3502f163"
resource_type: "protocol"
resource_name: "cli_vs_gui_launcher_diagnosis_protocol"
---
# Protocol: CLI vs GUI Launcher Diagnosis & Recovery

**Date Created**: 2026-02-26
**Status**: Active
**Scope**: Ubuntu/Linux systems where CLI commands work but GUI icon launches fail

---

## Problem Pattern

**Symptoms:**
- Application launches successfully via terminal: `nautilus`, `gnome-control-center`, `gedit`, etc.
- Same application fails silently or crashes when launched via GUI icon
- Some icons work fine (Firefox, Chrome, etc.)
- Inconsistent behavior across different applications

**Root Cause Categories:**
1. **Missing environment variables** (DISPLAY, XAUTHORITY, DBUS_SESSION_BUS_ADDRESS)
2. **Broken .desktop file** (launcher configuration)
3. **Session state issue** (D-Bus services not registered)
4. **Working directory mismatch** (app expects specific CWD)
5. **Permissions issue** (app can't access config/data dirs)

---

## Diagnosis Steps

### Step 1: Verify CLI Works
```bash
# Test the application via terminal
nautilus &
gnome-control-center &
gedit &
```
**Expected**: Application opens and functions normally.

### Step 2: Check Desktop File
```bash
# Find the .desktop file
find ~/.local/share/applications ~/.config -name "*.desktop" | grep -i nautilus

# Examine the launcher
cat ~/.local/share/applications/org.gnome.Nautilus.desktop
```
**Look for**: Exec line, Terminal=true/false, Environment variables

### Step 3: Capture Working Environment
```bash
# When CLI works, capture the environment
env | grep -E "DISPLAY|DBUS|XAUTH|PATH" > /tmp/working_env.txt

# Then try to launch via icon and capture any errors
# (If launcher runs in background, check: ~/.local/share/recently-used.xbel, journalctl)
```

### Step 4: Check Session State
```bash
# Is D-Bus session active?
echo $DBUS_SESSION_BUS_ADDRESS
dbus-launch --print-address  # If empty, D-Bus not running

# Is X11 session active?
echo $DISPLAY
ls -la /tmp/.X11-unix/

# Check if session services are registered
systemctl --user status

# Look for failures
systemctl --user --failed
```

### Step 5: Check Launcher Log
```bash
# Modern desktops may log launcher issues
journalctl -xe --user -n 50 | grep -i "nautilus\|launcher\|failed"

# Or check for .desktop file errors
/usr/libexec/gnome-control-center --version  # Direct check
```

---

## Recovery Solutions (in order of simplicity)

### Solution A: Fix Environment in Desktop File
Edit the .desktop file to include environment:

```bash
# Example: /home/user/.local/share/applications/nautilus.desktop
[Desktop Entry]
Name=Files
Exec=env DISPLAY=:0 nautilus %U
Terminal=false
Categories=System;FileManager;
```

### Solution B: Create Wrapper Script
Create a launcher wrapper that sets environment:

```bash
# File: ~/.local/bin/nautilus-wrapper
#!/bin/bash
export DISPLAY=${DISPLAY:-:0}
export XAUTHORITY=${XAUTHORITY:-$HOME/.Xauthority}
/usr/bin/nautilus "$@"
```

Then update .desktop file:
```
Exec=/home/user/.local/bin/nautilus-wrapper %U
```

### Solution C: Force D-Bus Session
```bash
# If DBUS_SESSION_BUS_ADDRESS is empty, manually set it
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
```

Add to `~/.profile` or `~/.bashrc` to make persistent.

### Solution D: Restart Desktop Session
```bash
# If launcher infrastructure is broken, restart the session
# On GNOME/Unity with X11:
systemctl --user restart gnome-session-manager.service

# Or simply log out and back in
```

### Solution E: Check systemd User Session
```bash
# User services may not have started properly
systemctl --user is-active dbus.service
systemctl --user is-active graphical-session.target

# If not active, enable and start
systemctl --user enable dbus.service
systemctl --user start graphical-session.target
```

---

## Decision Tree

```
CLI command works? → YES
   ↓
GUI icon fails? → YES
   ↓
Check $DISPLAY → Empty?
   ├─ YES: Solution A/B (set DISPLAY in launcher)
   └─ NO: Check $DBUS_SESSION_BUS_ADDRESS
      ├─ Empty: Solution C (set DBUS_SESSION_BUS_ADDRESS)
      └─ Set: Check systemctl --user --failed
         ├─ Services failed: Solution D (restart session)
         └─ All good: Check .desktop file permissions
            └─ Fix or recreate .desktop file
```

---

## Prevention

### For System Administrators
1. Ensure `graphical-session.target` is properly configured
2. Verify D-Bus user session auto-starts at login
3. Test icon launches after system restart (not just after login)

### For Users
1. Monitor `journalctl --user -f` while clicking launcher icons
2. Keep environment variables consistent across shell and session
3. After system changes, test icon launches, not just CLI

---

## Related Issues

- **Daemon persistence after restart** — gsd-* services failing breaks D-Bus
- **Display readiness** — DISPLAY not set causes "Cannot open display" errors
- **XAUTHORITY missing** — X11 auth failures for GUI apps
- **Stale gnome-shell grabs** — Keybindings fail post-sleep

---

## Implementation Notes

This protocol should be applied when:
1. User reports "app works in terminal, not from icon"
2. System shows inconsistent app launcher behavior
3. Desktop environment state is questionable
4. After system restart or session changes

**Success Criteria**: All tested applications launch correctly from GUI icons and function identically to CLI launches.

---

**Version**: 1.0
**Last Updated**: 2026-02-26
**Author**: AI Debugging Protocol
**Next Review**: After implementing daemon persistence fix
