---
resource_id: "7ca50f31-d869-4a7b-afb4-40b4e08fdf1d"
resource_type: "output"
resource_name: "oop_class_hierarchy"
---
# OOP Class Hierarchy for Dependency-Based Agent Structure

**Status**: DESIGN
**Date**: 2026-02-26
**Companion to**: `dependency_based_agent_hierarchy_design.md`
**Principle**: Map the 7-layer, 38-sub-layer LangTrak hierarchy to OOP classes using best practices (SOLID, composition over inheritance, interface segregation)

---

<!-- section_id: "6ffb6221-6e1a-455a-854e-dea671eb9630" -->
## Design Rules Applied

| OOP Principle | How It's Applied |
|---------------|-----------------|
| **SRP** (Single Responsibility) | Each class has exactly one domain. Sub-layer classes handle one feature. |
| **OCP** (Open/Closed) | New sub-layers = new classes. Existing classes don't change. |
| **LSP** (Liskov Substitution) | Any sub-layer implementing an interface can replace another implementer. |
| **ISP** (Interface Segregation) | Small, focused interfaces. Agents only depend on interfaces they use. |
| **DIP** (Dependency Inversion) | Layer agents depend on interfaces, not concrete sub-layer implementations. |
| **Composition over Inheritance** | Sub-layers are composed (has-a), not inherited (is-a). Max inheritance depth = 3. |
| **Encapsulation** | Sub-layers are private. Only the layer's aggregated interface is public. |

---

<!-- section_id: "2419d309-570e-42e7-b11a-cdf229eda351" -->
## Interfaces (Contracts Between Layers)

Interfaces define what each layer PROVIDES to the layers above it. They're small, segregated, and focused.

```
┌─────────────────────────────────────────────────────────────┐
│  INTERFACES (what layers expose to each other)              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  «interface» IStorageProvider                               │
│  ───────────────────────                                    │
│  + save(data) → Result                                      │
│  + load(id) → Data                                          │
│  + delete(id) → Result                                      │
│  + query(filter) → List[Data]                               │
│                                                             │
│  «interface» IAuthProvider                                  │
│  ───────────────────────                                    │
│  + login(credentials) → User                                │
│  + logout() → void                                          │
│  + check_auth() → bool                                      │
│  + get_current_user() → User                                │
│                                                             │
│  «interface» IUserProvider                                  │
│  ───────────────────────                                    │
│  + get_user(id) → User                                      │
│  + get_profile(user_id) → Profile                           │
│  + get_session() → Session                                  │
│                                                             │
│  «interface» IPhonemeProvider                               │
│  ───────────────────────                                    │
│  + get_phoneme(id) → Phoneme                                │
│  + list_by_group(group) → List[Phoneme]                     │
│  + list_by_type(type) → List[Phoneme]                       │
│  + get_all() → List[Phoneme]                                │
│                                                             │
│  «interface» IPhonemeAudio                                  │
│  ───────────────────────                                    │
│  + get_audio(phoneme_id) → AudioData                        │
│  + generate_tts(ipa_symbol) → AudioData                     │
│                                                             │
│  «interface» IFrequencyProvider                             │
│  ───────────────────────                                    │
│  + get_frequency(phoneme_id) → float                        │
│  + get_top_phonemes(n) → List[Phoneme]                      │
│                                                             │
│  «interface» IPhonemeAdmin                                  │
│  ───────────────────────                                    │
│  + create_phoneme(data) → Phoneme                           │
│  + update_phoneme(id, data) → Phoneme                       │
│  + delete_phoneme(id) → Result                              │
│  + create_group(data) → Group                               │
│                                                             │
│  «interface» ITemplateProvider                              │
│  ───────────────────────                                    │
│  + get_template(id) → Template                              │
│  + get_available_phonemes(template_id) → List[Phoneme]      │
│  + apply_to_project(template_id, project_id) → Result       │
│                                                             │
│  «interface» IContentProvider                               │
│  ───────────────────────                                    │
│  + get_word(id) → Word                                      │
│  + create_word(data) → Word                                 │
│  + get_syllables(word_id) → List[Syllable]                  │
│  + get_suggestions(template_id) → List[WordSuggestion]      │
│                                                             │
│  «interface» IContentAudio                                  │
│  ───────────────────────                                    │
│  + get_word_audio(word_id) → AudioData                      │
│  + get_syllable_audio(syllable_id) → AudioData              │
│                                                             │
│  «interface» IProjectProvider                               │
│  ───────────────────────                                    │
│  + get_project(id) → Project                                │
│  + list_projects(user_id) → List[Project]                   │
│  + get_dashboard(user_id) → DashboardData                   │
│                                                             │
│  «interface» ICollaborationProvider                         │
│  ───────────────────────                                    │
│  + get_team(id) → Team                                      │
│  + invite_member(team_id, user_id) → Invite                 │
│  + share_project(team_id, project_id) → Result              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

<!-- section_id: "25a71b92-20cc-4c62-99e6-224c97838502" -->
### Interface Segregation Map

Which layer agent USES which interfaces:

| Agent | Provides | Uses (depends on) |
|-------|---------|-------------------|
| L2 InfrastructureAgent | IStorageProvider, IAuthProvider | — |
| L3 UserAgent | IUserProvider | IStorageProvider, IAuthProvider |
| L4 PhonemeAgent | IPhonemeProvider, IPhonemeAudio, IFrequencyProvider, IPhonemeAdmin | IUserProvider |
| L5 TemplateAgent | ITemplateProvider | IPhonemeProvider |
| L6 ContentAgent | IContentProvider, IContentAudio | ITemplateProvider, IPhonemeAudio |
| L7 ProjectAgent | IProjectProvider | IContentProvider |
| L8 TeamAgent | ICollaborationProvider | IProjectProvider, IUserProvider |

Each agent only depends on the INTERFACES it actually uses — not the full implementation of the layer below.

---

<!-- section_id: "7ec0aa20-ebdb-487e-b31e-ce56a1824f31" -->
## Abstract Base Classes (Inheritance Chain)

Three levels of inheritance — no deeper.

```
«abstract» BaseAgent
│
│  Every agent in the system inherits from this.
│  Provides universal capabilities that ALL agents need.
│
│  Properties:
│  ─────────
│  + agent_id: str
│  + agent_name: str
│  + scope_description: str
│  + static_context: Context         ← own STATIC from 0AGNOSTIC.md
│  + neighbor_interfaces: Dict       ← compact summaries of neighbors
│
│  Methods:
│  ───────
│  + load_context() → void           ← read own 0AGNOSTIC.md
│  + delegate(task, target) → Result ← send work to another agent
│  + report(result) → void           ← send result back to delegator
│  + is_in_scope(task) → bool        ← check if task belongs to this agent
│  + escalate(task) → void           ← send out-of-scope work upward
│
├───────────────────────────────────────────────────────────────
│
├── «abstract» LayerAgent extends BaseAgent
│   │
│   │  An agent that owns a complete layer with sub-layers.
│   │  This is the DOMAIN EXPERT level.
│   │
│   │  Properties:
│   │  ─────────
│   │  + layer_number: int               ← L2, L3, etc.
│   │  + sub_layers: List[SubLayerAgent]  ← COMPOSITION (has-a)
│   │  + provided_interfaces: List[Interface]
│   │  + consumed_interfaces: List[Interface]
│   │  + public_interface: AggregatedInterface  ← what the next layer sees
│   │
│   │  Methods:
│   │  ───────
│   │  + delegate_to_sublayer(task) → Result   ← route work internally
│   │  + aggregate_interface() → Interface      ← combine sub-layer outputs
│   │  + get_dependency_shape() → Shape         ← sequence, tree, DAG, star
│   │  + can_parallelize(tasks) → List[List]    ← which tasks can run concurrently
│   │
│   ├── InfrastructureAgent extends LayerAgent    ← L2
│   ├── UserAgent extends LayerAgent              ← L3
│   ├── PhonemeAgent extends LayerAgent            ← L4
│   ├── TemplateAgent extends LayerAgent           ← L5
│   ├── ContentAgent extends LayerAgent            ← L6
│   ├── ProjectAgent extends LayerAgent            ← L7
│   └── TeamAgent extends LayerAgent               ← L8
│
├───────────────────────────────────────────────────────────────
│
├── «abstract» SubLayerAgent extends BaseAgent
│   │
│   │  An agent that handles ONE sub-feature within a layer.
│   │  The most specialized level — deep expertise, narrow scope.
│   │
│   │  Properties:
│   │  ─────────
│   │  + sublayer_id: str                ← L4.3, L2.5, etc.
│   │  + parent_layer: LayerAgent        ← reference to owning layer (COMPOSITION)
│   │  + internal_dependencies: List[str] ← which other sub-layers this depends on
│   │  + domain_context: Context          ← deep specialized knowledge
│   │
│   │  Methods:
│   │  ───────
│   │  + execute(task) → Result           ← do the actual work
│   │  + needs_sibling(task) → str|None   ← does this need another sub-layer?
│   │  + get_capability() → Interface     ← what this sub-layer can do
│   │
│   ├── (L2 sub-layers)
│   │   ├── AppFactoryAgent extends SubLayerAgent
│   │   ├── DatabaseAgent extends SubLayerAgent
│   │   ├── FirebaseAgent extends SubLayerAgent
│   │   ├── StorageManagerAgent extends SubLayerAgent
│   │   ├── AuthSystemAgent extends SubLayerAgent
│   │   ├── DbAdminAgent extends SubLayerAgent
│   │   └── FirebaseSyncAgent extends SubLayerAgent
│   │
│   ├── (L3 sub-layers)
│   │   ├── UserModelAgent extends SubLayerAgent
│   │   ├── ProfilesAgent extends SubLayerAgent
│   │   └── SessionsAgent extends SubLayerAgent
│   │
│   ├── (L4 sub-layers)
│   │   ├── PhonemeGroupsAgent extends SubLayerAgent
│   │   ├── PhonemeTypesAgent extends SubLayerAgent
│   │   ├── IndividualPhonemesAgent extends SubLayerAgent
│   │   ├── FrequencyTrackingAgent extends SubLayerAgent
│   │   ├── PhonemeDisplayAgent extends SubLayerAgent
│   │   ├── PhonemeTtsAgent extends SubLayerAgent
│   │   └── PhonemeAdminAgent extends SubLayerAgent
│   │
│   ├── (L5 sub-layers)
│   │   ├── TemplateCoreAgent extends SubLayerAgent
│   │   ├── PhonemeSelectionAgent extends SubLayerAgent
│   │   ├── TemplateApplicationAgent extends SubLayerAgent
│   │   └── TemplateAdminAgent extends SubLayerAgent
│   │
│   ├── (L6 sub-layers)
│   │   ├── WordsAgent extends SubLayerAgent
│   │   ├── SyllablesAgent extends SubLayerAgent
│   │   ├── PositionsAgent extends SubLayerAgent
│   │   ├── PhonemeReferencesAgent extends SubLayerAgent
│   │   ├── ContentTtsAgent extends SubLayerAgent
│   │   ├── SuggestionsAgent extends SubLayerAgent
│   │   └── VideoAgent extends SubLayerAgent
│   │
│   ├── (L7 sub-layers)
│   │   ├── ProjectCoreAgent extends SubLayerAgent
│   │   ├── StorageTypeAgent extends SubLayerAgent
│   │   ├── VariantsAgent extends SubLayerAgent
│   │   ├── ContentAssociationAgent extends SubLayerAgent
│   │   ├── DashboardAgent extends SubLayerAgent
│   │   └── MenuAgent extends SubLayerAgent
│   │
│   └── (L8 sub-layers)
│       ├── TeamModelAgent extends SubLayerAgent
│       ├── MembershipAgent extends SubLayerAgent
│       ├── InvitesAgent extends SubLayerAgent
│       └── ProjectSharingAgent extends SubLayerAgent
│
├───────────────────────────────────────────────────────────────
│
└── ManagerAgent extends BaseAgent
    │
    │  The top-level coordinator. NOT a LayerAgent — it doesn't own a domain.
    │  It's the Factory + Mediator.
    │
    │  Properties:
    │  ─────────
    │  + layer_agents: List[LayerAgent]     ← all 7 layer agents (COMPOSITION)
    │  + routing_table: Dict[str, LayerAgent] ← keyword → agent mapping
    │  + layer_overview: Dict               ← 2-3 line summary per layer
    │
    │  Methods:
    │  ───────
    │  + route_task(task) → LayerAgent       ← identify which layer handles this
    │  + delegate(task, layer) → Result      ← send to a specific layer agent
    │  + coordinate(tasks) → List[Result]    ← handle multi-layer tasks
    │  + get_status() → SystemStatus         ← aggregate status from all layers
```

---

<!-- section_id: "303959ad-8b4b-4ee9-96cb-5961b056aaea" -->
## Composition Structure (Has-A Relationships)

This is the ACTUAL object graph at runtime — who CONTAINS whom.

```
ManagerAgent
│
├── has-a InfrastructureAgent (L2)
│   ├── has-a AppFactoryAgent (L2.1)
│   ├── has-a DatabaseAgent (L2.2)
│   ├── has-a FirebaseAgent (L2.3)
│   ├── has-a StorageManagerAgent (L2.4)
│   ├── has-a AuthSystemAgent (L2.5)
│   ├── has-a DbAdminAgent (L2.6)
│   └── has-a FirebaseSyncAgent (L2.7)
│
├── has-a UserAgent (L3)
│   ├── has-a UserModelAgent (L3.1)
│   ├── has-a ProfilesAgent (L3.2)
│   └── has-a SessionsAgent (L3.3)
│
├── has-a PhonemeAgent (L4)
│   ├── has-a PhonemeGroupsAgent (L4.1)
│   ├── has-a PhonemeTypesAgent (L4.2)
│   ├── has-a IndividualPhonemesAgent (L4.3)
│   ├── has-a FrequencyTrackingAgent (L4.4)
│   ├── has-a PhonemeDisplayAgent (L4.5)
│   ├── has-a PhonemeTtsAgent (L4.6)
│   └── has-a PhonemeAdminAgent (L4.7)
│
├── has-a TemplateAgent (L5)
│   ├── has-a TemplateCoreAgent (L5.1)
│   ├── has-a PhonemeSelectionAgent (L5.2)
│   ├── has-a TemplateApplicationAgent (L5.3)
│   └── has-a TemplateAdminAgent (L5.4)
│
├── has-a ContentAgent (L6)
│   ├── has-a WordsAgent (L6.1)
│   ├── has-a SyllablesAgent (L6.2)
│   ├── has-a PositionsAgent (L6.3)
│   ├── has-a PhonemeReferencesAgent (L6.4)
│   ├── has-a ContentTtsAgent (L6.5)
│   ├── has-a SuggestionsAgent (L6.6)
│   └── has-a VideoAgent (L6.7)
│
├── has-a ProjectAgent (L7)
│   ├── has-a ProjectCoreAgent (L7.1)
│   ├── has-a StorageTypeAgent (L7.2)
│   ├── has-a VariantsAgent (L7.3)
│   ├── has-a ContentAssociationAgent (L7.4)
│   ├── has-a DashboardAgent (L7.5)
│   └── has-a MenuAgent (L7.6)
│
└── has-a TeamAgent (L8)
    ├── has-a TeamModelAgent (L8.1)
    ├── has-a MembershipAgent (L8.2)
    ├── has-a InvitesAgent (L8.3)
    └── has-a ProjectSharingAgent (L8.4)
```

**Total class count:**
- 1 ManagerAgent
- 7 LayerAgents
- 38 SubLayerAgents
- 12 Interfaces
- 3 Abstract base classes
- **= 61 classes/interfaces total**

---

<!-- section_id: "f1825757-19f3-43ef-b775-b6f0dae5693d" -->
## Interface Dependency Graph (DIP Applied)

Every dependency points to an INTERFACE, never to a concrete class.

```
                    «interface»
                  IStorageProvider
                  IAuthProvider
                        ▲
                        │ provides
                 InfrastructureAgent (L2)
                        │
                        │ uses IStorageProvider, IAuthProvider
                        ▼
                    «interface»
                   IUserProvider
                        ▲
                        │ provides
                    UserAgent (L3)
                        │
                        │ uses IUserProvider
                        ▼
                    «interface»
              IPhonemeProvider
              IPhonemeAudio
              IFrequencyProvider
              IPhonemeAdmin
                        ▲
                        │ provides
                  PhonemeAgent (L4)
                        │
                        │ uses IPhonemeProvider
                        ▼
                    «interface»
                ITemplateProvider
                        ▲
                        │ provides
                  TemplateAgent (L5)
                        │
                        │ uses ITemplateProvider, IPhonemeAudio
                        ▼
                    «interface»
                IContentProvider
                IContentAudio
                        ▲
                        │ provides
                  ContentAgent (L6)
                        │
                        │ uses IContentProvider
                        ▼
                    «interface»
                IProjectProvider
                        ▲
                        │ provides
                  ProjectAgent (L7)
                        │
                        │ uses IProjectProvider, IUserProvider
                        ▼
                    «interface»
             ICollaborationProvider
                        ▲
                        │ provides
                   TeamAgent (L8)
```

Note: ContentAgent (L6) uses `IPhonemeAudio` from L4 — it SKIPS L5 for this specific interface. This is valid because DIP says "depend on abstractions" — L6 depends on the IPhonemeAudio interface, not on the PhonemeAgent class. The interface is available to any layer that needs it.

---

<!-- section_id: "2d8167f7-d2d3-4fc3-b87c-b7834ac0045c" -->
## How Delegation Flows Through the Class Hierarchy

<!-- section_id: "f5f13925-92c7-445d-81ff-9ad1d441774a" -->
### Example: Task T1 — Fix multisyllable word creation test failures

```
1. ManagerAgent.route_task("fix multisyllable word creation failures")
   → routing_table matches "word" → ContentAgent (L6)

2. ContentAgent.delegate_to_sublayer(task)
   → identifies: word creation → WordsAgent (L6.1)
   → identifies: syllable structure → SyllablesAgent (L6.2)
   → identifies: positions → PositionsAgent (L6.3)
   → dependency shape is SEQUENCE → runs L6.1 → L6.2 → L6.3 sequentially

3. SyllablesAgent.execute(task)
   → needs_sibling() → "I need phoneme data from L4"
   → SyllablesAgent.escalate(task) → ContentAgent (parent)

4. ContentAgent uses IPhonemeProvider (L4 interface)
   → PhonemeAgent.get_phoneme(id) → returns phoneme data
   → passes back to SyllablesAgent

5. SyllablesAgent completes fix
   → reports to ContentAgent
   → ContentAgent aggregates result
   → reports to ManagerAgent
```

<!-- section_id: "59ed0260-e753-4bfa-ab08-5fd485db44cd" -->
### Example: Task T5 — Team invitation flow (MULTI-LAYER)

```
1. ManagerAgent.route_task("implement team invitation flow")
   → routing_table matches "team" + "invitation" → TeamAgent (L8)

2. TeamAgent.delegate_to_sublayer(task)
   → MembershipAgent (L8.2) handles member management
   → InvitesAgent (L8.3) handles invite codes

3. InvitesAgent.execute(task)
   → needs_sibling() → "I need user lookup"
   → InvitesAgent cannot resolve internally → escalate to TeamAgent

4. TeamAgent uses IUserProvider (L3 interface)
   → UserAgent.get_user(id) → returns user data
   → passes to InvitesAgent

5. InvitesAgent.execute(task) continues
   → needs: "I need project access check"
   → escalate to TeamAgent

6. TeamAgent uses IProjectProvider (L7 interface)
   → ProjectAgent.get_project(id) → returns project data

7. TeamAgent uses IAuthProvider (L2 interface)
   → InfrastructureAgent.check_auth() → returns auth status

8. InvitesAgent completes
   → ProjectSharingAgent (L8.4) links team to project
   → TeamAgent aggregates
   → reports to ManagerAgent
```

**Key OOP principle in action**: TeamAgent depends on `IUserProvider`, `IProjectProvider`, and `IAuthProvider` — all INTERFACES. It doesn't know or care about the internal sub-layers of L3, L7, or L2. That's encapsulation + DIP working together.

---

<!-- section_id: "0a8b8397-f025-4acd-ab0e-f89986ae8d70" -->
## Context Model Per Class Level

| Class Level | STATIC Context (always loaded) | DYNAMIC Context (on-demand) |
|-------------|-------------------------------|----------------------------|
| **ManagerAgent** | 2-3 line summary of each layer + routing table (~50 tokens per layer = ~350 total) | Any layer's full details via delegation |
| **LayerAgent** | Own domain knowledge + sub-layer summaries + neighbor interfaces (~500-800 tokens) | Other layers' full details via interface calls |
| **SubLayerAgent** | Own specialized knowledge + parent layer context + internal dependency info (~300-500 tokens) | Sibling sub-layers' details via parent coordination |

**Total STATIC per agent**: ~300-800 tokens (well within efficient range)
**Inheritance adds**: BaseAgent contributes ~50 tokens (agent ID, scope, universal methods). LayerAgent adds ~100 tokens (layer number, shape, interface lists). So a SubLayerAgent inherits ~150 tokens and adds ~300 of its own = ~450 total.

---

<!-- section_id: "02b40b80-b335-4135-9edd-4104bc22fef8" -->
## When to Use Each Class

| Situation | Class That Handles It | Why |
|-----------|----------------------|-----|
| Task clearly about one domain | LayerAgent routes to SubLayerAgent | SRP — one sub-layer, one responsibility |
| Task spans sub-layers within one domain | LayerAgent coordinates its SubLayerAgents | Composition — layer agent orchestrates its children |
| Task spans multiple domains | ManagerAgent coordinates LayerAgents via interfaces | DIP — agents depend on interfaces, not implementations |
| New feature added to a domain | New SubLayerAgent class, existing LayerAgent unchanged | OCP — open for extension, closed for modification |
| Domain agent swapped (e.g., new storage backend) | New class implements same interface | LSP — substitutable without affecting consumers |
| Agent needs capability from non-neighbor | Uses interface directly (ISP allows skipping) | ISP — depend only on interfaces you need |

---

<!-- section_id: "fecb13dd-89fc-42a5-8ff2-e94f3e5ef677" -->
## Class Hierarchy Summary

```
                          BaseAgent (abstract)
                         /          \
              LayerAgent (abstract)  ManagerAgent
             /    |    |   |   \
           L2    L3   L4  L5   L6   L7   L8
           │     │    │   │    │    │    │
        [7 sub] [3] [7]  [4]  [7]  [6]  [4]  ← SubLayerAgent instances
        ────────────────────────────────────
        38 SubLayerAgents total (COMPOSITION, not inheritance)

Interfaces: 12 segregated interfaces connecting layers
Inheritance depth: 3 (BaseAgent → LayerAgent → ConcreteLayer)
                   3 (BaseAgent → SubLayerAgent → ConcreteSubLayer)
                   2 (BaseAgent → ManagerAgent)
```

---

<!-- section_id: "b3864040-a601-4830-a3c3-6fc6890d0b51" -->
## Decisions

| Decision | OOP Principle | Rationale |
|----------|--------------|-----------|
| Max inheritance depth = 3 | Anti-pattern avoidance | Deep inheritance creates fragile hierarchies |
| Sub-layers are COMPOSED, not inherited | Composition over inheritance | LayerAgent has-a list of SubLayerAgents |
| 12 segregated interfaces | ISP | Each interface covers ONE capability area |
| LayerAgents depend on interfaces | DIP | Never depend on concrete neighbor implementations |
| ManagerAgent is Factory + Mediator | Design patterns | Creates agents, mediates cross-layer communication |
| SubLayerAgents can escalate to parent | Template Method pattern | Parent handles cross-domain coordination |
| Each LayerAgent knows its dependency shape | Strategy pattern | Sequence/tree/DAG shapes determine delegation strategy |

---

*Design created: 2026-02-26*
*Next: Create the experiment directory structure with actual 0AGNOSTIC.md files for each agent class*
