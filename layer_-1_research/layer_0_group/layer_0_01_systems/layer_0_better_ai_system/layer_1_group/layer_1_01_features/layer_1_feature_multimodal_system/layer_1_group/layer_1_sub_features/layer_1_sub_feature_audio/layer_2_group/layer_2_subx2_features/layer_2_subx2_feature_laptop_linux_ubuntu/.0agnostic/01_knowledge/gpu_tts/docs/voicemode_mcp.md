---
resource_id: "f029cfaf-0d01-4ae3-8931-8e5c4c283760"
resource_type: "knowledge"
resource_name: "voicemode_mcp"
---
# VoiceMode MCP Server

## Overview
VoiceMode enables natural voice conversations with Claude Code via MCP protocol. Very actively maintained: v8.3.0, 1,601 commits, 143 releases (as of 2026-02-24).

## Key Features
- **Local TTS**: Kokoro (GPU-accelerated, offline)
- **Local STT**: Whisper.cpp (offline speech-to-text)
- **Cloud fallback**: OpenAI TTS/STT API (if API key set)
- **Claude Code integration**: Plugin or MCP server
- **Smart silence detection**: Stops recording when you stop speaking
- **Privacy-focused**: Can run entirely locally

## Installation on Ubuntu
```bash
# System deps
sudo apt install -y ffmpeg gcc libasound2-dev libasound2-plugins libportaudio2 portaudio19-dev pulseaudio pulseaudio-utils python3-dev

# Install
uvx voice-mode-install

# Add to Claude Code
claude mcp add --scope user voicemode -- uvx --refresh voice-mode

# Install local services
voicemode service install kokoro
voicemode service install whisper
voicemode service enable kokoro
voicemode service enable whisper
```

## Configuration
File: `~/.voicemode/voicemode.env`

### Fully Local (Privacy-Focused)
```bash
export VOICEMODE_TTS_BASE_URLS=http://127.0.0.1:8880/v1
export VOICEMODE_STT_BASE_URLS=http://127.0.0.1:2022/v1
export VOICEMODE_VOICES=af_sky
```

### Key Settings
| Variable | Default | Description |
|----------|---------|-------------|
| VOICEMODE_VOICES | af_sky,nova | Comma-separated voice preferences |
| VOICEMODE_TTS_SPEED | 1.0 | Speech speed (0.25-4.0) |
| VOICEMODE_KOKORO_PORT | 8880 | Local Kokoro service port |
| VOICEMODE_VAD_AGGRESSIVENESS | 3 | Voice activity detection (0-3) |

## Claude Code Permissions
Add to `~/.claude/settings.json`:
```json
{
  "permissions": {
    "allow": ["mcp__voicemode__converse", "mcp__voicemode__service"]
  }
}
```

## Usage in Claude Code
```
/voicemode:converse    # Start voice conversation
/voicemode:install     # Install dependencies
```

## Architecture
- Kokoro runs as systemd user service on port 8880
- Whisper runs as systemd user service on port 2022
- VoiceMode auto-discovers local services on default ports
- Falls back to OpenAI cloud if local services unavailable

## Sources
- https://github.com/mbailey/voicemode
- https://voice-mode.readthedocs.io
