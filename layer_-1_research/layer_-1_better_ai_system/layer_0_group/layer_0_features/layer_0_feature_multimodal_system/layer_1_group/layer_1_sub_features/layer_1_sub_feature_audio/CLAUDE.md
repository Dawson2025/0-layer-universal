# Claude Code Context

## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Audio.
- **Role**: Audio capabilities research — text-to-speech (TTS), speech synthesis, audio I/O for the AI system
- **Scope**: TTS integration (system-wide and Claude Code), speech output workflows, audio modality research
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_multimodal_system)
- **Children**: `layer_2_group/layer_2_subx2_features/` contains 2 sub-features (system_tts, agentic_tts)

## Triggers
Load this context when:
- User mentions: audio, TTS, text-to-speech, speech synthesis, voice output, Orca, Kokoro
- Working on: Audio integration, TTS pipelines, speech output for CLI or desktop
- Entering: `layer_1_sub_feature_audio/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_1_group/layer_1_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| System TTS | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_system_tts/` |
| Agentic TTS | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agentic_tts/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Resources Available

### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| TTS Research | `.0agnostic/01_knowledge/` | TTS options, tools, integration patterns |

### Key References
- Perplexity extraction (TTS research): `layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`
- System-wide TTS: Orca (GNOME), Piper, eSpeak NG
- Claude Code TTS: Kokoro hook, MCP TTS plugin, pyttsx3 DIY

### Platform Dependencies (Local Ubuntu/GNOME)
Audio and TTS features depend on the local desktop environment. When troubleshooting keyboard shortcuts, audio output, or GNOME settings daemon issues, load the local Ubuntu entity:

**Local entity root** (from repo root): `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/`

| Resource | Location (within local entity) |
|----------|-------------------------------|
| Entity context | `0AGNOSTIC.md` — start here for all local Ubuntu issues |
| GNOME Architecture | `.0agnostic/01_knowledge/ubuntu_desktop/docs/gnome_architecture.md` |
| Linux Audio Stack | `.0agnostic/01_knowledge/audio/docs/linux_audio_stack.md` |
| Systemd User Services | `.0agnostic/01_knowledge/system_services/docs/systemd_user_services.md` |
| Inotify | `.0agnostic/01_knowledge/linux_fundamentals/docs/inotify.md` |
| GSD Keepalive Fix | `sub_layer_0_06_group/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md` |
| EasyEffects Config | `sub_layer_0_06_group/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/easyeffects_audio_enhancement.md` |
| WirePlumber Fix | `sub_layer_0_06_group/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/wireplumber_crash_fix.md` |

**Key facts**:
- Desktop is **Unity** (XDG_CURRENT_DESKTOP=Unity), NOT GNOME Shell — but uses GNOME components
- **GNOME Shell 46** handles standard media keys (volume, brightness) natively; gsd-media-keys "Failed to grab accelerator" is harmless for standard keys
- `gsd-media-keys` IS needed for **custom keybindings** (Ctrl+Alt+S for speak-selection)
- `gsd-keepalive.timer` auto-restarts dead daemons but CANNOT fix stale gnome-shell grabs after sleep
- Post-sleep recovery: `gnome-shell --replace` on X11 (WARNING: kills Cursor/Electron apps)
- Audio stack: PipeWire → ALSA/SOF → hardware; EasyEffects for speaker enhancement
- TTS pipeline: `xclip` → Piper (`~/.local/bin/piper`, `en_US-amy-medium` voice) → `paplay`

**Dynamic rule**: When troubleshooting these issues, the universal dynamic rule at `.0agnostic/02_rules/dynamic/local_ubuntu_desktop_troubleshooting/` triggers automatically.

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
