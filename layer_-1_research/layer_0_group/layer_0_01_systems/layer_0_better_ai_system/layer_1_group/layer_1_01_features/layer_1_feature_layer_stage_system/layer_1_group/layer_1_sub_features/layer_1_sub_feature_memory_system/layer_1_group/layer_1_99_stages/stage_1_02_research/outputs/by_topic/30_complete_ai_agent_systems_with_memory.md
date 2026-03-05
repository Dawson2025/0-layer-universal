---
resource_id: "e5e986be-a9eb-40e8-bf04-5b1bdd2f6ab0"
resource_type: "output"
resource_name: "30_complete_ai_agent_systems_with_memory"
---
# Complete AI Agent Systems with Memory

<!-- section_id: "a8b9f85a-9e3f-499a-9b24-c736e6ff4d98" -->
## Purpose

This document surveys **production-grade and open-source AI agent systems** that demonstrate full memory implementations (semantic, episodic, procedural) in working code. Unlike library documentation (see `07_memory_in_langchain_llamaindex.md`) or architecture patterns (see `23_core_ai_memory_systems.md`), these are complete, runnable systems that show how memory concepts compose into real applications.

---

<!-- section_id: "2bfd2065-d301-4484-ba7a-e3ab266f1640" -->
## 1. OASIS - Operational AI System for Incident Solutions (AWS)

<!-- section_id: "2457db45-da7f-453b-8dff-5b680d1a1f5b" -->
### Overview

OASIS is a production-grade IT incident management system built by AWS. It uses a multi-agent architecture with full memory across all three classical types.

<!-- section_id: "078f39de-9b74-4e47-9dec-a9e530b30ae5" -->
### Memory Architecture

| Memory Type | Implementation | What It Stores |
|-------------|----------------|----------------|
| Episodic | OpenSearch `app-logs-logs` index | Raw event logs, incident history, status transitions |
| Semantic | OpenSearch `app-logs-agent-findings` index | Incident patterns, knowledge base, cross-service correlations |
| Procedural | Automated remediation procedures | Deployment fixes, rollback sequences, approval workflows |
| Time-series | OpenSearch `app-logs-metrics` index | System metrics for anomaly detection |

<!-- section_id: "75ec1eab-89a7-4981-a9a3-ad5e6a9638c3" -->
### Status Transition Flow (Episodic Memory)

```
initial_detection -> analysis_complete -> pending_approval -> approved -> mitigated
```

Each transition is stored as an episodic record, creating a complete audit trail.

<!-- section_id: "df78e6f1-eb81-409e-81ef-5741bcd63ddf" -->
### Key Capabilities

- Real-time anomaly detection from streaming logs
- Cross-service event correlation (semantic relationships)
- Learning from past incidents to improve future remediation (procedural)
- Human-in-the-loop approval workflows for critical actions
- Email notifications with full incident context

<!-- section_id: "6af2866c-c586-4331-82eb-d2ceaaabf2bc" -->
### Technology Stack

LangGraph (orchestration), Amazon Bedrock (LLM), OpenSearch (memory store), AWS Lambda (compute), SES (notifications)

---

<!-- section_id: "ed94eee5-fb86-44c5-9a04-7460cdec2a50" -->
## 2. GenAI_Agents Repository - Multi-Agent Systems Collection

The GenAI_Agents repository by Nir Diamant contains 45+ complete agent implementations. Four stand out for their memory architectures:

<!-- section_id: "194a45c3-8615-4664-aede-cd88528483f7" -->
### 2.1 ATLAS - Academic Task and Learning Agent System

A four-agent educational system with comprehensive memory:

| Agent | Role | Memory Used |
|-------|------|-------------|
| Coordinator | Routes queries based on student understanding | Semantic (student profiles, course knowledge) |
| Planner | Creates personalized study schedules | Episodic (past assignments, performance history) |
| Notewriter | Generates notes matching learning style | Semantic (learning style preferences) |
| Advisor | Provides guidance on study strategies | Procedural (study strategies, time management patterns) |

ATLAS demonstrates how multiple agents can share memory stores while each specializing in different memory types for their particular function.

<!-- section_id: "47d1e80a-f632-486d-8c45-838f86effd9d" -->
### 2.2 Memory-Enhanced Email Agent

Implements all three classical memory types using LangMem:

| Memory Type | Backend | Content |
|-------------|---------|---------|
| Semantic | `InMemoryStore` | Facts about contacts, company policies |
| Episodic | `PostgresStore` | Email thread history, conversation context |
| Procedural | Dictionary | Response templates, workflow patterns, user preferences |

The agent uses `create_manage_memory_tool` and `create_search_memory_tool` from LangMem to give the LLM direct control over memory operations.

<!-- section_id: "1913be51-1ffd-454e-95cc-f55d0cd1d627" -->
### 2.3 DataScribe - Database Explorer Agent

Uses a knowledge graph approach to memory:

- **Semantic memory**: NetworkX graph storing database schemas and table relationships
- **Episodic memory**: Query history and result cache with vector-based retrieval
- **Procedural memory**: Successful query patterns indexed for reuse

DataScribe demonstrates how graph-based semantic memory (NetworkX) can complement vector-based episodic storage for structured data exploration.

<!-- section_id: "ca6c1096-2e0b-4040-a4ab-85e2e4442836" -->
### 2.4 Self-Healing Codebase System

Uses ChromaDB as its primary memory backend:

```
bug_memory.add(
    documents=[error_description],
    metadata={'fix': solution_code, 'timestamp': now()},
    ids=[bug_id]
)

similar_bugs = bug_memory.search(current_error, n=3)
```

- **Semantic**: Code patterns and function definitions
- **Episodic**: Bug history with vector similarity search via ChromaDB
- **Procedural**: Fix patterns for recurring error types

The system retrieves the 3 most similar past bugs when a new error occurs, then applies learned fixes.

---

<!-- section_id: "d63ed13b-a051-4f89-98be-0e16c74344f8" -->
## 3. CrewAI Built-in Memory System

CrewAI provides a unified `Memory` class with built-in weighting and decay:

<!-- section_id: "85905a16-1ca1-45b0-ad41-aab17bf8bb0d" -->
### Memory Configuration Parameters

| Parameter | Purpose | Default Behavior |
|-----------|---------|------------------|
| `recency_weight` | How much recent memories are preferred | 0.4 (40% weight) |
| `semantic_weight` | How much semantic similarity matters | 0.4 (40% weight) |
| `importance_weight` | Explicit importance scores | 0.2 (20% weight) |
| `recency_half_life_days` | Memory decay rate | 14 days |

<!-- section_id: "363d8c3a-22dd-4395-94e2-5d6ba76eabec" -->
### Five Memory Types in CrewAI

| Memory Type | Backend | Purpose |
|-------------|---------|---------|
| Short-Term Memory | RAG | Recent conversation context |
| Long-Term Memory | SQLite3 | Persistent knowledge across sessions |
| Entity Memory | RAG | Track entities mentioned across conversations |
| Contextual Memory | In-memory | Maintain conversation coherence |
| User Memory | Persistent store | Personalization data per user |

CrewAI memory is shared across all agents in a Crew, enabling implicit coordination through shared context.

---

<!-- section_id: "0ee8b4cd-521e-42dc-bf65-525188336c57" -->
## 4. LangGraph + LangMem Integration

LangMem provides structured memory tools on top of LangGraph's state management:

<!-- section_id: "73c14f2a-084e-4f3f-8455-c51b498817d9" -->
### Architecture

- **Backend**: PostgresStore with pgvector for semantic search
- **Embedding**: OpenAI `text-embedding-3-small` (1536 dimensions)
- **Namespace**: Memory is organized into namespaces for isolation
- **Tools**: `create_manage_memory_tool` (write) and `create_search_memory_tool` (read)

<!-- section_id: "347b8e6d-e7dc-4c11-9902-4b5ecb79c9d2" -->
### Multi-Agent Pattern

Agents in the same LangGraph workflow share a PostgresStore backend but can operate on different namespaces. A "Knowledge Learner" agent stores new information while a "Knowledge Teacher" agent retrieves and synthesizes stored knowledge.

This pattern separates the write path (learning) from the read path (teaching), allowing different retrieval strategies for each.

---

<!-- section_id: "df64175a-a8f9-4d1c-bd4a-25b69eb8c9f2" -->
## 5. AutoGen Research Team

A five-agent collaborative system using Microsoft AutoGen:

| Agent | Memory Role | Memory Type |
|-------|-------------|-------------|
| Admin | Task history, delegation records | Episodic |
| Planner | Knowledge of agent capabilities | Semantic |
| Developer | Code patterns and best practices | Procedural |
| Executor | Past execution results and errors | Episodic |
| QA | Quality standards and test criteria | Semantic |

<!-- section_id: "cdd9e510-7d1e-46ea-b2e0-0489b5eb097c" -->
### Shared Memory via GroupChat

All agents share memory through AutoGen's `GroupChat` mechanism. The message history serves as shared episodic memory, with each agent extracting the information relevant to its role. `max_round=12` limits conversation length to prevent context overflow.

---

<!-- section_id: "293ff7f8-c2c2-433f-8fc6-c651ba85b281" -->
## 6. System Comparison

| System | Framework | Backend | Agent Count | Memory Architecture | Use Case |
|--------|-----------|---------|-------------|---------------------|----------|
| OASIS | LangGraph + Bedrock | OpenSearch | 2 | Episodic + Semantic + Procedural (indexed) | Production IT ops |
| ATLAS | Custom (GenAI_Agents) | Custom stores | 4 | All three types, per-agent specialization | Educational tutoring |
| Email Agent | LangMem + LangGraph | PostgresStore + InMemory | 1 | All three types via LangMem tools | Email automation |
| DataScribe | Custom (GenAI_Agents) | NetworkX + Vectors | 1 | Knowledge graph + vector episodic | Database exploration |
| Self-Healing Code | Custom (GenAI_Agents) | ChromaDB | 1 | Vector episodic + pattern procedural | Code maintenance |
| CrewAI Examples | CrewAI | SQLite + RAG | 2+ | Unified Memory class (5 subtypes) | Multi-agent teams |
| LangGraph + LangMem | LangGraph | PostgresStore | 2+ | Namespaced structured memory | Knowledge management |
| AutoGen Research | AutoGen | GroupChat messages | 5 | Shared episodic via message history | Collaborative research |

<!-- section_id: "8ccdb959-b8f3-4226-8f64-6a8ea0d85e1a" -->
### Complexity vs Capability Tradeoff

- **Simplest start**: CrewAI with `memory=True` -- built-in, minimal configuration
- **Custom control**: LangGraph + LangMem -- explicit memory tools, PostgreSQL durability
- **Production scale**: OASIS architecture -- OpenSearch backend, multi-index, audit trails

---

<!-- section_id: "d80682a5-023c-4e0a-8b44-bfb9d837f9c0" -->
## 7. Recommended Learning Path

| Week | System | Time | Learning Focus |
|------|--------|------|----------------|
| 1 | CrewAI memory example | ~2 hours | Understand unified memory API and agent sharing |
| 2 | ATLAS agent system | ~5 hours | Multi-agent coordination with specialized memory roles |
| 3 | LangMem custom agent | ~10 hours | Build custom memory tools with PostgreSQL persistence |
| 4 | OASIS architecture | ~5 hours | Production patterns: indexing, audit trails, human-in-the-loop |

---

<!-- section_id: "80894cfb-383c-424b-b23d-e34ef77fcb8c" -->
## Cross-References

- **Memory library APIs**: `07_memory_in_langchain_llamaindex.md`
- **Memory architecture tiers**: `23_core_ai_memory_systems.md`
- **Data structures for memory**: `22_core_data_structure_hierarchy.md`
- **Cognitive science foundations**: `01_cognitive_science_foundations.md`
- **Personal AI tutor systems**: `31_personal_ai_tutor_systems.md`

---

<!-- section_id: "a76f7e6d-6b7b-4d42-93b3-fc66467f283d" -->
## Sources

- [OASIS - AWS Sample Operational AI Agent](https://github.com/aws-samples/sample-operational-ai-agent) -- production IT incident management
- [GenAI_Agents Repository (Nir Diamant)](https://github.com/NirDiamant/GenAI_Agents) -- 45+ agent implementations including ATLAS, DataScribe, Self-Healing Code
- [AI Agent Memory: CrewAI, LangGraph, and AutoGen Comparison](https://dev.to/foxgem/ai-agent-memory-a-comparative-analysis-of-langgraph-crewai-and-autogen-31dp) -- comparative analysis
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory) -- official Memory class reference
- [LangMem + CrewAI Guide](https://langchain-ai.github.io/langmem/guides/use_tools_in_crewai/) -- integration guide
- [500+ AI Agent Projects Collection](https://github.com/ashishpatel26/500-AI-Agents-Projects) -- curated project list
- [Mem0 Memory Framework](https://github.com/mem0ai/mem0) -- production memory layer
- [All Agentic Architectures](https://github.com/FareedKhan-dev/all-agentic-architectures) -- architecture patterns
- [AI Agents for Beginners (Microsoft)](https://github.com/microsoft/ai-agents-for-beginners) -- educational resource
- Perplexity AI research conversation (Feb 2026) -- synthesis of agent system survey
