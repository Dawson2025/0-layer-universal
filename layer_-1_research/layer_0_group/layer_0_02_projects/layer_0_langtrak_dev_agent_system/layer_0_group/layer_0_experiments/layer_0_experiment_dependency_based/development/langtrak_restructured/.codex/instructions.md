---
resource_id: "33ba5d8d-8223-43b2-a865-b788d7eef2bc"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "78c4d4eb-13fd-4dbe-908a-d9562eeafe78" -->
## Identity

**Role**: LangTrak Restructured Application Manager
**Scope**: Dependency-based 7-layer architecture for LangTrak language tracking platform
**Architecture**: L2 Infrastructure → L3 Users → L4 Phonemes → L5 Templates → L6 Content → L7 Projects → L8 Teams

<!-- section_id: "5eb377ad-06ee-4d30-afa9-fd79d3703bdd" -->
## Key Behaviors

<!-- section_id: "6e8399e5-3bc2-40f0-b404-21689c9639d7" -->
### Layer Dependency Chain
- L2 Infrastructure: Foundation — app factory, database, Firebase, storage, auth, TTS. No dependencies.
- L3 Users: User model, profiles, sessions. Depends on L2.
- L4 Phoneme System: Phoneme groups, types, frequency, display, admin, seed, phonotactics. Depends on L2, L3.
- L5 Templates: Template core, phoneme selection, application, admin. Depends on L2, L3, L4.
- L6 Language Content: Words, syllables, TTS, suggestions, video. Depends on L2, L3, L4.
- L7 Projects: Project core, dashboard, navigation, variants, storage type. Depends on L2, L3, L5, L6.
- L8 Teams: Team model, membership, invites, project sharing. Depends on L2, L3, L7.

<!-- section_id: "5ab46234-e02d-44b0-a403-18e65fd39970" -->
### Cross-Cutting Concerns (Absorbed)
- Firebase Sync: Absorbed into L2.7 (Firebase Sync sub-layer)
- Admin/Management: Absorbed into each layer's admin sub-layer
- Orchestration: Absorbed into L7 Projects (dashboard) and app factory

<!-- section_id: "83579885-7b95-403e-b500-c18856769483" -->
### Context Propagation
Each layer has its own 0AGNOSTIC.md with static/dynamic context. Context cascades:
- Root 0AGNOSTIC.md (this file) provides system-wide context
- Layer 0AGNOSTIC.md provides layer-specific context
- Stage 0AGNOSTIC.md provides stage-specific context within each layer

<!-- section_id: "64b87d67-bb84-47d4-a276-b3b8c48c21fc" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Working on infrastructure (auth, db, firebase) | Navigate to l2_infrastructure/ |
| Working on user features | Navigate to l3_users/ |
| Working on phoneme features | Navigate to l4_phoneme_system/ |
| Working on templates | Navigate to l5_templates/ |
| Working on words/content | Navigate to l6_language_content/ |
| Working on projects/dashboard | Navigate to l7_projects/ |
| Working on teams/collaboration | Navigate to l8_teams/ |

<!-- section_id: "e14a7ce2-fde1-461d-8ac3-272da637f77d" -->
## Interfaces

12 segregated interfaces define the contracts between layers:
- IStorageProvider, IAuthProvider (L2)
- IUserProvider (L3)
- IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin (L4)
- ITemplateProvider (L5)
- IContentProvider, IContentAudio (L6)
- IProjectProvider (L7)
- ICollaborationProvider (L8)


<!-- section_id: "4ae06006-613b-4356-be79-89caa3a9607c" -->
## Current Status

**Phase**: Restructuring — monolithic app.py decomposed into 7 layer blueprints
**Blueprint registration**: app.py factory registers l2_bp through l8_bp in dependency order
**Route extraction**: All 92 routes extracted from monolithic app.py into layer-specific routes.py files
**Next steps**: Fix imports, test, integrate layer-stage system fully

<!-- section_id: "b2f4c6eb-d30b-4bf2-a415-4c9f59547a5c" -->
## AutoGen-Specific Configuration

<!-- section_id: "dd609bfe-dc2d-49db-ba18-d746ea80ede6" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "0f6dfaa6-b119-4fb2-914b-4089864d9e99" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
