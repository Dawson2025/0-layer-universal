# Complete AI Agent Systems with Memory

## Purpose

This document surveys **production-grade and open-source AI agent systems** that demonstrate full memory implementations (semantic, episodic, procedural) in working code. Unlike library documentation (see `07_memory_in_langchain_llamaindex.md`) or architecture patterns (see `23_core_ai_memory_systems.md`), these are complete, runnable systems that show how memory concepts compose into real applications.

---

## 1. OASIS - Operational AI System for Incident Solutions (AWS)

### Overview

OASIS is a production-grade IT incident management system built by AWS. It uses a multi-agent architecture with full memory across all three classical types.

### Memory Architecture

| Memory Type | Implementation | What It Stores |
|-------------|----------------|----------------|
| Episodic | OpenSearch `app-logs-logs` index | Raw event logs, incident history, status transitions |
| Semantic | OpenSearch `app-logs-agent-findings` index | Incident patterns, knowledge base, cross-service correlations |
| Procedural | Automated remediation procedures | Deployment fixes, rollback sequences, approval workflows |
| Time-series | OpenSearch `app-logs-metrics` index | System metrics for anomaly detection |

### Status Transition Flow (Episodic Memory)

```
initial_detection -> analysis_complete -> pending_approval -> approved -> mitigated
```

Each transition is stored as an episodic record, creating a complete audit trail.

### Key Capabilities

- Real-time anomaly detection from streaming logs
- Cross-service event correlation (semantic relationships)
- Learning from past incidents to improve future remediation (procedural)
- Human-in-the-loop approval workflows for critical actions
- Email notifications with full incident context

### Technology Stack

LangGraph (orchestration), Amazon Bedrock (LLM), OpenSearch (memory store), AWS Lambda (compute), SES (notifications)

---

## 2. GenAI_Agents Repository - Multi-Agent Systems Collection

The GenAI_Agents repository by Nir Diamant contains 45+ complete agent implementations. Four stand out for their memory architectures:

### 2.1 ATLAS - Academic Task and Learning Agent System

A four-agent educational system with comprehensive memory:

| Agent | Role | Memory Used |
|-------|------|-------------|
| Coordinator | Routes queries based on student understanding | Semantic (student profiles, course knowledge) |
| Planner | Creates personalized study schedules | Episodic (past assignments, performance history) |
| Notewriter | Generates notes matching learning style | Semantic (learning style preferences) |
| Advisor | Provides guidance on study strategies | Procedural (study strategies, time management patterns) |

ATLAS demonstrates how multiple agents can share memory stores while each specializing in different memory types for their particular function.

### 2.2 Memory-Enhanced Email Agent

Implements all three classical memory types using LangMem:

| Memory Type | Backend | Content |
|-------------|---------|---------|
| Semantic | `InMemoryStore` | Facts about contacts, company policies |
| Episodic | `PostgresStore` | Email thread history, conversation context |
| Procedural | Dictionary | Response templates, workflow patterns, user preferences |

The agent uses `create_manage_memory_tool` and `create_search_memory_tool` from LangMem to give the LLM direct control over memory operations.

### 2.3 DataScribe - Database Explorer Agent

Uses a knowledge graph approach to memory:

- **Semantic memory**: NetworkX graph storing database schemas and table relationships
- **Episodic memory**: Query history and result cache with vector-based retrieval
- **Procedural memory**: Successful query patterns indexed for reuse

DataScribe demonstrates how graph-based semantic memory (NetworkX) can complement vector-based episodic storage for structured data exploration.

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

## 3. CrewAI Built-in Memory System

CrewAI provides a unified `Memory` class with built-in weighting and decay:

### Memory Configuration Parameters

| Parameter | Purpose | Default Behavior |
|-----------|---------|------------------|
| `recency_weight` | How much recent memories are preferred | 0.4 (40% weight) |
| `semantic_weight` | How much semantic similarity matters | 0.4 (40% weight) |
| `importance_weight` | Explicit importance scores | 0.2 (20% weight) |
| `recency_half_life_days` | Memory decay rate | 14 days |

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

## 4. LangGraph + LangMem Integration

LangMem provides structured memory tools on top of LangGraph's state management:

### Architecture

- **Backend**: PostgresStore with pgvector for semantic search
- **Embedding**: OpenAI `text-embedding-3-small` (1536 dimensions)
- **Namespace**: Memory is organized into namespaces for isolation
- **Tools**: `create_manage_memory_tool` (write) and `create_search_memory_tool` (read)

### Multi-Agent Pattern

Agents in the same LangGraph workflow share a PostgresStore backend but can operate on different namespaces. A "Knowledge Learner" agent stores new information while a "Knowledge Teacher" agent retrieves and synthesizes stored knowledge.

This pattern separates the write path (learning) from the read path (teaching), allowing different retrieval strategies for each.

---

## 5. AutoGen Research Team

A five-agent collaborative system using Microsoft AutoGen:

| Agent | Memory Role | Memory Type |
|-------|-------------|-------------|
| Admin | Task history, delegation records | Episodic |
| Planner | Knowledge of agent capabilities | Semantic |
| Developer | Code patterns and best practices | Procedural |
| Executor | Past execution results and errors | Episodic |
| QA | Quality standards and test criteria | Semantic |

### Shared Memory via GroupChat

All agents share memory through AutoGen's `GroupChat` mechanism. The message history serves as shared episodic memory, with each agent extracting the information relevant to its role. `max_round=12` limits conversation length to prevent context overflow.

---

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

### Complexity vs Capability Tradeoff

- **Simplest start**: CrewAI with `memory=True` -- built-in, minimal configuration
- **Custom control**: LangGraph + LangMem -- explicit memory tools, PostgreSQL durability
- **Production scale**: OASIS architecture -- OpenSearch backend, multi-index, audit trails

---

## 7. Recommended Learning Path

| Week | System | Time | Learning Focus |
|------|--------|------|----------------|
| 1 | CrewAI memory example | ~2 hours | Understand unified memory API and agent sharing |
| 2 | ATLAS agent system | ~5 hours | Multi-agent coordination with specialized memory roles |
| 3 | LangMem custom agent | ~10 hours | Build custom memory tools with PostgreSQL persistence |
| 4 | OASIS architecture | ~5 hours | Production patterns: indexing, audit trails, human-in-the-loop |

---

## Cross-References

- **Memory library APIs**: `07_memory_in_langchain_llamaindex.md`
- **Memory architecture tiers**: `23_core_ai_memory_systems.md`
- **Data structures for memory**: `22_core_data_structure_hierarchy.md`
- **Cognitive science foundations**: `01_cognitive_science_foundations.md`
- **Personal AI tutor systems**: `31_personal_ai_tutor_systems.md`

---

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
