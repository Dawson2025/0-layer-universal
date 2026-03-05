---
resource_id: "8bfc716a-525c-446e-b2e1-581e8d4f0fa9"
resource_type: "readme
output"
resource_name: "README"
---
# Context Avenue Web (03_context_avenue_web)

<!-- section_id: "b79d2cf9-7abb-4eb7-9e80-7b211f6daf41" -->
## What This Contains

The context avenue web adapts core system and setup-dependent content into **context avenue-specific formats**. Each avenue is an independent delivery mechanism — any one avenue can deliver the full context to an AI system.

<!-- section_id: "4db3df41-27c0-4d29-94a4-807b074a26e5" -->
## The Eight Avenues — Ordered by Comprehensiveness

The context avenue web consists of 8 file-based avenues ordered from **most detailed/comprehensive to most fragmented/specific**:

<!-- section_id: "bd054c97-0a93-4dc4-959c-869d1c3a25a6" -->
### File-Based Avenues (01-08): Most to Least Detailed

| # | Avenue | Format | Comprehensiveness | Purpose |
|---|--------|--------|-------------------|---------|
| 01 | AALang JSON-LD | `.gab.jsonld` | **Most detailed** | Complete agent definitions with all modes, actors, constraints, state machines |
| 02 | AALang Markdown | `.integration.md` | Somewhat less | Readable summaries of the JSON-LD (80% of detail) |
| 05 | Skills | `SKILL.md` | Well-detailed | Complete step-by-step execution with prerequisites and outputs |
| 04 | @Import References | `.md` files | Moderate detail | Curated reference collections and indexes |
| 06 | Agents | `.agent.jsonld` + `.md` | Less detailed | Agent stubs and lightweight definitions |
| 07 | Path Rules | `.md` files | Less detailed | Directory-scoped rules and context |
| 08 | Hooks | Shell scripts | **Least detailed** | Event-triggered scripts (most fragmented, most specific) |

<!-- section_id: "44cdc0f2-2576-45d7-81c6-2439d713127f" -->
### Data-Based Avenues (09-13) — Optional: Most Detailed → Optimization

| # | Avenue | Format | Purpose |
|---|--------|--------|---------|
| 09 | Knowledge Graph | `.json` | Semantic relationships between concepts |
| 10 | Relational Tables | SQL schema | Structured metadata with relational queries |
| 13 | SHIMI Structures | `.json` | Performance optimization primitives per node |
| 11 | Vector Embeddings | `.npy` / `.h5` | Semantic similarity fingerprints |
| 12 | Temporal Index | `.json` | Version history of all above structures |

<!-- section_id: "403522c3-7e50-47da-991d-468efc9818f7" -->
## Ordering Principle: Comprehensiveness

**The avenues are ordered from MOST comprehensive to MOST fragmented**:

- **Most comprehensive** (01): AALang JSON-LD contains the entire agent definition — every mode, every actor, every constraint, every state transition
- **Decreasing comprehensiveness** (02-07): Each subsequent avenue loses some detail in exchange for different representation (readability, task-focus, navigation, etc.)
- **Most fragmented** (08): Hooks are specific event triggers with minimal context — the most targeted, least comprehensive form

**Why this ordering?**

An AI system loading context should start with the most complete representation (01) and drill down if needed. The ordering reflects information density: start comprehensive, become more specific.

<!-- section_id: "7f4be0e4-a30f-4df0-b2f4-2f7fabce1ffc" -->
## Propagation Flow

```
Core System (01-05) + Setup-Dependent (02-08)
        ↓
Context Avenue Web
(File-based 01-08: comprehensive → fragmented)
(Data-based 09-13: optional enhancements)
        ↓
.1merge System (AI app-specific versions)
```

<!-- section_id: "5cb09968-9b8b-4c5a-9999-23486b7929a0" -->
## Key Principle: Any-One-Fires Resilience

Each avenue independently carries the full context. An AI system can load via:
- **Avenue 01** (AALang JSON-LD) — most complete
- **Avenue 02** (Integration Markdown) — readable alternative
- **Avenue 05** (Skills) — task-focused approach
- **Avenue 07** (Path Rules) — navigation-focused
- Or any combination

If one avenue is unavailable, others deliver the context intact.

<!-- section_id: "dc3c9d58-6715-4213-8f34-105fd5d84e6a" -->
## Next Steps

- File-based avenues overview: `01_file_based/00_file_based_overview/README.md`
- Data-based avenues overview: `02_data_based/00_data_based_overview/README.md`
