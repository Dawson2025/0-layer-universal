---
resource_id: "609df5d1-9f42-494d-a6aa-40a5b418fb73"
resource_type: "output"
resource_name: "24_biological_data_structures_per_memory_type"
---
# Biological Data Structures Per Memory Type

<!-- section_id: "8a2837d5-e0c6-441a-8e96-b353e3d4cf17" -->
## Purpose

This document catalogs the **neuroscience-grounded data structures** used by each memory type (time-based, episodic, procedural). While docs 21-23 cover hierarchies and AI system tiers, this document maps biological computational representations to their structural equivalents, providing the foundation for bio-inspired AI memory design.

---

<!-- section_id: "c2ef937f-cfbb-4c55-8640-042bac3674c0" -->
## 1. Time-Based Memory Data Structures

Time-based memory uses specialized structures to encode temporal sequences and timing information.

<!-- section_id: "23616ee2-6cf0-4695-be9f-2a8981ca8564" -->
### Temporal Context Model (TCM)

The most prominent biological model uses a **gradually drifting context vector** that changes slowly over time, acting as a continuous temporal signature.

| Property | Description |
|----------|-------------|
| **Structure** | Continuously evolving context vector |
| **Mechanism** | Starts at one state and gradually evolves, creating unique context signatures for different time points |
| **Retrieval** | Reconstruct "when" something happened by matching current context to stored context |
| **Computational analog** | Exponential moving average or recurrent state update |

The TCM enables temporal discrimination: two events close in time share similar context vectors, while distant events have dissimilar vectors.

<!-- section_id: "2dfadbc3-9b12-4091-9836-af64aa739b2b" -->
### Time Cell Sequences

Neural implementations use **sequential activation patterns** — arrays of "time cells" that fire in stereotypical sequences.

- Each cell activates at a specific delay after an event
- Similar to a chain of dominoes: the position in the sequence encodes elapsed time
- Found in the hippocampus and entorhinal cortex
- **Computational analog**: Ordered arrays or linked lists with position-based indexing

<!-- section_id: "a895061d-89bb-465b-98d6-19b862d72dc3" -->
### Synaptic Decay Spectrum

Recent models propose using a **spectrum of synaptic decay rates** to encode multiple timescales simultaneously.

| Decay Speed | What It Encodes | Timescale |
|-------------|-----------------|-----------|
| Fast | Very recent events | Seconds to minutes |
| Medium | Recent context | Minutes to hours |
| Slow | Longer-term patterns | Hours to days |

Together, the spectrum of decay rates creates a "timeline" of recent past events. The computational analog is multi-scale exponential decay buffers.

---

<!-- section_id: "c0b317ae-562d-42ab-aaa7-a00068b56948" -->
## 2. Episodic Memory Data Structures

Episodic memory is computationally complex because it must bind together **what** happened, **where** it happened, **when** it happened, and **how it felt**.

<!-- section_id: "5a2d4b0e-743a-4fac-86b8-6b598a7c03dd" -->
### Dictionary / Key-Value Stores

Modern neural network models treat episodic memory as a **dictionary-like structure**:

| Component | Role |
|-----------|------|
| **Keys** | Context representations (what was happening, where you were, emotional state) |
| **Values** | Actual event details and sensory content |
| **Retrieval** | Match current context (the key) to find similar past events (the values) |

This maps directly to hash-table or associative-array data structures.

<!-- section_id: "598f99e5-afc8-47ed-a4bc-0fdc0cbb6a64" -->
### Event Segmentation Boundaries

Memory is structured around **event boundaries** — moments when something changes:

- Events are stored as discrete chunks separated by boundaries
- Boundaries occur when prediction errors spike (something unexpected happens)
- The hippocampus shows increased activation at boundaries, "saving" the event to long-term memory
- Creates a **temporal-spatial graph** where nodes are events and edges represent transitions

```
Event_A --[boundary]--> Event_B --[boundary]--> Event_C
   |                       |                       |
 context_A              context_B              context_C
```

<!-- section_id: "2c5f9705-853d-4683-b939-5a9034e04f16" -->
### Contextual Binding Matrices

To link all components (semantic content + time + space + emotion), episodic memory uses **binding matrices**:

- **Outer product associations** between temporal context vector **t** and item representations **f**
- When recalling an episode, temporal context cues the items: items activate proportionally to how similar current context is to their encoding context
- This explains why smells or songs trigger vivid memories — they restore the original context vector

**Mathematical representation**: `M = sum(t_i * f_i^T)` where each episode contributes an outer product to the composite memory matrix.

<!-- section_id: "5f8cbe20-7e9d-41d6-b188-f36cd5dc0f76" -->
### Hierarchical Episode Structures

Episodes are organized **hierarchically** as nested containers:

```
High-level episode: "My vacation to Paris"
├── Sub-episode: "Visiting the Louvre"
│   ├── Micro-episode: "Seeing the Mona Lisa"
│   └── Micro-episode: "Getting lost in Egyptian wing"
└── Sub-episode: "Dinner at the bistro"
```

Stored as **nested tree structures** or **directed acyclic graphs (DAGs)**, allowing retrieval at different levels of granularity.

---

<!-- section_id: "4c85c901-d3eb-42bf-9ce1-d0f54d29bd47" -->
## 3. Procedural Memory Data Structures

Procedural memory (skills and habits) uses structures optimized for **how to do things**, not **what happened**.

<!-- section_id: "77a8fef4-15c1-424f-8e55-8379b9ec267f" -->
### Production Rules (IF-THEN Structures)

The dominant model uses **symbolic production rules**:

```
IF (condition is met)
THEN (execute this action)
```

| Property | Description |
|----------|-------------|
| **Storage** | Rule base / production system |
| **Example** | IF (ball approaches) AND (hold racket) THEN (swing forward) |
| **Chaining** | Rules chain together into complex sequences |
| **Cognitive architecture** | ACT-R and Soar use this as their primary procedural representation |

<!-- section_id: "d3a43a41-4dfb-4cdd-9703-5fc0c9960694" -->
### Motor Sequence Representations

For physical skills, procedural memory uses **trajectory representations**:

- **Temporal sequences** of motor commands
- Each element specifies muscle activation patterns and timing
- Stored in the basal ganglia and cerebellum as **state-action mappings**

```
[state_1 -> action_1] -> [state_2 -> action_2] -> [state_3 -> action_3]
```

**Computational analog**: Finite state machines or Markov decision processes where states map to actions.

<!-- section_id: "f5bc2faa-85b4-46aa-938b-584684c3ae7c" -->
### Chunk Hierarchies

Complex skills are broken into **chunks** organized hierarchically:

| Level | What It Contains | Example (Guitar) |
|-------|-----------------|-------------------|
| Low-level | Basic movements | Individual finger positions |
| Mid-level | Short sequences | A chord progression |
| High-level | Complete skills | Playing an entire song |

This is why practice creates "automaticity" — chunks get bound together so individual steps no longer require conscious attention.

<!-- section_id: "c68faeb9-f45b-4c81-bdf6-e53814d9f0e1" -->
### Reinforcement Learning Structures

Procedural learning uses **value functions** and **policy representations**:

- Maps from states to actions, weighted by expected reward
- Updated through practice via reinforcement learning
- The basal ganglia likely implements something like **Q-learning tables** or **policy gradient structures**

| Structure | What It Stores | Update Rule |
|-----------|---------------|-------------|
| Q-table | State-action values Q(s,a) | Q(s,a) += alpha * (reward + gamma * max(Q(s',a')) - Q(s,a)) |
| Policy | State -> action probability mapping | Updated via reward signal |

---

<!-- section_id: "a297c296-93ea-4d73-917a-3c88bb7865a5" -->
## 4. Cross-Type Comparison

| Memory Type | Primary Data Structure | Key Feature |
|-------------|----------------------|-------------|
| **Time-Based** | Temporal context vectors, time cell sequences | Gradually drifting temporal signatures |
| **Episodic** | Dictionary (key-value), event boundary graphs, binding matrices | Context-based retrieval binding multiple dimensions |
| **Procedural** | Production rules, motor sequences, chunk hierarchies | Condition-action mappings for skill execution |
| **Semantic** (ref) | Knowledge graphs, vectors, hierarchies | Static relationships between concepts |

<!-- section_id: "ffe2f664-b6da-470c-9567-2fb53b30e913" -->
### Integration Insight

Episodic memory sits at the intersection of other types: it uses temporal context from time-based memory, semantic knowledge for meaning, spatial maps for location, and can include procedural elements (remembering *how* you did something). This is why the hierarchy in doc 21 places episodic memory at Level 5 — it integrates multiple lower-level systems.

---

<!-- section_id: "853e4343-b68a-4d41-8c2b-a46645c02692" -->
## Cross-References

- **Memory type hierarchy**: `21_core_memory_structure_hierarchy.md`
- **Data structure hierarchy (computational)**: `22_core_data_structure_hierarchy.md`
- **AI memory system tiers**: `23_core_ai_memory_systems.md`
- **AI agent implementations of these structures**: `25_ai_agent_implementations_per_memory_type.md`
- **Cognitive science foundations**: `01_cognitive_science_foundations.md`
- **Memory by content type**: `03_memory_by_content_type.md`

---

<!-- section_id: "961f10d9-262b-48a6-9b7a-0cad059d3517" -->
## Sources

- [Computational Models of Episodic Memory (PMC9000961)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9000961/)
- [Temporal Context Model (PMC1421376)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1421376/)
- [Temporal Context Model — Howard & Kahana 2002](https://memory.psych.upenn.edu/files/pubs/HowaKaha02.pdf)
- [Contextual Retrieval and Temporal Context (PMC1444898)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1444898/)
- [Time Cells in Computational Neuroscience (Frontiers)](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2020.00051/full)
- [Time Cell Sequences in PNAS](https://www.pnas.org/doi/10.1073/pnas.1921609117)
- [Synaptic Decay Spectrum Model (OpenReview)](https://openreview.net/forum?id=4naoku2Ak0)
- [Episodic Memory and Event Boundaries (PMC12313307)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313307/)
- [Event Segmentation in Episodic Memory (Nature Communications)](https://www.nature.com/articles/s41467-022-28216-9)
- [Hierarchical Episode Structures (Wiley)](https://onlinelibrary.wiley.com/doi/abs/10.1111/tops.12505)
- [Procedural Memory in AI Agents (arXiv:2505.05083)](https://arxiv.org/html/2505.05083v1)
- [Procedural Memory — Neuroscience (ScienceDirect)](https://www.sciencedirect.com/topics/neuroscience/procedural-memory)
- [TCM Review — Howard 2004](https://sites.bu.edu/tcn/files/2015/12/Howard04-JMP.pdf)
