# Audio System Design

## High-Level Architecture

### Layer 1: TTS Engine (Shared)
Both system-wide and agentic TTS share the same engine stack:

| Component | Purpose | Install |
|-----------|---------|---------|
| **Piper** | Neural TTS engine — generates speech audio | `pip install piper-tts` or system package |
| **eSpeak NG** | Fallback lightweight engine | `apt install espeak-ng` |
| **Speech Dispatcher** | Routes text to engines, manages queue | `apt install speech-dispatcher` |
| **PulseAudio/PipeWire** | Audio output | Already installed on Ubuntu |

### Layer 2: System-Wide TTS
| Component | Purpose |
|-----------|---------|
| **Orca** | GNOME screen reader — reads focused UI, navigation, terminal |
| **Highlight-and-speak script** | Custom hotkey: `xsel` → Piper → `aplay` |
| **GNOME shortcut** | Binds script to keyboard shortcut (e.g., `Super+S`) |

### Layer 3: Agentic TTS (Claude Code)
| Component | Purpose |
|-----------|---------|
| **PostToolUse hook** | Fires after Claude Code responses |
| **Speech extractor** | Parses response for spoken summary (`<!-- speech: ... -->` or first sentence) |
| **TTS caller** | Sends extracted text to Piper/eSpeak |

## Implementation Phases

### Phase 1: Engine Setup
1. Install Piper + voice model
2. Verify `echo "test" | piper --model en_US-lessac-medium --output-raw | aplay -r 22050 -f S16_LE`
3. Install eSpeak NG as fallback

### Phase 2: System-Wide TTS
1. Enable Orca (`Super+Alt+S`)
2. Configure Speech Dispatcher to use Piper as default voice
3. Create highlight-and-speak script
4. Bind to GNOME keyboard shortcut
5. Test across: browser, terminal, GUI apps

### Phase 3: Agentic TTS
1. Try community Claude Code TTS hooks (Kokoro-based or MCP)
2. If needed, build custom PostToolUse hook with speech extraction
3. Test with various Claude Code outputs (code, text, diagrams)

## Coexistence Strategy

- Orca uses Speech Dispatcher's queue — messages are ordered
- Claude Code hook calls Piper directly (bypasses Speech Dispatcher) to avoid queue conflicts
- If both speak simultaneously, agentic TTS takes priority (Orca can be paused)
- Speech interruption: pressing hotkey again or Orca's stop key cancels current speech

## Children — Detailed Design

This document covers the **overall audio system design** at the parent level. Each child has its own design outputs:

### System TTS Design (Summary)
- Architecture: User hotkey/CLI → speak scripts → PID check → Piper → aplay → PulseAudio
- Two scripts: `speak` (general TTS) and `speak-selection` (X11 highlight-and-speak)
- Toggle behavior via PID files, voice model at `~/.local/share/piper-voices/`
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_system_tts/layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/system_tts_design.md`

### Agentic TTS Design (Summary)
- Architecture: Claude Stop event → Hook 1 (sound) → Hook 2 (tts-response.sh) → jq extract → sed strip → Piper background
- Text pipeline: strip code blocks, markdown, URLs, paths, tables → truncate to 600 chars → Piper → aplay
- Future: split-output pattern where Claude provides `spoken_summary` field
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agentic_tts/layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/agentic_tts_design.md`
