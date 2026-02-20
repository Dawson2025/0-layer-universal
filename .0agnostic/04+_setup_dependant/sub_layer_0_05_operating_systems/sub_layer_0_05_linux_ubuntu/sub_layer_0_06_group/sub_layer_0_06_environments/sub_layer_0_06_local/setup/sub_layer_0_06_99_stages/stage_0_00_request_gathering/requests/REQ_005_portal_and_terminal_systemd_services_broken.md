# REQ_005: Portal and Terminal systemd Services Completely Broken

**Date Reported**: 2026-01-29
**Status**: Active - Systemic failure
**Severity**: Critical (blocks all GUI app launching)
**Related**: REQ_003, REQ_004, ISSUE_005

---

## Problem Summary

After reboot:
- ❌ Files app won't open
- ❌ Terminal app won't open
- ❌ LibreOffice won't open
- ✅ **Workaround**: Manually running `bash /home/dawson/.local/bin/fix-portal-services.sh` makes everything work

**Root Cause**: systemd service files can't properly initialize GTK portal and Terminal services due to DISPLAY/X11 environment issues.

---

## Detailed Findings

### Issue 1: GTK Portal Service Failure

**Error**: `xdg-desktop-portal-gtk` exits with status 1
```
Failed to create access proxy: Error calling StartServiceByName
for org.freedesktop.impl.portal.desktop.gtk: Process org.freedesktop.impl.portal.desktop.gtk
exited with status 1
```

**Root Cause**: GTK portal can't initialize because:
1. DISPLAY environment variable not accessible in systemd service context
2. Service tries to start before X11 is fully initialized
3. Even with `Environment="DISPLAY=:0"` in override.conf, the service receives empty DISPLAY

**Evidence**:
- Direct command execution works: `/usr/libexec/xdg-desktop-portal-gtk -v` runs fine
- Systemd service startup fails every time
- Manual wrapper script attempts also fail (CRLF line ending issues)

### Issue 2: Terminal Server Service Failure

**Error**: `gnome-terminal-server` exits with status 10
```
Failed to parse arguments: Cannot open display:
```

**Root Cause**: Terminal server can't open display because:
1. DISPLAY not set in systemd service environment
2. Service tries to start before X11/session is fully ready
3. D-Bus service file references `SystemdService=gnome-terminal-server.service` which fails

**Evidence**:
```
gnome-terminal-server[69302]: Failed to parse arguments: Cannot open display:
systemd[2809]: gnome-terminal-server.service: Main process exited, code=exited, status=10/n/a
```

### Root Cause Pattern

**Both failures stem from the same systemic issue:**
```
Systemd service start order:
  1. systemd user session initializes (graphical-session.target)
  2. Services start: xdg-desktop-portal, gnome-terminal-server, etc.
  3. X11/Wayland display is not fully initialized yet
  4. Services try to connect to DISPLAY=:0 but it's not ready
  5. Services crash
  6. Systemd gives up, marks services as failed
  7. User tries to open Files/Terminal → fails because services are "down"
  8. Manual fix script runs 5+ seconds later and fixes everything
```

---

## Why The Workaround Works

The fix script (`/home/dawson/.local/bin/fix-portal-services.sh`):
```bash
export DISPLAY=:0
export XAUTHORITY=/home/dawson/.Xauthority
sleep 3  # ← Crucial! Waits for X11 to fully initialize

# Kill stuck processes
pkill -9 xdg-desktop-portal

# Restart in correct environment
/usr/libexec/xdg-desktop-portal-gtk &
sleep 2
/usr/libexec/xdg-desktop-portal &
sleep 2
/usr/libexec/gnome-terminal-server &
```

When run manually: ✅ Works
When run via autostart (with 5s delay): ✅ Works
When run via new `portal-init.service` (Before=xdg-desktop-portal): ❌ Still too late

---

## What We Tried (And Why It Failed)

### Attempt 1: Autostart Script
- ❌ Failed: Autostart delay=5s is too late, portal crashes at +6s
- Status: Superseded by `portal-init.service`

### Attempt 2: Create `portal-init.service`
- ✅ Partial success: Service runs and executes fix script
- ❌ Still fails: GTK portal exits with status 1 even after fix script runs
- Problem: xdg-desktop-portal.service may still be racing against GTK backend startup

### Attempt 3: Wrapper Scripts for GTK Portal/Terminal
- ❌ Failed: Systemd wrapper execution issues
- Problem: Script invocation in ExecStart= doesn't work as expected
- Issue: CRLF line ending problems initially, then wrapper just doesn't execute

### Attempt 4: `Environment="DISPLAY=:0"` Override
- ❌ Doesn't work: DISPLAY still empty in service context
- Reason: Environment= is static, evaluated at service startup time when X11 not ready

---

## The Core Problem

**Systemd services cannot reliably connect to X11 display because:**

1. **Timing**: Services start before X11 is ready
2. **Environment**: `Environment="DISPLAY=:0"` doesn't guarantee the display is actually available
3. **D-Bus**: The D-Bus daemon needs proper DISPLAY too
4. **Chicken-and-egg**: Portal/Terminal needed to launch GUI apps, but they need GUI to initialize

This is a **known limitation of systemd user services and Xwayland/X11 integration**.

---

## Solutions (In Order of Feasibility)

### Solution 1: Delay Portal Services Until X11 Ready (BEST)
- Create a systemd target that waits for DISPLAY to be accessible
- Have portal/terminal services depend on this target
- More complex but correct solution

### Solution 2: Systemd Socket Activation
- Instead of starting services at boot, activate them on demand
- When Files/Terminal request the service, it starts with proper environment
- Would require reworking systemd service files

### Solution 3: Make Autostart More Reliable
- Increase autostart delay to 10+ seconds (not elegant)
- Run multiple retry loops
- Current approach in `portal-init.service`

### Solution 4: Move to User Services Target
- Instead of graphical-session, use graphical-session-pre
- Delay portal init until after graphical-session is fully loaded
- This is what `portal-init.service` attempts

### Solution 5: GNOME/Systemd Policy Change
- This is a systemic issue that affects many distros
- Would need GNOME upstream fix

---

## Current Status Summary

### What Works ✅
- **Files App (nautilus)**: Fully functional
  - Opens via GUI without issues
  - Can be closed and reopened without problems
  - Portal services auto-restart if they crash

### What Doesn't Work ❌
- **GNOME Terminal**: D-BUS service activation blocked
  - Terminal server process CAN start with proper environment
  - But cannot claim the `org.gnome.Terminal` D-BUS service name
  - Results in "Error calling StartServiceByName" when trying to open terminal via GUI

### Workaround (Temporary)
If terminal service dies, restart it manually:
```bash
pkill -9 gnome-terminal-server
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/gnome-terminal-server &
```

### Original Fix Script (Still Works)
```bash
bash /home/dawson/.local/bin/fix-portal-services.sh
```
This kills all portal processes and restarts them with proper timing/environment. Used as last resort when services are in bad state.

---

## Next Steps / Future Investigation

### Files App: DONE ✅
The Files app issue is fully resolved. Portal services work correctly.

### Terminal: Requires Different Approach
The Terminal D-BUS service activation issue is a fundamental incompatibility between:
- D-BUS service activation mechanism (expects systemd to manage service lifecycle)
- systemd `Type=dbus` strict initialization protocol
- Environment variable propagation in systemd services

**Possible Future Solutions**:

1. **Option A: Use Alternative Terminal**
   - Install xfce4-terminal: `sudo apt install xfce4-terminal`
   - This doesn't depend on the problematic D-BUS service activation
   - Would completely bypass the systemd/D-BUS issue

2. **Option B: Patch D-BUS Service File**
   - Remove `SystemdService=` line from `/usr/share/dbus-1/services/org.gnome.Terminal.service`
   - Replace with direct `Exec=` invocation with full environment
   - Risk: May break when gnome-terminal is updated

3. **Option C: Investigate gnome-terminal-server Source**
   - Understand why it can't claim D-BUS name when environment is set externally
   - May involve gnome-shell or session-related initialization
   - Would require deeper C-level debugging

4. **Option D: Use Socket Activation**
   - Implement D-BUS socket activation instead of service activation
   - More complex but bypasses the systemd/D-BUS incompatibility
   - Would require creating custom `.socket` units

---

## Solution 1 Implementation (PARTIAL SUCCESS)

### Approach: Display-Ready Target + Environment Wrappers

Created a systemd service-based solution that waits for X11 to be accessible and properly sets environment variables before starting portal/terminal services:

**Created Files**:
- `~/.config/systemd/user/display-ready.service` - Waits for X11 readiness ✅
- `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf` - Uses display-ready dependency + Restart=on-failure
- `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf` - Uses environment wrapper + Restart=on-failure
- `~/.config/systemd/user/xdg-desktop-portal-gtk.service.d/override.conf` - Uses display-ready dependency
- `~/.local/bin/gnome-terminal-server-env.sh` - Wrapper sets DISPLAY + DBUS_SESSION_BUS_ADDRESS
- `~/.local/bin/xdg-desktop-portal-gtk-env.sh` - Wrapper sets DISPLAY + DBUS_SESSION_BUS_ADDRESS
- `~/.local/bin/start-gnome-terminal-server.sh` - Alternative wrapper script
- `~/.config/autostart/gnome-terminal-server-startup.desktop` - Autostart desktop entry

**Status**: PARTIAL SUCCESS
- ✅ display-ready.service works (correctly detects X11 readiness)
- ✅ Files app (nautilus) opens and works via GUI
- ✅ Files app can be closed and reopened without issues
- ✅ Portal services have Restart=on-failure configured
- ⚠️ GNOME Terminal server process can be started with proper environment
- ❌ D-BUS service name 'org.gnome.Terminal' cannot be claimed/registered
- ❌ gnome-terminal command fails: "Error calling StartServiceByName for org.gnome.Terminal: Process org.gnome.Terminal exited with status 10"

**What Works**: Files app fully functional with proper restart behavior

**What Doesn't Work**: GNOME Terminal D-BUS service activation

### The Terminal Issue

Even though gnome-terminal-server process CAN run with proper environment (DISPLAY=:0, XAUTHORITY, DBUS_SESSION_BUS_ADDRESS set), it fails to register the `org.gnome.Terminal` D-BUS service name. This prevents the `gnome-terminal` command from working via D-BUS activation.

**Attempts Made**:
1. Setting `Environment=` variables in systemd override - Process exits with "Cannot open display"
2. Using wrapper scripts with explicit `export` - Process runs but D-BUS registration fails
3. Using `/usr/bin/env` to pass environment - Process runs but D-BUS still fails
4. Using `bash -c` with inline exports - Process runs but D-BUS still fails
5. Creating autostart desktop entry - Process runs but D-BUS still fails
6. Running gnome-terminal-server directly - Process runs but D-BUS still fails
7. Changing `Type=dbus` to `Type=simple` with `Restart=on-failure` - No improvement

**Root Cause**: The D-BUS service file at `/usr/share/dbus-1/services/org.gnome.Terminal.service` references `SystemdService=gnome-terminal-server.service`, which means D-BUS expects systemd to manage the lifecycle. However, the service initialization protocol between systemd (Type=dbus) and D-BUS service activation is not compatible with our environment-setting approach. The gnome-terminal-server process cannot claim the service name during its startup handshake with D-BUS.

## Investigation Checklist

### Completed
- [x] Identified GTK portal crashes at service startup
- [x] Identified Terminal server crashes at service startup
- [x] Found that manual scripts work fine
- [x] Confirmed DISPLAY environment issue
- [x] Attempted systemd wrapper solutions (initially unsuccessful)
- [x] Implemented display-ready.service solution
- [x] Added DBUS_SESSION_BUS_ADDRESS to environment
- [x] Verified Files app works via GUI
- [x] Verified Files app reopens after closing (persistent)
- [x] Added Restart=on-failure to auto-recovery
- [x] Created multiple wrapper/startup scripts
- [x] Tested 7+ different approaches to fix Terminal D-BUS activation

### Blocked / Open
- [ ] GNOME Terminal D-BUS service registration (stuck on D-BUS activation protocol)
- [ ] Terminal server cannot claim org.gnome.Terminal service name
- [ ] Root cause appears to be systemd/D-BUS compatibility issue

### Status
- **Files App**: ✅ RESOLVED (fully functional)
- **Portal Services**: ✅ RESOLVED (working with auto-restart)
- **Terminal**: ❌ UNRESOLVED (requires different approach - see Next Steps)
- [x] Confirmed `portal-init.service` partial fix
- [ ] Try socket activation approach
- [ ] Try custom systemd target approach
- [ ] Test with Wayland instead of X11
- [ ] Check GNOME upstream for related issues

---

## Files Related to This Issue

| File | Purpose | Status |
|------|---------|--------|
| `~/.local/bin/fix-portal-services.sh` | Manual fix script | Working ✓ |
| `~/.config/autostart/fix-portal-services.desktop` | Autostart attempt | Too late ✗ |
| `~/.config/systemd/user/portal-init.service` | Systemd service attempt | Partial ✗ |
| `~/.config/systemd/user/xdg-desktop-portal*.service.d/override.conf` | Portal overrides | Ineffective ✗ |
| `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf` | Terminal overrides | Ineffective ✗ |
