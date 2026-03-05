---
resource_id: "f029cfaf-0d01-4ae3-8931-8e5c4c283760"
resource_type: "knowledge"
resource_name: "voicemode_mcp"
---
# VoiceMode MCP Server

<!-- section_id: "23265ced-2ea5-4245-9941-d0c7089913e5" -->
## Overview
VoiceMode enables natural voice conversations with Claude Code via MCP protocol. Very actively maintained: v8.3.0, 1,601 commits, 143 releases (as of 2026-02-24).

<!-- section_id: "83f3a271-ce36-4bce-9480-2a09d7fa884c" -->
## Key Features
- **Local TTS**: Kokoro (GPU-accelerated, offline)
- **Local STT**: Whisper.cpp (offline speech-to-text)
- **Cloud fallback**: OpenAI TTS/STT API (if API key set)
- **Claude Code integration**: Plugin or MCP server
- **Smart silence detection**: Stops recording when you stop speaking
- **Privacy-focused**: Can run entirely locally

<!-- section_id: "d6c38726-9935-4cd9-9752-ecf43cf1a91e" -->
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

<!-- section_id: "6f7a6f27-4b20-4018-b8bf-cb3fd1e72fd5" -->
## Configuration
File: `~/.voicemode/voicemode.env`

<!-- section_id: "0af932b8-cd29-468d-b99b-b8593f9e172e" -->
### Fully Local (Privacy-Focused)
```bash
export VOICEMODE_TTS_BASE_URLS=http://127.0.0.1:8880/v1
export VOICEMODE_STT_BASE_URLS=http://127.0.0.1:2022/v1
export VOICEMODE_VOICES=af_sky
```

<!-- section_id: "816f9751-d045-4413-813e-d14d669d106d" -->
### Key Settings
| Variable | Default | Description |
|----------|---------|-------------|
| VOICEMODE_VOICES | af_sky,nova | Comma-separated voice preferences |
| VOICEMODE_TTS_SPEED | 1.0 | Speech speed (0.25-4.0) |
| VOICEMODE_KOKORO_PORT | 8880 | Local Kokoro service port |
| VOICEMODE_VAD_AGGRESSIVENESS | 3 | Voice activity detection (0-3) |

<!-- section_id: "3facf8a7-b293-4446-849e-596f6445c917" -->
## Claude Code Permissions
Add to `~/.claude/settings.json`:
```json
{
  "permissions": {
    "allow": ["mcp__voicemode__converse", "mcp__voicemode__service"]
  }
}
```

<!-- section_id: "f496f251-5ad5-40b6-a029-48fa4a3c9922" -->
## Usage in Claude Code
```
/voicemode:converse    # Start voice conversation
/voicemode:install     # Install dependencies
```

<!-- section_id: "4bbf8c15-3b9e-4ca0-b8e9-dd3b1bad06e1" -->
## Architecture
- Kokoro runs as systemd user service on port 8880
- Whisper runs as systemd user service on port 2022
- VoiceMode auto-discovers local services on default ports
- Falls back to OpenAI cloud if local services unavailable

<!-- section_id: "cd3a3852-4847-418c-8731-d35dcd2e0f37" -->
## Sources
- https://github.com/mbailey/voicemode
- https://voice-mode.readthedocs.io
