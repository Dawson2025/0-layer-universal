---
resource_id: "9d301778-0e0e-4206-a381-e2fc9f5a2d26"
resource_type: "output"
resource_name: "01_comprehensive_test_design"
---
# Daemon Persistence After Restart — Test Suite Design

**Date**: 2026-02-26
**Objective**: Validate three solution approaches to daemon persistence

---

## Test Scenarios

All tests executed after a **full system restart** (power-off/on).

### Pre-Test State
- System powered off
- User logs back in
- GNOME session starts (daemons expected to fail initially)
- Tests execute

### Success Criteria (All Solutions)
- ✓ `pgrep -a gsd-media-keys` returns process
- ✓ `pgrep -a gsd-power` returns process
- ✓ Volume key press changes volume (`pactl get-sink-volume @DEFAULT_SINK@`)
- ✓ Brightness key press changes brightness
- ✓ Control-Alt-S hotkey responds (triggers speak-selection)
- ✓ `systemctl --user --failed` shows 0 failed services (or excludes gsd-*)

---

## Solution 1: Fix gnome-session Service Startup Order

### Design
```
graphical-session.target (existing)
  ↓
graphical-session-ready.target (our new target)
  ↓ (depends on)
graphical-session-readiness.service (wait-for-display.sh)
  ↓ (waits until display ready, THEN succeeds)
gnome-session daemons can now start reliably
```

### Implementation Steps

**Step 1a**: Create systemd override for gnome-session

File: `~/.config/systemd/user/gnome-session-binary.service.d/override.conf`

```ini
[Unit]
Wants=graphical-session-ready.target
After=graphical-session-ready.target
```

**Step 1b**: Update graphical-session.target to require readiness

File: `~/.config/systemd/user/graphical-session.target.d/override.conf`

```ini
[Unit]
Requires=graphical-session-readiness.service
After=graphical-session-readiness.service
```

### Test Procedure

1. Reload systemd: `systemctl --user daemon-reload`
2. **Restart system**: `sudo systemctl reboot`
3. After login, wait 10 seconds
4. Check daemons: `pgrep -a gsd-media-keys && pgrep -a gsd-power`
5. Test volume key: Press volume up, verify volume changed
6. Test brightness key: Press brightness up, verify brightness changed
7. Test custom keybinding: Press Control-Alt-S, verify speak-selection executes
8. Check services: `systemctl --user --failed`

### Expected Outcome
- If successful: Daemons start automatically on first login, all keys work
- If failed: Same "Cannot open display:" errors, or new timing issues

---

## Solution 2: Post-Login Hook

### Design
```
User logs in
  ↓
gnome-session starts (daemons may fail)
  ↓
~/.config/autostart/daemon-health-check.desktop executes
  ↓
Script checks daemon status, restarts if needed
  ↓
Keybindings work
```

### Implementation Steps

**Step 2a**: Create autostart desktop file

File: `~/.config/autostart/daemon-health-check.desktop`

```ini
[Desktop Entry]
Type=Application
Name=Daemon Health Check
Exec=/home/dawson/.local/bin/daemon-health-check.sh
OnlyShowIn=GNOME
NoDisplay=true
X-GNOME-Autostart-Phase=PreDisplayServer
```

**Step 2b**: Create health check script

File: `~/.local/bin/daemon-health-check.sh`

```bash
#!/bin/bash
# Wait 5 seconds for gnome-session to fully initialize
sleep 5

# Check and restart daemons if needed
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority
export DISPLAY XAUTHORITY

pgrep -x gsd-media-keys > /dev/null 2>&1 || /usr/libexec/gsd-media-keys &
pgrep -x gsd-power > /dev/null 2>&1 || /usr/libexec/gsd-power &

exit 0
```

### Test Procedure

1. Remove/disable Solution 1 overrides if testing in isolation
2. Create autostart desktop file
3. **Restart system**: `sudo systemctl reboot`
4. After login, wait 15 seconds (5s sleep + startup + 10s buffer)
5. Check daemons: `pgrep -a gsd-media-keys && pgrep -a gsd-power`
6. Test all three keybindings (volume, brightness, Control-Alt-S)
7. Check if desktop file actually executed: `journalctl -e` look for any errors

### Expected Outcome
- If successful: Script runs post-login, daemons start, keys work within 15 seconds
- If failed: Script doesn't run, or manual daemon start still fails

---

## Solution 3: Re-Login Trigger

### Design
```
System boots
  ↓
Daemon health check service runs (checks if daemons work)
  ↓
If broken: Display notification "Desktop needs refresh, please re-login"
  ↓
User logs out and back in
  ↓
gnome-session fully reinitializes all daemons
  ↓
Keys work
```

### Implementation Steps

**Step 3a**: Create keybinding test service

File: `~/.config/systemd/user/keybinding-health-check.service`

```ini
[Unit]
Description=Check Keybinding Health
After=graphical-session-ready.target
Requires=graphical-session-ready.target

[Service]
Type=oneshot
ExecStart=/home/dawson/.local/bin/test-keybindings.sh
RemainAfterExit=yes

[Install]
WantedBy=graphical-session-ready.target
```

**Step 3b**: Create keybinding test script

File: `~/.local/bin/test-keybindings.sh`

```bash
#!/bin/bash
# Test if keybindings are responsive

DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
export DISPLAY XAUTHORITY

# Wait for gnome-shell to fully initialize
sleep 5

# Try to query keybinding (xdotool can test if X11 is responsive)
if ! xdotool search --name "" > /dev/null 2>&1; then
  # Keybindings likely not working
  notify-send "System Issue" "Desktop keybindings not responsive. Please log out and back in." -u critical
  exit 1
fi

exit 0
```

### Test Procedure

1. Create both files (service + script)
2. Reload systemd: `systemctl --user daemon-reload`
3. **Restart system**: `sudo systemctl reboot`
4. After login, wait 15 seconds
5. If notification appears: Note the prompt
6. Test keybindings (should fail initially)
7. Log out: `gnome-session-quit --logout`
8. Log back in
9. Test keybindings again (should work now)

### Expected Outcome
- If successful: Notification appears, user re-logs in, keys work after re-login
- If failed: No notification, or notification but re-login doesn't help

---

## Test Execution Matrix

| Solution | Method | On First Login | After Re-Login | Daemons Running | Keys Working | Side Effects |
|----------|--------|---|---|---|---|---|
| 1 | gnome-session override | ? | N/A | ? | ? | ? |
| 2 | Post-login hook | ? | N/A | ? | ? | ? |
| 3 | Re-login trigger | ? | ? | ? | ? | ? |

(? = to be filled during testing)

---

## Test Execution Order

1. **Baseline Test** (no changes): Restart, log in, check daemon status → verify problem exists
2. **Solution 1**: Implement, restart, test
3. **Solution 2**: Remove Solution 1, implement Solution 2, restart, test
4. **Solution 3**: Remove Solution 2, implement Solution 3, restart, test
5. **Combination Test** (if successful): Enable solutions 1 + 2 together

---

## Metrics to Collect

For each test:
- Time from login to daemons becoming available
- Daemon startup success/failure count
- Keybinding response time
- Any error messages or side effects
- Desktop stability (crashes, hangs)

---

## Risk Assessment

**Solution 1** (gnome-session override): Medium
- Modifying gnome-session ordering could affect other autostart processes
- Could delay desktop initialization if display check takes too long

**Solution 2** (Post-login hook): Low
- Runs independently, non-blocking
- Worst case: daemons don't start (same as current state)

**Solution 3** (Re-login trigger): Low
- Only prompts user, doesn't force anything
- Leverages gnome-session's existing recovery

---

## Next Steps

1. Create actual test scripts (shell scripts + test execution logs)
2. Set up restart testing environment
3. Execute tests in sequence
4. Document results in stage_0_06_testing
5. Evaluate which solution(s) to implement permanently

