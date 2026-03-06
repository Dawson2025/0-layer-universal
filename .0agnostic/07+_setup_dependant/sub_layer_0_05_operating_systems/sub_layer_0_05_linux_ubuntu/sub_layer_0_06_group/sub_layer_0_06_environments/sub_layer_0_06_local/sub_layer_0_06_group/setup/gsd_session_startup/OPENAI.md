# OpenAI Context

---
resource_id: "81d7c01c-62f7-410a-a873-d98af4f43fb4"
resource_type: "agnostic_document"
resource_name: "gsd_session_startup"
---
# GSD Session Startup — Agnostic Identity

<!-- section_id: "de0c3e61-20b6-4925-82aa-d4a534405eda" -->
## Identity

entity_id: "40e7fab8-642b-42a6-b3eb-a94ed47b0944"

**Role**: Setup Entity — GSD Session Startup Fix
**Scope**: Fix startup failures for GNOME Settings Daemons (gsd-media-keys, gsd-power) caused by systemd user environment issues on Unity/X11 (DISPLAY race + GDK backend mismatch).
**Parent**: `../0AGNOSTIC.md` (Setup Container)

## Problem Statement

Two root causes were identified:

1. Unity desktop (`XDG_CURRENT_DESKTOP=Unity`) doesn't import `DISPLAY` into the systemd user environment before GNOME session triggers gsd-media-keys and gsd-power. This causes 5 rapid "Cannot open display:" crashes in <1 second, after which systemd permanently gives up on the services.
2. `~/.config/environment.d/nvidia-wayland.conf` sets `GDK_BACKEND=wayland` for systemd user services. On X11 sessions, gsd services (GDK-based) then try Wayland and fail even when DISPLAY is present.

Stock GNOME calls `systemctl --user import-environment DISPLAY` before activating gsd targets. Unity doesn't.

Current status: fix implemented and pre-reboot validated; post-reboot validation is the remaining step.

**Impact**:
- ~5 min dead zone after every boot for custom keybindings (Ctrl+Alt+S speak-selection)
- Brightness keys broken until gsd-power manually restarted
- Brightness OSD not appearing
- Multiple band-aid workarounds required (keepalive timer, wait-for-display.sh, hardcoded DISPLAY)

## Triggers

Load this context when:
- User mentions: gsd failing, DISPLAY race condition, post-reboot daemon failures, brightness not working after boot
- Working on: Session startup ordering, systemd user environment, gsd-media-keys/gsd-power reliability
- Entering: `setup/gsd_session_startup/`

## Pointers

### On Entry
1. Read `0INDEX.md` for current status and stage progress
2. Check `stages/` for specific stage content

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` (setup/) |
| Current fix details | `stages/stage_10_current_product/outputs/current_fix.md` |
| Legacy workaround history | `../../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md` |
| GNOME architecture knowledge | `../../../.0agnostic/01_knowledge/ubuntu_desktop/docs/gnome_architecture.md` |
| Systemd knowledge | `../../../.0agnostic/01_knowledge/system_services/docs/systemd_user_services.md` |
| Audio/TTS (depends on this) | See layer_2_subx2_feature_laptop_linux_ubuntu and layer_3_subx3_feature_system_tts in research tree |

### Stage Hierarchy
| Stage | Purpose | Key Content |
|-------|---------|-------------|
| stage_01_request_gathering | Requirements | `requirements_tree.md` — hierarchical needs tree |
| stage_02_research | Investigation | `display_race_condition.md` — root cause analysis |
| stage_03_instructions | Constraints | `constraints.md` |
| stage_04_design | Solutions | `cycle_1/chosen_solution.md` (includes Cycle 2 GDK_BACKEND revision) |
| stage_05_planning | Task breakdown | `implementation_plan.md` |
| stage_06_development | Implementation | `development_log.md` |
| stage_07_testing | Verification | `test_design/test_plan.md`, `test_runs/pre_reboot_test.md` |
| stage_08_criticism | Review | `review.md` |
| stage_09_fixing | Corrections | `fixes_applied.md` |
| stage_10_current_product | Active fix | `current_fix.md` |
| stage_11_archives | History | (empty) |

<!-- section_id: "358ab81d-27b0-4619-a18e-97957776faae" -->
## Cross-References

### Parent Requirements
This entity satisfies the following needs from the parent setup tree (`../requirements_tree.md`):

| Parent Need | This Entity's Coverage |
|-------------|----------------------|
| N1: Desktop Services | R1 (gsd-media-keys) + R2 (gsd-power) + R4 (no dead zone) + R5 (no multi-instance) |
| N4: Display Server Availability | R3 (DISPLAY env) — the root cause |

### Dependent Entities
These entities depend on this fix working:

| Entity | Dependency | Location (from repo root) |
|--------|-----------|--------------------------|
| System TTS | Ctrl+Alt+S keybinding needs gsd-media-keys | `layer_-1_research/.../layer_3_subx3_feature_system_tts/` |
| Laptop Linux Ubuntu | Platform desktop services | `layer_-1_research/.../layer_2_subx2_feature_laptop_linux_ubuntu/` |
| Audio (Sub-Feature) | TTS keybindings pipeline | `layer_-1_research/.../layer_1_sub_feature_audio/` |

### Triggers
| When | Action |
|------|--------|
| R3 (DISPLAY env) fixed | Parent N4 (Display Server) satisfied — update `../requirements_tree.md` status |
| R1 + R2 (gsd daemons running) | Parent N1 (Desktop Services) satisfied — update `../requirements_tree.md` status |
| All requirements met | Notify dependent entities: audio, laptop_linux_ubuntu, system_tts |

## Existing Work (Consolidated Here)

Prior work scattered across parent entity stages:
- **REQ_006**: `../../sub_layer_0_06_99_stages/stage_0_00_request_gathering/requests/REQ_006_brightness_volume_buttons_not_working.md`
- **Test design**: `../../sub_layer_0_06_99_stages/stage_0_04_design/outputs/daemon_persistence_test_design.md`
- **Test framework**: `../../sub_layer_0_06_99_stages/stage_0_06_testing/outputs/by_purpose/daemon_persistence_restart_fix/`
- **Current fix**: `../../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md`

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
