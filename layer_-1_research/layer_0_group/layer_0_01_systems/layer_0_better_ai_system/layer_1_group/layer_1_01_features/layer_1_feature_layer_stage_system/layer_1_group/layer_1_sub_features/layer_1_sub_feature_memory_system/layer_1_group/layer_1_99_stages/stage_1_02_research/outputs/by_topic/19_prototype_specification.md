# Prototype Specification: Layer-Stage System as Memory System Prototype

## Decision

The **layer-stage system** at `layer_0_feature_layer_stage_system/` is the primary prototype for the better_ai_system memory system research.

**Rationale**: The layer-stage system is already a working memory system for AI agents — it's used daily across Claude Code, Cursor, Gemini, and other tools. Rather than building a separate prototype from scratch, we iterate on the system we already have.

**Prototype location**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/`

---

## What the Prototype Already Implements

### Data Structures Currently In Use

| # | Data Structure (from file 18) | Where in Layer-Stage System | Status |
|---|---|---|---|
| 9 | **Plain text files (Markdown/JSON on disk)** | Entire system — `0AGNOSTIC.md`, `CLAUDE.md`, episodic files, knowledge files, rules, protocols | **Primary backbone** |
| 3 | **Key-value store (hash map)** | `status.json` files, YAML frontmatter, entity identity blocks in `0AGNOSTIC.md` | **In use** |
| 5 | **Knowledge graph (graph database)** | `.gab.jsonld` agent definitions use JSON-LD graph structure; parent-child declarations in `0AGNOSTIC.md` | **Partially in use** (implicit, not formalized) |
| 12 | **Semantic tree (hierarchical tree)** | The layer-stage hierarchy itself IS a semantic tree — layers → features → sub-features, each with stages | **Core architecture** |
| 15 | **Production rule database (IF-THEN)** | `.0agnostic/rules/static/` and `rules/dynamic/` — condition-action rules for agent behavior | **In use** |

### Memory Types Currently Implemented

| Memory Type | Implementation | Quality |
|---|---|---|
| **Episodic memory** | `.0agnostic/episodic_memory/` — session files, change logs | Working but underused |
| **Semantic / factual memory** | `.0agnostic/knowledge/` — domain knowledge files, principles | Working well |
| **Procedural memory** | `.0agnostic/skills/` — SKILL.md files with WHEN/WHEN NOT conditions; `.0agnostic/rules/` | Working well |
| **Profile / persona memory** | `0AGNOSTIC.md` Identity section — role, scope, parent, children | Working well |
| **Hierarchical memory** | Layer-stage tree (semantic tree) — layer_0 → layer_1 → layer_2 levels with scoping | Core strength |
| **Context chain (working memory)** | CLAUDE.md chain loaded into system prompt; on-demand reads for dynamic context | Working — the main innovation |
| **Shared / collaborative memory** | Git-based — all context files version-controlled, synced across tools via agnostic system | Working well |

### Context Chain Architecture Already Built

The context chain system (at `layer_2_subx2_feature_context_chain_system/`) has:
- 9 knowledge files (architecture, optimization, principles)
- 4 protocols (validation, audit, repair, setup)
- 9 rules (5 static, 4 dynamic)
- 2 skills (chain-validate, avenue-check)
- 8 redundant avenues for context delivery
- 2 child features (chain_visualization, context_loading)

---

## What's Missing (Gap Analysis from Research)

### Data Structures NOT Yet In Use

| # | Data Structure | What It Would Add | Priority | Proposed Location |
|---|---|---|---|---|
| 4 | **Vector store** | Semantic search across knowledge files, episodic memories, research docs — find related content by meaning, not just filename/grep | High | New sub-feature or tool integration |
| 5 | **Knowledge graph (formalized)** | Explicit typed relationships between entities — parent/child, dependency, cross-reference, temporal — currently implicit in 0AGNOSTIC.md declarations | High | `context_chain_system/.0agnostic/knowledge/` as JSON-LD KG |
| 6 | **LLM-generated summary** | Rolling summaries of episodic memory across sessions — compressed history without losing gist | Medium | Episodic memory consolidation process |
| 13 | **Scored list / priority queue** | Composite scoring for retrieval (recency × relevance × importance) instead of manual file selection | Medium | Context loading optimization |
| 14 | **Stack** | Goal/task tracking with nesting — push subgoals, pop when done | Low | Could integrate with existing stage workflow |
| 1 | **Raw message list** | Already handled by the LLM's conversation buffer — not our concern | N/A | — |
| 2 | **Sliding window** | Already handled by the LLM — not our concern | N/A | — |
| 10 | **KV cache** | Internal to LLM — not something we control | N/A | — |
| 11 | **Model parameters** | Internal to LLM — not something we control | N/A | — |
| 16 | **Activation snapshots** | Requires model-level access — not feasible for our prototype | N/A | — |

### Memory Types NOT Yet Implemented

| Memory Type | What's Missing | How To Add |
|---|---|---|
| **Entity memory (structured)** | No centralized entity database — entities are documented in scattered 0AGNOSTIC.md files | Formalize as knowledge graph (see above) |
| **Reflection memory** | No system for agents to record "what worked, what didn't" after tasks | Add to episodic memory with a reflection protocol |
| **Summary / consolidated memory** | Episodic files grow indefinitely; no summarization or consolidation | Add LLM-based summary generation (periodic or on-demand) |
| **Scored retrieval** | Context loading is currently manual (read specific files) or rule-based; no relevance scoring | Add composite scoring to context loading decisions |

---

## Knowledge Graph Proposal for Context Chain System

### Location
`context_chain_system/.0agnostic/knowledge/context_chain_graph.jsonld`

### What It Would Contain

```
Nodes: Every entity in the layer-stage hierarchy
  - type: feature | sub-feature | stage | knowledge-file | rule | skill | protocol
  - properties: role, scope, layer-depth, token-cost

Edges (typed, directed):
  - PARENT_OF / CHILD_OF (hierarchical)
  - CROSS_REFERENCES (lateral)
  - DEPENDS_ON (functional)
  - TRIGGERS (conditional — "load X when entering Y")
  - AVENUE_DELIVERS (which avenue delivers which context)
  - PRECEDES / FOLLOWS (stage ordering)
```

### How to Build and Maintain

1. **Auto-generate** from 0AGNOSTIC.md declarations — a script reads all 0AGNOSTIC.md files, extracts Identity (parent/children), Triggers, and Pointers sections, and outputs JSON-LD
2. **Validate** with the existing `chain-validate` skill — compare graph against actual file system
3. **Regenerate** after structural changes (new entities, moved files) — add to `agnostic-sync.sh` workflow
4. **Manual overrides** only for relationships not declared in 0AGNOSTIC.md (cross-references, dependencies)

### Why This Fits (Research Grounding)

| Research Finding (from our docs) | Application |
|---|---|
| KGs capture typed relationships that vectors can't (file 15, Section 2) | Context chains have typed edges: parent-of, triggers, delivers-via-avenue |
| KGs enable multi-hop traversal (file 18, Section 5) | "What context should I load 3 levels up from here?" |
| KGs are strongest for structural, causal, and procedural relationships (file 15, Section 2) | The entire layer-stage hierarchy is structural; avenues are procedural |
| Auto-generation prevents staleness (file 15, Section 3.5 cautions) | Script-based generation from existing 0AGNOSTIC.md declarations |
| JSON-LD is already the system's graph format (GAB agents) | Consistent tooling, no new format to learn |

---

## Prototype Strengths (What We Already Do Well)

Based on the research (files 01-18), the layer-stage system already has several advantages over commercial systems:

1. **Tool-agnostic** — works with Claude, Gemini, Cursor, Copilot (most memory systems are locked to one tool)
2. **Human-readable and editable** — plain text files in git (most systems use opaque vector stores)
3. **Git-versioned** — full history, diffs, branching for free (most systems have no version control)
4. **Hierarchical scoping** — context narrows as you descend the tree (most systems are flat)
5. **Multi-avenue redundancy** — 8 ways to deliver context (most systems have one)
6. **File baseline performance** — Letta showed 74% LoCoMo with just files + GPT-4o mini (file 12); our system adds structure on top of files

---

## Next Steps

| Step | Stage | Description |
|---|---|---|
| 1 | Research (current) | Complete — 19 research files documenting the landscape |
| 2 | Instructions (stage 03) | Define what the prototype should do: feature requirements, acceptance criteria |
| 3 | Planning (stage 04) | Order of implementation: which gaps to fill first, dependencies |
| 4 | Design (stage 05) | Detailed design for each new component (KG schema, vector integration, summary pipeline) |
| 5 | Development (stage 06) | Build it — scripts, schemas, integrations |
| 6 | Testing (stage 07) | Validate against benchmarks (LoCoMo, LongMemEval) |
| 7 | Criticism (stage 08) | What doesn't work, what's over-engineered |
| 8 | Fixing (stage 09) | Iterate based on criticism |

---

## Sources

- All research files in this directory (files 00-18)
- Layer-stage system architecture: `layer_0_feature_layer_stage_system/0AGNOSTIC.md`
- Context chain system: `context_chain_system/0AGNOSTIC.md` and `.0agnostic/knowledge/`
- Letta file baseline: `12_benchmarks_and_performance.md`
- Knowledge graph research: `15_vectors_graphs_and_neurology.md` and `18_underlying_data_structures.md`
