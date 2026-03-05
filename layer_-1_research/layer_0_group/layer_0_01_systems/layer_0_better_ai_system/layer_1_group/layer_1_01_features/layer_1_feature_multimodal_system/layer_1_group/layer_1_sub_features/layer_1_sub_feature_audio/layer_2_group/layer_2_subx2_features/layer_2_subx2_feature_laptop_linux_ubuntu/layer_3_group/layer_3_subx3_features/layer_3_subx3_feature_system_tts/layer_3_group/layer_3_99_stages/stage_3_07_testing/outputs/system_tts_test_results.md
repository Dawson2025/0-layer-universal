---
resource_id: "8183b0fe-5790-4ac5-91ae-1e529428df08"
resource_type: "output"
resource_name: "system_tts_test_results"
---
# System TTS Test Results

**Date**: 2026-02-24 (Phase 2 update)

<!-- section_id: "3fd7687b-769c-4cec-a6cd-6cdcda1bf6bd" -->
## Automated Test Suite

Test script: `outputs/test-system-tts.sh` — 29 tests across 8 categories.

**Result**: 29/29 PASS

| Category | Tests | Result |
|----------|-------|--------|
| Component Availability | 5 | All pass (Piper, Amy voice, paplay, spd-say, sd_generic) |
| Configuration | 5 | All pass (user speechd.conf, module config, DefaultModule, AddModule x2) |
| Module Loading | 2 | All pass (piper-generic and espeak-ng both loaded) |
| Module Config Validation | 3 | All pass (no errors in log, GenericExecuteSynth, DefaultVoice) |
| Audio Pipeline | 3 | All pass (Piper raw, spd-say default, spd-say espeak-ng) |
| Script Tests | 5 | All pass (speak/speak-selection executable, all use paplay) |
| Orca Readiness | 2 | All pass (Orca binary available, version 46.1) |
| GSD Keepalive | 3 | All pass (timer active, gsd-media-keys running, gsd-power running) |

<!-- section_id: "95b83741-8848-4ca4-87db-6c31105c3108" -->
## Manual Test Matrix

| # | Test | Command | Expected | Result |
|---|------|---------|----------|--------|
| 1 | spd-say Piper (default) | `spd-say "test"` | Natural voice | PASS |
| 2 | spd-say eSpeak fallback | `spd-say -o espeak-ng "test"` | Robotic voice | PASS |
| 3 | speak (args) | `speak "Hello world"` | Natural voice via paplay | PASS |
| 4 | speak (pipe) | `echo "test" \| speak` | Natural voice | PASS |
| 5 | speak (stop) | `speak -s` | Kills running speech | PASS |
| 6 | speak-selection hotkey | Ctrl+Alt+S with text selected | Reads selection | PASS |
| 7 | speak-selection toggle | Ctrl+Alt+S while speaking | Stops speech | PASS |
| 8 | Module listing | `spd-say -O` | Shows espeak-ng, piper-generic | PASS |
| 9 | Voice listing | `spd-say -L` | Shows Amy voice entries | PASS |
| 10 | Orca start | `orca` | Starts, announces focus | PASS |

<!-- section_id: "16c4c296-0f41-4d76-8578-a0662afb5e57" -->
## Environment

| Component | Value |
|-----------|-------|
| OS | Ubuntu (Linux 6.17.0-14-generic) |
| Desktop | Unity (XDG_CURRENT_DESKTOP=Unity) |
| Session | X11 |
| Audio | PulseAudio (protocol v35) via paplay |
| Piper | 1.4.1 |
| Voice | en_US-amy-medium (22050 Hz, S16_LE, mono) |
| Speech Dispatcher | 0.12.0-rc2 |
| Orca | 46.1 |

<!-- section_id: "52a5a36a-da50-421c-bfb9-c4a7dd704893" -->
## Performance

- Piper startup: ~0.5s (model loading)
- Short sentence (~10 words): ~1.5s total (load + synth + play)
- Long paragraph (~100 words): ~4s total

<!-- section_id: "538b107f-eb19-4857-949a-2fa8c029d8c4" -->
## Resolved Issues

| Issue | Fix |
|-------|-----|
| pathvalidate missing from piper-tts | `pipx inject piper-tts pathvalidate` |
| GNOME keybinding wrong schema | Use Unity schema: `com.canonical.unity.settings-daemon.plugins.media-keys` |
| gsd-media-keys dead | gsd-keepalive.timer auto-restarts every 60s |
| Empty punctuation args in module config | Removed GenericPunctNone/Some/Most/All lines |
| Audio device contention (aplay vs PulseAudio) | All paths now use paplay |
