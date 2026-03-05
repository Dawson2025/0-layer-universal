---
resource_id: "b6970a54-8971-4fcd-97f0-567337d95127"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "abb0e773-c838-4116-a6f1-d91313b940bb" -->
## Identity

entity_id: "e39ab9de-988c-4fa9-b045-d0b8c8a78ea0"

**Role**: L4 Phoneme System Layer Agent
**Scope**: Phoneme groups, types, individual phonemes, frequency analysis, display, TTS, admin, seed data, phonotactics
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions)
**Provides**: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin

<!-- section_id: "a8997038-19b1-4140-b31a-2dab66fdac2e" -->
## Key Behaviors

<!-- section_id: "186f0cc1-a458-4c58-9d95-ac9248dd0d56" -->
### Sub-layers
- L4.1 Core: Phoneme CRUD, group/type management, display logic
- L4.2 Phonotactics: Phonotactic rules engine, constraint validation
- L4.3 TTS: Text-to-speech for phoneme pronunciation (uses L2.8 TTS)
- L4.4 Admin: Phoneme administration, bulk operations, frequency management
- L4.5 Seed: Default phoneme data, IPA standard sets
- L4.6 Display: Phoneme display views (nested, flat, full)
- L4.7 Frequency: Phoneme usage frequency calculation and tracking

<!-- section_id: "be41b189-3b49-4d54-bcdf-4c7182c58207" -->
### Dependency Shape
DAG — Core is shared foundation; Admin, Display, Frequency depend on Core; TTS and Phonotactics are independent

<!-- section_id: "0cc30899-00dd-4eaf-9be9-f8047f749661" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Phoneme CRUD issues | Check core/ sub-layer |
| Phonotactic rules | Check phonotactics/ sub-layer |
| Pronunciation/TTS | Check tts/ sub-layer |
| Admin operations | Check admin/ sub-layer |

# ── Current Status ──

<!-- section_id: "93709717-6b87-42f7-92a5-a2bb7395674a" -->
## Current Status

**Phase**: Routes extracted — all phoneme display, admin, and API routes
**Routes file**: routes.py (phoneme display, admin, frequency, single-check routes)
**Key modules**: core/ (phonemes_bp), admin/, phonotactics/, seed/

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "5e4f52c0-bc14-4244-af6e-7450f2464a24" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Core module | core/ |
| Phonotactics | phonotactics/ |
| Parent context | ../0AGNOSTIC.md |
