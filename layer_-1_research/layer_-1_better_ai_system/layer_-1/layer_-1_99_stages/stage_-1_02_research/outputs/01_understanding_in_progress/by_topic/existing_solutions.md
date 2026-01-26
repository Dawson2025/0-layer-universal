# Existing Solutions Survey

Research on existing tools and systems that address needs in the Tree of Needs.

**Last Updated**: 2026-01-26

---

## Solutions Analyzed

| Solution | Creator | Primary Focus | Overall Fit |
|----------|---------|---------------|-------------|
| [Clawdbot](#clawdbot) | Peter Steinberger (@steipete) | Personal AI Assistant | Partial - Strong patterns to learn from |

---

## Clawdbot

### Overview

**Creator**: Peter Steinberger (@steipete)
**Type**: Personal AI assistant with multi-channel support
**Architecture**: Gateway-based, local-first
**Status**: Active development (open source)

Clawdbot is a sophisticated personal AI assistant that runs 24/7, providing persistent memory and multi-channel access through WhatsApp, Telegram, email, and other platforms.

### Key Architecture

```
┌─────────────────────────────────────────────────┐
│                   Gateway                        │
│  (WebSocket control plane, channel routing)      │
├─────────────────────────────────────────────────┤
│                    Nodes                         │
│  (Distributed execution, Claude Code agents)     │
├─────────────────────────────────────────────────┤
│               Skills System                      │
│  (SKILL.md definitions, three-tier loading)      │
├─────────────────────────────────────────────────┤
│            Persistent Memory                     │
│  (MEMORY.md, daily files, semantic search)       │
└─────────────────────────────────────────────────┘
```

### Feature Deep-Dive

#### 1. Gateway Architecture
- Central control plane via WebSocket
- Routes messages from multiple channels to appropriate nodes
- Abstracts channel-specific differences
- Enables 24/7 availability

#### 2. Skills System
- **Format**: SKILL.md files with structured definitions
- **Loading**: Three-tier (always → on-demand → lazy)
- **Registry**: Skills can be discovered and composed
- **MCP Integration**: Skills can integrate with Model Context Protocol

Example SKILL.md structure:
```markdown
# Skill Name
Description of what this skill does

## Triggers
- When to activate this skill

## Capabilities
- What this skill can do

## Dependencies
- Other skills or tools required
```

#### 3. Persistent Memory
- **MEMORY.md**: Core persistent facts
- **memory/YYYY-MM-DD.md**: Daily conversation summaries
- **Semantic Search**: Find relevant memories across files
- **Manual + Automatic**: AI can be told to remember, also auto-extracts important facts

#### 4. Context Management
- **Compaction**: Summarizes old conversation history
- **Pre-flush**: Saves context before it would be lost
- **Progressive Loading**: Loads relevant context as needed

---

## Mapping to Tree of Needs

### Fit Assessment Legend

| Rating | Meaning |
|--------|---------|
| **STRONG** | Directly addresses the need with proven patterns |
| **GOOD** | Addresses the need with adaptable patterns |
| **PARTIAL** | Some relevant patterns, significant gaps |
| **WEAK** | Minimal relevance or opposite approach |
| **N/A** | Not addressed by this solution |

---

### Branch 01: Capable - "Can AI do the work?"

| Need | Fit | Analysis |
|------|-----|----------|
| **persistent_knowledge** | **STRONG** | MEMORY.md + daily files + semantic search provides exactly this. AI remembers facts, conversations, preferences. Proven pattern. |
| **scalable_context** | **GOOD** | Context compaction + progressive loading handles scale. Skills system enables delegation. Gateway distributes load. |
| **discoverable** | **PARTIAL** | SKILL.md files are self-describing but no hierarchy navigation. Memory search helps find things. Missing: directory structure awareness. |
| **multimodal** ⟷ | **WEAK** | Text-focused. Multi-channel (WhatsApp, Telegram) but not voice I/O or diagram generation. No Vibe Typer integration. |

### Branch 02: Continuous - "Does work keep going?"

| Need | Fit | Analysis |
|------|-----|----------|
| **tool_portable** | **PARTIAL** | Gateway abstracts channels (good). BUT internally Claude-specific. SKILL.md format is proprietary. Not truly tool-agnostic. |
| **session_resilient** | **STRONG** | Persistent memory + context saves means work continues across sessions. Daily files track what happened. Pre-flush preserves state. |
| **failure_recoverable** | **PARTIAL** | Memory persists on crash. Gateway can reconnect. BUT no explicit idempotency or rollback patterns documented. |
| **evolvable** | **GOOD** | Skills/plugins are modular and replaceable. BUT tight Claude coupling limits evolution to other AI models. |
| **cross_platform** | **PARTIAL** | Multi-channel good for access points. BUT runs on specific infrastructure. Unknown portability across Mac/Linux/Windows. |

### Branch 03: Trustworthy - "Can I trust AI?"

| Need | Fit | Analysis |
|------|-----|----------|
| **rule_compliant** | **N/A** | No documented rule hierarchy system. Skills have triggers but not compliance rules. |
| **predictable** | **PARTIAL** | Skills provide consistent behavior patterns. BUT no versioning or behavior contracts documented. |
| **bounded** | **WEAK** | Gateway routes messages but no scope definition system. Skills don't define boundaries. |

### Branch 04: Observable - "Can I see what's happening?"

| Need | Fit | Analysis |
|------|-----|----------|
| **transparent** | **PARTIAL** | Can view memory files directly. BUT no state inspection tools or visibility into active context. |
| **debuggable** | **WEAK** | No documented validation or diagnostic tools. Memory files help trace but no structured debugging. |
| **auditable** | **PARTIAL** | Daily memory files provide history trail. BUT no structured audit log or change tracking. |

### Branch 05: Engaging - "Is it enjoyable?"

| Need | Fit | Analysis |
|------|-----|----------|
| **multimodal** ⟷ | **WEAK** | Text-based interaction only. Multi-channel convenience but not rich interaction (voice, diagrams). |

---

## Summary Assessment

### Strengths to Learn From

| Pattern | Why It's Good | Applicable To |
|---------|---------------|---------------|
| **MEMORY.md + daily files** | Simple, file-based persistence that AI can read/write | persistent_knowledge |
| **Semantic memory search** | Find relevant context without loading everything | scalable_context |
| **SKILL.md format** | Self-describing capability definitions | discoverable |
| **Context compaction** | Manages context window limits gracefully | scalable_context |
| **Pre-flush saves** | Preserves work before context loss | session_resilient |
| **Gateway abstraction** | Separates channel handling from logic | tool_portable |

### Weaknesses / Gaps

| Gap | Impact | Our Approach Needed |
|-----|--------|-------------------|
| **Claude-specific** | Violates P2 (Technology Agnostic) | Need AGNOSTIC.md pattern |
| **No rule system** | No trustworthy branch coverage | Need rule hierarchy |
| **No debugging tools** | Limited observability | Need validation suite |
| **No scope boundaries** | AI could exceed intended scope | Need boundary definitions |
| **Text-only** | Limited engagement options | Need voice/visual support |
| **No CLAUDE.md cascade** | Doesn't use directory hierarchy | Need hierarchy navigation |

### Integration Potential

**Question**: Should we integrate Clawdbot directly?

**Answer**: **No, but learn from it.**

| Factor | Assessment |
|--------|------------|
| **P1: Future-Proof** | Clawdbot is Claude-specific, limiting evolution |
| **P2: Agnostic** | Gateway good, but internals are Claude-locked |
| **P3: Incremental** | Skills are modular, could adopt pattern |
| **P4: Human-AI** | Multi-channel access increases human connection |
| **P5: Simplicity** | File-based memory is beautifully simple |

**Recommendation**: Extract patterns, don't adopt wholesale.

---

## Patterns to Adopt

### 1. Memory File Pattern
Adopt MEMORY.md approach for persistent_knowledge:
```
project/
├── AGNOSTIC.md          # System prompt (agnostic)
├── MEMORY.md            # Persistent facts (agnostic)
└── memory/
    ├── 2026-01-26.md    # Daily summary
    └── 2026-01-25.md    # Previous day
```

### 2. Skill Definition Pattern
Adapt SKILL.md for discoverable agents:
```markdown
# skill_name/SKILL.md
## Purpose
What this skill does

## Triggers
When to use this skill

## Capabilities
What it can accomplish

## Dependencies
Required tools/other skills
```

### 3. Context Compaction Pattern
For scalable_context, implement:
- Automatic summarization of old conversation
- Pre-flush saves before context would be lost
- Progressive loading of relevant context

### 4. Gateway Abstraction Pattern
For tool_portable, consider:
- Central routing layer that abstracts AI tool differences
- Unified message format that translates to tool-specific

---

## Related Research

| Document | Relevance |
|----------|-----------|
| `memory_systems.md` | Deep dive on memory approaches (Clawdbot, Layer-Stage, SHIMI) |
| `agnostic_memory_system_research.md` | Builds on memory patterns |
| `by_need/01_persistent_knowledge/` | Will use memory patterns |
| `by_need/04_tool_portable/` | Will consider gateway pattern |

---

## References

- Clawdbot GitHub: github.com/steipete/clawdbot
- Peter Steinberger: @steipete
- Research via: Perplexity API (2026-01-26)
