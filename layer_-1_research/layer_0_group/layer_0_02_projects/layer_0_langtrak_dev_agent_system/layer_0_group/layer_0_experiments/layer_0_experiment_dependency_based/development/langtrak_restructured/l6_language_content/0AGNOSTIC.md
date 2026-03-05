---
resource_id: "1e176ffa-1d49-4aa5-9633-42471e5651b4"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "77e05173-f6dc-4cfd-abc1-0c1de275b599" -->
## Identity

entity_id: "378da9b4-0a65-4467-8869-9bc3fa8717b4"

**Role**: L6 Language Content Layer Agent
**Scope**: Words, syllables, phoneme references, TTS for words, suggestions, video content
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: IContentProvider, IContentAudio

<!-- section_id: "5a22a60f-62f0-4021-aaae-a1ee357a9db0" -->
## Key Behaviors

<!-- section_id: "212a5828-925a-43cc-8fbe-b2c6c02152b8" -->
### Sub-layers
- L6.1 Words: Word CRUD, display, creation (table-based and form-based), editing, search
- L6.2 Suggestions: Word suggestion system
- L6.3 TTS: Text-to-speech for word pronunciation (uses L2.8 TTS)
- L6.4 Video: Video recording, storage, playback for word pronunciation

<!-- section_id: "02ba2fbf-89e0-438a-bff3-bb7d1ce5aea6" -->
### Dependency Shape
Tree — Words is root; Suggestions, TTS, Video branch from Words

<!-- section_id: "32413b8e-3465-4d4e-b3c0-d2a57c514ded" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Word CRUD issues | Check words/ sub-layer |
| Suggestion problems | Check suggestions/ sub-layer |
| Word pronunciation | Check tts/ sub-layer |
| Video content | Check video/ sub-layer |

# ── Current Status ──

<!-- section_id: "a0b3706e-ad32-4e54-ad71-cc1a96135574" -->
## Current Status

**Phase**: Routes extracted — word display, creation, deletion, video, admin bulk operations
**Routes file**: routes.py (word routes, video removal, bulk delete, fix video paths, serve videos)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "7197682c-f3ee-4ac8-a05a-5ec07ed62eac" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Words module | words/ |
| Parent context | ../0AGNOSTIC.md |
