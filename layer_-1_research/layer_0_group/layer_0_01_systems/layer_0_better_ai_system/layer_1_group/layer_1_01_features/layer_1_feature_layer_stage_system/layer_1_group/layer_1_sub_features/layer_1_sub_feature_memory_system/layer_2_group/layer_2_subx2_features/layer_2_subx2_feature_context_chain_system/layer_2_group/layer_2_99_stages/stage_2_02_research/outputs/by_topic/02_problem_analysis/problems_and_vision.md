---
resource_id: "73c9e7ad-5a29-49a0-aac5-de1e45bea65f"
resource_type: "output"
resource_name: "problems_and_vision"
---
# Problems & Vision — AALang Integration

## The Core Problems

### Problem 1: Instructions Lost Across Sessions

**Symptom**: Instructions to the AI are not clear enough and get lost between chat sessions. Each new session starts without the nuance built up in previous sessions.

**Root cause**: Markdown-based instructions (CLAUDE.md) are good for human readability but lack the precision needed for machine execution. Natural language instructions are ambiguous — the agent "interprets" them differently each time.

**How AALang could help**: AALang's JSON-LD format is a graph-based, linked-data structure designed specifically for agent execution. It defines:
- Exact conditions for when an action should be taken (mode transition gates)
- Exact actors responsible for each type of work (persona assignments)
- Exact state that persists across execution phases (state actors)
- Exact communication patterns between components (message interface)

JSON-LD is more precise than markdown for machine consumption because it's structured data with explicit relationships, not prose that requires interpretation.

**Professor's resolution (2026-02-07)**: AALang's "Explicit Over Implicit" philosophy (#1 best practice) and self-check actors directly target this problem. Self-check actors catch vagueness, missing instructions, inconsistencies, and logic errors before deployment. The Definition Adoption model means the LLM BECOMES the actor — reading structured definitions as context-setting text. **Resolution: PARTIAL** — AALang solves the *definition precision* problem but not the *persistence-across-sessions* problem. Our layer-stage system (CLAUDE.md files, hand-off documents) provides the persistence layer.

---

### Problem 2: Agent Teams — Created Then Destroyed

**Symptom**: Claude Code's Agent Teams feature spawns a team of agents for a task, but when the task completes, the agents are terminated. Their context, learned patterns, and work state are lost. The agents aren't reusable.

**Root cause**: Agent Teams treats agents as ephemeral workers — spin up, do work, tear down. There's no persistence model.

**What the layer-stage system already solves**: The layer-stage system provides persistent agent context at every level:
- Each layer has a CLAUDE.md with management instructions
- Each layer has hand-off documents for IPC
- Each layer has status tracking (status.json)
- Each layer can have an orchestrator.gab.jsonld
- Context survives across sessions because it's in the file system, not in memory

**What the layer-stage system doesn't yet solve**: Interactive access to running agents. Agent Teams lets you "enter" any agent and interact with it live. The layer-stage system has the context and structure, but doesn't currently support jumping into a specific layer's agent and interacting with it while other layer agents are also running.

**The gap**: We need the **persistence and reusability** of the layer-stage system combined with the **interactivity and live orchestration** of Agent Teams.

**Professor's resolution (2026-02-07)**: AALang is MCP and A2A ready. The architecture supports persistent agents conceptually (state actors, file I/O). External agents are modeled as modes. But the professor doesn't address Claude Code Agent Teams specifically. **Resolution: NOT DIRECTLY ADDRESSED** — our layer-stage persistence + spawn prompts + hand-off documents is our bridge (not something the professor considers).

---

### Problem 3: Skills Not Being Used When They Should Be

**Symptom**: Skills files and folders exist but AI agents don't use them in situations where they should. The agent either doesn't know the skill exists, doesn't recognize when it applies, or doesn't know how to invoke it correctly.

**Root cause (hypothesis)**: Skills are defined in a way that relies on the agent's own judgment to recognize applicability. The trigger conditions ("use this when...") are written in natural language, which the agent may interpret loosely or miss entirely.

**How AALang could help**: AALang's mode-actor pattern includes explicit trigger conditions, confidence thresholds, and mode transition gates. If skill invocation were defined as an AALang pattern:
- **Trigger conditions** would be formalized (not just "use when the user asks about X" but structured conditions)
- **Actor assignments** would specify which skill handles which scenario
- **Confidence thresholds** would prevent premature or incorrect skill selection
- **The graph structure** (JSON-LD links) would create explicit connections between scenarios and skills

**Professor's resolution (2026-02-07)**: Not addressed. AALang's model is: load the .jsonld file, LLM follows it. There is no concept of a "skills ecosystem" or skill discovery. **Resolution: NOT ADDRESSED** — this is a Claude Code-specific problem. Our 6 markdown-based approaches (better descriptions, increased char budget, CLAUDE.md skill hints, path-specific rules, skill routing skill, WHEN/WHEN NOT patterns) remain the right direction. AALang patterns could inform skill description structure (formalized trigger conditions).

---

### Problem 4: Context Chain Efficiency

**Symptom**: The context chain (CLAUDE.md files from root to working directory) takes up space in the static context. Some of it is essential, some is wasted. There's no efficient way to keep critical instructions in static context while making detailed instructions available on-demand.

**Root cause**: Everything in CLAUDE.md is loaded at the same priority level. There's no distinction between "this MUST be in every message" vs "this should be available when needed."

**What we need**:
- **Static context** (always loaded): Minimal, critical, unadulterated rules and navigation pointers
- **Dynamic context** (loaded on-demand): Detailed instructions, agent definitions, skill configs
- **Clear referencing**: Static context points to dynamic context with precise instructions on when to load it

**How AALang fits**: The JSON-LD graph format is inherently a referencing system. A CLAUDE.md file could contain a small static section plus JSON-LD references that say "when in scenario X, load agent definition Y." The agent definitions themselves live in `.jsonld` files that are loaded only when needed.

**Professor's resolution (2026-02-07)**: Not directly addressed. The professor's model loads the entire .jsonld into context. The README acknowledges this needs "significant context windows." **Resolution: PARTIALLY VALIDATED** — our concern about context efficiency is confirmed by the professor's own acknowledgment. Our selective JSON-LD navigation idea and transpiler concept are novel — the professor doesn't propose either.

---

### Problem 5: Markdown vs JSON-LD for Agent Instructions

**Symptom**: Markdown is the standard format for CLAUDE.md, skills, and other agent configuration files across Claude Code, Codex, Gemini CLI, etc. But markdown is imprecise for machine execution.

**The tension**:
- **Markdown**: Human-readable, widely adopted, standard format for all major CLI tools (Claude Code's CLAUDE.md, Codex's AGENTS.md, Gemini's GEMINI.md)
- **JSON-LD**: Machine-precise, graph-structured, supports explicit relationships and conditions, better for exact agent behavior specification

**We can't abandon markdown** because:
- It's the standard that all tools (Claude Code, Codex, Gemini CLI) read
- Skills files/folders are markdown-based and shared across the community
- Human readability matters for debugging and understanding

**We can't rely only on markdown** because:
- Natural language instructions are ambiguous
- The agent interprets them inconsistently across sessions
- Complex conditional logic (do X when Y but not when Z) is hard to express precisely

**Professor's resolution (2026-02-07)**: The professor is firmly in the JSON-LD camp. Claims: formal structure reduces hallucinations, enables version control, provides reproducible bounded behavior. However, research (KG-LLM-Bench arXiv:2504.07087) shows JSON-LD scores lowest for LLM accuracy. **Resolution: TENSION REMAINS** — the professor may be right for complex agent orchestration with many cross-references; for simpler skills/rules, markdown is clearly better. The answer may be: **JSON-LD for complex agent definitions (navigated selectively), markdown for everything else.**

---

## The Vision (REVISED after verification — 2026-02-07)

> **CORRECTION**: Original vision proposed "markdown as surface, JSON-LD as depth." Research shows JSON-LD is the WORST format for LLM instruction (0.34 accuracy, 3-5x token cost). Vision revised below. See `verification_results.md` for full evidence.

### Architecture: Markdown All the Way Down, AALang as Design Vocabulary

```
┌─────────────────────────────────────────────────────────────┐
│                     STATIC CONTEXT (always loaded)           │
│                                                             │
│  CLAUDE.md (markdown, <500 lines)                           │
│  ├── Critical rules (always enforced)                       │
│  ├── @import references to detailed docs (max 5 hops)       │
│  ├── Skill trigger hints (WHEN + WHEN NOT descriptions)     │
│  └── Navigation pointers to layer-specific context          │
│                                                             │
│  .claude/rules/*.md (path-specific via paths: frontmatter)  │
│  ├── Rules that only activate for matching file patterns    │
│  └── Targeted context injection without static bloat        │
│                                                             │
└──────────────────────────┬──────────────────────────────────┘
                           │ on-demand loading
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    DYNAMIC CONTEXT (loaded when needed)      │
│                                                             │
│  Skills (.claude/skills/*/SKILL.md — markdown + YAML)       │
│  ├── Detailed execution instructions                        │
│  ├── Strong descriptions with explicit trigger conditions   │
│  └── Templates and supporting files                         │
│                                                             │
│  Child CLAUDE.md files (loaded when accessing subdirs)      │
│  ├── Layer-specific management instructions                 │
│  ├── Hand-off document protocols                            │
│  └── Status tracking references                             │
│                                                             │
│  @imported reference docs (max 5 hops from CLAUDE.md)       │
│  ├── Detailed procedures and guides                         │
│  └── Knowledge base articles                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│         STRUCTURED NAVIGATION (JSON-LD as graph index)      │
│                                                             │
│  AALang .gab.jsonld files (SELECTIVELY navigated)           │
│  ├── NOT loaded wholesale into context (too expensive)      │
│  ├── AI reads top-level structure first (~50 lines)         │
│  ├── AI navigates to specific nodes via @id references      │
│  ├── Only relevant sections loaded (10-25% of file)         │
│  └── Graph structure enables precise cross-referencing      │
│                                                             │
│  Think of it as: JSON-LD = structured database the AI       │
│  queries, NOT a document the AI reads cover-to-cover        │
│                                                             │
│  Future: AALang-to-Markdown transpiler (also valuable)      │
│  ├── Takes .gab.jsonld → produces optimized .md             │
│  ├── For cases where markdown skills are more appropriate   │
│  └── Bridge between design precision and runtime efficiency │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Design Principles (Revised — includes three-layer redundancy)

1. **Three-layer redundancy for skill invocation** — no single mechanism is sufficient; use jq-first (primary) + skill descriptions (fallback) + transpiled markdown (second fallback). See `architecture_decision_reference_chain.md`.
2. **AALang is a navigable graph** — JSON-LD defines agent architecture; the AI navigates it selectively via jq (2-5% of file), NOT loading it wholesale. See `selective_jsonld_navigation.md`.
3. **Transpiler keeps everything in sync** — auto-generated `.integration.md` files provide the same precision as JSON-LD, in the format LLMs read best (markdown). Never hand-edited, always regenerated.
4. **Use Claude Code's native mechanisms** — @import (5 hops), skills (on-demand), path-specific rules, child CLAUDE.md (dynamic)
5. **Skills remain shareable** — community format preserved (markdown + YAML frontmatter)
6. **jq instructions in CLAUDE.md** — explicit "run this command" is more reliable than implicit skill matching
7. **Layer-stage system provides persistence** — context survives across sessions via files
8. **Agent Teams provides interactivity** — live orchestration; spawn prompts inject layer context
9. **JSON-LD is the single source of truth** — all precision flows from JSON-LD into skills, markdown, and instructions

### Skills Integration Approach (Revised — three-layer redundancy)

> **CORRECTION**: Both "skills-first" (Pattern B) and "skills → JSON-LD pipeline" were rejected. Skills-first is circular (if skills don't fire, putting them first doesn't help). JSON-LD is worse for LLM direct comprehension.

**Approach: Three-Layer Redundancy**

1. **Layer 1 (PRIMARY): jq instructions in CLAUDE.md** — Agent runs jq against JSON-LD graph, gets precise mode/skill mappings. "Run this command" is more actionable than "decide if this skill matches."
2. **Layer 2 (FALLBACK): Improved skill descriptions** — WHEN/WHEN NOT patterns in YAML frontmatter, derived from JSON-LD mode constraints. Claude Code's native skill matcher uses these as fallback.
3. **Layer 3 (SECOND FALLBACK): Transpiled `.integration.md`** — Auto-generated markdown from JSON-LD. Agent reads this if jq doesn't run AND skills don't match. Same precision, native format, no tool calls needed.
4. **Supporting mechanisms** — CLAUDE.md compact mapping table, path-specific rules (`.claude/rules/*.md`), increase skill char budget via `SLASH_COMMAND_TOOL_CHAR_BUDGET`

### Agent Teams + Layer-Stage Convergence (Revised)

**Confirmed findings**:
- Agent Teams IS ad-hoc only — no declarative config from directory structure
- No custom CLAUDE.md per teammate — all load standard project CLAUDE.md
- Customization is through **spawn prompts** — this is our injection point
- Users CAN enter any agent (Shift+Up/Down, click panes) — interactivity confirmed
- Context is NOT reusable across sessions — our persistence layer fills this gap

**Approach**:
- **Spawn prompts** inject layer-stage context when creating teammates
- **Hand-off documents** persist results between Agent Teams sessions
- **Status files** track progress across sessions
- **Skills** encode the procedures that teammates should follow
- **A team-creation skill** could automate "read layer structure → spawn appropriate teammates with layer context"

---

## Next Steps (Revised — 2026-02-07)

### Completed
1. ~~Research JSON-LD references in CLAUDE.md~~ → **Done. Not supported. Use @import instead.**
2. ~~Prototype skill router in JSON-LD~~ → **Abandoned. Use markdown skills with better descriptions.**
3. ~~Test AALang definitions in context~~ → **Deprioritized. Too token-expensive. Build transpiler first.**
4. ~~Test JSON-LD selective navigation~~ → **PROVEN. jq loads 2-5% of file. See `selective_jsonld_navigation.md`.**
5. ~~Decide reference chain architecture~~ → **DECIDED. Three-layer redundancy. See `architecture_decision_reference_chain.md`.**

### Ready to Execute
6. **Write jq instructions for CLAUDE.md** — draft the 20-25 lines, test in a real session
7. **Build transpiler v1** (shell script) — generate `.integration.md` from existing JSON-LD
8. **Improve skill descriptions** — use JSON-LD mode constraints to write WHEN/WHEN NOT patterns
9. **Slim CLAUDE.md chain** — remove bloat (717 → ~350 lines), add jq instructions
10. **Create `.claude/rules/`** — path-specific rules for research, school, universal, aalang

### Planned
11. **Prototype @import-based context loading** — test whether @importing detailed docs improves instruction following
12. **Prototype team-creation skill** — automate layer-structure → Agent Teams mapping
13. **Test all three redundancy layers** — verify each layer independently, then test failover

---

*Research feature: layer_0_feature_aalang_integration/problems_and_vision*
*Last updated: 2026-02-07*
