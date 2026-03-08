---
resource_id: "b3e7d4a1-f892-4c5b-9a6e-1d8f3c7b2e40"
resource_type: "output"
resource_name: "performance_mode"
---
# performance-mode — System Performance Profile Manager

<!-- section_id: "a4f5b6c7-d8e9-4f0a-1b2c-3d4e5f6a7b8c" -->
## Status: Active (installed 2026-03-07)

## Purpose

Single command to switch the entire system between three performance tiers: quiet, normal, and max. Controls platform profile, CPU governor, fan mode, and GPU clock limits in one shot.

Replaces the previous always-max-at-boot configuration with a user-controlled toggle system. The system boots into **normal** mode by default.

<!-- section_id: "c5d6e7f8-a9b0-4c1d-2e3f-4a5b6c7d8e9f" -->
## Installation

| Component | Location |
|-----------|----------|
| Script | `/home/dawson/dawson-workspace/scripts/performance-mode` |
| Symlink | `/usr/local/bin/performance-mode` → script |
| Permissions | Script is `+x`, symlink owned by root |

The command self-elevates via `sudo` when switching modes (status check needs no elevation).

<!-- section_id: "d6e7f8a9-b0c1-4d2e-3f4a-5b6c7d8e9f0a" -->
## Usage

```bash
performance-mode              # Show current mode + thermals
performance-mode --quiet      # or -q
performance-mode --normal     # or -n
performance-mode --max        # or -m
performance-mode --help       # or -h
```

<!-- section_id: "e7f8a9b0-c1d2-4e3f-4a5b-6c7d8e9f0a1b" -->
## Mode Definitions

| Setting | `--quiet` | `--normal` | `--max` |
|---------|-----------|------------|---------|
| Platform profile | `low-power` | `balanced` | `performance` |
| CPU governor | `powersave` | `powersave` | `performance` (all 22 cores) |
| Fan mode | auto (0) | auto (0) | max (1) |
| GPU clocks | 210-900 MHz | 210-1200 MHz | 210-3105 MHz (uncapped) |
| Use case | Meeting, library, browsing | Everyday coding, light work | ML training, heavy builds |

### Ordering Logic

- **Stepping down** (max → normal/quiet): GPU clocks are capped FIRST (reduce heat before slowing fans)
- **Stepping up** (quiet/normal → max): Platform profile and CPU governor set FIRST (let CPU boost immediately, then uncap GPU)

<!-- section_id: "f8a9b0c1-d2e3-4f4a-5b6c-7d8e9f0a1b2c" -->
## Boot Behavior

The system boots into **normal** mode:
- `nvidia-gpu-clocks.service` (enabled at boot) caps GPU at 210-1200 MHz
- `fan-mode-max.service` is **disabled** at boot — fans start on auto
- Platform profile defaults to `balanced`
- CPU governor defaults to `powersave`

To engage max mode for ML training, run `performance-mode --max` after boot.

<!-- section_id: "a9b0c1d2-e3f4-4a5b-6c7d-8e9f0a1b2c3d" -->
## Changes Made (2026-03-07)

| Change | Before | After |
|--------|--------|-------|
| `fan-mode-max.service` | enabled (fans always max at boot) | disabled (fans on auto at boot) |
| Fan control | Always max, no toggle | `performance-mode` toggles between modes |
| GPU control | Always capped at 1200 MHz | Capped at 900/1200/uncapped depending on mode |
| CPU governor | Always `powersave` | `powersave` for quiet/normal, `performance` for max |
| Platform profile | Always `performance` | `low-power`/`balanced`/`performance` per mode |

<!-- section_id: "b0c1d2e3-f4a5-4b6c-7d8e-9f0a1b2c3d4e" -->
## Related Services (Still Active)

| Service | Type | What It Does |
|---------|------|-------------|
| `nvidia-gpu-clocks.service` | system, enabled | Caps GPU at 1200 MHz at boot (normal mode default) |
| `coolercontrold.service` | system, enabled | CoolerControl daemon for fan curve management |
| `thermald.service` | system, enabled | Intel thermal daemon with adaptive mode |
| `hardware-health-snapshot.timer` | user, enabled | Telemetry snapshot every 5 min |
| `fan-mode-max.service` | system, **disabled** | Was always-max; now disabled, controlled by perfmode |

<!-- section_id: "c1d2e3f4-a5b6-4c7d-8e9f-0a1b2c3d4e5f" -->
## Hardware Reference

| Component | Detail |
|-----------|--------|
| Machine | Lenovo Yoga Pro 9 16IMH9 |
| CPU | Intel i9, 22 cores |
| GPU | NVIDIA RTX 4060 Laptop (8GB VRAM, max 3105 MHz, 5-100W) |
| Fan sysfs | `/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/fan_mode` |
| Platform sysfs | `/sys/firmware/acpi/platform_profile` |
| Fan mode values | Write 0 → auto, write 1 → max (readback values differ: 133=auto, 3/5=max) |

<!-- section_id: "d2e3f4a5-b6c7-4d8e-9f0a-1b2c3d4e5f6a" -->
## Supersedes

- Old `~/.local/bin/fan-toggle` (two-state fan toggle only)
- Old `maxmode` / `perfmode` commands (earlier iterations of this tool, removed)
- Always-on `fan-mode-max.service` at boot
