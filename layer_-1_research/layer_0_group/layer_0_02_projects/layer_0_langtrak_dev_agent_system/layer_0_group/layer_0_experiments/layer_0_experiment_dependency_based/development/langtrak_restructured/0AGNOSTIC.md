---
resource_id: "7fcc9368-26ec-45f6-b70f-31c889622423"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

entity_id: "7d7217a2-0afa-4559-bd77-d01174ac0276"

**Role**: LangTrak Restructured Application Manager
**Scope**: Dependency-based 7-layer architecture for LangTrak language tracking platform
**Architecture**: L2 Infrastructure → L3 Users → L4 Phonemes → L5 Templates → L6 Content → L7 Projects → L8 Teams

## Key Behaviors

### Layer Dependency Chain
- L2 Infrastructure: Foundation — app factory, database, Firebase, storage, auth, TTS. No dependencies.
- L3 Users: User model, profiles, sessions. Depends on L2.
- L4 Phoneme System: Phoneme groups, types, frequency, display, admin, seed, phonotactics. Depends on L2, L3.
- L5 Templates: Template core, phoneme selection, application, admin. Depends on L2, L3, L4.
- L6 Language Content: Words, syllables, TTS, suggestions, video. Depends on L2, L3, L4.
- L7 Projects: Project core, dashboard, navigation, variants, storage type. Depends on L2, L3, L5, L6.
- L8 Teams: Team model, membership, invites, project sharing. Depends on L2, L3, L7.

### Cross-Cutting Concerns (Absorbed)
- Firebase Sync: Absorbed into L2.7 (Firebase Sync sub-layer)
- Admin/Management: Absorbed into each layer's admin sub-layer
- Orchestration: Absorbed into L7 Projects (dashboard) and app factory

### Context Propagation
Each layer has its own 0AGNOSTIC.md with static/dynamic context. Context cascades:
- Root 0AGNOSTIC.md (this file) provides system-wide context
- Layer 0AGNOSTIC.md provides layer-specific context
- Stage 0AGNOSTIC.md provides stage-specific context within each layer

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

## Current Status

**Phase**: Restructuring — monolithic app.py decomposed into 7 layer blueprints
**Blueprint registration**: app.py factory registers l2_bp through l8_bp in dependency order
**Route extraction**: All 92 routes extracted from monolithic app.py into layer-specific routes.py files
**Next steps**: Fix imports, test, integrate layer-stage system fully

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

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

## Deferred Components

Components not yet integrated into the layer architecture:
- `deferred/firebase_orchestration/` — Firebase-specific orchestration system
- `deferred/universal_orchestration/` — Universal orchestration engine
- `deferred/meta_intelligent_orchestration/` — Meta-decision and adaptive learning system

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
