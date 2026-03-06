---
resource_id: "e5f6a7b8-c9d0-1234-efab-456789012345"
resource_type: "output"
resource_name: "solution_overview"
---
# GSD Session Startup — Solution Overview (Pre-Testing)

**Date**: 2026-03-06
**Status**: Pre-testing — designs ready, none tested after reboot yet
**Source**: Consolidated from parent entity's `daemon_persistence_test_design.md`

<!-- section_id: "d6e7f8a9-0b1c-2d3e-4f5a-6b7c8d9e0f1a" -->
## Solution 1: gnome-session Service Startup Order Override

**Approach**: Create a systemd readiness gate that blocks gsd services until DISPLAY is available.

```
graphical-session.target (existing)
  ↓ (requires)
graphical-session-readiness.service (runs wait-for-display.sh)
  ↓ (succeeds when display ready)
graphical-session-ready.target (our new target)
  ↓ (gnome-session depends on this)
gsd-media-keys, gsd-power can now start reliably
```

**Files**:
- `~/.config/systemd/user/graphical-session.target.d/override.conf` — Requires readiness service
- `~/.config/systemd/user/gnome-session-binary.service.d/override.conf` — Wants + After readiness target

**Risk**: Medium — modifying gnome-session ordering could affect other autostart processes

**Existing implementation**: Parent entity `daemon_persistence_test_design.md` has full config

<!-- section_id: "e7f8a90b-1c2d-3e4f-5a6b-7c8d9e0f1a2b" -->
## Solution 2: Post-Login Autostart Hook

**Approach**: XDG autostart `.desktop` file that runs after login, checks daemon health, restarts if needed.

```
User logs in → gnome-session starts (daemons may fail)
  ↓
~/.config/autostart/daemon-health-check.desktop executes
  ↓
Script waits 5s, checks daemons, restarts if dead
  ↓
Keybindings work
```

**Files**:
- `~/.config/autostart/daemon-health-check.desktop` — Autostart entry
- `~/.local/bin/daemon-health-check.sh` — Health check + restart script

**Risk**: Low — runs independently, non-blocking, worst case same as current state

**Key improvement over keepalive**: Runs once at login (not every 60s), can include `systemctl --user reset-failed` to clear the D-Bus name conflict, eliminates the ~5 min dead zone.

<!-- section_id: "f8a90b1c-2d3e-4f5a-6b7c-8d9e0f1a2b3c" -->
## Solution 3: Re-Login Trigger Notification

**Approach**: Detect broken state, notify user to log out and back in.

```
System boots → health check service runs
  ↓
If broken: notify-send "Desktop needs refresh, please re-login"
  ↓
User logs out/in → gnome-session fully reinitializes
  ↓
Keys work
```

**Files**:
- `~/.config/systemd/user/keybinding-health-check.service` — After graphical-session-ready
- `~/.local/bin/test-keybindings.sh` — Tests X11 responsiveness with xdotool

**Risk**: Low — only prompts user, doesn't force anything

**Limitation**: Requires manual user action (logout/login). Not automated.

<!-- section_id: "a90b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d" -->
## Recommended Test Order

1. **Baseline**: Fresh reboot, no changes → confirm problem exists (already done 2026-03-06)
2. **Solution 2** (lowest risk): Post-login hook with `reset-failed` + restart
3. **Solution 1** (medium risk): systemd ordering override
4. **Solution 3** (fallback): Re-login notification if nothing else works
5. **Combination**: Solutions 1 + 2 together for defense in depth

<!-- section_id: "b0c1d2e3-4f5a-6b7c-8d9e-0f1a2b3c4d5e" -->
## New Solution Idea: Early DISPLAY Import

**Not in original 3 solutions** — discovered during root cause analysis:

The simplest possible fix: an XDG autostart script (or systemd user service) that runs `systemctl --user import-environment DISPLAY XAUTHORITY` as early as possible in the login sequence, BEFORE gsd services trigger.

This directly addresses the root cause (DISPLAY not in systemd env) without restructuring service dependencies.

**To investigate**: What autostart phase runs before gsd services? Can we use `X-GNOME-Autostart-Phase=EarlyInitialization`?

<!-- section_id: "c1d2e3f4-5a6b-7c8d-9e0f-1a2b3c4d5e6f" -->
## Success Criteria

From `requirements_tree.md`:
1. Custom keybindings work within 30 seconds of desktop appearing
2. Brightness keys change brightness and OSD appears
3. No manual intervention required
4. No duplicate daemon processes
5. Journal shows clean startup
6. Keepalive timer becomes safety net, not necessity
