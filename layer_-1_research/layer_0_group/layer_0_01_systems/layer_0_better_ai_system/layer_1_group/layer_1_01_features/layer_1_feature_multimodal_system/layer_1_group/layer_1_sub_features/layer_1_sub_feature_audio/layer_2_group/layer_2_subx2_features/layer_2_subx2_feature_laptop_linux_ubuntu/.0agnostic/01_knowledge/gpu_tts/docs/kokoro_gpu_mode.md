---
resource_id: "37babab1-fa33-409a-8c2e-d9a4cb94a5cf"
resource_type: "knowledge"
resource_name: "kokoro_gpu_mode"
---
# Kokoro TTS — GPU-Accelerated Mode

<!-- section_id: "68f51fc9-e6e9-4686-b4ca-bed83afba3a4" -->
## Overview
Kokoro is an 82M-parameter neural TTS model. Top of HuggingFace TTS Arena. 40+ voices across 7 languages. Runs on CPU at real-time speed, on GPU at near-instant speed.

<!-- section_id: "11e3535d-8d0a-4f1d-8528-07300ddf69de" -->
## Installation Options

<!-- section_id: "afa9eec4-fbe8-4166-9765-d9d9db030476" -->
### CLI Tool (simple pipe usage)
```bash
pip install kokoro-tts
# or
uv tool install kokoro-tts
```
Usage: `echo "Hello" | kokoro-tts - --stream | paplay`
Requires model files: `voices-v1.0.bin` and `kokoro-v1.0.onnx`

<!-- section_id: "85a4065e-d5af-4bde-8f11-8e164b1dd8b8" -->
### FastAPI Server (recommended for persistent service)
```bash
# GPU variant with CUDA
uvx kokoro-fastapi[gpu] serve --host 127.0.0.1 --port 8880 --models-dir ~/Models/kokoro

# CPU variant
uvx kokoro-fastapi[cpu] serve --host 127.0.0.1 --port 8880 --models-dir ~/Models/kokoro
```
Models auto-download from HuggingFace on first use (~300MB per language).

<!-- section_id: "d97ef84c-39e6-4766-9777-47d85c61330b" -->
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

<!-- section_id: "5112a2df-e1a6-44ce-bd17-19162d58a360" -->
### VoiceMode Managed (simplest)
```bash
voicemode service install kokoro
voicemode service enable kokoro
```

<!-- section_id: "b35f7c82-c2eb-4a57-8e49-38ac1108fc67" -->
## API
OpenAI-compatible REST API at `http://127.0.0.1:8880/v1`:
```bash
curl -s http://127.0.0.1:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"input":"Hello world","voice":"af_sky","model":"kokoro"}' \
  --output speech.wav
```

<!-- section_id: "ee8ec3bf-a339-490f-9e31-f1b44efc8bfa" -->
## Voice Selection
- **American Female**: af_sky (default), af_sarah
- **American Male**: am_adam, am_michael
- **British Female**: bf_emma, bf_isabella
- **British Male**: bm_george, bm_lewis
- Plus Spanish, French, Italian, Portuguese, Chinese, Japanese, Hindi voices

<!-- section_id: "0cabe8a6-0922-41f2-86b9-9090cc4b2a49" -->
## Performance on RTX 4060
- ~200-300MB VRAM usage
- Sub-0.1s for sentence-length text
- 96x+ real-time generation
- ~500MB-1GB system RAM

<!-- section_id: "208efb34-d178-4300-bd6a-c578d92898f3" -->
## Sources
- https://github.com/nazdridoy/kokoro-tts (CLI)
- https://github.com/PierrunoYT/Kokoro-TTS-Local (local impl)
- https://huggingface.co/hexgrad/Kokoro-82M (model)
