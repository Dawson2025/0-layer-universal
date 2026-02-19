# Automated Traversal for Your System

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: Could you adopt SHIMI-style automated traversal? What benefits?

---

## Current State: Manual Traversal

Right now, your system uses explicit traversal:

```
User asks question
    ↓
CLAUDE.md says "read outputs/episodic/index.md"
    ↓
You manually specify what to read
    ↓
Content loaded into context
```

**You decide** what's relevant. Full control, but manual effort.

---

## SHIMI-Style: Automated Traversal

```
User asks question
    ↓
System compares question to root summaries
    ↓
Automatically descends into most relevant branch
    ↓
Repeats at each level until finding specific content
    ↓
Relevant content loaded into context
```

**Algorithm decides** what's relevant. Less effort, but less control.

---

## How You Could Implement It (Simple Version)

You don't need SHIMI's full infrastructure. Here's a lightweight approach:

### Step 1: Add Summaries to Each Level

Every directory gets a `0INDEX.md` with:
```markdown
# Summary
This directory contains [brief description].

## Children
| Child | Summary |
|-------|---------|
| layer_0_group/ | Universal rules, prompts, knowledge |
| layer_1/ | Projects and features |
| layer_-1_research/ | Research projects |

## Keywords
rules, prompts, universal, projects, research
```

### Step 2: Traversal Algorithm

```
function find_relevant(query, current_dir):
    index = read(current_dir + "/0INDEX.md")

    if is_leaf(current_dir):
        return current_dir contents

    best_child = LLM_pick_most_relevant(query, index.children)

    return find_relevant(query, best_child)
```

### Step 3: Implementation Options

| Method | Complexity | Accuracy | Speed |
|--------|------------|----------|-------|
| **LLM-based** | Medium | High | Slow (API calls) |
| **Keyword matching** | Low | Medium | Fast |
| **Embeddings** | High | High | Medium |

**Recommended**: Start with LLM-based (ask Claude "which child is most relevant?")

---

## Benefits for You

### 1. Reduced Manual Effort
**Now**: You specify "read this file, then that file"
**With automation**: "Find what's relevant to X" → system navigates

### 2. Better Discovery
You might not know where relevant info is. Automated traversal can find:
- Old research you forgot about
- Related work in different layers
- Connections across stages

### 3. Scales with Growth
As your system grows:
- Manual: More files to remember, harder to specify
- Automated: Same query, system handles complexity

### 4. Consistent Retrieval
You might miss things when tired or rushed. Algorithm doesn't.

### 5. Works Across Tools
If implemented at the file/index level, it's still tool-agnostic.

---

## Drawbacks / Risks

### 1. Loss of Control
Automation might retrieve wrong things. You lose explicit "I know exactly what's loaded."

### 2. Added Complexity
Need to maintain summaries/indices at each level. More moving parts.

### 3. Latency
LLM-based traversal = API calls at each level. Could be slow for deep hierarchies.

### 4. Harder to Debug
When something goes wrong, harder to trace "why did it load this?"

### 5. Over-engineering Risk
Your system is small enough that manual might be fine. Automation adds overhead.

---

## Hybrid Approach (Recommended)

**Don't replace manual with automated. Add automation as an option.**

```
Manual (default):
  CLAUDE.md → "Read outputs/episodic/index.md"

Automated (when needed):
  User: "Find relevant research on memory systems"
  System: Traverses hierarchy, returns relevant files
```

### Implementation

1. **Keep current explicit pointers** in CLAUDE.md
2. **Add 0INDEX.md files** to each directory
3. **Create a `/find` skill** that does automated traversal
4. **Use `/find` when you don't know where something is**

---

## Simple Implementation Plan

### Phase 1: Add Indices (Low effort)
- Add `0INDEX.md` to each layer/stage with summary + children
- No automation yet, just documentation

### Phase 2: Manual Traversal Helper
- Skill that shows you the hierarchy and lets you pick
- Semi-automated: you see summaries, you choose

### Phase 3: Full Automated Traversal
- LLM-based "find most relevant" at each level
- Only if Phase 2 isn't enough

---

## Example: Automated Traversal in Action

**Query**: "What did I learn about Claude Code's memory?"

```
Start: 0_layer_universal/0INDEX.md
  → layer_-1_research most relevant (it's about research)

Descend: layer_-1_research/0INDEX.md
  → layer_-1_better_ai_system most relevant

Descend: layer_-1_better_ai_system/.../stage_-1_02_research/0INDEX.md
  → outputs/01_understanding_in_progress most relevant

Descend: outputs/01_understanding_in_progress/by_topic/0INDEX.md
  → Files about claude_code_memory, why_claude_code_lacks_memory

Return: [list of relevant files]
```

**Result**: System found the right files without you specifying paths.

---

## Verdict

| Question | Answer |
|----------|--------|
| Can you adopt automated traversal? | Yes, with simple index files + LLM matching |
| Should you? | Start with indices (Phase 1), add automation only if needed |
| Main benefit | Discovery + scaling without manual path specification |
| Main risk | Complexity + loss of explicit control |

**Recommendation**: Add `0INDEX.md` summaries now. They help manual navigation AND enable future automation. Don't build full automation until you feel the pain of manual traversal.
