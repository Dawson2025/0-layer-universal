# Dependency-Based Agent Hierarchy Design

**Status**: DESIGN — Ready for experiment implementation
**Date**: 2026-02-26
**Companion research**: `../../stage_-1_02_research/outputs/by_topic/01_hierarchy_structural_ideas.md`, `02_sublayer_dependency_structures.md`, `03_oop_agent_hierarchy_patterns.md`
**Experiment trial**: Trial A (revised) in `agent_hierarchy_structure_experiment.md`

---

## Design Principle

**Dependency ordering with absorbed cross-cutting features.**

Every feature lives inside the layer it most naturally belongs to. There are no standalone "cross-cutting" layers. What were previously L9 (Enhancements), L10 (Admin), and L11 (Orchestration) are dissolved — their sub-features are absorbed into the domain layers they serve.

Within each layer, sub-layers are ordered by internal dependency — the same principle applied recursively.

### Why This Design

| Problem with the original L2-L11 flat chain | How this design solves it |
|---------------------------------------------|--------------------------|
| L9-L11 cross-cutting layers don't fit the linear chain | Eliminated — features absorbed into their parent domains |
| Cross-cutting agents need to bypass the relay chain | No bypass needed — TTS for phonemes is IN the phoneme layer |
| Admin tools manage multiple layers but sit at L10 | Admin tools split: DB admin → L2, phoneme admin → L4, project dashboard → L7 |
| The chain is 10 layers long with 3 awkward outliers | Now 7 clean layers (L2-L8) with richer internal structure |

---

## The Hierarchy

### Layer 2: Infrastructure

Everything the system needs to run. Without this, nothing works.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| App Factory | L2.1 | — | Flask `create_app()`, config loading, blueprint registration |
| Database | L2.2 | L2.1 | SQLite connection, schema, `db.session`, model base classes |
| Firebase | L2.3 | L2.1 | Firestore client, Firebase Auth SDK, cloud config |
| Storage Manager | L2.4 | L2.2, L2.3 | Unified local/cloud interface (`storage.save()`, `storage.load()`) |
| Auth System | L2.5 | L2.2, L2.4 | Login flows (email + Google OAuth), `@login_required`, `current_user` |
| DB Admin Tools | L2.6 | L2.2 | Database inspection, reset, migration tools (was L10) |
| Firebase Sync | L2.7 | L2.3, L2.4 | Cloud sync orchestration, real-time listeners (was L11) |

**Internal dependency shape**: DAG (diamond at Storage Manager, convergence at Auth)

```
         L2.1 App Factory
          /              \
   L2.2 Database    L2.3 Firebase
      |    \          /      |
      |   L2.4 Storage Mgr  |
      |        |             |
      |   L2.5 Auth          |
      |                      |
   L2.6 DB Admin       L2.7 Firebase Sync
```

**Public interface to L3**: Auth check API (`@login_required`, `current_user`), Storage API (`storage.save/load`), DB session

---

### Layer 3: Users

Identity within the system. Once authenticated (L2), everything is scoped to a user.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| User Model | L3.1 | — | `User` class, database table, core fields |
| Profiles | L3.2 | L3.1 | User preferences, display settings, avatar |
| Sessions | L3.3 | L3.1 | Session management, active session state |

**Internal dependency shape**: Sequence (simple)

```
L3.1 User Model → L3.2 Profiles → L3.3 Sessions
```

**Public interface to L4**: User identity (`current_user.id`), session context, user preferences

---

### Layer 4: Phoneme System

The universe of possible sounds. The most fundamental domain concept — every language feature depends on having a sound inventory.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| Phoneme Groups | L4.1 | — | Categories: vowels, consonants, clicks, tones, etc. |
| Phoneme Types | L4.2 | L4.1 | Subcategories within groups: stops, fricatives, nasals, etc. |
| Individual Phonemes | L4.3 | L4.2 | Atomic sound units: /p/, /b/, /m/, each with IPA symbol |
| Frequency Tracking | L4.4 | L4.3 | Usage statistics: how often each phoneme appears in content |
| Phoneme Display | L4.5 | L4.3 | Hierarchy views, nested display, browsing UI |
| TTS for Phonemes | L4.6 | L4.3 | Audio generation for individual phoneme sounds (was L9) |
| Phoneme Admin | L4.7 | L4.1, L4.2, L4.3 | Admin CRUD for groups, types, phonemes (was L10) |

**Internal dependency shape**: Sequence with trailing branches

```
L4.1 Groups → L4.2 Types → L4.3 Phonemes
                                 |
                    ┌────────────┼────────────┐
               L4.4 Frequency  L4.5 Display  L4.6 TTS

               L4.7 Admin (depends on L4.1 + L4.2 + L4.3)
```

**Public interface to L5**: Phoneme inventory API (query by group, type, or individual; get IPA symbol; get frequency; get audio)

---

### Layer 5: Templates

A user-selected view/filter of the full phoneme system. Defines which phonemes are available for a specific language project.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| Template Core | L5.1 | — | Template model, CRUD operations |
| Phoneme Selection | L5.2 | L5.1 | Choose subset of phonemes from L4 inventory |
| Template Application | L5.3 | L5.1 | Apply a template to a project (link template → project) |
| Template Admin | L5.4 | L5.1, L5.2 | Admin template management, import/export (was L10) |

**Internal dependency shape**: Shallow tree

```
         L5.1 Template Core
          /        |         \
   L5.2 Selection  L5.3 Application  L5.4 Admin
```

**Public interface to L6**: Template API (get available phonemes for a project's template; reference by template ID)

---

### Layer 6: Language Content

The actual language being created. Words built from syllables, syllables built from positions, positions filled with phonemes from the template.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| Words | L6.1 | — | Word creation, display, editing, search |
| Syllables | L6.2 | L6.1 | Multi-syllable structure within words |
| Positions | L6.3 | L6.2 | Onset/nucleus/coda slots within syllables |
| Phoneme References | L6.4 | L6.3 | Actual phoneme assignments in positions (links to L4 via L5 template) |
| TTS for Content | L6.5 | L6.4 | Audio generation for syllables and full words (was L9) |
| Word Suggestions | L6.6 | L6.4 | Phonotactic rule-based word generation suggestions (was L9) |
| Video | L6.7 | L6.1 | Video upload/playback for pronunciation examples (was L9) |

**Internal dependency shape**: Containment sequence with trailing branches

```
L6.1 Words → L6.2 Syllables → L6.3 Positions → L6.4 Phoneme Refs
                                                       |
                                              ┌────────┼────────┐
                                         L6.5 TTS  L6.6 Suggest  L6.7 Video
```

**Public interface to L7**: Content API (CRUD words with full syllable → position → phoneme structure; get audio; get suggestions)

---

### Layer 7: Projects

Containers that organize language content. A project links a user to a template and the words they've created.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| Project Core | L7.1 | — | Project model, CRUD, metadata |
| Storage Type | L7.2 | L7.1 | Local (SQLite) vs cloud (Firestore) selection |
| Variants | L7.3 | L7.1 | Project duplication, forking, branching |
| Content Association | L7.4 | L7.1 | Links project to its template and word collection |
| Dashboard | L7.5 | L7.1 | Project overview, stats, quick access (was L10) |
| Menu/Navigation | L7.6 | L7.1 | Main menu, navigation between projects (was L10) |

**Internal dependency shape**: Star/hub

```
              L7.1 Project Core
          /    |      |     \      \       \
   L7.2     L7.3   L7.4   L7.5   L7.6
  Storage  Variants Content Dashboard Menu
   Type              Assoc.
```

**Public interface to L8**: Project API (CRUD projects with storage type, variants, content; reference by project ID)

---

### Layer 8: Teams

Collaboration. Users working together on shared projects.

| Sub-layer | ID | Depends On | Purpose |
|-----------|----|-----------|---------|
| Team Model | L8.1 | — | Team class, database table |
| Membership | L8.2 | L8.1 | Member management, roles |
| Invites | L8.3 | L8.2 | Invite codes, invite flow |
| Project Sharing | L8.4 | L8.1, L7 | Share projects with team members (cross-layer ref to L7) |

**Internal dependency shape**: Short sequence with cross-layer reference

```
L8.1 Team Model → L8.2 Membership → L8.3 Invites
       |
L8.4 Project Sharing (depends on L8.1 + L7 Project interface)
```

**Public interface**: Collaboration API (team CRUD, invite members, share projects)

---

## What Happened to L9, L10, L11

They no longer exist as standalone layers. Every sub-feature was absorbed:

| Original | Was | Now Lives At | Why There |
|----------|-----|-------------|-----------|
| TTS (phoneme-level) | L9 | **L4.6** | TTS of individual phonemes is a phoneme feature |
| TTS (word/syllable-level) | L9 | **L6.5** | TTS of words is a content feature |
| Video | L9 | **L6.7** | Video for pronunciation is a content enrichment |
| Suggestions | L9 | **L6.6** | Word suggestions are a content creation tool |
| Phoneme Admin | L10 | **L4.7** | Managing phonemes is a phoneme system task |
| Template Admin | L10 | **L5.4** | Managing templates is a template task |
| DB Admin | L10 | **L2.6** | Database tools are an infrastructure task |
| Dashboard | L10 | **L7.5** | Project overview is a project view |
| Menu | L10 | **L7.6** | Navigation is a project-level UI concern |
| Firebase Sync | L11 | **L2.7** | Cloud sync is an infrastructure service |
| Universal Orchestration | L11 | *(deferred)* | True cross-system coordination needs further design |
| AI Orchestration | L11 | *(deferred)* | Meta-intelligence needs further design |

**Deferred items**: Universal Orchestration and AI Orchestration are genuinely system-wide and don't belong to a single domain. They may need to be a capability of the Manager Agent rather than a layer — research ongoing.

---

## The Inter-Layer Dependency Chain

```
L2 Infrastructure
       ↓ provides: auth, storage, DB
L3 Users
       ↓ provides: user identity, session
L4 Phoneme System
       ↓ provides: phoneme inventory, TTS, admin
L5 Templates
       ↓ provides: filtered phoneme subsets
L6 Language Content
       ↓ provides: words, syllables, suggestions, video
L7 Projects
       ↓ provides: project containers, dashboard
L8 Teams
       provides: collaboration, sharing
```

7 layers. Clean linear chain. No cross-cutting outliers.

Each arrow means "the layer below provides an interface that the layer above depends on."

---

## Sub-Layer Count Summary

| Layer | Sub-layers | Dependency Shape |
|-------|-----------|-----------------|
| L2 Infrastructure | 7 | DAG |
| L3 Users | 3 | Sequence |
| L4 Phoneme System | 7 | Sequence + branches |
| L5 Templates | 4 | Shallow tree |
| L6 Language Content | 7 | Containment sequence + branches |
| L7 Projects | 6 | Star/hub |
| L8 Teams | 4 | Short sequence |
| **Total** | **38** | |

38 sub-layers across 7 layers. This is the full feature decomposition of LangTrak with no cross-cutting exceptions.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Absorb L9-L11 into domain layers | Cross-cutting features are better owned by the domain they enhance |
| Keep 7 layers (L2-L8) | Clean dependency chain, no exceptions |
| TTS split between L4 and L6 | Phoneme-level TTS is a phoneme feature; word-level TTS is a content feature |
| Admin tools split across L2, L4, L5, L7 | Each admin tool manages a specific domain |
| Dashboard → L7 | Project overview is a project-level view |
| Firebase Sync → L2 | Cloud sync is infrastructure |
| Defer Universal/AI Orchestration | Genuinely system-wide; may become Manager Agent capability |
| Internal sub-layers follow dependency ordering | Same principle applied recursively at every level |

---

## Companion Diagrams

See `diagrams/` directory for Mermaid visualizations of:
1. Full inter-layer dependency chain
2. Each layer's internal sub-layer dependency shape
3. Agent context model (what each agent knows)

---

*Design created: 2026-02-26*
*Next: Map to OOP class hierarchy, then create experiment structure*
