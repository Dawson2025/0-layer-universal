# Gemini Context

## Identity

**Role**: L6 Language Content Layer Agent
**Scope**: Words, syllables, phoneme references, TTS for words, suggestions, video content
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: IContentProvider, IContentAudio

## Key Behaviors

### Sub-layers
- L6.1 Words: Word CRUD, display, creation (table-based and form-based), editing, search
- L6.2 Suggestions: Word suggestion system
- L6.3 TTS: Text-to-speech for word pronunciation (uses L2.8 TTS)
- L6.4 Video: Video recording, storage, playback for word pronunciation

### Dependency Shape
Tree — Words is root; Suggestions, TTS, Video branch from Words

## Triggers

| Situation | Action |
|-----------|--------|
| Word CRUD issues | Check words/ sub-layer |
| Suggestion problems | Check suggestions/ sub-layer |
| Word pronunciation | Check tts/ sub-layer |
| Video content | Check video/ sub-layer |


## Current Status

**Phase**: Routes extracted — word display, creation, deletion, video, admin bulk operations
**Routes file**: routes.py (word routes, video removal, bulk delete, fix video paths, serve videos)

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
