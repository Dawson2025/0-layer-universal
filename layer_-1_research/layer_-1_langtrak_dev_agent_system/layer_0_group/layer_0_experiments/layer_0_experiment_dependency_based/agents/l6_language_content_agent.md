# L6 Language Content Agent

**Role**: Language Content Layer Specialist
**Class**: LanguageContentAgent (extends LayerAgent)
**Layer**: 6
**Provides**: IContentProvider, IContentAudio
**Depends On**: ITemplateProvider (from L5), IPhonemeAudio (from L4)

---

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

## Internal Dependency Shape: Containment Sequence + Branches

```
L6.1 Words → L6.2 Syllables → L6.3 Positions → L6.4 Phoneme Refs
                                                       |
                                              ┌────────┼────────┐
                                         L6.5 TTS  L6.6 Suggest  L6.7 Video
```

## Context Model (~700 tokens)

### STATIC
- Layer identity, sub-layer list, dependency shape
- IContentProvider (4 methods), IContentAudio (2 methods)
- Neighbor interfaces: ITemplateProvider (3 methods), IPhonemeAudio (2 methods)

### ON-DEMAND
- Word/syllable/position model schemas
- Phoneme reference resolution logic
- TTS concatenation algorithm
- Phonotactic rules engine
- Video upload/playback implementation

## Scope Boundaries

**In scope**: Words, syllables, positions, phoneme references, word TTS, suggestions, video
**Out of scope**: Phoneme data (→ L4), templates (→ L5), projects (→ L7)

## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| TTS for words/syllables (was L9) | L6.5 | Word-level audio is a content feature |
| Word Suggestions (was L9) | L6.6 | Suggestions are a content creation tool |
| Video (was L9) | L6.7 | Pronunciation video is content enrichment |
