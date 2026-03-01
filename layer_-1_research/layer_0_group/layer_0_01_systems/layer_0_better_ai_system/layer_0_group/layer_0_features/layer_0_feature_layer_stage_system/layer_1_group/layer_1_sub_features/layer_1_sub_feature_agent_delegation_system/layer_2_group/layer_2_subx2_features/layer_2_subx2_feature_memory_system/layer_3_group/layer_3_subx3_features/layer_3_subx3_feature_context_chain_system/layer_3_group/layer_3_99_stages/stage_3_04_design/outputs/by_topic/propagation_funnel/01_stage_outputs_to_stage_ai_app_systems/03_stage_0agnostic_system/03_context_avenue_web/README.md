# Context Avenue Web (03_context_avenue_web)

## What This Contains

The context avenue web adapts core system and setup-dependent content into **context avenue-specific formats**. Each avenue is an independent delivery mechanism — any one avenue can deliver the full context to an AI system.

## The Eight Avenues — Ordered by Comprehensiveness

The context avenue web consists of 8 file-based avenues ordered from **most detailed/comprehensive to most fragmented/specific**:

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

### Data-Based Avenues (09-13) — Optional: Most Detailed → Optimization

| # | Avenue | Format | Purpose |
|---|--------|--------|---------|
| 09 | Knowledge Graph | `.json` | Semantic relationships between concepts |
| 10 | Relational Tables | SQL schema | Structured metadata with relational queries |
| 13 | SHIMI Structures | `.json` | Performance optimization primitives per node |
| 11 | Vector Embeddings | `.npy` / `.h5` | Semantic similarity fingerprints |
| 12 | Temporal Index | `.json` | Version history of all above structures |

## Ordering Principle: Comprehensiveness

**The avenues are ordered from MOST comprehensive to MOST fragmented**:

- **Most comprehensive** (01): AALang JSON-LD contains the entire agent definition — every mode, every actor, every constraint, every state transition
- **Decreasing comprehensiveness** (02-07): Each subsequent avenue loses some detail in exchange for different representation (readability, task-focus, navigation, etc.)
- **Most fragmented** (08): Hooks are specific event triggers with minimal context — the most targeted, least comprehensive form

**Why this ordering?**

An AI system loading context should start with the most complete representation (01) and drill down if needed. The ordering reflects information density: start comprehensive, become more specific.

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

## Key Principle: Any-One-Fires Resilience

Each avenue independently carries the full context. An AI system can load via:
- **Avenue 01** (AALang JSON-LD) — most complete
- **Avenue 02** (Integration Markdown) — readable alternative
- **Avenue 05** (Skills) — task-focused approach
- **Avenue 07** (Path Rules) — navigation-focused
- Or any combination

If one avenue is unavailable, others deliver the context intact.

## Next Steps

- File-based avenues overview: `01_file_based/00_file_based_overview/README.md`
- Data-based avenues overview: `02_data_based/00_data_based_overview/README.md`
