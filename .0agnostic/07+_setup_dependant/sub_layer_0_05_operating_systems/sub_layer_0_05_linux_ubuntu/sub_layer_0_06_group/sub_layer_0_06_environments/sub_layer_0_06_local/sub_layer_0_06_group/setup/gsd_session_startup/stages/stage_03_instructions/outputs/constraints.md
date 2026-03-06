---
resource_id: "d4e1a3f7-8b2c-4d91-a6e5-3f7c9b1d2e4a"
resource_type: "output"
resource_name: "constraints"
---

# GSD Session Startup — Constraints

<!-- section_id: "a1b2c3d4-5e6f-7a8b-9c0d-e1f2a3b4c5d6" -->
## System Environment

| Constraint | Detail |
|-----------|--------|
| Desktop | Unity (XDG_CURRENT_DESKTOP=Unity), NOT stock GNOME Shell |
| Display server | X11 (Wayland not active) |
| Display manager | GDM3 — always assigns DISPLAY=:0 on this single-seat laptop |
| Session manager | gnome-session manages gsd services via systemd targets |
| Init system | systemd (user instance at /run/user/1000/systemd/) |

<!-- section_id: "b2c3d4e5-6f7a-8b9c-0d1e-f2a3b4c5d6e7" -->
## environment.d Support

- `30-systemd-environment-d-generator` is present and active
- Processes `~/.config/environment.d/*.conf` at systemd user manager startup
- Runs BEFORE any target or service — guaranteed earliest environment injection
- Existing file: `~/.config/environment.d/nvidia-wayland.conf` (confirms format works)
- Format: `KEY=value` (one per line, no shell expansion)

<!-- section_id: "c3d4e5f6-7a8b-9c0d-1e2f-a3b4c5d6e7f8" -->
## GSD Service Characteristics

| Property | Value |
|----------|-------|
| Service type | `Type=dbus` |
| Restart policy | `Restart=on-failure` |
| Manual start | `RefuseManualStart=true` — cannot `systemctl start` the .service directly |
| Start method | Must start via `.target` (e.g., `org.gnome.SettingsDaemon.MediaKeys.target`) |
| Dependency | `After=gnome-session-initialized.target` |
| Rate limit | 5 failures in rapid succession → "Start request repeated too quickly" → permanent failure |
| Recovery | `systemctl --user reset-failed <service>` required before systemd will retry |

<!-- section_id: "d4e5f6a7-8b9c-0d1e-2f3a-b4c5d6e7f8a9" -->
## Dependency Chain

```
systemd user manager startup
  → 30-systemd-environment-d-generator (processes environment.d/*.conf)
    → graphical-session-pre.target
      → gnome-session-pre.target
        → gnome-session-initialized.target
          → org.gnome.SettingsDaemon.MediaKeys.service (After=)
          → org.gnome.SettingsDaemon.Power.service (After=)
```

**Critical constraint**: DISPLAY must be in the systemd user environment BEFORE `gnome-session-initialized.target` activates gsd services. environment.d injection happens at user manager startup (earliest possible point), well before any target.

<!-- section_id: "e5f6a7b8-9c0d-1e2f-3a4b-c5d6e7f8a9b0" -->
## Current Workaround Limitations

The current `gsd-keepalive.service` has several problems:

1. **Raw process spawning**: Uses `pgrep || /usr/libexec/gsd-media-keys &` — bypasses systemd service tracking
2. **Error suppression**: `2>/dev/null` hides startup failures (violates R6)
3. **No reset-failed**: Doesn't clear systemd's "permanently failed" state before retry
4. **Hardcoded DISPLAY**: `DISPLAY=:0` set inline per command (fragile)
5. **Race conditions**: No D-Bus name conflict prevention between raw process and systemd service
6. **Multi-instance risk**: Can spawn duplicate processes (violates R5)

<!-- section_id: "f6a7b8c9-0d1e-2f3a-4b5c-d6e7f8a9b0c1" -->
## Dead/Unused Services (Cleanup Candidates)

| Service | State | Why Dead |
|---------|-------|----------|
| `graphical-session-readiness.service` | disabled | Never activated, not needed |
| `graphical-session-ready.target` | disabled | Never activated, not needed |
| `gsd-keepalive-v2.service` | unused | Alternative attempt, never deployed |
| `gnome-session-binary.service.d/override.conf` | references disabled target | Depends on graphical-session-ready.target which is disabled |

<!-- section_id: "a7b8c9d0-1e2f-3a4b-5c6d-e7f8a9b0c1d2" -->
## DISPLAY=:0 Safety

On this system, DISPLAY=:0 is always correct because:
- Single-seat laptop (one physical console)
- GDM always assigns :0 to the first X session
- No multi-user/multi-seat configuration
- No remote X sessions

However, hardcoding DISPLAY=:0 in environment.d is still a static assumption. The safety net (display-ready.service ExecStartPost) provides runtime verification by importing the actual DISPLAY value after X11 is confirmed ready.
