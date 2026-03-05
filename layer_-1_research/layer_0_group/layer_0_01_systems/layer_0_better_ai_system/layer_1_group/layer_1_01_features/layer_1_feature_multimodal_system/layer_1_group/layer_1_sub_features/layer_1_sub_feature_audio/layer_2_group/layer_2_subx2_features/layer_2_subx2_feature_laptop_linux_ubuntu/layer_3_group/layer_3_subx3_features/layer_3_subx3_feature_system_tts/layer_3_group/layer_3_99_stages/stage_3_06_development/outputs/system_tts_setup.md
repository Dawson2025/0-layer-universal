---
resource_id: "61fa1db2-4bc4-46ee-ae7e-89891f8ea2fd"
resource_type: "output"
resource_name: "system_tts_setup"
---
# System TTS Setup — Development Log

**Date**: 2026-02-24 (Phase 2 update)
**Status**: Working (Phase 2 complete)

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

## Phase 1: Direct Piper Scripts

### Piper TTS Installation
```bash
pipx install piper-tts
pipx inject piper-tts pathvalidate  # missing dependency fix
```

### Voice Model
```bash
mkdir -p ~/.local/share/piper-voices
curl -L -o ~/.local/share/piper-voices/en_US-amy-medium.onnx \
  "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx?download=true"
curl -L -o ~/.local/share/piper-voices/en_US-amy-medium.onnx.json \
  "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json?download=true"
```

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

## Phase 2: Speech Dispatcher + Piper + Orca

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

### Orca Enablement
```bash
gsettings set org.gnome.desktop.a11y.applications screen-reader-enabled true
orca  # or DISPLAY=:0 orca &
```

### Verification
```bash
spd-say -O                                    # Shows: espeak-ng, piper-generic
spd-say "Hello from Piper"                    # Natural voice (Piper)
spd-say -o espeak-ng "Hello from eSpeak"      # Robotic voice (eSpeak NG)
speak "Hello from speak script"               # Direct Piper pipeline
```

---

## Audio Stack

```
Session: X11
Audio: PulseAudio (server protocol v35)
Direct path: Piper → paplay → PulseAudio → hardware
speechd path: speechd daemon → sd_generic → Piper → paplay → PulseAudio → hardware
```

## Known Issues (Resolved)

| Issue | Fix |
|-------|-----|
| Piper missing `pathvalidate` | `pipx inject piper-tts pathvalidate` |
| GNOME keybinding schema wrong for Unity | Use `com.canonical.unity.settings-daemon.plugins.media-keys` |
| gsd-media-keys dead (shortcuts broken) | gsd-keepalive.timer auto-restarts every 60s |
| gsd-power dead (brightness broken) | gsd-keepalive.timer auto-restarts every 60s |
| speechd.conf empty punctuation args | Removed GenericPunctNone/Some/Most/All empty strings |

## Platform Dependencies

See `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/setup/.../outputs/` for:
- `gnome_architecture.md` — gsd-* daemon roles and failure modes
- `gsd_keepalive_fix.md` — keepalive timer setup
