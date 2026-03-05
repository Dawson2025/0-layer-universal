---
resource_id: "8014497d-3bfd-4abb-a8ca-8d41bc8b3938"
resource_type: "output"
resource_name: "STAGE_REPORT_CLI_GUI_LAUNCHER_INVESTIGATION"
---
# Stage Report: CLI vs GUI Launcher Failure Investigation

**Date**: 2026-02-26 17:00+ MST
**Stage**: stage_0_06_testing (Testing)
**Investigation Focus**: Desktop Environment Launcher Infrastructure
**Status**: Findings Documented, Solutions Identified

---

<!-- section_id: "e3f4892c-3efd-42b8-89af-c3b68a5da619" -->
## Executive Summary

Discovered a critical pattern: **applications launch successfully via CLI but fail when clicked from GUI icons**. This is a session-level issue, not a daemon issue, though it's caused by the same root cause (failed gsd-* daemons breaking D-Bus).

**Key Finding**: The problem is not that daemons can't start — they can be restarted manually. The problem is that they fail during system boot before D-Bus is properly initialized, which cascades to break all GUI app launchers.

---

<!-- section_id: "024a3c65-33cf-45c9-b2bf-ae1ae7bfd76d" -->
## Findings

<!-- section_id: "858f6620-ec13-4ebd-87a1-3b9ad1a6d93c" -->
### What Works
- ✓ Terminal commands: `nautilus`, `gnome-control-center`, `gedit` all open
- ✓ Some GUI icons work: Chrome, Firefox, Cursor
- ✓ Settings opened after running diagnostic commands (D-Bus activated)
- ✓ Bluetooth pairing works via Settings
- ✓ GNOME Terminal opens from command line

<!-- section_id: "3bcda620-b06a-4422-b67c-1218b1fd219b" -->
### What Doesn't Work
- ✗ Nautilus icon (Files) doesn't open
- ✗ Settings icon doesn't open (but CLI `gnome-control-center` works)
- ✗ GNOME Terminal icon doesn't open (but CLI `gnome-terminal` works)
- ✗ Volume keys don't work (gsd-media-keys failed)
- ✗ Brightness keys don't work (gsd-power failed)
- ✗ Brightness slider missing from Settings

<!-- section_id: "d8a6193f-9cd4-40bd-b179-aed7acd158df" -->
### The Pattern

**Terminal Environment vs Desktop Session Environment**:
- Terminal inherits full environment: DISPLAY, XAUTHORITY, DBUS_SESSION_BUS_ADDRESS, PATH
- GUI icon launcher depends on systemd --user services and D-Bus
- When D-Bus fails (due to gsd-* failures), icon launchers fail
- But CLI still works because it doesn't depend on D-Bus

---

<!-- section_id: "bd102433-cb5b-4d62-8718-d515b60fcc4b" -->
## Root Cause Analysis

<!-- section_id: "92228905-ae78-4c99-9de7-432f05f09179" -->
### Primary Cause: Failed gsd-* Services Block D-Bus
```
System boots
  ↓
systemd --user session starts
  ↓
gsd-media-keys, gsd-power attempt to start (but fail: DISPLAY not ready, etc.)
  ↓
Systemd gives up after 5 retries ("Start request repeated too quickly")
  ↓
D-Bus session services don't fully initialize
  ↓
GUI app launchers fail (they depend on D-Bus)
  ↓
CLI still works (doesn't depend on D-Bus)
```

<!-- section_id: "1149abaf-a17f-4877-a94f-427d905012fc" -->
### Secondary Issue: DISPLAY Readiness Race
- gsd-* services start before X11 display is ready
- Daemon failure triggers keep-alive timer (60s delay)
- By then, D-Bus has already failed
- Manual restart of daemons works (display is ready by then)
- But launcher infrastructure remains broken until session restart

---

<!-- section_id: "9c5c39df-3165-4f44-b8d4-4d7a706b7c1c" -->
## What Was Tested

<!-- section_id: "ed5cd0e3-9d94-4a1a-8b78-c787e4679b30" -->
### Test 1: Manual Daemon Restart
**Command**: `systemctl --user restart org.gnome.SettingsDaemon.MediaKeys.service`
**Result**: ✓ Daemon starts, but fails to grab accelerators (gnome-shell has them)
**Finding**: Daemon CAN be manually restarted; it's the initial boot startup that fails

<!-- section_id: "b811d1ec-c301-4965-a4d4-48169dc1633b" -->
### Test 2: CLI App Launch
**Command**: `gnome-control-center`, `nautilus`, `gedit` in terminal
**Result**: ✓ All work perfectly
**Finding**: Apps are not broken; launcher infrastructure is

<!-- section_id: "0396282a-9665-4952-8e15-8130d7bc7514" -->
### Test 3: GUI Icon Launch
**Action**: Click Nautilus, Settings, Terminal icons
**Result**: ✗ Silent failure or no response
**Finding**: Desktop launcher is broken due to D-Bus failure

<!-- section_id: "505a8226-b926-4cdd-8707-994de912b749" -->
### Test 4: D-Bus Status Check
**Command**: `dbus-send --print-reply --dest=org.gnome.ControlCenter ...`
**Result**: ✗ Service not registered
**Finding**: D-Bus didn't activate the service (infrastructure broken)

<!-- section_id: "52745f68-7832-4867-917f-453c73f12378" -->
### Test 5: Environment Variables
**Current State**:
- DISPLAY=:0 ✓
- XDG_CURRENT_DESKTOP=Unity ✓
- DBUS_SESSION_BUS_ADDRESS set ✓
- gnome-shell running ✓
**Finding**: Environment looks healthy, but launcher still fails

<!-- section_id: "71cafdc8-023b-4be0-8afd-f79b913c037d" -->
### Test 6: Recovery via Diagnostic Commands
**What Happened**: Running several commands in sequence (`dbus-send`, `gnome-control-center` with GNOME desktop env, then power panel) somehow triggered D-Bus to initialize and Settings opened.
**Finding**: D-Bus can be manually activated, recovery is possible

---

<!-- section_id: "2570fb1c-7d71-4239-9f57-c064ddec7697" -->
## Why The Three Daemon Solutions Are Relevant

The daemon persistence solutions (Solution 1/2/3) address exactly this:

1. **Solution 1** (systemd startup order): Delays daemon startup until display is ready
   - Impact on CLI/GUI: Should fix the boot-time race condition

2. **Solution 2** (GNOME autostart hook): Restarts daemons post-login
   - Impact on CLI/GUI: Ensures daemons work when user is at desktop

3. **Solution 3** (Re-login trigger): Detects broken state and prompts re-login
   - Impact on CLI/GUI: Forces full session reinit which restores D-Bus

---

<!-- section_id: "d732aaf4-030b-4379-8739-d1920402b80a" -->
## New Artifacts Created

<!-- section_id: "c3880cbb-d966-4754-a6f9-60ddc7881dc5" -->
### Protocols
- `.0agnostic/03_protocols/cli_vs_gui_launcher_diagnosis_protocol.md`
  - Step-by-step diagnosis and recovery procedures
  - Decision tree for identifying root cause
  - Five solution approaches (A-E)

<!-- section_id: "65a1dbdd-0620-4c23-a56d-9a794f157f2d" -->
### Knowledge Base
- `.0agnostic/01_knowledge/desktop_environment_health/cli_vs_gui_launcher_issue.md`
  - Comprehensive explanation of the problem
  - Why CLI works but GUI doesn't
  - Connection to daemon persistence issue
  - Diagnostic commands and examples

<!-- section_id: "9e57408b-1529-48d3-a44c-29119c1fb2fb" -->
### Rules
- `.0agnostic/02_rules/dynamic/cli_gui_launcher_mismatch_rule/cli_gui_launcher_mismatch_rule.md`
  - Automatic detection rule
  - Immediate action steps (15 min diagnostic)
  - Three levels of permanent solutions
  - Escalation path if issue persists
  - Stage documentation requirements

---

<!-- section_id: "57cbab9b-3738-47f0-bc26-9225beafe3df" -->
## Critical Insights

<!-- section_id: "9d2628ca-8361-4952-b1ec-0e7792954bf5" -->
### 1. This Is A Symptom, Not The Root Cause
- CLI/GUI mismatch is a SYMPTOM of D-Bus failure
- Root cause is gsd-* daemons failing at boot
- Fixing daemon startup fixes the GUI launcher problem

<!-- section_id: "bf7393ef-a279-4da3-be73-2f5686df048e" -->
### 2. The Keepalive Timer Isn't Enough
- Currently deployed `gsd-keepalive.timer` runs every 60s
- But system boot happens faster; D-Bus fails before timer kicks in
- Solutions 1/2/3 address this by fixing startup timing

<!-- section_id: "ffdbbd1a-f1c5-4a38-8b82-314218e8e48e" -->
### 3. Environment Variables Are Not The Issue
- DISPLAY, XAUTHORITY, DBUS_SESSION_BUS_ADDRESS are all set correctly
- The issue is D-Bus SERVICE not responding, not environment variables

<!-- section_id: "79b8fa49-c958-492d-ba57-63a5de5e59b9" -->
### 4. Manual Operations Work, Automated Ones Don't
- User can run `gnome-control-center` and it works
- System can run it via .desktop file launcher and it fails
- This is because manual invocation bypasses D-Bus activation
- Automated launchers REQUIRE D-Bus to work

---

<!-- section_id: "3d5a2884-f3d7-422e-bcca-8f6074c006df" -->
## Next Steps

<!-- section_id: "a80ef526-987f-48f5-acc4-51bb5e19798f" -->
### Immediate (Before Restart Testing)
- [ ] Document these findings in stages
- [ ] Create trajectory stores (done ✓)
- [ ] Update knowledge base (done ✓)
- [ ] Add rules to system (done ✓)

<!-- section_id: "74bc4fde-5d6a-49d4-be30-ca95b493c421" -->
### Before System Restart
- [ ] Review all three daemon persistence solutions
- [ ] Choose which solution to test first (recommend Solution 1)
- [ ] Prepare restart test procedure

<!-- section_id: "d3878cbe-3d5c-4a4b-9b13-a1d29241fdbb" -->
### During Restart Testing
- [ ] Test that GUI icons work post-boot (not just CLI)
- [ ] Verify Settings opens from icon (not just terminal)
- [ ] Confirm volume AND brightness keys work
- [ ] Document results in stage reports

<!-- section_id: "9390c9ca-ab71-4514-a45e-5a0c00f51211" -->
### Success Criteria
- ✓ All GUI icons launch from desktop
- ✓ Settings displays correctly with brightness slider
- ✓ Volume keys work
- ✓ Brightness keys work
- ✓ Custom keybinding (Ctrl+Alt+S) works
- ✓ All functionality persists across system restart

---

<!-- section_id: "03418b96-a337-4e73-9c97-7325bc83c54f" -->
## Files Updated/Created

**Protocols**:
- `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/03_protocols/cli_vs_gui_launcher_diagnosis_protocol.md`

**Knowledge**:
- `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/01_knowledge/desktop_environment_health/cli_vs_gui_launcher_issue.md`

**Rules**:
- `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/02_rules/dynamic/cli_gui_launcher_mismatch_rule/cli_gui_launcher_mismatch_rule.md`

**Stage Reports**:
- This file (stage_0_06_testing stage report)

---

<!-- section_id: "3944bfa8-5437-449b-afd1-a00e4ec7cc84" -->
## Handoff to Next Stage

**To Stage 0_07_Criticism**: Review whether the CLI/GUI mismatch is indeed a symptom of daemon persistence, or if it indicates a separate session initialization issue.

**To Stage 0_08_Fixing**: Proceed with daemon persistence solutions (1/2/3) testing, which should resolve both the daemon failures AND the GUI launcher issues.

**To Stage 0_09_Current_Product**: After solutions are validated, update gsd-keepalive.timer and daemon startup procedures to ensure proper boot-time initialization.

---

<!-- section_id: "75a12d0d-b5a5-45f8-b710-2c7b20b142d0" -->
## Appendix: Diagnostic Commands Reference

```bash
# Check what's running
ps aux | grep -E "gsd-|gnome-shell|mutter"
pgrep -a gsd-media-keys
pgrep -a gsd-power

# Check service status
systemctl --user status org.gnome.SettingsDaemon.MediaKeys.service
systemctl --user status org.gnome.SettingsDaemon.Power.service
systemctl --user --failed

# Check environment
echo $DISPLAY
echo $XAUTHORITY
echo $DBUS_SESSION_BUS_ADDRESS

# Check if services are registered in D-Bus
dbus-send --print-reply --dest=org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus.ListNames

# Test CLI vs GUI
nautilus &           # Works
# Then click Files icon  # Fails
```

---

**Stage**: Testing (stage_0_06_testing)
**Status**: Investigation Complete, Solutions Identified
**Date**: 2026-02-26
**Next Milestone**: System restart testing of daemon persistence solutions
