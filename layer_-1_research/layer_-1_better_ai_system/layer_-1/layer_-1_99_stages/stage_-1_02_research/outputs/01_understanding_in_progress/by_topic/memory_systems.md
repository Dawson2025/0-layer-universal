# Memory Systems Research

Research on AI memory approaches and how they apply to the Tree of Needs.

**Last Updated**: 2026-01-26
**Related Needs**: persistent_knowledge, scalable_context, discoverable

---

## Overview

Three approaches to AI memory were analyzed:

| Approach | Description | Fit |
|----------|-------------|-----|
| [Clawdbot Memory](#clawdbot-memory) | MEMORY.md + daily files + semantic search | Patterns to adopt |
| [Layer-Stage Structure](#layer-stage-as-memory) | Hierarchical CLAUDE.md with ## Memory sections | Already have it |
| [SHIMI](#shimi-semantic-hierarchical-memory-index) | Semantic search + hierarchical structure | Best of both worlds |

**Conclusion**: Our Layer-Stage system already provides hierarchical memory. Adding SHIMI-style semantic matching would make it even more powerful.

---

## Clawdbot Memory

### How It Works

```
project/
├── MEMORY.md                 # Core persistent facts
└── memory/
    ├── 2026-01-26.md         # Today's conversation summary
    ├── 2026-01-25.md         # Yesterday
    └── ...                   # History
```

### Mechanisms

| Mechanism | Description |
|-----------|-------------|
| **Explicit** | User says "Remember X" → AI writes to MEMORY.md |
| **Auto-extract** | AI notices important facts → writes automatically |
| **Semantic search** | AI searches memory files for relevant context |

### Key Insight

MEMORY.md is **NOT** a system prompt file. It's application-managed:

```
User sends message
    ↓
Clawdbot code reads MEMORY.md
    ↓
Searches for relevant memories
    ↓
Injects relevant parts into prompt
    ↓
Sends to Claude
```

This allows selective injection (only relevant memories) vs. loading everything.

### Strengths

- Simple file-based storage (human-readable)
- Semantic search finds related content
- Daily journals provide audit trail
- Grows smarter over time

### Weaknesses

- Flat structure (no hierarchy)
- Requires separate application (Clawdbot) to manage
- Not built into Claude Code

---

## Layer-Stage as Memory

### How It Works

Our existing system already provides hierarchical memory through CLAUDE.md cascade:

```
0_layer_universal/
├── CLAUDE.md                          # Universal memories
│   └── ## Memory
│       - User preferences
│       - Global decisions
│
└── layer_-1_research/
    └── better_ai_system/
        ├── CLAUDE.md                  # Project memories
        │   └── ## Memory
        │       - Project decisions
        │       - Architecture choices
        │
        └── layer_-1/
            └── stage_02_research/
                └── CLAUDE.md          # Stage memories
                    └── ## Memory
                        - Research findings
                        - Options evaluated
```

### Mechanisms

| Mechanism | Description |
|-----------|-------------|
| **Cascade loading** | Claude Code walks up directory tree, loads all CLAUDE.md |
| **Hierarchical scope** | Universal → Project → Feature → Stage |
| **Manual updates** | AI or human updates ## Memory sections |

### Key Insight

Claude Code **automatically loads** CLAUDE.md files. No separate application needed.

### Strengths

- Already exists (no new system)
- Automatic loading by Claude Code
- Hierarchical scope (right memory at right level)
- Tool-agnostic via AGNOSTIC.md

### Weaknesses

- No semantic search (must know where to look)
- Loads entire CLAUDE.md (not selective)
- No auto-extraction of important facts

---

## SHIMI (Semantic Hierarchical Memory Index)

### What It Is

SHIMI combines semantic search WITH hierarchical structure. From research paper (arXiv:2504.06135):

> "A memory architecture that organizes knowledge as a dynamic, hierarchical tree of semantic concepts, enabling meaning-driven retrieval over surface-level similarity matching."

### How It Works

```
                    ┌─────────────────┐
                    │   Root Concept   │  ← Semantic summary
                    └────────┬────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         ┌────────┐    ┌────────┐    ┌────────┐
         │ Branch │    │ Branch │    │ Branch │  ← Semantic summaries
         └───┬────┘    └───┬────┘    └───┬────┘
             │             │             │
         ┌───┴───┐     ┌───┴───┐     ┌───┴───┐
         ▼       ▼     ▼       ▼     ▼       ▼
      [leaf]  [leaf] [leaf] [leaf] [leaf] [leaf]  ← Actual content
```

Query traversal:
1. Start at root
2. Semantic match query against child summaries
3. Expand high-similarity branches only
4. Prune low-similarity branches (don't search there)
5. Continue to leaves
6. Return relevant content

### Key Insight

Hierarchy makes semantic search **better**:
- Pruning reduces search space
- Logarithmic scalability (efficient for thousands of entities)
- More accurate than flat vector search
- Explainable (can trace path to result)

### Comparison

| Approach | Problem |
|----------|---------|
| Flat semantic search | Searches everything - slow, irrelevant matches |
| Hierarchy only | Must know exactly where to look |
| **SHIMI (both)** | Hierarchy prunes, semantic finds within |

---

## Applying SHIMI to Layer-Stage

### We Already Have the Hierarchy

```
0_layer_universal/                          # Node: Universal
├── CLAUDE.md                               # Summary: "Universal framework..."
│
└── layer_-1_research/                      # Node: Research Layer
    └── better_ai_system/                   # Node: This Project
        ├── CLAUDE.md                       # Summary: "Research project..."
        │
        └── layer_-1/
            └── stage_02_research/          # Node: Research Stage
                ├── CLAUDE.md               # Summary: "Explore solutions..."
                │
                └── outputs/
                    ├── by_need/            # Node: Per-Need Research
                    │   └── 01_persistent_knowledge/
                    │
                    └── by_topic/           # Node: Cross-Cutting
                        └── memory_systems.md  # Leaf: This file
```

### What We'd Add: Semantic Matching

Each CLAUDE.md already has semantic content:

```markdown
# CLAUDE.md

## Purpose
Research stage for exploring solutions...   ← Semantic summary

## Contains
- by_need/: Research per Tree of Needs need  ← Child descriptions
- by_topic/: Cross-cutting research
```

SHIMI-style query:
```
Query: "How should AI remember things?"

1. Root → Semantic match → "better_ai_system" (high)
2. Project → Semantic match → "stage_02_research" (high)
3. Research → Semantic match → "by_need/01_persistent_knowledge" (high!)
4. Result: persistent_knowledge research files
```

### Implementation Options

| Option | Complexity | Benefit |
|--------|------------|---------|
| **A: Manual navigation** | None (current) | AI reasons about structure |
| **B: Embedding summaries** | Medium | Add embeddings to CLAUDE.md Purpose sections |
| **C: Full SHIMI** | High | Build complete semantic index over hierarchy |

### Recommendation

**Start with Option A** (current structure + AI reasoning), document well.

**Consider Option B** if retrieval becomes a bottleneck:
- Generate embeddings for each CLAUDE.md ## Purpose section
- Store in lightweight index
- Query matches against summaries, returns paths

**Option C** likely overkill for our scale.

---

## Synthesis: Memory Architecture for Our System

### Critical Principle: CLAUDE.md Must Stay Lean

**CLAUDE.md is a system prompt** - it's loaded every time. It should contain:
- Instructions on HOW to use the system
- Navigation guidance (where to find things)
- Rules for this context
- Brief purpose description

**CLAUDE.md should NOT contain:**
- Memories (put in MEMORY.md)
- Detailed context (put in separate files)
- Research findings (put in outputs/)
- Session state (put in handoffs/)

### Separation of Concerns

```
CLAUDE.md (System Prompt - Always Loaded)
    │
    │  "Here's how to use this system..."
    │  "Find memories in MEMORY.md..."
    │  "Find research in outputs/..."
    │
    ├──→ MEMORY.md (Referenced When Needed)
    │    - Persistent facts
    │    - Decisions made
    │    - Preferences learned
    │
    ├──→ outputs/ (Navigated To)
    │    - Research findings
    │    - Analysis documents
    │
    └──→ hand_off_documents/ (Read on Resume)
         - Session context
         - Work in progress
```

### CLAUDE.md as Navigation Guide

```markdown
# CLAUDE.md (project level)

## Purpose
Research project for improving AI system architecture.

## Navigation
| Content | Location |
|---------|----------|
| Persistent memories | ./MEMORY.md |
| Research outputs | ./layer_-1/stage_02_research/outputs/ |
| Session handoffs | ./layer_-1/stage_*/hand_off_documents/ |
| Tree of Needs | ./layer_-1/stage_01_request_gathering/outputs/requests/tree_of_needs/ |

## How to Find Things
1. Check current stage's CLAUDE.md for context
2. Read MEMORY.md for persistent facts and decisions
3. Check hand_off_documents/incoming/ when resuming work
4. Navigate to outputs/ for detailed research

## Rules
- Update MEMORY.md when important decisions are made
- Create handoff documents before ending sessions
- Keep CLAUDE.md lean - reference, don't embed
```

### MEMORY.md (Separate File)

```markdown
# MEMORY.md

## Decisions
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-01-26 | DAG structure for Tree of Needs | Allows shared needs |
| 2026-01-26 | Layer-Stage for memory hierarchy | Already have structure |

## Preferences
- User prefers simple file-based solutions
- Avoid over-engineering

## Context
- Project started: 2026-01-26
- Current focus: Research stage
```

### Query Flow

```
Query: "What memory approach did we choose?"

1. AI reads CLAUDE.md (always loaded)
2. CLAUDE.md says: "Find memories in MEMORY.md"
3. AI reads MEMORY.md
4. Finds: "Layer-Stage for memory hierarchy"
5. Returns answer

CLAUDE.md stayed lean - just pointed to where to look.
```

---

## Key Findings

| Finding | Implication |
|---------|-------------|
| Clawdbot uses file-based memory | Simple, proven pattern |
| Layer-Stage already provides hierarchy | No new system needed |
| SHIMI shows hierarchy + semantic work together | Not either/or |
| **CLAUDE.md must stay lean** | System prompt, not content dump |
| **CLAUDE.md teaches navigation** | Tell AI how to find things, not everything |
| **MEMORY.md for persistent facts** | Separate file, referenced when needed |
| **Handoffs for session context** | Read on resume, not always loaded |

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE.md (Lean)                         │
│  - Purpose (brief)                                          │
│  - Navigation (where to find things)                        │
│  - How to use the system                                    │
│  - Rules                                                    │
│                                                             │
│  ALWAYS LOADED → Must stay small                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ References
                              ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ MEMORY.md   │  │ outputs/    │  │ handoffs/   │
│             │  │             │  │             │
│ Persistent  │  │ Research    │  │ Session     │
│ facts       │  │ findings    │  │ context     │
│             │  │             │  │             │
│ READ WHEN   │  │ NAVIGATE    │  │ READ ON     │
│ NEEDED      │  │ TO          │  │ RESUME      │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## References

- SHIMI Paper: arXiv:2504.06135 (April 2025)
- Clawdbot: github.com/steipete/clawdbot
- Research via: Perplexity API (2026-01-26)
