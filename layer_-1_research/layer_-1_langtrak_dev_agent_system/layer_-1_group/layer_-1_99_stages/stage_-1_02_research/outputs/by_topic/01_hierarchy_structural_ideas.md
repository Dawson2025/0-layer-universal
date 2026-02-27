# Hierarchy Structural Ideas for LangTrak

**Status**: RESEARCH — Exploring different organizing principles
**Date**: 2026-02-26
**Context**: The current design uses dependency ordering. But there are other valid ways to organize a hierarchy. Each produces a different agent structure, different context cascading, and different development workflows.

---

## The Core Question

In our layer-stage system, **lower layer numbers = more universal** (applies to more things above). When we organize LangTrak's features into layers, the ordering principle determines:

1. **What context cascades** — lower layers' context is available to everything above
2. **What agents know** — each agent's "neighbor interfaces" depend on what's adjacent
3. **How delegation flows** — requests traverse the hierarchy differently
4. **Where boundaries sit** — which features are grouped vs. separated

Different ordering principles produce fundamentally different hierarchies. Let's explore each.

---

## Principle 1: Dependency (Current Design)

**Rule**: Layer N depends on all layers below it (lower numbers). If you need X to exist before Y can work, X goes at a lower layer number.

**Question it answers**: "What must exist before this feature can function?"

### Structure

```
L2: Infrastructure (DB, Auth, Firebase, Storage, App)
     ↓ everything needs storage and auth
L3: Users (Profiles, Sessions)
     ↓ all data is user-scoped
L4: Full Phoneme System (Inventory, Groups, Types, Frequency)
     ↓ templates filter this
L5: Phoneme Templates (Subset Selection)
     ↓ content uses templates
L6: Language Content (Words, Syllables, Positions)
     ↓ projects contain content
L7: Projects (Containers, Storage Type, Variants)
     ↓ teams share projects
L8: Teams (Collaboration, Invites, Sharing)

Cross-cutting: L9 Enhancements, L10 Admin, L11 Orchestration
```

### What Cascades

Infrastructure context (storage API, auth checks) reaches EVERYTHING. User scoping reaches everything above L3. Phoneme system context reaches templates, content, projects — but NOT teams or enhancements (they don't directly need phoneme internals).

### Agent Implications

- Infrastructure agent is the most loaded (everything depends on it)
- Relay chains can be long (Teams → Projects → Content → Templates → Phonemes → Users → Infrastructure)
- Cross-cutting layers break the clean chain

### Strengths

- Mirrors technical reality (you literally can't run templates without the phoneme system existing)
- Clear build order (you'd implement bottom-up)
- Minimal context is truly minimal (each layer only needs what it directly depends on)

### Weaknesses

- Doesn't reflect how USERS think about the app
- The relay chain for cross-cutting features is awkward (TTS needs L4 and L6 but not L5, L7, L8)
- Some layers are artificially separated (Templates are really part of the phoneme domain)

---

## Principle 2: Containment (Ownership)

**Rule**: Layer N contains/owns the things at higher layer numbers. What HOLDS what in the data model?

**Question it answers**: "What owns this data? If I delete X, what else gets deleted?"

### Structure

```
L2: Infrastructure (DB, Auth, Firebase, App)
     ↓ infrastructure hosts everything
L3: Users (own everything below)
     ↓ users own projects and teams
L4: Projects (own all content within them)
     ↓ projects contain words and use templates
L5: Templates (define what phonemes are available)
     ↓ templates constrain content
L6: Words (contain syllables)
     ↓ words contain syllables
L7: Syllables + Positions (contain phoneme assignments)
     ↓ positions hold phoneme references
L8: Phoneme References (instances of phonemes used in positions)

Reference Data (doesn't fit the ownership chain):
L9: Phoneme Type System (Groups, Types, Individual Phonemes)
L10: Teams + Sharing (shared ownership — cross-cuts)
L11: Enhancements + Admin + Orchestration
```

### What Cascades

User identity cascades to everything (all data is user-owned). Project context cascades to all content within it. The phoneme TYPE system is reference data that's queried but not owned by any single feature.

### Agent Implications

- The Project agent becomes central (knows about all content within its projects)
- Content agents (Words, Syllables) have narrow scope (only what's inside a word)
- The Phoneme Type System is a "library" that anything can query — it doesn't own anything, things reference it
- Teams complicate the hierarchy because they introduce SHARED ownership (a project can belong to multiple users via a team)

### Strengths

- Matches the DATABASE schema naturally (foreign key relationships = ownership)
- Clear deletion semantics (delete a user → all their projects → all words → all syllables cascade)
- Users and developers intuitively understand "what's inside what"
- Makes data isolation easy (a project's content is self-contained)

### Weaknesses

- Phoneme type system is awkward — it's reference data, not owned by any container
- Teams break single-ownership (shared projects need different handling)
- Deep nesting (User → Project → Word → Syllable → Position → Phoneme) means very long context chains
- Doesn't reflect how features are DEVELOPED (you don't implement words before the phoneme system)

---

## Principle 3: User Interaction Depth

**Rule**: Features users interact with most directly go at the top. Features users never see go at the bottom. Layer number = distance from the user.

**Question it answers**: "How visible is this feature to the end user?"

### Structure

```
L2: Dashboard + Menu (first thing users see)
     ↓ dashboard shows projects
L3: Projects (users create and manage projects)
     ↓ inside projects, users work with content
L4: Words + Content Creation (users create words, syllables)
     ↓ content uses templates
L5: Templates + Phoneme Selection (users choose phoneme subsets)
     ↓ templates filter the system
L6: Phoneme System Browser (users browse available sounds)
     ↓ phonemes have TTS
L7: TTS + Video + Suggestions (users play sounds, watch videos)
     ↓ users collaborate
L8: Teams + Invites (users share with others)

Below user visibility:
L9: Admin Tools (admin-only)
L10: Auth + Users + Sessions (invisible login layer)
L11: Infrastructure (DB, Firebase, Storage — invisible)
```

### What Cascades

The dashboard's context (what to display, navigation structure) cascades to everything — every feature is eventually displayed through the dashboard. Project context cascades to all content views.

### Agent Implications

- Dashboard agent needs broad knowledge (it displays info from every feature)
- Infrastructure agent is deeply buried — it supports everything but has no user visibility
- The cascade is INVERTED from dependency (infrastructure is universal in dependency, but deepest in interaction)

### Strengths

- Matches the USER EXPERIENCE (how people actually use the app)
- Prioritizes what users care about (dashboard, projects, content creation)
- Natural for UI/UX-first development
- Testing can follow user flows (top-down)

### Weaknesses

- The "most universal" context is the dashboard, which is actually the LEAST foundational technically
- Infrastructure at L11 means its context doesn't cascade — but everything depends on it
- Inverts the build order (you can't build the dashboard without the backend)
- Doesn't help with debugging (bugs in L11 affect L2, which is confusing)

---

## Principle 4: Frequency of Change

**Rule**: Things that change rarely go at lower layer numbers. Things that change constantly go at higher numbers. Lower = more stable.

**Question it answers**: "How often does this need to be modified?"

### Structure

```
L2: Infrastructure (DB schema, Auth flow — changes once, runs forever)
     ↓ stable foundation
L3: Phoneme Type System (IPA standard — almost never changes)
     ↓ reference data is stable
L4: Auth + Users (login flow rarely changes)
     ↓ user model is stable
L5: Admin + Management (changes with new features, not constantly)
     ↓ admin evolves slowly
L6: Templates + Projects (change per user session, relatively stable structure)
     ↓ container structure is stable, contents vary
L7: Words + Syllables + Content (change every session — user creates content)
     ↓ most volatile content
L8: TTS + Suggestions (computed dynamically every time)
     ↓ always recomputed
L9: Teams + Invites (event-driven, changes only on specific user actions)
L10: Firebase Sync + Orchestration (runs on every change)
L11: Dashboard (re-renders on every navigation)
```

### What Cascades

Infrastructure stability cascades — everyone can rely on the DB schema not changing. Phoneme type system stability cascades — templates know the phoneme vocabulary is fixed.

### Agent Implications

- Lower layer agents rarely need updates — they become "fire and forget" specialists
- Higher layer agents are constantly active (content creation, dashboard updates)
- Testing strategy inverts: test lower layers once thoroughly, test upper layers continuously
- The most stable context is the most universal — good for caching

### Strengths

- Matches deployment reality (you deploy infra changes carefully, UI changes frequently)
- Good for CI/CD (stable layers have stable tests, volatile layers need frequent testing)
- Reduces cascading changes (changing infrastructure SHOULD be rare and carefully managed)
- Context caching works well (lower layers' context rarely invalidates)

### Weaknesses

- "Frequency of change" is subjective and can shift over time
- Teams and Firebase are awkward to place (they're event-driven, not constantly changing)
- Doesn't directly help agents understand dependencies
- Dashboard at L11 means it gets NO cascading context — but it needs to display everything

---

## Principle 5: Data Flow (Input → Process → Output)

**Rule**: Follow how data moves through the system. Input layers at the bottom, processing in the middle, output at the top.

**Question it answers**: "Where in the processing pipeline does this feature sit?"

### Structure

```
L2: Input Layer
    - Auth (user credentials in)
    - Forms (word creation, project creation)
    - File uploads (video, audio)
     ↓ input validated
L3: Validation Layer
    - Session validation
    - Data format checking
    - Phonotactic rule checking
     ↓ validated data processed
L4: Business Logic Layer
    - Phoneme system rules
    - Template application
    - Word/syllable structure rules
    - Project management logic
     ↓ processed data stored
L5: Storage Layer
    - SQLite operations
    - Firestore operations
    - Storage manager
     ↓ stored data retrieved
L6: Computation Layer
    - TTS generation
    - Frequency analysis
    - Suggestion engine
    - NetworkX graph analysis
     ↓ computed data formatted
L7: Presentation Layer
    - Dashboard rendering
    - Word lists
    - Project views
    - Phoneme browsers
     ↓ presented to users
L8: Collaboration Layer
    - Teams
    - Sharing
    - Real-time sync
```

### What Cascades

Input format context (what data types, what validation rules) cascades to all processing. Storage API cascades to everything that reads/writes. Computation results cascade to presentation.

### Agent Implications

- Pipeline-style processing: each agent hands off to the next
- Clear boundaries: input agent → validation agent → logic agent → storage agent
- BUT: most real features span the ENTIRE pipeline (creating a word touches input, validation, logic, storage, presentation)
- Cross-cutting features like TTS don't fit neatly into one pipeline stage

### Strengths

- Matches the MVC/pipeline architecture pattern familiar to developers
- Clear separation of concerns (input vs. logic vs. storage vs. output)
- Easy to reason about data flow
- Good for debugging (follow the data through the pipeline)

### Weaknesses

- Real features span ALL layers (word creation touches every pipeline stage)
- Agents need very broad knowledge (the storage agent handles phonemes, projects, users, etc.)
- Loses domain specialization (no "phoneme expert" — just a "business logic" generalist)
- Doesn't match how users think about the app at all

---

## Principle 6: Feature Coupling (Cluster by Relatedness)

**Rule**: Features that are tightly coupled (frequently change together, share data structures, have similar domain concepts) belong in the same layer. Like bounded contexts in DDD.

**Question it answers**: "What features belong together? What changes together?"

### Structure

```
L2: Identity Cluster
    - Auth, Users, Sessions
    - All about "who is using the system"
     ↓ identity established
L3: Phoneme Domain Cluster
    - Full Phoneme System, Groups, Types
    - Templates (filter of the system)
    - Frequency tracking
    - All about "the sound inventory"
     ↓ phoneme domain established
L4: Content Domain Cluster
    - Words, Syllables, Positions
    - Content creation and structure
    - All about "language content"
     ↓ content created
L5: Project Management Cluster
    - Projects, Variants
    - Storage type management
    - All about "organizing content"
     ↓ content organized
L6: Collaboration Cluster
    - Teams, Invites, Sharing
    - All about "working together"
     ↓ sharing enabled
L7: Enhancement Cluster
    - TTS, Video, Suggestions
    - All about "enriching content"
     ↓ content enriched
L8: Management Cluster
    - Admin tools, Dashboard, Menu
    - All about "managing the system"
     ↓ system managed
L9: Infrastructure Cluster
    - Database, Firebase, Storage Manager
    - All about "where data lives"
```

### What Cascades

Identity context (who's logged in) cascades everywhere. Phoneme domain context cascades to content and enhancements. Infrastructure is at L9 — it's available to everything but isn't "universal" in the cascading sense.

Wait — this breaks the "lower = more universal" rule. Infrastructure IS universal but it's at L9. We'd need to either:
- **Invert**: Put infrastructure at L2 (but then it's not "clustered by coupling")
- **Separate infrastructure**: Have it as a foundation below all clusters
- **Make it cross-cutting**: Like L9-L11 in the dependency model

### Revised Structure (Infrastructure as Foundation)

```
L2: Infrastructure Foundation
    - Database, Firebase, Storage Manager, App
     ↓ foundation for all clusters

L3: Identity Cluster (Auth, Users, Sessions)
L4: Phoneme Domain (System, Templates, Types, Frequency)
L5: Content Domain (Words, Syllables, Positions)
L6: Project Management (Projects, Variants, Storage Type)
L7: Collaboration (Teams, Invites, Sharing)
L8: Enhancements (TTS, Video, Suggestions)
L9: Management (Admin, Dashboard, Menu)
```

### Agent Implications

- Cluster agents are true DOMAIN EXPERTS — the Phoneme Domain agent knows everything about phonemes, templates, groups, types, and frequency
- Fewer handoffs for within-domain work (adding a phoneme type stays entirely in L4)
- Cross-domain work requires cluster-to-cluster communication (creating a word needs L4 + L5)
- Infrastructure agent is universally available

### Strengths

- Matches Domain-Driven Design (bounded contexts)
- Domain expertise is concentrated (one agent knows everything about phonemes)
- Reduces within-domain relay chains to zero
- Natural for microservices architecture
- Teams can own clusters independently

### Weaknesses

- Cluster boundaries are subjective (should Templates be in Phoneme Domain or Content Domain?)
- Cross-cluster work still needs coordination
- Some clusters are huge (Phoneme Domain has 4 sub-features) while others are small (Collaboration has 2)
- Infrastructure at L2 doesn't cascade to clusters naturally — it's more of a service than a parent

---

## Comparison Matrix

| Principle | Lower Layers Are... | Best For | Worst For | Context Cascade Makes Sense? |
|-----------|-------------------|----------|-----------|------------------------------|
| **Dependency** | What everything needs | Build ordering, technical correctness | User experience, cross-cutting | Yes — dependencies cascade naturally |
| **Containment** | What owns the most | Data modeling, deletion rules | Reference data, shared ownership | Partially — ownership cascades but refs don't |
| **User Interaction** | What users see first | UX-first development, UI testing | Backend development, debugging | No — dashboard doesn't provide universal context |
| **Change Frequency** | Most stable things | CI/CD, deployment safety | Feature development prioritization | Partially — stability is good to cascade |
| **Data Flow** | Where data enters | Pipeline debugging, data tracing | Domain specialization, feature scoping | Yes — input formats cascade through pipeline |
| **Feature Coupling** | Foundation + domain clusters | Domain expertise, bounded contexts | Ordering between clusters | Partially — clusters are peers, not hierarchical |

---

## Hybrid Ideas

### Hybrid 1: Dependency + Containment

Use dependency for the ORDERING between layers, but group features within layers by containment.

```
L2: Infrastructure (owns nothing, everything depends on it)
L3: Users (own everything below — containment root)
L4: Phoneme System (reference data — not owned, but depended upon)
L5: Templates + Content (owned by projects, depends on phonemes)
L6: Projects (contains templates and content — containment parent)
L7: Teams (shares projects — cross-cuts containment)
```

Problem: Dependency says Phonemes → Templates → Content → Projects. Containment says Projects → Content → Templates → Phonemes. **They order in opposite directions.** You can't satisfy both.

### Hybrid 2: Feature Coupling + Dependency (Between Clusters)

Use feature coupling WITHIN layers (group related features). Use dependency BETWEEN layers (order clusters by what depends on what).

```
L2: Infrastructure Cluster (DB, Auth, Firebase, Storage, App)
     ↓ depends: everything
L3: Identity Cluster (Users, Sessions, Profiles)
     ↓ depends: infrastructure
L4: Phoneme Domain Cluster (System, Templates, Groups, Types, Frequency)
     ↓ depends: users
L5: Content Domain Cluster (Words, Syllables, Positions)
     ↓ depends: phoneme domain (content uses templates)
L6: Project Cluster (Projects, Variants, Storage Type)
     ↓ depends: content domain (projects contain content)
L7: Collaboration Cluster (Teams, Invites, Sharing)
     ↓ depends: projects (teams share projects)
L8: Enhancement Cluster (TTS, Video, Suggestions)
     ↓ cross-cuts: phoneme domain + content domain
L9: Management Cluster (Admin, Dashboard, Menu)
     ↓ cross-cuts: everything
```

**This is probably the strongest hybrid.** It preserves dependency ordering between clusters while giving each cluster deep domain knowledge. The agent structure maps 1:1 to clusters.

### Hybrid 3: Stable Core + Volatile Shell

Use change frequency to define an inner "stable core" and an outer "volatile shell":

```
STABLE CORE (rarely changes):
  L2: Infrastructure
  L3: Users
  L4: Phoneme Type System

ACTIVE ZONE (changes per feature work):
  L5: Templates
  L6: Content
  L7: Projects

VOLATILE SHELL (changes per user session):
  L8: Dashboard, Menu
  L9: TTS, Suggestions
  L10: Teams, Sync
```

Agents in the stable core have fewer updates. Active zone agents do most of the work. Volatile shell agents handle presentation and user-facing changes.

---

## Recommendation for Experiment

Add these as new trials to the Agent Hierarchy Structure Experiment:

| Trial | Principle | Why Test It |
|-------|-----------|-------------|
| F | Containment | Tests ownership-based hierarchy — opposite direction from dependency |
| G | Feature Coupling + Dependency (Hybrid 2) | Tests clustered domain experts with dependency ordering between clusters |
| H | Stable Core + Volatile Shell (Hybrid 3) | Tests whether stability-based layering improves agent efficiency |

These three, combined with the existing 5 trials (A-E), cover a wide range of structural philosophies.

---

## Next Steps

1. Add Trials F, G, H to the experiment document
2. For each trial, define the specific agent 0AGNOSTIC.md content
3. Choose 3-4 trials with maximum structural variation to run first
4. Execute test tasks and score results
