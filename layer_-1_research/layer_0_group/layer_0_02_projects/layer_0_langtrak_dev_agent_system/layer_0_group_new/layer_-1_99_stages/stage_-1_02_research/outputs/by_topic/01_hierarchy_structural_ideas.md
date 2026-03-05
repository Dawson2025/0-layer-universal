---
resource_id: "37eac977-e2f7-448e-bca6-192419dc0098"
resource_type: "output"
resource_name: "01_hierarchy_structural_ideas"
---
# Hierarchy Structural Ideas for LangTrak

**Status**: RESEARCH — Exploring different organizing principles
**Date**: 2026-02-26
**Context**: The current design uses dependency ordering. But there are other valid ways to organize a hierarchy. Each produces a different agent structure, different context cascading, and different development workflows.

---

<!-- section_id: "d00be75e-2ad5-4a4c-932a-940e01e5c1d9" -->
## The Core Question

In our layer-stage system, **lower layer numbers = more universal** (applies to more things above). When we organize LangTrak's features into layers, the ordering principle determines:

1. **What context cascades** — lower layers' context is available to everything above
2. **What agents know** — each agent's "neighbor interfaces" depend on what's adjacent
3. **How delegation flows** — requests traverse the hierarchy differently
4. **Where boundaries sit** — which features are grouped vs. separated

Different ordering principles produce fundamentally different hierarchies. Let's explore each.

---

<!-- section_id: "336457e2-ffc3-4e25-9494-eaf817d0c6b0" -->
## Principle 1: Dependency (Current Design)

**Rule**: Layer N depends on all layers below it (lower numbers). If you need X to exist before Y can work, X goes at a lower layer number.

**Question it answers**: "What must exist before this feature can function?"

<!-- section_id: "6509d497-3f6a-46ff-9986-799b49d69990" -->
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

<!-- section_id: "d37de600-2063-42ff-8d0d-453ef23bba00" -->
### What Cascades

Infrastructure context (storage API, auth checks) reaches EVERYTHING. User scoping reaches everything above L3. Phoneme system context reaches templates, content, projects — but NOT teams or enhancements (they don't directly need phoneme internals).

<!-- section_id: "3ebd3248-c04d-4df2-9021-433c588e792a" -->
### Agent Implications

- Infrastructure agent is the most loaded (everything depends on it)
- Relay chains can be long (Teams → Projects → Content → Templates → Phonemes → Users → Infrastructure)
- Cross-cutting layers break the clean chain

<!-- section_id: "d4a95532-e39a-45a8-9f70-b9b2c99ad14a" -->
### Strengths

- Mirrors technical reality (you literally can't run templates without the phoneme system existing)
- Clear build order (you'd implement bottom-up)
- Minimal context is truly minimal (each layer only needs what it directly depends on)

<!-- section_id: "696dbb4b-2e57-49e3-a26a-1528cf84743b" -->
### Weaknesses

- Doesn't reflect how USERS think about the app
- The relay chain for cross-cutting features is awkward (TTS needs L4 and L6 but not L5, L7, L8)
- Some layers are artificially separated (Templates are really part of the phoneme domain)

---

<!-- section_id: "f6aff517-95b1-46be-bc30-46bf05a18dd1" -->
## Principle 2: Containment (Ownership)

**Rule**: Layer N contains/owns the things at higher layer numbers. What HOLDS what in the data model?

**Question it answers**: "What owns this data? If I delete X, what else gets deleted?"

<!-- section_id: "7c0df750-e1d0-4592-9758-a70976910960" -->
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

<!-- section_id: "e9ce00ff-1a95-4348-882e-5fa0b4be7a86" -->
### What Cascades

User identity cascades to everything (all data is user-owned). Project context cascades to all content within it. The phoneme TYPE system is reference data that's queried but not owned by any single feature.

<!-- section_id: "45433aab-b1a3-42c6-8faa-749f26597c9c" -->
### Agent Implications

- The Project agent becomes central (knows about all content within its projects)
- Content agents (Words, Syllables) have narrow scope (only what's inside a word)
- The Phoneme Type System is a "library" that anything can query — it doesn't own anything, things reference it
- Teams complicate the hierarchy because they introduce SHARED ownership (a project can belong to multiple users via a team)

<!-- section_id: "484158e0-1f28-4738-a74b-794020f18bb7" -->
### Strengths

- Matches the DATABASE schema naturally (foreign key relationships = ownership)
- Clear deletion semantics (delete a user → all their projects → all words → all syllables cascade)
- Users and developers intuitively understand "what's inside what"
- Makes data isolation easy (a project's content is self-contained)

<!-- section_id: "986e991b-979d-40df-a608-1207574ba93a" -->
### Weaknesses

- Phoneme type system is awkward — it's reference data, not owned by any container
- Teams break single-ownership (shared projects need different handling)
- Deep nesting (User → Project → Word → Syllable → Position → Phoneme) means very long context chains
- Doesn't reflect how features are DEVELOPED (you don't implement words before the phoneme system)

---

<!-- section_id: "318120b6-e5c0-4c3a-8356-071682f09f4d" -->
## Principle 3: User Interaction Depth

**Rule**: Features users interact with most directly go at the top. Features users never see go at the bottom. Layer number = distance from the user.

**Question it answers**: "How visible is this feature to the end user?"

<!-- section_id: "61514b0d-6ada-4c53-a4c0-615ff0e5f045" -->
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

<!-- section_id: "f56eb4b8-a7c0-4a9a-b415-8515edecaf15" -->
### What Cascades

The dashboard's context (what to display, navigation structure) cascades to everything — every feature is eventually displayed through the dashboard. Project context cascades to all content views.

<!-- section_id: "e3789b3d-18f9-4bb2-8e09-9ab76187f9a1" -->
### Agent Implications

- Dashboard agent needs broad knowledge (it displays info from every feature)
- Infrastructure agent is deeply buried — it supports everything but has no user visibility
- The cascade is INVERTED from dependency (infrastructure is universal in dependency, but deepest in interaction)

<!-- section_id: "05314df2-2e29-4769-bd83-4609e5a43b63" -->
### Strengths

- Matches the USER EXPERIENCE (how people actually use the app)
- Prioritizes what users care about (dashboard, projects, content creation)
- Natural for UI/UX-first development
- Testing can follow user flows (top-down)

<!-- section_id: "a37d630c-5097-4367-8619-23cc1f93c683" -->
### Weaknesses

- The "most universal" context is the dashboard, which is actually the LEAST foundational technically
- Infrastructure at L11 means its context doesn't cascade — but everything depends on it
- Inverts the build order (you can't build the dashboard without the backend)
- Doesn't help with debugging (bugs in L11 affect L2, which is confusing)

---

<!-- section_id: "60fe63b1-ec40-4a89-8570-d32843329c9e" -->
## Principle 4: Frequency of Change

**Rule**: Things that change rarely go at lower layer numbers. Things that change constantly go at higher numbers. Lower = more stable.

**Question it answers**: "How often does this need to be modified?"

<!-- section_id: "85c100a5-36ef-4cc4-8b2a-af40b1673d68" -->
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

<!-- section_id: "34b694f6-a377-4203-8fa6-0c08fe2ed501" -->
### What Cascades

Infrastructure stability cascades — everyone can rely on the DB schema not changing. Phoneme type system stability cascades — templates know the phoneme vocabulary is fixed.

<!-- section_id: "25320266-2e68-4364-af76-26171e9aede4" -->
### Agent Implications

- Lower layer agents rarely need updates — they become "fire and forget" specialists
- Higher layer agents are constantly active (content creation, dashboard updates)
- Testing strategy inverts: test lower layers once thoroughly, test upper layers continuously
- The most stable context is the most universal — good for caching

<!-- section_id: "9ccc19cb-51d4-47c4-971a-65169b21abc1" -->
### Strengths

- Matches deployment reality (you deploy infra changes carefully, UI changes frequently)
- Good for CI/CD (stable layers have stable tests, volatile layers need frequent testing)
- Reduces cascading changes (changing infrastructure SHOULD be rare and carefully managed)
- Context caching works well (lower layers' context rarely invalidates)

<!-- section_id: "69696af5-5a7f-488c-b2d7-d1cd6eed5acd" -->
### Weaknesses

- "Frequency of change" is subjective and can shift over time
- Teams and Firebase are awkward to place (they're event-driven, not constantly changing)
- Doesn't directly help agents understand dependencies
- Dashboard at L11 means it gets NO cascading context — but it needs to display everything

---

<!-- section_id: "215b7096-767a-4f26-9f96-e7b3f6f7b8c4" -->
## Principle 5: Data Flow (Input → Process → Output)

**Rule**: Follow how data moves through the system. Input layers at the bottom, processing in the middle, output at the top.

**Question it answers**: "Where in the processing pipeline does this feature sit?"

<!-- section_id: "6cd59721-e646-4d30-9d01-e220fbc13be6" -->
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

<!-- section_id: "34e719b5-8509-425d-9cab-cc7e41e576c6" -->
### What Cascades

Input format context (what data types, what validation rules) cascades to all processing. Storage API cascades to everything that reads/writes. Computation results cascade to presentation.

<!-- section_id: "0999c810-4b4e-4790-8021-b0458b871ad6" -->
### Agent Implications

- Pipeline-style processing: each agent hands off to the next
- Clear boundaries: input agent → validation agent → logic agent → storage agent
- BUT: most real features span the ENTIRE pipeline (creating a word touches input, validation, logic, storage, presentation)
- Cross-cutting features like TTS don't fit neatly into one pipeline stage

<!-- section_id: "f2e47ffd-e6e7-42ab-bb9a-6586a811445c" -->
### Strengths

- Matches the MVC/pipeline architecture pattern familiar to developers
- Clear separation of concerns (input vs. logic vs. storage vs. output)
- Easy to reason about data flow
- Good for debugging (follow the data through the pipeline)

<!-- section_id: "150a2db3-c696-45ab-a065-75537a772160" -->
### Weaknesses

- Real features span ALL layers (word creation touches every pipeline stage)
- Agents need very broad knowledge (the storage agent handles phonemes, projects, users, etc.)
- Loses domain specialization (no "phoneme expert" — just a "business logic" generalist)
- Doesn't match how users think about the app at all

---

<!-- section_id: "b5278f5f-0ccc-4df8-942a-79bb1b2659d1" -->
## Principle 6: Feature Coupling (Cluster by Relatedness)

**Rule**: Features that are tightly coupled (frequently change together, share data structures, have similar domain concepts) belong in the same layer. Like bounded contexts in DDD.

**Question it answers**: "What features belong together? What changes together?"

<!-- section_id: "490f44cd-cbe1-48f5-9655-135839254770" -->
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

<!-- section_id: "04386559-93f4-49b9-8120-0655cdb0159d" -->
### What Cascades

Identity context (who's logged in) cascades everywhere. Phoneme domain context cascades to content and enhancements. Infrastructure is at L9 — it's available to everything but isn't "universal" in the cascading sense.

Wait — this breaks the "lower = more universal" rule. Infrastructure IS universal but it's at L9. We'd need to either:
- **Invert**: Put infrastructure at L2 (but then it's not "clustered by coupling")
- **Separate infrastructure**: Have it as a foundation below all clusters
- **Make it cross-cutting**: Like L9-L11 in the dependency model

<!-- section_id: "3c2252e7-d403-4e31-a81b-c936dbc4aaa8" -->
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

<!-- section_id: "c965799a-8d47-44c1-898e-b9c638077dca" -->
### Agent Implications

- Cluster agents are true DOMAIN EXPERTS — the Phoneme Domain agent knows everything about phonemes, templates, groups, types, and frequency
- Fewer handoffs for within-domain work (adding a phoneme type stays entirely in L4)
- Cross-domain work requires cluster-to-cluster communication (creating a word needs L4 + L5)
- Infrastructure agent is universally available

<!-- section_id: "6e8873db-5f71-4c44-ae00-14a7cc0733a9" -->
### Strengths

- Matches Domain-Driven Design (bounded contexts)
- Domain expertise is concentrated (one agent knows everything about phonemes)
- Reduces within-domain relay chains to zero
- Natural for microservices architecture
- Teams can own clusters independently

<!-- section_id: "1178fa76-bb15-482b-870a-1757986a637d" -->
### Weaknesses

- Cluster boundaries are subjective (should Templates be in Phoneme Domain or Content Domain?)
- Cross-cluster work still needs coordination
- Some clusters are huge (Phoneme Domain has 4 sub-features) while others are small (Collaboration has 2)
- Infrastructure at L2 doesn't cascade to clusters naturally — it's more of a service than a parent

---

<!-- section_id: "2bf3d09e-76a4-4f1f-a9d9-36e6eca7a334" -->
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

<!-- section_id: "61eee24c-ed0c-4e6d-8396-2b380afb99c9" -->
## Hybrid Ideas

<!-- section_id: "a1400cb6-de1d-4d85-bc77-4b6552684400" -->
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

<!-- section_id: "45b1a7d2-ea74-404a-bd09-2c5a2e3856a8" -->
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

<!-- section_id: "ab2b57ff-b301-472e-9488-721b1014c4ca" -->
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

<!-- section_id: "739d4fe5-c5f0-420c-bc85-35aefe60a588" -->
## Two Fundamental Design Axes

Before adding more principles, we need to name the two meta-dimensions that ALL structural choices are optimizing for. Every hierarchy design makes tradeoffs between these two:

<!-- section_id: "5e530931-a7e1-4466-9b0b-10a534274a6e" -->
### Axis 1: Cascading Context (Top-Down Flow)

**The question**: What universal knowledge should flow downward from parent to child, so that every agent below a certain point in the tree has the right foundational context?

In the layer-stage system, lower-numbered layers (closer to root) provide context that cascades to ALL higher-numbered layers. This means:
- L2 Infrastructure context reaches every agent in the system
- L3 Users context reaches everything from L4 onward
- The ROOT of the tree is the most universal, the LEAVES are the most specific

**Optimization target**: Minimize what each agent needs to load while ensuring it still has enough context to work correctly. The ideal cascading structure means an agent at L6 automatically inherits L2-L5 context and only needs to load L6-specific details.

**When this axis dominates**: Architecture design, context efficiency, reducing token budgets, ensuring consistency across the system.

<!-- section_id: "3d157d5f-122d-4a5a-be08-4ecd217b94c4" -->
### Axis 2: Delegation/Traversal (Manager-Worker Trees)

**The question**: How should manager agents delegate to sub-managers and eventually to leaf worker agents, so that:
- Leaf agents truly inform the parent's decisions (bottom-up information flow)
- Scope boundaries are clear (agent knows what's in-scope vs. out-of-scope)
- Traversal works (when work is out-of-scope, the agent can route it correctly)

In this axis, the hierarchy isn't about what context flows down — it's about what WORK flows down and what REPORTS flow up:
- Manager says "fix the word creation bug" → delegates to Content Domain sub-manager → delegates to Words worker agent
- Words worker agent finds the root cause involves phonemes → recognizes it's out-of-scope → reports back up → manager re-routes to Phoneme Domain sub-manager

**Optimization target**: Minimize delegation hops, ensure scope boundaries are accurate, make traversal reliable (agents correctly identify when work is out-of-scope and route to the right sibling).

**When this axis dominates**: Task execution, debugging, feature implementation, coordination between teams.

<!-- section_id: "383ca156-3bee-4735-ba34-d8c940968984" -->
### The Tension

These axes can CONFLICT:
- **Best for cascading context**: Deep, narrow hierarchies (many layers, each very focused) — context cascades precisely
- **Best for delegation**: Shallow, wide hierarchies (few layers, each covering a broad domain) — fewer delegation hops

The ideal structure balances both. The principles below are organized by which axis they primarily serve.

---

<!-- section_id: "a8589746-c890-43de-91c1-049fc1ad68ac" -->
## Additional Structural Principles

<!-- section_id: "cc7957ab-bdbf-4526-b4b0-486f9b33e988" -->
### Principle 7: Skill/Capability Clustering

**Rule**: Group agents by what TOOLS and CAPABILITIES they need, not by what domain they work on.

**Question it answers**: "What tools does this agent need to do its job?"

**Primary axis**: Delegation (agents with the right skills get the right work)

#### Structure

```
Manager Agent
├── Database Agents (need SQL, migration tools, schema knowledge)
│   ├── Schema Agent
│   ├── Query Agent
│   └── Migration Agent
├── API/Route Agents (need Flask, HTTP, endpoint patterns)
│   ├── Auth Routes Agent
│   ├── Content Routes Agent
│   └── Admin Routes Agent
├── Frontend/Template Agents (need Jinja2, HTML, CSS, JS)
│   ├── Dashboard Agent
│   ├── Forms Agent
│   └── Component Agent
├── Computation Agents (need NetworkX, TTS, algorithms)
│   ├── TTS Agent
│   ├── Graph Analysis Agent
│   └── Frequency Agent
└── Testing Agents (need pytest, fixtures, mocking)
    ├── Unit Test Agent
    ├── Integration Test Agent
    └── E2E Test Agent
```

#### Context Model

Each capability cluster shares tool-specific context: Database agents all know the schema, ORM patterns, and migration tools. API agents all know Flask routing patterns and middleware. This avoids loading irrelevant tool context (a database agent doesn't need Jinja2 knowledge).

#### Strengths

- Agents are TOOL EXPERTS — they know their stack deeply
- Natural MCP tool assignment (database agents get SQLite tools, frontend agents get Playwright)
- Good for parallelism (database work and frontend work can happen concurrently)
- Matches how human teams often organize (backend team, frontend team, QA team)

#### Weaknesses

- A single FEATURE touches multiple capability clusters (adding a phoneme group needs DB + API + frontend + test work)
- No agent has full domain knowledge (the database agent knows phoneme tables but not phoneme linguistics)
- Heavy coordination needed for any feature work
- Cross-cutting features require ALL clusters

---

<!-- section_id: "810ebe4f-1fe3-48f2-84ad-c3904bc3bf07" -->
### Principle 8: Knowledge Depth vs. Breadth (Specialist Tree)

**Rule**: Root agents are GENERALISTS who know a little about everything. Deeper agents are SPECIALISTS who know one thing deeply. The tree mirrors expertise depth.

**Question it answers**: "How specialized should this agent's knowledge be?"

**Primary axis**: Both (context cascades as general → specific; delegation routes to the right specialist)

#### Structure

```
Root: System Generalist (knows all 10 layers at overview level)
├── Phoneme Specialist (deep phoneme knowledge)
│   ├── IPA Expert (knows International Phonetic Alphabet deeply)
│   ├── Phonotactic Rules Expert (syllable structure rules)
│   └── Frequency Analyst (phoneme usage patterns)
├── Content Specialist (deep content structure knowledge)
│   ├── Word Builder Expert (word creation, syllable assignment)
│   ├── Template Designer Expert (subset selection, filtering)
│   └── Position Manager Expert (phoneme-to-position mapping)
├── Project Specialist (deep project management knowledge)
│   ├── Storage Expert (SQLite vs Firestore, dual DB)
│   ├── Variant Expert (project duplication, forking)
│   └── Collaboration Expert (teams, sharing, invites)
├── Infrastructure Specialist (deep backend knowledge)
│   ├── Database Expert (schema, migrations, queries)
│   ├── Auth Expert (login, sessions, permissions)
│   └── Firebase Expert (sync, real-time, cloud storage)
└── Enhancement Specialist (deep enhancement knowledge)
    ├── TTS Expert (text-to-speech generation)
    ├── Suggestion Expert (recommendation engine)
    └── Admin Expert (management tools, dashboards)
```

#### Context Model

- Root agent: 2-3 sentence summary of each layer (50-100 tokens total). Enough to ROUTE work, not enough to DO work.
- Specialist agents: Full context for their domain (500-1000 tokens). Enough to DO work within their domain.
- Expert agents (leaves): Complete context for their narrow area (1000-2000 tokens). Deep expertise, narrow scope.

#### What Cascades

General system knowledge (how layers relate, what dependencies exist, what the architecture looks like) cascades from root to all specialists. Each specialist adds domain context that cascades to its experts. An IPA Expert inherits both system overview AND phoneme domain knowledge.

#### Delegation Pattern

1. Task arrives at root generalist
2. Root identifies domain → delegates to specialist
3. Specialist identifies specific area → delegates to expert
4. If expert discovers work is out-of-scope → reports back to specialist → specialist routes to sibling expert or escalates to root

#### Strengths

- **Clean traversal**: Scope boundaries are natural (IPA Expert knows phonemes, not projects)
- **Efficient context loading**: Root is lightweight, experts are focused
- **Good for both axes**: Context cascades general → specific; delegation routes to right specialist
- **Matches how human organizations work**: VP → Director → Engineer

#### Weaknesses

- 3 levels deep means more delegation hops (root → specialist → expert = 2 hops minimum)
- Root agent can become a bottleneck (every cross-domain task goes through it)
- Leaf experts may be too narrow (the IPA Expert can't help with word creation)
- Specialist level must be well-defined (too broad = no benefit over flat; too narrow = too many specialists)

---

<!-- section_id: "4185d36a-e4e9-4b3f-bde7-be71ba9d6426" -->
### Principle 9: Communication Topology

**Rule**: Structure the hierarchy based on what agents need to TALK TO each other about, not what they OWN or depend on. Minimize communication distance between frequently-communicating agents.

**Question it answers**: "Which agents need to coordinate most frequently?"

**Primary axis**: Delegation (optimize for coordination, not context)

#### Analysis: What Communicates in LangTrak?

Looking at the 7 test tasks from the experiment:

| Task | Agents That Must Coordinate |
|------|----------------------------|
| T1: Multisyllable word failures | Content ↔ Phoneme ↔ Project |
| T2: New phoneme group type | Phoneme ↔ Template ↔ Admin |
| T3: Project variant duplication | Project ↔ Infrastructure ↔ Orchestration |
| T4: Admin auth routing | Admin ↔ Auth ↔ Users |
| T5: Team invitation flow | Teams ↔ Users ↔ Project ↔ Auth |
| T6: TTS syllable preview | TTS ↔ Content ↔ Phoneme |
| T7: Dual DB path design | Infrastructure (ALL modules) |

**High-frequency communication pairs**:
- Phoneme ↔ Content (T1, T6)
- Auth ↔ Users (T4, T5)
- Project ↔ Infrastructure (T3, T7)
- Content ↔ Project (T1)
- Phoneme ↔ Template (T2)

#### Structure (Optimized for Communication)

```
Manager Agent
├── Phoneme-Content Hub (most frequent communication pair)
│   ├── Phoneme System Agent
│   ├── Template Agent
│   ├── Content Agent (Words, Syllables, Positions)
│   └── TTS Agent (needs phoneme + content)
├── Identity Hub (auth/user communication pair)
│   ├── Auth Agent
│   ├── Users Agent
│   └── Sessions Agent
├── Project-Infrastructure Hub
│   ├── Project Agent
│   ├── Infrastructure Agent
│   ├── Storage Agent
│   └── Orchestration Agent
└── Collaboration-Admin Hub (lowest-frequency communication)
    ├── Teams Agent
    ├── Admin Agent
    └── Dashboard Agent
```

#### Strengths

- Minimizes inter-hub communication for common tasks
- High-frequency pairs are co-located (phoneme + content in same hub)
- Communication within a hub is "free" (shared context)
- Naturally creates efficient sub-teams

#### Weaknesses

- Communication patterns can change as the app evolves
- Some tasks STILL cross hubs (T5 needs Identity + Project + Collaboration)
- Hub assignment is based on historical patterns, not architectural principles
- Doesn't help with NEW features (no historical communication data)

---

<!-- section_id: "c9a14729-0438-4ae7-bc0a-93052eabf70d" -->
### Principle 10: Risk/Criticality-Based Hierarchy

**Rule**: The most critical, highest-risk components sit closest to root with the most oversight. Lower-risk, more isolated components are deeper leaves. Root manager has direct visibility into high-risk areas.

**Question it answers**: "What happens if this breaks? How much of the system goes down?"

**Primary axis**: Both (critical context cascades broadly; delegation keeps risky work close to manager oversight)

#### Criticality Analysis for LangTrak

| Component | Risk Level | Why |
|-----------|-----------|-----|
| Database/Storage | CRITICAL | If DB goes down, everything goes down |
| Auth | CRITICAL | Auth failure = locked out of app |
| Firebase Sync | HIGH | Sync failure = data loss across devices |
| User Data | HIGH | User data corruption is catastrophic |
| Phoneme System | MEDIUM | Core but self-contained, doesn't cascade failures |
| Projects | MEDIUM | Container corruption loses content |
| Content (Words) | LOW | Individual word failures are isolated |
| Templates | LOW | Template failure only affects filtering |
| TTS | LOW | TTS failure = degraded but usable app |
| Teams | LOW | Collaboration failure doesn't break solo use |
| Dashboard | LOW | Display failure is visible but non-destructive |

#### Structure

```
Root Manager (has full critical visibility)
├── [CRITICAL] Infrastructure Guardian
│   ├── Database Agent (schema, queries, integrity)
│   ├── Auth Agent (login, permissions, sessions)
│   └── Firebase Sync Agent (real-time, cloud)
├── [HIGH] Data Integrity Agents
│   ├── User Data Agent (profiles, preferences)
│   └── Project Container Agent (projects, variants)
├── [MEDIUM] Core Domain Agents
│   ├── Phoneme System Agent (inventory, groups, types)
│   └── Content Structure Agent (words, syllables, positions)
└── [LOW] Feature Agents
    ├── Template Agent
    ├── TTS Agent
    ├── Teams Agent
    ├── Admin Agent
    └── Dashboard Agent
```

#### Context Model

Root manager has detailed STATIC context for CRITICAL components (always loaded — can intervene quickly). HIGH components have summary STATIC + detailed DYNAMIC. MEDIUM and LOW components are DYNAMIC-only at the manager level.

#### Strengths

- **Risk-aware delegation**: Manager can closely supervise database changes, loosely supervise dashboard tweaks
- **Failure response**: When critical components break, the manager has immediate context to triage
- **Testing priority**: Test critical components exhaustively, feature agents can have lighter testing
- **Matches operational reality**: You monitor your database more closely than your dashboard

#### Weaknesses

- Risk assessment is subjective and changes over time
- Low-risk components may get insufficient attention (Teams bugs can still frustrate users)
- Doesn't help with feature DEVELOPMENT (risk is about operations, not building)
- Can slow down development of critical components (too much oversight)

---

<!-- section_id: "23446a2b-a00d-47fe-a1fc-d957b2ec7b1a" -->
### Principle 11: Lifecycle/Temporal Hierarchy

**Rule**: Organize by WHEN things happen in the application lifecycle. Boot-time components at the root, session-time at the middle, interaction-time at the leaves.

**Question it answers**: "When in the app lifecycle does this component activate?"

**Primary axis**: Cascading Context (boot context is universal; session context builds on it; interaction context is transient)

#### Structure

```
Boot-Time (runs once at startup — universal context):
  L2: App Initialization (Flask app factory, config loading)
  L3: Database Setup (connection pool, schema verification)
  L4: Auth System Bootstrap (session management, OAuth init)

Session-Time (runs per user session):
  L5: User Login + Profile Load
  L6: Project Selection + Content Load
  L7: Template Application (filter phoneme system for active project)

Interaction-Time (runs per user action):
  L8: Content Creation (word/syllable CRUD)
  L9: TTS Generation (on-demand)
  L10: Team Actions (invite, share — event-driven)
  L11: Dashboard Refresh (re-render on every navigation)
```

#### What Cascades

Boot-time context (app config, DB connection info, auth setup) is available to ALL subsequent phases — it's truly universal. Session-time context (who's logged in, which project is active) cascades to all interaction-time agents. Interaction-time context is ephemeral and doesn't cascade.

#### Strengths

- Perfect match for cascading context axis (boot context → session context → interaction context)
- Agents know exactly when they're relevant (boot agents don't need to handle interaction events)
- Natural caching strategy (boot context cached once, session context cached per session, interaction context computed fresh)
- Clean initialization ordering

#### Weaknesses

- Many components span multiple lifecycle phases (auth is boot-time setup + interaction-time checking)
- Doesn't help with delegation (knowing when something runs doesn't tell you who should fix it)
- Phoneme system is awkward (loaded at boot but used at interaction time)
- Not intuitive for developers thinking about features

---

<!-- section_id: "72033379-fbec-45cb-8cc1-c505dac13340" -->
### Principle 12: API Surface Hierarchy

**Rule**: Organize by what INTERFACES components expose to other components. Components with the most consumers (widest API surface) sit at lower layers.

**Question it answers**: "How many other components depend on this component's interface?"

**Primary axis**: Cascading Context (interfaces cascade; implementations don't)

#### Interface Analysis for LangTrak

| Component | # of Consumers | Interface Surface |
|-----------|---------------|-------------------|
| Database (SQLite + Firestore) | ALL (16 modules) | `db.session`, query patterns, model classes |
| Auth | 14 modules | `@login_required`, `current_user`, permission checks |
| Users/Profiles | 10 modules | `User` model, user preferences, session data |
| Phoneme System | 6 modules | `Phoneme` model, IPA lookup, group membership |
| Templates | 4 modules | `Template` model, active phoneme filter |
| Projects | 5 modules | `Project` model, project-scoped queries |
| Content (Words) | 3 modules | `Word` model, syllable structure |
| Teams | 2 modules | `Team` model, membership check |
| TTS | 1 module | TTS API endpoint |
| Admin | 0 (standalone) | No outward API |

#### Structure

```
L2: Database Interface (consumed by everything — widest API)
L3: Auth Interface (consumed by 14/16 modules)
L4: User Interface (consumed by 10 modules)
L5: Phoneme System Interface (consumed by 6 modules)
L6: Project Interface (consumed by 5 modules)
L7: Template Interface (consumed by 4 modules)
L8: Content Interface (consumed by 3 modules)
L9: Teams Interface (consumed by 2 modules)
L10: TTS Interface (consumed by 1 module)
L11: Admin + Dashboard (standalone — no consumers)
```

#### What Cascades

The DATABASE INTERFACE cascades to everything — every agent knows how to query the DB. Auth interface cascades to everything that needs login. The cascading is purely about INTERFACES, not implementations. An agent at L8 knows the DB query patterns, auth decorators, user model, phoneme API, project API, and template API — but only the INTERFACES, not the internal implementations.

#### Context Model

Each agent's STATIC context contains:
- All interface definitions from lower layers (just function signatures, not implementations)
- Its OWN full implementation + interface

This is extremely efficient for cascading context — interfaces are small (a few function signatures), implementations are large. The cascade is lightweight.

#### Strengths

- **Minimizes interface discovery**: Every agent already knows what's available below it
- **Clean dependency inversion**: Agents depend on interfaces, not implementations
- **Efficient context**: Interface definitions are small; cascade overhead is minimal
- **Matches software engineering principles**: ISP, DIP from SOLID

#### Weaknesses

- Consumer count changes as app evolves (a new feature might give TTS 5 consumers)
- Pure interface ordering may conflict with domain logic (phonemes before projects?)
- Admin at L11 gets maximum cascade but needs nothing — wasteful
- Some interfaces are bidirectional (Projects query Content; Content references Projects)

---

<!-- section_id: "65463491-d52f-4f74-98c0-ab367429ce56" -->
### Principle 13: Concurrency/Isolation (Parallel Execution Tree)

**Rule**: Things that can be developed, tested, and modified INDEPENDENTLY sit as siblings. Things that require coordination sit in parent-child relationships.

**Question it answers**: "Can I work on these two things at the same time without conflicts?"

**Primary axis**: Delegation (maximize parallel work)

#### Independence Analysis

| Feature Pair | Independent? | Why |
|--------------|-------------|-----|
| Phonemes ↔ Teams | YES | Completely separate domains, no shared state |
| Phonemes ↔ Templates | NO | Templates filter phonemes — shared data model |
| Projects ↔ TTS | YES | TTS doesn't need project context |
| Content ↔ Phonemes | NO | Content references phonemes |
| Dashboard ↔ Admin | YES | Different UIs, different routes |
| Auth ↔ Database | NO | Auth depends on DB |

#### Structure

```
Root (coordinates all work)
├── BRANCH A: Sound Domain (must be sequential internally)
│   L4: Phoneme System → L5: Templates → (feeds into Branch B)
├── BRANCH B: Content Domain (sequential internally, parallel with C, D)
│   L6: Words → Syllables → Positions
├── BRANCH C: Organization Domain (parallel with B, D)
│   L7: Projects → L8: Teams
├── BRANCH D: Enhancement Domain (parallel with B, C)
│   L9: TTS, L10: Admin, L11: Dashboard (all independent leaves)
└── FOUNDATION (must complete before branches start)
    L2: Infrastructure → L3: Users
```

#### Agent Implications

- Foundation agents work first (sequential)
- Branch A works next (sequential within, but Branch B can START once A reaches Templates)
- Branches B, C, D work CONCURRENTLY after their dependencies are met
- Leaf nodes in Branch D are all independent — maximum parallelism

#### Strengths

- **Maximum parallelism**: Independent branches work simultaneously
- **Clear sequencing**: Dependencies are explicit (Foundation before Branches)
- **Efficient resource use**: More agents can work at the same time
- **Good for CI/CD**: Independent branches can be tested independently

#### Weaknesses

- Branch boundaries are static (if a new cross-branch dependency appears, the structure breaks)
- Branch assignment is complex (is Templates part of Sound Domain or Content Domain?)
- Doesn't help with context cascading (siblings don't cascade to each other)
- Some tasks inherently span branches (T5 team invitation needs Auth + Projects + Teams)

---

<!-- section_id: "8480e221-b8dd-4be9-96cf-cd05714406e6" -->
## Meta-Analysis: Which Axis Does Each Principle Serve?

| Principle | Cascading Context (top-down) | Delegation/Traversal (manager-worker) | Both? |
|-----------|:---:|:---:|:---:|
| 1. Dependency | Strong | Moderate | |
| 2. Containment | Moderate | Strong | |
| 3. User Interaction | Weak | Moderate | |
| 4. Change Frequency | Moderate | Weak | |
| 5. Data Flow | Strong | Moderate | |
| 6. Feature Coupling | Moderate | Strong | |
| 7. Skill/Capability | Weak | Strong | |
| 8. Knowledge Depth vs Breadth | | | Both |
| 9. Communication Topology | Weak | Strong | |
| 10. Risk/Criticality | | | Both |
| 11. Lifecycle/Temporal | Strong | Weak | |
| 12. API Surface | Strong | Moderate | |
| 13. Concurrency/Isolation | Weak | Strong | |

<!-- section_id: "7d41d811-91dd-4302-924e-71e0ef5bca3d" -->
### Key Insight

**No single principle optimizes both axes equally.** This is why hybrid approaches are necessary:

- **For cascading context**, the strongest principles are: Dependency (1), Data Flow (5), Lifecycle (11), API Surface (12)
- **For delegation/traversal**, the strongest are: Containment (2), Feature Coupling (6), Skill/Capability (7), Communication Topology (9), Concurrency (13)
- **Principles that serve BOTH axes** (Knowledge Depth, Risk/Criticality) tend to produce the most balanced hierarchies but may not excel at either

<!-- section_id: "ed08d350-1457-4db6-b029-4e1081c2433e" -->
### The Design Space

The ideal LangTrak agent hierarchy likely combines:
1. **A cascading-context principle** for the LAYER ORDERING (what context is universal)
2. **A delegation principle** for the AGENT TREE STRUCTURE (how managers delegate to workers)

These can be DIFFERENT principles applied at different levels:
- **Between layers**: Use dependency or API surface (cascading context)
- **Within layers**: Use feature coupling or skill clustering (delegation efficiency)
- **For the agent tree**: Use knowledge depth (generalist managers, specialist workers)

---

<!-- section_id: "e48fb586-1914-4f17-8287-9b7c40db1e79" -->
## Updated Hybrid Ideas

<!-- section_id: "20b44a99-b233-4666-b36c-45720f007b23" -->
### Hybrid 4: API Surface Ordering + Feature Coupling Clusters

Layers are ordered by interface consumer count (API surface). Within each layer, features are grouped by coupling (bounded contexts).

```
L2: Infrastructure Cluster (DB + Firebase + Storage — widest API)
L3: Identity Cluster (Auth + Users + Sessions — 14 consumers)
L4: Phoneme Domain Cluster (System + Templates + Types — 6 consumers)
L5: Content Cluster (Words + Syllables + Positions — 3 consumers)
L6: Project Cluster (Projects + Variants — 5 consumers)
L7: Collaboration Cluster (Teams + Sharing — 2 consumers)
L8: Enhancement Cluster (TTS + Suggestions — 1 consumer)
L9: Management Cluster (Admin + Dashboard — 0 consumers)
```

**Agent tree**: Root generalist → cluster specialists → feature experts (Principle 8)

**Why this works**: API surface gives clean cascading (interfaces are small, cascade is cheap). Feature coupling gives clean delegation (domain experts handle domain work). Knowledge depth gives clean agent tree.

<!-- section_id: "a30f05a8-5ea1-4bf3-ac4f-3bb3b31a6a6c" -->
### Hybrid 5: Risk-Aware Dependency with Communication-Optimized Hubs

Use dependency for layer ordering. Add risk-awareness to the manager's context model (critical components get more attention). Organize the agent TREE by communication topology (frequently-communicating agents are co-located).

```
Layer ordering (dependency): L2 Infra → L3 Users → L4 Phonemes → L5 Templates → L6 Content → L7 Projects → L8 Teams

Agent tree (communication hubs):
Root Manager [CRITICAL awareness: L2, Auth]
├── Phoneme-Content Hub (high-frequency pair)
│   ├── Phoneme Agent
│   ├── Template Agent
│   ├── Content Agent
│   └── TTS Agent
├── Identity Hub
│   ├── Auth Agent [CRITICAL]
│   ├── Users Agent
│   └── Infrastructure Agent [CRITICAL]
├── Project-Collaboration Hub
│   ├── Project Agent
│   ├── Teams Agent
│   └── Orchestration Agent
└── Management Hub
    ├── Admin Agent
    └── Dashboard Agent
```

**Why this works**: Dependency ordering ensures context cascades correctly. Communication hubs ensure agents that need to talk are co-located. Risk awareness ensures the manager closely supervises critical components.

<!-- section_id: "086e73b5-862f-4b7a-8af0-5aefc6142f48" -->
### Hybrid 6: Concurrency-First with Specialist Depth

Use independence analysis to create parallel branches. Within each branch, use knowledge depth (generalist branch manager → specialist leaf agents).

```
Foundation (sequential): Infrastructure → Auth → Users
                              ↓
              ┌───────────────┼───────────────┐
         Branch A         Branch B         Branch C
     Sound Domain      Content+Projects  Enhancements
      Specialist          Specialist       Specialist
      ├── Phoneme         ├── Word          ├── TTS
      │   Expert          │   Expert        │   Expert
      ├── Template        ├── Project       ├── Suggest
      │   Expert          │   Expert        │   Expert
      └── Frequency       ├── Team          └── Admin
          Expert          │   Expert            Expert
                          └── Variant
                              Expert
```

**Why this works**: Foundation runs first (unavoidable dependency). Then three branches work in parallel. Each branch has a domain specialist who routes to leaf experts. Maximizes both parallelism AND specialization.

---

<!-- section_id: "9478693a-89f3-49b2-b459-6018a14cdeba" -->
## Recommendation for Experiment

<!-- section_id: "83ca97f7-d382-4568-808d-55b448bc04a1" -->
### Original Trials (A-E): From experiment document

| Trial | Structure | Tests What |
|-------|-----------|-----------|
| A | One Agent Per Layer | Clean layer separation |
| B | Domain Clusters | Feature grouping |
| C | Stage-First | Workflow phases |
| D | Hybrid Layer+Stage | Both dimensions |
| E | Flat Team | No hierarchy at all |

<!-- section_id: "dd0c119a-308e-4936-b324-f29116c253bf" -->
### New Trials from Structural Ideas

| Trial | Principle(s) | Why Test It |
|-------|-----------|-------------|
| F | Containment (Principle 2) | Opposite ordering from dependency — tests ownership-based context cascade |
| G | Feature Coupling + Dependency hybrid (Hybrid 2) | Domain experts with dependency ordering between clusters |
| H | Stable Core + Volatile Shell (Hybrid 3) | Stability-based zones — tests change-frequency impact |
| I | Knowledge Depth + Feature Coupling (Hybrid 4/6) | Generalist managers → specialist → expert tree — tests whether 3-level depth helps |
| J | Communication-Optimized Hubs (Principle 9 + Hybrid 5) | Tests whether co-locating high-frequency communication pairs improves coordination |
| K | Concurrency-First Branches (Principle 13 + Hybrid 6) | Tests whether maximizing parallel execution improves throughput |

<!-- section_id: "f6ad2eee-bd7d-491d-acc1-4da866d99e69" -->
### Recommended First Trials (Maximum Variation)

Run these 4 first for maximum structural diversity:

1. **Trial B** (Domain Clusters) — baseline clustered approach
2. **Trial G** (Feature Coupling + Dependency) — strongest hybrid from Axis 1+2
3. **Trial I** (Knowledge Depth tree) — tests 3-level specialist depth
4. **Trial K** (Concurrency-First) — tests parallel execution optimization

These four test fundamentally different organizational philosophies: domain grouping, hybrid cascading+delegation, expertise depth, and parallel execution.

---

<!-- section_id: "96e8c020-369e-4586-9dd5-c6a3945be223" -->
## Next Steps

1. Add Trials F-K to the experiment document with concrete agent definitions
2. For Trials B, G, I, K (recommended first batch): define specific agent 0AGNOSTIC.md content
3. Create context model specifications for each trial (what's STATIC vs. DYNAMIC per agent)
4. Execute calibration tasks (T1, T2) for the first batch
5. Run full task suite and score results
6. Analyze which axis tradeoffs produced the best outcomes
