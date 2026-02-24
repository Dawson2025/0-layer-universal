# Claude Code Context

## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: System TTS.
- **Role**: System-wide text-to-speech — Orca screen reader, Piper engine, highlight-and-speak scripts
- **Scope**: Linux/Ubuntu desktop + terminal TTS integration, voice engine setup, GNOME accessibility
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_audio)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: Orca, Piper, system TTS, highlight-and-speak, screen reader, Speech Dispatcher
- Working on: System-wide TTS setup, voice engine installation, GNOME keyboard shortcuts for speech
- Entering: `layer_2_subx2_feature_system_tts/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_99_stages/` for stage progress
3. Read parent overview: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Sibling (Agentic TTS) | `../layer_2_subx2_feature_agentic_tts/` |
| Stages | `layer_2_group/layer_2_99_stages/` |
| Parent research | `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Resources Available

### Key References
- Parent architecture overview: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- Parent design doc: `../../../layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/audio_system_design.md`
- TTS research extraction: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

### Key Components
- **Orca**: GNOME screen reader, toggle with `Super+Alt+S`
- **Piper**: Neural TTS engine (offline, natural-sounding)
- **Speech Dispatcher**: Middleware routing text to TTS engines
- **Highlight-and-speak**: Custom script: `xsel | piper | aplay`, bound to GNOME shortcut

### Platform Dependencies (Local Ubuntu/GNOME)
System TTS depends on the local desktop environment. When troubleshooting keyboard shortcuts, audio output, or gsd-* daemon issues, consult:

| Resource | Location (from repo root) | Content |
|----------|--------------------------|---------|
| GNOME Architecture | `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/setup/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gnome_architecture.md` | gsd-* daemon roles, failure modes, restart procedures |
| GSD Keepalive Fix | `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/setup/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md` | Keepalive timer for dead gsd-media-keys/gsd-power |
| Local setup root | `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/` | Full local Ubuntu environment documentation |

**Key facts**:
- Desktop is Unity (`XDG_CURRENT_DESKTOP=Unity`), not GNOME Shell
- Custom keybindings use `com.canonical.unity.settings-daemon.plugins.media-keys` (NOT `org.gnome.settings-daemon.plugins.media-keys`)
- `gsd-media-keys` must be running for custom keyboard shortcuts to work
- `gsd-power` must be running for brightness buttons to work
- A systemd user timer (`gsd-keepalive.timer`) auto-restarts dead daemons every 60s

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
