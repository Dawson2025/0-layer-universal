# Gemini Context

## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Laptop Linux Ubuntu.
- **Role**: Platform-specific TTS implementation for Ubuntu Linux on Lenovo Yoga Pro 9 with NVIDIA RTX 4060 GPU
- **Scope**: Hardware-specific TTS setup, GPU-accelerated inference (Kokoro), Ubuntu/GNOME desktop integration, PipeWire audio stack, system TTS scripts, Claude Code hooks
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_audio)
- **Children**: `layer_3_group/layer_3_subx3_features/` contains 2 sub-features (system_tts, agentic_tts)

## Triggers
Load this context when:
- User mentions: Ubuntu, Linux, GNOME, Unity, PipeWire, RTX 4060, GPU TTS, Lenovo Yoga, laptop audio
- Working on: Platform-specific TTS setup, GPU-accelerated TTS, desktop audio integration
- Entering: `layer_2_subx2_feature_laptop_linux_ubuntu/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_2_group/layer_2_99_stages/` |
| System TTS | `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/` |
| Agentic TTS | `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Hardware Specs

| Component | Details |
|-----------|---------|
| **Laptop** | Lenovo Yoga Pro 9 16IMH9 |
| **GPU** | NVIDIA GeForce RTX 4060 Laptop GPU (AD107M) |
| **VRAM** | 8188 MiB (8 GB) |
| **GPU Driver** | 580.126.09 (NVIDIA UNIX Open Kernel Module) |
| **CUDA** | Available (libnvidia-compute-580 installed) |
| **OS** | Ubuntu Linux with Unity desktop (XDG_CURRENT_DESKTOP=Unity) |
| **Display Server** | X11 (Wayland not active) |
| **Audio Stack** | PipeWire -> ALSA/SOF -> hardware; EasyEffects for speaker enhancement |
| **nvidia-smi** | `/usr/bin/nvidia-smi` |

### GPU Capabilities for TTS
- 8GB VRAM is more than enough for Kokoro (82M params, ~200-300MB VRAM)
- Can run Kokoro + Whisper STT simultaneously on same GPU
- `kokoro-fastapi[gpu]` variant uses CUDA for near-instant generation
- Sub-0.1s TTS generation for short text with GPU acceleration

## Platform Dependencies

This entity's TTS implementations depend on the local desktop environment. The local Ubuntu entity contains foundational platform knowledge:

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

**Key platform facts**:
- Desktop is **Unity** (XDG_CURRENT_DESKTOP=Unity), NOT GNOME Shell — but uses GNOME components
- **GNOME Shell 46** handles standard media keys natively; gsd-media-keys "Failed to grab accelerator" is harmless for standard keys
- `gsd-media-keys` IS needed for **custom keybindings** (Ctrl+Alt+S for speak-selection)
- `gsd-keepalive.timer` auto-restarts dead daemons but CANNOT fix stale gnome-shell grabs after sleep
- Post-sleep recovery: `gnome-shell --replace` on X11 (WARNING: kills Cursor/Electron apps)
- Audio stack: PipeWire -> ALSA/SOF -> hardware; EasyEffects for speaker enhancement
- Current TTS pipeline: `xclip` -> Piper (`~/.local/bin/piper`, `en_US-amy-medium` voice) -> `paplay`
- Target TTS pipeline: `xclip` -> Kokoro (GPU-accelerated, `kokoro-fastapi[gpu]` on port 8880) -> `paplay`

**Dynamic rule**: Universal rule at `.0agnostic/02_rules/dynamic/local_ubuntu_desktop_troubleshooting/` triggers for desktop/audio issues.

## Resources Available

### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| GPU TTS | `.0agnostic/01_knowledge/gpu_tts/` | RTX 4060 capabilities, Kokoro GPU mode, VoiceMode MCP |

### Key References
- **TTS Engine (target)**: Kokoro TTS — 82M params, top of HuggingFace TTS Arena, 40+ voices, GPU-accelerated
- **TTS Engine (current)**: Piper — Amy voice, CPU-only, `~/.local/bin/piper`
- **MCP Integration**: VoiceMode (v8.3.0, 1600+ commits) — local Kokoro + Whisper, Claude Code plugin
- **System TTS script**: `~/.local/bin/speak-selection` (xclip -> Piper -> paplay)
- **Claude Code hook**: `~/.claude/hooks/tts-response.sh` (Stop hook -> Piper -> paplay)
- **Perplexity research**: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

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
