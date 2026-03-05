---
resource_id: "78a2c98d-19be-4a12-aafc-b9a27502bcdb"
resource_type: "output"
resource_name: "06_dedicated_memory_platforms"
---
# Dedicated Memory Platforms and Systems

<!-- section_id: "90e20d49-3252-4d84-af91-4889105e78fb" -->
## Overview

Purpose-built memory platforms that can be integrated into any AI agent system, providing memory as a service layer independent of the agent framework.

---

<!-- section_id: "75a5e108-eb39-4669-ace3-7da8d8f0c3df" -->
## 1. MemGPT / Letta

<!-- section_id: "0367b943-ba71-4b60-b906-d2278a389ff7" -->
### Paper
"MemGPT: Towards LLMs as Operating Systems" (Packer et al., 2023, arXiv:2310.08560)

<!-- section_id: "700d58b6-5a93-46bb-8014-eab665103ae4" -->
### Core Concept
Inspired by operating system virtual memory management: provides the illusion of unlimited memory while working within fixed context window limits. The LLM itself acts as the "OS" that manages memory, moving data in and out of context using designated tools.

<!-- section_id: "70b8ba4a-040b-4bb4-9081-bf0a14ac1774" -->
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

<!-- section_id: "b43745a8-d669-4751-bd55-c420a989950c" -->
### Key Innovation
- **Self-editing memory**: The agent reads and writes its own core memory blocks
- **Function-calling memory management**: Memory operations exposed as tools
- **Virtual context management**: Agent controls what's in context window

<!-- section_id: "0e3e00c9-f232-48cc-8d12-29c1396d9ea4" -->
### Letta Framework (2024+)
- Open-source agent framework building on MemGPT concepts
- Added: multi-agent support, tool builder, REST API
- Persistent agents with stateful memory across sessions
- Agent loop rearchitected drawing from ReAct, MemGPT, and Claude Code patterns

---

<!-- section_id: "ac174f8b-71eb-4125-95c5-521cc132488a" -->
## 2. Mem0

<!-- section_id: "c75a1cd5-70b6-4643-a72d-b2a439931f13" -->
### Paper
"Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory" (Chhikara et al., 2025, arXiv:2504.19413)

<!-- section_id: "e0c6b4b2-5d1b-45ae-a745-b23095875df6" -->
### Core Concept
A universal memory layer that sits between applications and LLMs. Automatically extracts, consolidates, and retrieves information from conversations.

<!-- section_id: "adc16d48-e494-4b13-b862-6c0291bb6b8b" -->
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

<!-- section_id: "c338824c-d1d6-4532-a816-e3e8bee94f72" -->
### Performance
- 26% improvement in LLM-as-a-Judge metric over OpenAI
- 91% lower p95 latency
- 90%+ token cost savings
- 1.44 second response latency (92% improvement)

<!-- section_id: "2adf36ca-c8b4-4f0a-b4e7-a2907f103b16" -->
### Integration
- Works with any LLM provider (OpenAI, Anthropic, Ollama, custom)
- CrewAI integration (as memory provider)
- AWS integration (ElastiCache + Neptune Analytics)
- $24M raised (October 2025)

---

<!-- section_id: "ed439fac-b2b5-403f-89c8-9471608d381c" -->
## 3. Zep

<!-- section_id: "1fcf1e27-b3b1-4975-bd31-c111df2ce0ae" -->
### Core Concept
Temporal knowledge graph architecture for AI agent memory. Focuses on temporal reasoning and enterprise use cases.

<!-- section_id: "19fe6a84-a6ea-498f-946f-53bc3457bb1a" -->
### Architecture
- **Temporal knowledge graph**: Entities and relationships with temporal metadata
- **Fact extraction**: Automatic extraction of facts from conversations
- **Temporal queries**: "What did the user say about X last week?"
- **User/session scoping**: Memory partitioned by user and session

<!-- section_id: "0318a4e6-35ef-4437-a0f2-5999ab6ab3bf" -->
### Performance
- Outperforms MemGPT on Deep Memory Retrieval benchmark
- Validated on LongMemEval benchmark (complex temporal reasoning)
- Focus on enterprise use cases requiring temporal reasoning

<!-- section_id: "db72a0c8-83ea-4f33-a822-97a76467fefb" -->
### Key Differentiator
- Temporal-first design (vs. Mem0's hybrid and MemGPT's OS-inspired approach)
- Knowledge graph as primary representation (not just vector similarity)

---

<!-- section_id: "21c61234-ae4e-4027-965c-052e29f576e2" -->
## 4. MemoryOS (EMNLP 2025 Oral)

<!-- section_id: "6d87148a-8a81-45c4-b096-cac8fa3efa38" -->
### Paper
"Memory OS of AI Agent" (Kang et al., 2025, arXiv:2506.06326)

<!-- section_id: "b47d9e5a-17da-4489-9a1b-d8790f5ee352" -->
### Core Concept
Inspired by OS memory management principles: hierarchical storage with automated promotion/demotion between levels.

<!-- section_id: "3c1c7d12-37f1-4f42-9a92-90c6f4e37a76" -->
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

<!-- section_id: "04f6136a-2d7a-469e-8afe-5d3b5f102fea" -->
### Four Functional Modules
1. **Storage**: Organizes information across tiers with fixed capacities
2. **Updating**: Manages tier transitions (FIFO for STM→MTM; heat scoring for MTM→LPM)
3. **Retrieval**: Two-stage for MTM (segment match → page ranking); all STM + top-10 LPM
4. **Generation**: Synthesizes all three tiers into coherent prompts

<!-- section_id: "53bdd828-6e0a-467d-bc3d-276586df1714" -->
### Heat Score Formula
```
heat = f(visit_frequency, interaction_length, temporal_decay)
```

---

<!-- section_id: "acf64da0-3610-440c-94a0-fa0d5829cbd7" -->
## 5. MemOS (MemTensor, 2025)

<!-- section_id: "d72b79a9-d540-4199-97d2-749be2db6250" -->
### Paper
"MemOS: A Memory OS for AI System" (arXiv:2507.03724)

<!-- section_id: "6030fc29-521d-4411-9621-df0f44c4eb26" -->
### Core Concept
Treats memory as a manageable system resource. Unifies representation, scheduling, and evolution of multiple memory forms.

<!-- section_id: "cc57943a-1d48-434d-8947-8c50049c8c98" -->
### Key Innovation: MemCube
- Encapsulates both memory content and metadata
- Metadata includes: provenance, versioning
- Can be composed, migrated, and fused over time

<!-- section_id: "f7a6fc1a-44fb-4c7a-80d5-4322a2923a77" -->
### Memory Forms Unified
- Plaintext memories
- Activation-based memories (KV cache states)
- Parameter-level memories (LoRA adapters, weight edits)

<!-- section_id: "20b1450f-d066-4a1d-a638-41f6f00ee35d" -->
### Performance
- 159% improvement in temporal reasoning over OpenAI's global memory (LoCoMo benchmark)
- 38.97% overall accuracy gain
- 60.95% reduction in token overhead

---

<!-- section_id: "27463f87-67df-4aa4-8937-caa6dbf85175" -->
## 6. SHIMI (Semantic Hierarchical Memory Index)

<!-- section_id: "fd0b1402-3050-4100-b8cb-28db760a46cd" -->
### Paper
"Decentralizing AI Memory: SHIMI, a Semantic Hierarchical Memory Index for Scalable Agent Reasoning" (Helmi, 2025, arXiv:2504.06135)

<!-- section_id: "d70594bf-c7b2-4d5e-863e-542d9db79792" -->
### Core Concept
Organizes memory as a rooted directed tree where each node represents a semantic concept, enabling meaning-based retrieval through hierarchical traversal rather than flat vector similarity.

<!-- section_id: "e749fd64-07cb-4613-987a-574bd332db55" -->
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

<!-- section_id: "3e73dd7a-a1de-4519-a2a8-cc6afc99b56c" -->
### Decentralized Synchronization Protocol
Three complementary techniques:
1. **Merkle-DAG Divergence Detection**: Hash-based identification of differing subtrees
2. **Bloom Filter Filtering**: Compact summaries to infer missing nodes without full scans
3. **CRDT Conflict Resolution**: Merge function satisfying commutativity, idempotence, associativity

<!-- section_id: "2349b2a7-75d5-4a6b-b0bf-69b24aeefa60" -->
### Performance vs. RAG
| Metric | SHIMI | RAG Baseline |
|--------|-------|-------------|
| Top-1 Accuracy | 90% | 65% |
| Mean Precision@3 | 92.5% | 68.0% |
| Interpretability | 4.7/5 | 2.1/5 |
| Bandwidth (sync) | >90% savings | N/A |

<!-- section_id: "09bbed4a-a394-4177-81ea-5fbf15e0bbdd" -->
### Key Differentiators
- Semantic abstraction hierarchy (vs. flat vector embeddings)
- Explainable retrieval paths (vs. opaque similarity scores)
- Natively decentralized (agents maintain local trees, sync asynchronously)
- Sublinear query scaling (vs. linear for flat vector search)

---

<!-- section_id: "6325ef52-0faf-4906-8733-53f10e42b97d" -->
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

<!-- section_id: "095cbf06-07ea-43be-bb05-8bbd011fdaa1" -->
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
