# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Role**: L4 Phoneme System Layer Agent
**Scope**: Phoneme groups, types, individual phonemes, frequency analysis, display, TTS, admin, seed data, phonotactics
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions)
**Provides**: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin

## Key Behaviors

### Sub-layers
- L4.1 Core: Phoneme CRUD, group/type management, display logic
- L4.2 Phonotactics: Phonotactic rules engine, constraint validation
- L4.3 TTS: Text-to-speech for phoneme pronunciation (uses L2.8 TTS)
- L4.4 Admin: Phoneme administration, bulk operations, frequency management
- L4.5 Seed: Default phoneme data, IPA standard sets
- L4.6 Display: Phoneme display views (nested, flat, full)
- L4.7 Frequency: Phoneme usage frequency calculation and tracking

### Dependency Shape
DAG — Core is shared foundation; Admin, Display, Frequency depend on Core; TTS and Phonotactics are independent

## Triggers

| Situation | Action |
|-----------|--------|
| Phoneme CRUD issues | Check core/ sub-layer |
| Phonotactic rules | Check phonotactics/ sub-layer |
| Pronunciation/TTS | Check tts/ sub-layer |
| Admin operations | Check admin/ sub-layer |

# ── Current Status ──

## Current Status

**Phase**: Routes extracted — all phoneme display, admin, and API routes
**Routes file**: routes.py (phoneme display, admin, frequency, single-check routes)
**Key modules**: core/ (phonemes_bp), admin/, phonotactics/, seed/

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Core module | core/ |
| Phonotactics | phonotactics/ |
| Parent context | ../0AGNOSTIC.md |
