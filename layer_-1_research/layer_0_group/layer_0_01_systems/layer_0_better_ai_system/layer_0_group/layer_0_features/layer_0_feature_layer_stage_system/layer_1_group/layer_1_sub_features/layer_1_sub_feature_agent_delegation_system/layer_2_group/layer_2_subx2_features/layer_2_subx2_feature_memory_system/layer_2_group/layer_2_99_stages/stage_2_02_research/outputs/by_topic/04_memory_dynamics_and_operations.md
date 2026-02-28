# Memory Dynamics: Formation, Evolution, Retrieval, and Forgetting

## Overview

How memories are created, transformed, accessed, and removed over time. These dynamics apply across all memory types and form the lifecycle of information in agent systems.

---

## 1. Memory Formation (Encoding / Extraction)

### Raw Storage
- Direct preservation of input/output sequences
- No processing or transformation
- Example: Appending each message to conversation log
- Implementations: ConversationBufferMemory, chat history databases

### Extraction-Based Formation
- LLM-driven extraction of salient information from raw data
- Identifies key facts, entities, relationships, preferences
- Example: Mem0 analyzing conversations to extract user preferences
- Example: CrewAI's unified Memory class using LLM to infer scope, categories, importance

### Chunking / Segmentation
- Breaking continuous streams into discrete memory units
- Semantic chunking (by meaning) vs. fixed-size chunking (by tokens)
- Example: MemoryOS grouping dialogue pages into topic-based segments

### Embedding / Encoding
- Converting textual memory into vector representations
- Enables similarity-based retrieval
- Dense embeddings (sentence transformers) vs. sparse (BM25)

### Schema Formation
- Organizing extracted information into structured formats
- Knowledge graph triple extraction (subject-predicate-object)
- Entity-attribute-value structures
- Example: LangChain ConversationKGMemory extracting knowledge graph triples

---

## 2. Memory Consolidation (STM → LTM Transfer)

### Progressive Summarization
- Information is summarized as it ages
- Recent: verbatim → Older: summary → Oldest: key facts only
- Example: ConversationSummaryBufferMemory keeping recent raw + old summarized

### Tier Promotion
- Information moves from faster/smaller to slower/larger storage
- **MemoryOS**: STM → MTM (FIFO when STM full) → LPM (heat-based scoring: visit frequency + interaction length + temporal decay)
- **MemGPT**: Message buffer → Core memory → Archival memory (agent-controlled)

### Reflection-Based Consolidation
- Periodic review of recent experiences to extract lasting insights
- **Generative Agents**: Reflection mechanism synthesizing observations into higher-level insights
- **Reflexion**: Self-reflection on task outcomes to improve future performance
- **SAGE**: Self-evolving reflective memory with consolidation

### Complementary Learning Systems
- Inspired by hippocampus (fast, episodic) → neocortex (slow, semantic) transfer
- AI analog: External episodic memory → parametric knowledge via fine-tuning
- Sleep/replay mechanisms: periodic offline consolidation

---

## 3. Memory Updating

### Additive Updates
- New information appended to existing memory
- No modification of prior entries
- Simplest but can lead to contradictions

### In-Place Modification
- Existing memory entries modified with new information
- Entity summaries updated as new facts emerge
- Example: LangChain EntityMemory updating entity descriptions

### Knowledge Editing
- Modifying specific facts in parametric memory (model weights)
- Techniques: ROME, MEMIT, knowledge neurons
- Challenges: locality (not affecting unrelated knowledge), generalization

### Versioning
- Maintaining history of memory states
- MemOS MemCube: encapsulates content + metadata (provenance, versioning)
- Enables rollback and audit trails

### Conflict Resolution
- Handling contradictory information across memory sources
- Recency-based: newer information preferred
- Source-reliability: trusted sources weighted higher
- SHIMI CRDT-style: merge function satisfying commutativity, idempotence, associativity

---

## 4. Memory Retrieval

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

### Retrieval Mechanisms

| Mechanism | How It Works | Best For |
|-----------|-------------|----------|
| **Semantic similarity** | Vector cosine similarity between query and memory embeddings | Finding conceptually related information |
| **Keyword/entity match** | Exact or fuzzy string matching | Looking up specific named items |
| **Temporal queries** | Filtering by time ranges or recency | "What happened yesterday?" |
| **Graph traversal** | Following relationships in knowledge graphs | Multi-hop reasoning, entity relationships |
| **Hierarchical descent** | Top-down traversal through semantic levels (SHIMI) | Precise semantic narrowing |
| **Composite scoring** | Weighted combination of recency + relevance + importance | Balanced, multi-factor retrieval |

### Composite Scoring Example (CrewAI)
```
score = (recency_weight * recency_score) +
        (semantic_weight * semantic_similarity) +
        (importance_weight * importance_score)
```
- `recency_half_life_days`: 30 (default)
- Configurable weights for each factor

### Two-Stage Retrieval (MemoryOS)
1. **Segment matching**: Find relevant topic segments in MTM
2. **Page-level ranking**: Semantic ranking within matched segments

---

## 5. Memory Forgetting / Decay

### Why Forgetting Matters
- Prevents memory bloat and retrieval degradation
- Removes outdated or contradictory information
- Reduces noise in retrieval results
- Mirrors biological memory optimization

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

### Anti-Forgetting: Preventing Catastrophic Loss
- **SAGE**: Self-evolving agents with mechanisms to mitigate catastrophic forgetting in lifelong learning
- **WISE, ELDER**: Papers on lifelong learning balancing stability and plasticity
- Replay mechanisms: periodically re-presenting old memories during training

---

## 6. Memory Integration and Synthesis

### Cross-Memory Integration
- Combining information from multiple memory types for coherent output
- MemoryOS Generation Module: synthesizes STM + MTM + LPM into unified prompts
- Challenge: resolving conflicts between memory sources

### Memory-Augmented Generation
- Retrieved memories injected into LLM context for response generation
- RAG: external memory augments parametric knowledge
- Balance between relying on internal vs. external memory

---

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

## Sources

- [Rethinking Memory in AI (arXiv:2505.00675)](https://arxiv.org/html/2505.00675v1)
- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
- [SAGE: Self-Evolving Reflective Memory Agents](https://www.emergentmind.com/topics/self-evolving-agents-with-reflective-and-memory-augmented-abilities-sage)
