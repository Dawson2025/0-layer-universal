---
resource_id: "1e176ffa-1d49-4aa5-9633-42471e5651b4"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

entity_id: "378da9b4-0a65-4467-8869-9bc3fa8717b4"

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

# ── Current Status ──

## Current Status

**Phase**: Routes extracted — word display, creation, deletion, video, admin bulk operations
**Routes file**: routes.py (word routes, video removal, bulk delete, fix video paths, serve videos)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Words module | words/ |
| Parent context | ../0AGNOSTIC.md |
