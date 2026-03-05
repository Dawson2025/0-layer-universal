<!-- derived_from: "7d7217a2-0afa-4559-bd77-d01174ac0276" -->
# Claude Code Context

## Identity

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


## Current Status

**Phase**: Restructuring — monolithic app.py decomposed into 7 layer blueprints
**Blueprint registration**: app.py factory registers l2_bp through l8_bp in dependency order
**Route extraction**: All 92 routes extracted from monolithic app.py into layer-specific routes.py files
**Next steps**: Fix imports, test, integrate layer-stage system fully

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
