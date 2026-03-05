---
resource_id: "0639a1d7-c48e-452a-92d8-3c8763eb1e55"
resource_type: "document"
resource_name: "cloud_apis"
---
# Cloud Speech-to-Text APIs

**Last Updated**: January 12, 2026
**Category**: Developer APIs for custom solutions

<!-- section_id: "cc87be33-e5af-41b1-bce6-7f8a8b9852ee" -->
## Overview

These are cloud-based speech-to-text APIs for developers building custom solutions. They are **not** turnkey desktop dictation tools - they require integration work.

<!-- section_id: "40b14287-8d6d-4481-b6e8-1cae15c43e7b" -->
## When to Use These

| Use Case | Recommendation |
|----------|----------------|
| Need system-wide dictation now | Use [Vibe Typer](vibe_typer.md) or [Whisper-Dictation](whisper_dictation.md) |
| Building custom application | Consider these APIs |
| Need specific language support | Check API language coverage |
| Enterprise integration | These may fit better |

<!-- section_id: "3afa12b3-2ab6-4f11-a236-444633d602f3" -->
## Google Cloud Speech-to-Text

**Website**: [cloud.google.com/speech-to-text](https://cloud.google.com/speech-to-text)

| Aspect | Details |
|--------|---------|
| Accuracy | Highly accurate |
| Languages | 125+ languages and variants |
| Features | Real-time, batch, auto punctuation |
| Pricing | Pay per use (free tier available) |
| Integration | REST API, client libraries |

<!-- section_id: "84f14252-4799-4abb-a42f-540d03ff6b6f" -->
### Pros
- Extensive language support
- High accuracy
- Well-documented
- Multiple output formats

<!-- section_id: "61ac46f6-e225-48f5-b0d4-e63c4e4af849" -->
### Cons
- Requires cloud connection
- Pay per use after free tier
- No turnkey desktop UX
- Requires development work

<!-- section_id: "c0db2a26-26d6-432b-98c6-6c7abc5c1046" -->
## AssemblyAI

**Website**: [assemblyai.com](https://www.assemblyai.com)

| Aspect | Details |
|--------|---------|
| Focus | Developer-friendly API |
| Features | Transcription, speaker diarization, summarization |
| Accuracy | Competitive with Google |
| Pricing | Pay per audio hour |

<!-- section_id: "cc8800c7-6c0d-4c60-a5c7-38e0d301e306" -->
### Pros
- Easy to integrate
- Good documentation
- Additional AI features (summarization, etc.)

<!-- section_id: "4cc26bfa-fc75-44b5-a076-77b49a5e8c24" -->
### Cons
- No desktop UX
- Cloud-only
- Requires development

<!-- section_id: "73a9302e-f591-4819-9f1d-34fa0ba94ca0" -->
## Picovoice

**Website**: [picovoice.ai](https://picovoice.ai)

| Aspect | Details |
|--------|---------|
| Focus | On-device voice AI |
| Features | Wake word, speech-to-text, intent recognition |
| Privacy | Can run fully on-device |
| Pricing | Free tier, paid plans |

<!-- section_id: "336d84de-2971-43e1-92b1-1c45ac7e41b3" -->
### Pros
- On-device processing option
- Privacy-friendly
- Low latency

<!-- section_id: "25ab2eee-1ea1-4280-9a3d-112a8121e4f5" -->
### Cons
- No system-wide desktop UX out of box
- Requires integration work

<!-- section_id: "d0c6e7d9-d105-4408-a36a-2255455ee77d" -->
## Comparison

| API | Accuracy | Languages | On-device | Ease of Use |
|-----|----------|-----------|-----------|-------------|
| Google Cloud | Excellent | 125+ | No | Medium |
| AssemblyAI | Excellent | 20+ | No | Easy |
| Picovoice | Good | 10+ | Yes | Medium |

<!-- section_id: "782427e4-6c1e-4e87-8995-4860f2046e3e" -->
## For Most Users

If you just want system-wide dictation on Linux, skip these APIs and use:

1. **[Vibe Typer](vibe_typer.md)** - Easiest setup, cloud processing
2. **[Whisper-Dictation](whisper_dictation.md)** - Local processing, privacy
3. **[OpenWhispr](openwhispr.md)** - Cross-platform, open source

These APIs are for developers building custom voice applications, not end-users wanting dictation.

<!-- section_id: "adc6e5fb-5cdc-4dd3-ab68-a3c995503172" -->
## Sources

- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)
- [AssemblyAI](https://www.assemblyai.com)
- [Picovoice](https://picovoice.ai)
- [DevOps School: Top 10 Speech-to-Text Tools](https://www.devopsschool.com/blog/top-10-speech-to-text-tools-in-2025-features-pros-cons-comparison/)
