---
resource_id: "37c79dbc-54ec-4535-a1cf-f8b7b0afeba9"
resource_type: "output"
resource_name: "29_open_source_memory_implementations"
---
# Open-Source AI Agent Memory Implementations

<!-- section_id: "35cbf824-e7ea-4558-b71b-6fbc4c6def7f" -->
## Purpose

This document surveys the most notable **open-source AI agent memory systems** with working code. Each project demonstrates different approaches to the memory architectures described in earlier documents (see `22_core_data_structure_hierarchy.md`, `23_core_ai_memory_systems.md`). Includes API patterns, architectural choices, and guidance on where to start.

---

<!-- section_id: "f3f2f673-a797-4efb-969e-a582577d1b6a" -->
## 1. Mem0 (mem0ai/mem0) — Most Popular and Production-Ready

<!-- section_id: "3fb325a0-17f4-4295-a194-ed0b6c7e7f78" -->
### Overview

The most widely adopted open-source memory framework for AI agents with 25k+ GitHub stars. Provides a clean `Memory` class API with automatic memory extraction, consolidation, and multi-backend support.

<!-- section_id: "fe91720b-3f87-4a7e-9dde-e1f57856d810" -->
### Key Features

- **Multi-level memory**: User, Session, and Agent scopes
- **Multi-backend vector storage**: Qdrant, PostgreSQL (pgvector), ChromaDB, and others
- **Automatic memory extraction**: LLM-powered extraction of facts from conversations
- **Full memory lifecycle**: Add, search, update, delete operations
- **Memory consolidation**: Deduplication and merging of related memories
- **Graph memory**: Neo4j integration for knowledge graph storage alongside vectors

<!-- section_id: "331a3f13-d882-40e4-acd0-31354bfd3aa5" -->
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

<!-- section_id: "6d1c59cb-8beb-410e-bd9f-ac7cf15cc665" -->
### Architecture Highlights

- Vector embeddings for semantic memory storage and retrieval
- LLM-in-the-loop for memory extraction (identifies facts worth remembering)
- Multi-backend abstraction layer (swap storage without changing application code)
- Memory consolidation pipeline: deduplication, merging, conflict resolution

<!-- section_id: "4d6e1215-6bb6-4776-b42e-c87b7accb088" -->
### What You Learn

- Production-grade memory API design patterns
- Multi-backend vector store abstraction
- LLM-assisted memory extraction and consolidation
- Scoped memory (per-user, per-session, per-agent)

**GitHub**: [github.com/mem0ai/mem0](https://github.com/mem0ai/mem0) | **Stars**: 25k+

---

<!-- section_id: "9d15b2dc-89cc-43d9-b502-4675794f09be" -->
## 2. Eion (eiondb/eion) — Knowledge Graph + Vector Hybrid

<!-- section_id: "280499a7-6591-4299-a5c9-57f3d6541c11" -->
### Overview

A hybrid memory system combining **PostgreSQL + pgvector** for semantic search with **Neo4j** for temporal knowledge graphs. Designed for multi-agent shared memory scenarios where relational reasoning matters alongside similarity search.

<!-- section_id: "1b2e5e90-1225-46a9-9be7-1d14e33ae2c7" -->
### Key Features

- **Dual backend**: PostgreSQL for vectors, Neo4j for knowledge graphs
- **Automatic knowledge extraction**: Extracts entities and relationships from conversations
- **Multi-agent shared memory**: Multiple agents can read/write to the same memory store
- **Temporal knowledge tracking**: Tracks when facts were learned and how they change over time
- **Hybrid queries**: Combines semantic similarity with graph traversal in a single query

<!-- section_id: "d2d53108-d594-41b8-a002-3fe7589bb922" -->
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

<!-- section_id: "58b1bfe4-ffb0-4fdb-a2df-978f2c5cb567" -->
### Architecture Highlights

- PostgreSQL stores embeddings via pgvector extension for similarity search
- Neo4j stores extracted entities and relationships as a property graph
- Hybrid query planner decides when to use vector search, graph traversal, or both
- Agent-scoped writes with shared reads for multi-agent coordination

<!-- section_id: "dd531802-da04-43fb-8e53-5b20d9ef2209" -->
### What You Learn

- Hybrid vector + graph architecture design
- Automatic knowledge extraction into graph databases
- Multi-agent memory sharing patterns
- Temporal knowledge tracking (fact versioning)

**GitHub**: [github.com/eiondb/eion](https://github.com/eiondb/eion)

---

<!-- section_id: "9b7bb221-36da-4cf5-b653-8a7f83eceeff" -->
## 3. LangChain Email Assistant — Semantic + Episodic + Procedural Memory

<!-- section_id: "8ffbf0a3-769e-4166-acd6-307dac90c307" -->
### Overview

A practical demonstration of **three memory types working together** in a single agent. Built on LangGraph for agent orchestration with Mem0 as the memory backend. Shows how semantic, episodic, and procedural memories serve different roles in the same application.

<!-- section_id: "b3cb6620-1f73-4129-bde0-a041e0c64cee" -->
### Key Features

- **Semantic memory**: User preferences and company policies (static facts)
- **Episodic memory**: Past email conversations (specific events)
- **Procedural memory**: User-defined workflows and email handling instructions (how-to knowledge)
- **Human-in-the-loop**: Agent learns from user corrections to improve procedural memory

<!-- section_id: "6ffe5a0f-db3e-43a1-aa34-06b3ef58b758" -->
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

<!-- section_id: "88a9234c-312b-46f0-aaf9-07dbe9eaa5f6" -->
### Architecture Highlights

- Each memory type has its own store with different access patterns
- LangGraph manages agent state transitions and tool calling
- Human-in-the-loop feedback updates procedural memory (agent learns new workflows)
- Episodic memories are time-ordered and windowed (last N interactions)

<!-- section_id: "32b1089e-5959-48bc-abad-7d9b77a6b8d1" -->
### What You Learn

- How to combine three memory types in one agent system
- LangGraph agent orchestration with memory integration
- Human-in-the-loop learning for procedural memory
- Practical memory type selection (which type for which data)

**GitHub**: [github.com/sushant1827/Long-Term-Memory-Agent](https://github.com/sushant1827/Long-Term-Memory-Agent)

---

<!-- section_id: "68ddae87-5f47-4e1d-b815-5daa5793f851" -->
## 4. MongoDB AI Memory Service — Cognitive Memory Dynamics

<!-- section_id: "c64682ad-045b-44fa-8923-980cfbc87b9b" -->
### Overview

A cognitively-inspired memory system built on **MongoDB Atlas** that models biological memory processes: importance scoring, temporal decay, reinforcement through repetition, and semantic merging. Goes beyond simple storage to simulate how human memory strengthens, fades, and consolidates.

<!-- section_id: "1ea1db9a-1ef4-4c7f-b2c2-07260832b7e2" -->
### Key Features

- **Memory importance scoring**: Each memory gets an importance weight (manual or auto-assessed)
- **Memory decay**: Unused memories fade over time (configurable decay factor)
- **Memory reinforcement**: Repeated or related concepts strengthen existing memories
- **Semantic merging**: Similar memories are automatically merged to reduce redundancy
- **Memory pruning**: Low-importance memories are removed to stay within capacity limits
- **MongoDB Atlas Vector Search**: Native vector similarity on MongoDB documents

<!-- section_id: "6c6fb52c-58c6-404b-a0a1-4c7af77a6b16" -->
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

<!-- section_id: "02638793-3ebc-4ca4-a922-16cc0b33d3cf" -->
### Architecture Highlights

- Each memory document includes: content, embedding, importance score, access count, last accessed timestamp, decay state
- Decay is applied as a multiplier on importance: `new_importance = importance * decay_factor ^ time_steps`
- Reinforcement increases importance when a new memory is similar to an existing one
- Merging combines two similar memories into one, averaging their embeddings and summing importance
- MongoDB Atlas vector search provides the similarity backbone

<!-- section_id: "ebb16dcb-4060-412f-9f41-1da0efb450b8" -->
### What You Learn

- Biologically-inspired memory dynamics (decay, reinforcement, consolidation)
- Importance-weighted memory management
- Memory consolidation strategies (merge vs. replace vs. keep both)
- MongoDB Atlas vector search integration

**GitHub**: [github.com/mongodb-partners/ai-memory](https://github.com/mongodb-partners/ai-memory)

---

<!-- section_id: "f197c67d-f567-4483-abcd-3fcc1f678672" -->
## 5. MemOS (MemTensor/MemOS) — Modular Memory Operating System

<!-- section_id: "c0076fb2-fa1d-4f40-908f-b253e44e13cf" -->
### Overview

A **Memory-Augmented Generation (MAG)** framework that treats memory as a modular operating system. Uses a "MemCube" abstraction where different memory types are pluggable modules with a unified API. Designed for researchers who want to experiment with different memory architectures.

<!-- section_id: "923aab3e-a1b2-4532-9326-2ef5238935cd" -->
### Key Features

- **MemCube architecture**: Each memory type is an independent, pluggable module
- **Unified API**: Same operations (store, retrieve, update, delete) across all memory types
- **Memory-Augmented Generation**: Retrieval is tightly integrated into the generation process
- **Pluggable backends**: Swap storage implementations without changing application code

<!-- section_id: "1ecfde68-60e8-48a3-a956-5e6ed9c468b4" -->
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

<!-- section_id: "002047ca-c4ec-4507-95d4-7b2f3aa663d6" -->
### Architecture Highlights

- Plugin architecture: Each memory type implements a standard interface
- MemCube abstraction decouples memory logic from storage backend
- Cross-module retrieval: A single query can draw from multiple memory types
- Designed for research experimentation (easy to swap components)

<!-- section_id: "8cba6489-d4ab-4c01-8ef7-4392f5fa8366" -->
### What You Learn

- Modular memory system design with plugin architecture
- Unified memory API patterns (one interface, many implementations)
- Memory-Augmented Generation (MAG) integration with LLMs
- How to design extensible memory frameworks

**GitHub**: [github.com/MemTensor/MemOS](https://github.com/MemTensor/MemOS)

---

<!-- section_id: "ace3c854-32be-41ab-a56d-e5235baece3e" -->
## 6. Hindsight (vectorize-io/hindsight) — Learning from Experience

<!-- section_id: "c50c5198-e9fe-49f9-ab85-92a3b97cacf2" -->
### Overview

A memory system focused on **agents that learn from experience**. Rather than just storing and retrieving memories, Hindsight enables agents to recognize patterns across past episodes and improve their behavior over time. Emphasizes the feedback loop between memory and action.

<!-- section_id: "feeea22d-9f90-4cb9-ba2a-903440f02bd3" -->
### Key Features

- **Experience-based learning loops**: Agent stores outcomes, reflects on patterns, adjusts behavior
- **Pattern recognition across episodes**: Identifies recurring situations and successful strategies
- **Self-improving retrieval**: Retrieval strategies adapt based on which memories proved useful
- **Adaptive behavior**: Agent learns which approaches work in which contexts

<!-- section_id: "fc19d8da-32b3-4e9d-b5a1-f2cecd167dc7" -->
### What You Learn

- Experience-based learning loop design
- Pattern extraction from interaction history
- Adaptive retrieval strategies (learn what to remember)
- Feedback-driven memory systems

**GitHub**: [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

---

<!-- section_id: "bfa15549-abd4-4413-a86b-d2d75d7a85b0" -->
## 7. Simple RAG with ChromaDB — Minimal Working Example

<!-- section_id: "e543180a-bcff-4f15-89e7-626a3ee6fd5f" -->
### Overview

A minimal implementation of **vector memory with ChromaDB** and a local LLM. The simplest possible working example of an agent with memory. Ideal for learning the fundamentals before moving to more complex systems.

<!-- section_id: "dcc0f57e-2290-4454-9513-66e805e26d69" -->
### Key Features

- **Basic vector memory**: ChromaDB for embedding storage and retrieval
- **Natural language memory operations**: Agent understands commands like "add this to memory"
- **Local LLM integration**: Works with Llama via llama_cpp (no API keys needed)
- **Internet search integration**: Can search the web and store results in memory

<!-- section_id: "15641047-22a3-466a-8a07-96d3214bf46f" -->
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

<!-- section_id: "0eaa564e-f8f5-4581-8f96-39d06058ed50" -->
### Architecture Highlights

- ChromaDB handles embedding generation, storage, and similarity search in one package
- No external API keys required (local embeddings + local LLM)
- Simple document-in, document-out interface
- Agent loop: receive input -> check memory -> generate response -> optionally store to memory

<!-- section_id: "338c3dec-25e5-4a9a-8648-e681d40c02fc" -->
### What You Learn

- Minimal RAG (Retrieval-Augmented Generation) implementation
- ChromaDB fundamentals (collections, add, query)
- Local LLM integration without cloud dependencies
- The basic memory-augmented agent loop

**GitHub**: [github.com/AkiRusProd/llm-agent](https://github.com/AkiRusProd/llm-agent)

---

<!-- section_id: "09c1d3eb-0ea3-41aa-ad4b-bf83f1ca64af" -->
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

<!-- section_id: "90205c49-7c3c-4cbe-a210-5c64bb6770a4" -->
## 9. Recommended Learning Path

<!-- section_id: "e3583202-04b5-48fa-b531-263072dcc46c" -->
### For Learning Fundamentals

1. **Start with Simple RAG** (ChromaDB example) — understand basic vector memory, the add/query loop, and how retrieval augments generation
2. **Move to Mem0** — see production-grade patterns: multi-backend support, LLM-assisted extraction, memory lifecycle management

<!-- section_id: "92a6724e-da58-412e-a452-1091ba1fbba9" -->
### For Real Projects

- **Mem0** if you want a managed service with flexibility and community support
- **Eion** if your application needs knowledge graph reasoning alongside vector search
- **MongoDB AI Memory** if you want biologically-inspired cognitive dynamics (decay, reinforcement)

<!-- section_id: "15f5391b-a282-45c9-a19e-2b7477f3f762" -->
### For Research and Experimentation

- **MemOS** for modular architecture research (swap memory types as plugins)
- **LangChain Email Agent** for studying how three memory types interact in practice
- **Hindsight** for experience-based learning and adaptive retrieval

---

<!-- section_id: "30030389-8595-4a81-9946-c67593195d4f" -->
## Cross-References

- **Data structures used by these systems**: `22_core_data_structure_hierarchy.md`, `28_supporting_data_structures_deep_dive.md`
- **Memory type taxonomy**: `21_core_memory_structure_hierarchy.md`
- **AI system tiers**: `23_core_ai_memory_systems.md`
- **Cognitive science foundations**: `01_cognitive_science_foundations.md`

---

<!-- section_id: "bf8f0999-9490-40ba-9e50-6aad8a60b5dd" -->
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
