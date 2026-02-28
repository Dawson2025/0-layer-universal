# Benchmark Results and Performance Comparison of AI Memory Systems

## Overview

A comparative analysis of published benchmark results across memory systems, including methodology critiques and the evolving landscape of evaluation frameworks.

---

## 1. Major Benchmarks

### LoCoMo (Long-term Conversational Memory)
- **Source**: Snap Research, ICLR 2025
- **Dataset**: 50 human-human conversations, ~300 turns each, ~9K-26K tokens, up to 35 sessions
- **Categories**: Single-hop, multi-hop, temporal, commonsense/world knowledge, adversarial
- **Metrics**: F1 score, J score (judge score)
- **Limitation**: Context size (16K-26K tokens) fits within modern LLM context windows, making it potentially solvable without memory systems; no knowledge update testing

### LongMemEval
- **Source**: Published 2024-2025
- **Dataset**: 500 manually curated questions, ~115K tokens average
- **Categories**: Information extraction, multi-session reasoning, temporal reasoning, knowledge updates, abstention
- **Strengths**: Much longer context than LoCoMo; tests temporal reasoning and state changes; human-curated quality
- **Considered**: Most rigorous benchmark for enterprise use cases

### MemBench (ACL Findings 2025)
- **Evaluates**: Effectiveness, efficiency, and capacity of memory
- **Levels**: Factual memory and reflective memory
- **Scenarios**: Participation (agent actively engages) and observation (agent watches)

### MemoryAgentBench
- **Four core competencies**: Accurate Retrieval (AR), Test-Time Learning (TTL), Long-Range Understanding, Selective Forgetting
- **Tested models**: GPT-4o, Gemini-2.0-Flash, Claude-3.7-Sonnet with 128K-200K context windows

### Evo-Memory
- **Focus**: Test-time learning with self-evolving memory
- **Evaluates**: Both task performance AND memory quality

---

## 2. LoCoMo Benchmark Results (Consolidated Leaderboard)

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

### Key Insight
A simple filesystem-based approach (Letta) with GPT-4o mini scored 74.0%, beating Mem0's reported 68.5% and approaching specialized systems. This suggests agent capability with familiar tools may matter more than specialized memory architecture on simpler benchmarks.

---

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

## 4. Head-to-Head: Mem0 vs. Zep (Disputed)

The comparison between Mem0 and Zep is contentious due to implementation issues in Mem0's evaluation of Zep.

### Mem0's Reported Results
| Metric | Mem0 Graph | Zep (Mem0's impl) |
|--------|-----------|-------------------|
| J Score | ~75.71 | 65.99% |
| p95 Latency | 0.657s | 0.778s |

### Zep's Corrected Results
| Metric | Zep (correct impl) | Mem0 Graph |
|--------|-------------------|-----------|
| J Score | **75.14% +/- 0.17** | ~68% |
| p95 Latency | **0.632s** | 0.657s |

### Implementation Errors in Mem0's Zep Evaluation
1. Incorrect user model (both conversation participants assigned as single user)
2. Non-standard timestamp handling (appended to message text vs. dedicated field)
3. Sequential rather than parallel searches (artificially inflated latency)

### Task-Specific Strengths (from Mem0's paper)
| Task Type | Best System | F1 | J Score |
|-----------|------------|-----|---------|
| Multi-hop queries | Mem0 Graph | 28.64 | 51.15 |
| Temporal reasoning | Mem0 Graph | 51.55 | 58.13 |
| Open-domain | Zep | 49.56 | 76.60 |

---

## 5. MemOS Performance

### vs. OpenAI Global Memory (LoCoMo)
- **159% improvement** in temporal reasoning
- **38.97% overall accuracy gain**
- **60.95% reduction** in token overhead

### MemOS Rankings
- Ranks #1 in ALL LoCoMo categories (both MemOS-0630 and MemOS-1031 versions)
- Outperforms: Mem0, Zep, Memobase, LangMem, OpenAI Memory, Supermemory, MIRIX, MemU

---

## 6. SHIMI Performance (Synthetic Benchmark)

| Metric | SHIMI | RAG Baseline |
|--------|-------|-------------|
| Top-1 Retrieval Accuracy | **90%** | 65% |
| Mean Precision@3 | **92.5%** | 68.0% |
| Interpretability (human eval, /5) | **4.7** | 2.1 |
| Sync Bandwidth Savings | >90% | N/A |

### Scaling Characteristics
- Query latency remains relatively flat up to 2,000 entities
- RAG shows linear latency degradation
- Sublinear growth in node visits as tree depth increases

**Caveat**: SHIMI benchmarks use synthetic evaluation with 20 queries; not directly comparable to LoCoMo/LongMemEval.

---

## 7. Reflexion Performance (Task Benchmarks)

| Benchmark | Without Reflexion | With Reflexion | Improvement |
|-----------|------------------|----------------|-------------|
| HumanEval (code, pass@1) | 67% (GPT-4) | **91%** | +24 pts |
| AlfWorld (decision-making) | ~78% (ReAct) | **97%** (130/134 tasks) | +22 pts |
| HotPotQA (reasoning) | ~60% | **80%** | +20 pts |
| WebShop (web navigation) | Baseline | No improvement | 0 |

---

## 8. Memobase Performance

### LoCoMo Temporal Reasoning
- **85.05%** accuracy on temporal reasoning category
- Profile-based approach using user profile + event timeline
- Online latency under 100ms

---

## 9. Latency Comparison

| System | p95 Search Latency | Notes |
|--------|-------------------|-------|
| Mem0 Base | **0.200s** | Fastest but lower accuracy |
| Zep (correct) | 0.632s | Accurate implementation |
| Mem0 Graph | 0.657s | Higher accuracy variant |
| Memobase | <0.100s | Profile-based, very fast |
| Mem0 (reported) | 1.44s | Full pipeline latency |

---

## 10. Critical Analysis of Benchmarks

### LoCoMo Limitations
- Context size (16K-26K tokens) fits modern LLM windows → solvable without memory systems
- Missing ground truth answers in Category 5
- No knowledge update testing (critical for real applications)
- Speaker attribution errors
- Being superseded by LoCoMo-Plus (2026)

### LongMemEval Advantages
- 115K average tokens (requires actual memory management)
- Tests temporal reasoning and state changes
- Human-curated quality
- Better represents enterprise use cases
- Becoming the preferred benchmark

### General Benchmark Issues
- **Methodology disputes**: Different implementations of competitor systems produce different results (Mem0 vs. Zep controversy)
- **Self-reporting bias**: Companies benchmark their own systems favorably
- **Benchmark saturation**: LoCoMo becoming too easy for modern systems
- **Missing real-world metrics**: Production reliability, maintenance cost, operational complexity not measured
- **LLM backbone dependency**: Results heavily depend on which LLM is used (GPT-4o vs. Gemini vs. open-source)

### What Benchmarks Don't Measure
- Memory system complexity and maintenance burden
- Cost per query in production
- Graceful degradation under load
- Multi-agent coordination overhead
- Privacy and security characteristics
- Developer experience and integration difficulty

---

## 11. Performance Trends Summary

### Clear Patterns
1. **OS-inspired hierarchical systems** (MemOS, MemoryOS, Hindsight) consistently outperform flat approaches
2. **Temporal reasoning** is the hardest category across all benchmarks and differentiates systems most
3. **Graph-augmented** systems (Mem0 Graph, Zep) outperform pure vector approaches on multi-hop queries
4. **Simple baselines** (filesystem, full-context) perform surprisingly well on easier benchmarks
5. **LLM backbone quality** has massive impact; same system can vary 20+ points with different LLMs
6. **Specialized memory** provides diminishing returns as context windows grow

### Current State of the Art (Early 2026)
- **LoCoMo SOTA**: MemOS (~87%+) and Hindsight (89.61%)
- **LongMemEval SOTA**: Hindsight with Gemini-3 (91.4%)
- **Temporal reasoning SOTA**: MemOS (159% improvement over OpenAI baseline)
- **Best cost/performance**: Letta filesystem (74% with GPT-4o mini)

---

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
