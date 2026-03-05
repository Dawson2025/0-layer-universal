---
resource_id: "5863407e-9d2c-4cf8-9ae4-0aac12651b7a"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "cefbfe75-70f8-440a-b46a-128469db8560" -->
## Identity

**Role**: L6 Language Content Layer Agent
**Scope**: Words, syllables, phoneme references, TTS for words, suggestions, video content
**Depends On**: L2 Infrastructure (auth, firebase, storage, TTS), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: IContentProvider, IContentAudio

<!-- section_id: "bc4f9776-a306-489e-89d0-498d022cdd8a" -->
## Key Behaviors

<!-- section_id: "95e12cdd-1be3-4f31-8182-5604546cd324" -->
### Sub-layers
- L6.1 Words: Word CRUD, display, creation (table-based and form-based), editing, search
- L6.2 Suggestions: Word suggestion system
- L6.3 TTS: Text-to-speech for word pronunciation (uses L2.8 TTS)
- L6.4 Video: Video recording, storage, playback for word pronunciation

<!-- section_id: "60c8c087-8505-4475-a0d1-ad86fa2dad73" -->
### Dependency Shape
Tree — Words is root; Suggestions, TTS, Video branch from Words

<!-- section_id: "3529272b-d771-4c54-860b-5bec7b26bac2" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Word CRUD issues | Check words/ sub-layer |
| Suggestion problems | Check suggestions/ sub-layer |
| Word pronunciation | Check tts/ sub-layer |
| Video content | Check video/ sub-layer |


<!-- section_id: "ff95b9ff-ce79-444b-b54b-ca032e0cacb5" -->
## Current Status

**Phase**: Routes extracted — word display, creation, deletion, video, admin bulk operations
**Routes file**: routes.py (word routes, video removal, bulk delete, fix video paths, serve videos)

<!-- section_id: "822ad590-28ec-482c-842c-a214d507df89" -->
## AutoGen-Specific Configuration

<!-- section_id: "950cf9eb-24fe-4dcc-849a-8342acde1263" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "a440da2c-9f58-4be1-b372-2222fac41000" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
