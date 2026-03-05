---
resource_id: "67d175da-eb63-4ddf-849b-a15f1492031d"
resource_type: "output"
resource_name: "system_tts_criticism"
---
# System TTS Criticism / Review

**Date**: 2026-02-23

<!-- section_id: "0b90a4f8-83a6-4224-a5c4-8c9178f90a6b" -->
## What Works Well

- Piper produces natural-sounding speech, significantly better than eSpeak
- Simple pipeline design (echo | piper | aplay) is easy to understand and debug
- PID-based toggle is intuitive — same hotkey to start/stop
- Scripts are self-contained with no external service dependencies

<!-- section_id: "00b47f0f-f693-4599-aa3d-e9818902003b" -->
## Issues and Gaps

1. **No speech queue**: New speech kills old speech. If you select new text while speech is playing, you lose the previous. Consider a queue or "finish then play next" mode.

2. **No visual feedback**: User has no way to know if speech is playing or stopped without listening. A tray icon or notification would help.

3. **Fixed voice**: Only Amy medium is available. No voice switching, no speed/pitch control exposed via CLI flags.

4. **Startup latency**: ~0.5s model loading on each invocation. Consider a Piper daemon that keeps the model warm in memory.

5. **No sentence-level control**: Can't pause/resume, skip forward, or repeat. Only start and stop.

6. **X11 only**: wl-paste not integrated, so Wayland users would need modification.

7. **No text preprocessing**: No handling of abbreviations, numbers, URLs, or code in the selected text. Piper reads them literally.

<!-- section_id: "2ca03d89-f80b-47ba-b5dd-dc0021232813" -->
## Recommendations

- **Priority 1**: Configure the GNOME hotkey to make it usable day-to-day
- **Priority 2**: Add `--voice` and `--speed` flags to the speak script
- **Priority 3**: Investigate piper-daemon or HTTP server for warm model
- **Priority 4**: Add notification feedback (notify-send on start/stop)
