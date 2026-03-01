# Dedicated Memory Platforms and Systems

## Overview

Purpose-built memory platforms that can be integrated into any AI agent system, providing memory as a service layer independent of the agent framework.

---

## 1. MemGPT / Letta

### Paper
"MemGPT: Towards LLMs as Operating Systems" (Packer et al., 2023, arXiv:2310.08560)

### Core Concept
Inspired by operating system virtual memory management: provides the illusion of unlimited memory while working within fixed context window limits. The LLM itself acts as the "OS" that manages memory, moving data in and out of context using designated tools.

### Memory Architecture (Four Tiers)

#### Message Buffer (Immediate Context)
- Most recent messages in active conversation
- Always in context window
- Temporary; evicted or summarized when full
- Analog: CPU cache

#### Core Memory (In-Context Editable Blocks)
- Managed, editable memory blocks pinned permanently to context window
- Agent updates its own blocks via tools (or external agents modify them)
- Contains structured blocks: `human` (user info) and `persona` (agent identity)
- Each block has: label, description, editable value, character limit
- Analog: RAM

#### Recall Memory (Conversation Archive)
- Complete interaction history stored externally
- Searchable when needed, automatically saved to disk
- Raw conversation records (not processed/indexed)
- Analog: Disk (sequential files)

#### Archival Memory (Knowledge Store)
- Processed, indexed knowledge in external databases
- Explicitly formulated knowledge (not raw conversation data)
- Formats: vector databases or graph databases
- Accessed via specialized tool calls (vector search, graph traversal)
- Analog: Disk (indexed database)

### Key Innovation
- **Self-editing memory**: The agent reads and writes its own core memory blocks
- **Function-calling memory management**: Memory operations exposed as tools
- **Virtual context management**: Agent controls what's in context window

### Letta Framework (2024+)
- Open-source agent framework building on MemGPT concepts
- Added: multi-agent support, tool builder, REST API
- Persistent agents with stateful memory across sessions
- Agent loop rearchitected drawing from ReAct, MemGPT, and Claude Code patterns

---

## 2. Mem0

### Paper
"Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory" (Chhikara et al., 2025, arXiv:2504.19413)

### Core Concept
A universal memory layer that sits between applications and LLMs. Automatically extracts, consolidates, and retrieves information from conversations.

### Architecture

#### Hybrid Datastore
Three complementary storage backends:
- **Vector store**: Embedding-based semantic search
- **Graph store**: Relational structure between entities (knowledge graphs)
- **Key-value store**: Fast lookup for specific items

#### Memory Types Supported
- Episodic memory (interaction records)
- Semantic memory (factual knowledge)
- Procedural memory (how-to knowledge)
- Associative memory (cross-referential links)

#### Active Curation
- Not passive storage: actively updates, enriches, and cleans memory as new information arrives
- Contradiction detection and resolution
- Deduplication of semantically equivalent memories

### Performance
- 26% improvement in LLM-as-a-Judge metric over OpenAI
- 91% lower p95 latency
- 90%+ token cost savings
- 1.44 second response latency (92% improvement)

### Integration
- Works with any LLM provider (OpenAI, Anthropic, Ollama, custom)
- CrewAI integration (as memory provider)
- AWS integration (ElastiCache + Neptune Analytics)
- $24M raised (October 2025)

---

## 3. Zep

### Core Concept
Temporal knowledge graph architecture for AI agent memory. Focuses on temporal reasoning and enterprise use cases.

### Architecture
- **Temporal knowledge graph**: Entities and relationships with temporal metadata
- **Fact extraction**: Automatic extraction of facts from conversations
- **Temporal queries**: "What did the user say about X last week?"
- **User/session scoping**: Memory partitioned by user and session

### Performance
- Outperforms MemGPT on Deep Memory Retrieval benchmark
- Validated on LongMemEval benchmark (complex temporal reasoning)
- Focus on enterprise use cases requiring temporal reasoning

### Key Differentiator
- Temporal-first design (vs. Mem0's hybrid and MemGPT's OS-inspired approach)
- Knowledge graph as primary representation (not just vector similarity)

---

## 4. MemoryOS (EMNLP 2025 Oral)

### Paper
"Memory OS of AI Agent" (Kang et al., 2025, arXiv:2506.06326)

### Core Concept
Inspired by OS memory management principles: hierarchical storage with automated promotion/demotion between levels.

### Three-Tier Architecture

#### Short-Term Memory (STM)
- **Capacity**: 7 dialogue pages
- **Storage**: User queries + model responses + timestamps per page
- **Contextual chains**: Links semantically related exchanges
- **Eviction**: FIFO (First In, First Out) to MTM when full

#### Mid-Term Memory (MTM)
- **Capacity**: 200 segments
- **Storage**: Topic-based segments grouping related dialogue pages
- **Grouping**: Semantic similarity + keyword overlap (threshold 0.6)
- **Contains**: Summarized content + metadata per segment
- **Promotion criteria**: Heat-based scoring to LPM

#### Long-Term Persona Memory (LPM)
- **Capacity**: 100 entries per category
- **Categories**: Static profiles (name, role) + Dynamic knowledge (extracted facts) + Evolving traits (interests, preferences, behavioral patterns)
- **Persistence**: Across all sessions

### Four Functional Modules
1. **Storage**: Organizes information across tiers with fixed capacities
2. **Updating**: Manages tier transitions (FIFO for STM→MTM; heat scoring for MTM→LPM)
3. **Retrieval**: Two-stage for MTM (segment match → page ranking); all STM + top-10 LPM
4. **Generation**: Synthesizes all three tiers into coherent prompts

### Heat Score Formula
```
heat = f(visit_frequency, interaction_length, temporal_decay)
```

---

## 5. MemOS (MemTensor, 2025)

### Paper
"MemOS: A Memory OS for AI System" (arXiv:2507.03724)

### Core Concept
Treats memory as a manageable system resource. Unifies representation, scheduling, and evolution of multiple memory forms.

### Key Innovation: MemCube
- Encapsulates both memory content and metadata
- Metadata includes: provenance, versioning
- Can be composed, migrated, and fused over time

### Memory Forms Unified
- Plaintext memories
- Activation-based memories (KV cache states)
- Parameter-level memories (LoRA adapters, weight edits)

### Performance
- 159% improvement in temporal reasoning over OpenAI's global memory (LoCoMo benchmark)
- 38.97% overall accuracy gain
- 60.95% reduction in token overhead

---

## 6. SHIMI (Semantic Hierarchical Memory Index)

### Paper
"Decentralizing AI Memory: SHIMI, a Semantic Hierarchical Memory Index for Scalable Agent Reasoning" (Helmi, 2025, arXiv:2504.06135)

### Core Concept
Organizes memory as a rooted directed tree where each node represents a semantic concept, enabling meaning-based retrieval through hierarchical traversal rather than flat vector similarity.

### Architecture

#### Tree Structure
- Rooted directed tree T = (V, E)
- Each node v contains: semantic summary s(v), child nodes C(v), associated entities, parent pointer
- Parameters: T (branching factor), L (abstraction levels), δ (similarity threshold), γ (compression ratio)

#### Three Core Mechanisms
1. **Semantic Descent**: Top-down traversal using LLM-based relation classification (ancestor-descendant, equivalent, or unrelated)
2. **Sibling Matching/Merging**: When children exceed branching factor T, similar nodes merge under new parent via intermediate abstraction generation
3. **Abstraction Compression**: Enforces word count constraint: w_(i+1) <= γ * w_i (prevents overly vague categories)

#### Retrieval
- Top-down traversal: evaluates sim(q, s(v)) >= δ at each level
- Expands only semantically aligned branches
- Leaf nodes return associated entities
- Efficient pruning of irrelevant subtrees

### Decentralized Synchronization Protocol
Three complementary techniques:
1. **Merkle-DAG Divergence Detection**: Hash-based identification of differing subtrees
2. **Bloom Filter Filtering**: Compact summaries to infer missing nodes without full scans
3. **CRDT Conflict Resolution**: Merge function satisfying commutativity, idempotence, associativity

### Performance vs. RAG
| Metric | SHIMI | RAG Baseline |
|--------|-------|-------------|
| Top-1 Accuracy | 90% | 65% |
| Mean Precision@3 | 92.5% | 68.0% |
| Interpretability | 4.7/5 | 2.1/5 |
| Bandwidth (sync) | >90% savings | N/A |

### Key Differentiators
- Semantic abstraction hierarchy (vs. flat vector embeddings)
- Explainable retrieval paths (vs. opaque similarity scores)
- Natively decentralized (agents maintain local trees, sync asynchronously)
- Sublinear query scaling (vs. linear for flat vector search)

---

## Platform Comparison Matrix

| Feature | MemGPT/Letta | Mem0 | Zep | MemoryOS | MemOS | SHIMI |
|---------|-------------|------|-----|----------|-------|-------|
| **Primary metaphor** | OS virtual memory | Universal layer | Temporal KG | OS memory mgmt | System resource | Semantic tree |
| **Storage** | 4-tier context | Hybrid (vec+graph+KV) | Temporal KG | 3-tier hierarchical | MemCubes | Semantic tree |
| **Self-editing** | Yes (agent edits core) | No (automated) | No | No (automated) | Yes (composable) | No (tree ops) |
| **Temporal reasoning** | Basic | Basic | Strong | Heat-based | Strong | Implicit (levels) |
| **Multi-agent** | Yes (Letta) | Via scoping | Via scoping | No | Yes | Yes (decentralized) |
| **Open source** | Yes | Yes (+ paid) | Partially | Yes | Yes | Research |
| **Unique strength** | Agent-controlled memory | Production scale | Temporal facts | Persona tracking | Memory unification | Semantic hierarchy |

---

## Sources

- [MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560)
- [Agent Memory: How to Build Agents that Learn and Remember (Letta)](https://www.letta.com/blog/agent-memory)
- [Mem0: Building Production-Ready AI Agents (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413)
- [Mem0 Research](https://mem0.ai/research)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
- [MemOS: A Memory OS for AI System (arXiv:2507.03724)](https://arxiv.org/abs/2507.03724)
- [SHIMI: Decentralizing AI Memory (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- [MemGPT/Letta Documentation](https://docs.letta.com/concepts/memgpt/)
- [Rearchitecting Letta's Agent Loop (Letta Blog)](https://www.letta.com/blog/letta-v1-agent)
