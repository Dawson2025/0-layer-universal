---
resource_id: "f6a7b8c9-d0e1-2345-fabc-567890123456"
resource_type: "output"
resource_name: "current_workaround"
---
# Current Workaround — GSD Keepalive Timer

<!-- section_id: "e2f3a4b5-c6d7-8e9f-0a1b-2c3d4e5f6a7b" -->
## Pointer

The current active workaround is documented in the parent entity's current product stage:

**Canonical location**: `../../../../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md`

This is a band-aid that polls every 60s and restarts dead gsd daemons. It does NOT fix the root cause (DISPLAY race condition). See `../../../stage_02_research/outputs/display_race_condition.md` for the root cause analysis.

## Status

- **Working**: Eventually recovers gsd-media-keys (~5 min delay)
- **Broken**: gsd-power often never recovers; brightness keys stay broken
- **Known bugs**: Multi-instance spawning, silent error suppression, D-Bus name conflict delays

## Goal

Replace this workaround with a proper fix that imports DISPLAY into systemd user env before gsd services start. See `../../../stage_04_design/outputs/pre_testing/solution_overview.md` for proposed solutions.
