# System TTS Instructions / Constraints

**Date**: 2026-02-23

## Technical Constraints

1. **Audio format**: Piper outputs raw PCM S16_LE at 22050 Hz mono — aplay must match these params exactly
2. **PID file isolation**: System TTS uses `/tmp/speak-selection.pid` and `/tmp/speak.pid`, separate from agentic TTS (`/tmp/claude-tts.pid`)
3. **No concurrent speech**: New speech kills any existing speech (toggle/replace pattern)
4. **Voice model path**: All models stored at `~/.local/share/piper-voices/`
5. **Script location**: All scripts at `~/.local/bin/` (in PATH)

## Dependencies

- `piper` (via pipx, version 1.4.1+)
- `pathvalidate` (injected into piper venv — known missing dependency)
- `xclip` (for X selection/clipboard access)
- `aplay` (ALSA utils, for audio playback)
- `jq` (not needed for system TTS, but used by agentic TTS)

## Installation Order

1. `pipx install piper-tts`
2. `pipx inject piper-tts pathvalidate`
3. Download voice model to `~/.local/share/piper-voices/`
4. Create scripts in `~/.local/bin/`
5. Configure keyboard shortcut in GNOME Settings

## Do NOT

- Do not use `pactl` or `paplay` for Piper output (raw PCM needs aplay)
- Do not run Piper with `--cuda` unless NVIDIA GPU is configured
- Do not set sample rate other than what the model specifies (22050 Hz for medium models)
