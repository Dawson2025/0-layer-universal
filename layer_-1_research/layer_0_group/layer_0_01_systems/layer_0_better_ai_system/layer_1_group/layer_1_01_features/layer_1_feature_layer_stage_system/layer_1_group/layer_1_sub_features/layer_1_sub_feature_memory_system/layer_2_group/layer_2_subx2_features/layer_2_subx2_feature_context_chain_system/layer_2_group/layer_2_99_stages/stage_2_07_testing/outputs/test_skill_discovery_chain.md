---
resource_id: "abd92d0b-57a4-4058-90de-3f54f9ccddd8"
resource_type: "output"
resource_name: "test_skill_discovery_chain"
---
# Test: Skill Discovery Chain — `/perplexity-extract`

**Date**: 2026-02-23
**Scope**: Verify that a new skill registered via .1merge + dynamic rules + SKILLS.md is discoverable by a fresh agent through the context chain
**Status**: PASS (6/6 checkpoints)

---

## Test Design

### What We're Testing

The `/perplexity-extract` skill was created and registered through multiple context avenues:
1. `.1merge/.1claude_merge/2_additions/tool_additions.md` (Claude-specific, universal)
2. `.0agnostic/02_rules/dynamic/browser_extraction_rule.md` (tool-agnostic, universal)
3. `.claude/skills/perplexity-extract/SKILL.md` (skill definition)
4. `.claude/skills/SKILLS.md` (skills index)
5. `.claude/rules/setup-dependant-context.md` (path-specific rule)
6. `sub_layer_0_10_claude_in_chrome/0AGNOSTIC.md` (entity-level registration)

The question: **Will a fresh agent, receiving a Perplexity URL, discover and use this skill?**

### Test Method

Two parallel agents were spawned:
1. **Mechanical verification**: Check each component exists and contains the right content
2. **Discovery simulation**: A fresh agent given a Perplexity URL traces through the context chain

---

## Checkpoint Results

### 1. Root CLAUDE.md (HOT context — every session)

| Field | Value |
|-------|-------|
| File | `0_layer_universal/CLAUDE.md` |
| Exists | YES |
| Location | Lines 113-142 ("Browser Extraction Capabilities" section) |
| Source | Auto-generated from 0AGNOSTIC.md + .1merge additions |
| Content | Skill table with `/perplexity-extract`, trigger conditions, prerequisites, key knowledge |
| Discovery | **IMMEDIATE** — loaded in every Claude Code session |

**PASS** — The skill is directly visible in hot context.

### 2. Global Config (~/.claude/CLAUDE.md)

| Field | Value |
|-------|-------|
| File | `~/.claude/CLAUDE.md` |
| Exists | YES |
| Direct mention | NO |
| Indirect path | Context Traversal Rule (step 3) → .0agnostic/02_rules/ → browser_extraction_rule.md |
| Discovery | **INDIRECT** — agent follows traversal rule to find dynamic rules |

**PASS (partial)** — No direct mention, but the traversal rule leads to the dynamic rule.

### 3. Path-Specific Rule (WARM context — on path entry)

| Field | Value |
|-------|-------|
| File | `.claude/rules/setup-dependant-context.md` |
| Exists | YES |
| Content | "Available Skills in This Tree" table explicitly lists `/perplexity-extract` |
| Trigger | Agents entering `.0agnostic/07+_setup_dependant/**` |
| Discovery | **AUTOMATIC** — Claude Code loads path-specific rules when working in matched directories |

**PASS** — Skill explicitly listed with scope and trigger.

### 4. Dynamic Rule (COLD context — on trigger)

| Field | Value |
|-------|-------|
| File | `.0agnostic/02_rules/dynamic/browser_extraction_rule.md` |
| Exists | YES |
| Importance | I2 (Standard) |
| Scope | All agents at all levels |
| Trigger conditions | 4 explicit conditions: Perplexity URL pattern, "extract citations" request, "get source URLs" request, React-rendered content mention |
| Action | Check Claude in Chrome MCP → invoke `/perplexity-extract` or fall back to WebFetch |
| Discovery | **ON DEMAND** — agent reads .0agnostic/02_rules/ as part of context traversal |

**PASS** — Comprehensive trigger conditions with clear action protocol.

### 5. .1merge Tool Additions (SOURCE for hot context)

| Field | Value |
|-------|-------|
| File | `.1merge/.1claude_merge/2_additions/tool_additions.md` |
| Exists | YES |
| Content | Identical to CLAUDE.md lines 113-142 (it's the source) |
| Scope | Claude Code only (not AGENTS.md, GEMINI.md, OPENAI.md) |
| Integration | agnostic-sync.sh reads this and appends to CLAUDE.md |
| Discovery | **N/A** — this is the generation source, not directly read by agents |

**PASS** — Source data is correct and properly scoped to Claude only.

### 6. Skill Definition (COLD context — on invocation)

| Field | Value |
|-------|-------|
| File | `.claude/skills/perplexity-extract/SKILL.md` |
| Exists | YES |
| Length | 180 lines |
| WHEN conditions | 4 conditions (Perplexity URL, extract with citations, knowledge base building, multi-turn capture) |
| WHEN NOT | 4 exclusions (non-Perplexity, simple page read, new query, behind auth) |
| Protocol | 9 detailed steps with JavaScript code |
| Known limitations | 5 documented issues with workarounds |
| Discovery | **ON INVOCATION** — loaded when `/perplexity-extract` is called |

**PASS** — Complete skill definition with protocol, limitations, and references.

---

## Discovery Simulation Results

A fresh Opus agent was given this task:
> "Extract content and citations from https://www.perplexity.ai/search/compare-openai-tts-vs-google-lBc2xVjJQYqjkceMFqWraw"

### Agent's Discovery Chain

1. **Read root CLAUDE.md** → Found "Browser Extraction Capabilities" at lines 113-142
2. **Recognized trigger** → URL matches `perplexity.ai/search/*` pattern
3. **Read SKILLS.md** → Found `perplexity-extract` in skills index (line 17)
4. **Read SKILL.md** → Loaded full 9-step protocol
5. **Read dynamic rule** → Confirmed trigger conditions and fallback behavior
6. **Located knowledge** → Found perplexity_extraction_rules.md and perplexity_extraction_protocol.md in AI apps level

### Agent's Planned Action

The agent would:
1. Call `tabs_context_mcp` to check Claude in Chrome availability
2. Create a fresh tab with `tabs_create_mcp`
3. Navigate to the Perplexity URL
4. Scroll through all answers (React virtualization)
5. Extract citations via React fiber traversal (exact JS from SKILL.md)
6. Supplement from Links tab
7. Output structured markdown

**PASS** — Agent correctly discovered the skill and knew exactly how to execute it.

---

## Insights

### What Works Well

1. **Hot context is the primary discovery mechanism** — The .1merge system successfully injects skill documentation into root CLAUDE.md, making it visible in every session without agents needing to search
2. **Multiple redundant paths** — Even if an agent missed the CLAUDE.md section, the dynamic rule, path-specific rule, or SKILLS.md would still lead to the skill
3. **Trigger conditions are specific enough** — URL pattern matching (`perplexity.ai/search/*`) prevents false positives
4. **Fallback behavior is documented** — If Claude in Chrome isn't available, agents know to fall back to WebFetch

### What Could Be Improved

1. **Global config gap** — `~/.claude/CLAUDE.md` doesn't directly mention perplexity extraction; the path to discovery is indirect (Context Traversal Rule → .0agnostic/02_rules/). This is by design (it's in .1merge additions, which only affect repo-level CLAUDE.md), but it means sessions outside the repo don't have the trigger.
2. **`...` in knowledge path** — The CLAUDE.md reference uses `...` shorthand for the deep sub-layer path. This is readable but not copy-pasteable. Agent 2 had to glob for the actual path.
3. **macOS mirror** — There's a `sub_layer_0_10_claude_in_chrome` under the macOS path too, but it only has the old structure (not migrated to .0agnostic/). This is a consistency issue.

### Key Metrics

| Metric | Value |
|--------|-------|
| Discovery paths | 5 (hot + warm + 3 cold) |
| Total trigger conditions | 4 explicit, 2 implicit |
| Steps to action from Perplexity URL | 1 (immediately visible in CLAUDE.md) |
| Steps to action without CLAUDE.md | 3 (context traversal → .0agnostic/02_rules/ → dynamic rule) |
| Skill protocol steps | 9 |
| Known limitations documented | 5 |

---

## Test Environment

- **Workspace**: `~/dawson-workspace/code/0_layer_universal/`
- **Agents used**: 2 (Haiku for mechanical verification, Opus for discovery simulation)
- **Commits tested against**: `2353b574` (user-level-sync.sh)
- **Context chain state**: agnostic-sync.sh validated with 0 warnings at claude_in_chrome level
