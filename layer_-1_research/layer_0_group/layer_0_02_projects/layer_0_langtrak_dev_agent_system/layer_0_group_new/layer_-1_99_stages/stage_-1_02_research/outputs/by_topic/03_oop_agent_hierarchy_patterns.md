---
resource_id: "85f8d0b3-eed9-4e13-8a94-b7eddf01f9f1"
resource_type: "output"
resource_name: "03_oop_agent_hierarchy_patterns"
---
# OOP Agent Hierarchy Patterns

**Status**: RESEARCH — Mapping object-oriented programming patterns to agent team structures
**Date**: 2026-02-26
**Companion to**: `01_hierarchy_structural_ideas.md`, `02_sublayer_dependency_structures.md`
**Core question**: Would agent teams perform better if structured like OOP class hierarchies — with inheritance, polymorphism, encapsulation, and composition?

---

<!-- section_id: "118eaedf-a46c-4a54-bf83-2d64d0f6b498" -->
## The Analogy

In OOP, we organize code using:
- **Classes** (blueprints for objects)
- **Inheritance** (child classes extend parent classes)
- **Interfaces** (contracts that define what an object can do)
- **Encapsulation** (hide internals, expose only the public API)
- **Composition** (objects contain other objects)
- **Polymorphism** (different implementations of the same interface)
- **Abstract classes** (partial implementations that must be extended)
- **SOLID principles** (design rules for maintainable hierarchies)

If we map these to agent teams:

| OOP Concept | Agent Equivalent |
|-------------|-----------------|
| Class | Agent definition (0AGNOSTIC.md — identity, behaviors, interfaces) |
| Instance | A running agent (a specific instance executing tasks) |
| Inheritance | Agent inherits context from parent agent |
| Interface | Agent's public contract (what it provides, what it accepts) |
| Encapsulation | Agent hides internal sublayer details, exposes aggregated interface |
| Composition | Agent contains sub-agents (has-a relationship) |
| Polymorphism | Multiple agent implementations for the same role |
| Abstract class | Agent template with some behaviors defined, others left to specialization |
| Method | A specific capability the agent can perform |
| Constructor | Agent initialization (loading context, connecting to tools) |

---

<!-- section_id: "025cc788-0723-415f-ad78-a5934ee28023" -->
## OOP Principle 1: Inheritance → Context Inheritance

<!-- section_id: "7efa83fe-9939-4d32-957a-9f24ea9dab8a" -->
### In OOP

```python
class BaseAgent:
    storage_api = "..."      # All agents can use storage
    auth_check = "..."       # All agents can check auth

class DomainAgent(BaseAgent):
    domain_knowledge = "..."  # Inherits storage + auth, adds domain

class PhonemeAgent(DomainAgent):
    phoneme_knowledge = "..." # Inherits storage + auth + domain, adds phoneme specifics
```

<!-- section_id: "0e1c4e60-2eb0-4003-92cc-da249c43a08a" -->
### In Agent Teams

```
BaseAgent (0AGNOSTIC.md — universal context)
├── STATIC: storage API interface, auth check API, app context
├── Methods: query_storage(), check_auth(), get_config()

    DomainAgent extends BaseAgent
    ├── INHERITS: storage API, auth check, app context
    ├── ADDS: domain model (what entities exist, how they relate)
    ├── Methods: query_domain(), validate_entity()

        PhonemeAgent extends DomainAgent
        ├── INHERITS: storage API, auth check, domain model
        ├── ADDS: phoneme system knowledge (groups, types, IPA)
        ├── Methods: lookup_phoneme(), validate_phoneme_assignment()
```

<!-- section_id: "260179e4-a6f6-4b62-802e-c58d7e8f0917" -->
### What This Gives Us

**Context cascading is INHERITANCE.** When we say "L2 Infrastructure context cascades to all higher layers," that IS inheritance — child agents automatically get parent context.

But in OOP, inheritance has rules:
1. **Single inheritance** (most languages): A class has ONE parent. This maps to a LINEAR hierarchy (L2 → L3 → L4 → ...).
2. **Multiple inheritance** (Python, C++): A class can have MULTIPLE parents. This maps to CROSS-CUTTING layers (L9 Enhancements inherits from BOTH L4 Phonemes and L6 Content).
3. **Interface implementation** (Java, Go): A class implements multiple interfaces without inheriting implementation. This maps to agents having contracts with multiple layers without inheriting their context.

<!-- section_id: "29f20440-1daf-4314-8089-c2cfcde9aac4" -->
### Problem: The Diamond Problem

In OOP, if `class D extends B, C` and both B and C extend A, which version of A does D get?

In agents: If the Enhancement Agent (L9) inherits from both Phoneme Agent (L4) and Content Agent (L6), and both inherit from Users Agent (L3), does L9 get TWO copies of user context? One copy? Which one?

**Solution (same as OOP)**: Use **interface inheritance** for cross-cutting, not **implementation inheritance**. The Enhancement Agent doesn't EXTEND Phoneme and Content agents — it IMPLEMENTS their interfaces (knows how to talk to them) without inheriting their full context.

```
BaseAgent
├── InfrastructureAgent extends BaseAgent
├── UsersAgent extends InfrastructureAgent
├── PhonemeAgent extends UsersAgent
├── TemplateAgent extends PhonemeAgent
├── ContentAgent extends TemplateAgent
├── ProjectAgent extends ContentAgent
├── TeamAgent extends ProjectAgent
│
├── EnhancementAgent extends BaseAgent
│   implements PhonemeInterface, ContentInterface
│   (NOT extends PhonemeAgent — avoids diamond problem)
```

---

<!-- section_id: "204913d7-c296-4e2a-918a-336514280bb1" -->
## OOP Principle 2: Encapsulation → Agent Boundaries

<!-- section_id: "fe1b9b48-041b-4b0d-851a-35666e96c6ea" -->
### In OOP

```python
class PhonemeSystem:
    # PRIVATE (internal implementation)
    _groups = [...]
    _types = [...]
    _phonemes = [...]
    _frequency_data = [...]

    def _resolve_type(self, phoneme_id): ...
    def _calculate_frequency(self, phoneme_id): ...

    # PUBLIC (external interface)
    def get_phoneme(self, id) -> Phoneme: ...
    def list_by_group(self, group_name) -> List[Phoneme]: ...
    def get_frequency(self, phoneme_id) -> float: ...
```

<!-- section_id: "c327dc7b-0373-41a6-a4e2-ffa3f5f97773" -->
### In Agent Teams

The Phoneme System Agent has:
- **Private** (internal context, not shared): How groups are structured, how types relate to groups, how frequency is calculated, the display rendering logic
- **Public** (interface, shared with neighbors): "I can look up phonemes by ID, list phonemes by group, report frequency. Call me with a phoneme ID or group name."

This IS what document 02 calls "interface aggregation" — sublayer complexity is encapsulated, only the aggregated interface is public.

<!-- section_id: "91166bfc-689c-4340-b455-86e299e64cb0" -->
### What This Gives Us

**Strong encapsulation means agents need LESS context.** If the Template Agent doesn't know HOW the Phoneme System tracks frequency internally, it doesn't need to load that context. It just calls `get_phoneme()` and gets a result.

This directly reduces token usage and context window consumption. An agent's STATIC context only needs:
1. Its OWN private implementation (full details)
2. Its neighbors' PUBLIC interfaces (compact summaries)

<!-- section_id: "5b0cf465-d205-43aa-88fc-3b7a90514cb4" -->
### The Encapsulation Spectrum

```
MAXIMUM ENCAPSULATION                            MINIMUM ENCAPSULATION
(OOP ideal)                                      (all context shared)

Agent knows ONLY:          Agent knows:           Agent knows EVERYTHING:
- Own internals            - Own internals         - Own internals
- Neighbor interfaces      - Neighbor internals    - All agents' internals
  (3-5 lines each)          + their interfaces      (full context dump)
                             (100s of lines)

Pros: Minimal context,     Pros: Moderate context,  Pros: Agent can handle
  lean agents               can debug neighbors       any task without delegation
Cons: Can't debug           Cons: More to load       Cons: Massive context,
  cross-layer issues                                    slow, unfocused
  without delegation
```

For LangTrak, the sweet spot is maximum encapsulation with ON-DEMAND access:
- Agents start with only their internals + neighbor interfaces
- When they need to debug a cross-layer issue, they REQUEST the neighbor's internals
- This is like Python's `__dict__` or Java's reflection — breaking encapsulation deliberately when needed

---

<!-- section_id: "beee9024-4724-40ca-9a89-35f38d5e7028" -->
## OOP Principle 3: Composition → Agent Composition (Has-A)

<!-- section_id: "6a5de19e-6956-44e6-86cf-7702a8178dab" -->
### In OOP

```python
class Project:
    storage: StorageType           # has-a storage type
    variants: List[Variant]        # has-a list of variants
    content: ContentAssociation    # has-a content association
    settings: ProjectSettings      # has-a settings object
```

<!-- section_id: "d0133dbd-ec08-488d-a01a-0c4a1380d4d1" -->
### In Agent Teams

Composition means an agent CONTAINS sub-agents (has-a relationship), as opposed to inheritance (is-a relationship).

```
Project Agent (CONTAINS)
├── has-a Storage Type Sub-Agent
├── has-a Variants Sub-Agent
├── has-a Content Association Sub-Agent
└── has-a Settings Sub-Agent
```

**Key distinction from inheritance:**
- Inheritance: "A PhonemeAgent IS-A DomainAgent" → inherits context
- Composition: "A ProjectAgent HAS-A StorageType sub-agent" → delegates to contained agents

<!-- section_id: "deb45702-2249-436e-83d8-3d6f1bceee91" -->
### When to Use Composition vs. Inheritance

**Use inheritance (is-a)** for the VERTICAL hierarchy between layers:
```
PhonemeAgent IS-A DomainAgent IS-A BaseAgent
(context cascades downward through the inheritance chain)
```

**Use composition (has-a)** for the HORIZONTAL structure within layers:
```
ProjectAgent HAS-A StorageType, HAS-A Variants, HAS-A ContentAssoc
(sub-agents are contained, not inherited from)
```

This is the classic OOP principle: **"Favor composition over inheritance."** In agent terms: use inheritance for the layer dependency chain (vertical context cascade), use composition for sublayer structure (horizontal internal organization).

---

<!-- section_id: "03a8b18b-018b-47e6-8f72-6da5bb05b462" -->
## OOP Principle 4: Polymorphism → Agent Polymorphism

<!-- section_id: "8a35e92f-08bf-48d3-a4e0-b1b9c8014fab" -->
### In OOP

```python
class StorageBackend(ABC):
    @abstractmethod
    def save(self, data): ...

    @abstractmethod
    def load(self, id): ...

class SQLiteBackend(StorageBackend):
    def save(self, data):
        # SQLite-specific implementation

class FirestoreBackend(StorageBackend):
    def save(self, data):
        # Firestore-specific implementation
```

<!-- section_id: "b5b20474-acdc-4557-b00f-a2e70b3aeead" -->
### In Agent Teams

Different agent implementations can fulfill the same role. The caller doesn't need to know which implementation is active.

```
Storage Interface:
  "I can save() and load() data"

SQLite Storage Agent (implements Storage Interface):
  - Uses SQLite queries
  - Knows about local file paths

Firestore Storage Agent (implements Storage Interface):
  - Uses Firestore client
  - Knows about cloud collections

Storage Manager Agent (polymorphic dispatcher):
  - Routes save/load calls to the right implementation based on project's storage type
```

<!-- section_id: "d8220c8c-93c2-4954-b7e5-213728996b60" -->
### What This Gives Us

**Polymorphism allows SWAPPING agent implementations without changing the hierarchy.** If we add a new storage backend (PostgreSQL), we create a new agent that implements the Storage Interface. No other agent needs to change.

For LangTrak, this applies to:
- **Storage** (SQLite vs. Firestore — already dual-path)
- **Auth** (email/password vs. Google OAuth vs. Firebase Auth — multiple auth methods)
- **TTS** (Azure Cognitive Services today, could swap to another TTS provider)
- **Development approaches** (different trial structures in the experiment are literally polymorphic agent hierarchies — same interface, different implementations)

<!-- section_id: "eebf8918-2986-4974-ade4-2010af17ab15" -->
### Polymorphism in the Experiment

The experiment itself is testing POLYMORPHISM — all trials implement the same interface ("develop LangTrak features") with different internal structures. The best-performing implementation wins, just like choosing the best algorithm implementation in OOP.

---

<!-- section_id: "0118176b-5072-4312-ad7c-4256b1946dd0" -->
## OOP Principle 5: SOLID Principles → Agent Design Principles

<!-- section_id: "30b25300-113a-48a0-bfbf-54b355a8b3ac" -->
### S — Single Responsibility Principle

**OOP**: Each class should have one reason to change.
**Agents**: Each agent should have ONE domain. If a change to phonemes AND a change to projects both require updating the same agent, that agent has too many responsibilities.

**Application**: This is why single-layer agents (Trial A in the experiment) can be good — each agent has exactly one responsibility. But it can be too granular (does "Frequency Tracking" need its own agent?).

**Sweet spot**: One agent per DOMAIN CLUSTER (Trial B/G), not per individual component.

<!-- section_id: "437ec30d-02bf-4d32-8778-622dbf4f9cba" -->
### O — Open/Closed Principle

**OOP**: Open for extension, closed for modification.
**Agents**: Adding a new feature should require ADDING a new agent, not MODIFYING existing agents.

**Application**: If we add "Audio Recording" to LangTrak, we should create a new Enhancement Agent, not modify the TTS Agent. The agent hierarchy should be extensible without touching existing agents.

**How**: Use interfaces. The Enhancement layer defines an interface. New enhancements implement it. Existing agents don't change.

<!-- section_id: "9051f161-6115-4d26-ab7e-2a89c1b65574" -->
### L — Liskov Substitution Principle

**OOP**: Subtypes must be substitutable for their base types.
**Agents**: If a specialized agent replaces a general agent, everything should still work.

**Application**: If we replace the generic "Content Agent" with a specialized "Multi-Syllable Content Agent," every agent that talks to the Content interface should still work. The specialized agent must honor the same interface contract.

<!-- section_id: "8a483104-51de-48f1-a009-6b3ecd209e4c" -->
### I — Interface Segregation Principle

**OOP**: Clients shouldn't depend on interfaces they don't use.
**Agents**: The Template Agent shouldn't need to know about the Phoneme System's frequency tracking capability if it never uses it.

**Application**: Instead of one big "Phoneme System Interface" that includes groups, types, phonemes, frequency, AND display, have:
- PhonemeQueryInterface (for agents that look up phonemes)
- FrequencyInterface (for agents that need usage stats)
- DisplayInterface (for agents that render phoneme views)

The Template Agent only implements PhonemeQueryInterface. The Dashboard Agent implements DisplayInterface. Neither loads the other's interface.

<!-- section_id: "62d6d28c-3c7f-4ccf-8993-3b31b27ad7ad" -->
### D — Dependency Inversion Principle

**OOP**: High-level modules shouldn't depend on low-level modules. Both should depend on abstractions.
**Agents**: The Project Agent shouldn't depend on the SPECIFIC implementation of the Storage Manager. It should depend on the Storage INTERFACE.

**Application**: This is why agents communicate via interface summaries, not full implementation details. The inter-agent communication is:
```
Project Agent → calls "Storage Interface: save(project_data)"
                NOT "SQLite: INSERT INTO projects ..."
```

If we change the storage implementation, the Project Agent doesn't notice.

---

<!-- section_id: "ba82e605-0331-406c-abb0-71c08c13b671" -->
## The OOP Agent Hierarchy: Full Structure

Combining all OOP principles into one coherent agent hierarchy for LangTrak:

```
                    ┌────────────────────────┐
                    │  «abstract»            │
                    │  BaseAgent             │
                    │  ──────────────────    │
                    │  + storage_interface   │
                    │  + auth_interface      │
                    │  + app_context         │
                    │  ──────────────────    │
                    │  + query_storage()     │
                    │  + check_auth()        │
                    └───────────┬────────────┘
                                │ inherits
                    ┌───────────┴────────────┐
                    │  «abstract»            │
                    │  DomainAgent           │
                    │  ──────────────────    │
                    │  + domain_model        │
                    │  + entity_interfaces   │
                    │  ──────────────────    │
                    │  + validate_entity()   │
                    │  + route_to_domain()   │
                    └───────────┬────────────┘
                                │ inherits
              ┌─────────────────┼─────────────────┐
              │                 │                  │
   ┌──────────┴─────┐ ┌────────┴──────┐ ┌────────┴────────┐
   │ PhonemeAgent   │ │ ContentAgent  │ │ ProjectAgent    │
   │ ─────────────  │ │ ─────────────│ │ ────────────── │
   │ groups, types, │ │ words, sylls,│ │ projects,      │
   │ inventory,     │ │ positions,   │ │ variants,      │
   │ frequency      │ │ phoneme refs │ │ storage type   │
   │ ─────────────  │ │ ─────────────│ │ ────────────── │
   │ «has-a»        │ │ «has-a»      │ │ «has-a»        │
   │ GroupsSub      │ │ WordsSub     │ │ StorageSub     │
   │ TypesSub       │ │ SyllablesSub │ │ VariantsSub    │
   │ FrequencySub   │ │ PositionsSub │ │ ContentAssocSub│
   └────────────────┘ └──────────────┘ └────────────────┘
              │                │                │
              │    «implements»│                │
              ├──── PhonemeQueryInterface       │
              ├──── FrequencyInterface          │
              │                ├──── ContentInterface
              │                │                ├──── ProjectInterface
              │                │                │
   ┌──────────┴─────────────────────────────────┤
   │  «implements multiple interfaces»           │
   │  EnhancementAgent (cross-cutting)          │
   │  implements PhonemeQueryInterface          │
   │  implements ContentInterface               │
   │  ────────────────────                      │
   │  «has-a» TTS, Video, Suggestions sub-agents│
   └────────────────────────────────────────────┘
```

<!-- section_id: "ba5da597-b73b-472c-bc57-b38d8e5330b6" -->
### How Delegation Works in This Structure

1. **Task arrives**: "Add a new phoneme type for fricatives"
2. **Manager routes to PhonemeAgent** (inherits from DomainAgent inherits from BaseAgent)
3. **PhonemeAgent has context from inheritance**: storage API (from BaseAgent), domain model (from DomainAgent), phoneme specifics (own)
4. **PhonemeAgent delegates internally via composition**: GroupsSub-agent checks group exists → TypesSub-agent adds the new type
5. **Public interface updated**: PhonemeQueryInterface now returns the new type
6. **No other agents modified**: Template Agent queries PhonemeQueryInterface — it sees the new type automatically (polymorphism)

<!-- section_id: "826364d2-2e2c-46ef-8a32-c8d15f88f7fd" -->
### How Cross-Cutting Works

1. **Task arrives**: "Add TTS preview for syllables"
2. **Manager routes to EnhancementAgent** (implements PhonemeQueryInterface + ContentInterface)
3. **EnhancementAgent queries PhonemeAgent** via PhonemeQueryInterface: "What phonemes are in this syllable?"
4. **EnhancementAgent queries ContentAgent** via ContentInterface: "Give me the syllable structure"
5. **EnhancementAgent delegates to TTS sub-agent**: "Generate audio for these phonemes in this order"
6. **No inheritance from PhonemeAgent or ContentAgent** — only interface calls (avoids diamond problem)

---

<!-- section_id: "760fbc80-a823-43fe-850a-a90b258958c4" -->
## OOP Patterns That Map to Agent Patterns

<!-- section_id: "82d6a043-699e-4c55-9650-3f64b9d6bde7" -->
### Factory Pattern → Agent Spawning

```python
class AgentFactory:
    def create_agent(self, layer_type, task):
        if layer_type == "phoneme":
            return PhonemeAgent(context=self.build_phoneme_context())
        elif layer_type == "content":
            return ContentAgent(context=self.build_content_context())
```

The Manager Agent IS a factory — it creates specialized agents based on the task type.

<!-- section_id: "5ee50347-c391-446e-ba3f-ed320a1c977b" -->
### Observer Pattern → Agent Event System

```python
class PhonemeSystem:
    observers = []

    def add_phoneme(self, phoneme):
        self._phonemes.append(phoneme)
        for observer in self.observers:
            observer.on_phoneme_added(phoneme)  # Notify Template, TTS, Frequency agents
```

When the Phoneme Agent adds a new phoneme, it should NOTIFY agents that care (Template Agent, TTS Agent, Frequency Agent). This is event-driven coordination rather than polling.

<!-- section_id: "80f4b58f-66ff-4a3c-9a97-a12d2e263e38" -->
### Strategy Pattern → Polymorphic Agent Implementations

The experiment trials ARE the Strategy Pattern — different algorithms (agent structures) for the same problem (developing LangTrak). The Manager picks a strategy at runtime.

<!-- section_id: "66ea5c3e-916e-446a-8744-2dff9fcd42f1" -->
### Decorator Pattern → Agent Capability Enhancement

```python
class LoggingAgent(AgentDecorator):
    def execute(self, task):
        log(f"Starting: {task}")
        result = self.wrapped_agent.execute(task)
        log(f"Completed: {task}")
        return result
```

Wrap any agent with logging, monitoring, or validation capabilities without modifying the agent itself. The "Stage Coordinator" in Trial D is essentially a decorator that adds workflow tracking to domain agents.

<!-- section_id: "160653be-9024-4b77-ad65-6dc75ac8689f" -->
### Mediator Pattern → Hub Coordination

Instead of agents communicating directly (peer-to-peer), a mediator coordinates:

```
Without mediator: Phoneme ↔ Template ↔ Content ↔ Project ↔ Teams
                  (N*(N-1)/2 communication channels)

With mediator:    Phoneme ↔ HUB ↔ Template
                  Content ↔ HUB ↔ Project
                  Teams   ↔ HUB
                  (N communication channels — much simpler)
```

The Manager Agent IS a mediator. Cross-layer communication goes through it rather than agents talking directly.

---

<!-- section_id: "158fc694-b6c1-46ca-9e4c-411a53384b2a" -->
## Would OOP-Structured Agents Perform Better?

<!-- section_id: "f3b9ff3f-c283-451d-be53-b84860003c2f" -->
### Arguments FOR (Yes)

1. **Encapsulation reduces context load**: Each agent only needs its own internals + neighbor interfaces. This is PROVEN to work well in OOP for reducing complexity.

2. **Inheritance gives clean context cascading**: The inheritance chain (BaseAgent → DomainAgent → PhonemeAgent) means each level adds only what's new, inheriting everything below. No duplication.

3. **Interface segregation reduces coupling**: Agents depend on interfaces, not implementations. This means changing one agent's internals doesn't cascade changes to other agents.

4. **Composition handles sublayers naturally**: Sub-agents inside an agent match the "has-a" relationship. The layer agent owns its sub-agents, manages their lifecycle, and aggregates their outputs.

5. **Polymorphism enables experimentation**: Different trial structures are just different implementations of the same agent interface. The best one can be selected at runtime.

6. **SOLID principles give design rules**: Instead of ad-hoc decisions about agent structure, SOLID provides principled answers to "should this be one agent or two?" (SRP), "can I add without modifying?" (OCP), "do agents depend on abstractions?" (DIP).

<!-- section_id: "24035360-d0c0-420a-9a14-9cb642b314a4" -->
### Arguments AGAINST (Maybe Not)

1. **Agents aren't classes**: Classes are deterministic — calling `get_phoneme()` always does the same thing. Agents are stochastic — the same prompt might produce different results. OOP assumes deterministic behavior.

2. **Inheritance depth hurts context**: In OOP, deep inheritance hierarchies are an anti-pattern ("favor composition over inheritance"). Similarly, deep agent inheritance chains mean context accumulates at each level, potentially overwhelming leaf agents.

3. **Interfaces need formal definitions**: In OOP, interfaces are enforced by the compiler. In agent teams, "interfaces" are just natural language descriptions in 0AGNOSTIC.md. There's no compiler to enforce them — an agent might violate its interface contract.

4. **Overhead of formalization**: Setting up proper interface definitions, inheritance chains, and composition relationships takes effort. For a small project, a flat team (Trial E) might outperform a carefully structured OOP hierarchy simply because it's faster to set up.

5. **Agent communication is expensive**: In OOP, calling `object.method()` is nearly free (nanoseconds). In agent teams, sending a message costs API calls, context loading, and latency. Every "method call" (delegation) has real cost.

<!-- section_id: "a7232cbb-a8ff-4753-a7d3-dff4614714ad" -->
### Verdict: Strong Yes with Caveats

The OOP model likely WILL improve agent performance because:
- It provides **principled design rules** (SOLID) instead of ad-hoc decisions
- It naturally handles both **vertical** (inheritance = context cascade) and **horizontal** (composition = sublayers) organization
- It solves the **cross-cutting problem** cleanly (interface implementation, not multiple inheritance)
- It gives a framework for **interface aggregation** (public API = what the next layer sees)

**BUT** keep these caveats:
- Cap inheritance depth at 3 levels (BaseAgent → DomainAgent → SpecificAgent)
- Use interfaces for cross-cutting (never multiple inheritance)
- Favor composition for sublayers (has-a, not is-a)
- Accept that "interfaces" are natural language, not compiler-enforced
- Be aware that every "method call" (delegation) costs real API tokens

---

<!-- section_id: "f9d9737f-7146-4e2b-a353-a12ddaa11b9f" -->
## New Experiment Trial: OOP-Structured Agents

<!-- section_id: "035d1a09-1983-4dfd-8e5f-ab69a5f2374b" -->
### Trial O: Full OOP Agent Hierarchy

```
«abstract» BaseAgent
├── context: storage_interface, auth_interface, app_context
├── methods: query_storage(), check_auth()
│
├── «abstract» DomainAgent extends BaseAgent
│   ├── context: + domain_model, entity_interfaces
│   │
│   ├── InfrastructureAgent extends DomainAgent
│   │   ├── «has-a» DatabaseSub, FirebaseSub, StorageMgrSub, AuthSub
│   │   ├── implements: StorageInterface, AuthInterface
│   │   └── aggregated interface: "Infrastructure API"
│   │
│   ├── UserAgent extends DomainAgent
│   │   ├── context: + user model, sessions
│   │   ├── implements: UserInterface
│   │   └── aggregated interface: "User API"
│   │
│   ├── PhonemeAgent extends DomainAgent
│   │   ├── «has-a» GroupsSub, TypesSub, FrequencySub, DisplaySub
│   │   ├── implements: PhonemeQueryInterface, FrequencyInterface
│   │   └── aggregated interface: "Phoneme System API"
│   │
│   ├── TemplateAgent extends DomainAgent
│   │   ├── implements: TemplateInterface
│   │   ├── uses: PhonemeQueryInterface
│   │   └── aggregated interface: "Template API"
│   │
│   ├── ContentAgent extends DomainAgent
│   │   ├── «has-a» WordsSub, SyllablesSub, PositionsSub
│   │   ├── implements: ContentInterface
│   │   ├── uses: TemplateInterface
│   │   └── aggregated interface: "Content API"
│   │
│   ├── ProjectAgent extends DomainAgent
│   │   ├── «has-a» StorageTypeSub, VariantsSub, ContentAssocSub
│   │   ├── implements: ProjectInterface
│   │   ├── uses: ContentInterface
│   │   └── aggregated interface: "Project API"
│   │
│   └── TeamAgent extends DomainAgent
│       ├── implements: CollaborationInterface
│       ├── uses: ProjectInterface, UserInterface
│       └── aggregated interface: "Collaboration API"
│
├── «abstract» CrossCuttingAgent extends BaseAgent
│   ├── Does NOT extend DomainAgent (no domain_model inheritance)
│   ├── Instead: implements specific interfaces from domain agents
│   │
│   ├── EnhancementAgent extends CrossCuttingAgent
│   │   ├── «has-a» TTSSub, VideoSub, SuggestionsSub
│   │   ├── implements: PhonemeQueryInterface, ContentInterface (READ-ONLY)
│   │   └── aggregated interface: "Enhancement APIs" (faceted)
│   │
│   ├── AdminAgent extends CrossCuttingAgent
│   │   ├── implements: PhonemeQueryInterface, TemplateInterface, StorageInterface (WRITE)
│   │   └── aggregated interface: "Admin API"
│   │
│   └── OrchestrationAgent extends CrossCuttingAgent
│       ├── implements: ALL interfaces (READ-ONLY coordinator)
│       └── aggregated interface: "Orchestration API"
│
└── ManagerAgent (the Factory + Mediator)
    ├── Creates agents from BaseAgent subtypes
    ├── Routes tasks to the right agent based on interface
    └── Mediates cross-cutting communication
```

<!-- section_id: "9db01c35-c0b5-4f25-b24a-8b1b054a61c1" -->
### Context Model for Trial O

| Agent | Inherited Context | Own Context | Interface Dependencies |
|-------|------------------|-------------|----------------------|
| BaseAgent | — | storage API, auth API, app context | — |
| DomainAgent | + BaseAgent | + domain model, entity graph | — |
| PhonemeAgent | + DomainAgent | + phoneme groups, types, IPA | PhonemeQueryInterface, FrequencyInterface |
| TemplateAgent | + DomainAgent | + template CRUD, selection logic | TemplateInterface; uses PhonemeQueryInterface |
| ContentAgent | + DomainAgent | + word/syllable/position structure | ContentInterface; uses TemplateInterface |
| ProjectAgent | + DomainAgent | + project lifecycle, variants | ProjectInterface; uses ContentInterface |
| TeamAgent | + DomainAgent | + collaboration, invites, sharing | CollaborationInterface; uses ProjectInterface, UserInterface |
| EnhancementAgent | + BaseAgent (NOT Domain) | + TTS, video, suggestions | uses PhonemeQueryInterface, ContentInterface |
| AdminAgent | + BaseAgent (NOT Domain) | + admin tools, management | uses PhonemeQueryInterface, TemplateInterface, StorageInterface |

<!-- section_id: "75330133-f384-4576-b29b-85a989e421da" -->
### Why This Structure Might Win

1. **Inheritance depth = 3** (Base → Domain → Specific) — manageable, not too deep
2. **Cross-cutting agents skip DomainAgent** — they inherit base capabilities but NOT domain model (they use interfaces instead)
3. **Sublayers are composition** (has-a sub-agents) — each layer agent coordinates its own sub-agents
4. **Interfaces are segregated** — PhonemeQueryInterface (read phonemes) is separate from FrequencyInterface (get stats). Agents only implement what they use.
5. **The diamond problem is solved** — EnhancementAgent uses interfaces, not inheritance, for cross-cutting relationships

---

<!-- section_id: "66b37749-2ef2-4cd9-8d22-04e9f33efa9d" -->
## Summary: OOP Concepts Applied to Agent Design

| OOP Rule | Agent Design Rule |
|----------|------------------|
| **SRP**: One reason to change | One agent per domain cluster |
| **OCP**: Open for extension | New features = new agents, not modified existing agents |
| **LSP**: Subtypes are substitutable | Specialized agents honor the same interface as generic ones |
| **ISP**: Segregate interfaces | Small, focused interfaces (PhonemeQuery, Frequency, Display) not one big "Phoneme" interface |
| **DIP**: Depend on abstractions | Agents depend on interfaces, not specific implementations |
| **Favor composition over inheritance** | Sublayers are has-a (sub-agents), not is-a (inheritance) |
| **Cap inheritance depth** | Max 3 levels: Base → Domain → Specific |
| **Encapsulate internals** | Agents expose aggregated interfaces, hide sublayer details |
| **Use factories** | Manager Agent creates specialized agents based on task type |
| **Use mediators** | Cross-cutting communication goes through the Manager, not direct agent-to-agent |

---

<!-- section_id: "24b9434b-9dc9-4555-b540-341c2304098a" -->
## Next Steps

1. Add Trial O (OOP-structured) to the experiment document
2. Formally define each interface (PhonemeQueryInterface, ContentInterface, etc.) as compact natural language contracts
3. Compare Trial O against Trial G (Feature Coupling + Dependency hybrid) — they're similar but Trial O adds formal OOP structure
4. Design the Manager Agent's routing logic: how does it map incoming tasks to the right agent based on interface?
5. Consider whether the BaseAgent context should be a real 0AGNOSTIC.md template that all agents inherit from
