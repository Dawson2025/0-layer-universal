---
resource_id: "88cdfa13-db22-4818-801d-fc5825414872"
resource_type: "output"
resource_name: "agentic_tts_criticism"
---
# Agentic TTS Criticism / Review

**Date**: 2026-02-23

<!-- section_id: "ca9ef13a-08b7-4293-b8ff-aa41a694af96" -->
## What Works Well

- Simple hook architecture — single bash script, no daemon
- Reuses Piper infrastructure from system TTS
- Background execution prevents blocking Claude
- JSON extraction via jq is clean and reliable
- Coexists with completion sound hook

<!-- section_id: "30e3979b-545e-4f53-8641-7dc9fa9e25f3" -->
## Issues and Gaps

1. **No spoken_summary field**: Claude doesn't emit TTS-optimized text. The hook must guess what's important by truncating to 600 chars. A split-output pattern where Claude provides a `spoken_summary` would be much better.

2. **Crude text cleanup**: sed-based markdown stripping is fragile. Complex responses with nested formatting, lists, or mixed content may produce awkward speech. A proper markdown-to-plaintext tool would be better.

3. **Fixed truncation**: 600 chars may be too short for complex explanations or too long for simple confirmations. Should be adaptive based on response type.

4. **No context awareness**: The hook doesn't know if the response is an error, a question, a file listing, or a narrative. All are treated the same.

5. **Single hook event**: Only Stop is hooked. Long-running operations (builds, tests, large file writes) give no audio feedback until Claude's full turn ends.

6. **No user control**: No way to disable TTS for specific responses without editing settings.json. A `--quiet` flag or environment variable would help.

<!-- section_id: "a08b3adf-5df8-40e3-b7a8-b0ffaa702a6b" -->
## Recommendations

- **Priority 1**: Live test and tune truncation length
- **Priority 2**: Add PostToolUse hooks for long operations
- **Priority 3**: Investigate split-output pattern for Claude
- **Priority 4**: Replace sed chain with a proper markdown-to-text tool (pandoc or python)
