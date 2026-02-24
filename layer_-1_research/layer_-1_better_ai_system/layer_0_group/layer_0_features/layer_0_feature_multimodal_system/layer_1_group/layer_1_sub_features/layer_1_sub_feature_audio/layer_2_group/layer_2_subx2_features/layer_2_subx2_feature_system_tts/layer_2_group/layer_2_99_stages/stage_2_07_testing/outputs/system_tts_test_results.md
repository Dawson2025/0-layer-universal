# System TTS Test Results

**Date**: 2026-02-23

## Test Matrix

| # | Test | Command | Expected | Result |
|---|------|---------|----------|--------|
| 1 | Speech Dispatcher | `spd-say "test"` | Audio (robotic) | PASS |
| 2 | eSpeak NG direct | `espeak-ng "test"` | Audio (robotic) | PASS |
| 3 | Piper raw pipeline | `echo "test" \| piper --model amy ... \| aplay ...` | Audio (natural) | PASS |
| 4 | speak (args) | `speak "Hello world"` | Audio (natural) | PASS |
| 5 | speak (pipe) | `echo "test" \| speak` | Audio (natural) | PASS |
| 6 | speak (stop) | `speak -s` | Kills running speech | PASS |
| 7 | speak-selection | `speak-selection` (with text selected) | Audio of selection | Not yet tested with hotkey |

## Environment

| Component | Value |
|-----------|-------|
| OS | Ubuntu (Linux 6.17.0-14-generic) |
| Session | X11 |
| Audio | PulseAudio (protocol v35) |
| Piper | 1.4.1 |
| Voice | en_US-amy-medium (22050 Hz, S16_LE) |

## Performance

- Piper startup: ~0.5s (model loading)
- Short sentence (~10 words): ~1.5s total (load + synth + play)
- Long paragraph (~100 words): ~4s total

## Known Issues

| Issue | Severity | Status |
|-------|----------|--------|
| GNOME hotkey not yet configured | Low | Pending manual setup |
| No Wayland clipboard support | Low | X11 session currently |
| pathvalidate missing from piper-tts pip package | Medium | Fixed via pipx inject |
