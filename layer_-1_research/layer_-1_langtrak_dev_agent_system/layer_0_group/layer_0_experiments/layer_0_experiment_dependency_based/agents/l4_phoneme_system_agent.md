# L4 Phoneme System Agent

**Role**: Phoneme Domain Specialist
**Class**: PhonemeSystemAgent (extends LayerAgent)
**Layer**: 4
**Provides**: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin
**Depends On**: IUserProvider (from L3)

---

## Sub-Layers (7)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L4.1 | Phoneme Groups | — | Categories: vowels, consonants, clicks, tones |
| L4.2 | Phoneme Types | L4.1 | Subcategories: stops, fricatives, nasals |
| L4.3 | Individual Phonemes | L4.2 | Atomic sound units: /p/, /b/, /m/ with IPA |
| L4.4 | Frequency Tracking | L4.3 | Usage statistics per phoneme |
| L4.5 | Phoneme Display | L4.3 | Hierarchy views, browsing UI |
| L4.6 | TTS for Phonemes | L4.3 | Audio generation for individual sounds (absorbed from L9) |
| L4.7 | Phoneme Admin | L4.1, L4.2, L4.3 | Admin CRUD for groups, types, phonemes (absorbed from L10) |

## Internal Dependency Shape: Sequence + Branches

```
L4.1 Groups → L4.2 Types → L4.3 Phonemes
                                 |
                    ┌────────────┼────────────┐
               L4.4 Frequency  L4.5 Display  L4.6 TTS

               L4.7 Admin (depends on L4.1 + L4.2 + L4.3)
```

## Context Model (~700 tokens)

### STATIC
- Layer identity, sub-layer list, dependency shape
- IPhonemeProvider (4 methods), IPhonemeAudio (2 methods)
- IFrequencyProvider (2 methods), IPhonemeAdmin (4 methods)
- Neighbor interface: IUserProvider (3 methods)

### ON-DEMAND
- Phoneme group/type/individual schemas
- IPA symbol mappings
- TTS implementation details
- Frequency calculation logic

## Scope Boundaries

**In scope**: All phoneme data, phoneme audio, frequency stats, phoneme admin
**Out of scope**: Templates (→ L5), word content (→ L6), user identity (→ L3)

## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| TTS for phonemes (was L9) | L4.6 | Phoneme-level audio is a phoneme feature |
| Phoneme Admin (was L10) | L4.7 | Managing phonemes is a phoneme task |
