# Claude Code Context

## Identity
You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: Agentic TTS.
- **Role**: Claude Code agentic text-to-speech — hooks, MCP plugins, split-output patterns
- **Scope**: AI-driven speech for CLI tools, PostToolUse hooks, spoken summary extraction
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_laptop_linux_ubuntu)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: Claude Code TTS, agentic TTS, speech hooks, Kokoro hook, MCP TTS, spoken summary
- Working on: Claude Code speech integration, hook-based TTS, split visual/spoken output
- Entering: `layer_3_subx3_feature_agentic_tts/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_99_stages/` for stage progress
3. Read parent for platform context: `../../../0AGNOSTIC.md`

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Sibling (System TTS) | `../layer_3_subx3_feature_system_tts/` |
| Stages | `layer_3_group/layer_3_99_stages/` |
| Platform parent | `../../../0AGNOSTIC.md` (has hardware specs, platform deps) |
| Audio research | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Resources Available

### Key References
- Audio architecture: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- Audio design: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/audio_system_design.md`
- TTS research: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

### Key Components
- **VoiceMode** (target): MCP server managing local Kokoro + Whisper, Claude Code plugin — see parent knowledge at `../../../.0agnostic/01_knowledge/gpu_tts/`
- **Kokoro hook** (sourcehut): Claude Code hook using local Kokoro TTS model
- **MCP TTS plugin** (GitHub): Exposes TTS as MCP tool for Claude Code
- **PostToolUse hook**: Claude Code event that fires after responses — attach TTS here
- **Split-output pattern**: `spoken_summary` (short, conversational) vs `visual_output` (full text, code, diagrams)
- **pyttsx3**: Python TTS wrapper for offline eSpeak/Festival integration

### Community Projects
- [claude-code-tts (sourcehut)](https://git.sr.ht/~cg/claude-code-tts) — Hook-based TTS
- [claude-code-tts (GitHub)](https://github.com/ybouhjira/claude-code-tts) — MCP plugin
- [Local Voice Pipeline for Claude Code](https://crunchtools.com/local-voice-pipeline-claude-code-rhel10-intel-gpu/) — Full setup guide

### Platform Dependencies
Platform-specific details (hardware specs, Ubuntu/GNOME configuration, audio stack, gsd-* daemons) are documented in the parent entity: `../../../0AGNOSTIC.md`

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
