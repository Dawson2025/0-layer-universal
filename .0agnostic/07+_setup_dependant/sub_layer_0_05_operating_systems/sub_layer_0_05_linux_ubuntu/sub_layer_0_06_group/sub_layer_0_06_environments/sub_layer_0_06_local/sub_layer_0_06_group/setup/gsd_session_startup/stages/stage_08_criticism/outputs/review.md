---
resource_id: "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a"
resource_type: "output"
resource_name: "review"
---

# GSD Session Startup — Criticism / Review

## Date: 2026-03-06

### What Worked

1. **environment.d approach**: Confirmed that `30-systemd-environment-d-generator` processes `~/.config/environment.d/*.conf` and makes variables available to all systemd user services. DISPLAY=:0 is correctly propagated.

2. **Service drop-in pattern**: systemd drop-in directories (`.service.d/display.conf`) correctly override/add environment variables to stock system services without modifying the originals.

3. **Rewritten keepalive**: Using `reset-failed` + `restart .target` instead of `pgrep || spawn` properly manages services through systemd, preventing duplicates and maintaining D-Bus name integrity.

4. **Enhanced display-ready.service**: Adding `ExecStartPost` for runtime DISPLAY import provides a belt-and-suspenders backup.

### What Didn't Work (Initially)

1. **environment.d alone was insufficient**: The original design assumed that setting `DISPLAY=:0` in environment.d would be enough. It wasn't — because `nvidia-wayland.conf` sets `GDK_BACKEND=wayland` which causes gsd to ignore DISPLAY and try Wayland.

2. **The research missed GDK_BACKEND**: The stage_02 research identified DISPLAY as the root cause by testing from the shell (which had `GDK_BACKEND=x11` from the login session). The systemd service environment has `GDK_BACKEND=wayland` from nvidia-wayland.conf, which wasn't tested.

### Design Revision (Cycle 2 changes)

Added to the solution:
- **Service drop-in directories** for both gsd services with `GDK_BACKEND=x11`
- This wasn't in the Cycle 1 design and was discovered during testing

### Open Questions

1. **Should nvidia-wayland.conf be fixed?** Currently it sets `GDK_BACKEND=wayland` for ALL systemd user services. Since the system runs X11, this is incorrect. However, it may have been added intentionally for specific apps. For now, the service drop-ins override it only for gsd services. A broader fix would be to comment out or condition the `GDK_BACKEND` line.

2. **Is DISPLAY=:0 always correct?** Yes for this single-seat GDM laptop. If multi-seat or remote X ever becomes relevant, the service drop-ins would need updating.

3. **Should keepalive timer be removed?** No — keep as safety net. If environment.d + drop-ins work correctly at boot, the keepalive will log "already active" and do nothing. But if something unexpected fails, it provides automatic recovery.

4. **Post-reboot validation pending**: The pre-reboot test confirms the fix works mid-session. Post-reboot testing will confirm environment.d is processed early enough.

### Survivability

| Concern | Assessment |
|---------|-----------|
| Ubuntu upgrade | environment.d and drop-in files are in user config (`~/.config/`), not overwritten by upgrades |
| gnome-settings-daemon update | Drop-in directories survive package updates (user override takes precedence) |
| nvidia-wayland.conf change | Service drop-ins explicitly set GDK_BACKEND, independent of nvidia-wayland.conf |
| Session type change to Wayland | Would need to update drop-ins (remove GDK_BACKEND=x11) |
