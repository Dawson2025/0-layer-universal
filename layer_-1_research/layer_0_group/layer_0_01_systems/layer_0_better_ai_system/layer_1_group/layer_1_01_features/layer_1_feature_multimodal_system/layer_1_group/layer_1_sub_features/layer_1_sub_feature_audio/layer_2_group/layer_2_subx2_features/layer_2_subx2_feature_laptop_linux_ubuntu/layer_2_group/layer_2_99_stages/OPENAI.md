<!-- derived_from: "70228222-a4b6-48f5-b599-ed6ab57226fe" -->
# OpenAI Context

## Identity
Stages container for the laptop linux ubuntu platform sub-feature.
- **Parent**: `../../0AGNOSTIC.md` (layer_2_subx2_feature_laptop_linux_ubuntu)

## Stages

| Stage | Name | Purpose |
|-------|------|---------|
| 00 | Stage Registry | Stage metadata and proposals |
| 01 | Request Gathering | Platform-specific TTS requirements |
| 02 | Research | GPU TTS engines, Ubuntu integration, VoiceMode |
| 03 | Instructions | Platform constraints and guidelines |
| 04 | Design | Architecture for GPU-accelerated TTS on Ubuntu |
| 05 | Planning | Implementation task breakdown |
| 06 | Development | Install and configure Kokoro, VoiceMode |
| 07 | Testing | Verify TTS quality, latency, GPU usage |
| 08 | Criticism | Review setup and identify gaps |
| 09 | Fixing | Address issues from testing/criticism |
| 10 | Current Product | Working Kokoro TTS on Ubuntu |
| 11 | Archives | Historical records |

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
