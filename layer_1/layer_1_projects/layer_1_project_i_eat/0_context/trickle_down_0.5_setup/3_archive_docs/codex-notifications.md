---
resource_id: "fb3fe75c-4d6f-4503-9c6c-d84660e93c9b"
resource_type: "document"
resource_name: "codex-notifications"
---
<!-- section_id: "0939b422-6b08-4fe2-9de6-c60ae55cc456" -->
## Codex Desktop & Audio Alerts (WSL)

This guide wires Codex (or any CLI tool) into Windows toast notifications and loud audible alerts while running inside WSL.

<!-- section_id: "af8e100c-0525-48e8-9196-46ec8ae71b3f" -->
### 1. Install the helpers

- **Windows notification bridge:** download [`wsl-notify-send.exe`](https://github.com/stuartleeks/wsl-notify-send/releases) to a Windows directory such as `C:\Tools\wsl-notify-send.exe`, then add that directory to your Windows `PATH`.
- **Speech synthesis (WSL):**
  ```bash
  sudo apt-get update && sudo apt-get install -y speech-dispatcher
  ```
- **Audio playback (WSL):**
  ```bash
  sudo apt-get install -y ffmpeg
  ```
  `ffplay` ships with ffmpeg.

Optionally pick `.wav` files under Windows (for example `C:\Windows\Media\notify.wav`) for distinctive success/failure sounds.

<!-- section_id: "68810c27-022b-421a-a1c9-168856871e9d" -->
### 2. Wrapper script

`scripts/dev/codex-notify.sh` wraps any command, watches its exit status, then triggers the notification stack:

```bash
scripts/dev/codex-notify.sh codex <your codex args>
```

The script auto-detects `wsl-notify-send.exe`, `spd-say`, and `ffplay`. Configure behaviour with environment variables (set in `.bashrc`/`.zshrc` or inline):

```bash
export CODEX_NOTIFY_SENDER="/mnt/c/Tools/wsl-notify-send.exe"
export CODEX_NOTIFY_SUCCESS_SOUND="/mnt/c/Users/<you>/Sounds/success.wav"
export CODEX_NOTIFY_FAILURE_SOUND="/mnt/c/Users/<you>/Sounds/fail.wav"
export CODEX_NOTIFY_SUCCESS_TEXT="Codex finished."
export CODEX_NOTIFY_FAILURE_TEXT="Codex is waiting for you."
export CODEX_NOTIFY_TURN_TITLE="Codex needs input"
export CODEX_NOTIFY_TURN_TEXT="Codex needs your input."
# Play distinct Windows system sounds without extra packages
export CODEX_NOTIFY_COMMAND_SUCCESS='powershell.exe -c "[System.Media.SystemSounds]::Asterisk.Play()"'
export CODEX_NOTIFY_COMMAND_FAILURE='powershell.exe -c "[System.Media.SystemSounds]::Hand.Play()"'
export CODEX_NOTIFY_COMMAND_TURN='powershell.exe -c "[System.Media.SystemSounds]::Question.Play()"'
```

Disable the terminal bell with `export CODEX_NOTIFY_BELL=0` if desired.

To make it seamless, add an alias:

```bash
alias codex-notify="$HOME/code/lang-trak-in-progress/scripts/dev/codex-notify.sh codex"
```

Then run Codex as:

```bash
codex-notify <args>
```

<!-- section_id: "ff81244a-dccf-4d8e-98c4-b69bb93c9d3c" -->
### 3. Interactive turn notifications

Codex' built-in `notify` hook runs an external program after each turn. Point it to `scripts/dev/codex-turn-notify.py` so you get alerts whenever the agent pauses for your input:

```toml
# ~/.codex/config.toml
notify = ["/home/dawson/dawson-workspace/code/lang-trak-in-progress/scripts/dev/codex-turn-notify.py"]
```

The hook reuses the same `CODEX_NOTIFY_*` environment variables shown above. Add the optional variables `CODEX_NOTIFY_TURN_*` to customize the title/text/sound specifically for "waiting for input" events. The script emits:

- Windows toast (`CODEX_NOTIFY_SENDER` or auto-detected `wsl-notify-send.exe`)
- Optional speech (`CODEX_NOTIFY_TURN_TEXT`)
- Optional WAV playback (`CODEX_NOTIFY_TURN_SOUND`)
- Optional PowerShell system sound (`CODEX_NOTIFY_COMMAND_TURN`)
- Terminal bell (unless `CODEX_NOTIFY_BELL=0`)

When running inside WSL, if no Linux speech engine is available the hook automatically calls `powershell.exe` to speak the notification text and plays a short console beep—no extra setup needed.

<!-- section_id: "f8364e8f-b189-407f-879c-6c73cf3895b2" -->
### 4. Windows Terminal / VS Code integration

Use the alias in your WSL shell sessions (including VS Code's integrated terminal). Whenever Codex exits—success, error, or pause—you'll get:

- A Windows toast via `wsl-notify-send`
- Spoken feedback via `spd-say`
- A loud `.wav` via `ffplay`
- A terminal bell (unless disabled)
- Optional PowerShell-triggered Windows system sounds

All notifications run in the background so the wrapper exits promptly with Codex's original status code.
