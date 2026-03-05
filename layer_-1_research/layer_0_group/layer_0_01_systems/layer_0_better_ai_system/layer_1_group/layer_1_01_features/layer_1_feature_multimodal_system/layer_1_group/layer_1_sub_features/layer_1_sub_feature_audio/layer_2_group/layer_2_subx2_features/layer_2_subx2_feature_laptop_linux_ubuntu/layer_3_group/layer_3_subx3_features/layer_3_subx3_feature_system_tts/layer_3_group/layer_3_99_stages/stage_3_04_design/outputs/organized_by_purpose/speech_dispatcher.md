---
resource_id: "a2709b30-7a0f-42eb-bcb4-121a993c0ed5"
resource_type: "output"
resource_name: "speech_dispatcher"
---
# Design: Speech Dispatcher Integration

**Purpose**: Let any app that uses Speech Dispatcher (spd-say, Orca, etc.) use the same high-quality TTS voice.
**Priority**: Tertiary — infrastructure for app integration, not directly user-facing.

## User Flow

```bash
spd-say "Hello from any app"         # Uses Piper (default module)
spd-say -o espeak-ng "Robotic voice" # Explicit eSpeak fallback
```

## Current Implementation (Working)

```
Application (spd-say, Orca, etc.)
  → Speech Dispatcher daemon (speechd)
  → piper-generic module (sd_generic)
  → piper --model amy --output-raw | paplay
  → speakers
```

### Configuration

| File | Purpose |
|------|---------|
| `~/.config/speech-dispatcher/speechd.conf` | User Speech Dispatcher config, sets piper-generic as default |
| `~/.config/speech-dispatcher/modules/piper-generic.conf` | sd_generic module that invokes Piper |

### Available Modules

| Module | Engine | Quality |
|--------|--------|---------|
| piper-generic (default) | Piper neural TTS | High, natural |
| espeak-ng | eSpeak NG formant | Low, robotic (fallback) |

## Target Implementation (Kokoro Upgrade)

Replace `piper-generic.conf` with `kokoro-generic.conf`:

```
Application
  → speechd
  → kokoro-generic module (sd_generic)
  → curl http://localhost:8880/v1/audio/speech ... | paplay
  → speakers
```

### New Module Config (`kokoro-generic.conf`)

The sd_generic module config would call Kokoro's API instead of Piper CLI. The `GenericExecuteSynth` command changes from a Piper pipe to a curl call.

## Orca (Screen Reader) Note

Orca (v46.1) is installed but deliberately DISABLED. It's configured to use Speech Dispatcher (and therefore Piper/Kokoro), but enabling it would cause all UI elements and keystrokes to be read aloud — that's a screen reader, not selective TTS. The user's design philosophy is on-demand TTS only.

If Orca is ever needed:
- Toggle: Super+Alt+S
- It will automatically use whatever Speech Dispatcher module is default (Piper now, Kokoro after upgrade)
