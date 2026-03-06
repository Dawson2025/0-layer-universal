---
resource_id: "9f09783e-fcb0-4934-82b9-f460abb6cac2"
resource_type: "output"
resource_name: "current_workaround"
---
# Current Workaround — GSD Keepalive Timer

<!-- section_id: "4abaa750-7b55-4d51-ac7f-e2825845cb98" -->
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
