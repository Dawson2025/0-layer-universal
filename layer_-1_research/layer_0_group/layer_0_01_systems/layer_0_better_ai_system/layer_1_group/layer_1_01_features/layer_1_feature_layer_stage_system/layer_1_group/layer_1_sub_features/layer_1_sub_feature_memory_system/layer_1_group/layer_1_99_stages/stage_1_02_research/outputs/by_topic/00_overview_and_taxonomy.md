---
resource_id: "78daa88b-2d96-4ac5-aa4c-7c8c6be93c43"
resource_type: "output"
resource_name: "00_overview_and_taxonomy"
---
# AI Agent Memory Systems: Master Taxonomy and Overview

<!-- section_id: "90a1cd8e-2f8e-4566-9d33-bfdce1206292" -->
## Research Scope

A comprehensive survey of memory system types used in AI agent architectures, spanning cognitive science foundations, modern LLM agent frameworks, dedicated memory platforms, and emerging research (2023-2026).

---

<!-- section_id: "21ec881d-00d5-4e01-af94-71b74dec1f5d" -->
## 1. Three-Dimensional Taxonomy (Liu et al., 2025)

The most authoritative recent taxonomy comes from "Memory in the Age of AI Agents" (arXiv:2512.13564), which organizes agent memory across three unified dimensions:

<!-- section_id: "3b3b5dc0-b38c-47d6-bb5c-f4e48805be79" -->
### Dimension 1: Forms (Storage Medium)

| Form | Description | Examples |
|------|-------------|----------|
| **Token-level** | Explicit discrete tokens stored externally, injected into context | RAG documents, conversation logs, knowledge base entries |
| **Parametric** | Information encoded in model weights via training/fine-tuning | LoRA adapters, knowledge editing, continual pre-training |
| **Latent** | Hidden state representations in intermediate layers | KV cache states, compressed memory embeddings, activation memories |

<!-- section_id: "a0a94183-28cb-4a0e-82c1-610853490165" -->
### Dimension 2: Functions (Purpose)

| Function | Description | Cognitive Analog |
|----------|-------------|-----------------|
| **Factual Memory** | Objective facts, knowledge, world state | Semantic memory |
| **Experiential Memory** | Past interactions, skills, reflections, episodes | Episodic + procedural memory |
| **Working Memory** | Active information for current task execution | Working memory / attention |

<!-- section_id: "bb5a96a7-59c1-40e5-9ce2-1e3e986dedad" -->
### Dimension 3: Dynamics (Lifecycle)

| Phase | Description | Key Operations |
|-------|-------------|----------------|
| **Formation** | How memory is initially created | Extraction, encoding, chunking |
| **Evolution** | How memory changes over time | Consolidation, updating, forgetting, merging |
| **Retrieval** | How stored information is accessed | Similarity search, temporal queries, graph traversal |

---

<!-- section_id: "91b20711-61ec-4373-a1d1-7a059866b1a3" -->
## 2. Memory Operations Taxonomy (arXiv:2505.00675)

Six fundamental operations across all memory types:

<!-- section_id: "0695cc90-faab-4564-a3fb-cb92b1ddac23" -->
### Management Operations
1. **Consolidation** - Converting short-term experiences into persistent storage
2. **Indexing** - Creating auxiliary access points and organizational structures
3. **Updating** - Modifying existing memory representations
4. **Forgetting** - Strategically removing outdated or harmful information

<!-- section_id: "29c10d03-4277-4ef3-b5bc-a748b7947c67" -->
### Utilization Operations
5. **Retrieval** - Accessing relevant memory content when needed
6. **Compression** - Reducing memory footprint while preserving essential information

---

<!-- section_id: "76a0b279-1b54-47ca-9062-e235e9b53562" -->
## 3. Memory Representations (Three Primary Types)

<!-- section_id: "149d7751-f02e-4ba8-bf4f-8bee1106bacb" -->
### Parametric Memory
- Knowledge embedded within model parameters during pretraining
- Provides instant, long-term, persistent recall without explicit storage
- Lacks transparency and selective updating capability
- Modified via: knowledge editing, unlearning, continual learning

<!-- section_id: "f2846f2a-a7c2-4070-ba1f-d172e6a6e8a2" -->
### Contextual Unstructured Memory
- Explicit storage across heterogeneous modalities (text, images, audio)
- Divided into: short-term (current session) and long-term (cross-session)
- Stored as raw text, embeddings, or summaries

<!-- section_id: "04e0e7ab-2673-48ca-9354-76798880fc3e" -->
### Contextual Structured Memory
- Information organized into interpretable formats
- Knowledge graphs, relational tables, ontologies
- Supports symbolic reasoning and precise querying

---

<!-- section_id: "9822dc7b-1489-4306-a233-937bf400b652" -->
## 4. Evolutionary Framework (From Storage to Experience)

Three developmental stages of LLM agent memory mechanisms:

1. **Storage Stage** - Trajectory preservation (raw conversation logs)
2. **Reflection Stage** - Trajectory refinement (summaries, insights)
3. **Experience Stage** - Trajectory abstraction (generalized knowledge, skills)

---

<!-- section_id: "455c8b64-2b1d-4566-a83c-51eb1decf7ea" -->
## 5. System-Level Research Domains

| Domain | Focus |
|--------|-------|
| **Long-Term Memory** | Persistent info from multi-turn dialogues; consolidation, indexing, retrieval |
| **Long-Context Memory** | Handling extensive input sequences; KV cache efficiency |
| **Parametric Memory Modification** | Knowledge editing, unlearning, continual learning within weights |
| **Multi-Source Memory** | Integrating heterogeneous textual + multimodal inputs |

---

<!-- section_id: "fde33121-945f-4393-8a5b-f92d8ce86301" -->
## 6. Topic Index

| File | Content |
|------|---------|
| `01_cognitive_science_foundations.md` | SOAR, ACT-R, LIDA, CLARION, human memory mapping |
| `02_memory_by_duration.md` | Short-term, working, long-term, sensory memory |
| `03_memory_by_content_type.md` | Episodic, semantic, procedural, entity, factual |
| `04_memory_dynamics_and_operations.md` | Formation, consolidation, forgetting, retrieval |
| `05_framework_implementations.md` | LangChain, CrewAI, AutoGPT, AutoGen, LangGraph |
| `06_dedicated_memory_platforms.md` | Mem0, Zep, MemGPT/Letta, MemoryOS |
| `07_commercial_ai_memory.md` | OpenAI, Anthropic Claude, Google Gemini |
| `08_multi_agent_memory.md` | Shared memory, collaborative memory, synchronization |
| `09_rag_and_knowledge_graphs.md` | RAG-as-memory, graph memory, agentic RAG |
| `10_reflection_and_learning.md` | Reflexion, self-reflection, experience accumulation |
| `11_key_papers_and_references.md` | Bibliography organized by topic |
| `12_benchmarks_and_performance.md` | LoCoMo, LongMemEval, head-to-head results, latency, methodology critiques |
| `13_practitioners_complete_guide.md` | Complete guide: design, architecture, planning, implementation, testing, criticism, fixing |
| `14_memory_types_best_for_guide.md` | Every memory type: what it's best for, not for, best implementation, key metric |
| `15_vectors_graphs_and_neurology.md` | Vector embeddings vs knowledge graphs vs human neurology: deep comparison, relationship types, brain circuits |
| `16_answer_traceability_log.md` | Per-answer map of findings to exact documents/sections for fast lookup |
| `17_learning_path.md` | Ordered learning sequence: what to watch, read, and study (12 phases, neuroscience → AI → our framework) |
| `18_underlying_data_structures.md` | All 16 underlying data structures: raw message list, sliding window, KV store, vector store, knowledge graph, LLM summary, relational DB, document store, plain text files, KV cache, model parameters, semantic tree, scored list, stack, production rules, activation snapshots |
| `19_prototype_specification.md` | Prototype decision: layer-stage system as primary prototype; what's already built vs what's missing; knowledge graph proposal for context chain system; next steps through stages 03-09 |
| `20_three_tier_knowledge_architecture.md` | Where content lives: Tier 1 (0AGNOSTIC.md pointers), Tier 2 (.0agnostic/knowledge/ distilled summaries), Tier 3 (stage outputs full content); consolidation process; anti-patterns; brain analogy mapping |

---

<!-- section_id: "4b47c044-bbf6-4037-be89-f9bac15554e7" -->
## Sources

- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Rethinking Memory in AI: Taxonomy, Operations, Topics (arXiv:2505.00675)](https://arxiv.org/html/2505.00675v1)
- [From Storage to Experience: Evolution of LLM Agent Memory](https://www.preprints.org/manuscript/202601.0618)
- [Agent Memory Paper List (GitHub)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
