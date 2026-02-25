# Kokoro TTS — GPU-Accelerated Mode

## Overview
Kokoro is an 82M-parameter neural TTS model. Top of HuggingFace TTS Arena. 40+ voices across 7 languages. Runs on CPU at real-time speed, on GPU at near-instant speed.

## Installation Options

### CLI Tool (simple pipe usage)
```bash
pip install kokoro-tts
# or
uv tool install kokoro-tts
```
Usage: `echo "Hello" | kokoro-tts - --stream | paplay`
Requires model files: `voices-v1.0.bin` and `kokoro-v1.0.onnx`

### FastAPI Server (recommended for persistent service)
```bash
# GPU variant with CUDA
uvx kokoro-fastapi[gpu] serve --host 127.0.0.1 --port 8880 --models-dir ~/Models/kokoro

# CPU variant
uvx kokoro-fastapi[cpu] serve --host 127.0.0.1 --port 8880 --models-dir ~/Models/kokoro
```
Models auto-download from HuggingFace on first use (~300MB per language).

### Systemd Service (auto-start)
```ini
# ~/.config/systemd/user/kokoro.service
[Unit]
Description=Kokoro Text-to-Speech Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/uvx kokoro-fastapi[gpu] serve --host 127.0.0.1 --port 8880 --models-dir %h/Models/kokoro
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
```

### VoiceMode Managed (simplest)
```bash
voicemode service install kokoro
voicemode service enable kokoro
```

## API
OpenAI-compatible REST API at `http://127.0.0.1:8880/v1`:
```bash
curl -s http://127.0.0.1:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"input":"Hello world","voice":"af_sky","model":"kokoro"}' \
  --output speech.wav
```

## Voice Selection
- **American Female**: af_sky (default), af_sarah
- **American Male**: am_adam, am_michael
- **British Female**: bf_emma, bf_isabella
- **British Male**: bm_george, bm_lewis
- Plus Spanish, French, Italian, Portuguese, Chinese, Japanese, Hindi voices

## Performance on RTX 4060
- ~200-300MB VRAM usage
- Sub-0.1s for sentence-length text
- 96x+ real-time generation
- ~500MB-1GB system RAM

## Sources
- https://github.com/nazdridoy/kokoro-tts (CLI)
- https://github.com/PierrunoYT/Kokoro-TTS-Local (local impl)
- https://huggingface.co/hexgrad/Kokoro-82M (model)
