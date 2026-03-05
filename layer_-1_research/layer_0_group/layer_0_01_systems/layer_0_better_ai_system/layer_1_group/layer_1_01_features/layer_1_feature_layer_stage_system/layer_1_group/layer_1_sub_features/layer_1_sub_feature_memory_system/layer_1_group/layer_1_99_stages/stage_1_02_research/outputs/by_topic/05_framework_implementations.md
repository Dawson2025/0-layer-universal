---
resource_id: "bea93f0a-f564-4e25-9e35-75fb6f7aa89a"
resource_type: "output"
resource_name: "05_framework_implementations"
---
# Memory Implementations in AI Agent Frameworks

<!-- section_id: "cb5819bc-4f79-4013-a94c-7270f1f08116" -->
## Overview

How major open-source AI agent frameworks implement memory systems, their architectures, storage backends, and trade-offs.

---

<!-- section_id: "fd449058-6220-42c5-9e13-2f53071f9344" -->
## 1. LangChain Memory Types

LangChain provides the most granular set of named memory implementations. Note: many are now legacy (pre-LangGraph) but remain widely referenced.

<!-- section_id: "301d1cfa-8eb7-4ebe-836d-e74ff78260b3" -->
### ConversationBufferMemory
- **What it stores**: Complete verbatim conversation history
- **How it works**: Appends every human/AI message to a growing buffer
- **Storage**: In-memory list
- **Retrieval**: Returns full history as context
- **Strengths**: Full fidelity, simplest implementation
- **Weaknesses**: Token overflow in long conversations; O(n) growth
- **Best for**: Short conversations where complete context matters

<!-- section_id: "1ea3b26d-f7c6-44ff-aa30-2d838e1800c2" -->
### ConversationBufferWindowMemory
- **What it stores**: Last K conversation turns
- **How it works**: Sliding window of recent messages
- **Storage**: In-memory list with max length
- **Retrieval**: Returns last K turns
- **Strengths**: Bounded token usage
- **Weaknesses**: Loses all context beyond window; abrupt cutoff

<!-- section_id: "213659bf-5798-4e78-aae2-c5758713e409" -->
### ConversationSummaryMemory
- **What it stores**: LLM-generated summary of conversation history
- **How it works**: After each exchange, LLM updates running summary
- **Storage**: Single summary string (updated in-place)
- **Retrieval**: Returns current summary
- **Strengths**: Constant-ish token usage; retains gist of long conversations
- **Weaknesses**: Summarization cost (LLM call per turn); detail loss; summarization errors

<!-- section_id: "4c899cd9-1af9-47b6-a1c2-878057a5af7b" -->
### ConversationSummaryBufferMemory
- **What it stores**: Recent messages verbatim + summary of older messages
- **How it works**: Keeps recent messages raw until token limit; summarizes overflow
- **Storage**: Buffer of recent messages + running summary
- **Retrieval**: Returns summary + recent raw messages
- **Strengths**: Best of both worlds - recent detail + long-term gist
- **Weaknesses**: Complexity; summarization overhead; token limit tuning

<!-- section_id: "57e409b7-28e7-4811-8c3b-38d642351586" -->
### ConversationTokenBufferMemory
- **What it stores**: Recent conversation messages up to a token limit
- **How it works**: Keeps adding messages until max tokens; drops oldest
- **Storage**: In-memory buffer with token counting
- **Retrieval**: Returns messages fitting within token budget

<!-- section_id: "8945a651-93d0-4127-8402-da96afe76bd6" -->
### VectorStoreRetrieverMemory
- **What it stores**: Conversation history as vector embeddings
- **How it works**: Each message embedded and stored in vector DB; retrieval via semantic similarity
- **Storage**: External vector store (Pinecone, ChromaDB, Weaviate, FAISS)
- **Retrieval**: Top-K most semantically similar past messages to current query
- **Strengths**: Scales to huge histories; retrieves only relevant context
- **Weaknesses**: Embedding quality dependency; may miss temporally important context

<!-- section_id: "fa288511-9bdb-4929-8ac5-919751eb226e" -->
### ConversationEntityMemory
- **What it stores**: Per-entity summaries extracted from conversation
- **How it works**: LLM extracts named entities; maintains evolving summary per entity
- **Storage**: Entity store (in-memory, Redis, or SQLite)
- **Retrieval**: Returns entity summaries relevant to current input
- **Strengths**: Structured knowledge about key entities; grows intelligently
- **Weaknesses**: Entity extraction cost; may miss entities; summaries can diverge from reality

<!-- section_id: "341731a2-78af-42db-a9c3-28a26cf6d95e" -->
### ConversationKGMemory (Knowledge Graph)
- **What it stores**: Knowledge graph triples extracted from conversation
- **How it works**: LLM extracts (subject, predicate, object) triples; builds graph
- **Storage**: NetworkX graph (in-memory) or external graph DB
- **Retrieval**: Graph traversal from entities mentioned in current input
- **Strengths**: Structured relational knowledge; enables multi-hop reasoning
- **Weaknesses**: Extraction quality; graph management complexity

---

<!-- section_id: "5c7ff82b-6964-45b0-a621-5544e6a0bd4b" -->
## 2. LangGraph Memory (State-Based)

LangGraph replaced many LangChain memory types with a unified state-based approach.

<!-- section_id: "c124ac87-151c-4e38-bf01-97f78518b540" -->
### Architecture
- **State graph**: Conversation state tracked as nodes/edges in a computational graph
- **Checkpointing**: State persisted at each node for resumption
- **Memory store**: Key-value store for cross-thread information

<!-- section_id: "b5650b41-6dff-41d2-a75c-da9ba75537b9" -->
### Key Features
- Thread-level memory: each conversation thread maintains its own state
- Cross-thread memory: shared state accessible across threads
- Persistence backends: SQLite, PostgreSQL, custom
- Human-in-the-loop: state can be inspected/modified between steps

---

<!-- section_id: "94d98b40-e9a1-4a33-b1fa-bed4a6875056" -->
## 3. CrewAI Memory System

<!-- section_id: "a8dd2ffe-920b-4400-a8c1-2ef0c2b2f84a" -->
### Current Architecture (Unified Memory)
CrewAI replaced separate memory types with a single `Memory` class:

- **Storage**: LanceDB (default), configurable via `StorageBackend` protocol
- **Location**: `./.crewai/memory` or `CREWAI_STORAGE_DIR`
- **Analysis**: LLM analyzes content on save (infers scope, categories, importance)
- **Retrieval**: Composite scoring blending semantic similarity + recency + importance
- **Organization**: Hierarchical tree of scopes (filesystem-like)
- **Consolidation**: Threshold of 0.85 prevents duplicates
- **Deduplication**: Batch threshold of 0.98

<!-- section_id: "a9c423a5-cc36-4b65-b6fa-048d6d247cc8" -->
### Tuning Parameters
| Parameter | Default | Purpose |
|-----------|---------|---------|
| `recency_weight` | configurable | Weight for recency in scoring |
| `semantic_weight` | configurable | Weight for semantic similarity |
| `importance_weight` | configurable | Weight for importance |
| `recency_half_life_days` | 30 | Decay rate for recency |
| `consolidation_threshold` | 0.85 | Duplicate prevention |
| `query_analysis_threshold` | 200 chars | Min query length for LLM analysis |

<!-- section_id: "81e4b87d-fdf1-40ba-92f5-e4b2c000dd0d" -->
### Legacy Architecture (Pre-Unification)
Previously had four separate types:
- **Short-Term**: ChromaDB + RAG for session context
- **Long-Term**: SQLite3 for cross-session task results
- **Entity**: RAG-based entity tracking
- **Contextual**: Combined synthesis of other types

<!-- section_id: "45849ce1-140e-4626-9c2c-48b12e58f9ab" -->
### Provider Integration
- Short-term and entity memory support Mem0 OSS and Mem0 Client as providers
- Qdrant integration available for vector storage

---

<!-- section_id: "c2cdf926-4c2a-4d2d-abd3-11b4b9807c1b" -->
## 4. AutoGPT Memory

<!-- section_id: "039c8922-614b-4660-b860-e70d10d8a5e5" -->
### Architecture
- **Vector-based long-term memory**: Stores observations and learnings as embeddings
- **File-based persistence**: Workspace files as durable memory
- **Self-prompting loop**: Continuous think → plan → act → observe cycle
- **Memory retrieval**: Semantic search over past observations

<!-- section_id: "1517f02b-ecd9-44f5-a216-8f6e640e27c5" -->
### Key Features
- Pioneered autonomous agent memory (2023)
- Self-directed memory management (agent decides what to remember)
- File system as persistent memory store

---

<!-- section_id: "822167a2-fa15-4ca4-a7ca-5935305d2787" -->
## 5. Microsoft AutoGen Memory

<!-- section_id: "a5e101a9-e1fe-4f4e-86bc-854141c51e9f" -->
### Architecture
- **Conversation-based**: Maintains dialogue history for multi-turn interactions
- **Teachability**: Agents can learn from user instructions and remember across sessions
- **Shared context**: Multi-agent conversations with shared message history

<!-- section_id: "ea60ce88-3613-41eb-93fb-7eb2003203ee" -->
### Memory Types
- Chat history per conversation
- Teachable agent memory (persistent user instructions)
- Group chat memory (shared across agents in a conversation)

---

<!-- section_id: "a2389442-4a14-4dff-857f-57d8e476d2cb" -->
## 6. OpenAI Swarm
- **Stateless design**: No built-in memory features
- **Context passing**: State carried via function parameters
- **External memory**: Must be implemented by developer

---

<!-- section_id: "3b15682d-bd7f-47e6-a782-c030c716db92" -->
## Framework Comparison Matrix

| Feature | LangChain | LangGraph | CrewAI | AutoGPT | AutoGen |
|---------|-----------|-----------|--------|---------|---------|
| Memory types | 8+ named types | State-based | Unified | Vector + file | Chat + teachable |
| Persistence | Varies by type | Checkpointing | LanceDB | File system | Session-based |
| Retrieval | Type-dependent | State access | Composite scoring | Semantic search | Chat history |
| Multi-agent | No | Yes | Yes | No | Yes |
| Customization | High (swappable stores) | Medium | Medium | Low | Medium |
| Learning | Entity/KG memory | Cross-thread state | Importance scoring | Self-directed | Teachable agents |
| Maturity | Most mature | Newer, replacing LC | Rapidly evolving | Pioneering but basic | Enterprise-focused |

---

<!-- section_id: "f4c48ec5-84e2-4e0f-b6f4-e8c13f3843b2" -->
## Sources

- [LangChain Conversational Memory (Aurelio AI)](https://www.aurelio.ai/learn/langchain-conversational-memory)
- [Conversational Memory for LLMs with LangChain (Pinecone)](https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/)
- [LangChain Memory Types (ProjectPro)](https://www.projectpro.io/article/langchain-memory/1161)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
- [Deep Dive into CrewAI Memory Systems (SparkCo)](https://sparkco.ai/blog/deep-dive-into-crewai-memory-systems)
- [CrewAI vs LangGraph vs AutoGen (DataCamp)](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)
- [Comparing Multi-Agent AI Frameworks (Concision AI)](https://www.concision.ai/blog/comparing-multi-agent-ai-frameworks-crewai-langgraph-autogpt-autogen)
