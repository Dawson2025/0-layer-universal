---
resource_id: "57846c13-8a42-4f71-ab3c-233d9e3b4e0e"
resource_type: "output"
resource_name: "00_test_overview"
---
# Daemon Persistence After Restart — Test Suite Design

**Date**: 2026-02-26
**Objective**: Validate three solution approaches to daemon persistence

---

<!-- section_id: "9035fc63-c311-46cc-ae60-be4d62192e4d" -->
## Test Scenarios

All tests executed after a **full system restart** (power-off/on).

<!-- section_id: "3c63dd13-cb32-484c-b7dc-68359ead4a0c" -->
### Pre-Test State
- System powered off
- User logs back in
- GNOME session starts (daemons expected to fail initially)
- Tests execute

<!-- section_id: "537f1ee2-dca1-4607-bc87-8c7e57a98cfb" -->
### Success Criteria (All Solutions)
- ✓ `pgrep -a gsd-media-keys` returns process
- ✓ `pgrep -a gsd-power` returns process
- ✓ Volume key press changes volume (`pactl get-sink-volume @DEFAULT_SINK@`)
- ✓ Brightness key press changes brightness
- ✓ Control-Alt-S hotkey responds (triggers speak-selection)
- ✓ `systemctl --user --failed` shows 0 failed services (or excludes gsd-*)

---

<!-- section_id: "7532ff37-80f6-4d6c-9ae9-304d3f8f2783" -->
## Solution 1: Fix gnome-session Service Startup Order

<!-- section_id: "a7bf35e1-7a89-4d2b-ab6d-654dcb2fc504" -->
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

<!-- section_id: "71e60d35-0fb8-4ae8-8130-48a7358bd314" -->
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

<!-- section_id: "e8845a0b-56e2-45b5-8f34-5ab2fba88e55" -->
### Test Procedure

1. Reload systemd: `systemctl --user daemon-reload`
2. **Restart system**: `sudo systemctl reboot`
3. After login, wait 10 seconds
4. Check daemons: `pgrep -a gsd-media-keys && pgrep -a gsd-power`
5. Test volume key: Press volume up, verify volume changed
6. Test brightness key: Press brightness up, verify brightness changed
7. Test custom keybinding: Press Control-Alt-S, verify speak-selection executes
8. Check services: `systemctl --user --failed`

<!-- section_id: "77b1e193-1f50-40bb-9796-a562a30e52a9" -->
### Expected Outcome
- If successful: Daemons start automatically on first login, all keys work
- If failed: Same "Cannot open display:" errors, or new timing issues

---

<!-- section_id: "21fa4d4d-a21f-4c88-8f83-9e5ccdc903a6" -->
## Solution 2: Post-Login Hook

<!-- section_id: "16073fd4-e5e7-4dc9-8c23-0bc887fdee1c" -->
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

<!-- section_id: "d5cc69cf-ae1c-414a-9ee4-0a1e7d1195c0" -->
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

<!-- section_id: "fa321425-8ed9-4c12-8afa-8c293bc7d35f" -->
### Test Procedure

1. Remove/disable Solution 1 overrides if testing in isolation
2. Create autostart desktop file
3. **Restart system**: `sudo systemctl reboot`
4. After login, wait 15 seconds (5s sleep + startup + 10s buffer)
5. Check daemons: `pgrep -a gsd-media-keys && pgrep -a gsd-power`
6. Test all three keybindings (volume, brightness, Control-Alt-S)
7. Check if desktop file actually executed: `journalctl -e` look for any errors

<!-- section_id: "f31ced49-0ee1-40fc-868c-f0e31fca6ba8" -->
### Expected Outcome
- If successful: Script runs post-login, daemons start, keys work within 15 seconds
- If failed: Script doesn't run, or manual daemon start still fails

---

<!-- section_id: "0753e251-a7ca-4969-a06a-52a5f2844d1d" -->
## Solution 3: Re-Login Trigger

<!-- section_id: "fcb80530-d082-40ef-8c99-1cbf1b377093" -->
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

<!-- section_id: "96fdabac-7aed-4870-a6fc-e1f7e4fdfd6a" -->
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

<!-- section_id: "666d44b1-6b5d-457b-8c85-f36ce5ee4f9b" -->
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

<!-- section_id: "e58b3d69-09a1-48d3-902d-232cfb7920bc" -->
### Expected Outcome
- If successful: Notification appears, user re-logs in, keys work after re-login
- If failed: No notification, or notification but re-login doesn't help

---

<!-- section_id: "03aea03c-6262-45bc-bba7-9df8dfc3ce11" -->
## Test Execution Matrix

| Solution | Method | On First Login | After Re-Login | Daemons Running | Keys Working | Side Effects |
|----------|--------|---|---|---|---|---|
| 1 | gnome-session override | ? | N/A | ? | ? | ? |
| 2 | Post-login hook | ? | N/A | ? | ? | ? |
| 3 | Re-login trigger | ? | ? | ? | ? | ? |

(? = to be filled during testing)

---

<!-- section_id: "364d5f48-0e9f-442e-a934-c5a9d9d73f91" -->
## Test Execution Order

1. **Baseline Test** (no changes): Restart, log in, check daemon status → verify problem exists
2. **Solution 1**: Implement, restart, test
3. **Solution 2**: Remove Solution 1, implement Solution 2, restart, test
4. **Solution 3**: Remove Solution 2, implement Solution 3, restart, test
5. **Combination Test** (if successful): Enable solutions 1 + 2 together

---

<!-- section_id: "845f41ce-da5c-4994-863e-7f8b0dfa32d8" -->
## Metrics to Collect

For each test:
- Time from login to daemons becoming available
- Daemon startup success/failure count
- Keybinding response time
- Any error messages or side effects
- Desktop stability (crashes, hangs)

---

<!-- section_id: "c139b2ea-4c5b-4675-b27e-04df99a24cb2" -->
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

<!-- section_id: "01a81c45-8d0e-4872-a1a0-2ded1837702a" -->
## Next Steps

1. Create actual test scripts (shell scripts + test execution logs)
2. Set up restart testing environment
3. Execute tests in sequence
4. Document results in stage_0_06_testing
5. Evaluate which solution(s) to implement permanently

