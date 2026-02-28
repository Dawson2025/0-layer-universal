# Open-Source AI Agent Memory Implementations

## Purpose

This document surveys the most notable **open-source AI agent memory systems** with working code. Each project demonstrates different approaches to the memory architectures described in earlier documents (see `22_core_data_structure_hierarchy.md`, `23_core_ai_memory_systems.md`). Includes API patterns, architectural choices, and guidance on where to start.

---

## 1. Mem0 (mem0ai/mem0) — Most Popular and Production-Ready

### Overview

The most widely adopted open-source memory framework for AI agents with 25k+ GitHub stars. Provides a clean `Memory` class API with automatic memory extraction, consolidation, and multi-backend support.

### Key Features

- **Multi-level memory**: User, Session, and Agent scopes
- **Multi-backend vector storage**: Qdrant, PostgreSQL (pgvector), ChromaDB, and others
- **Automatic memory extraction**: LLM-powered extraction of facts from conversations
- **Full memory lifecycle**: Add, search, update, delete operations
- **Memory consolidation**: Deduplication and merging of related memories
- **Graph memory**: Neo4j integration for knowledge graph storage alongside vectors

### API Pattern

```python
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "agent_memory",
            "host": "localhost",
            "port": 6333,
        }
    },
    "llm": {
        "provider": "openai",
        "config": {"model": "gpt-4"}
    }
}

memory = Memory.from_config(config)

# Add memories from conversation
messages = [
    {"role": "user", "content": "I'm allergic to peanuts"},
    {"role": "assistant", "content": "I'll remember that"}
]
memory.add(messages, user_id="user_123")

# Search memories by semantic similarity
results = memory.search("What are my allergies?", user_id="user_123")

# Get all memories for a user
all_memories = memory.get_all(user_id="user_123")
```

### Architecture Highlights

- Vector embeddings for semantic memory storage and retrieval
- LLM-in-the-loop for memory extraction (identifies facts worth remembering)
- Multi-backend abstraction layer (swap storage without changing application code)
- Memory consolidation pipeline: deduplication, merging, conflict resolution

### What You Learn

- Production-grade memory API design patterns
- Multi-backend vector store abstraction
- LLM-assisted memory extraction and consolidation
- Scoped memory (per-user, per-session, per-agent)

**GitHub**: [github.com/mem0ai/mem0](https://github.com/mem0ai/mem0) | **Stars**: 25k+

---

## 2. Eion (eiondb/eion) — Knowledge Graph + Vector Hybrid

### Overview

A hybrid memory system combining **PostgreSQL + pgvector** for semantic search with **Neo4j** for temporal knowledge graphs. Designed for multi-agent shared memory scenarios where relational reasoning matters alongside similarity search.

### Key Features

- **Dual backend**: PostgreSQL for vectors, Neo4j for knowledge graphs
- **Automatic knowledge extraction**: Extracts entities and relationships from conversations
- **Multi-agent shared memory**: Multiple agents can read/write to the same memory store
- **Temporal knowledge tracking**: Tracks when facts were learned and how they change over time
- **Hybrid queries**: Combines semantic similarity with graph traversal in a single query

### API Pattern

```python
from eiondb import Eion

# Initialize with both backends
eion = Eion(
    postgres_url="postgresql://localhost/eion",
    neo4j_url="bolt://localhost:7687"
)

# Add conversation — automatically extracts to both vector store and knowledge graph
eion.add_conversation(
    agent_id="agent_1",
    messages=[
        {"role": "user", "content": "John works at Google"},
        {"role": "assistant", "content": "Got it, stored"}
    ]
)

# Hybrid query: semantic search + graph traversal
results = eion.query(
    "Where does John work?",
    use_graph=True  # Enables knowledge graph reasoning
)
```

### Architecture Highlights

- PostgreSQL stores embeddings via pgvector extension for similarity search
- Neo4j stores extracted entities and relationships as a property graph
- Hybrid query planner decides when to use vector search, graph traversal, or both
- Agent-scoped writes with shared reads for multi-agent coordination

### What You Learn

- Hybrid vector + graph architecture design
- Automatic knowledge extraction into graph databases
- Multi-agent memory sharing patterns
- Temporal knowledge tracking (fact versioning)

**GitHub**: [github.com/eiondb/eion](https://github.com/eiondb/eion)

---

## 3. LangChain Email Assistant — Semantic + Episodic + Procedural Memory

### Overview

A practical demonstration of **three memory types working together** in a single agent. Built on LangGraph for agent orchestration with Mem0 as the memory backend. Shows how semantic, episodic, and procedural memories serve different roles in the same application.

### Key Features

- **Semantic memory**: User preferences and company policies (static facts)
- **Episodic memory**: Past email conversations (specific events)
- **Procedural memory**: User-defined workflows and email handling instructions (how-to knowledge)
- **Human-in-the-loop**: Agent learns from user corrections to improve procedural memory

### API Pattern

```python
from langgraph.prebuilt import create_react_agent
from mem0 import MemoryClient

# Three distinct memory stores
semantic_store = {}    # Static facts (preferences, policies)
episodic_store = []    # Past interactions (email history)
procedural_store = {}  # Workflows (how to handle emails)

def email_agent(state):
    user_id = state['user_id']

    # Retrieve semantic memory (preferences)
    preferences = semantic_store.get(user_id)

    # Retrieve episodic memory (recent past emails)
    past_emails = [e for e in episodic_store
                   if e['user_id'] == user_id][-5:]

    # Retrieve procedural memory (email handling workflow)
    workflow = procedural_store.get('email_handling')

    # Combine all memory types for context
    context = f"""
    User preferences: {preferences}
    Recent emails: {past_emails}
    Workflow: {workflow}
    """

    return agent.invoke(context + state['input'])
```

### Architecture Highlights

- Each memory type has its own store with different access patterns
- LangGraph manages agent state transitions and tool calling
- Human-in-the-loop feedback updates procedural memory (agent learns new workflows)
- Episodic memories are time-ordered and windowed (last N interactions)

### What You Learn

- How to combine three memory types in one agent system
- LangGraph agent orchestration with memory integration
- Human-in-the-loop learning for procedural memory
- Practical memory type selection (which type for which data)

**GitHub**: [github.com/sushant1827/Long-Term-Memory-Agent](https://github.com/sushant1827/Long-Term-Memory-Agent)

---

## 4. MongoDB AI Memory Service — Cognitive Memory Dynamics

### Overview

A cognitively-inspired memory system built on **MongoDB Atlas** that models biological memory processes: importance scoring, temporal decay, reinforcement through repetition, and semantic merging. Goes beyond simple storage to simulate how human memory strengthens, fades, and consolidates.

### Key Features

- **Memory importance scoring**: Each memory gets an importance weight (manual or auto-assessed)
- **Memory decay**: Unused memories fade over time (configurable decay factor)
- **Memory reinforcement**: Repeated or related concepts strengthen existing memories
- **Semantic merging**: Similar memories are automatically merged to reduce redundancy
- **Memory pruning**: Low-importance memories are removed to stay within capacity limits
- **MongoDB Atlas Vector Search**: Native vector similarity on MongoDB documents

### API Pattern

```python
# Cognitive memory parameters
config = {
    "MAX_DEPTH": 5,                  # Max memories per user
    "SIMILARITY_THRESHOLD": 0.7,     # Threshold for reinforcement
    "DECAY_FACTOR": 0.99,            # Fade rate per time step
    "REINFORCEMENT_FACTOR": 1.1      # Strengthen rate on re-encounter
}

# Store memory with importance
memory_service.add_memory(
    user_id="user_123",
    content="User prefers morning meetings",
    importance=0.8  # Auto-assessed or manually set
)

# Memories automatically decay over time
memory_service.apply_decay()

# Related memories get merged when similarity exceeds threshold
memory_service.merge_similar_memories(threshold=0.7)

# Low-importance memories are pruned
memory_service.prune(min_importance=0.1)
```

### Architecture Highlights

- Each memory document includes: content, embedding, importance score, access count, last accessed timestamp, decay state
- Decay is applied as a multiplier on importance: `new_importance = importance * decay_factor ^ time_steps`
- Reinforcement increases importance when a new memory is similar to an existing one
- Merging combines two similar memories into one, averaging their embeddings and summing importance
- MongoDB Atlas vector search provides the similarity backbone

### What You Learn

- Biologically-inspired memory dynamics (decay, reinforcement, consolidation)
- Importance-weighted memory management
- Memory consolidation strategies (merge vs. replace vs. keep both)
- MongoDB Atlas vector search integration

**GitHub**: [github.com/mongodb-partners/ai-memory](https://github.com/mongodb-partners/ai-memory)

---

## 5. MemOS (MemTensor/MemOS) — Modular Memory Operating System

### Overview

A **Memory-Augmented Generation (MAG)** framework that treats memory as a modular operating system. Uses a "MemCube" abstraction where different memory types are pluggable modules with a unified API. Designed for researchers who want to experiment with different memory architectures.

### Key Features

- **MemCube architecture**: Each memory type is an independent, pluggable module
- **Unified API**: Same operations (store, retrieve, update, delete) across all memory types
- **Memory-Augmented Generation**: Retrieval is tightly integrated into the generation process
- **Pluggable backends**: Swap storage implementations without changing application code

### API Pattern

```python
from memos import MemOS, MemCube

# Initialize the memory operating system
memos = MemOS()

# Add different memory modules as plugins
memos.add_module("semantic", SemanticMemory())
memos.add_module("episodic", EpisodicMemory())
memos.add_module("procedural", ProceduralMemory())

# Unified store API across all types
memos.store(
    content="User prefers Python",
    memory_type="semantic"
)

# Unified retrieve API — queries all modules
context = memos.retrieve(
    query="What languages does user like?",
    k=5  # Top-5 results across all memory types
)
```

### Architecture Highlights

- Plugin architecture: Each memory type implements a standard interface
- MemCube abstraction decouples memory logic from storage backend
- Cross-module retrieval: A single query can draw from multiple memory types
- Designed for research experimentation (easy to swap components)

### What You Learn

- Modular memory system design with plugin architecture
- Unified memory API patterns (one interface, many implementations)
- Memory-Augmented Generation (MAG) integration with LLMs
- How to design extensible memory frameworks

**GitHub**: [github.com/MemTensor/MemOS](https://github.com/MemTensor/MemOS)

---

## 6. Hindsight (vectorize-io/hindsight) — Learning from Experience

### Overview

A memory system focused on **agents that learn from experience**. Rather than just storing and retrieving memories, Hindsight enables agents to recognize patterns across past episodes and improve their behavior over time. Emphasizes the feedback loop between memory and action.

### Key Features

- **Experience-based learning loops**: Agent stores outcomes, reflects on patterns, adjusts behavior
- **Pattern recognition across episodes**: Identifies recurring situations and successful strategies
- **Self-improving retrieval**: Retrieval strategies adapt based on which memories proved useful
- **Adaptive behavior**: Agent learns which approaches work in which contexts

### What You Learn

- Experience-based learning loop design
- Pattern extraction from interaction history
- Adaptive retrieval strategies (learn what to remember)
- Feedback-driven memory systems

**GitHub**: [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

---

## 7. Simple RAG with ChromaDB — Minimal Working Example

### Overview

A minimal implementation of **vector memory with ChromaDB** and a local LLM. The simplest possible working example of an agent with memory. Ideal for learning the fundamentals before moving to more complex systems.

### Key Features

- **Basic vector memory**: ChromaDB for embedding storage and retrieval
- **Natural language memory operations**: Agent understands commands like "add this to memory"
- **Local LLM integration**: Works with Llama via llama_cpp (no API keys needed)
- **Internet search integration**: Can search the web and store results in memory

### API Pattern

```python
import chromadb
from llama_cpp import Llama

# Initialize vector database
client = chromadb.Client()
collection = client.create_collection("memory")

# Add to memory — ChromaDB handles embedding automatically
collection.add(
    documents=["The user name is Rustam Akimov"],
    ids=["mem_1"]
)

# Query memory — returns semantically similar results
results = collection.query(
    query_texts=["What is my name?"],
    n_results=1
)
# results: {"documents": [["The user name is Rustam Akimov"]]}
```

### Architecture Highlights

- ChromaDB handles embedding generation, storage, and similarity search in one package
- No external API keys required (local embeddings + local LLM)
- Simple document-in, document-out interface
- Agent loop: receive input -> check memory -> generate response -> optionally store to memory

### What You Learn

- Minimal RAG (Retrieval-Augmented Generation) implementation
- ChromaDB fundamentals (collections, add, query)
- Local LLM integration without cloud dependencies
- The basic memory-augmented agent loop

**GitHub**: [github.com/AkiRusProd/llm-agent](https://github.com/AkiRusProd/llm-agent)

---

## 8. Comparison Table

| System | Backend | Memory Types | Stars / Maturity | Key Innovation | Best For |
|--------|---------|-------------|-----------------|----------------|----------|
| **Mem0** | Qdrant, pgvector, Chroma, Neo4j | Semantic, Episodic, Graph | 25k+ / Production | Multi-backend abstraction, LLM extraction | Production apps, getting started |
| **Eion** | PostgreSQL + Neo4j | Semantic, Knowledge Graph | Emerging | Hybrid vector + graph queries | Multi-agent systems, relational reasoning |
| **LangChain Email** | Custom stores + Mem0 | Semantic, Episodic, Procedural | Example project | Three memory types in one agent | Learning multi-memory integration |
| **MongoDB AI** | MongoDB Atlas | Semantic (cognitive dynamics) | Example project | Decay, reinforcement, merging | Cognitive dynamics research |
| **MemOS** | Pluggable backends | Modular (all types) | Research | MemCube plugin architecture | Research, architecture experiments |
| **Hindsight** | Vectors | Episodic (learning) | Emerging | Learning from experience | Adaptive/self-improving agents |
| **Simple RAG** | ChromaDB | Basic vector | Example project | Minimal working example | Learning fundamentals, prototyping |

---

## 9. Recommended Learning Path

### For Learning Fundamentals

1. **Start with Simple RAG** (ChromaDB example) — understand basic vector memory, the add/query loop, and how retrieval augments generation
2. **Move to Mem0** — see production-grade patterns: multi-backend support, LLM-assisted extraction, memory lifecycle management

### For Real Projects

- **Mem0** if you want a managed service with flexibility and community support
- **Eion** if your application needs knowledge graph reasoning alongside vector search
- **MongoDB AI Memory** if you want biologically-inspired cognitive dynamics (decay, reinforcement)

### For Research and Experimentation

- **MemOS** for modular architecture research (swap memory types as plugins)
- **LangChain Email Agent** for studying how three memory types interact in practice
- **Hindsight** for experience-based learning and adaptive retrieval

---

## Cross-References

- **Data structures used by these systems**: `22_core_data_structure_hierarchy.md`, `28_supporting_data_structures_deep_dive.md`
- **Memory type taxonomy**: `21_core_memory_structure_hierarchy.md`
- **AI system tiers**: `23_core_ai_memory_systems.md`
- **Cognitive science foundations**: `01_cognitive_science_foundations.md`

---

## Sources

- [Mem0 GitHub Repository](https://github.com/mem0ai/mem0) — production memory framework (25k+ stars)
- [Mem0 Documentation](https://docs.mem0.ai/) — API reference and guides
- [Eion GitHub Repository](https://github.com/eiondb/eion) — hybrid vector + graph memory
- [Long-Term-Memory-Agent (LangChain Email)](https://github.com/sushant1827/Long-Term-Memory-Agent) — multi-memory-type agent
- [MongoDB AI Memory Service](https://github.com/mongodb-partners/ai-memory) — cognitive memory dynamics
- [MemOS GitHub Repository](https://github.com/MemTensor/MemOS) — modular memory OS
- [Hindsight GitHub Repository](https://github.com/vectorize-io/hindsight) — learning from experience
- [LLM Agent with ChromaDB](https://github.com/AkiRusProd/llm-agent) — minimal RAG example
- Perplexity AI research conversation (Feb 2026) — synthesis of open-source memory implementations
