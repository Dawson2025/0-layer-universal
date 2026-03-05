---
resource_id: "a2709b30-7a0f-42eb-bcb4-121a993c0ed5"
resource_type: "output"
resource_name: "speech_dispatcher"
---
# Design: Speech Dispatcher Integration

**Purpose**: Let any app that uses Speech Dispatcher (spd-say, Orca, etc.) use the same high-quality TTS voice.
**Priority**: Tertiary — infrastructure for app integration, not directly user-facing.

<!-- section_id: "1f513408-bc0e-4012-8b9e-4af58518742d" -->
## User Flow

```bash
spd-say "Hello from any app"         # Uses Piper (default module)
spd-say -o espeak-ng "Robotic voice" # Explicit eSpeak fallback
```

<!-- section_id: "2bb299be-9347-4e51-b547-eb9ca83e11c3" -->
## Current Implementation (Working)

```
Application (spd-say, Orca, etc.)
  → Speech Dispatcher daemon (speechd)
  → piper-generic module (sd_generic)
  → piper --model amy --output-raw | paplay
  → speakers
```

<!-- section_id: "e68de9af-e8d9-46d9-9845-c82f4d85ac9b" -->
### Configuration

| File | Purpose |
|------|---------|
| `~/.config/speech-dispatcher/speechd.conf` | User Speech Dispatcher config, sets piper-generic as default |
| `~/.config/speech-dispatcher/modules/piper-generic.conf` | sd_generic module that invokes Piper |

<!-- section_id: "a96f17b4-c8bf-4e35-8a84-f416f5ebdea8" -->
### Available Modules

| Module | Engine | Quality |
|--------|--------|---------|
| piper-generic (default) | Piper neural TTS | High, natural |
| espeak-ng | eSpeak NG formant | Low, robotic (fallback) |

<!-- section_id: "8942d58b-4f08-421f-82a8-3db063f4db94" -->
## Target Implementation (Kokoro Upgrade)

Replace `piper-generic.conf` with `kokoro-generic.conf`:

```
Application
  → speechd
  → kokoro-generic module (sd_generic)
  → curl http://localhost:8880/v1/audio/speech ... | paplay
  → speakers
```

<!-- section_id: "349608e4-4b7b-42e5-be57-8f4ffc53771f" -->
### New Module Config (`kokoro-generic.conf`)

The sd_generic module config would call Kokoro's API instead of Piper CLI. The `GenericExecuteSynth` command changes from a Piper pipe to a curl call.

<!-- section_id: "982c2b65-2aa2-4eac-9766-4a99f9e84dc0" -->
## Orca (Screen Reader) Note

Orca (v46.1) is installed but deliberately DISABLED. It's configured to use Speech Dispatcher (and therefore Piper/Kokoro), but enabling it would cause all UI elements and keystrokes to be read aloud — that's a screen reader, not selective TTS. The user's design philosophy is on-demand TTS only.

If Orca is ever needed:
- Toggle: Super+Alt+S
- It will automatically use whatever Speech Dispatcher module is default (Piper now, Kokoro after upgrade)
