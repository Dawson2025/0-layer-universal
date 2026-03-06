---
resource_id: "afcfca90-c5d5-41db-8fff-9d0ae77009e9"
resource_type: "output"
resource_name: "setup_requirements_tree"
---
# Setup — Tree of Needs

<!-- section_id: "e4227888-7f1a-45fa-a432-fb9a228b1f9f" -->
## Overview

This is the root requirements tree for the local Ubuntu environment setup. Each need (N) represents a category of system health. Child entities may have their own detailed requirements trees that trace back to needs defined here.

<!-- section_id: "356f59d6-835e-42fd-9347-517969e4fba8" -->
## Tree

```
Local Ubuntu environment must work reliably without manual intervention
├── N1: Desktop Services
│   ├── N1.1: gsd-media-keys must run for custom keybindings
│   ├── N1.2: gsd-power must run for brightness keys and power management
│   ├── N1.3: No ~5 min dead zone after boot
│   ├── N1.4: No multi-instance spawning
│   └── **Detailed breakdown** → gsd_session_startup/stages/stage_01_request_gathering/outputs/requirements_tree.md
│
├── N2: System Resource Limits
│   ├── N2.1: inotify watch limits sufficient for all file watchers
│   ├── N2.2: File descriptor limits adequate
│   └── **Status**: Resolved — see inotify_fix.md
│
├── N3: Audio Stack
│   ├── N3.1: PipeWire running and routing audio correctly
│   ├── N3.2: EasyEffects processing active for speaker enhancement
│   ├── N3.3: WirePlumber stable (no crashes)
│   └── **Status**: Resolved (workarounds in place)
│
├── N4: Display Server Availability
│   ├── N4.1: DISPLAY env var available in systemd user environment
│   ├── N4.2: XAUTHORITY env var available in systemd user environment
│   ├── N4.3: Must be imported BEFORE gsd services trigger
│   └── **Detailed breakdown** → gsd_session_startup/stages/stage_02_research/outputs/display_race_condition.md
│
└── NOT in scope (handled elsewhere)
    └── Volume keys — handled by custom volume-control.sh, not dependent on gsd
```

<!-- section_id: "989ea17f-431f-49d9-aa01-912e9cba0f04" -->
## Cross-References

### Child Entity Requirements Trees

| Child Entity | Their Tree | Satisfies Parent Needs |
|-------------|-----------|----------------------|
| gsd_session_startup | `gsd_session_startup/stages/stage_01_request_gathering/outputs/requirements_tree.md` | N1 (Desktop Services), N4 (Display Server) |

### Triggers

| When This Happens | Action |
|-------------------|--------|
| N1 needs are unmet (gsd daemons failing) | Traverse to `gsd_session_startup/` and work through its stages |
| N2 needs are unmet (inotify/resource limits) | Check `../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md` |
| N3 needs are unmet (audio issues) | Check audio-related fixes in current product stage |
| N4 needs are unmet (DISPLAY not available) | Traverse to `gsd_session_startup/` — root cause is documented there |

<!-- section_id: "c6f01be6-93fb-4886-9f68-814d1fabab61" -->
## Status

| Need | Status | Last Checked |
|------|--------|-------------|
| N1: Desktop Services | **Active** — gsd_session_startup entity created, solutions designed, testing not started | 2026-03-06 |
| N2: System Resource Limits | **Resolved** | 2026-01-25 |
| N3: Audio Stack | **Resolved** (workarounds) | 2026-03-06 |
| N4: Display Server | **Active** — root cause identified, fix pending | 2026-03-06 |
