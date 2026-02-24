# Local Ubuntu Desktop Troubleshooting Rule

**Type**: Dynamic (loaded when triggered)
**Importance**: 1 (high — must be loaded when working on local Ubuntu desktop issues)
**Scope**: All agents working on the local machine

## Rule

When troubleshooting Ubuntu desktop, GNOME, system services, audio, or keybinding issues on the local machine, the agent MUST:

1. **Load** the local Ubuntu environment context at `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/0AGNOSTIC.md`
2. **Read** relevant knowledge topics in `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/.0agnostic/01_knowledge/`
3. **Check** stage outputs for existing fixes at `.../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/`
4. **Follow** established recovery protocols before attempting novel fixes

## Trigger Conditions

This rule activates when ANY of these conditions are met:

- User reports volume/brightness buttons not working
- User reports custom keyboard shortcuts not responding
- gsd-media-keys or gsd-power daemon failures
- GNOME Shell post-sleep recovery needed
- Audio stack issues (PipeWire, ALSA, EasyEffects)
- Systemd user service failures
- Inotify exhaustion symptoms
- Portal service failures
- Any local Ubuntu desktop/GNOME troubleshooting

## Key Knowledge Paths (from repo root)

| Topic | Path |
|-------|------|
| GNOME Architecture | `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/.0agnostic/01_knowledge/ubuntu_desktop/docs/gnome_architecture.md` |
| Systemd User Services | `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/.0agnostic/01_knowledge/system_services/docs/systemd_user_services.md` |
| Linux Audio Stack | `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/.0agnostic/01_knowledge/audio/docs/linux_audio_stack.md` |
| Inotify | `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/.0agnostic/01_knowledge/linux_fundamentals/docs/inotify.md` |
| GSD Keepalive Fix | `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/sub_layer_0_06_group/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md` |

**Note**: `...` abbreviates `sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments`

## Critical Facts

- Desktop is **Unity** (XDG_CURRENT_DESKTOP=Unity), NOT GNOME Shell — but uses GNOME components
- **GNOME Shell 46** handles standard media keys natively; gsd-media-keys "Failed to grab accelerator" warnings for volume/brightness are HARMLESS
- gsd-media-keys IS needed for **custom keybindings** (e.g., Ctrl+Alt+S for speak-selection)
- **Post-sleep stale grabs**: `gnome-shell --replace` on X11 fixes stale grab table (WARNING: kills Cursor/Electron apps)
- **gsd-keepalive.timer** restarts dead daemons but CANNOT fix stale gnome-shell grabs
