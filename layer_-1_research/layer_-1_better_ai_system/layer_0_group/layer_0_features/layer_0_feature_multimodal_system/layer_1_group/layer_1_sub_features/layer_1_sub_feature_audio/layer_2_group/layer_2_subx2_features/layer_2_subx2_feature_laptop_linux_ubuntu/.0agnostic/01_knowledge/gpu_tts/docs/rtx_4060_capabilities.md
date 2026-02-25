# RTX 4060 Laptop GPU — TTS Capabilities

## Hardware
- **Model**: NVIDIA GeForce RTX 4060 Laptop GPU (AD107M)
- **VRAM**: 8188 MiB (8 GB GDDR6)
- **Driver**: 580.126.09 (NVIDIA UNIX Open Kernel Module)
- **CUDA Compute**: libnvidia-compute-580 installed
- **nvidia-smi**: `/usr/bin/nvidia-smi` (not in default PATH for some shells)

## TTS Inference Performance
- 8GB VRAM is far more than needed for Kokoro (82M params, ~200-300MB VRAM)
- Kokoro achieves 96x real-time on basic cloud GPU; RTX 4060 should exceed this
- Sub-0.1s generation for short text (sentence-length) with GPU
- Can run Kokoro TTS + Whisper STT simultaneously (combined <2GB VRAM)

## CUDA Setup Notes
- PyTorch with CUDA not installed by default; need `pip install torch --index-url https://download.pytorch.org/whl/cu121`
- `kokoro-fastapi[gpu]` variant includes CUDA ONNX runtime
- ONNX Runtime GPU: `onnxruntime-gpu` package for CUDA-accelerated inference
- Verify: `python3 -c "import torch; print(torch.cuda.is_available())"` should return True after setup
