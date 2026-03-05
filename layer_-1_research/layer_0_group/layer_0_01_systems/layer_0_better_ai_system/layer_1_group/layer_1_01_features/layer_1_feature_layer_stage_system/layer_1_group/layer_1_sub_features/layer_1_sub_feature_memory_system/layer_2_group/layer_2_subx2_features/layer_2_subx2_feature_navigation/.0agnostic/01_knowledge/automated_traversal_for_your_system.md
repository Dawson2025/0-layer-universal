---
resource_id: "937c9476-9dfc-4b32-af44-4b2d888e0eed"
resource_type: "knowledge"
resource_name: "automated_traversal_for_your_system"
---
# Automated Traversal for Your System

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: Could you adopt SHIMI-style automated traversal? What benefits?

---

<!-- section_id: "4580b3b3-b2e7-411a-b57a-3d7d154e84ab" -->
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

<!-- section_id: "88d74630-c9d4-4100-b5b3-36eb659507c5" -->
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

<!-- section_id: "83dd46ad-4f13-4121-840f-b8490e545bc0" -->
## How You Could Implement It (Simple Version)

You don't need SHIMI's full infrastructure. Here's a lightweight approach:

<!-- section_id: "93fc384f-3171-4a57-967a-e7f682e8c16b" -->
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

<!-- section_id: "f592ced4-5249-447a-bd20-c667b055e734" -->
### Step 2: Traversal Algorithm

```
function find_relevant(query, current_dir):
    index = read(current_dir + "/0INDEX.md")

    if is_leaf(current_dir):
        return current_dir contents

    best_child = LLM_pick_most_relevant(query, index.children)

    return find_relevant(query, best_child)
```

<!-- section_id: "20c60fa8-d5fe-40f3-aea1-4bfc2ade2119" -->
### Step 3: Implementation Options

| Method | Complexity | Accuracy | Speed |
|--------|------------|----------|-------|
| **LLM-based** | Medium | High | Slow (API calls) |
| **Keyword matching** | Low | Medium | Fast |
| **Embeddings** | High | High | Medium |

**Recommended**: Start with LLM-based (ask Claude "which child is most relevant?")

---

<!-- section_id: "200c13f3-a7ed-46c8-9481-499ceb305392" -->
## Benefits for You

<!-- section_id: "e26cd0f5-9f08-43e0-a8f6-14c978626b84" -->
### 1. Reduced Manual Effort
**Now**: You specify "read this file, then that file"
**With automation**: "Find what's relevant to X" → system navigates

<!-- section_id: "fce13188-5320-402f-a864-c9a57adc9587" -->
### 2. Better Discovery
You might not know where relevant info is. Automated traversal can find:
- Old research you forgot about
- Related work in different layers
- Connections across stages

<!-- section_id: "eedd9140-42a4-4c46-851c-c50ccfe2f0b6" -->
### 3. Scales with Growth
As your system grows:
- Manual: More files to remember, harder to specify
- Automated: Same query, system handles complexity

<!-- section_id: "df8593a3-84bc-4374-b349-e04473012534" -->
### 4. Consistent Retrieval
You might miss things when tired or rushed. Algorithm doesn't.

<!-- section_id: "e2105340-11f8-4e2f-8bf3-9135eb51971a" -->
### 5. Works Across Tools
If implemented at the file/index level, it's still tool-agnostic.

---

<!-- section_id: "5e23ea50-fdc7-4afd-a58f-90235ee2237d" -->
## Drawbacks / Risks

<!-- section_id: "2e4f84b4-dc5d-422a-a678-645e5efa84a8" -->
### 1. Loss of Control
Automation might retrieve wrong things. You lose explicit "I know exactly what's loaded."

<!-- section_id: "9ad0233a-fe99-480f-9b17-d6a7a3c3b871" -->
### 2. Added Complexity
Need to maintain summaries/indices at each level. More moving parts.

<!-- section_id: "64b5c769-7e5c-4b7d-80f8-8dc308e35737" -->
### 3. Latency
LLM-based traversal = API calls at each level. Could be slow for deep hierarchies.

<!-- section_id: "405e0c0b-fef7-4d90-a398-0b7c4803cfac" -->
### 4. Harder to Debug
When something goes wrong, harder to trace "why did it load this?"

<!-- section_id: "5d5637cb-282e-4acf-9f05-ca2cfb5b926d" -->
### 5. Over-engineering Risk
Your system is small enough that manual might be fine. Automation adds overhead.

---

<!-- section_id: "435ef5ae-0d18-4c9b-8a9b-bbf3922eeab5" -->
## Hybrid Approach (Recommended)

**Don't replace manual with automated. Add automation as an option.**

```
Manual (default):
  CLAUDE.md → "Read outputs/episodic/index.md"

Automated (when needed):
  User: "Find relevant research on memory systems"
  System: Traverses hierarchy, returns relevant files
```

<!-- section_id: "331a6234-207e-40af-b077-2f73a4283b50" -->
### Implementation

1. **Keep current explicit pointers** in CLAUDE.md
2. **Add 0INDEX.md files** to each directory
3. **Create a `/find` skill** that does automated traversal
4. **Use `/find` when you don't know where something is**

---

<!-- section_id: "8c6f8c68-1df4-40c6-b5e8-a678c2f34050" -->
## Simple Implementation Plan

<!-- section_id: "b6d22e20-8756-4ac4-a169-1f288e0a39a7" -->
### Phase 1: Add Indices (Low effort)
- Add `0INDEX.md` to each layer/stage with summary + children
- No automation yet, just documentation

<!-- section_id: "e112a57a-598d-4c4a-bf62-dd249226cff6" -->
### Phase 2: Manual Traversal Helper
- Skill that shows you the hierarchy and lets you pick
- Semi-automated: you see summaries, you choose

<!-- section_id: "f249c6f1-1295-46a0-8f3c-aea6a500a4cf" -->
### Phase 3: Full Automated Traversal
- LLM-based "find most relevant" at each level
- Only if Phase 2 isn't enough

---

<!-- section_id: "08b31a99-dc99-44ef-bfdd-b7ed9bfcf874" -->
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

<!-- section_id: "397c6b20-7b3d-4ecb-92dc-555b4e57814e" -->
## Verdict

| Question | Answer |
|----------|--------|
| Can you adopt automated traversal? | Yes, with simple index files + LLM matching |
| Should you? | Start with indices (Phase 1), add automation only if needed |
| Main benefit | Discovery + scaling without manual path specification |
| Main risk | Complexity + loss of explicit control |

**Recommendation**: Add `0INDEX.md` summaries now. They help manual navigation AND enable future automation. Don't build full automation until you feel the pain of manual traversal.
