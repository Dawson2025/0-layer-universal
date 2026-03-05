---
resource_id: "f18a2262-3465-49ba-9862-87228788af9f"
resource_type: "output"
resource_name: "02_sublayer_dependency_structures"
---
# Sublayer Dependency Structures

**Status**: RESEARCH — Exploring how dependencies work WITHIN layers, not just between them
**Date**: 2026-02-26
**Companion to**: `01_hierarchy_structural_ideas.md` (which treats layers as atomic units)

---

## The Problem with Atomic Layers

Document 01 explored 13 principles for organizing the **ordering between layers**. But it treated each layer as a single, indivisible unit. In reality:

- **L2 Infrastructure** has Database, Firebase, Auth, Storage Manager, App Factory — and they depend on EACH OTHER internally
- **L4 Phoneme System** has Groups, Types, Individual Phonemes, Frequency Tracking — in a strict sequence
- **L6 Language Content** has Words containing Syllables containing Positions containing Phoneme References — a nested containment tree

Each layer is itself a miniature dependency system. The question this document explores: **How should we structure these internal dependencies, and what does that mean for agents?**

---

## Three Dependency Shapes

Dependencies within a layer (or between any set of components) follow one of three shapes:

### Shape 1: Dependency Sequence (Linear Chain)

```
A → B → C → D
```

Each component depends on exactly ONE predecessor. The chain is strict — you can't build C without B existing first.

**Properties:**
- One entry point (A) and one exit point (D)
- Order is unambiguous — there's exactly one valid build order
- Testing can follow the chain: test A first, then B with A, then C with A+B, etc.
- Failure at any point blocks everything after it

**LangTrak Example — L4 Phoneme System:**

```
Phoneme Groups → Phoneme Types → Individual Phonemes → Frequency Tracking
     (vowels,        (stops,         (specific IPA       (how often each
    consonants)      fricatives)      symbols: /p/,       phoneme appears
                                      /b/, /m/)           in user content)
```

- Groups MUST exist before Types (types belong to groups)
- Types MUST exist before Individual Phonemes (phonemes have a type)
- Individual Phonemes MUST exist before Frequency Tracking (you track frequency OF something)
- Each step depends on exactly the previous step

**Agent implication:** A sequential chain maps naturally to a pipeline of sub-agents, OR a single agent that processes steps in order. There's no parallelism possible — it's strictly sequential internally.

### Shape 2: Dependency Tree (Branching)

```
      A
    / | \
   B  C  D
      |
     E F
```

One root component, multiple children that depend on it. Children are INDEPENDENT of each other — they only depend on the root.

**Properties:**
- One entry point (root A), multiple exit points (leaves B, D, E, F)
- Children can be built IN PARALLEL (B, C, D don't depend on each other)
- The combined output of all leaves forms the layer's public interface
- Failure at a leaf only blocks that leaf's subtree, not siblings

**LangTrak Example — L7 Projects:**

```
          Project Core (CRUD, metadata)
          /        |          \          \
   Storage     Variants    Content       Settings
   Type Mgmt   (dup/fork)  Association   (preferences)
                            (links to L6)
```

- Project Core MUST exist before any sub-feature can work
- Storage Type, Variants, Content Association, and Settings are INDEPENDENT of each other
- They all depend on Project Core but NOT on each other
- Building Storage Type doesn't require Variants to exist

**Agent implication:** The root (Project Core) can be a single sub-agent, and the branches can be handled by parallel sub-agents or by a single agent that tackles them in any order. Maximum parallelism potential.

### Shape 3: Dependency DAG (Diamond/Graph)

```
       A
      / \
     B   C
      \ /
       D
       |
       E
```

Components have MULTIPLE dependencies. D depends on BOTH B and C. This creates "diamond" patterns where multiple paths converge.

**Properties:**
- Multiple valid build orders (B before C, or C before B, or B and C in parallel — but D must wait for BOTH)
- More complex than sequences or trees — requires dependency resolution
- Convergence points (D) need context from MULTIPLE predecessors
- Failure at B blocks D even if C succeeds

**LangTrak Example — L2 Infrastructure:**

```
         App Factory (Flask create_app)
          /                    \
   Database (SQLite)      Firebase (Cloud)
    - DB connection         - Firestore client
    - Schema setup          - Auth SDK
          \                    /
         Storage Manager
         (unified local/cloud interface)
                |
            Auth System
            (login, sessions, permissions)
            (needs DB for user storage + Storage Manager for dual-path)
```

- App Factory MUST exist first (Flask context needed by everything)
- Database and Firebase are INDEPENDENT of each other (neither needs the other)
- Storage Manager depends on BOTH Database AND Firebase (it unifies them)
- Auth depends on BOTH Database (user table) AND Storage Manager (dual-path storage)
- This is a DAG — not a simple tree or sequence

**Agent implication:** Diamond convergence points (Storage Manager, Auth) need context from multiple sources. A simple parent-child relay doesn't work — the Storage Manager agent needs to talk to BOTH the Database agent AND the Firebase agent. This requires either:
- A coordinator sub-agent that gathers from both and provides to the convergence point
- The convergence point agent directly querying multiple predecessors
- The layer agent acting as the coordinator (not delegating this part)

---

## Concrete LangTrak Sublayer Structures

Let's map every layer's internal dependency shape:

### L2: Infrastructure — DAG

```
         App Factory
          /       \
    Database     Firebase
     (SQLite)    (Cloud)
      |    \      /
      |    Storage Manager
      |        |
      Auth System
```

**Shape**: DAG (diamond at Storage Manager + convergence at Auth)
**Internal interfaces**: App provides Flask context. DB provides `db.session`. Firebase provides Firestore client. Storage Manager provides unified `storage.save()/load()`. Auth provides `@login_required`, `current_user`.
**Public layer interface** (what L3 Users sees): Auth check API + Storage API + DB session
**Build order**: App Factory → [Database, Firebase] in parallel → Storage Manager → Auth

### L3: Users — Sequence (simple)

```
User Model → User Profiles → Sessions
```

**Shape**: Simple sequence
**Internal interfaces**: User Model provides the `User` class. Profiles add preferences/settings. Sessions add login state.
**Public layer interface**: `current_user` (authenticated user with profile loaded)
**Build order**: User Model → Profiles → Sessions

### L4: Phoneme System — Sequence (with branch)

```
Phoneme Groups → Phoneme Types → Individual Phonemes
                                       |
                                 Frequency Tracking
                                       |
                                 Display/Hierarchy Views
```

**Shape**: Sequence with a trailing branch (Display depends on Phonemes but is independent of Frequency)
**Internal interfaces**: Groups provide categorization. Types provide subcategories. Phonemes provide the atomic sound units. Frequency provides usage stats. Display provides visualization.
**Public layer interface**: Phoneme inventory API (query by group, type, or individual. Get frequency. Render hierarchy views.)
**Build order**: Groups → Types → Phonemes → [Frequency, Display] in parallel

### L5: Templates — Tree (shallow)

```
Template Core (CRUD)
    /         \
Selection     Application
(choose       (apply template
phonemes)      to a project)
```

**Shape**: Shallow tree — Core is the root, Selection and Application are independent branches
**Internal interfaces**: Core provides `Template` model. Selection provides subset logic. Application provides project linkage.
**Public layer interface**: Template API (get available phonemes for a project's template)
**Build order**: Core → [Selection, Application] in parallel

### L6: Language Content — Deep Sequence (Containment Chain)

```
Words → Syllables → Positions → Phoneme References
```

**Shape**: Deep sequence — each level CONTAINS the next (a word contains syllables, a syllable contains positions, a position contains phoneme references)
**Note**: This is containment-as-dependency — the dependency IS the containment relationship
**Internal interfaces**: Words provide the vocabulary. Syllables provide structural breakdown. Positions provide onset/nucleus/coda slots. Phoneme References link to actual phonemes from L4.
**Public layer interface**: Content API (create/read/update/delete words with full syllable → position → phoneme structure)
**Build order**: Words → Syllables → Positions → Phoneme References (strictly sequential — can't have syllables without words)

### L7: Projects — Star/Hub

```
    Project Core
   / |    |     \
Storage Variants Content  Settings
Type             Assoc.
```

**Shape**: Star/hub — everything depends on the core, nothing depends on each other
**Internal interfaces**: Core provides `Project` model. Each branch adds a specific capability.
**Public layer interface**: Project API (CRUD projects with storage type, variants, content, settings)
**Build order**: Core → [Storage Type, Variants, Content Assoc., Settings] all in parallel

### L8: Teams — Sequence (short)

```
Team Model → Membership → Invite System → Project Sharing
```

**Shape**: Short sequence
**Internal interfaces**: Team Model provides the `Team` class. Membership adds member management. Invites add invite codes. Sharing adds project access.
**Public layer interface**: Collaboration API (create team, invite members, share projects)
**Build order**: Team Model → Membership → Invites → Sharing

### L9-L11: Cross-Cutting — Independent Leaves

```
L9: TTS    Video    Suggestions   (three independent enhancements)
L10: Admin  Dashboard  Menu       (three independent management tools)
L11: Firebase-Orch  Universal-Orch  Meta-AI-Orch  (three independent orchestrators)
```

**Shape**: Flat — all components within each cross-cutting layer are independent of each other
**Internal interfaces**: Each component has its own API.
**Public layer interface**: Multiple independent APIs (no aggregation needed)
**Build order**: All parallel within each layer

---

## The "Giant Dependency" Concept

This is the key insight: **sublayers form internal dependency chains, but collectively they produce ONE interface that the next layer depends on.**

```
L4 internally:  Groups → Types → Phonemes → Frequency → Display
L4's output:    "Phoneme Inventory API"

L5 only sees:   "Phoneme Inventory API" (doesn't know about groups, types, frequency, display)
L5 internally:  Core → [Selection, Application]
L5's output:    "Template API"

L6 only sees:   "Template API" (doesn't know about selection vs application logic)
```

This is **interface aggregation** — the sublayer complexity is hidden behind a clean public interface. It's exactly like a software module with private implementation and public API.

### Three Levels of Structure

```
┌─────────────────────────────────────────────────────┐
│  BETWEEN LAYERS (Principles 1-13 from document 01) │
│                                                      │
│  L2 ─────→ L3 ─────→ L4 ─────→ L5 ─────→ L6       │
│  Infra      Users     Phonemes  Templates  Content  │
│                                                      │
│  Each arrow = "public interface dependency"          │
│  Each box = an aggregated interface                  │
├──────────────────────────────────────────────────────┤
│  WITHIN LAYERS (this document)                       │
│                                                      │
│  L4 = Groups → Types → Phonemes → Frequency         │
│       (sequence)                                     │
│                                                      │
│  L7 = Core → [Storage, Variants, Assoc., Settings]  │
│       (star/hub)                                     │
│                                                      │
│  L2 = App → [DB, Firebase] → Storage Mgr → Auth     │
│       (DAG)                                          │
│                                                      │
│  Each internal arrow = "sublayer dependency"         │
├──────────────────────────────────────────────────────┤
│  WITHIN SUBLAYERS (recursive depth)                  │
│                                                      │
│  Database sublayer of L2:                            │
│    Connection Pool → Schema → Migration → Query API  │
│    (sub-sublayer sequence)                           │
│                                                      │
│  Types sublayer of L4:                               │
│    Group Assignment → Naming → Display Rules         │
│    (sub-sublayer sequence)                           │
│                                                      │
│  How deep do we go? This is the depth question.      │
└──────────────────────────────────────────────────────┘
```

---

## Sublayer Depth: How Deep Should Internal Structure Go?

### Option A: Two Levels Only (Layers + Sublayers)

```
Layer (L4: Phoneme System)
├── Sublayer (Groups)
├── Sublayer (Types)
├── Sublayer (Phonemes)
└── Sublayer (Frequency)
```

**No sub-sublayers.** Each sublayer is atomic. If there's internal complexity within a sublayer (e.g., "Types" has group assignment, naming, display rules), it's all one thing.

**Pros**: Simple, easy to reason about, each sublayer = one agent or one agent's task
**Cons**: Some sublayers are still complex (Database sublayer has connection, schema, migration, query patterns)
**When to use**: Small-to-medium projects, layers with few components (< 8 sublayers)

### Option B: Three Levels (Layers + Sublayers + Sub-sublayers)

```
Layer (L2: Infrastructure)
├── Sublayer (Database)
│   ├── Sub-sublayer (Connection Pool)
│   ├── Sub-sublayer (Schema)
│   └── Sub-sublayer (Migration)
├── Sublayer (Firebase)
│   ├── Sub-sublayer (Firestore Client)
│   └── Sub-sublayer (Auth SDK)
├── Sublayer (Storage Manager)
└── Sublayer (Auth System)
```

**Three levels of nesting.** Sublayers can have their own internal components.

**Pros**: Matches the actual code structure (packages → modules → classes), handles complex sublayers
**Cons**: More complex, more agents/sub-agents to coordinate, deeper delegation chains
**When to use**: Complex layers with internally complex sublayers

### Option C: Recursive (Fractal — Layers All the Way Down)

```
Layer (L4: Phoneme System)
├── Sublayer (Groups)
│   ├── Sub-sublayer (Group Categories)
│   │   ├── Sub-sub-sublayer (Vowel Rules)
│   │   └── Sub-sub-sublayer (Consonant Rules)
│   └── Sub-sublayer (Group Display)
├── Sublayer (Types)
│   ├── Sub-sublayer (Type Definition)
│   │   ├── Sub-sub-sublayer (Stop Consonants)
│   │   └── Sub-sub-sublayer (Fricatives)
│   └── Sub-sublayer (Type Navigation)
...
```

**No limit on depth.** Each sublayer can have sub-sublayers which can have sub-sub-sublayers.

**Pros**: Models any complexity level, matches recursive directory structures, each leaf is truly atomic
**Cons**: Can become absurdly deep, coordination overhead grows exponentially, context chains become unmanageable
**When to use**: Never in practice — this is the theoretical extreme. Real systems should cap depth.

### Recommended: Adaptive Depth (2 levels default, 3 when needed)

```
Rule: Default to 2 levels (Layer + Sublayers).
      Add a 3rd level ONLY when a sublayer has 4+ internal components
      that have their own dependency relationships.

L2 Infrastructure → 3 levels (Database has Connection/Schema/Migration, Firebase has Firestore/Auth)
L3 Users → 2 levels (simple — 3 sublayers, all atomic)
L4 Phoneme System → 2 levels (4 sublayers but each is atomic)
L5 Templates → 2 levels (3 sublayers, each atomic)
L6 Language Content → 2 levels (4 sublayers in containment chain)
L7 Projects → 2 levels (star with 5 sublayers, each atomic)
L8 Teams → 2 levels (4 sublayers in sequence)
L9-L11 → 2 levels (independent leaf components)
```

Only L2 (Infrastructure) actually needs 3 levels. Everything else works fine at 2.

---

## Agent Implications: How Sublayers Change the Agent Tree

### Model 1: One Agent Per Layer (sublayers are internal tasks)

The layer agent handles ALL sublayers itself. Sublayers aren't separate agents — they're tasks the layer agent works through.

```
Phoneme System Agent
  - Task 1: Set up Groups
  - Task 2: Set up Types
  - Task 3: Set up Phonemes
  - Task 4: Set up Frequency Tracking
```

**When this works**: When sublayers are simple and the layer agent has enough context to handle all of them. Good for 2-level depth with < 5 sublayers.
**When this breaks**: When sublayers are complex enough to need specialized knowledge (e.g., Firebase sublayer needs Firestore expertise that's very different from SQLite expertise).

### Model 2: Layer Agent + Sub-Agents

The layer agent coordinates sub-agents for complex sublayers. Simple sublayers stay as tasks; complex ones get their own agent.

```
Infrastructure Agent (coordinator)
├── Database Sub-Agent (handles Connection, Schema, Migration)
├── Firebase Sub-Agent (handles Firestore, Auth SDK)
├── Storage Manager task (simple — Infrastructure Agent handles directly)
└── Auth task (simple — Infrastructure Agent handles directly)
```

**When this works**: Complex layers (L2 Infrastructure) where sublayers need different expertise. The layer agent acts as a mini-manager.
**When this breaks**: When too many sub-agents create coordination overhead that exceeds the benefit of specialization.

### Model 3: Sublayers as First-Class Agents (Flat Within Layer)

Each sublayer gets its own agent, and they communicate peer-to-peer within the layer. The layer agent is just a router/coordinator.

```
Infrastructure Layer Router
├── App Factory Agent
├── Database Agent
├── Firebase Agent
├── Storage Manager Agent
└── Auth Agent

(Database Agent and Firebase Agent can work in parallel.
 Storage Manager Agent waits for both.
 Auth Agent waits for Storage Manager.)
```

**When this works**: When sublayers have complex internal state, need different tools, and the dependency shape benefits from parallel execution (DAGs especially).
**When this breaks**: When the router becomes a bottleneck and agents need to understand the layer-level interface (which is an aggregation of all sublayers).

### Recommendation: Adaptive Model

```
Simple layers (sequence, <5 sublayers): Model 1 — one agent handles all
Complex layers (DAG, >5 sublayers): Model 2 — agent + sub-agents for complex parts
Cross-cutting layers (independent leaves): Model 3 — independent agents, light router
```

For LangTrak:
- L2 Infrastructure → Model 2 (DAG, complex sublayers)
- L3 Users → Model 1 (simple sequence)
- L4 Phoneme System → Model 1 (sequence, 4 sublayers)
- L5 Templates → Model 1 (shallow tree, 3 sublayers)
- L6 Language Content → Model 1 (sequence, 4 sublayers)
- L7 Projects → Model 1 (star/hub, 5 sublayers but all simple)
- L8 Teams → Model 1 (short sequence)
- L9-L11 Cross-cutting → Model 3 (independent components)

---

## Interface Aggregation Patterns

How sublayers' outputs combine into the layer's public interface:

### Pattern A: Sequential Aggregation

Each sublayer builds on the previous, and the LAST sublayer's output IS the layer interface.

```
Groups → Types → Phonemes → Frequency
                                 ↓
                        Layer Interface = "Phoneme Inventory API"
                        (the final output includes everything built up through the chain)
```

**Context implication**: The next layer (L5 Templates) only needs to know about the aggregated API. It doesn't need to understand that groups exist separately from types — it just queries "give me phonemes."

### Pattern B: Hub Aggregation

A central component collects outputs from all sublayers and produces a unified interface.

```
Storage Type ──→
Variants     ──→  Project Core (hub)  ──→  Layer Interface = "Project API"
Content Assoc ──→
Settings     ──→
```

**Context implication**: The hub (Project Core) acts as the aggregation point. The next layer (L8 Teams) talks to the Project API, which internally routes to the right sublayer.

### Pattern C: Faceted Aggregation

Multiple sublayers each expose PART of the layer interface. The layer interface is a collection of independent facets, not a single unified API.

```
TTS   ──→ "TTS API"       ─┐
Video ──→ "Video API"       ├──→ Layer Interface = Collection of Enhancement APIs
Suggest ──→ "Suggest API"  ─┘
```

**Context implication**: Consumers of this layer may only need ONE facet (e.g., only TTS, not Video). The layer interface is more like a catalog than a single endpoint.

### Pattern D: Diamond Aggregation

Multiple paths converge, and the convergence point IS the layer interface.

```
Database ──┐
            ├──→ Storage Manager ──→ Auth ──→ Layer Interface = "Infrastructure API"
Firebase ──┘
```

**Context implication**: The convergence point (Storage Manager, then Auth) integrates multiple paths. The layer interface reflects the merged capabilities.

---

## How This Interacts with the Two Design Axes

### Cascading Context Axis

**Sublayers WITHIN a layer** do NOT cascade to external layers. Only the layer's **aggregated interface** cascades.

```
L4 internally: Groups → Types → Phonemes → Frequency (PRIVATE)
L4 interface:  "Phoneme Inventory API"                (PUBLIC — this cascades to L5, L6, etc.)
```

This is critical: the cascading context between layers stays LEAN because sublayer details are hidden. An agent at L6 doesn't need to know about phoneme groups — it just queries the Phoneme Inventory API.

**But WITHIN a layer**, sublayer context DOES cascade internally:
- The Types sub-agent inherits Groups context
- The Phonemes sub-agent inherits Groups + Types context
- This is a PRIVATE cascade within the layer

### Delegation Axis

**Between layers**: Delegation follows the inter-layer hierarchy (Manager → L4 agent → L5 agent)
**Within layers**: Delegation follows the sublayer dependency shape

For a sequence: Layer agent delegates sequentially (do A, then B, then C)
For a tree: Layer agent delegates in parallel (do B, C, D simultaneously after A)
For a DAG: Layer agent resolves the dependency graph (do B and C in parallel, then D after both finish)

```
Task: "Add a new phoneme type"

Inter-layer delegation:
  Manager → L4 Phoneme System Agent

Intra-layer delegation (within L4):
  L4 Agent → Check Groups (sublayer 1) → Add Type (sublayer 2) → Register Phonemes (sublayer 3)
  (sequential delegation following the internal sequence)
```

---

## New Experiment Trials Based on Sublayer Structures

| Trial | Structure | What It Tests |
|-------|-----------|---------------|
| L | Flat sublayers (Model 1 everywhere) | Can a single agent per layer handle all internal complexity? |
| M | Adaptive sublayers (Model 1/2/3 based on complexity) | Does matching agent model to dependency shape improve performance? |
| N | Deep sublayers (3 levels, sub-agents for everything) | Does maximum specialization outweigh coordination overhead? |

### Trial L: Flat Sublayers (Single Agent Per Layer)

Each layer gets exactly ONE agent. That agent handles all sublayers as internal tasks. No sub-agents.

```
Manager
├── L2 Agent (handles App, DB, Firebase, Storage Mgr, Auth as tasks)
├── L3 Agent (handles Users, Profiles, Sessions as tasks)
├── L4 Agent (handles Groups, Types, Phonemes, Frequency as tasks)
├── L5 Agent (handles Core, Selection, Application as tasks)
├── L6 Agent (handles Words, Syllables, Positions, Refs as tasks)
├── L7 Agent (handles Core, Storage, Variants, Assoc, Settings as tasks)
├── L8 Agent (handles Teams, Membership, Invites, Sharing as tasks)
└── L9-L11 Agent(s) (handles cross-cutting as tasks)
```

**Predicted outcome**: Works well for simple layers (L3, L5, L8). Struggles for L2 (DAG is hard for one agent to manage) and for tasks spanning multiple sublayers that need different expertise.

### Trial M: Adaptive Sublayers (Matched to Dependency Shape)

Layer agent model chosen based on sublayer dependency shape:

```
Manager
├── L2: Model 2 — Agent + Sub-Agents
│   ├── DB Sub-Agent
│   ├── Firebase Sub-Agent
│   └── L2 Agent handles Storage Mgr + Auth directly
├── L3: Model 1 — Single Agent (simple sequence)
├── L4: Model 1 — Single Agent (sequence, each step atomic)
├── L5: Model 1 — Single Agent (shallow tree)
├── L6: Model 1 — Single Agent (containment sequence)
├── L7: Model 1 — Single Agent (star/hub, simple branches)
├── L8: Model 1 — Single Agent (short sequence)
├── L9: Model 3 — Independent Agents per enhancement
│   ├── TTS Agent
│   ├── Video Agent
│   └── Suggestions Agent
├── L10: Model 3 — Independent Agents per admin tool
└── L11: Model 3 — Independent Agents per orchestrator
```

**Predicted outcome**: Best balance — complex areas (L2) get sub-agents, simple areas stay lean, cross-cutting areas get independence. Predicted to outperform flat (Trial L) on L2 tasks specifically.

### Trial N: Deep Sublayers (Maximum Specialization)

Every sublayer with >1 internal component gets its own sub-agent. Sub-sublayers get sub-sub-agents.

```
Manager
├── L2 Agent (coordinator only)
│   ├── App Factory Agent
│   ├── Database Agent
│   │   ├── Connection Sub-Agent
│   │   ├── Schema Sub-Agent
│   │   └── Migration Sub-Agent
│   ├── Firebase Agent
│   │   ├── Firestore Sub-Agent
│   │   └── Auth SDK Sub-Agent
│   ├── Storage Manager Agent
│   └── Auth System Agent
├── L4 Agent (coordinator only)
│   ├── Groups Agent
│   ├── Types Agent
│   ├── Phonemes Agent
│   ├── Frequency Agent
│   └── Display Agent
... (every sublayer has its own agent)
```

**Predicted outcome**: Maximum specialization but maximum coordination overhead. Predicted to be SLOWEST due to delegation hops: Manager → L2 → Database → Schema Agent = 3 hops for a schema change. But might produce the most ACCURATE results because each agent is laser-focused.

---

## Key Insight: The Fractal Nature of Agent Hierarchies

The same structural choices that apply BETWEEN layers also apply WITHIN layers. You can:

1. Use **dependency ordering** between sublayers just like between layers
2. Use **interface aggregation** to hide sublayer complexity just like hiding layer internals
3. Choose **flat vs. deep** agent trees within layers just like choosing hierarchy depth overall
4. Apply **cascading context** within layers (sublayer context cascades to later sublayers)

This means the agent hierarchy is potentially **fractal** — the same pattern repeats at every level of zoom:

```
System level:  Root → Layer → Layer → Layer
Layer level:   Layer Agent → Sublayer → Sublayer → Sublayer
Sublayer level: Sublayer Agent → Sub-sublayer → Sub-sublayer

Same principles, different scales.
```

The practical question isn't "how deep CAN we go?" (answer: infinitely deep, in theory). It's "how deep SHOULD we go before the coordination overhead exceeds the specialization benefit?"

Based on LangTrak's concrete structure, the answer appears to be **2-3 levels max**:
- Most layers need only 2 levels (layer + sublayers)
- Only L2 Infrastructure benefits from 3 levels
- Going deeper than 3 would create sub-sub-agents so narrow they can't do useful work

---

## Relationship to Document 01 Principles

| Doc 01 Principle | How Sublayers Interact |
|-----------------|----------------------|
| Dependency (P1) | Internal dependency shapes (sequence, tree, DAG) are mini-dependency hierarchies |
| Containment (P2) | L6 Language Content is pure containment internally (Word contains Syllable contains Position) |
| Feature Coupling (P6) | Sublayers within a layer are tightly coupled BY DEFINITION — they're in the same layer because they belong together |
| Knowledge Depth (P8) | Sublayer agents are the DEEPEST specialists — they know one tiny piece extremely well |
| API Surface (P12) | Interface aggregation patterns determine what the layer exposes (sequential, hub, faceted, diamond) |
| Concurrency (P13) | Sublayer dependency shapes determine what can run in parallel (trees and independent DAG branches allow parallelism; sequences don't) |

---

## Next Steps

1. Add Trials L, M, N to the experiment document
2. For each LangTrak layer, formally document the sublayer dependency shape and interface aggregation pattern
3. Design the concrete context model for adaptive sublayers (Trial M) — what goes in each sub-agent's context
4. Consider whether sublayer structure should inform the BETWEEN-layer ordering (e.g., layers with complex DAGs might need to be closer to the manager for better coordination)
