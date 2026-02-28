# Memory Implementations in AI Agent Frameworks

## Overview

How major open-source AI agent frameworks implement memory systems, their architectures, storage backends, and trade-offs.

---

## 1. LangChain Memory Types

LangChain provides the most granular set of named memory implementations. Note: many are now legacy (pre-LangGraph) but remain widely referenced.

### ConversationBufferMemory
- **What it stores**: Complete verbatim conversation history
- **How it works**: Appends every human/AI message to a growing buffer
- **Storage**: In-memory list
- **Retrieval**: Returns full history as context
- **Strengths**: Full fidelity, simplest implementation
- **Weaknesses**: Token overflow in long conversations; O(n) growth
- **Best for**: Short conversations where complete context matters

### ConversationBufferWindowMemory
- **What it stores**: Last K conversation turns
- **How it works**: Sliding window of recent messages
- **Storage**: In-memory list with max length
- **Retrieval**: Returns last K turns
- **Strengths**: Bounded token usage
- **Weaknesses**: Loses all context beyond window; abrupt cutoff

### ConversationSummaryMemory
- **What it stores**: LLM-generated summary of conversation history
- **How it works**: After each exchange, LLM updates running summary
- **Storage**: Single summary string (updated in-place)
- **Retrieval**: Returns current summary
- **Strengths**: Constant-ish token usage; retains gist of long conversations
- **Weaknesses**: Summarization cost (LLM call per turn); detail loss; summarization errors

### ConversationSummaryBufferMemory
- **What it stores**: Recent messages verbatim + summary of older messages
- **How it works**: Keeps recent messages raw until token limit; summarizes overflow
- **Storage**: Buffer of recent messages + running summary
- **Retrieval**: Returns summary + recent raw messages
- **Strengths**: Best of both worlds - recent detail + long-term gist
- **Weaknesses**: Complexity; summarization overhead; token limit tuning

### ConversationTokenBufferMemory
- **What it stores**: Recent conversation messages up to a token limit
- **How it works**: Keeps adding messages until max tokens; drops oldest
- **Storage**: In-memory buffer with token counting
- **Retrieval**: Returns messages fitting within token budget

### VectorStoreRetrieverMemory
- **What it stores**: Conversation history as vector embeddings
- **How it works**: Each message embedded and stored in vector DB; retrieval via semantic similarity
- **Storage**: External vector store (Pinecone, ChromaDB, Weaviate, FAISS)
- **Retrieval**: Top-K most semantically similar past messages to current query
- **Strengths**: Scales to huge histories; retrieves only relevant context
- **Weaknesses**: Embedding quality dependency; may miss temporally important context

### ConversationEntityMemory
- **What it stores**: Per-entity summaries extracted from conversation
- **How it works**: LLM extracts named entities; maintains evolving summary per entity
- **Storage**: Entity store (in-memory, Redis, or SQLite)
- **Retrieval**: Returns entity summaries relevant to current input
- **Strengths**: Structured knowledge about key entities; grows intelligently
- **Weaknesses**: Entity extraction cost; may miss entities; summaries can diverge from reality

### ConversationKGMemory (Knowledge Graph)
- **What it stores**: Knowledge graph triples extracted from conversation
- **How it works**: LLM extracts (subject, predicate, object) triples; builds graph
- **Storage**: NetworkX graph (in-memory) or external graph DB
- **Retrieval**: Graph traversal from entities mentioned in current input
- **Strengths**: Structured relational knowledge; enables multi-hop reasoning
- **Weaknesses**: Extraction quality; graph management complexity

---

## 2. LangGraph Memory (State-Based)

LangGraph replaced many LangChain memory types with a unified state-based approach.

### Architecture
- **State graph**: Conversation state tracked as nodes/edges in a computational graph
- **Checkpointing**: State persisted at each node for resumption
- **Memory store**: Key-value store for cross-thread information

### Key Features
- Thread-level memory: each conversation thread maintains its own state
- Cross-thread memory: shared state accessible across threads
- Persistence backends: SQLite, PostgreSQL, custom
- Human-in-the-loop: state can be inspected/modified between steps

---

## 3. CrewAI Memory System

### Current Architecture (Unified Memory)
CrewAI replaced separate memory types with a single `Memory` class:

- **Storage**: LanceDB (default), configurable via `StorageBackend` protocol
- **Location**: `./.crewai/memory` or `CREWAI_STORAGE_DIR`
- **Analysis**: LLM analyzes content on save (infers scope, categories, importance)
- **Retrieval**: Composite scoring blending semantic similarity + recency + importance
- **Organization**: Hierarchical tree of scopes (filesystem-like)
- **Consolidation**: Threshold of 0.85 prevents duplicates
- **Deduplication**: Batch threshold of 0.98

### Tuning Parameters
| Parameter | Default | Purpose |
|-----------|---------|---------|
| `recency_weight` | configurable | Weight for recency in scoring |
| `semantic_weight` | configurable | Weight for semantic similarity |
| `importance_weight` | configurable | Weight for importance |
| `recency_half_life_days` | 30 | Decay rate for recency |
| `consolidation_threshold` | 0.85 | Duplicate prevention |
| `query_analysis_threshold` | 200 chars | Min query length for LLM analysis |

### Legacy Architecture (Pre-Unification)
Previously had four separate types:
- **Short-Term**: ChromaDB + RAG for session context
- **Long-Term**: SQLite3 for cross-session task results
- **Entity**: RAG-based entity tracking
- **Contextual**: Combined synthesis of other types

### Provider Integration
- Short-term and entity memory support Mem0 OSS and Mem0 Client as providers
- Qdrant integration available for vector storage

---

## 4. AutoGPT Memory

### Architecture
- **Vector-based long-term memory**: Stores observations and learnings as embeddings
- **File-based persistence**: Workspace files as durable memory
- **Self-prompting loop**: Continuous think → plan → act → observe cycle
- **Memory retrieval**: Semantic search over past observations

### Key Features
- Pioneered autonomous agent memory (2023)
- Self-directed memory management (agent decides what to remember)
- File system as persistent memory store

---

## 5. Microsoft AutoGen Memory

### Architecture
- **Conversation-based**: Maintains dialogue history for multi-turn interactions
- **Teachability**: Agents can learn from user instructions and remember across sessions
- **Shared context**: Multi-agent conversations with shared message history

### Memory Types
- Chat history per conversation
- Teachable agent memory (persistent user instructions)
- Group chat memory (shared across agents in a conversation)

---

## 6. OpenAI Swarm
- **Stateless design**: No built-in memory features
- **Context passing**: State carried via function parameters
- **External memory**: Must be implemented by developer

---

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

## Sources

- [LangChain Conversational Memory (Aurelio AI)](https://www.aurelio.ai/learn/langchain-conversational-memory)
- [Conversational Memory for LLMs with LangChain (Pinecone)](https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/)
- [LangChain Memory Types (ProjectPro)](https://www.projectpro.io/article/langchain-memory/1161)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
- [Deep Dive into CrewAI Memory Systems (SparkCo)](https://sparkco.ai/blog/deep-dive-into-crewai-memory-systems)
- [CrewAI vs LangGraph vs AutoGen (DataCamp)](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)
- [Comparing Multi-Agent AI Frameworks (Concision AI)](https://www.concision.ai/blog/comparing-multi-agent-ai-frameworks-crewai-langgraph-autogpt-autogen)
