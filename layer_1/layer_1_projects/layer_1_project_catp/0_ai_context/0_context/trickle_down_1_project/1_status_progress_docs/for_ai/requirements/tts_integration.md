---
resource_id: "f8b19608-a6af-4d96-b83e-587aca915941"
resource_type: "document"
resource_name: "tts_integration"
---
# Text-to-Speech Integration

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 2957-3078, `tts_ipa.py`, Azure Cognitive Services

<!-- section_id: "16f6ef69-869f-4343-a6cd-c4360b42eb6d" -->
## Goal
Provide audible pronunciation feedback for IPA phonemes and constructed words using text-to-speech technology, enabling users to hear how phonemes and words should sound during creation and study.

<!-- section_id: "352b54d1-c740-4a16-8e38-ad015618b787" -->
## Functional Requirements
- Integrate Azure Cognitive Services Speech SDK to convert IPA phonemes into audio playback.
- Provide API endpoints for single phoneme pronunciation and multi-phoneme word synthesis.
- Support preview requests for individual syllables inside multi-syllable words as well as full-word playback.
- Support checking individual phoneme pronounceability before attempting full word synthesis.
- Return audio status (success, failure, unsupported phoneme) with clear error messaging.
- Handle Azure API unavailability gracefully by returning informative status without crashing.
- Cache or stream audio to minimize API calls and latency during interactive use.
- Expose TTS status endpoint to verify Azure connectivity and service health.

<!-- section_id: "18b00a01-4c1f-4d90-bbfb-22480d06e577" -->
## Acceptance Criteria
- Requesting `/api/tts/phoneme` with an IPA symbol triggers Azure TTS and returns success/failure status.
- Requesting `/api/tts/ipa` with a phoneme sequence synthesizes the full word pronunciation.
- Expanded TTS API accepts syllable-scoped payloads so UI components can play each syllable independently while assembling multi-syllable words.
- API endpoint `/api/phonemes/check-single` validates whether a given phoneme is supported by Azure TTS.
- TTS status endpoint (`/api/tts/status`) reports whether Azure Speech Services are available and configured.
- Unsupported or malformed phonemes return clear error messages without blocking word creation.
- Audio playback integrates into the word creation and phoneme exploration interfaces.
- When Azure credentials are missing or invalid, TTS gracefully degrades without affecting other app features.

<!-- section_id: "8c86c8a2-c872-413f-b3bc-89073443861c" -->
## UI Flows Verified
- Create Word (table-based) page: phoneme cell click plays individual phoneme; unified display supports full-word click and individual syllable block click; double-click/hold triggers per-phoneme sequence playback.
- Optional X-SAMPA input: conversion to IPA and playback via a single Play control.
- Words list/detail: verify presence of phonetic values; TTS controls are exercised where present in the current UI.

<!-- section_id: "7623f5d3-db71-42e5-b1bb-3eaa892cd54f" -->
## Automation Mapping
- Playwright MCP flows:
  - `scripts/mcp-tts-experience.mjs` — exercises phoneme playback, syllable/full-word playback (when available), and `/api/tts/status`.
  - `scripts/mcp-words-flow.mjs` — creates words via API and visits UI to snapshot phonetics; used as a supporting flow.
- Running headless (recommended for CI):
  - Start MCP: `npm run mcp:playwright` (Chromium headless on port 9234)
  - Run flow: `MCP_URL=http://127.0.0.1:9234/mcp node scripts/mcp-tts-experience.mjs`
- Running headed (local debugging):
  - Start MCP: `npm run mcp:playwright:headed`
  - Run flow: `MCP_URL=http://127.0.0.1:9234/mcp node scripts/mcp-tts-experience.mjs`

<!-- section_id: "0c18c0b8-7145-4d0f-ab33-0b54272f0b36" -->
## Notes
- Azure Speech SDK requires valid subscription key and region configuration via environment variables or config.
- IPA symbols may not all be supported by Azure's TTS engine; unsupported phonemes should be documented.
- Consider fallback TTS engines (Google Cloud, AWS Polly) for broader phoneme coverage.
- Future enhancements could include custom voice selection, speed/pitch adjustment, or downloadable audio files.
- Audio caching could significantly improve performance and reduce Azure API costs.
