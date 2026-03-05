---
resource_id: "a8d59194-b0b2-4af9-9f3d-3b836e545e91"
resource_type: "output"
resource_name: "02_memory_by_duration"
---
# Memory Types by Duration / Temporal Scope

<!-- section_id: "6aa55c96-220f-426e-923f-77174fac7b24" -->
## Overview

Memory systems categorized by how long information persists and the temporal role it plays in agent operation.

---

<!-- section_id: "5471280e-fcb1-4728-958a-bb7268e236f0" -->
## 1. Sensory Memory / Input Buffer

**Duration**: Milliseconds to seconds
**Capacity**: High bandwidth, minimal retention

<!-- section_id: "35269942-559b-4e79-94b2-c015dfbea7f9" -->
### What It Stores
- Raw, unprocessed sensory input (text tokens, image pixels, audio samples)
- Full fidelity representation before any filtering

<!-- section_id: "d51146bb-f0db-44b0-b75e-e29b8f58a3e7" -->
### How It Works
- Brief registration of all input before selective attention
- Information not attended to decays immediately
- Acts as a pre-processing buffer

<!-- section_id: "0e2ede2c-86da-436e-ad31-d65b78d5d72c" -->
### AI Implementations
- Token input buffers in transformer models
- Raw observation logs in embodied agents
- Unprocessed API response caches

<!-- section_id: "f878fb71-4416-47b3-8cda-c2830ef06cd1" -->
### Strengths / Weaknesses
- (+) Captures everything momentarily
- (-) No persistence, no organization, no retrieval

---

<!-- section_id: "1deab6cd-2761-4a81-9447-ac552ed21aa1" -->
## 2. Short-Term Memory (STM)

**Duration**: Seconds to minutes (within a single interaction turn)
**Capacity**: Limited (~context window size)

<!-- section_id: "6a53c0b8-a257-470f-a23a-1d5b21784bd1" -->
### What It Stores
- Current conversation context
- Immediate task-relevant information
- Recent observations and responses

<!-- section_id: "42489cae-083d-4b02-82e9-de3d547036e2" -->
### How It Works
- Information held in active processing (context window)
- Displaced by new information when capacity exceeded
- No explicit storage mechanism - just "what's currently visible"

<!-- section_id: "70ebb351-8f86-4639-b43a-19922cec41e5" -->
### AI Implementations
- **LLM Context Window**: The most direct STM analog; tokens currently in the prompt
- **MemGPT Message Buffer**: Most recent messages in active conversation
- **CrewAI Short-Term Memory**: Session-specific context via ChromaDB + RAG
- **MemoryOS STM**: Dialogue pages (7-page capacity) with contextual chains

<!-- section_id: "2c24c4f9-fa67-415f-b23f-d97cb1752f21" -->
### Retrieval
- Directly available (already in context)
- No retrieval needed - it IS the current state

<!-- section_id: "20ab97fd-67cd-4b79-83fb-57e8d6a882b7" -->
### Strengths / Weaknesses
- (+) Immediate access, full fidelity
- (-) Severely capacity-limited, lost after session/context reset

---

<!-- section_id: "65de4ac1-0e28-4a38-b096-e6ad9355d597" -->
## 3. Working Memory

**Duration**: Active task duration
**Capacity**: Limited but managed

<!-- section_id: "103e7bae-b2e1-4350-a8c0-7095c06bdf13" -->
### What It Stores
- Information actively being manipulated for current task
- Intermediate reasoning states
- Task plans and subgoals

<!-- section_id: "ee2f5cf1-8861-43ae-8824-736ae9cdeac9" -->
### Distinguished from STM
- Working memory implies active manipulation, not just passive holding
- Includes executive control functions (attention, updating, inhibition)

<!-- section_id: "6f9e1c07-6ec3-49e9-8db9-98da3fd230fc" -->
### AI Implementations
- **Scratchpad Memory**: Dedicated space for intermediate reasoning (chain-of-thought)
- **MemGPT Core Memory**: Editable blocks pinned to context window
- **SOAR Working Memory**: Central active representation, goal stack
- **ACT-R Buffers**: Limited-capacity interfaces between modules
- **Agent Planning State**: Current plan, active subgoals, partial results

<!-- section_id: "6081690a-6173-4a36-9b3b-aefef5bf0f3b" -->
### Key Research
- Attention mechanisms in transformers as working memory analogs
- KV cache as implicit working memory
- Papers: AgentFold, ACON, Sculptor (token-level working memory)

<!-- section_id: "839a307e-d839-40a6-9c76-98e43066ae40" -->
### Strengths / Weaknesses
- (+) Active manipulation, task-focused, always available
- (-) Capacity-limited, requires management strategy

---

<!-- section_id: "c5293c84-2887-4fe8-bfd6-800bae6b2106" -->
## 4. Mid-Term Memory (MTM)

**Duration**: Within a session or across recent sessions
**Capacity**: Moderate (larger than STM, smaller than LTM)

<!-- section_id: "a40c515c-3029-4dd6-bb1f-5a214197584a" -->
### What It Stores
- Topic clusters from recent conversations
- Summarized segments of interaction history
- Recently accessed knowledge

<!-- section_id: "2c8e16b3-aafe-4899-8068-7d00f7a3c955" -->
### How It Works
- Bridges gap between immediate context and permanent storage
- Groups related information into thematic segments
- Periodically consolidated into long-term memory

<!-- section_id: "df6b761c-1c70-4bd0-b696-04d71beb4d5d" -->
### AI Implementations
- **MemoryOS MTM**: Segmented paging architecture (200-segment capacity); groups related dialogue pages by topic using semantic similarity + keyword overlap (threshold 0.6)
- **Conversation Summary Buffer**: LangChain's ConversationSummaryBufferMemory - retains recent messages raw while summarizing older ones
- **Session-scoped caches**: Information relevant to current work session

<!-- section_id: "77fa51b1-1588-4330-aebe-3b0bb6ea0c44" -->
### Retrieval
- Two-stage: segment matching then page-level semantic ranking
- More structured than STM, less indexed than LTM

<!-- section_id: "09f17020-ed3f-42bf-b8e8-c6b125f41648" -->
### Strengths / Weaknesses
- (+) Balances recency and breadth, manageable size
- (-) Requires active management of what to promote/demote

---

<!-- section_id: "059df96e-1fe3-4e3b-899d-04e7950f82b4" -->
## 5. Long-Term Memory (LTM)

**Duration**: Persistent across sessions, potentially indefinite
**Capacity**: Theoretically unlimited (with appropriate storage)

<!-- section_id: "cea9a748-9c03-4015-8d2e-3a3d6deef10d" -->
### What It Stores
- Accumulated knowledge and facts (semantic)
- Historical interactions and experiences (episodic)
- Learned skills and procedures (procedural)
- User profiles and preferences (personalization)

<!-- section_id: "e347d5ad-0b4a-4012-a284-6b58b74627b7" -->
### How It Works
- External storage systems (databases, vector stores, knowledge graphs)
- Requires explicit retrieval mechanisms
- Consolidation from shorter-term memories
- May undergo decay/forgetting based on recency and importance

<!-- section_id: "654321f5-767a-4a59-adc6-a9a7ca74947a" -->
### AI Implementations
- **LangChain VectorStoreRetrieverMemory**: Conversation history as vector embeddings
- **CrewAI Long-Term Memory**: SQLite3 for task results across sessions
- **MemGPT Archival Memory**: Processed, indexed knowledge in external databases
- **MemoryOS LPM**: Persistent user/agent profiles (100 entries per category)
- **Mem0**: Hybrid datastore (graph + vector + KV) with active curation
- **Zep**: Temporal knowledge graph for long-term agent memory
- **Knowledge Graphs**: Structured relational storage for entity-relationship data

<!-- section_id: "83faf2e4-599f-4238-a74d-2a481d94142a" -->
### Retrieval Mechanisms
- Semantic similarity search (vector embeddings)
- Keyword/entity matching
- Temporal queries
- Graph traversal
- Hybrid scoring (recency + relevance + importance)

<!-- section_id: "b2a865b7-1814-49b6-a072-4021f7b0aff0" -->
### Strengths / Weaknesses
- (+) Persistent, scalable, enables learning over time
- (-) Retrieval latency, relevance challenges, storage costs, stale information

---

<!-- section_id: "f750fc80-858d-4a95-aa90-5035eb6e373e" -->
## 6. Recall Memory (Interaction Archive)

**Duration**: Indefinite
**Capacity**: Complete history

<!-- section_id: "0567f798-ae5a-490c-a5a2-59612f8b5aa7" -->
### What It Stores
- Complete raw interaction history
- Every message, query, and response
- Unprocessed conversation logs

<!-- section_id: "01fefe22-ef54-44f7-9e35-54d398794d4a" -->
### How It Works
- Automatic archival of all interactions
- Searchable when needed but not always in context
- Distinguished from archival memory by being raw (not processed/indexed)

<!-- section_id: "dd83df81-f1b9-4ebb-81f5-40502668e8a6" -->
### AI Implementations
- **MemGPT/Letta Recall Memory**: Complete searchable conversation history
- **Chat history databases**: Stored conversation threads
- **OpenAI Threads**: Complete conversation history per thread

<!-- section_id: "fb1b16ce-47b9-4b66-9234-5bf5a88b3f1e" -->
### Strengths / Weaknesses
- (+) Nothing is lost, full audit trail
- (-) Unprocessed, can be noisy, requires search to access

---

<!-- section_id: "82d6a375-e15e-4bfb-bd29-74735b9c4862" -->
## Duration Hierarchy Summary

```
Sensory (ms) → STM (seconds) → Working (task) → MTM (session) → LTM (permanent)
                                                                    ↑
                                                              Recall (archive)
```

Each tier feeds into the next through consolidation, with information becoming more abstracted and less detailed as it moves toward long-term storage.

---

<!-- section_id: "c9622b4c-049f-4071-a2f4-1f98603beadc" -->
## Sources

- [MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
- [Agent Memory: How to Build Agents that Learn and Remember (Letta)](https://www.letta.com/blog/agent-memory)
- [LangChain Conversational Memory (Aurelio AI)](https://www.aurelio.ai/learn/langchain-conversational-memory)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
