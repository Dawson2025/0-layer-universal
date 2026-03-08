# OpenAI Context

---
resource_id: "8ae4ad0e-36b5-4ec2-919e-585a5bc5a7f1"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_2_subx2_feature_laptop_linux_ubuntu

<!-- section_id: "4553d879-3be4-4503-aec4-c55a15d09dd1" -->
## Identity

entity_id: "115127f8-4201-4892-b616-3cd706593cf6"

You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Laptop Linux Ubuntu.
- **Role**: Platform-specific TTS implementation for Ubuntu Linux on Lenovo Yoga Pro 9 with NVIDIA RTX 4060 GPU
- **Scope**: Hardware-specific TTS setup, GPU-accelerated inference (Kokoro), Ubuntu/GNOME desktop integration, PipeWire audio stack, system TTS scripts, Claude Code hooks
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_audio)
- **Children**: `layer_3_group/layer_3_subx3_features/` contains 2 sub-features (system_tts, agentic_tts)

<!-- section_id: "514fbdd2-77f1-4017-a44c-623b8380b67a" -->
## Triggers
Load this context when:
- User mentions: Ubuntu, Linux, GNOME, Unity, PipeWire, RTX 4060, GPU TTS, Lenovo Yoga, laptop audio
- Working on: Platform-specific TTS setup, GPU-accelerated TTS, desktop audio integration
- Entering: `layer_2_subx2_feature_laptop_linux_ubuntu/`
- Post-reboot daemon/keybinding/brightness failures → traverse to setup entity at `.0agnostic/.../sub_layer_0_06_local/sub_layer_0_06_group/setup/0AGNOSTIC.md`

<!-- section_id: "2840d544-7387-4639-a04a-39bd81b5554d" -->
## Pointers
<!-- section_id: "13f456ce-e490-4936-9769-3af136c97689" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_99_stages/` for stage progress

<!-- section_id: "c576dbe8-8540-43cf-a1ff-0d179e9f9ea4" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_2_group/layer_2_99_stages/` |
| System TTS | `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/` |
| Agentic TTS | `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/` |

<!-- section_id: "f2e8f492-e361-4b76-8f32-7d3642ace8b8" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

<!-- section_id: "4e9892c5-6360-46cc-b8fb-5c81b9c538c7" -->
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

<!-- section_id: "b0a99bc7-1321-4360-a927-878f57bbdbf4" -->
### GPU Capabilities for TTS
- 8GB VRAM is more than enough for Kokoro (82M params, ~200-300MB VRAM)
- Can run Kokoro + Whisper STT simultaneously on same GPU
- `kokoro-fastapi[gpu]` variant uses CUDA for near-instant generation
- Sub-0.1s TTS generation for short text with GPU acceleration

<!-- section_id: "2d5a76f9-828b-482c-97c8-7877caa0221c" -->
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
| **GSD Session Startup** | `sub_layer_0_06_group/setup/gsd_session_startup/` — dedicated entity for fixing the gsd startup issues after reboot (DISPLAY race + GDK backend mismatch on X11) |
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

<!-- section_id: "fb295b03-9c17-4c74-8390-b5204dc11f8e" -->
## Resources Available

<!-- section_id: "eccad0ef-d986-473b-8a2e-c8a5670232ad" -->
### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| GPU TTS | `.0agnostic/01_knowledge/gpu_tts/` | RTX 4060 capabilities, Kokoro GPU mode, VoiceMode MCP |

<!-- section_id: "edce7d16-2339-4f30-aed2-8b3c96a19180" -->
### Key References
- **TTS Engine (target)**: Kokoro TTS — 82M params, top of HuggingFace TTS Arena, 40+ voices, GPU-accelerated
- **TTS Engine (current)**: Piper — Amy voice, CPU-only, `~/.local/bin/piper`
- **MCP Integration**: VoiceMode (v8.3.0, 1600+ commits) — local Kokoro + Whisper, Claude Code plugin
- **System TTS script**: `~/.local/bin/speak-selection` (xclip -> Piper -> paplay)
- **Claude Code hook**: `~/.claude/hooks/tts-response.sh` (Stop hook -> Piper -> paplay)
- **Perplexity research**: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

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
