---
resource_id: "d2788dbf-8376-4aee-aa93-41946b91f01b"
resource_type: "output"
resource_name: "sync_health_service_fix"
---
# Sync Health Service Fix

<!-- section_id: "54852f2b-08b4-477c-acc9-52079020df56" -->
## Problem

`sync-health.service` failing with status 203/EXEC, causing system to be in "degraded" state.

```
× sync-health.service - Syncthing Health Monitor
  Process: ExecStart=/.../sync-health-monitor.sh (code=exited, status=203/EXEC)
```

<!-- section_id: "cff25197-fb7e-468a-b2e2-20598132b196" -->
## Root Cause

The service file referenced an outdated path that no longer exists:
```
/home/dawson/dawson-workspace/code/0_layer_universal/-1_research/-1.01_things_researched/multi_os_system/sync-health-monitor.sh
```

The script was moved during a restructuring to:
```
/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_better_setup_system/layer_1/layer_1_features/layer_1_feature_multi_os_system/layer_1/layer_1_99_stages/stage_1_06_development/outputs/code/sync-health-monitor.sh
```

<!-- section_id: "782f7fb3-55bc-4411-8f8b-3989c64cfb21" -->
## Solution

<!-- section_id: "046be17d-6571-4460-9bb8-29402ad5bad3" -->
### 1. Update Service File

Edit `/home/dawson/.config/systemd/user/sync-health.service`:

```ini
[Unit]
Description=Syncthing Health Monitor

[Service]
Type=oneshot
ExecStart=/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_better_setup_system/layer_1/layer_1_features/layer_1_feature_multi_os_system/layer_1/layer_1_99_stages/stage_1_06_development/outputs/code/sync-health-monitor.sh
StandardOutput=journal
StandardError=journal
```

<!-- section_id: "d659103c-5767-4a3f-9b24-9a0a794e5cd2" -->
### 2. Reload and Test

```bash
systemctl --user daemon-reload
systemctl --user reset-failed
systemctl --user start sync-health.service
systemctl --user status sync-health.service
```

<!-- section_id: "96bc162b-22a6-4998-8aa7-23e4611b0da4" -->
### 3. Verify System Status

```bash
systemctl --user is-system-running  # Should show: running
```

<!-- section_id: "278566f9-f3a1-41e7-8887-1b8fb6e40531" -->
## File Locations

| File | Purpose |
|------|---------|
| `~/.config/systemd/user/sync-health.service` | Service unit file |
| `~/.config/systemd/user/sync-health.timer` | Timer that triggers the service |
| `.../sync-health-monitor.sh` | The actual monitoring script |

<!-- section_id: "c2cff66a-dc91-473c-b48a-aea4c61c2aa3" -->
## Prevention

When restructuring the codebase, ensure systemd service files are updated to reflect new paths. Consider using symlinks or environment variables for frequently-moved scripts.

---
*Fixed: 2026-01-25*
