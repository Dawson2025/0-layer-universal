---
resource_id: "ba1c94e4-1f8d-40ea-a825-51ecd5c27a0d"
resource_type: "output"
resource_name: "system_tts_fixes"
---
# System TTS Fixes Log

**Date**: 2026-02-23

## Fix 1: pathvalidate Missing Dependency

**Problem**: Piper 1.4.1 via pipx fails on launch with `ModuleNotFoundError: No module named 'pathvalidate'`
**Cause**: piper-tts pip package doesn't declare pathvalidate as a dependency
**Fix**: `pipx inject piper-tts pathvalidate`
**Status**: Fixed

## No Other Fixes Required

Initial setup worked after the dependency fix. All tests pass.
