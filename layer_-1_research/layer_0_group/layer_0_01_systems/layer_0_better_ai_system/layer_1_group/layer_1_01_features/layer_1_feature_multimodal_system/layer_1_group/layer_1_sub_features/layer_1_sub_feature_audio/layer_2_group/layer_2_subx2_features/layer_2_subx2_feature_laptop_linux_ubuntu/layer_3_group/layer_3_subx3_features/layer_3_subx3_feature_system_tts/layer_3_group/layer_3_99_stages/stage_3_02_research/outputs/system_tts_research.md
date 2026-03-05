---
resource_id: "c6f90a9d-d51e-4ab8-9e47-9ae8379db07a"
resource_type: "output"
resource_name: "system_tts_research"
---
# System TTS Research

**Date**: 2026-02-23

<!-- section_id: "c1b8c3fd-f9a4-4c61-ab04-02b909e99aa3" -->
## TTS Engine Comparison

| Engine | Type | Quality | Speed | Size | License |
|--------|------|---------|-------|------|---------|
| eSpeak NG | Formant | Low (robotic) | Instant | ~2MB | GPL-3 |
| Piper | Neural (VITS) | High (natural) | Fast (~1s startup) | ~60MB/voice | MIT |
| **Kokoro** | **Neural (82M)** | **Highest (#1 HF Arena)** | **Sub-0.1s (GPU)** | **~200-300MB VRAM** | **Apache-2** |
| Festival | Diphone | Medium | Medium | ~50MB | BSD-like |
| Mimic 3 | Neural | High | Medium | ~100MB/voice | Apache-2 |

**Current**: Piper — working, good quality, CPU-only.
**Target upgrade**: Kokoro — #1 on HuggingFace TTS Arena, 40+ voices, GPU-accelerated (sub-0.1s on RTX 4060 with 8GB VRAM). Install via `pip install kokoro-tts` (CLI) or `uvx kokoro-fastapi[gpu] serve` (FastAPI server on port 8880, OpenAI-compatible API).

<!-- section_id: "9bac292a-fc1c-42b9-93aa-29438d9c5fc1" -->
## Voice Models Evaluated

| Model | Accent | Quality | Size | Sample Rate |
|-------|--------|---------|------|-------------|
| en_US-amy-medium | US Female | Good | 60MB | 22050 Hz |
| en_US-lessac-medium | US Male | Good | 63MB | 22050 Hz |
| en_GB-alan-medium | British Male | Good | 60MB | 22050 Hz |

**Decision**: en_US-amy-medium as default. Additional voices can be added later.

<!-- section_id: "a5469bc8-5663-4f43-b660-56985c239e06" -->
## Clipboard/Selection Tools

| Tool | Works With | Status |
|------|-----------|--------|
| xclip | X11 | Installed, working |
| xsel | X11 | Not installed |
| wl-paste | Wayland | Installed, not needed (X11 session) |

**Decision**: xclip for X11 primary selection + clipboard fallback.

<!-- section_id: "3a198557-990d-463f-b79c-8dd1b772c807" -->
## Audio Output Stack

```
Text → Piper (ONNX inference) → raw PCM (S16_LE, 22050Hz, mono) → aplay → ALSA → PulseAudio → hardware
```

Alternative: `paplay` for PulseAudio direct, but aplay is more universal.

<!-- section_id: "0899e550-1377-4eac-a255-de10bed3a096" -->
## Kokoro Details

- **Model**: 82M parameters, StyleTTS2-inspired architecture
- **Voices**: 40+ built-in (af_heart default, multiple accents/genders)
- **GPU**: CUDA-accelerated via `kokoro-fastapi[gpu]` — uses RTX 4060 for near-instant generation
- **API**: OpenAI-compatible (`/v1/audio/speech`), runs as systemd service or managed by VoiceMode
- **Install options**:
  - CLI: `pip install kokoro-tts` → `kokoro "text" --voice af_heart`
  - Server: `uvx kokoro-fastapi[gpu] serve` → `curl localhost:8880/v1/audio/speech -d '{"input":"text","voice":"af_heart"}'`
  - VoiceMode managed: handles Kokoro lifecycle as systemd service

<!-- section_id: "9ebf5545-30ff-47ca-a9fc-aba63ed7bdca" -->
## Sources

- [Piper TTS GitHub](https://github.com/rhasspy/piper)
- [Piper Voice Models on HuggingFace](https://huggingface.co/rhasspy/piper-voices)
- [eSpeak NG](https://github.com/espeak-ng/espeak-ng)
- [Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M)
- [Kokoro FastAPI](https://github.com/remsky/Kokoro-FastAPI)
- [VoiceMode MCP](https://github.com/nicobailey/voicemode)
