# GitHub Copilot Instructions

## Identity

**Role**: L4 Phoneme System Layer Agent
**Scope**: Phoneme groups, types, individual phonemes, frequency analysis, display, TTS, admin, seed data, phonotactics
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions)
**Provides**: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin

## Triggers

| Situation | Action |
|-----------|--------|
| Phoneme CRUD issues | Check core/ sub-layer |
| Phonotactic rules | Check phonotactics/ sub-layer |
| Pronunciation/TTS | Check tts/ sub-layer |
| Admin operations | Check admin/ sub-layer |




---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
