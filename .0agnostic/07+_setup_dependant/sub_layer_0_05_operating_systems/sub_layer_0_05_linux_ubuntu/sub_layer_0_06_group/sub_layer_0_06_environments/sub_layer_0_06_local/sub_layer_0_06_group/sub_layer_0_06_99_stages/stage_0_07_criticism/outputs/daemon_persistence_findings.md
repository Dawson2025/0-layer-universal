# Daemon Persistence After Restart — Investigation Findings

**Date**: 2026-02-26
**Issue**: After full computer restart, GNOME Settings Daemons (gsd-media-keys, gsd-power) fail to start, causing brightness/volume keys and custom keybindings (Control-Alt-S) to stop working.

---

## Problem Statement

After power-off/power-on restart:
1. User logs in successfully
2. Desktop appears, but keybindings don't respond
3. Brightness/volume keys don't work
4. Control-Alt-S (speak-selection) doesn't work
5. System status shows `degraded` with multiple failed services
6. Need to manually restart daemons or re-login to fix

---

## Root Cause Analysis

### Current Implementation (Existing)

**Systemd-based keepalive approach**:
- `gsd-keepalive.timer` — triggers every 60 seconds after 30-second initial delay
- `gsd-keepalive.service` — attempts to manually restart dead daemons
- Problem: Services fail with `Cannot open display:` even when display IS ready

### Why Manual Restart Fails

The GNOME SettingsDaemon services are marked as **"static"** units:

```bash
$ systemctl --user list-unit-files | grep SettingsDaemon.MediaKeys
org.gnome.SettingsDaemon.MediaKeys.service    static    -
```

This means:
1. They are **managed by gnome-session**, not systemd directly
2. They expect to run **within the gnome-session context**
3. Manual `/usr/libexec/gsd-media-keys` invocations from systemd services fail because:
   - Missing D-Bus context
   - Missing session manager registration
   - Missing proper environment setup that only gnome-session provides

### Service Startup Flow (Current Broken State)

```
System Boot
  ↓
Systemd user session starts
  ↓
graphical-session.target reached
  ↓
gnome-session-binary starts (manages gsd-* daemons)
  ↓
gsd-* services attempt to start BUT display not ready yet
  ↓
Services fail: "Cannot open display:"
  ↓
Systemd gives up after 5 retries: "Start request repeated too quickly"
  ↓
User logs in to see broken keybindings
```

---

## What We've Built (Phase 1)

### 1. Display Readiness Detection ✓

**File**: `/home/dawson/.local/bin/wait-for-display.sh`
**Status**: Working

Checks for actual display readiness:
- DISPLAY variable set
- X11 socket exists (`/tmp/.X11-unix/X0`)
- XAUTHORITY file accessible
- gnome-shell process running

**Result**: Successfully detects when display is ready (waited 0s = already available)

### 2. Graphical Session Ready Target ✓

**Files**:
- `/home/dawson/.config/systemd/user/graphical-session-ready.target`
- `/home/dawson/.config/systemd/user/graphical-session-readiness.service`

**Status**: Working infrastructure

- `graphical-session-readiness.service` runs `wait-for-display.sh` on startup
- When it succeeds, `graphical-session-ready.target` becomes available
- Other services can now depend on this target for proper ordering

**Result**: Clean systemd-native approach to signal display readiness

### 3. Enhanced Keepalive Timers ✓

**Files**:
- Updated `gsd-keepalive.timer` — increased OnBootSec from 30s to 60s
- Updated `gsd-keepalive.service` — calls wait-for-display.sh first
- Created `gsd-keepalive-v2.service` — alternative using graphical-session-ready.target

**Status**: Functional but unable to fix the core problem (manual daemon restart doesn't work)

---

## The Core Problem: Manual Daemon Restart ✗

When we try to restart daemons from a systemd service:

```bash
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/gsd-media-keys &
```

**Result**: `Cannot open display:`

**Why**: Even though the display exists and is accessible from the user's shell, it's NOT accessible from systemd service context because:
1. Systemd services don't inherit the full D-Bus session context
2. gsd-* daemons need `org.gnome.SessionManager` to register themselves
3. They expect to be started and monitored by gnome-session, not independently

**Evidence from logs**:
```
wait-for-display.sh[3183040]: Display is ready! (waited 0s)
bash[3183046]: Cannot open display:
```

Display detection works, but daemon start still fails.

---

## Next Phase: Three Parallel Solutions

To fix daemon persistence after restart, we need to work **with gnome-session**, not around it.

### Solution 1: Fix gnome-session Service Startup Order
Delay gnome-session's daemon startup until display is confirmed ready.

**Approach**:
- Create systemd service override for gnome-session
- Make it depend on `graphical-session-ready.target`
- gnome-session won't start daemons until display is actually available

**Pros**: Fixes root cause, clean systemd ordering
**Cons**: Requires system service modifications

### Solution 2: Post-Login Hook
Create a script that runs immediately after login and checks daemon status.

**Approach**:
- Create GNOME autostart desktop file: `~/.config/autostart/daemon-health-check.desktop`
- Runs after gnome-session is fully loaded
- Checks if daemons are running, restarts them if needed

**Pros**: Works within existing gnome-session framework
**Cons**: Small delay before daemon restart on login

### Solution 3: Re-Login Trigger
Detect broken keybindings on startup and guide user to re-login.

**Approach**:
- Create systemd service that runs after graphical-session-ready.target
- Tests if keybindings work (try to execute Control-Alt-S action)
- If broken, display notification: "Desktop needs restart. Please log out and back in."

**Pros**: Simple, leverages gnome-session's own recovery mechanism
**Cons**: Requires user action

---

## Testing Plan

See: `stage_0_06_testing/design/daemon_persistence_test_suite.md`

Each solution will be tested:
1. In a controlled environment (not affecting production immediately)
2. After a simulated/actual restart
3. For daemon status, keybinding responsiveness, and side effects

---

## Files Created

**Phase 1 (Detection)**:
- `.local/bin/wait-for-display.sh` — display readiness script
- `.config/systemd/user/graphical-session-ready.target` — readiness target
- `.config/systemd/user/graphical-session-readiness.service` — brings up target
- `.config/systemd/user/gsd-keepalive.service` — updated with display wait
- `.config/systemd/user/gsd-keepalive-v2.service` — target-based variant

---

## Next Steps

1. Design test suite for three solutions
2. Create test procedures for each approach
3. Execute tests after restart
4. Document results: what works, what doesn't, why
5. Implement winning solution(s)

