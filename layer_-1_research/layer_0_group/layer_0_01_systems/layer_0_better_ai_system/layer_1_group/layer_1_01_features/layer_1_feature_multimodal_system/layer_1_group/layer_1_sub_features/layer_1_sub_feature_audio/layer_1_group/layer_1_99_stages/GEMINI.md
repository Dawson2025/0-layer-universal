<!-- derived_from: "f9c8ab58-4500-40ed-872a-f35cef68c09c" -->
# Gemini Context

## Identity
Stages container for the audio sub-feature.
- **Parent**: `../../0AGNOSTIC.md` (layer_1_sub_feature_audio)

## Stages

| Stage | Name | Purpose |
|-------|------|---------|
| 00 | Stage Registry | Stage metadata and proposals |
| 01 | Request Gathering | Clarify TTS/audio requirements |
| 02 | Research | Investigate TTS tools, APIs, integration patterns |
| 03 | Instructions | Define constraints and guidelines |
| 04 | Design | Architecture for audio integration |
| 05 | Planning | Break into implementation tasks |
| 06 | Development | Build TTS integration |
| 07 | Testing | Verify audio output quality and reliability |
| 08 | Criticism | Review and identify gaps |
| 09 | Fixing | Address issues from criticism |
| 10 | Current Product | Working TTS integration |
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
