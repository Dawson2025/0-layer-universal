---
resource_id: "f45b3e32-4e29-4336-9f73-cb3d233191ed"
resource_type: "index
document"
resource_name: "0INDEX"
---
# 0INDEX.md - Laptop Linux Ubuntu

## Current Status
- **Phase**: Initial creation — platform entity for Ubuntu-specific TTS implementation
- **Active Stage**: 02 (Research)
- **Last Updated**: 2026-02-25

## Hardware
Lenovo Yoga Pro 9 16IMH9 | RTX 4060 Laptop GPU (8GB VRAM) | Ubuntu Linux / Unity

## TTS Engine Status
| Engine | Status | Notes |
|--------|--------|-------|
| **Kokoro (primary)** | **Working** | **0.9.4, GPU (RTX 4060), systemd service on port 8880, 0.17s/6s audio** |
| Piper (fallback) | Working | Amy voice, CPU-only, auto-activates if Kokoro down |
| VoiceMode MCP | Not installed | Manages Kokoro lifecycle, Claude Code plugin |

## Children
| Sub-Feature | Path | Purpose |
|-------------|------|---------|
| System TTS | `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/` | Highlight-and-speak, Ctrl+Alt+S, desktop TTS |
| Agentic TTS | `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/` | Claude Code Stop hook, spoken summaries |

## Stage Progress
| Stage | Status | Key Outputs |
|-------|--------|-------------|
| 00 Stage Registry | Empty | |
| 01 Request Gathering | Empty | |
| 02 Research | Has content | GPU TTS research, Kokoro findings, VoiceMode |
| 03-09 | Empty | |
| 10 Current Product | Empty | |
| 11 Archives | Empty | |
