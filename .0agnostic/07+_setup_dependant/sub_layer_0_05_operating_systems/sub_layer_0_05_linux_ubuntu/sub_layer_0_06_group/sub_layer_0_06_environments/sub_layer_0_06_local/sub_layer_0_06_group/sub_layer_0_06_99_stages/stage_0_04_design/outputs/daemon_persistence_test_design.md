---
resource_id: "5f2bde01-1569-4ca4-a763-a64253507680"
resource_type: "output"
resource_name: "daemon_persistence_test_design"
---
# Daemon Persistence After Restart — Test Suite Design

**Date**: 2026-02-26
**Objective**: Validate three solution approaches to daemon persistence

---

<!-- section_id: "95263c93-1ead-4dbb-91d9-a3d07de84255" -->
## Test Scenarios

All tests executed after a **full system restart** (power-off/on).

<!-- section_id: "0aa5a15c-5af9-4846-9f84-a04e1d09db61" -->
### Pre-Test State
- System powered off
- User logs back in
- GNOME session starts (daemons expected to fail initially)
- Tests execute

<!-- section_id: "c46ce9cc-7e80-478e-99b2-e3e4e7311f0d" -->
### Success Criteria (All Solutions)
- ✓ `pgrep -a gsd-media-keys` returns process
- ✓ `pgrep -a gsd-power` returns process
- ✓ Volume key press changes volume (`pactl get-sink-volume @DEFAULT_SINK@`)
- ✓ Brightness key press changes brightness
- ✓ Control-Alt-S hotkey responds (triggers speak-selection)
- ✓ `systemctl --user --failed` shows 0 failed services (or excludes gsd-*)

---

<!-- section_id: "735e63f6-82f4-427a-90c4-0500346b4a5b" -->
## Solution 1: Fix gnome-session Service Startup Order

<!-- section_id: "29c5bcfd-4ff8-4361-839d-0f30bdbab118" -->
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

<!-- section_id: "36453ef5-5376-4e18-b67c-5f478791caa2" -->
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

<!-- section_id: "eccc9941-9325-48c5-bf5f-bdcc5a5c0e2f" -->
### Test Procedure

1. Reload systemd: `systemctl --user daemon-reload`
2. **Restart system**: `sudo systemctl reboot`
3. After login, wait 10 seconds
4. Check daemons: `pgrep -a gsd-media-keys && pgrep -a gsd-power`
5. Test volume key: Press volume up, verify volume changed
6. Test brightness key: Press brightness up, verify brightness changed
7. Test custom keybinding: Press Control-Alt-S, verify speak-selection executes
8. Check services: `systemctl --user --failed`

<!-- section_id: "0e641d15-844c-490c-aa7c-0c17139be8b0" -->
### Expected Outcome
- If successful: Daemons start automatically on first login, all keys work
- If failed: Same "Cannot open display:" errors, or new timing issues

---

<!-- section_id: "47d91bb6-ed78-4e81-847c-9a881e810877" -->
## Solution 2: Post-Login Hook

<!-- section_id: "6b40b76d-e4f7-4662-8823-83e6a06b205c" -->
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

<!-- section_id: "035692b1-4238-4acf-844b-8dbe534271ab" -->
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

<!-- section_id: "3533702b-4139-47cf-9388-4d33ede32929" -->
### Test Procedure

1. Remove/disable Solution 1 overrides if testing in isolation
2. Create autostart desktop file
3. **Restart system**: `sudo systemctl reboot`
4. After login, wait 15 seconds (5s sleep + startup + 10s buffer)
5. Check daemons: `pgrep -a gsd-media-keys && pgrep -a gsd-power`
6. Test all three keybindings (volume, brightness, Control-Alt-S)
7. Check if desktop file actually executed: `journalctl -e` look for any errors

<!-- section_id: "7efe8907-7593-48c9-9720-556a0900130c" -->
### Expected Outcome
- If successful: Script runs post-login, daemons start, keys work within 15 seconds
- If failed: Script doesn't run, or manual daemon start still fails

---

<!-- section_id: "6219db4c-df01-4f82-9e25-53f71f6e2d4f" -->
## Solution 3: Re-Login Trigger

<!-- section_id: "607d39f0-4585-46de-8cb4-f6d8b1d194a7" -->
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

<!-- section_id: "5b294c9a-de58-4acb-bca3-6e64a492baa4" -->
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

<!-- section_id: "383792b0-2875-463c-b855-d76ba7ba54e3" -->
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

<!-- section_id: "f73ed8ba-9c52-4fe4-bc85-84f46983f49d" -->
### Expected Outcome
- If successful: Notification appears, user re-logs in, keys work after re-login
- If failed: No notification, or notification but re-login doesn't help

---

<!-- section_id: "cc87647a-c495-478d-a63c-c279f90e2a19" -->
## Test Execution Matrix

| Solution | Method | On First Login | After Re-Login | Daemons Running | Keys Working | Side Effects |
|----------|--------|---|---|---|---|---|
| 1 | gnome-session override | ? | N/A | ? | ? | ? |
| 2 | Post-login hook | ? | N/A | ? | ? | ? |
| 3 | Re-login trigger | ? | ? | ? | ? | ? |

(? = to be filled during testing)

---

<!-- section_id: "2b73a2e6-13d9-4bb8-8401-44c4158d4851" -->
## Test Execution Order

1. **Baseline Test** (no changes): Restart, log in, check daemon status → verify problem exists
2. **Solution 1**: Implement, restart, test
3. **Solution 2**: Remove Solution 1, implement Solution 2, restart, test
4. **Solution 3**: Remove Solution 2, implement Solution 3, restart, test
5. **Combination Test** (if successful): Enable solutions 1 + 2 together

---

<!-- section_id: "715895c2-0204-4f46-8cee-d94f4a19de02" -->
## Metrics to Collect

For each test:
- Time from login to daemons becoming available
- Daemon startup success/failure count
- Keybinding response time
- Any error messages or side effects
- Desktop stability (crashes, hangs)

---

<!-- section_id: "adb6a888-f037-4241-a7cc-c4cb151c2756" -->
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

<!-- section_id: "828a9d37-1f99-4225-9b24-6aa6878f1fee" -->
## Next Steps

1. Create actual test scripts (shell scripts + test execution logs)
2. Set up restart testing environment
3. Execute tests in sequence
4. Document results in stage_0_06_testing
5. Evaluate which solution(s) to implement permanently

