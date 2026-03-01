# System TTS Criticism / Review

**Date**: 2026-02-23

## What Works Well

- Piper produces natural-sounding speech, significantly better than eSpeak
- Simple pipeline design (echo | piper | aplay) is easy to understand and debug
- PID-based toggle is intuitive — same hotkey to start/stop
- Scripts are self-contained with no external service dependencies

## Issues and Gaps

1. **No speech queue**: New speech kills old speech. If you select new text while speech is playing, you lose the previous. Consider a queue or "finish then play next" mode.

2. **No visual feedback**: User has no way to know if speech is playing or stopped without listening. A tray icon or notification would help.

3. **Fixed voice**: Only Amy medium is available. No voice switching, no speed/pitch control exposed via CLI flags.

4. **Startup latency**: ~0.5s model loading on each invocation. Consider a Piper daemon that keeps the model warm in memory.

5. **No sentence-level control**: Can't pause/resume, skip forward, or repeat. Only start and stop.

6. **X11 only**: wl-paste not integrated, so Wayland users would need modification.

7. **No text preprocessing**: No handling of abbreviations, numbers, URLs, or code in the selected text. Piper reads them literally.

## Recommendations

- **Priority 1**: Configure the GNOME hotkey to make it usable day-to-day
- **Priority 2**: Add `--voice` and `--speed` flags to the speak script
- **Priority 3**: Investigate piper-daemon or HTTP server for warm model
- **Priority 4**: Add notification feedback (notify-send on start/stop)
