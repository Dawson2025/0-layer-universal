# System TTS Research

**Date**: 2026-02-23

## TTS Engine Comparison

| Engine | Type | Quality | Speed | Size | License |
|--------|------|---------|-------|------|---------|
| eSpeak NG | Formant | Low (robotic) | Instant | ~2MB | GPL-3 |
| Piper | Neural (VITS) | High (natural) | Fast (~1s startup) | ~60MB/voice | MIT |
| Festival | Diphone | Medium | Medium | ~50MB | BSD-like |
| Mimic 3 | Neural | High | Medium | ~100MB/voice | Apache-2 |

**Decision**: Piper — best quality-to-speed ratio, MIT license, small model files, active development by Rhasspy project.

## Voice Models Evaluated

| Model | Accent | Quality | Size | Sample Rate |
|-------|--------|---------|------|-------------|
| en_US-amy-medium | US Female | Good | 60MB | 22050 Hz |
| en_US-lessac-medium | US Male | Good | 63MB | 22050 Hz |
| en_GB-alan-medium | British Male | Good | 60MB | 22050 Hz |

**Decision**: en_US-amy-medium as default. Additional voices can be added later.

## Clipboard/Selection Tools

| Tool | Works With | Status |
|------|-----------|--------|
| xclip | X11 | Installed, working |
| xsel | X11 | Not installed |
| wl-paste | Wayland | Installed, not needed (X11 session) |

**Decision**: xclip for X11 primary selection + clipboard fallback.

## Audio Output Stack

```
Text → Piper (ONNX inference) → raw PCM (S16_LE, 22050Hz, mono) → aplay → ALSA → PulseAudio → hardware
```

Alternative: `paplay` for PulseAudio direct, but aplay is more universal.

## Sources

- [Piper TTS GitHub](https://github.com/rhasspy/piper)
- [Piper Voice Models on HuggingFace](https://huggingface.co/rhasspy/piper-voices)
- [eSpeak NG](https://github.com/espeak-ng/espeak-ng)
