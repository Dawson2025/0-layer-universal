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

## Current Workaround Status

**Manual Fix**: ✅ Works 100%
```bash
bash /home/dawson/.local/bin/fix-portal-services.sh
```
After running this, Files, Terminal, and LibreOffice all open successfully.

**Automated At Login**: ⚠️ Partially works
- `fix-portal-services.desktop` (autostart) - doesn't run early enough
- `portal-init.service` (new systemd service) - runs but GTK portal still has issues

---

## Recommendations

### Immediate (For Current Session)
Until we find a permanent fix, run this at login:
```bash
bash /home/dawson/.local/bin/fix-portal-services.sh
```

### Long-Term (Permanent Fix)
Need to implement **Solution 1** or **Solution 2** above.

The issue is deep enough that we likely need to:
1. Create a custom target that checks X11 readiness
2. Make portal/terminal services depend on that target
3. Or rewrite with socket activation

---

## Investigation Checklist

- [x] Identified GTK portal crashes at service startup
- [x] Identified Terminal server crashes at service startup
- [x] Found that manual scripts work fine
- [x] Confirmed DISPLAY environment issue
- [x] Attempted systemd wrapper solutions (failed)
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
