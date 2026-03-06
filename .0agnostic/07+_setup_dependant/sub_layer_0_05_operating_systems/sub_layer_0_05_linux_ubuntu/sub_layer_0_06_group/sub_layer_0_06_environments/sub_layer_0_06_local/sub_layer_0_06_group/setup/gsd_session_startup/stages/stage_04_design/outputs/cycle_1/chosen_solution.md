---
resource_id: "e8f2a1b3-4c5d-6e7f-8a9b-0c1d2e3f4a5b"
resource_type: "output"
resource_name: "chosen_solution_cycle_1"
---

# GSD Session Startup — Chosen Solution (Cycle 1)

<!-- section_id: "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d" -->
## Solution Architecture

Three-layer defense:

1. **Primary Fix** — `environment.d` DISPLAY import (prevents the problem)
2. **Safety Net** — Enhanced `display-ready.service` (runtime verification)
3. **Recovery** — Improved `gsd-keepalive.service` (proper systemd restart)

<!-- section_id: "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e" -->
## Layer 1: Primary Fix — environment.d DISPLAY Import

**File**: `~/.config/environment.d/10-display.conf`

```ini
DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
```

**How it works**:
- `30-systemd-environment-d-generator` processes this at systemd user manager startup
- Runs BEFORE any targets or services activate
- When `gnome-session-initialized.target` triggers gsd services, DISPLAY is already in their environment
- Eliminates the 5 rapid "Cannot open display:" crashes entirely

**Why environment.d**:
- Earliest possible injection point — before any service starts
- No timing dependencies or race conditions
- Survives Ubuntu upgrades (user config, not system)
- Already proven on this system (`nvidia-wayland.conf` uses same mechanism)
- Zero additional services or scripts needed

**Tradeoff**: Static DISPLAY=:0 assumption. Acceptable on this single-seat GDM laptop. Safety net (Layer 2) provides runtime backup.

<!-- section_id: "3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f" -->
## Layer 2: Safety Net — Enhanced display-ready.service

**File**: `~/.config/systemd/user/display-ready.service`

**Change**: Add `ExecStartPost` to import the runtime DISPLAY value:

```ini
ExecStartPost=/usr/bin/systemctl --user import-environment DISPLAY XAUTHORITY
```

**Why**: Belt-and-suspenders approach. Even if environment.d doesn't work for some reason (e.g., generator disabled, config file corrupted), display-ready.service will import DISPLAY once X11 is confirmed ready. This also imports the actual runtime DISPLAY value rather than a static assumption.

<!-- section_id: "4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a" -->
## Layer 3: Recovery — Improved gsd-keepalive.service

**File**: `~/.config/systemd/user/gsd-keepalive.service`

**Complete rewrite** — replace raw process spawning with proper systemd commands:

```ini
[Unit]
Description=GSD Keepalive - Restart failed GSD services via systemd
After=display-ready.service
Wants=display-ready.service

[Service]
Type=oneshot
ExecStart=/bin/bash -c '\
  for svc in org.gnome.SettingsDaemon.MediaKeys org.gnome.SettingsDaemon.Power; do \
    if systemctl --user is-failed "$svc.service" 2>/dev/null; then \
      echo "Resetting failed $svc..." ; \
      systemctl --user reset-failed "$svc.service" ; \
      systemctl --user restart "$svc.target" ; \
      echo "Restarted $svc.target" ; \
    elif ! systemctl --user is-active "$svc.service" 2>/dev/null; then \
      echo "Starting inactive $svc..." ; \
      systemctl --user start "$svc.target" ; \
    else \
      echo "$svc already active" ; \
    fi ; \
  done'
```

**Improvements over current keepalive**:
- Uses `reset-failed` before restart (clears "Start request repeated too quickly" state)
- Starts via `.target` (not raw process — respects RefuseManualStart=true)
- No error suppression (logging visible in journal)
- No multi-instance risk (systemd manages single instance)
- No `wait-for-display.sh` needed (environment.d handles DISPLAY)

**Timer**: Reduce `OnBootSec` from 60s to 10s for faster first recovery.

<!-- section_id: "5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b" -->
## Cleanup: Dead Services

Remove unused services that add confusion:

| File | Action | Reason |
|------|--------|--------|
| `gsd-keepalive-v2.service` | DELETE | Unused alternative, never deployed |
| `gnome-session-binary.service.d/override.conf` | DELETE | References disabled graphical-session-ready.target |
| `graphical-session-readiness.service` | Leave disabled | May be needed for future reference, harmless when disabled |
| `graphical-session-ready.target` | Leave disabled | May be needed for future reference, harmless when disabled |

<!-- section_id: "6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c" -->
## Requirements Coverage

| Requirement | How Addressed |
|-------------|---------------|
| R1: gsd-media-keys running | environment.d prevents crash; keepalive restarts if needed |
| R2: gsd-power running | Same mechanism as R1 |
| R3: DISPLAY available before services | environment.d provides at user manager startup |
| R4: No ~5 min dead zone | environment.d prevents initial failure; keepalive at 10s if needed |
| R5: No multi-instance | Keepalive uses systemd restart (not raw spawn) |
| R6: Visible errors | No 2>/dev/null; all output to journal |

<!-- section_id: "7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d" -->
## Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| DISPLAY changes from :0 | Very low (single-seat GDM) | Safety net imports runtime value |
| environment.d generator removed | Very low (core systemd) | display-ready.service as backup |
| gsd services fail for non-DISPLAY reason | Low | Keepalive timer provides recovery |
| Ubuntu upgrade resets user services | None (user config preserved) | N/A |

<!-- section_id: "8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e" -->
## Cycle 2 Revision: GDK_BACKEND Override

**Discovered during testing**: `nvidia-wayland.conf` in environment.d sets `GDK_BACKEND=wayland` for all systemd user services. Since gsd services are GDK-based, they try to connect to a Wayland display instead of X11, regardless of DISPLAY being set.

**Addition**: Service drop-in directories for both gsd services:
- `~/.config/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service.d/display.conf`
- `~/.config/systemd/user/org.gnome.SettingsDaemon.Power.service.d/display.conf`

Each sets `Environment=GDK_BACKEND=x11` in addition to DISPLAY and XAUTHORITY.

**Why service drop-ins instead of environment.d**: nvidia-wayland.conf (`GDK_BACKEND=wayland`) may be needed for other applications. Setting `GDK_BACKEND=x11` globally would break those. Service drop-ins override only for gsd services.

## Previous Solutions Considered

See `../pre_testing/solution_overview.md` for the 3 original approaches (systemd ordering override, post-login autostart hook, re-login notification). The environment.d approach was identified during research as superior to all three because it eliminates the race condition at the earliest possible point rather than working around it.
