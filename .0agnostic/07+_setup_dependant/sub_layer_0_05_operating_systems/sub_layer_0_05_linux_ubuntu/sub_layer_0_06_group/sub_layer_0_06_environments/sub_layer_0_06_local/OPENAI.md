# OpenAI Context

<!-- section_id: "ebca792c-90d6-4817-99a9-f4fd30681811" -->
## Identity

**Entity**: Local Ubuntu Environment
**Sub-Layer**: 0.06
**Type**: Increased Specificity (narrows from Environments → Local machine setup)
**Scope**: Comprehensive knowledge base and operational hub for this specific Ubuntu machine — everything needed to understand, configure, troubleshoot, optimize, and maintain the system. Includes: GNOME/Unity desktop, system services, audio stack, TTS, hardware-specific setup, daemon persistence, performance tuning, and all related troubleshooting procedures.

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → **Local (06)**

<!-- section_id: "ef660a6a-3dbf-494d-a28e-de3c63cb7020" -->
## Key Behaviors

<!-- section_id: "d0ba8d63-a227-43d9-9ff5-82039bb9b7ef" -->
### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary:
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

<!-- section_id: "8a9c09fa-2eb2-4308-8caf-69ca7f8d990b" -->
### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/01_knowledge/` for topic-specific knowledge
3. Check `sub_layer_0_06_group/sub_layer_0_06_99_stages/` for stage progress
4. Read episodic memory if resuming work

<!-- section_id: "c82a022a-cff9-48aa-beaa-dce0d347a9b4" -->
### Key Facts
- **Desktop**: Unity (XDG_CURRENT_DESKTOP=Unity), NOT GNOME Shell — but uses GNOME components underneath
- **GNOME Shell 46** on X11: Handles standard media keys (volume, brightness) NATIVELY via mutter compositor
- **gsd-media-keys**: Still needed for CUSTOM keybindings (e.g., Ctrl+Alt+S for speak-selection)
- **GSD startup fix**: Dedicated setup entity at `sub_layer_0_06_group/setup/gsd_session_startup/` tracks the DISPLAY race and X11/Wayland backend mismatch fix
- **gsd-keepalive.timer**: Auto-restarts dead gsd-media-keys/gsd-power but CANNOT fix stale gnome-shell grabs
- **Post-sleep recovery**: gnome-shell's grab table can become stale after suspend/resume; `gnome-shell --replace` on X11 fixes this (WARNING: kills Cursor/Electron apps)
- **TTS stack**: Piper (neural TTS) + Speech Dispatcher + espeak-ng (fallback)
- **Audio**: PipeWire → ALSA/SOF → hardware; EasyEffects for speaker enhancement

<!-- section_id: "b994ed58-44d4-4d71-8895-cbdc61a39515" -->
## Delegation Contract

**Children** (level 07): Coding Apps (sub_layer_0_07_coding_apps) — Cursor IDE and future coding tools
**Parent** (level 06): Environments (sub_layer_0_06_environments)


<!-- section_id: "3c61ace6-4644-45ed-98e7-8dca02a341fa" -->
## Current Status

**State**: Entity restructured to canonical format
**Scope**: Local Ubuntu desktop setup, system services, GNOME/Unity desktop, audio, TTS
**Content**: 4 knowledge topics (linux_fundamentals, ubuntu_desktop, system_services, audio), setup stages with real output content, 1 child entity (coding_apps)
**Readiness**: Structure complete, knowledge migrated from deprecated sub-layers

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
