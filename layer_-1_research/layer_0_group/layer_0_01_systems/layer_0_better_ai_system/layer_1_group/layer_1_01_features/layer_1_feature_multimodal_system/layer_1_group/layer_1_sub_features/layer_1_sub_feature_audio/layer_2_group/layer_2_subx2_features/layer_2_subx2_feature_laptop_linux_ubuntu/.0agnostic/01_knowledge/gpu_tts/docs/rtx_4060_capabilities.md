---
resource_id: "9c823964-69b6-43fd-9253-88a72aff8f3f"
resource_type: "knowledge"
resource_name: "rtx_4060_capabilities"
---
# RTX 4060 Laptop GPU — TTS Capabilities

<!-- section_id: "0b8a69fd-e7f2-442e-8bfc-df2a4580a86d" -->
## Hardware
- **Model**: NVIDIA GeForce RTX 4060 Laptop GPU (AD107M)
- **VRAM**: 8188 MiB (8 GB GDDR6)
- **Driver**: 580.126.09 (NVIDIA UNIX Open Kernel Module)
- **CUDA Compute**: libnvidia-compute-580 installed
- **nvidia-smi**: `/usr/bin/nvidia-smi` (not in default PATH for some shells)

<!-- section_id: "b561dc56-4e24-4da0-a390-a534beab72ac" -->
## TTS Inference Performance
- 8GB VRAM is far more than needed for Kokoro (82M params, ~200-300MB VRAM)
- Kokoro achieves 96x real-time on basic cloud GPU; RTX 4060 should exceed this
- Sub-0.1s generation for short text (sentence-length) with GPU
- Can run Kokoro TTS + Whisper STT simultaneously (combined <2GB VRAM)

<!-- section_id: "80584537-867e-433b-b092-d82f2fde2290" -->
## CUDA Setup Notes
- PyTorch with CUDA not installed by default; need `pip install torch --index-url https://download.pytorch.org/whl/cu121`
- `kokoro-fastapi[gpu]` variant includes CUDA ONNX runtime
- ONNX Runtime GPU: `onnxruntime-gpu` package for CUDA-accelerated inference
- Verify: `python3 -c "import torch; print(torch.cuda.is_available())"` should return True after setup
