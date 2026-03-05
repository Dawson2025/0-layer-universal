---
resource_id: "f44b08ed-b786-4db7-9aab-21eb5f5e6a26"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Entity**: Local Ubuntu Environment
**Sub-Layer**: 0.06
**Type**: Increased Specificity (narrows from Environments → Local machine setup)
**Scope**: Comprehensive knowledge base and operational hub for this specific Ubuntu machine — everything needed to understand, configure, troubleshoot, optimize, and maintain the system. Includes: GNOME/Unity desktop, system services, audio stack, TTS, hardware-specific setup, daemon persistence, performance tuning, and all related troubleshooting procedures.

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

# ── Current Status ──

## Current Status

**State**: Entity restructured to canonical format
**Scope**: Local Ubuntu desktop setup, system services, GNOME/Unity desktop, audio, TTS
**Content**: 4 knowledge topics (linux_fundamentals, ubuntu_desktop, system_services, audio), setup stages with real output content, 1 child entity (coding_apps)
**Readiness**: Structure complete, knowledge migrated from deprecated sub-layers

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Triggers

| Situation | Action |
|-----------|--------|
| Ubuntu desktop issues | Read `.0agnostic/01_knowledge/ubuntu_desktop/` |
| Volume/brightness/keybinding issues | Read `.0agnostic/01_knowledge/ubuntu_desktop/docs/gnome_architecture.md` + `system_services/docs/systemd_user_services.md` |
| Audio stack problems | Read `.0agnostic/01_knowledge/audio/docs/linux_audio_stack.md` |
| Inotify exhaustion | Read `.0agnostic/01_knowledge/linux_fundamentals/docs/inotify.md` |
| Post-sleep daemon failures | Check stage outputs: `sub_layer_0_06_group/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md` |
| Coding app issues | Navigate to `sub_layer_0_07_group/sub_layer_0_07_coding_apps/` |

## Navigation

| Path | Purpose |
|------|---------|
| `.0agnostic/01_knowledge/` | 4 knowledge topics (linux_fundamentals, ubuntu_desktop, system_services, audio) |
| `.0agnostic/02_rules/` | Entity-level rules (static + dynamic) |
| `.0agnostic/03_protocols/` | Protocols |
| `sub_layer_0_06_group/sub_layer_0_06_99_stages/` | Stages 01-10: request gathering, research, instructions, planning, design, development, testing, criticism, fixing, current product, archives |
| `sub_layer_0_07_group/sub_layer_0_07_coding_apps/` | Child: Coding Apps entity |

## Resources Available

### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| Linux Fundamentals | `.0agnostic/01_knowledge/linux_fundamentals/` | Inotify, kernel subsystems |
| Ubuntu Desktop | `.0agnostic/01_knowledge/ubuntu_desktop/` | GNOME architecture, Shell behavior, GSD daemons |
| System Services | `.0agnostic/01_knowledge/system_services/` | Systemd user services, service management |
| Audio | `.0agnostic/01_knowledge/audio/` | PipeWire, ALSA, SOF, EasyEffects |
