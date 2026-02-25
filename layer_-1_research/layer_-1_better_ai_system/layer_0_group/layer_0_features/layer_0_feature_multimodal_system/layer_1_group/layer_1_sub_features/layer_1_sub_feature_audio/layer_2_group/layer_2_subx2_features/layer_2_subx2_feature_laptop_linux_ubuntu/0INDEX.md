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
| Piper (current) | Working | Amy voice, CPU-only, `~/.local/bin/piper` |
| Kokoro (target) | Not installed | GPU-accelerated, superior quality, 40+ voices |
| VoiceMode MCP | Not installed | Manages Kokoro as systemd service, Claude Code plugin |

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
