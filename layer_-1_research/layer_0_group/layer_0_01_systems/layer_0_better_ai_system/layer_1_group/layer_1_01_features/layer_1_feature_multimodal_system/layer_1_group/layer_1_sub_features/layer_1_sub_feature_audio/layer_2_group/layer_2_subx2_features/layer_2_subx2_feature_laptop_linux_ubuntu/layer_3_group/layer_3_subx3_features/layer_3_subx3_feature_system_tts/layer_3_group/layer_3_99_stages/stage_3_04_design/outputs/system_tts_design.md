---
resource_id: "c02f6461-fc6b-40e6-b91b-13a5fed139a5"
resource_type: "output"
resource_name: "system_tts_design"
---
# System TTS Design

**Date**: 2026-02-24 (Phase 2 update)

<!-- section_id: "37a01618-f27a-417e-a23d-e4c6a9d47e31" -->
## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      User Interface                       │
│                                                           │
│  [Ctrl+Alt+S]    [Terminal]       [Orca/Screen Reader]    │
│       │              │                    │               │
│       v              v                    v               │
│  speak-selection   speak         Orca (accessibility)     │
│       │              │                    │               │
│       v              v                    │               │
│  xclip (selection) args/stdin             │               │
│       │              │                    │               │
│       └──────┬───────┘                    │               │
│              v                            │               │
│  PID check (kill existing)                │               │
│              │                            │               │
│              v                            v               │
│     Piper (direct)          Speech Dispatcher (daemon)    │
│              │                    │               │       │
│              │              piper-generic    espeak-ng     │
│              │              (sd_generic)    (fallback)     │
│              │                    │               │       │
│              └──────┬─────────────┘               │       │
│                     v                             v       │
│              paplay (PulseAudio) ──────────> Speakers     │
└──────────────────────────────────────────────────────────┘
```

<!-- section_id: "5e5c4a66-3f83-4e17-a57e-12c754f50bb6" -->
## Two Audio Paths

<!-- section_id: "6653ee92-26e7-4b9b-960e-51d3eb05019b" -->
### Path 1: Direct Scripts (speak, speak-selection)
- User triggers via hotkey (Ctrl+Alt+S) or CLI (`speak "text"`)
- Text piped directly: `piper → paplay`
- Fastest path — no middleware overhead
- Toggle behavior via PID files

<!-- section_id: "3cfdbfc7-8559-4ef3-bfc2-b68f6d930942" -->
### Path 2: Speech Dispatcher (Orca, spd-say, apps)
- Orca and any Speech Dispatcher client send text to speechd daemon
- speechd routes to piper-generic module (sd_generic)
- sd_generic invokes: `printf '%s' '$DATA' | piper -m $VOICE --output-raw | paplay`
- eSpeak NG available as fallback: `spd-say -o espeak-ng "text"`

<!-- section_id: "58c3b7b6-d5d4-4d2c-8ae6-845f6917d478" -->
## Components

| Component | Role | Location |
|-----------|------|----------|
| speak | General TTS: args, stdin, stop | `~/.local/bin/speak` |
| speak-selection | X11 highlight-and-speak | `~/.local/bin/speak-selection` |
| Piper | Neural TTS engine | `~/.local/bin/piper` (pipx) |
| Amy voice | VITS voice model | `~/.local/share/piper-voices/en_US-amy-medium.onnx` |
| Speech Dispatcher | TTS routing daemon | System package, user config at `~/.config/speech-dispatcher/` |
| piper-generic | sd_generic module config for Piper | `~/.config/speech-dispatcher/modules/piper-generic.conf` |
| Orca | GNOME screen reader | `/usr/bin/orca` (system package) |
| paplay | PulseAudio playback | `/usr/bin/paplay` (system) |

<!-- section_id: "a235714a-36f8-4dba-9e43-67ba1f07f3fb" -->
## Coexistence Strategy

- Both paths use PulseAudio (paplay) — PulseAudio handles mixing automatically
- Direct scripts kill previous speech before starting new (PID file toggle)
- Speech Dispatcher manages its own queue for Orca/app requests
- No audio device contention since everything goes through PulseAudio

<!-- section_id: "4d8056b7-dafd-414c-8cee-74ce17d7b7d2" -->
## Stop/Toggle Behavior

| Trigger | Behavior |
|---------|----------|
| Ctrl+Alt+S (while speaking) | Kills existing speak-selection, stops speech |
| Ctrl+Alt+S (while silent) | Reads highlighted text |
| `speak -s` | Stops any speak-initiated speech |
| Caps Lock+S | Toggles Orca speech on/off |
| Super+Alt+S | Toggles Orca entirely |

<!-- section_id: "3459f9de-2052-4faa-a3a4-6fa23484d81f" -->
## Configuration Files

| File | Purpose |
|------|---------|
| `~/.config/speech-dispatcher/speechd.conf` | User-local Speech Dispatcher config |
| `~/.config/speech-dispatcher/modules/piper-generic.conf` | Piper module for sd_generic |
| `~/.local/share/orca/user-settings.conf` | Orca preferences (created on first run) |

<!-- section_id: "fdae1542-8b85-4044-996b-90af022daa51" -->
## Planned Upgrade: Piper → Kokoro

The current design uses Piper throughout. The target upgrade replaces Piper with Kokoro for higher quality and GPU-accelerated speed:

| Aspect | Current (Piper) | Target (Kokoro) |
|--------|-----------------|-----------------|
| Engine | Piper 1.4.1 (VITS, CPU) | Kokoro 82M (StyleTTS2, GPU) |
| Quality | High | Highest (#1 HF TTS Arena) |
| Latency | ~1s startup + generation | Sub-0.1s (RTX 4060) |
| Voices | 1 (Amy medium) | 40+ built-in |
| Integration | Direct CLI pipe | FastAPI server (port 8880) or CLI |
| API | None | OpenAI-compatible `/v1/audio/speech` |

**Migration path**: The `speak` and `speak-selection` scripts swap the Piper pipe for a `curl` call to Kokoro's FastAPI server. Speech Dispatcher's `piper-generic.conf` module gets replaced with a `kokoro-generic.conf` module.

<!-- section_id: "b8bb5c51-159b-4e5f-b309-43e145718f23" -->
## Future Extensions

- Multiple voice models selectable via `speak -v male "text"` or Kokoro voice parameter
- Speed/pitch control via Kokoro API parameters
- Wayland support via wl-paste (when session switches from X11)
- Rate/pitch post-processing via sox for Speech Dispatcher path
