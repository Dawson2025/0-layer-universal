---
resource_id: "61fa1db2-4bc4-46ee-ae7e-89891f8ea2fd"
resource_type: "output"
resource_name: "system_tts_setup"
---
# System TTS Setup — Development Log

**Date**: 2026-02-24 (Phase 2 update)
**Status**: Working (Phase 2 complete)

<!-- section_id: "390657b2-ca35-4dd6-9461-c16b2e12f8c0" -->
## Components Installed

| Component | Version | Status |
|-----------|---------|--------|
| Orca | 46.1 | Pre-installed, enabled via gsettings |
| eSpeak NG | 1.51 | Pre-installed, registered as Speech Dispatcher fallback |
| Speech Dispatcher | 0.12.0-rc2 | Pre-installed, user config with Piper as default |
| Piper TTS | 1.4.1 | Installed via `pipx install piper-tts` |
| Voice Model | en_US-amy-medium | Downloaded from HuggingFace |
| xclip | system | Pre-installed (X11 clipboard) |
| paplay | system | PulseAudio playback (all audio paths) |

<!-- section_id: "d95afbd5-5e16-482f-b3f3-549d2093d48f" -->
## Phase 1: Direct Piper Scripts

<!-- section_id: "76a41144-c5a4-4b4f-958b-5a0e2789975d" -->
### Piper TTS Installation
```bash
pipx install piper-tts
pipx inject piper-tts pathvalidate  # missing dependency fix
```

<!-- section_id: "da5829bb-4191-437b-a465-2c0b7d6c6549" -->
### Voice Model
```bash
mkdir -p ~/.local/share/piper-voices
curl -L -o ~/.local/share/piper-voices/en_US-amy-medium.onnx \
  "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx?download=true"
curl -L -o ~/.local/share/piper-voices/en_US-amy-medium.onnx.json \
  "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json?download=true"
```

<!-- section_id: "9871a6b7-7835-48a1-8a7f-62c8ff0fe395" -->
### Scripts Created

**`~/.local/bin/speak`** — General TTS command:
- `speak "Hello world"` — speak from arguments
- `echo "Hello" | speak` — speak from stdin
- `speak -s` — stop current speech

**`~/.local/bin/speak-selection`** — X11 highlight-and-speak:
- Reads X primary selection (highlighted text)
- Falls back to clipboard if no selection
- Toggle: run again to stop
- Bound to Ctrl+Alt+S via Unity keybinding

<!-- section_id: "d9bbceb2-4f43-4b77-ae28-8fa4cac670f6" -->
### Hotkey Binding (Unity)
```bash
gsettings set com.canonical.unity.settings-daemon.plugins.media-keys custom-keybindings \
  "['/com/canonical/unity/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"
gsettings set com.canonical.unity.settings-daemon.plugins.media-keys.custom-keybinding:/com/canonical/unity/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name 'Speak Selection'
gsettings set com.canonical.unity.settings-daemon.plugins.media-keys.custom-keybinding:/com/canonical/unity/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command '/home/dawson/.local/bin/speak-selection'
gsettings set com.canonical.unity.settings-daemon.plugins.media-keys.custom-keybinding:/com/canonical/unity/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding '<Ctrl><Alt>s'
```

**Note**: Desktop is Unity (`XDG_CURRENT_DESKTOP=Unity`), uses `com.canonical.unity.settings-daemon.plugins.media-keys` — NOT `org.gnome.settings-daemon.plugins.media-keys`.

---

<!-- section_id: "2d0cf602-de43-4fd0-8a91-6998d4a31520" -->
## Phase 2: Speech Dispatcher + Piper + Orca

<!-- section_id: "4f5896c5-151f-4d21-84f5-88de732a148a" -->
### Piper Module for Speech Dispatcher

Created user-local config (no sudo needed):

```bash
mkdir -p ~/.config/speech-dispatcher/modules
```

**`~/.config/speech-dispatcher/modules/piper-generic.conf`**:
- Uses sd_generic module to invoke Piper via shell command
- Routes audio through paplay (PulseAudio)
- Defines Amy voice as default

**`~/.config/speech-dispatcher/speechd.conf`** (copied from system, modified):
- Added: `AddModule "espeak-ng" "sd_espeak-ng" "espeak-ng.conf"`
- Added: `AddModule "piper-generic" "sd_generic" "piper-generic.conf"`
- Set: `DefaultModule piper-generic`

<!-- section_id: "b3409fe7-bdad-4701-98cf-ef8ae6f1f572" -->
### Orca Enablement
```bash
gsettings set org.gnome.desktop.a11y.applications screen-reader-enabled true
orca  # or DISPLAY=:0 orca &
```

<!-- section_id: "2b7d1b24-83d3-46f0-9dc1-96d625031889" -->
### Verification
```bash
spd-say -O                                    # Shows: espeak-ng, piper-generic
spd-say "Hello from Piper"                    # Natural voice (Piper)
spd-say -o espeak-ng "Hello from eSpeak"      # Robotic voice (eSpeak NG)
speak "Hello from speak script"               # Direct Piper pipeline
```

---

<!-- section_id: "7a308735-97b2-4614-900c-88d471c60637" -->
## Audio Stack

```
Session: X11
Audio: PulseAudio (server protocol v35)
Direct path: Piper → paplay → PulseAudio → hardware
speechd path: speechd daemon → sd_generic → Piper → paplay → PulseAudio → hardware
```

<!-- section_id: "516d3946-7890-4c61-915e-73e917a033a6" -->
## Known Issues (Resolved)

| Issue | Fix |
|-------|-----|
| Piper missing `pathvalidate` | `pipx inject piper-tts pathvalidate` |
| GNOME keybinding schema wrong for Unity | Use `com.canonical.unity.settings-daemon.plugins.media-keys` |
| gsd-media-keys dead (shortcuts broken) | gsd-keepalive.timer auto-restarts every 60s |
| gsd-power dead (brightness broken) | gsd-keepalive.timer auto-restarts every 60s |
| speechd.conf empty punctuation args | Removed GenericPunctNone/Some/Most/All empty strings |

<!-- section_id: "c0f7d61f-4a55-4cbd-a00c-2c5a8ee92a95" -->
## Platform Dependencies

See `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/setup/.../outputs/` for:
- `gnome_architecture.md` — gsd-* daemon roles and failure modes
- `gsd_keepalive_fix.md` — keepalive timer setup
