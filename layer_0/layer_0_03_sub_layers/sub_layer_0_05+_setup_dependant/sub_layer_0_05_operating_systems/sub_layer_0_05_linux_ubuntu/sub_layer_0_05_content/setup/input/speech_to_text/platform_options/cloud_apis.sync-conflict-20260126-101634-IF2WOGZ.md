# Cloud Speech-to-Text APIs

**Last Updated**: January 12, 2026
**Category**: Developer APIs for custom solutions

## Overview

These are cloud-based speech-to-text APIs for developers building custom solutions. They are **not** turnkey desktop dictation tools - they require integration work.

## When to Use These

| Use Case | Recommendation |
|----------|----------------|
| Need system-wide dictation now | Use [Vibe Typer](vibe_typer.md) or [Whisper-Dictation](whisper_dictation.md) |
| Building custom application | Consider these APIs |
| Need specific language support | Check API language coverage |
| Enterprise integration | These may fit better |

## Google Cloud Speech-to-Text

**Website**: [cloud.google.com/speech-to-text](https://cloud.google.com/speech-to-text)

| Aspect | Details |
|--------|---------|
| Accuracy | Highly accurate |
| Languages | 125+ languages and variants |
| Features | Real-time, batch, auto punctuation |
| Pricing | Pay per use (free tier available) |
| Integration | REST API, client libraries |

### Pros
- Extensive language support
- High accuracy
- Well-documented
- Multiple output formats

### Cons
- Requires cloud connection
- Pay per use after free tier
- No turnkey desktop UX
- Requires development work

## AssemblyAI

**Website**: [assemblyai.com](https://www.assemblyai.com)

| Aspect | Details |
|--------|---------|
| Focus | Developer-friendly API |
| Features | Transcription, speaker diarization, summarization |
| Accuracy | Competitive with Google |
| Pricing | Pay per audio hour |

### Pros
- Easy to integrate
- Good documentation
- Additional AI features (summarization, etc.)

### Cons
- No desktop UX
- Cloud-only
- Requires development

## Picovoice

**Website**: [picovoice.ai](https://picovoice.ai)

| Aspect | Details |
|--------|---------|
| Focus | On-device voice AI |
| Features | Wake word, speech-to-text, intent recognition |
| Privacy | Can run fully on-device |
| Pricing | Free tier, paid plans |

### Pros
- On-device processing option
- Privacy-friendly
- Low latency

### Cons
- No system-wide desktop UX out of box
- Requires integration work

## Comparison

| API | Accuracy | Languages | On-device | Ease of Use |
|-----|----------|-----------|-----------|-------------|
| Google Cloud | Excellent | 125+ | No | Medium |
| AssemblyAI | Excellent | 20+ | No | Easy |
| Picovoice | Good | 10+ | Yes | Medium |

## For Most Users

If you just want system-wide dictation on Linux, skip these APIs and use:

1. **[Vibe Typer](vibe_typer.md)** - Easiest setup, cloud processing
2. **[Whisper-Dictation](whisper_dictation.md)** - Local processing, privacy
3. **[OpenWhispr](openwhispr.md)** - Cross-platform, open source

These APIs are for developers building custom voice applications, not end-users wanting dictation.

## Sources

- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)
- [AssemblyAI](https://www.assemblyai.com)
- [Picovoice](https://picovoice.ai)
- [DevOps School: Top 10 Speech-to-Text Tools](https://www.devopsschool.com/blog/top-10-speech-to-text-tools-in-2025-features-pros-cons-comparison/)
