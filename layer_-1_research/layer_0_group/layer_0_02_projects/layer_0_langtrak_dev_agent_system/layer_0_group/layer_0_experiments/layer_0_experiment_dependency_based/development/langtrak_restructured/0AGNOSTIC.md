---
resource_id: "7fcc9368-26ec-45f6-b70f-31c889622423"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "b3cfb09f-c421-4e62-a358-80701e6b9680" -->
## Identity

entity_id: "7d7217a2-0afa-4559-bd77-d01174ac0276"

**Role**: LangTrak Restructured Application Manager
**Scope**: Dependency-based 7-layer architecture for LangTrak language tracking platform
**Architecture**: L2 Infrastructure → L3 Users → L4 Phonemes → L5 Templates → L6 Content → L7 Projects → L8 Teams

<!-- section_id: "fdf53077-c6c1-40bb-8a99-294dcf6d50ef" -->
## Key Behaviors

<!-- section_id: "927705b5-038c-4720-8004-47a527d9fe39" -->
### Layer Dependency Chain
- L2 Infrastructure: Foundation — app factory, database, Firebase, storage, auth, TTS. No dependencies.
- L3 Users: User model, profiles, sessions. Depends on L2.
- L4 Phoneme System: Phoneme groups, types, frequency, display, admin, seed, phonotactics. Depends on L2, L3.
- L5 Templates: Template core, phoneme selection, application, admin. Depends on L2, L3, L4.
- L6 Language Content: Words, syllables, TTS, suggestions, video. Depends on L2, L3, L4.
- L7 Projects: Project core, dashboard, navigation, variants, storage type. Depends on L2, L3, L5, L6.
- L8 Teams: Team model, membership, invites, project sharing. Depends on L2, L3, L7.

<!-- section_id: "11733e67-9b0b-4d85-844a-163d782becea" -->
### Cross-Cutting Concerns (Absorbed)
- Firebase Sync: Absorbed into L2.7 (Firebase Sync sub-layer)
- Admin/Management: Absorbed into each layer's admin sub-layer
- Orchestration: Absorbed into L7 Projects (dashboard) and app factory

<!-- section_id: "021dc8b5-3bcd-44e8-a29b-1eeca33ad88b" -->
### Context Propagation
Each layer has its own 0AGNOSTIC.md with static/dynamic context. Context cascades:
- Root 0AGNOSTIC.md (this file) provides system-wide context
- Layer 0AGNOSTIC.md provides layer-specific context
- Stage 0AGNOSTIC.md provides stage-specific context within each layer

<!-- section_id: "77393f5d-ecce-41a2-a8c1-b620e5dc23ba" -->
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

<!-- section_id: "f99fc886-9baa-4dfe-977e-a5c9e0041a84" -->
## Interfaces

12 segregated interfaces define the contracts between layers:
- IStorageProvider, IAuthProvider (L2)
- IUserProvider (L3)
- IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin (L4)
- ITemplateProvider (L5)
- IContentProvider, IContentAudio (L6)
- IProjectProvider (L7)
- ICollaborationProvider (L8)

# ── Current Status ──

<!-- section_id: "4592d9f0-e025-446f-9409-0ac417cc81ce" -->
## Current Status

**Phase**: Restructuring — monolithic app.py decomposed into 7 layer blueprints
**Blueprint registration**: app.py factory registers l2_bp through l8_bp in dependency order
**Route extraction**: All 92 routes extracted from monolithic app.py into layer-specific routes.py files
**Next steps**: Fix imports, test, integrate layer-stage system fully

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "09bb8033-b283-40b2-b145-f4d74efd0330" -->
## Layer Details

| Layer | Blueprint | Routes File | Sub-layers |
|-------|-----------|-------------|------------|
| L2 Infrastructure | l2_bp | l2_infrastructure/routes.py | app_factory, database, firebase, storage, auth, db_admin, firebase_sync, tts, api_gateway |
| L3 Users | l3_bp | l3_users/routes.py | model, profiles, sessions |
| L4 Phoneme System | l4_bp | l4_phoneme_system/routes.py | core, phonotactics, tts, admin, seed, display, frequency |
| L5 Templates | l5_bp | l5_templates/routes.py | core, admin |
| L6 Language Content | l6_bp | l6_language_content/routes.py | words, suggestions, tts, video |
| L7 Projects | l7_bp | l7_projects/routes.py | core, dashboard, navigation, variants, storage_type |
| L8 Teams | l8_bp | l8_teams/routes.py | core, membership, invites, project_sharing |

<!-- section_id: "99bd3456-2611-4baf-832f-0b2c0378cb49" -->
## Deferred Components

Components not yet integrated into the layer architecture:
- `deferred/firebase_orchestration/` — Firebase-specific orchestration system
- `deferred/universal_orchestration/` — Universal orchestration engine
- `deferred/meta_intelligent_orchestration/` — Meta-decision and adaptive learning system

<!-- section_id: "cf4c6c9e-012f-484b-ac81-a2ea97d190c7" -->
## Interface Dependency Map

```
L2 provides: IStorageProvider, IAuthProvider
     |
L3 uses: IStorageProvider, IAuthProvider
L3 provides: IUserProvider
     |
L4 uses: IUserProvider
L4 provides: IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin
     |
L5 uses: IPhonemeProvider
L5 provides: ITemplateProvider
     |
L6 uses: ITemplateProvider, IPhonemeAudio
L6 provides: IContentProvider, IContentAudio
     |
L7 uses: IContentProvider
L7 provides: IProjectProvider
     |
L8 uses: IProjectProvider, IUserProvider (skip-link to L3)
L8 provides: ICollaborationProvider
```

# ── References ──

<!-- section_id: "ec27006a-4674-4411-ada9-268ff95de9a5" -->
## Navigation

| Resource | Path |
|----------|------|
| App Factory | app.py |
| Original Monolith | ../langtrak_original/app.py |
| Experiment Design | ../../README.md |
| Agent Definitions | ../../agents/ |
| Interface Definitions | ../../interfaces/interface_definitions.md |
| Deferred Components | deferred/ |
| Tests | tests/ |
| Configuration | config/ |
