---
resource_id: "12fa512f-96aa-43dd-a41d-87be73028c3f"
resource_type: "output"
resource_name: "12_benchmarks_and_performance"
---
# Benchmark Results and Performance Comparison of AI Memory Systems

<!-- section_id: "fd887035-36f2-43b9-8915-5e9bcc40fd92" -->
## Overview

A comparative analysis of published benchmark results across memory systems, including methodology critiques and the evolving landscape of evaluation frameworks.

---

<!-- section_id: "eeca1201-e475-4a45-9b8e-56d588b27149" -->
## 1. Major Benchmarks

<!-- section_id: "2ef9a88b-8e77-44a2-bb96-d996943cf4d3" -->
### LoCoMo (Long-term Conversational Memory)
- **Source**: Snap Research, ICLR 2025
- **Dataset**: 50 human-human conversations, ~300 turns each, ~9K-26K tokens, up to 35 sessions
- **Categories**: Single-hop, multi-hop, temporal, commonsense/world knowledge, adversarial
- **Metrics**: F1 score, J score (judge score)
- **Limitation**: Context size (16K-26K tokens) fits within modern LLM context windows, making it potentially solvable without memory systems; no knowledge update testing

<!-- section_id: "6532d56f-1e21-444d-bff2-37a89a479248" -->
### LongMemEval
- **Source**: Published 2024-2025
- **Dataset**: 500 manually curated questions, ~115K tokens average
- **Categories**: Information extraction, multi-session reasoning, temporal reasoning, knowledge updates, abstention
- **Strengths**: Much longer context than LoCoMo; tests temporal reasoning and state changes; human-curated quality
- **Considered**: Most rigorous benchmark for enterprise use cases

<!-- section_id: "a566e209-5717-4969-a8a3-c8138dc618e7" -->
### MemBench (ACL Findings 2025)
- **Evaluates**: Effectiveness, efficiency, and capacity of memory
- **Levels**: Factual memory and reflective memory
- **Scenarios**: Participation (agent actively engages) and observation (agent watches)

<!-- section_id: "7fcc3cad-4bb0-4650-801e-571abe9ff983" -->
### MemoryAgentBench
- **Four core competencies**: Accurate Retrieval (AR), Test-Time Learning (TTL), Long-Range Understanding, Selective Forgetting
- **Tested models**: GPT-4o, Gemini-2.0-Flash, Claude-3.7-Sonnet with 128K-200K context windows

<!-- section_id: "86e67d67-9ded-45a0-8901-84b7c51b7084" -->
### Evo-Memory
- **Focus**: Test-time learning with self-evolving memory
- **Evaluates**: Both task performance AND memory quality

---

<!-- section_id: "2fcd07b7-10a1-43c1-bd13-40890a6e2149" -->
## 2. LoCoMo Benchmark Results (Consolidated Leaderboard)

<!-- section_id: "6a017f63-5447-4c7a-b249-fbfc8cf3ddbb" -->
### Top Performers (Latest Data, 2025-2026)

| System | Overall Accuracy | Notes |
|--------|-----------------|-------|
| **Hindsight (Gemini-3)** | **91.4%** | Current SOTA on LongMemEval |
| **Hindsight (OSS-120B)** | **89.61%** | SOTA on LoCoMo |
| **MemOS (MemOS-1031)** | ~87%+ | Ranks #1 across all LoCoMo categories |
| **Hindsight (OSS-20B)** | 85.67% | +44.6 pts over full-context OSS-20B |
| **Supermemory (GPT-5)** | ~84.6% | Strong on LongMemEval |
| **Backboard** | 78.88% | - |
| **LangMem** | 77.77% | - |
| **Mem0 Graph** | 75.78% | Best Mem0 variant |
| **Mem0 Base** | 74.84% | - |
| **Letta Filesystem** | 74.0% | Simple filesystem approach, GPT-4o mini |
| **Memobase** | ~74.30% | Profile-based approach |
| **OpenAI Memory** | 72.04% | - |
| **Zep** | 71.72% | - |

<!-- section_id: "668da353-9982-4c01-b051-97bb878f6502" -->
### Key Insight
A simple filesystem-based approach (Letta) with GPT-4o mini scored 74.0%, beating Mem0's reported 68.5% and approaching specialized systems. This suggests agent capability with familiar tools may matter more than specialized memory architecture on simpler benchmarks.

---

<!-- section_id: "23d86209-f128-4ce1-b58f-3a9553cc3738" -->
## 3. LongMemEval Results (Consolidated)

| System | Overall | Temporal | Multi-Session | Knowledge Update |
|--------|---------|----------|---------------|-----------------|
| **Hindsight (Gemini-3)** | **91.4%** | - | - | - |
| **Hindsight (OSS-120B)** | 89.0% | 85.7% | 81.2% | 92.3% |
| **Supermemory (Gemini-3)** | 85.2% | - | - | - |
| **Supermemory (GPT-5)** | 84.6% | - | - | - |
| **Hindsight (OSS-20B)** | 83.6% | - | - | - |
| **Supermemory (GPT-4o)** | 81.6% | 81.95%* | 71.43%* | - |
| **Zep (GPT-4o)** | 71.2% | - | - | - |
| **Full-context GPT-4o** | 60.2% | - | - | - |
| **Full-context OSS-20B** | 39.0% | - | - | - |

*Supermemory's category-specific numbers from their own reporting.

---

<!-- section_id: "f1275ad7-d59c-4ce0-9003-b59a7d389682" -->
## 4. Head-to-Head: Mem0 vs. Zep (Disputed)

The comparison between Mem0 and Zep is contentious due to implementation issues in Mem0's evaluation of Zep.

<!-- section_id: "28eb58b9-3978-45be-9b64-f71c1115ee74" -->
### Mem0's Reported Results
| Metric | Mem0 Graph | Zep (Mem0's impl) |
|--------|-----------|-------------------|
| J Score | ~75.71 | 65.99% |
| p95 Latency | 0.657s | 0.778s |

<!-- section_id: "d09663ba-3852-409d-b834-8ef679d0d4fd" -->
### Zep's Corrected Results
| Metric | Zep (correct impl) | Mem0 Graph |
|--------|-------------------|-----------|
| J Score | **75.14% +/- 0.17** | ~68% |
| p95 Latency | **0.632s** | 0.657s |

<!-- section_id: "87f6053d-5a1a-465c-b743-196d800a0f6f" -->
### Implementation Errors in Mem0's Zep Evaluation
1. Incorrect user model (both conversation participants assigned as single user)
2. Non-standard timestamp handling (appended to message text vs. dedicated field)
3. Sequential rather than parallel searches (artificially inflated latency)

<!-- section_id: "d800983c-0df5-4ffa-b951-26c2f704e8b5" -->
### Task-Specific Strengths (from Mem0's paper)
| Task Type | Best System | F1 | J Score |
|-----------|------------|-----|---------|
| Multi-hop queries | Mem0 Graph | 28.64 | 51.15 |
| Temporal reasoning | Mem0 Graph | 51.55 | 58.13 |
| Open-domain | Zep | 49.56 | 76.60 |

---

<!-- section_id: "3aa7beca-a7dc-49cb-a553-4558faf82909" -->
## 5. MemOS Performance

<!-- section_id: "de6d6323-a09b-45f5-8b65-1540a5b587e7" -->
### vs. OpenAI Global Memory (LoCoMo)
- **159% improvement** in temporal reasoning
- **38.97% overall accuracy gain**
- **60.95% reduction** in token overhead

<!-- section_id: "7c1990b1-a609-449f-88fd-74f7499a10f1" -->
### MemOS Rankings
- Ranks #1 in ALL LoCoMo categories (both MemOS-0630 and MemOS-1031 versions)
- Outperforms: Mem0, Zep, Memobase, LangMem, OpenAI Memory, Supermemory, MIRIX, MemU

---

<!-- section_id: "e4cd8de5-8fbf-4dd3-afa3-2ffbc01e1606" -->
## 6. SHIMI Performance (Synthetic Benchmark)

| Metric | SHIMI | RAG Baseline |
|--------|-------|-------------|
| Top-1 Retrieval Accuracy | **90%** | 65% |
| Mean Precision@3 | **92.5%** | 68.0% |
| Interpretability (human eval, /5) | **4.7** | 2.1 |
| Sync Bandwidth Savings | >90% | N/A |

<!-- section_id: "2c256928-1424-4d25-8bc6-7a6d484606c5" -->
### Scaling Characteristics
- Query latency remains relatively flat up to 2,000 entities
- RAG shows linear latency degradation
- Sublinear growth in node visits as tree depth increases

**Caveat**: SHIMI benchmarks use synthetic evaluation with 20 queries; not directly comparable to LoCoMo/LongMemEval.

---

<!-- section_id: "42d95a6e-0f10-483f-b0f8-ebf1e1530f3c" -->
## 7. Reflexion Performance (Task Benchmarks)

| Benchmark | Without Reflexion | With Reflexion | Improvement |
|-----------|------------------|----------------|-------------|
| HumanEval (code, pass@1) | 67% (GPT-4) | **91%** | +24 pts |
| AlfWorld (decision-making) | ~78% (ReAct) | **97%** (130/134 tasks) | +22 pts |
| HotPotQA (reasoning) | ~60% | **80%** | +20 pts |
| WebShop (web navigation) | Baseline | No improvement | 0 |

---

<!-- section_id: "83e4a023-ef8d-4f1c-8a04-036e2f5ca299" -->
## 8. Memobase Performance

<!-- section_id: "3f74155d-c833-48c6-abb2-c0652bdda84f" -->
### LoCoMo Temporal Reasoning
- **85.05%** accuracy on temporal reasoning category
- Profile-based approach using user profile + event timeline
- Online latency under 100ms

---

<!-- section_id: "26e7141f-6a3f-429b-bc06-c2ece9a558a3" -->
## 9. Latency Comparison

| System | p95 Search Latency | Notes |
|--------|-------------------|-------|
| Mem0 Base | **0.200s** | Fastest but lower accuracy |
| Zep (correct) | 0.632s | Accurate implementation |
| Mem0 Graph | 0.657s | Higher accuracy variant |
| Memobase | <0.100s | Profile-based, very fast |
| Mem0 (reported) | 1.44s | Full pipeline latency |

---

<!-- section_id: "10f85e2f-249d-43c0-95f7-fa7f10f45ed3" -->
## 10. Critical Analysis of Benchmarks

<!-- section_id: "7c8f6738-9299-44a1-8f31-2673aa413e5a" -->
### LoCoMo Limitations
- Context size (16K-26K tokens) fits modern LLM windows → solvable without memory systems
- Missing ground truth answers in Category 5
- No knowledge update testing (critical for real applications)
- Speaker attribution errors
- Being superseded by LoCoMo-Plus (2026)

<!-- section_id: "a48fc72f-9f3e-4237-9634-b646329b97e5" -->
### LongMemEval Advantages
- 115K average tokens (requires actual memory management)
- Tests temporal reasoning and state changes
- Human-curated quality
- Better represents enterprise use cases
- Becoming the preferred benchmark

<!-- section_id: "c2cc8df6-1abd-4053-a0c2-392b83407533" -->
### General Benchmark Issues
- **Methodology disputes**: Different implementations of competitor systems produce different results (Mem0 vs. Zep controversy)
- **Self-reporting bias**: Companies benchmark their own systems favorably
- **Benchmark saturation**: LoCoMo becoming too easy for modern systems
- **Missing real-world metrics**: Production reliability, maintenance cost, operational complexity not measured
- **LLM backbone dependency**: Results heavily depend on which LLM is used (GPT-4o vs. Gemini vs. open-source)

<!-- section_id: "e46249a9-2802-4f5c-b249-88080c5c6604" -->
### What Benchmarks Don't Measure
- Memory system complexity and maintenance burden
- Cost per query in production
- Graceful degradation under load
- Multi-agent coordination overhead
- Privacy and security characteristics
- Developer experience and integration difficulty

---

<!-- section_id: "bba6a965-b196-422f-ae07-2e78350a0382" -->
## 11. Performance Trends Summary

<!-- section_id: "625a614a-3bd7-4b27-b6e2-938eb0cc2a8f" -->
### Clear Patterns
1. **OS-inspired hierarchical systems** (MemOS, MemoryOS, Hindsight) consistently outperform flat approaches
2. **Temporal reasoning** is the hardest category across all benchmarks and differentiates systems most
3. **Graph-augmented** systems (Mem0 Graph, Zep) outperform pure vector approaches on multi-hop queries
4. **Simple baselines** (filesystem, full-context) perform surprisingly well on easier benchmarks
5. **LLM backbone quality** has massive impact; same system can vary 20+ points with different LLMs
6. **Specialized memory** provides diminishing returns as context windows grow

<!-- section_id: "ec4d627a-f94f-41f2-982c-580d41366a30" -->
### Current State of the Art (Early 2026)
- **LoCoMo SOTA**: MemOS (~87%+) and Hindsight (89.61%)
- **LongMemEval SOTA**: Hindsight with Gemini-3 (91.4%)
- **Temporal reasoning SOTA**: MemOS (159% improvement over OpenAI baseline)
- **Best cost/performance**: Letta filesystem (74% with GPT-4o mini)

---

<!-- section_id: "1b41efd9-9301-4688-8191-c1c415a01d3b" -->
## Sources

- [Hindsight: Building Agent Memory that Retains, Recalls, and Reflects (arXiv:2512.12818)](https://arxiv.org/html/2512.12818v1)
- [Supermemory Research](https://supermemory.ai/research)
- [Benchmarking AI Agent Memory: Is a Filesystem All You Need? (Letta)](https://www.letta.com/blog/benchmarking-ai-agent-memory)
- [Is Mem0 Really SOTA in Agent Memory? (Zep)](https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)
- [Mem0 Benchmark Blog](https://mem0.ai/blog/benchmarked-openai-memory-vs-langmem-vs-memgpt-vs-mem0-for-long-term-memory-here-s-how-they-stacked-up)
- [MemOS: A Memory OS for AI System (arXiv:2507.03724)](https://arxiv.org/abs/2507.03724)
- [LoCoMo Benchmark (Snap Research)](https://snap-research.github.io/locomo/)
- [Memobase LoCoMo Benchmark Results](https://www.memobase.io/blog/ai-memory-benchmark)
- [MemBench (ACL Findings 2025)](https://aclanthology.org/2025.findings-acl.989/)
- [Reflexion (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [SHIMI (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (arXiv:2507.05257)](https://arxiv.org/abs/2507.05257)
