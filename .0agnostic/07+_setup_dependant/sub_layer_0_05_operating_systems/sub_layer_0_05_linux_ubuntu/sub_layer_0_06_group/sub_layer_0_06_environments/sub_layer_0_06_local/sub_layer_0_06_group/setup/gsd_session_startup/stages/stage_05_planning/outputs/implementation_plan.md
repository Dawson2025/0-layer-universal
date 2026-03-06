---
resource_id: "f1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6"
resource_type: "output"
resource_name: "implementation_plan"
---

# GSD Session Startup — Implementation Plan

<!-- section_id: "0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d" -->
## Overview

6 implementation steps, 2 verification phases (pre-reboot and post-reboot).

All system file changes are in `~/.config/` (user config, no root needed).

<!-- section_id: "1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e" -->
## Step 1: Create environment.d Config

**Action**: Create `~/.config/environment.d/10-display.conf`

```ini
DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
```

**Verification**: File exists, correct permissions (644).

<!-- section_id: "2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f" -->
## Step 2: Enhance display-ready.service

**Action**: Add ExecStartPost line to `~/.config/systemd/user/display-ready.service`

```ini
ExecStartPost=/usr/bin/systemctl --user import-environment DISPLAY XAUTHORITY
```

**Verification**: `systemctl --user cat display-ready.service` shows the new line.

<!-- section_id: "3d4e5f6a-7b8c-9d0e-1f2a-3b4c5d6e7f8a" -->
## Step 3: Rewrite gsd-keepalive.service

**Action**: Replace entire `~/.config/systemd/user/gsd-keepalive.service` with proper systemd restart logic.

Key changes:
- Remove `ExecStartPre` (wait-for-display.sh no longer needed)
- Replace `pgrep || spawn` with `reset-failed` + `restart .target`
- Keep `After=display-ready.service` dependency
- Remove all `2>/dev/null` error suppression

**Verification**: `systemctl --user cat gsd-keepalive.service` shows new content.

<!-- section_id: "4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b" -->
## Step 4: Update gsd-keepalive.timer

**Action**: Change `OnBootSec=60` to `OnBootSec=10` in `~/.config/systemd/user/gsd-keepalive.timer`

**Rationale**: Faster first recovery attempt. With environment.d, this timer should rarely be needed, but when it is, 10s is better than 60s.

<!-- section_id: "5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c" -->
## Step 5: Clean Up Dead Services

**Action**:
- Delete `~/.config/systemd/user/gsd-keepalive-v2.service`
- Delete `~/.config/systemd/user/gnome-session-binary.service.d/override.conf`

**Verification**: Files no longer exist.

<!-- section_id: "6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d" -->
## Step 6: Reload and Pre-Reboot Test

**Action**:
```bash
systemctl --user daemon-reload
```

**Pre-reboot verification** (no reboot needed):
1. `systemctl --user show-environment | grep DISPLAY` — should show `:0`
2. Manual recovery test:
   ```bash
   systemctl --user reset-failed org.gnome.SettingsDaemon.MediaKeys.service
   systemctl --user restart org.gnome.SettingsDaemon.MediaKeys.target
   systemctl --user reset-failed org.gnome.SettingsDaemon.Power.service
   systemctl --user restart org.gnome.SettingsDaemon.Power.target
   ```
3. `systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service` — should be `active`
4. `systemctl --user is-active org.gnome.SettingsDaemon.Power.service` — should be `active`
5. Test Ctrl+Alt+S keybinding (speak-selection)
6. Test brightness keys (Fn+F5/F6) + OSD
7. `pgrep -c gsd-media-keys` — should return 1
8. `pgrep -c gsd-power` — should return 1

<!-- section_id: "7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e" -->
## Post-Reboot Verification (User-Triggered)

After reboot:
1. `journalctl --user -b -u org.gnome.SettingsDaemon.MediaKeys --no-pager` — no "Cannot open display:" errors
2. `journalctl --user -b -u org.gnome.SettingsDaemon.Power --no-pager` — no "Cannot open display:" errors
3. `systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service` — active
4. `systemctl --user is-active org.gnome.SettingsDaemon.Power.service` — active
5. Ctrl+Alt+S works within 30 seconds of desktop appearing
6. Brightness keys work + OSD appears
7. `pgrep -c gsd-media-keys` returns 1 (no duplicates)
8. `pgrep -c gsd-power` returns 1 (no duplicates)

<!-- section_id: "8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f" -->
## Rollback Plan

If the fix causes issues:
1. Delete `~/.config/environment.d/10-display.conf`
2. Restore original `gsd-keepalive.service` (uses pgrep||spawn pattern)
3. `systemctl --user daemon-reload`
4. The keepalive timer will resume managing services as before
