<!-- derived_from: "70228222-a4b6-48f5-b599-ed6ab57226fe" -->
# Gemini Context

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
