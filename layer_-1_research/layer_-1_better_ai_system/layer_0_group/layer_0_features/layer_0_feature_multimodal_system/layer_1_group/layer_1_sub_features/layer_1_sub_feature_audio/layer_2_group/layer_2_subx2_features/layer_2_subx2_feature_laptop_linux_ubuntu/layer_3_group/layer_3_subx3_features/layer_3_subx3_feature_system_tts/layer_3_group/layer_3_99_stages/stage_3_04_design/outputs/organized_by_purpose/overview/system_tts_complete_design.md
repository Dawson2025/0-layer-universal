# System TTS — Complete Design Overview

**Date**: 2026-02-24
**Platform**: Lenovo Yoga Pro 9, RTX 4060 (8GB VRAM), Ubuntu Linux, Unity Desktop, X11

## Design Philosophy

**Selective, on-demand TTS** — the user chooses exactly what gets spoken. No screen reader behavior. No automatic reading of UI elements, keystrokes, or focus changes. Every speech event is explicitly user-initiated.

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        USER INTERACTIONS                             │
│                                                                      │
│   Ctrl+Alt+S              speak "text"           spd-say "text"      │
│   (highlight-and-speak)   (CLI command)          (any app)           │
│        │                       │                      │              │
│        v                       v                      v              │
│  speak-selection            speak              Speech Dispatcher      │
│  (hotkey script)         (CLI script)           (speechd daemon)     │
│        │                       │                      │              │
│        v                       v                      v              │
│   xclip (get text)     args or stdin          kokoro-generic module  │
│        │                       │                      │              │
│        └───────────────────────┼──────────────────────┘              │
│                                │                                     │
│                                v                                     │
│              ┌─────────────────────────────────┐                    │
│              │  TTS ENGINE (one of):            │                    │
│              │                                  │                    │
│              │  PRIMARY: Kokoro FastAPI (GPU)   │                    │
│              │  localhost:8880                   │                    │
│              │  RTX 4060 CUDA, sub-0.1s         │                    │
│              │  40+ voices, 82M params           │                    │
│              │  OpenAI-compatible API            │                    │
│              │                                  │                    │
│              │  FALLBACK: Piper (CPU)           │                    │
│              │  ~/.local/bin/piper               │                    │
│              │  Amy voice, ~1s latency           │                    │
│              └──────────┬──────────────────────┘                    │
│                         │                                            │
│                         v                                            │
│                  paplay (PulseAudio)                                 │
│                         │                                            │
│                         v                                            │
│                  PipeWire → ALSA → Speakers                         │
└─────────────────────────────────────────────────────────────────────┘
```

## Three Use Cases

### 1. Highlight-and-Speak (Primary)

The main use case. Highlight text anywhere, press Ctrl+Alt+S.

| Aspect | Detail |
|--------|--------|
| Trigger | Ctrl+Alt+S (GNOME custom keybinding via gsd-media-keys) |
| Script | `~/.local/bin/speak-selection` |
| Input | X11 primary selection (xclip), clipboard fallback |
| Toggle | Press again while speaking to stop |
| Design doc | `highlight_and_speak.md` |

### 2. CLI Speak (Secondary)

Terminal convenience for scripting and quick speech.

| Aspect | Detail |
|--------|--------|
| Trigger | `speak "text"` or `echo "text" \| speak` or `speak -s` |
| Script | `~/.local/bin/speak` |
| Input | Command args or stdin |
| Stop | `speak -s` kills current speech |
| Design doc | `cli_speak_command.md` |

### 3. Speech Dispatcher (Tertiary)

Infrastructure for any app that uses spd-say or libspeechd.

| Aspect | Detail |
|--------|--------|
| Trigger | `spd-say "text"` or any Speech Dispatcher client |
| Config | `~/.config/speech-dispatcher/speechd.conf` + modules/ |
| Modules | kokoro-generic (default), espeak-ng (fallback) |
| Orca | Installed but disabled (screen reader, not selective TTS) |
| Design doc | `speech_dispatcher.md` |

## Current State vs Target

| Component | Current (Working) | Target (Kokoro Upgrade) |
|-----------|-------------------|-------------------------|
| TTS Engine | Piper 1.4.1 (CPU) | Kokoro 82M (GPU via FastAPI) |
| Voice | Amy (1 voice, US female) | 40+ voices (af_heart default) |
| Latency | ~1s per invocation | Sub-0.1s (warm server on RTX 4060) |
| Quality | High (VITS neural) | Highest (#1 HF TTS Arena) |
| Architecture | Process-per-invocation | Persistent FastAPI server (systemd) |
| Sample Rate | 22050 Hz | 24000 Hz |
| GPU Usage | None | ~200-300MB VRAM |
| API | None | OpenAI-compatible `/v1/audio/speech` |
| Fallback | eSpeak NG (robotic) | Piper (still good quality) |

## Key Dependencies

| Dependency | Role | Required By |
|------------|------|-------------|
| gsd-media-keys | Dispatches Ctrl+Alt+S keybinding | highlight-and-speak |
| gsd-keepalive.timer | Auto-restarts dead gsd daemons | highlight-and-speak |
| xclip | Gets X11 text selection | highlight-and-speak |
| PipeWire | Audio routing | all three use cases |
| paplay | Audio playback | all three use cases |
| X11 session | xclip works on X11 only | highlight-and-speak |

## Migration Plan Summary

1. Install Kokoro: `pip install kokoro-fastapi[gpu]`
2. Create systemd user service (`kokoro-tts.service`) on port 8880
3. Update `speak-selection` and `speak`: curl Kokoro with Piper fallback
4. Update Speech Dispatcher: `kokoro-generic.conf` module
5. Test all three use cases
6. Keep Piper installed as permanent fallback

Full migration details: `kokoro_migration.md`

## File Map

```
~/.local/bin/
├── speak               # CLI TTS command
├── speak-selection     # Highlight-and-speak (Ctrl+Alt+S)
└── piper               # Piper TTS binary (pipx venv)

~/.local/share/piper-voices/
└── en_US-amy-medium.onnx  # Piper voice model (fallback)

~/.config/speech-dispatcher/
├── speechd.conf                          # Speech Dispatcher config
└── modules/
    ├── piper-generic.conf                # Piper module (current default)
    └── kokoro-generic.conf               # Kokoro module (target default)

~/.config/systemd/user/
└── kokoro-tts.service                    # Kokoro FastAPI server (target)

/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/
├── binding: <Ctrl><Alt>s
├── command: /home/dawson/.local/bin/speak-selection
└── name: Speak Selection
```

## What's NOT Included (by design)

- **Screen reader (Orca)**: Installed but disabled. Reads everything — not selective TTS.
- **Automatic speech on events**: No hooks on focus change, keystroke, or notification.
- **Wayland support**: xclip is X11-only. Future: wl-paste for Wayland.
- **Network TTS**: No cloud APIs. Everything runs locally on GPU/CPU.
- **Voice cloning**: Not in scope. Using pre-built voice models only.
