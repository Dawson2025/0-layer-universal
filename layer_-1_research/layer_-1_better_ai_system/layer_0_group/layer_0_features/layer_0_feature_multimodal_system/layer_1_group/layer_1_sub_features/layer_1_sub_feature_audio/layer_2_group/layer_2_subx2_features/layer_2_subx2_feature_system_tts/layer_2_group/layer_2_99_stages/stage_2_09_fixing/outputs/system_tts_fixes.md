# System TTS Fixes Log

**Date**: 2026-02-23

## Fix 1: pathvalidate Missing Dependency

**Problem**: Piper 1.4.1 via pipx fails on launch with `ModuleNotFoundError: No module named 'pathvalidate'`
**Cause**: piper-tts pip package doesn't declare pathvalidate as a dependency
**Fix**: `pipx inject piper-tts pathvalidate`
**Status**: Fixed

## No Other Fixes Required

Initial setup worked after the dependency fix. All tests pass.
