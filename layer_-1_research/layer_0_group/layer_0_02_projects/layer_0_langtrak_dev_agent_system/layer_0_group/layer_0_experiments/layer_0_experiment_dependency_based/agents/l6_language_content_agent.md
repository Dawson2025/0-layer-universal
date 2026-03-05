---
resource_id: "056b318e-fb88-485d-b8e4-4ef1400f188d"
resource_type: "document"
resource_name: "l6_language_content_agent"
---
# L6 Language Content Agent

**Role**: Language Content Layer Specialist
**Class**: LanguageContentAgent (extends LayerAgent)
**Layer**: 6
**Provides**: IContentProvider, IContentAudio
**Depends On**: ITemplateProvider (from L5), IPhonemeAudio (from L4)

---

<!-- section_id: "e0baa0bd-2370-49fe-8508-37312db4b012" -->
## Sub-Layers (7)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L6.1 | Words | — | Word creation, display, editing, search |
| L6.2 | Syllables | L6.1 | Multi-syllable structure within words |
| L6.3 | Positions | L6.2 | Onset/nucleus/coda slots within syllables |
| L6.4 | Phoneme References | L6.3 | Phoneme assignments in positions (links to L4 via L5) |
| L6.5 | TTS for Content | L6.4 | Audio for syllables and words (absorbed from L9) |
| L6.6 | Word Suggestions | L6.4 | Phonotactic rule-based word generation (absorbed from L9) |
| L6.7 | Video | L6.1 | Video upload/playback for pronunciation (absorbed from L9) |

<!-- section_id: "f2125e73-b796-42af-91e4-11ae80b62da6" -->
## Internal Dependency Shape: Containment Sequence + Branches

```
L6.1 Words → L6.2 Syllables → L6.3 Positions → L6.4 Phoneme Refs
                                                       |
                                              ┌────────┼────────┐
                                         L6.5 TTS  L6.6 Suggest  L6.7 Video
```

<!-- section_id: "f309de6e-141e-45c0-bd3a-dc3abd7d73ef" -->
## Context Model (~700 tokens)

<!-- section_id: "5cffa7e6-de6d-4cf0-a252-6aeb2d66b605" -->
### STATIC
- Layer identity, sub-layer list, dependency shape
- IContentProvider (4 methods), IContentAudio (2 methods)
- Neighbor interfaces: ITemplateProvider (3 methods), IPhonemeAudio (2 methods)

<!-- section_id: "0b98d9bf-45d0-46ba-b4e1-8ae265bfefe3" -->
### ON-DEMAND
- Word/syllable/position model schemas
- Phoneme reference resolution logic
- TTS concatenation algorithm
- Phonotactic rules engine
- Video upload/playback implementation

<!-- section_id: "2f0655a0-4b54-4dd9-a643-c5e0237f2277" -->
## Scope Boundaries

**In scope**: Words, syllables, positions, phoneme references, word TTS, suggestions, video
**Out of scope**: Phoneme data (→ L4), templates (→ L5), projects (→ L7)

<!-- section_id: "ec5c8679-a414-45d6-9ae6-f60ad067deba" -->
## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| TTS for words/syllables (was L9) | L6.5 | Word-level audio is a content feature |
| Word Suggestions (was L9) | L6.6 | Suggestions are a content creation tool |
| Video (was L9) | L6.7 | Pronunciation video is content enrichment |
