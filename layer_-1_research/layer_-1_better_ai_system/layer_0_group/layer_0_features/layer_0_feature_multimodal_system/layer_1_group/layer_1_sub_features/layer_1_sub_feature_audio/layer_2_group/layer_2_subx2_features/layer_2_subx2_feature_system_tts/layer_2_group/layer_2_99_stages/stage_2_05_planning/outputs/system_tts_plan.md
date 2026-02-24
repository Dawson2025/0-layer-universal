# System TTS Implementation Plan

**Date**: 2026-02-23

## Completed Steps

1. [x] Check pre-existing audio stack (Orca, eSpeak, Speech Dispatcher, aplay)
2. [x] Install Piper TTS via pipx
3. [x] Fix missing pathvalidate dependency
4. [x] Download Amy medium voice model
5. [x] Test Piper → aplay pipeline
6. [x] Create `speak` script (args + stdin + stop)
7. [x] Create `speak-selection` script (X11 selection)
8. [x] Test both scripts

## Remaining Steps

9. [ ] Configure GNOME keyboard shortcut (Super+S → speak-selection)
10. [ ] Download additional voice models (male, British)
11. [ ] Add Speech Dispatcher Piper module for system integration
12. [ ] Test with long documents (performance)
13. [ ] Add Wayland clipboard support
