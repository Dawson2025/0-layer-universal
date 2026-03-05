---
resource_id: "62e546ef-0a08-45ee-ae1a-f7231f22e533"
resource_type: "document"
resource_name: "REQ_005_portal_and_terminal_systemd_services_broken"
---
# REQ_005: Portal and Terminal systemd Services Completely Broken

**Date Reported**: 2026-01-29
**Status**: Active - Systemic failure
**Severity**: Critical (blocks all GUI app launching)
**Related**: REQ_003, REQ_004, ISSUE_005

---

<!-- section_id: "7331298f-bd53-48ee-b5b1-d60fd9284da8" -->
## Problem Summary

After reboot:
- ❌ Files app won't open
- ❌ Terminal app won't open
- ❌ LibreOffice won't open
- ✅ **Workaround**: Manually running `bash /home/dawson/.local/bin/fix-portal-services.sh` makes everything work

**Root Cause**: systemd service files can't properly initialize GTK portal and Terminal services due to DISPLAY/X11 environment issues.

---

<!-- section_id: "3840d391-baf0-4182-8210-c29fc8c7fe74" -->
## Detailed Findings

<!-- section_id: "ad7b2bab-5670-420e-8f49-3c8269e21e77" -->
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

<!-- section_id: "09ea4ac2-3c21-4edb-a5eb-55de4fe14f12" -->
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

<!-- section_id: "f9e07dcf-bac1-458c-8136-8771c5825abe" -->
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

<!-- section_id: "50dd12cd-35d3-4505-bfbb-85572ac32d4a" -->
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

<!-- section_id: "d6ab5ddf-cf8f-4a62-be84-52fdff998f67" -->
## What We Tried (And Why It Failed)

<!-- section_id: "ac17116a-09c9-475e-9be2-fcd0dc1a0c27" -->
### Attempt 1: Autostart Script
- ❌ Failed: Autostart delay=5s is too late, portal crashes at +6s
- Status: Superseded by `portal-init.service`

<!-- section_id: "e3d695bb-5ae7-4b36-8a31-ba8ff8a47eec" -->
### Attempt 2: Create `portal-init.service`
- ✅ Partial success: Service runs and executes fix script
- ❌ Still fails: GTK portal exits with status 1 even after fix script runs
- Problem: xdg-desktop-portal.service may still be racing against GTK backend startup

<!-- section_id: "5c9ca5fd-0cc4-4688-999c-18fb86f3954e" -->
### Attempt 3: Wrapper Scripts for GTK Portal/Terminal
- ❌ Failed: Systemd wrapper execution issues
- Problem: Script invocation in ExecStart= doesn't work as expected
- Issue: CRLF line ending problems initially, then wrapper just doesn't execute

<!-- section_id: "51b023f2-4ac1-428d-86e1-35b4882007c4" -->
### Attempt 4: `Environment="DISPLAY=:0"` Override
- ❌ Doesn't work: DISPLAY still empty in service context
- Reason: Environment= is static, evaluated at service startup time when X11 not ready

---

<!-- section_id: "cc0db6f0-1968-4084-9607-1cef1052a502" -->
## The Core Problem

**Systemd services cannot reliably connect to X11 display because:**

1. **Timing**: Services start before X11 is ready
2. **Environment**: `Environment="DISPLAY=:0"` doesn't guarantee the display is actually available
3. **D-Bus**: The D-Bus daemon needs proper DISPLAY too
4. **Chicken-and-egg**: Portal/Terminal needed to launch GUI apps, but they need GUI to initialize

This is a **known limitation of systemd user services and Xwayland/X11 integration**.

---

<!-- section_id: "da35ff4b-20e0-4e21-a585-5b6439acb72d" -->
## Solutions (In Order of Feasibility)

<!-- section_id: "b69d3e1d-2bc7-4015-b90d-613239cac66f" -->
### Solution 1: Delay Portal Services Until X11 Ready (BEST)
- Create a systemd target that waits for DISPLAY to be accessible
- Have portal/terminal services depend on this target
- More complex but correct solution

<!-- section_id: "2a98801e-c4f4-455d-96a0-675b33c10c53" -->
### Solution 2: Systemd Socket Activation
- Instead of starting services at boot, activate them on demand
- When Files/Terminal request the service, it starts with proper environment
- Would require reworking systemd service files

<!-- section_id: "3a49b67e-16e8-409c-b4dc-f8727479e2ba" -->
### Solution 3: Make Autostart More Reliable
- Increase autostart delay to 10+ seconds (not elegant)
- Run multiple retry loops
- Current approach in `portal-init.service`

<!-- section_id: "d8cb5e55-b472-49ec-968b-84cb3795c731" -->
### Solution 4: Move to User Services Target
- Instead of graphical-session, use graphical-session-pre
- Delay portal init until after graphical-session is fully loaded
- This is what `portal-init.service` attempts

<!-- section_id: "7e75d5c4-9c6e-4b37-9669-51b241290094" -->
### Solution 5: GNOME/Systemd Policy Change
- This is a systemic issue that affects many distros
- Would need GNOME upstream fix

---

<!-- section_id: "8c333ff5-6090-4621-90f3-f7c16d44d0e3" -->
## Current Status Summary

<!-- section_id: "d8e3f672-417f-46be-839c-344e90e2156d" -->
### What Works ✅
- **Files App (nautilus)**: Fully functional
  - Opens via GUI without issues
  - Can be closed and reopened without problems
  - Portal services auto-restart if they crash

<!-- section_id: "740519ba-5b77-4fab-b189-68d1b04ecd7a" -->
### What Doesn't Work ❌
- **GNOME Terminal**: D-BUS service activation blocked
  - Terminal server process CAN start with proper environment
  - But cannot claim the `org.gnome.Terminal` D-BUS service name
  - Results in "Error calling StartServiceByName" when trying to open terminal via GUI

<!-- section_id: "c07bc4fc-b5fe-45c9-b137-a4210d7bb812" -->
### Workaround (Temporary)
If terminal service dies, restart it manually:
```bash
pkill -9 gnome-terminal-server
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/gnome-terminal-server &
```

<!-- section_id: "4b31548e-7ec6-4678-881a-b2d96be411d4" -->
### Original Fix Script (Still Works)
```bash
bash /home/dawson/.local/bin/fix-portal-services.sh
```
This kills all portal processes and restarts them with proper timing/environment. Used as last resort when services are in bad state.

---

<!-- section_id: "67841a59-7e58-4228-b429-5d098470bf6c" -->
## Next Steps / Future Investigation

<!-- section_id: "11206662-dd28-4541-b3e2-e8e69fba9c71" -->
### Files App: DONE ✅
The Files app issue is fully resolved. Portal services work correctly.

<!-- section_id: "738d1a50-abfc-4066-9fe3-49287ab01c46" -->
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

<!-- section_id: "b69c597d-5df5-4384-b0eb-a5c87003e993" -->
## Solution 1 Implementation (PARTIAL SUCCESS)

<!-- section_id: "1eb20f89-b92b-4b57-b1e7-851350bb206f" -->
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

<!-- section_id: "f60ca6d9-c8df-45dc-89bd-176ea26ab6c6" -->
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

<!-- section_id: "4411200d-9f27-47b6-b3f0-d50c4114fc78" -->
## Investigation Checklist

<!-- section_id: "1ae01bb5-2997-401f-b117-51d70aa6396e" -->
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

<!-- section_id: "968bddc3-f94a-41fa-aa94-b5ce4eba1ce6" -->
### Blocked / Open
- [ ] GNOME Terminal D-BUS service registration (stuck on D-BUS activation protocol)
- [ ] Terminal server cannot claim org.gnome.Terminal service name
- [ ] Root cause appears to be systemd/D-BUS compatibility issue

<!-- section_id: "e9900d82-efa1-4d79-bbeb-d04bdf537baa" -->
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

<!-- section_id: "3fcb87fe-e449-49d5-9768-7ccc0c4d10f7" -->
## Files Related to This Issue

| File | Purpose | Status |
|------|---------|--------|
| `~/.local/bin/fix-portal-services.sh` | Manual fix script | Working ✓ |
| `~/.config/autostart/fix-portal-services.desktop` | Autostart attempt | Too late ✗ |
| `~/.config/systemd/user/portal-init.service` | Systemd service attempt | Partial ✗ |
| `~/.config/systemd/user/xdg-desktop-portal*.service.d/override.conf` | Portal overrides | Ineffective ✗ |
| `~/.config/systemd/user/gnome-terminal-server.service.d/override.conf` | Terminal overrides | Ineffective ✗ |
