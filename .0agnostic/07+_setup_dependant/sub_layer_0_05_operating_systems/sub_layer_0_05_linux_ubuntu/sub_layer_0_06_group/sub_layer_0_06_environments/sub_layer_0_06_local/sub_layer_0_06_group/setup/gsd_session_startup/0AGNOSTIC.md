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
**Scope**: Fix the DISPLAY race condition that prevents GNOME Settings Daemons (gsd-media-keys, gsd-power) from starting reliably after every reboot on Unity desktop.
**Parent**: `../0AGNOSTIC.md` (Setup Container)

## Problem Statement

Unity desktop (`XDG_CURRENT_DESKTOP=Unity`) doesn't import `DISPLAY` into the systemd user environment before GNOME session triggers gsd-media-keys and gsd-power. This causes 5 rapid "Cannot open display:" crashes in <1 second, after which systemd permanently gives up on the services.

Stock GNOME calls `systemctl --user import-environment DISPLAY` before activating gsd targets. Unity doesn't.

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
| Current workaround | `../../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md` |
| GNOME architecture knowledge | `../../../.0agnostic/01_knowledge/ubuntu_desktop/docs/gnome_architecture.md` |
| Systemd knowledge | `../../../.0agnostic/01_knowledge/system_services/docs/systemd_user_services.md` |
| Audio/TTS (depends on this) | See layer_2_subx2_feature_laptop_linux_ubuntu and layer_3_subx3_feature_system_tts in research tree |

### Stage Hierarchy
| Stage | Purpose | Key Content |
|-------|---------|-------------|
| stage_01_request_gathering | Requirements | `requirements_tree.md` — hierarchical needs tree |
| stage_02_research | Investigation | `display_race_condition.md` — root cause analysis |
| stage_03_instructions | Constraints | (empty) |
| stage_04_design | Solutions | `pre_testing/solution_overview.md` — 3 solution approaches |
| stage_05_planning | Task breakdown | (empty) |
| stage_06_development | Implementation | (empty) |
| stage_07_testing | Verification | Subdirs: test_design, test_development, test_runs, test_insights |
| stage_08_criticism | Review | (empty) |
| stage_09_fixing | Corrections | (empty) |
| stage_10_current_product | Active fix | Pointer to gsd_keepalive_fix.md (current workaround) |
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
