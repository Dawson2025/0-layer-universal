---
resource_id: "a8d59194-b0b2-4af9-9f3d-3b836e545e91"
resource_type: "output"
resource_name: "02_memory_by_duration"
---
# Memory Types by Duration / Temporal Scope

## Overview

Memory systems categorized by how long information persists and the temporal role it plays in agent operation.

---

## 1. Sensory Memory / Input Buffer

**Duration**: Milliseconds to seconds
**Capacity**: High bandwidth, minimal retention

### What It Stores
- Raw, unprocessed sensory input (text tokens, image pixels, audio samples)
- Full fidelity representation before any filtering

### How It Works
- Brief registration of all input before selective attention
- Information not attended to decays immediately
- Acts as a pre-processing buffer

### AI Implementations
- Token input buffers in transformer models
- Raw observation logs in embodied agents
- Unprocessed API response caches

### Strengths / Weaknesses
- (+) Captures everything momentarily
- (-) No persistence, no organization, no retrieval

---

## 2. Short-Term Memory (STM)

**Duration**: Seconds to minutes (within a single interaction turn)
**Capacity**: Limited (~context window size)

### What It Stores
- Current conversation context
- Immediate task-relevant information
- Recent observations and responses

### How It Works
- Information held in active processing (context window)
- Displaced by new information when capacity exceeded
- No explicit storage mechanism - just "what's currently visible"

### AI Implementations
- **LLM Context Window**: The most direct STM analog; tokens currently in the prompt
- **MemGPT Message Buffer**: Most recent messages in active conversation
- **CrewAI Short-Term Memory**: Session-specific context via ChromaDB + RAG
- **MemoryOS STM**: Dialogue pages (7-page capacity) with contextual chains

### Retrieval
- Directly available (already in context)
- No retrieval needed - it IS the current state

### Strengths / Weaknesses
- (+) Immediate access, full fidelity
- (-) Severely capacity-limited, lost after session/context reset

---

## 3. Working Memory

**Duration**: Active task duration
**Capacity**: Limited but managed

### What It Stores
- Information actively being manipulated for current task
- Intermediate reasoning states
- Task plans and subgoals

### Distinguished from STM
- Working memory implies active manipulation, not just passive holding
- Includes executive control functions (attention, updating, inhibition)

### AI Implementations
- **Scratchpad Memory**: Dedicated space for intermediate reasoning (chain-of-thought)
- **MemGPT Core Memory**: Editable blocks pinned to context window
- **SOAR Working Memory**: Central active representation, goal stack
- **ACT-R Buffers**: Limited-capacity interfaces between modules
- **Agent Planning State**: Current plan, active subgoals, partial results

### Key Research
- Attention mechanisms in transformers as working memory analogs
- KV cache as implicit working memory
- Papers: AgentFold, ACON, Sculptor (token-level working memory)

### Strengths / Weaknesses
- (+) Active manipulation, task-focused, always available
- (-) Capacity-limited, requires management strategy

---

## 4. Mid-Term Memory (MTM)

**Duration**: Within a session or across recent sessions
**Capacity**: Moderate (larger than STM, smaller than LTM)

### What It Stores
- Topic clusters from recent conversations
- Summarized segments of interaction history
- Recently accessed knowledge

### How It Works
- Bridges gap between immediate context and permanent storage
- Groups related information into thematic segments
- Periodically consolidated into long-term memory

### AI Implementations
- **MemoryOS MTM**: Segmented paging architecture (200-segment capacity); groups related dialogue pages by topic using semantic similarity + keyword overlap (threshold 0.6)
- **Conversation Summary Buffer**: LangChain's ConversationSummaryBufferMemory - retains recent messages raw while summarizing older ones
- **Session-scoped caches**: Information relevant to current work session

### Retrieval
- Two-stage: segment matching then page-level semantic ranking
- More structured than STM, less indexed than LTM

### Strengths / Weaknesses
- (+) Balances recency and breadth, manageable size
- (-) Requires active management of what to promote/demote

---

## 5. Long-Term Memory (LTM)

**Duration**: Persistent across sessions, potentially indefinite
**Capacity**: Theoretically unlimited (with appropriate storage)

### What It Stores
- Accumulated knowledge and facts (semantic)
- Historical interactions and experiences (episodic)
- Learned skills and procedures (procedural)
- User profiles and preferences (personalization)

### How It Works
- External storage systems (databases, vector stores, knowledge graphs)
- Requires explicit retrieval mechanisms
- Consolidation from shorter-term memories
- May undergo decay/forgetting based on recency and importance

### AI Implementations
- **LangChain VectorStoreRetrieverMemory**: Conversation history as vector embeddings
- **CrewAI Long-Term Memory**: SQLite3 for task results across sessions
- **MemGPT Archival Memory**: Processed, indexed knowledge in external databases
- **MemoryOS LPM**: Persistent user/agent profiles (100 entries per category)
- **Mem0**: Hybrid datastore (graph + vector + KV) with active curation
- **Zep**: Temporal knowledge graph for long-term agent memory
- **Knowledge Graphs**: Structured relational storage for entity-relationship data

### Retrieval Mechanisms
- Semantic similarity search (vector embeddings)
- Keyword/entity matching
- Temporal queries
- Graph traversal
- Hybrid scoring (recency + relevance + importance)

### Strengths / Weaknesses
- (+) Persistent, scalable, enables learning over time
- (-) Retrieval latency, relevance challenges, storage costs, stale information

---

## 6. Recall Memory (Interaction Archive)

**Duration**: Indefinite
**Capacity**: Complete history

### What It Stores
- Complete raw interaction history
- Every message, query, and response
- Unprocessed conversation logs

### How It Works
- Automatic archival of all interactions
- Searchable when needed but not always in context
- Distinguished from archival memory by being raw (not processed/indexed)

### AI Implementations
- **MemGPT/Letta Recall Memory**: Complete searchable conversation history
- **Chat history databases**: Stored conversation threads
- **OpenAI Threads**: Complete conversation history per thread

### Strengths / Weaknesses
- (+) Nothing is lost, full audit trail
- (-) Unprocessed, can be noisy, requires search to access

---

## Duration Hierarchy Summary

```
Sensory (ms) → STM (seconds) → Working (task) → MTM (session) → LTM (permanent)
                                                                    ↑
                                                              Recall (archive)
```

Each tier feeds into the next through consolidation, with information becoming more abstracted and less detailed as it moves toward long-term storage.

---

## Sources

- [MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
- [Agent Memory: How to Build Agents that Learn and Remember (Letta)](https://www.letta.com/blog/agent-memory)
- [LangChain Conversational Memory (Aurelio AI)](https://www.aurelio.ai/learn/langchain-conversational-memory)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
