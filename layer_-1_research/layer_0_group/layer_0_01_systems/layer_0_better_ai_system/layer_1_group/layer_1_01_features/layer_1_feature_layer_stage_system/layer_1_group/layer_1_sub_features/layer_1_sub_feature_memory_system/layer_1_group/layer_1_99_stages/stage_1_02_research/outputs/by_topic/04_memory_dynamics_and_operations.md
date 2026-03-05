---
resource_id: "26a4b925-b5cf-48b2-a63e-e6d89ce5bfef"
resource_type: "output"
resource_name: "04_memory_dynamics_and_operations"
---
# Memory Dynamics: Formation, Evolution, Retrieval, and Forgetting

<!-- section_id: "717e8ee2-e34a-4bd2-946e-550a8ad1e4c2" -->
## Overview

How memories are created, transformed, accessed, and removed over time. These dynamics apply across all memory types and form the lifecycle of information in agent systems.

---

<!-- section_id: "94c9f2e0-7ad1-4328-a7f4-d756c9eac4cd" -->
## 1. Memory Formation (Encoding / Extraction)

<!-- section_id: "f33a2c77-97b8-4ee8-9fb7-6fe58f060676" -->
### Raw Storage
- Direct preservation of input/output sequences
- No processing or transformation
- Example: Appending each message to conversation log
- Implementations: ConversationBufferMemory, chat history databases

<!-- section_id: "bbb9517a-a4b3-4239-8181-8c8ca704d0f2" -->
### Extraction-Based Formation
- LLM-driven extraction of salient information from raw data
- Identifies key facts, entities, relationships, preferences
- Example: Mem0 analyzing conversations to extract user preferences
- Example: CrewAI's unified Memory class using LLM to infer scope, categories, importance

<!-- section_id: "1c982cef-1788-4870-bbeb-1d37f5ca3bfd" -->
### Chunking / Segmentation
- Breaking continuous streams into discrete memory units
- Semantic chunking (by meaning) vs. fixed-size chunking (by tokens)
- Example: MemoryOS grouping dialogue pages into topic-based segments

<!-- section_id: "77678296-1c9f-4efc-95ef-7a1d434a41e1" -->
### Embedding / Encoding
- Converting textual memory into vector representations
- Enables similarity-based retrieval
- Dense embeddings (sentence transformers) vs. sparse (BM25)

<!-- section_id: "26ad27c9-03e4-4f28-bb13-7c613899d15f" -->
### Schema Formation
- Organizing extracted information into structured formats
- Knowledge graph triple extraction (subject-predicate-object)
- Entity-attribute-value structures
- Example: LangChain ConversationKGMemory extracting knowledge graph triples

---

<!-- section_id: "85547376-2f7f-403a-896f-03bafc82a46e" -->
## 2. Memory Consolidation (STM → LTM Transfer)

<!-- section_id: "7d8f56ba-efa5-437d-bc41-4edb53a989f8" -->
### Progressive Summarization
- Information is summarized as it ages
- Recent: verbatim → Older: summary → Oldest: key facts only
- Example: ConversationSummaryBufferMemory keeping recent raw + old summarized

<!-- section_id: "354f5727-35d1-4969-bd59-68da1e216920" -->
### Tier Promotion
- Information moves from faster/smaller to slower/larger storage
- **MemoryOS**: STM → MTM (FIFO when STM full) → LPM (heat-based scoring: visit frequency + interaction length + temporal decay)
- **MemGPT**: Message buffer → Core memory → Archival memory (agent-controlled)

<!-- section_id: "912da266-87af-446d-83af-acc029cf0d5a" -->
### Reflection-Based Consolidation
- Periodic review of recent experiences to extract lasting insights
- **Generative Agents**: Reflection mechanism synthesizing observations into higher-level insights
- **Reflexion**: Self-reflection on task outcomes to improve future performance
- **SAGE**: Self-evolving reflective memory with consolidation

<!-- section_id: "e22e358d-df4e-4d3a-a5be-8b32dee6979e" -->
### Complementary Learning Systems
- Inspired by hippocampus (fast, episodic) → neocortex (slow, semantic) transfer
- AI analog: External episodic memory → parametric knowledge via fine-tuning
- Sleep/replay mechanisms: periodic offline consolidation

---

<!-- section_id: "1bea41ac-24e4-49bd-bf23-4084940b12d6" -->
## 3. Memory Updating

<!-- section_id: "41088c0e-967f-40ff-9de9-3b7f019fe9b6" -->
### Additive Updates
- New information appended to existing memory
- No modification of prior entries
- Simplest but can lead to contradictions

<!-- section_id: "83cc9a51-09e4-47f6-a0a3-4294ce8bf9fc" -->
### In-Place Modification
- Existing memory entries modified with new information
- Entity summaries updated as new facts emerge
- Example: LangChain EntityMemory updating entity descriptions

<!-- section_id: "536d128f-6700-4705-ab71-db46010cb33b" -->
### Knowledge Editing
- Modifying specific facts in parametric memory (model weights)
- Techniques: ROME, MEMIT, knowledge neurons
- Challenges: locality (not affecting unrelated knowledge), generalization

<!-- section_id: "16a27cc7-2bf9-4939-acd2-09ce5e39efbc" -->
### Versioning
- Maintaining history of memory states
- MemOS MemCube: encapsulates content + metadata (provenance, versioning)
- Enables rollback and audit trails

<!-- section_id: "6eb7ce5f-c68e-4da3-ab41-c2e782a97564" -->
### Conflict Resolution
- Handling contradictory information across memory sources
- Recency-based: newer information preferred
- Source-reliability: trusted sources weighted higher
- SHIMI CRDT-style: merge function satisfying commutativity, idempotence, associativity

---

<!-- section_id: "3a46ffd0-233d-4e1b-8c5b-83e1cac22dd8" -->
## 4. Memory Retrieval

<!-- section_id: "8812988d-2fe1-48a6-a191-6e6ac1b714b5" -->
### Retrieval Paradigms (from arXiv:2505.00675)

#### Query-Centered
- Focus on improving query formulation
- Query expansion, reformulation, decomposition
- HyDE: Hypothetical Document Embeddings for better queries

#### Memory-Centered
- Focus on better indexing and ranking of stored memories
- Improved embedding models, re-ranking, multi-index strategies

#### Event-Centered
- Focus on temporal and causal structures
- Temporal ordering, causal chains, event sequences

<!-- section_id: "ff9513e2-d827-4a9a-ab22-c684e6102e4d" -->
### Retrieval Mechanisms

| Mechanism | How It Works | Best For |
|-----------|-------------|----------|
| **Semantic similarity** | Vector cosine similarity between query and memory embeddings | Finding conceptually related information |
| **Keyword/entity match** | Exact or fuzzy string matching | Looking up specific named items |
| **Temporal queries** | Filtering by time ranges or recency | "What happened yesterday?" |
| **Graph traversal** | Following relationships in knowledge graphs | Multi-hop reasoning, entity relationships |
| **Hierarchical descent** | Top-down traversal through semantic levels (SHIMI) | Precise semantic narrowing |
| **Composite scoring** | Weighted combination of recency + relevance + importance | Balanced, multi-factor retrieval |

<!-- section_id: "64c0f9f7-9e9e-4c45-959d-693807f31dab" -->
### Composite Scoring Example (CrewAI)
```
score = (recency_weight * recency_score) +
        (semantic_weight * semantic_similarity) +
        (importance_weight * importance_score)
```
- `recency_half_life_days`: 30 (default)
- Configurable weights for each factor

<!-- section_id: "abb596c1-f37a-4965-ab26-2d497fc8d1f5" -->
### Two-Stage Retrieval (MemoryOS)
1. **Segment matching**: Find relevant topic segments in MTM
2. **Page-level ranking**: Semantic ranking within matched segments

---

<!-- section_id: "4e3c39f7-f9b5-48f9-a88e-bd435b3a222b" -->
## 5. Memory Forgetting / Decay

<!-- section_id: "615b0eca-816a-4cd0-b975-4575846f3fb4" -->
### Why Forgetting Matters
- Prevents memory bloat and retrieval degradation
- Removes outdated or contradictory information
- Reduces noise in retrieval results
- Mirrors biological memory optimization

<!-- section_id: "7233f9e8-ee4a-4e2c-a2c1-2b15cf3602a1" -->
### Forgetting Mechanisms

#### Temporal Decay
- Memories lose activation over time without access
- ACT-R: logarithmic decay of base-level activation
- Exponential decay curves with configurable half-life
- CrewAI: `recency_half_life_days` parameter

#### Importance-Based Retention
- Low-importance memories forgotten first
- Importance scored by access frequency, LLM-judged salience, or user marking
- MemoryOS heat scoring: visit frequency + interaction length + temporal proximity

#### Capacity-Based Eviction
- When storage reaches capacity, least relevant items evicted
- MemoryOS STM: FIFO eviction (7-page limit)
- LRU (Least Recently Used) or LFU (Least Frequently Used) policies

#### Active Forgetting / Unlearning
- Deliberate removal of specific information
- Machine unlearning techniques for parametric memory
- Privacy-motivated deletion
- Contradiction-driven removal (when new info supersedes old)

#### Consolidation-Based Forgetting
- Details lost during summarization
- Raw episodes replaced by summaries
- Specific instances merged into general patterns

<!-- section_id: "b370a36b-f8f9-465e-aeb4-6905e72238ad" -->
### Anti-Forgetting: Preventing Catastrophic Loss
- **SAGE**: Self-evolving agents with mechanisms to mitigate catastrophic forgetting in lifelong learning
- **WISE, ELDER**: Papers on lifelong learning balancing stability and plasticity
- Replay mechanisms: periodically re-presenting old memories during training

---

<!-- section_id: "31d7d4f9-fe7b-4aa5-968b-23a2b1f93325" -->
## 6. Memory Integration and Synthesis

<!-- section_id: "18cbaada-a1b1-448f-97ac-af71bf47fd30" -->
### Cross-Memory Integration
- Combining information from multiple memory types for coherent output
- MemoryOS Generation Module: synthesizes STM + MTM + LPM into unified prompts
- Challenge: resolving conflicts between memory sources

<!-- section_id: "be90ce7b-ffb5-4e73-b7de-a133b9701a1f" -->
### Memory-Augmented Generation
- Retrieved memories injected into LLM context for response generation
- RAG: external memory augments parametric knowledge
- Balance between relying on internal vs. external memory

---

<!-- section_id: "fe800720-a6a5-4015-b80c-bd189314cd73" -->
## Dynamics Lifecycle Summary

```
Input → Formation (extract/chunk/embed) → Storage (STM/MTM/LTM)
                                              ↓
                                        Consolidation (promote/summarize/reflect)
                                              ↓
                                        Evolution (update/version/resolve conflicts)
                                              ↓
                                        Retrieval (query/score/rank)
                                              ↓
                                        Forgetting (decay/evict/unlearn)
```

---

<!-- section_id: "7dfc8205-981c-4773-84a1-7b1d00ebb366" -->
## Sources

- [Rethinking Memory in AI (arXiv:2505.00675)](https://arxiv.org/html/2505.00675v1)
- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
- [SAGE: Self-Evolving Reflective Memory Agents](https://www.emergentmind.com/topics/self-evolving-agents-with-reflective-and-memory-augmented-abilities-sage)
