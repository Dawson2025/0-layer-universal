# Dependency-Based Agent Architecture Diagrams

Visualizations of the dependency-based agent hierarchy design for LangTrak.

**Companion to**: `../dependency_based_agent_hierarchy_design.md`, `../oop_class_hierarchy.md`
**Date**: 2026-02-26

---

## 1. Inter-Layer Dependency Chain

The 7-layer linear dependency chain. Each layer depends on all layers below it.

```mermaid
flowchart TB
    L2["L2: Infrastructure<br/>App, DB, Firebase, Storage Mgr,<br/>Auth, DB Admin, Firebase Sync"]
    L3["L3: Users<br/>User Model, Profiles, Sessions"]
    L4["L4: Phoneme System<br/>Groups, Types, Phonemes, Frequency,<br/>Display, TTS, Admin"]
    L5["L5: Templates<br/>Core, Selection, Application, Admin"]
    L6["L6: Language Content<br/>Words, Syllables, Positions, Refs,<br/>TTS, Suggestions, Video"]
    L7["L7: Projects<br/>Core, Storage Type, Variants,<br/>Content Assoc, Dashboard, Menu"]
    L8["L8: Teams<br/>Model, Membership, Invites, Sharing"]

    L2 -->|"auth, storage, DB"| L3
    L3 -->|"user identity, session"| L4
    L4 -->|"phoneme inventory, audio"| L5
    L5 -->|"filtered phoneme subsets"| L6
    L6 -->|"words, syllables, content"| L7
    L7 -->|"project containers"| L8

    style L2 fill:#1a237e,color:#fff
    style L3 fill:#283593,color:#fff
    style L4 fill:#303f9f,color:#fff
    style L5 fill:#3949ab,color:#fff
    style L6 fill:#3f51b5,color:#fff
    style L7 fill:#5c6bc0,color:#fff
    style L8 fill:#7986cb,color:#fff
```

---

## 2. L2 Infrastructure Internal Dependencies (DAG)

The most complex layer — a directed acyclic graph with diamond convergence patterns.

```mermaid
flowchart TB
    L21["L2.1: App Factory<br/>Flask create_app"]
    L22["L2.2: Database<br/>SQLite, schema, models"]
    L23["L2.3: Firebase<br/>Firestore, Auth SDK"]
    L24["L2.4: Storage Manager<br/>Unified local/cloud"]
    L25["L2.5: Auth System<br/>Login, OAuth, permissions"]
    L26["L2.6: DB Admin Tools<br/>Inspection, reset, migration"]
    L27["L2.7: Firebase Sync<br/>Cloud sync orchestration"]

    L21 --> L22
    L21 --> L23
    L22 --> L24
    L23 --> L24
    L22 --> L25
    L24 --> L25
    L22 --> L26
    L23 --> L27
    L24 --> L27

    style L21 fill:#e65100,color:#fff
    style L22 fill:#bf360c,color:#fff
    style L23 fill:#bf360c,color:#fff
    style L24 fill:#d84315,color:#fff
    style L25 fill:#f4511e,color:#fff
    style L26 fill:#ff7043,color:#fff
    style L27 fill:#ff7043,color:#fff
```

---

## 3. L4 Phoneme System Internal Dependencies (Sequence + Branches)

A sequence core with independent feature branches trailing from the main chain.

```mermaid
flowchart TB
    L41["L4.1: Phoneme Groups<br/>Vowels, Consonants, etc."]
    L42["L4.2: Phoneme Types<br/>Stops, Fricatives, Nasals"]
    L43["L4.3: Individual Phonemes<br/>IPA symbols: /p/, /b/, /m/"]
    L44["L4.4: Frequency Tracking<br/>Usage statistics"]
    L45["L4.5: Phoneme Display<br/>Hierarchy views, browsing"]
    L46["L4.6: TTS for Phonemes<br/>Audio generation"]
    L47["L4.7: Phoneme Admin<br/>CRUD management"]

    L41 --> L42
    L42 --> L43
    L43 --> L44
    L43 --> L45
    L43 --> L46
    L41 --> L47
    L42 --> L47
    L43 --> L47

    style L41 fill:#1b5e20,color:#fff
    style L42 fill:#2e7d32,color:#fff
    style L43 fill:#388e3c,color:#fff
    style L44 fill:#43a047,color:#fff
    style L45 fill:#43a047,color:#fff
    style L46 fill:#66bb6a,color:#fff
    style L47 fill:#66bb6a,color:#fff
```

---

## 4. L6 Language Content Internal Dependencies (Containment Sequence + Branches)

A containment chain (words contain syllables contain positions) with enhancement branches.

```mermaid
flowchart TB
    L61["L6.1: Words<br/>Word CRUD, search"]
    L62["L6.2: Syllables<br/>Multi-syllable structure"]
    L63["L6.3: Positions<br/>Onset, Nucleus, Coda"]
    L64["L6.4: Phoneme References<br/>Phoneme assignments in positions"]
    L65["L6.5: TTS for Content<br/>Word and syllable audio"]
    L66["L6.6: Word Suggestions<br/>Phonotactic generation"]
    L67["L6.7: Video<br/>Pronunciation video"]

    L61 --> L62
    L62 --> L63
    L63 --> L64
    L64 --> L65
    L64 --> L66
    L61 --> L67

    style L61 fill:#4a148c,color:#fff
    style L62 fill:#6a1b9a,color:#fff
    style L63 fill:#7b1fa2,color:#fff
    style L64 fill:#8e24aa,color:#fff
    style L65 fill:#ab47bc,color:#fff
    style L66 fill:#ab47bc,color:#fff
    style L67 fill:#ab47bc,color:#fff
```

---

## 5. L7 Projects Internal Dependencies (Star/Hub)

A hub pattern — everything depends on the core, nothing depends on each other.

```mermaid
flowchart TB
    L71["L7.1: Project Core<br/>CRUD, metadata"]
    L72["L7.2: Storage Type<br/>SQLite vs Firestore"]
    L73["L7.3: Variants<br/>Duplication, forking"]
    L74["L7.4: Content Association<br/>Template + word linkage"]
    L75["L7.5: Dashboard<br/>Overview, stats"]
    L76["L7.6: Menu/Navigation<br/>Project switching"]

    L71 --> L72
    L71 --> L73
    L71 --> L74
    L71 --> L75
    L71 --> L76

    style L71 fill:#880e4f,color:#fff
    style L72 fill:#ad1457,color:#fff
    style L73 fill:#ad1457,color:#fff
    style L74 fill:#ad1457,color:#fff
    style L75 fill:#c2185b,color:#fff
    style L76 fill:#c2185b,color:#fff
```

---

## 6. OOP Inheritance Hierarchy

The three-level class hierarchy with abstract bases and concrete implementations.

```mermaid
classDiagram
    class BaseAgent {
        <<abstract>>
        +agent_id: str
        +agent_name: str
        +scope_description: str
        +static_context: Context
        +neighbor_interfaces: Dict
        +load_context() void
        +delegate(task, target) Result
        +report(result) void
        +is_in_scope(task) bool
        +escalate(task) void
    }

    class ManagerAgent {
        +layer_agents: List~LayerAgent~
        +routing_table: Dict
        +layer_overview: Dict
        +route_task(task) LayerAgent
        +coordinate(tasks) List~Result~
        +get_status() SystemStatus
    }

    class LayerAgent {
        <<abstract>>
        +layer_number: int
        +sub_layers: List~SubLayerAgent~
        +provided_interfaces: List
        +consumed_interfaces: List
        +public_interface: Interface
        +delegate_to_sublayer(task) Result
        +aggregate_interface() Interface
        +get_dependency_shape() Shape
        +can_parallelize(tasks) List
    }

    class SubLayerAgent {
        <<abstract>>
        +sublayer_id: str
        +parent_layer: LayerAgent
        +internal_dependencies: List
        +domain_context: Context
        +execute(task) Result
        +needs_sibling(task) str
        +get_capability() Interface
    }

    BaseAgent <|-- ManagerAgent
    BaseAgent <|-- LayerAgent
    BaseAgent <|-- SubLayerAgent
    LayerAgent o-- SubLayerAgent : composes
    ManagerAgent o-- LayerAgent : composes
```

---

## 7. Concrete Layer Agents

The 7 concrete LayerAgent implementations with their interface relationships.

```mermaid
classDiagram
    class LayerAgent {
        <<abstract>>
    }

    class InfrastructureAgent {
        +layer_number = 2
        +sub_layers: 7
        +shape: DAG
    }

    class UserAgent {
        +layer_number = 3
        +sub_layers: 3
        +shape: Sequence
    }

    class PhonemeAgent {
        +layer_number = 4
        +sub_layers: 7
        +shape: Sequence+Branch
    }

    class TemplateAgent {
        +layer_number = 5
        +sub_layers: 4
        +shape: ShallowTree
    }

    class ContentAgent {
        +layer_number = 6
        +sub_layers: 7
        +shape: Sequence+Branch
    }

    class ProjectAgent {
        +layer_number = 7
        +sub_layers: 6
        +shape: Star
    }

    class TeamAgent {
        +layer_number = 8
        +sub_layers: 4
        +shape: Sequence
    }

    LayerAgent <|-- InfrastructureAgent
    LayerAgent <|-- UserAgent
    LayerAgent <|-- PhonemeAgent
    LayerAgent <|-- TemplateAgent
    LayerAgent <|-- ContentAgent
    LayerAgent <|-- ProjectAgent
    LayerAgent <|-- TeamAgent

    InfrastructureAgent ..> UserAgent : IStorageProvider, IAuthProvider
    UserAgent ..> PhonemeAgent : IUserProvider
    PhonemeAgent ..> TemplateAgent : IPhonemeProvider
    TemplateAgent ..> ContentAgent : ITemplateProvider
    ContentAgent ..> ProjectAgent : IContentProvider
    ProjectAgent ..> TeamAgent : IProjectProvider
```

---

## 8. Interface Segregation Map

Which interfaces each layer provides and which it consumes.

```mermaid
flowchart LR
    subgraph PROVIDES["Interfaces Provided"]
        IP_STOR["IStorageProvider"]
        IP_AUTH["IAuthProvider"]
        IP_USER["IUserProvider"]
        IP_PHON["IPhonemeProvider"]
        IP_PAUD["IPhonemeAudio"]
        IP_FREQ["IFrequencyProvider"]
        IP_PADM["IPhonemeAdmin"]
        IP_TMPL["ITemplateProvider"]
        IP_CONT["IContentProvider"]
        IP_CAUD["IContentAudio"]
        IP_PROJ["IProjectProvider"]
        IP_COLB["ICollaborationProvider"]
    end

    subgraph AGENTS["Layer Agents"]
        A2["L2 Infrastructure"]
        A3["L3 Users"]
        A4["L4 Phonemes"]
        A5["L5 Templates"]
        A6["L6 Content"]
        A7["L7 Projects"]
        A8["L8 Teams"]
    end

    A2 --> IP_STOR
    A2 --> IP_AUTH
    A3 --> IP_USER
    A4 --> IP_PHON
    A4 --> IP_PAUD
    A4 --> IP_FREQ
    A4 --> IP_PADM
    A5 --> IP_TMPL
    A6 --> IP_CONT
    A6 --> IP_CAUD
    A7 --> IP_PROJ
    A8 --> IP_COLB

    IP_STOR -.->|used by| A3
    IP_AUTH -.->|used by| A3
    IP_USER -.->|used by| A4
    IP_USER -.->|used by| A8
    IP_PHON -.->|used by| A5
    IP_PAUD -.->|used by| A6
    IP_TMPL -.->|used by| A6
    IP_CONT -.->|used by| A7
    IP_PROJ -.->|used by| A8

    style A2 fill:#1a237e,color:#fff
    style A3 fill:#283593,color:#fff
    style A4 fill:#1b5e20,color:#fff
    style A5 fill:#33691e,color:#fff
    style A6 fill:#4a148c,color:#fff
    style A7 fill:#880e4f,color:#fff
    style A8 fill:#b71c1c,color:#fff
```

---

## 9. Delegation Flow — Task T5: Team Invitation

Sequence diagram showing how a multi-layer task flows through the class hierarchy.

```mermaid
sequenceDiagram
    participant M as ManagerAgent
    participant T8 as TeamAgent L8
    participant T82 as MembershipSub L8.2
    participant T83 as InvitesSub L8.3
    participant T84 as SharingSub L8.4
    participant U3 as UserAgent L3
    participant P7 as ProjectAgent L7
    participant I2 as InfrastructureAgent L2

    M->>T8: route_task "team invitation flow"
    T8->>T82: delegate membership setup
    T82-->>T8: membership ready

    T8->>T83: delegate invite creation
    T83->>T8: needs_sibling "user lookup"
    T8->>U3: IUserProvider.get_user(id)
    U3-->>T8: User data
    T8->>T83: pass user data
    T83->>T8: needs "project access check"
    T8->>P7: IProjectProvider.get_project(id)
    P7-->>T8: Project data
    T8->>I2: IAuthProvider.check_auth()
    I2-->>T8: auth confirmed
    T8->>T83: pass project + auth
    T83-->>T8: invite created

    T8->>T84: delegate project sharing
    T84-->>T8: sharing linked

    T8-->>M: task complete
```

---

## 10. Cross-Cutting Feature Absorption

Shows where L9, L10, L11 features were absorbed into domain layers.

```mermaid
flowchart TB
    subgraph OLD["Original Structure — 10 Layers"]
        OL9["L9: Enhancements<br/>TTS, Video, Suggestions"]
        OL10["L10: Admin<br/>Phoneme Mgmt, DB Tools, Dashboard"]
        OL11["L11: Orchestration<br/>Firebase Sync, Universal, AI"]
    end

    subgraph NEW["New Structure — Absorbed Into Domains"]
        subgraph NL2["L2 Infrastructure"]
            NL26["L2.6: DB Admin"]
            NL27["L2.7: Firebase Sync"]
        end
        subgraph NL4["L4 Phoneme System"]
            NL46["L4.6: Phoneme TTS"]
            NL47["L4.7: Phoneme Admin"]
        end
        subgraph NL5["L5 Templates"]
            NL54["L5.4: Template Admin"]
        end
        subgraph NL6["L6 Content"]
            NL65["L6.5: Content TTS"]
            NL66["L6.6: Suggestions"]
            NL67["L6.7: Video"]
        end
        subgraph NL7["L7 Projects"]
            NL75["L7.5: Dashboard"]
            NL76["L7.6: Menu"]
        end
    end

    OL9 -.->|"TTS phonemes"| NL46
    OL9 -.->|"TTS words"| NL65
    OL9 -.->|"Suggestions"| NL66
    OL9 -.->|"Video"| NL67
    OL10 -.->|"DB tools"| NL26
    OL10 -.->|"Phoneme mgmt"| NL47
    OL10 -.->|"Template mgmt"| NL54
    OL10 -.->|"Dashboard"| NL75
    OL10 -.->|"Menu"| NL76
    OL11 -.->|"Firebase sync"| NL27

    style OLD fill:#ffcdd2,color:#000
    style NL2 fill:#1a237e,color:#fff
    style NL4 fill:#1b5e20,color:#fff
    style NL5 fill:#33691e,color:#fff
    style NL6 fill:#4a148c,color:#fff
    style NL7 fill:#880e4f,color:#fff
```

---

## 11. Full Composition Tree

The complete has-a object graph at runtime — Manager contains Layers, Layers contain Sub-layers.

```mermaid
flowchart TB
    MGR["ManagerAgent<br/>Factory + Mediator"]

    subgraph L2["L2: InfrastructureAgent — 7 sub-layers"]
        L21["L2.1 AppFactory"]
        L22["L2.2 Database"]
        L23["L2.3 Firebase"]
        L24["L2.4 StorageMgr"]
        L25["L2.5 Auth"]
        L26["L2.6 DbAdmin"]
        L27["L2.7 FbSync"]
    end

    subgraph L3["L3: UserAgent — 3 sub-layers"]
        L31["L3.1 UserModel"]
        L32["L3.2 Profiles"]
        L33["L3.3 Sessions"]
    end

    subgraph L4["L4: PhonemeAgent — 7 sub-layers"]
        L41["L4.1 Groups"]
        L42["L4.2 Types"]
        L43["L4.3 Phonemes"]
        L44["L4.4 Frequency"]
        L45["L4.5 Display"]
        L46["L4.6 TTS"]
        L47["L4.7 Admin"]
    end

    subgraph L5["L5: TemplateAgent — 4 sub-layers"]
        L51["L5.1 Core"]
        L52["L5.2 Selection"]
        L53["L5.3 Application"]
        L54["L5.4 Admin"]
    end

    subgraph L6["L6: ContentAgent — 7 sub-layers"]
        L61["L6.1 Words"]
        L62["L6.2 Syllables"]
        L63["L6.3 Positions"]
        L64["L6.4 PhonemeRefs"]
        L65["L6.5 TTS"]
        L66["L6.6 Suggestions"]
        L67["L6.7 Video"]
    end

    subgraph L7["L7: ProjectAgent — 6 sub-layers"]
        L71["L7.1 Core"]
        L72["L7.2 StorageType"]
        L73["L7.3 Variants"]
        L74["L7.4 ContentAssoc"]
        L75["L7.5 Dashboard"]
        L76["L7.6 Menu"]
    end

    subgraph L8["L8: TeamAgent — 4 sub-layers"]
        L81["L8.1 TeamModel"]
        L82["L8.2 Membership"]
        L83["L8.3 Invites"]
        L84["L8.4 Sharing"]
    end

    MGR --> L2
    MGR --> L3
    MGR --> L4
    MGR --> L5
    MGR --> L6
    MGR --> L7
    MGR --> L8

    style MGR fill:#f57f17,color:#000
    style L2 fill:#1a237e,color:#fff
    style L3 fill:#283593,color:#fff
    style L4 fill:#1b5e20,color:#fff
    style L5 fill:#33691e,color:#fff
    style L6 fill:#4a148c,color:#fff
    style L7 fill:#880e4f,color:#fff
    style L8 fill:#b71c1c,color:#fff
```

---

## Diagram Index

| # | Diagram | Shows |
|---|---------|-------|
| 1 | Inter-Layer Dependency Chain | 7-layer linear chain L2→L8 with interface labels |
| 2 | L2 Infrastructure Internal | DAG with diamond convergence at Storage Manager and Auth |
| 3 | L4 Phoneme System Internal | Sequence core with TTS, Display, Frequency branches |
| 4 | L6 Language Content Internal | Containment chain with TTS, Suggestions, Video branches |
| 5 | L7 Projects Internal | Star/hub pattern — everything depends on Core |
| 6 | OOP Inheritance Hierarchy | BaseAgent → LayerAgent/ManagerAgent/SubLayerAgent class diagram |
| 7 | Concrete Layer Agents | 7 LayerAgent subclasses with interface dependencies |
| 8 | Interface Segregation Map | 12 interfaces: who provides, who consumes |
| 9 | Delegation Flow T5 | Sequence diagram of multi-layer team invitation task |
| 10 | Cross-Cutting Absorption | Where L9/L10/L11 features moved into domain layers |
| 11 | Full Composition Tree | Complete has-a graph: Manager → Layers → 38 Sub-layers |
