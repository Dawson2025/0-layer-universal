# Gemini Context

## Identity

**Entity**: Local Ubuntu Environment
**Sub-Layer**: 0.06
**Type**: Increased Specificity (narrows from Environments → Local machine setup)
**Scope**: Local Ubuntu desktop environment — GNOME/Unity desktop, system services, audio stack, TTS

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → **Local (06)**

## Key Behaviors

### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary:
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/01_knowledge/` for topic-specific knowledge
3. Check `sub_layer_0_06_group/sub_layer_0_06_99_stages/` for stage progress
4. Read episodic memory if resuming work

### Key Facts
- **Desktop**: Unity (XDG_CURRENT_DESKTOP=Unity), NOT GNOME Shell — but uses GNOME components underneath
- **GNOME Shell 46** on X11: Handles standard media keys (volume, brightness) NATIVELY via mutter compositor
- **gsd-media-keys**: Still needed for CUSTOM keybindings (e.g., Ctrl+Alt+S for speak-selection)
- **gsd-keepalive.timer**: Auto-restarts dead gsd-media-keys/gsd-power but CANNOT fix stale gnome-shell grabs
- **Post-sleep recovery**: gnome-shell's grab table can become stale after suspend/resume; `gnome-shell --replace` on X11 fixes this (WARNING: kills Cursor/Electron apps)
- **TTS stack**: Piper (neural TTS) + Speech Dispatcher + espeak-ng (fallback)
- **Audio**: PipeWire → ALSA/SOF → hardware; EasyEffects for speaker enhancement

## Delegation Contract

**Children** (level 07): Coding Apps (sub_layer_0_07_coding_apps) — Cursor IDE and future coding tools
**Parent** (level 06): Environments (sub_layer_0_06_environments)


## Current Status

**State**: Entity restructured to canonical format
**Scope**: Local Ubuntu desktop setup, system services, GNOME/Unity desktop, audio, TTS
**Content**: 4 knowledge topics (linux_fundamentals, ubuntu_desktop, system_services, audio), setup stages with real output content, 1 child entity (coding_apps)
**Readiness**: Structure complete, knowledge migrated from deprecated sub-layers

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
