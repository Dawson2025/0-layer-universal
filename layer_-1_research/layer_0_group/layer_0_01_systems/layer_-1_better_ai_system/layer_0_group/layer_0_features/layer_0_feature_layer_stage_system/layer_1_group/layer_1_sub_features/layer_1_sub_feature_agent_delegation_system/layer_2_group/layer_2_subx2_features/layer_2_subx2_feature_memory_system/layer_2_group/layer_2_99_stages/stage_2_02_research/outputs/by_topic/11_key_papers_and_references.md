# Key Papers and References: AI Agent Memory Systems

## Overview

Organized bibliography of the most important papers, surveys, and resources on AI agent memory systems. Papers grouped by topic with links and brief descriptions.

---

## 1. Comprehensive Surveys

| Paper | Year | Venue | Focus |
|-------|------|-------|-------|
| [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) | 2025 | arXiv | 3D taxonomy (forms, functions, dynamics); most comprehensive survey |
| [Rethinking Memory in AI: Taxonomy, Operations, Topics](https://arxiv.org/html/2505.00675v1) | 2025 | arXiv | 6 operations (consolidation, indexing, updating, forgetting, retrieval, compression); 30K+ papers reviewed |
| [From Storage to Experience: Evolution of LLM Agent Memory](https://www.preprints.org/manuscript/202601.0618) | 2026 | Preprints | Evolutionary framework: Storage → Reflection → Experience |
| [Memory in LLM-based Multi-agent Systems](https://www.techrxiv.org/users/1007269/articles/1367390/) | 2025 | TechRxiv | Multi-agent memory coordination, shared memory |
| [Agent Memory Paper List (GitHub)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) | 2025 | GitHub | Curated list of 150+ papers organized by taxonomy |

---

## 2. Foundational Memory Architectures

| Paper | Year | Venue | Focus |
|-------|------|-------|-------|
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | 2023 | arXiv | OS-inspired virtual context management; 4-tier memory |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | UIST | Observation → Reflection → Planning memory architecture |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | NeurIPS | Self-reflection as memory; verbal reinforcement learning |

---

## 3. Memory OS and Platforms

| Paper/System | Year | Venue | Focus |
|-------------|------|-------|-------|
| [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) | 2025 | EMNLP (Oral) | 3-tier hierarchical memory (STM/MTM/LPM); 4 functional modules |
| [MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724) | 2025 | arXiv | MemCube abstraction; unifies plaintext, activation, parametric memory |
| [Mem0: Building Production-Ready AI Agents](https://arxiv.org/abs/2504.19413) | 2025 | arXiv | Hybrid datastore (vector+graph+KV); production-scale memory |
| [SHIMI: Decentralizing AI Memory](https://arxiv.org/abs/2504.06135) | 2025 | arXiv | Semantic hierarchical tree; decentralized sync (Merkle-DAG + CRDT) |

---

## 4. RAG and Knowledge Graph Memory

| Paper | Year | Venue | Focus |
|-------|------|-------|-------|
| [Agentic Retrieval-Augmented Generation Survey](https://arxiv.org/abs/2501.09136) | 2025 | arXiv | Agents embedded in RAG pipeline |
| [Graph Retrieval-Augmented Generation Survey](https://dl.acm.org/doi/10.1145/3777378) | 2025 | ACM TOIS | Knowledge graphs + RAG |
| [HippoRAG](https://arxiv.org/abs/2405.14831) | 2024 | arXiv | Hippocampus-inspired memory indexing for RAG |
| [Graph-Based Agentic RAG Survey](https://www.academia.edu/144313989/) | 2025 | Academia | GA-RAG for multi-hop reasoning |

---

## 5. Cognitive Architecture Memory Models

| Paper/System | Year | Focus |
|-------------|------|-------|
| [Introduction to the Soar Cognitive Architecture](https://arxiv.org/pdf/2205.03854) | 2022 | SOAR: WM + procedural + EPMEM + SMEM |
| [Analysis and Comparison of ACT-R and Soar](https://arxiv.org/abs/2201.09305) | 2022 | Comparative analysis of two major architectures |
| [LIDA: A Systems-level Architecture](https://www.semanticscholar.org/paper/440adc841d1fa8bc8e3d3441fb4154f04349745b) | Various | Global Workspace Theory; most memory types |
| [Cognitive Architectures and Agents (Purdue)](https://ccn.psych.purdue.edu/papers/cogArch_agent-springer.pdf) | Various | Comparison of architectures for agents |

---

## 6. Multi-Agent Memory

| Paper | Year | Venue | Focus |
|-------|------|-------|-------|
| [MemIndex: Agentic Event-based Distributed Memory](https://dl.acm.org/doi/10.1145/3774946) | 2025 | ACM TAAS | Distributed memory management for MAS |
| [Multi-Agent Systems and Workflow Survey](https://www.researchgate.net/publication/395128299) | 2025 | ResearchGate | Three pillars: architectures, protocols, workflows |
| [Memory Mechanisms in LLM Agents](https://www.emergentmind.com/topics/memory-mechanisms-in-llm-based-agents) | 2025 | Emergent Mind | Overview of memory in LLM-based agents |

---

## 7. Self-Evolving and Learning Memory

| Paper | Year | Venue | Focus |
|-------|------|-------|-------|
| [SAGE: Self-Evolving Reflective Memory](https://www.emergentmind.com/topics/self-evolving-agents-with-reflective-and-memory-augmented-abilities-sage) | 2024+ | Various | Mitigating catastrophic forgetting in lifelong learning |
| [Hierarchical Memory for Long-Term Reasoning](https://arxiv.org/abs/2507.22925) | 2025 | arXiv | High-efficiency hierarchical memory for LLM agents |
| [SwiftMem: Fast Agentic Memory via Query-aware Indexing](https://arxiv.org/html/2601.08160) | 2026 | arXiv | Fast memory indexing for agents |

---

## 8. Experiential and Procedural Memory

| Paper | Year | Focus |
|-------|------|-------|
| Memp | 2024+ | Memory for tool proficiency |
| ToolMem | 2024+ | Tool usage pattern retention |
| FLEX | 2024+ | Self-evolving experiential agents |
| Alita | 2024+ | Experience-based agent learning |
| ReasoningBank | 2024+ | Storing and reusing reasoning traces |

---

## 9. Framework Documentation

| Resource | URL | Focus |
|----------|-----|-------|
| [Letta/MemGPT Documentation](https://docs.letta.com/concepts/memgpt/) | docs.letta.com | Core/recall/archival memory concepts |
| [Agent Memory Blog (Letta)](https://www.letta.com/blog/agent-memory) | letta.com | Agent memory taxonomy and design |
| [LangChain Memory Types](https://python.langchain.com/v0.1/docs/modules/memory/) | python.langchain.com | All LangChain memory implementations |
| [CrewAI Memory](https://docs.crewai.com/en/concepts/memory) | docs.crewai.com | Unified memory system |
| [Mem0 Research](https://mem0.ai/research) | mem0.ai | Mem0 benchmarks and papers |

---

## 10. Recommended Reading Order

For someone new to AI agent memory systems:

1. **Start with taxonomy**: "Memory in the Age of AI Agents" (arXiv:2512.13564) - establishes vocabulary and framework
2. **Understand foundations**: MemGPT paper (arXiv:2310.08560) - OS metaphor makes memory tiers intuitive
3. **See reflection in action**: Reflexion paper (arXiv:2303.11366) - learning from experience
4. **Study implementations**: Letta blog + LangChain docs - practical implementations
5. **Go deeper**: MemoryOS (arXiv:2506.06326) and SHIMI (arXiv:2504.06135) - cutting-edge architectures
6. **Multi-agent**: Multi-agent memory survey (TechRxiv) - coordination challenges
7. **Cognitive science**: SOAR/ACT-R comparisons - theoretical foundations
