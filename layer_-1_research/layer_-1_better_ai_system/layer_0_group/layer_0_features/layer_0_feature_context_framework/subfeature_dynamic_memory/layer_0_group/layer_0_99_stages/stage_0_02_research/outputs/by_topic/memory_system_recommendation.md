# Memory System Recommendation

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: What approach to take for fixing agent amnesia

---

## The Question

Should you:
1. Use someone else's tool/framework?
2. Continue with your own system?
3. Integrate existing tools into your system?

---

## Recommendation: Hybrid Approach (Option 3, leaning toward Option 2)

**Continue your system as the core, selectively integrate tools for automation.**

---

## Why Your System Is Already Good

| What You Built | Why It's Good |
|----------------|---------------|
| `0AGNOSTIC.md` + `.0agnostic/` | Tool-agnostic (works with Claude, Codex, Gemini, Cursor) |
| Identity, Triggers, Pointers pattern | Context-efficient (~200-400 tokens) |
| `outputs/episodic/` | Explicit memory, git-trackable, human-readable |
| Output-First Protocol | Ensures nothing lost on compaction/crash |
| Layer-stage hierarchy | Your workflows, your organization |

**You've essentially built what the Memory Tool API does, but:**
- Tool-agnostic (not locked to Anthropic API)
- Integrated with your layer-stage system
- Git-versioned
- Human-readable/editable

---

## What Existing Tools Offer

### memory-mcp
- Auto-captures memories via hooks
- Injects into CLAUDE.md
- **Good for**: Automation of capture
- **Limitation**: Claude Code specific

### MemGPT / Letta
- Tiered memory (RAM/disk metaphor)
- Automatic memory management
- **Good for**: Complex long-running agents
- **Limitation**: Separate framework, not file-based

### Mem0
- Graph-based memory
- Better than RAG (67% vs 61%)
- **Good for**: Relational knowledge
- **Limitation**: Requires infrastructure

### Memory Tool API
- Official Anthropic solution
- Auto-checks /memories on start
- **Good for**: API-based apps
- **Limitation**: Not in Claude Code CLI

---

## Recommendation Details

### 1. Keep Your Core System (Don't Replace)

Your `0AGNOSTIC.md` + `.0agnostic/` + `outputs/episodic/` approach:
- Is tool-agnostic (huge advantage)
- Fits your layer-stage organization
- Is explicit and debuggable
- Doesn't lock you into any vendor

**Don't abandon this for a tool-specific solution.**

### 2. Add Automation via Hooks

The manual part of your system (writing to episodic/ before responding) can be automated:

```json
// .claude/settings.json
{
  "hooks": {
    "SessionEnd": [{
      "type": "command",
      "command": "scripts/save-session-summary.sh"
    }],
    "PreCompact": [{
      "type": "command",
      "command": "scripts/save-before-compact.sh"
    }]
  }
}
```

This gives you memory-mcp-like behavior without adopting their system.

### 3. Consider Integrating memory-mcp's Approach (Not the Tool)

Look at what memory-mcp does:
1. Hooks capture session info
2. Writes to CLAUDE.md or memory files
3. Next session reads it

You can implement this pattern yourself:
- SessionEnd hook → summarize → write to `outputs/episodic/`
- CLAUDE.md pointer → "On start, read `outputs/episodic/index.md`"

### 4. Don't Use Heavy Frameworks (Yet)

MemGPT, Mem0, LangGraph memory systems are:
- Complex to set up
- Require infrastructure
- Overkill for your current needs
- Not tool-agnostic

**Wait until you hit a wall with your simple approach.**

---

## Concrete Next Steps

### Immediate (Low Effort, High Value)

1. **Add to 0AGNOSTIC.md / CLAUDE.md**:
   ```markdown
   ## On Session Start
   Read `outputs/episodic/index.md` for recent session context.
   ```

2. **Create session summary template** in `.0agnostic/skills/`:
   - Skill that summarizes current session
   - Writes to episodic/sessions/

### Short-term (Medium Effort)

3. **Add hooks for automation**:
   - SessionEnd → auto-summarize
   - PreCompact → save state

4. **Test the pattern** on your current research stage

### Medium-term (If Needed)

5. **Build a simple retrieval system**:
   - Index episodic/ files
   - Semantic search over past sessions
   - Only if you find yourself not finding relevant history

---

## What NOT To Do

| Don't | Why |
|-------|-----|
| Replace your system with memory-mcp | Loses tool-agnostic advantage |
| Build complex RAG infrastructure | Overkill, adds latency, hard to debug |
| Wait for Claude Code to add memory | Could be months/years |
| Make memory implicit/hidden | Anthropic chose explicit for good reasons |

---

## Summary

```
Your System (core)     +    Selective Integration    =    Best Approach
─────────────────────       ──────────────────────       ─────────────────
0AGNOSTIC.md               Hooks for automation         Tool-agnostic
.0agnostic/                Session summary skill        Automated capture
outputs/episodic/          CLAUDE.md "read on start"    Explicit memory
Output-First Protocol      (Maybe memory-mcp ideas)     Your organization
```

**You're 80% there. The remaining 20% is automation, not architecture.**

---

## Sources Referenced

- [memory-mcp](https://github.com/anthropics/claude-code/issues/14227) (mentioned in GitHub issues)
- [Memory Tool API](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
- [Mem0 Research](https://arxiv.org/pdf/2504.19413)
- [MemGPT/Letta](https://www.letta.com/blog/agent-memory)
