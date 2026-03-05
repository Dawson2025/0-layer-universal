---
resource_id: "e009df1d-2c09-4b6d-be37-6d3d5d0374f7"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "14278c18-0ccb-4b3f-95fc-641159bcf528" -->
## Identity

**Role**: L4 Phoneme System Layer Agent
**Scope**: Phoneme groups, types, individual phonemes, frequency analysis, display, TTS, admin, seed data, phonotactics
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions)
**Provides**: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin

<!-- section_id: "57168853-1fdb-4e50-a66c-2261560803e7" -->
## Key Behaviors

<!-- section_id: "7751e82d-d7f4-4dc5-8920-2895031bb98a" -->
### Sub-layers
- L4.1 Core: Phoneme CRUD, group/type management, display logic
- L4.2 Phonotactics: Phonotactic rules engine, constraint validation
- L4.3 TTS: Text-to-speech for phoneme pronunciation (uses L2.8 TTS)
- L4.4 Admin: Phoneme administration, bulk operations, frequency management
- L4.5 Seed: Default phoneme data, IPA standard sets
- L4.6 Display: Phoneme display views (nested, flat, full)
- L4.7 Frequency: Phoneme usage frequency calculation and tracking

<!-- section_id: "023f0291-5a55-4693-9df0-77a48928f707" -->
### Dependency Shape
DAG — Core is shared foundation; Admin, Display, Frequency depend on Core; TTS and Phonotactics are independent

<!-- section_id: "bafaf6f2-e379-4a90-8ea5-a32d2f565448" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Phoneme CRUD issues | Check core/ sub-layer |
| Phonotactic rules | Check phonotactics/ sub-layer |
| Pronunciation/TTS | Check tts/ sub-layer |
| Admin operations | Check admin/ sub-layer |


<!-- section_id: "96c3a0aa-8f16-48dc-840d-40b0c8a5aca7" -->
## Current Status

**Phase**: Routes extracted — all phoneme display, admin, and API routes
**Routes file**: routes.py (phoneme display, admin, frequency, single-check routes)
**Key modules**: core/ (phonemes_bp), admin/, phonotactics/, seed/

<!-- section_id: "a92260d7-53b8-4d13-bf24-2555be39e645" -->
## AutoGen-Specific Configuration

<!-- section_id: "f120c67d-5d2e-4ed5-878a-dc49f004d907" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "bd5cd65b-a0e3-428f-be55-ab1944886900" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
