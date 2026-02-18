# Problem Statement: Memory System for the Layer-Stage Framework

## The Core Problem

The layer-stage framework currently has memory mechanisms that evolved organically — CLAUDE.md context chains, auto-memory files, episodic memory stubs, status.json tracking — but lacks a **deliberate, unified memory architecture**. Each mechanism was added to solve an immediate need without a holistic design. The result:

- **Context chain works but is static** — CLAUDE.md files load hierarchically, but there's no dynamic adaptation based on task relevance
- **Episodic memory exists structurally but is empty** — directories and index files are created but rarely populated
- **Auto-memory is flat and isolated** — per-launch-directory only, learnings don't bridge across projects or tools
- **No runtime memory management** — no mechanism for the agent to decide what to load, when to forget, or how to consolidate
- **AALang specifies ideal behavior that doesn't execute** — the GAB agent defines a 4-mode context loading process (Loading → Validation → Propagation → Delivery) but it's design documentation, not runtime code

## What This Means in Practice

1. **Every session starts cold** — The agent must re-read files to rebuild context, even for work it did yesterday
2. **Important learnings are lost** — Insights from one session don't reliably carry forward unless manually recorded
3. **Context is either too much or too little** — Static CLAUDE.md loads everything in the path (wastes tokens) or misses relevant context from sibling/cousin entities
4. **Cross-project knowledge doesn't transfer** — Learning from one project doesn't benefit another
5. **No temporal awareness** — The system can't answer "what were we working on last week?" without manual file reading
6. **Multi-agent memory doesn't exist** — When multiple agents collaborate (e.g., team workflows), there's no shared memory protocol

## The Opportunity

The research in `stage_1_02_research/` has surveyed the full landscape of AI agent memory systems — from cognitive science foundations to production platforms. We now know what's possible. The question is: **what should OUR memory system look like, given our specific constraints and goals?**

This isn't about building another Mem0 or MemGPT. This is about designing a memory architecture that:
- Fits the layer-stage framework's hierarchical structure
- Works across multiple AI tools (Claude Code, Cursor, Gemini, etc.) — tool-agnostic
- Leverages what already exists (CLAUDE.md chain, episodic structure, auto-memory)
- Solves the specific problems our framework faces

---

## Sources

- Current system analysis from context chain integration research
- Gap analysis from `layer_2_subx2_feature_context_chain_system` research outputs
- Auto-memory documentation in `~/.claude/CLAUDE.md`
