---
resource_id: "ba1c94e4-1f8d-40ea-a825-51ecd5c27a0d"
resource_type: "output"
resource_name: "system_tts_fixes"
---
# System TTS Fixes Log

**Date**: 2026-02-23

<!-- section_id: "29d0923b-20b4-437e-b3a4-d1b6e938cbab" -->
## Fix 1: pathvalidate Missing Dependency

**Problem**: Piper 1.4.1 via pipx fails on launch with `ModuleNotFoundError: No module named 'pathvalidate'`
**Cause**: piper-tts pip package doesn't declare pathvalidate as a dependency
**Fix**: `pipx inject piper-tts pathvalidate`
**Status**: Fixed

<!-- section_id: "5693ee07-27df-490f-8f96-362ace71c942" -->
## No Other Fixes Required

Initial setup worked after the dependency fix. All tests pass.
