# Learning Path: Understanding AI Memory Systems and Their Neurological Foundations

## Purpose

An ordered sequence of videos, articles, and our own research documents to build understanding from the ground up. Start at Phase 1 and work through in order — each phase builds on the previous one.

---

## Phase 1: How a Single Neuron Works

**Goal**: Understand the basic unit before understanding networks of them.

### Watch
1. **Khan Academy: The Neuron and Nervous System** — search YouTube for `Khan Academy neuron action potential`
   - Covers what a neuron is, dendrites, axons, cell body
   - ~10 minutes, foundational

2. **Khan Academy: Synapse and Neurotransmitters** — search YouTube for `Khan Academy synapse neurotransmitter`
   - How one neuron talks to another across the synaptic gap
   - Glutamate, receptors, signal transmission
   - ~10 minutes

3. **Osmosis: Action Potential** — search YouTube for `Osmosis action potential`
   - Beautiful animation of how electrical signals travel down a neuron
   - ~8 minutes

### Read (our docs)
- `01_cognitive_science_foundations.md` → Section 1 (Human Memory Types) — skim to see the big picture of how neuroscience maps to AI memory

---

## Phase 2: How Connections Strengthen and Weaken (Memory at the Molecular Level)

**Goal**: Understand the physical mechanism of how memories are formed — LTP and LTD.

### Watch (in this order)
1. **2-Minute Neuroscience: Long-Term Potentiation (LTP)**
   - [neuroscientificallychallenged.com](https://neuroscientificallychallenged.com/posts/2-minute-neuroscience-long-term-potentiation)
   - Quick 2-minute animated overview — NMDA receptor, magnesium block, calcium, AMPA insertion
   - Watch this FIRST to get the gist

2. **Alila Medical Media: Long-Term Potentiation and Memory**
   - [alilamedicalmedia.com](https://www.alilamedicalmedia.com/media/981890fd-dc0b-4db5-aa9a-7242290c3984-long-term-potentiation-and-memory-narrated-animation)
   - Professional 3D animation, more detail — both phases of LTP, connection to short-term vs long-term memory
   - Watch AFTER the 2-minute version to deepen understanding

3. **Khan Academy: Long-Term Potentiation and Synaptic Plasticity**
   - [khanacademy.org](https://www.khanacademy.org/test-prep/mcat/processing-the-environment/memory/v/long-term-potentiation-and-synaptic-plasticity)
   - Lecture-style, fills in conceptual gaps from the animations

4. **2-Minute Neuroscience: Long-Term Depression (LTD)**
   - [neuroscientificallychallenged.com](https://neuroscientificallychallenged.com/posts/2-minute-neuroscience-long-term-depression-ltd)
   - The opposite of LTP — how unused connections weaken (forgetting mechanism)

5. **(Optional deep dive) Ninja Nerd: Synaptic Plasticity** — search YouTube for `Ninja Nerd synaptic plasticity LTP`
   - 30-60 minute whiteboard lecture, step-by-step through every molecular detail
   - Only if you want the full biochemistry

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 3, "The Actual Mechanism" → **Level 1: Long-Term Potentiation**
  - Our own write-up with the "hard drive" analogy — ties the videos to the bigger picture

---

## Phase 3: How Cause-and-Effect Gets Encoded (STDP)

**Goal**: Understand how the brain learns that A causes B through spike timing.

### Watch
1. **Neuromatch Academy: STDP Interactive Tutorial**
   - [compneuro.neuromatch.io](https://compneuro.neuromatch.io/tutorials/W2D3_BiologicalNeuronModels/student/W2D3_Tutorial4.html)
   - Interactive — you can adjust timing parameters and see the effect on synaptic strength
   - This is the best resource for STDP because you can play with it

2. **YouTube search**: `spike timing dependent plasticity animation` or `STDP neuroscience explained`
   - Look for videos that show the timing curve (pre-before-post = strengthen, post-before-pre = weaken)

### Read
- [Scholarpedia: STDP](http://www.scholarpedia.org/article/Spike-timing_dependent_plasticity) — the classic timing curve diagram and explanation
- `15_vectors_graphs_and_neurology.md` → Section 3, "The Actual Mechanism" → **Level 2: Spike-Timing-Dependent Plasticity**
  - Our write-up with the "fire causes burn" example

---

## Phase 4: How Concepts Form in the Brain

**Goal**: Understand how networks of neurons become "concepts" (like your tree example).

### Watch
1. **YouTube search**: `how the brain forms concepts distributed representation neuroscience`
2. **YouTube search**: `Hebb's rule neurons that fire together wire together explained`
3. **(Optional) YouTube search**: `concept cells grandmother neuron Jennifer Aniston neuron` — fascinating research on single neurons that respond to specific concepts

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 3, "Concept Formation (Your Tree Example)"
  - How concepts are distributed across visual, auditory, motor, emotional brain regions
- `01_cognitive_science_foundations.md` → Section 4 (Key Principles: Complementary Learning Systems, Levels of Processing, Chunking)

---

## Phase 5: How Episodic Memory and Sequences Work

**Goal**: Understand how the brain chains events in order and connects the beginning of a story to the end.

### Watch
1. **YouTube search**: `hippocampus place cells time cells explained` — how the hippocampus maps both space and time
2. **YouTube search**: `hippocampus memory consolidation sharp wave ripple` — how sequences get replayed and compressed during sleep
3. **YouTube search**: `how sleep consolidates memory hippocampus neocortex` — the transfer from short-term hippocampal storage to long-term cortical storage

### Read
- [BrainFacts: Storing Memories in Your Synapses](https://www.brainfacts.org/thinking-sensing-and-behaving/learning-and-memory/2018/storing-memories-in-your-synapses-101118)
- `15_vectors_graphs_and_neurology.md` → Section 3, "The Actual Mechanism" → **Level 3: Time Cells and Sequence Encoding**
  - Time cells, theta oscillations, sharp-wave ripple replay, forward and reverse replay
  - How beginning and end of a story connect through compressed replay during sleep

### Read (our docs)
- `02_memory_by_duration.md` — How memory moves from sensory → short-term → working → long-term
- `04_memory_dynamics_and_operations.md` → Section 2 (Consolidation) — How STM becomes LTM: progressive summarization, tier promotion, reflection

---

## Phase 6: How Different Relationship Types Are Processed

**Goal**: Understand which brain regions handle which types of relationships (cause-effect, categories, part-whole, etc.).

### Watch
1. **YouTube search**: `prefrontal cortex relational reasoning neuroscience` — how the PFC integrates relationships
2. **YouTube search**: `temporal cortex semantic memory categories` — how category knowledge (is_a) is organized
3. **(Optional) YouTube search**: `transitive inference brain RLPFC hippocampus` — the specific experiment showing how the brain combines A>B and B>C to infer A>C

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 3, full subsection on "How the Brain Encodes Relationship TYPES"
  - The two-layer relational system (hippocampus for encoding, RLPFC for integration)
  - The anterior-posterior gradient table
  - Four semantic mechanisms (Pulvermüller)
  - The key insight: relationship types are encoded by WHICH CIRCUIT processes them

### Read (papers, for deeper understanding)
- [Transitive Inference: RLPFC and Hippocampus (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2858584/)
- [Neural mechanisms of relational learning (Nature Neuroscience, 2024)](https://www.nature.com/articles/s41593-024-01852-8)

---

## Phase 7: Vector Embeddings — What They Are and What They Can't Do

**Goal**: Understand the AI side — how vector embeddings work and why they're limited compared to the brain.

### Watch
1. **YouTube search**: `what are vector embeddings explained simply` — many good explainers exist
2. **YouTube search**: `word2vec explained visual` — the original word embedding breakthrough, visually explained
3. **YouTube search**: `RAG retrieval augmented generation explained` — how vector embeddings are used for AI memory

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 1 (Vector Embeddings: What They Actually Are)
  - How they're created, what they capture, what they can't capture, the retrieval mechanism
- `09_rag_and_knowledge_graphs.md` → Sections 1-2 (RAG as Memory, Agentic RAG)
  - How vector embeddings are used as memory in AI agent systems
- `09_rag_and_knowledge_graphs.md` → Section 7 (Retrieval Strategies)
  - Dense vs sparse vs hybrid retrieval, re-ranking

---

## Phase 8: Knowledge Graphs — What They Are and Why They're Closer to How the Brain Works

**Goal**: Understand knowledge graphs, relationship types, and how they compare to both vectors and the brain.

### Watch
1. **YouTube search**: `what is a knowledge graph explained` — conceptual overview
2. **YouTube search**: `Neo4j knowledge graph tutorial` — see a real graph database in action
3. **YouTube search**: `knowledge graph vs vector database RAG` — direct comparison for AI memory use

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 2 (Knowledge Graphs: What They Actually Are)
  - Full taxonomy of relationship types (structural, causal, functional, comparative, conditional, procedural)
  - How they're stored and queried (Cypher examples)
- `09_rag_and_knowledge_graphs.md` → Sections 3-5 (Knowledge Graph Memory, Graph RAG, Hybrid)
  - Knowledge graphs as memory systems, Graph RAG, vector+graph hybrid approaches
- `09_rag_and_knowledge_graphs.md` → Section 6 (Storage Backend Technologies)
  - Vector databases (Pinecone, ChromaDB, etc.) vs graph databases (Neo4j, etc.)

---

## Phase 9: The Full Comparison — Vectors vs Graphs vs Brain

**Goal**: Synthesize everything — understand the strengths, weaknesses, and analogies across all three systems.

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 4 (The Three-Way Comparison)
  - What each system is best at (comparison table)
  - Where the analogies hold and where they break down
- `15_vectors_graphs_and_neurology.md` → Section 5 (Implications for AI Memory System Design)
  - Why hybrid approaches win, what the brain teaches us about AI memory
- `14_memory_types_best_for_guide.md` → Decision Matrix at the bottom
  - Quick reference: "If you need X, use Y"

---

## Phase 10: Knowledge Graphs as a Learning Tool (Connecting to PERIO)

**Goal**: Understand how building knowledge graphs can serve as an active encoding/learning tool.

### Read (our docs)
- `15_vectors_graphs_and_neurology.md` → Section 3.5 (Knowledge Graphs as a Learning and Encoding Tool)
  - PERIO framework alignment table
  - Knowledge graph vs mind map comparison
  - 5 reasons interactive KGs beat static mind maps
  - 5 cautions to keep in mind

---

## Phase 11: AI Memory Systems — The Full Landscape

**Goal**: Understand all the different AI memory system approaches, benchmarks, and practical implementation.

### Read (our docs, in this order)
1. `00_overview_and_taxonomy.md` — Master overview with 3D taxonomy (forms, functions, dynamics)
2. `03_memory_by_content_type.md` — All content-based memory types (episodic, semantic, procedural, etc.)
3. `06_dedicated_memory_platforms.md` — MemGPT/Letta, Mem0, Zep, MemoryOS, MemOS, SHIMI
4. `05_framework_implementations.md` — LangChain, CrewAI, AutoGPT implementations
5. `12_benchmarks_and_performance.md` — LoCoMo, LongMemEval results, head-to-head comparisons
6. `14_memory_types_best_for_guide.md` — Decision guide: which memory type for which situation
7. `13_practitioners_complete_guide.md` — Complete design-to-implementation guide (the big one, read last)

---

## Phase 12: Our Framework Specifically

**Goal**: Understand what memory system we're building and the design decisions ahead.

### Read (our docs)
1. `../stage_1_01_request_gathering/outputs/01_problem_statement.md` — What problem we're solving
2. `../stage_1_01_request_gathering/outputs/02_current_state.md` — What we have now (gaps and strengths)
3. `../stage_1_01_request_gathering/outputs/03_requirements.md` — What the system must/should/could do
4. `../stage_1_01_request_gathering/outputs/04_constraints.md` — What limits our design
5. `../stage_1_01_request_gathering/outputs/05_use_cases.md` — Concrete scenarios to support
6. `../stage_1_01_request_gathering/outputs/06_open_questions.md` — 11 design decisions still needed

---

## Quick Reference: Estimated Time Per Phase

| Phase | Topic | Time Estimate |
|-------|-------|--------------|
| 1 | Single neuron basics | 30 min |
| 2 | LTP/LTD (memory mechanism) | 30-60 min |
| 3 | STDP (causal encoding) | 20-30 min |
| 4 | Concept formation | 20-30 min |
| 5 | Episodic memory and sequences | 30-45 min |
| 6 | Relationship types in the brain | 30-45 min |
| 7 | Vector embeddings | 30-45 min |
| 8 | Knowledge graphs | 30-45 min |
| 9 | Full comparison (vectors vs graphs vs brain) | 20-30 min (reading) |
| 10 | KGs as learning tool / PERIO | 15-20 min (reading) |
| 11 | AI memory systems landscape | 2-3 hours (reading) |
| 12 | Our framework specifically | 1-1.5 hours (reading) |

**Total**: ~8-10 hours spread across sessions. Phases 1-6 are neuroscience foundation. Phases 7-9 bridge to AI. Phases 10-12 are application.

---

## Tips for Going Through This Path

1. **Don't rush** — watch each video, pause, think about what you just saw before moving to the next
2. **Read our docs after watching videos** — the docs will make much more sense with the visual foundation
3. **Build your knowledge graph as you go** — add nodes and edges for each new concept you learn (this IS the encoding)
4. **Sleep between phases** — sharp-wave ripple replay consolidates what you learned (the science says so!)
5. **Revisit earlier phases** after completing later ones — you'll see things differently with more context (interleaving/retrieval practice)

---

## Sources

All video and article links are maintained in `15_vectors_graphs_and_neurology.md` → Sources → Video Resources section.
All research document references point to files in this same `by_topic/` directory.
