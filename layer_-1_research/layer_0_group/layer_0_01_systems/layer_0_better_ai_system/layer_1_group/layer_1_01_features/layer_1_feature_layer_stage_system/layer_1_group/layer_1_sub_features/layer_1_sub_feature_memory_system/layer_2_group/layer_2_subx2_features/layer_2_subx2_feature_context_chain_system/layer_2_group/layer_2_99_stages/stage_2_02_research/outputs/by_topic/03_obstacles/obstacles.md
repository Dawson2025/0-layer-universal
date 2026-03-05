---
resource_id: "656101b3-f748-487c-a129-252b3b209fc1"
resource_type: "output"
resource_name: "obstacles"
---
# Obstacles — What Stands in the Way

## Purpose

A catalog of known obstacles to building the context system described in the vision. Each obstacle includes what makes it hard, what we've learned about it, and possible paths forward.

---

## Obstacle 1: Skill Invocation Is Non-Deterministic

**The problem:** Claude Code has no algorithmic trigger system for skills. The LLM reads skill descriptions and decides — probabilistically — whether a situation matches. The same situation may trigger a skill in one session and miss it in another.

**Why it's hard:**
- We can't change how Claude Code's skill matcher works (it's built into the tool)
- Even perfect descriptions don't guarantee invocation
- The ~16K character budget means skills can be silently dropped
- There's no way to log or observe when a skill was considered but not invoked

**What we know:**
- Explicit `/skill-name` invocation by the user always works (not probabilistic)
- WHEN/WHEN NOT patterns in descriptions improve match quality
- CLAUDE.md trigger tables and path-specific rules can supplement the matcher
- Multi-avenue redundancy increases overall probability

**Paths forward:**
- Strong descriptions + trigger tables + rules as triggers (defense in depth)
- Increase char budget via `SLASH_COMMAND_TOOL_CHAR_BUDGET` when many skills exist
- Accept that agent-invoked skills will never be 100% reliable — design for graceful degradation

---

## Obstacle 2: Static Context Budget

**The problem:** Every line in the CLAUDE.md chain costs tokens in every API message. The current chain is 717 lines. The recommended target is <400-500 lines. More context = less room for the actual conversation.

**Why it's hard:**
- Rules, navigation, identity, triggers — all want to be in static context
- Multiple levels of the hierarchy each add their own content
- It's easy to add "just one more line" but hard to remove existing content
- No tooling to measure or enforce the budget

**What we know:**
- Current chain: 717 lines across 5 files (static)
- ~100 lines are duplicated CRITICAL rules (in multiple files)
- ~75-100 lines are ceremonial AALang annotations that no runtime enforces
- Anthropic recommends keeping CLAUDE.md under ~500 lines total
- CLAUDE.md survives context compaction (re-loaded as foundational context)

**Paths forward:**
- Remove duplicated rules (define once in `~/.claude/CLAUDE.md`, reference elsewhere)
- Remove ceremonial AALang annotations (replace with compact jq instructions)
- Move detailed procedures to skills (on-demand loading)
- Move directory trees and detailed tables to @imported files
- Set a budget target and enforce it (script to count total static chain lines)

---

## Obstacle 3: JSON-LD Format Mismatch

**The problem:** JSON-LD is the format used for AALang agent definitions, but research shows it's the worst-performing structured format for LLM comprehension (0.34 accuracy per KG-LLM-Bench). It also consumes 3-5x more tokens than equivalent markdown.

**Why it's hard:**
- We've invested in JSON-LD agent definitions (17 orchestrators, 67 stage agents)
- JSON-LD provides genuine value for design-time precision (graph structure, explicit relationships)
- Can't simply abandon it — the precision matters
- But can't feed it directly to LLMs as instructions either

**What we know:**
- LLM format accuracy hierarchy: Markdown > YAML > JSON Schema > XML > JSON > JSON-LD
- JSON-LD can be selectively navigated via jq (2-5% of file)
- A transpiler can convert JSON-LD → optimized markdown (.integration.md)
- Zero major agent frameworks use JSON-LD for runtime instructions

**Paths forward:**
- Keep JSON-LD as design-time source of truth
- Transpiler generates .integration.md (markdown) for runtime use
- Selective jq navigation for specific lookups (not whole-file loading)
- Never load raw JSON-LD into LLM context as instructions

---

## Obstacle 4: Cross-Session Context Loss

**The problem:** Each new AI session starts with a clean slate. The agent has its CLAUDE.md chain and auto-memory, but conversational context — nuance built up during a session, intermediate decisions, partial progress — is lost.

**Why it's hard:**
- Claude Code doesn't persist conversation across sessions (by design)
- Context compaction summarizes (lossy) rather than preserving
- Hand-off documents help but require the agent to write them (and it doesn't always)
- Auto-memory is limited to 200 lines and operational learnings

**What we know:**
- CLAUDE.md survives compaction (always re-loaded)
- Auto-memory persists operational learnings (but limited, per-project)
- Episodic memory can capture session records (but requires manual creation)
- Hand-off documents work for structured context transfer
- Agent Teams context is fully lost when the team is deleted

**Paths forward:**
- Systematic hand-off creation (skill or rule that triggers at session end)
- Episodic memory with sync to auto-memory (bridge between sessions)
- Status files (status.json) for lightweight progress tracking
- Accept that nuance will be lost — design for quick re-orientation, not full recall

---

## Obstacle 5: Agent Teams Ephemerality

**The problem:** Claude Code's Agent Teams spawns agents for a task, but when the team is deleted, all agent context is destroyed. Agents aren't reusable across sessions. No declarative config — teams are created ad-hoc via natural language.

**Why it's hard:**
- Agent Teams is designed for ephemeral use (by design, not a bug)
- No custom CLAUDE.md per teammate — all share the project's CLAUDE.md
- No API for programmatic team creation from directory structure
- Spawn prompts are the only customization vector

**What we know:**
- Spawn prompts can inject layer-stage context at team creation time
- Hand-off documents can persist results between team sessions
- Users can enter any running agent (Shift+Up/Down)
- A team-creation skill could automate the spawn-prompt injection

**Paths forward:**
- Spawn prompts inject layer context (proven pattern)
- A `/create-team` skill reads layer structure → generates spawn prompts
- Hand-off + status files bridge between team sessions
- Accept ephemerality as a constraint — design for quick re-creation, not persistence

---

## Obstacle 6: Tool Fragmentation

**The problem:** Different AI tools (Claude Code, Cursor, Codex CLI, Gemini CLI) each have their own context format, skill system, and features. A context system that only works with one tool is fragile.

**Why it's hard:**
- Each tool has different syntax (CLAUDE.md vs .cursorrules vs AGENTS.md)
- Each tool has different capabilities (@import depth, rules, skill systems)
- Features evolve independently (Claude Code adds rules, Cursor adds globs, Codex adds marketplace)
- No standard for cross-tool context portability

**What we know:**
- 0AGNOSTIC.md + agnostic-sync.sh can generate tool-specific files from one source
- .1merge/ provides tool-specific overrides without polluting the agnostic source
- Core concepts are converging (all tools have context files, import references, rules)
- Episodic memory and status files are already tool-neutral (plain markdown)

**Paths forward:**
- Maintain 0AGNOSTIC.md as single source of truth
- Expand agnostic-sync.sh to cover more tools and features
- Use .1merge/ for tool-specific additions
- Track tool capability convergence — reusable patterns will emerge

---

## Obstacle 7: Reference Chain Discoverability

**The problem:** The agent can only follow references it knows about. If a reference chain exists but the agent was never told about it, the context is invisible.

**Why it's hard:**
- Dynamic context is by definition not in the system prompt
- The agent must be told "look here" — but those instructions are themselves static context
- Too many "look here" pointers bloat the static context
- Too few means context goes undiscovered

**What we know:**
- Trigger tables in CLAUDE.md map situations to resources (~5-10 lines)
- Path-specific rules auto-load by directory (no agent decision needed)
- @import chains are followed automatically once encountered
- Skill descriptions serve as self-describing triggers

**Paths forward:**
- Trigger tables as the compact index (situations → resources)
- Path-specific rules as automatic directory-level triggers
- Convention over configuration — predictable naming (e.g., `.integration.md` always next to `.gab.jsonld`)
- Keep the "discovery index" small and in static context

---

## Obstacle 8: Maintenance Burden

**The problem:** The more structured the context system, the more maintenance it requires. Files must stay in sync, descriptions must be updated, transpiler must run, episodic memory must be written.

**Why it's hard:**
- Manual maintenance doesn't scale — the system has 298 CLAUDE.md files
- Automated maintenance requires tooling (transpilers, sync scripts, hooks)
- The AI can help maintain but must be reminded/instructed to do so
- Stale context is worse than no context (misleading)

**What we know:**
- agnostic-sync.sh automates 0AGNOSTIC.md → tool files
- jsonld-to-md.sh automates JSON-LD → .integration.md
- episodic-sync.sh automates episodic → auto-memory
- Pre-commit hooks can enforce sync-on-change

**Paths forward:**
- Automate everything possible (sync scripts, transpilers, hooks)
- Design for staleness detection (timestamps, checksums, "last updated" fields)
- The AI updates its own episodic memory and status files
- Structural changes (new entities, new layers) use skills that handle the boilerplate

---

## Summary: Obstacle Severity

| Obstacle | Severity | Solvable? | Approach |
|----------|----------|-----------|----------|
| Skill invocation non-deterministic | High | Partially | Multi-avenue redundancy, strong descriptions |
| Static context budget | High | Yes | Remove bloat, move detail to dynamic |
| JSON-LD format mismatch | Medium | Yes | Transpiler, selective navigation |
| Cross-session context loss | Medium | Partially | Hand-offs, episodic memory, status files |
| Agent Teams ephemerality | Medium | Partially | Spawn prompts, hand-offs, team-creation skill |
| Tool fragmentation | Medium | Yes | Agnostic system, .1merge/ |
| Reference chain discoverability | Medium | Yes | Trigger tables, rules, conventions |
| Maintenance burden | Low-Medium | Yes | Automation (sync scripts, transpilers, hooks) |

---

*Obstacles document for the context chain system*
*Created: 2026-02-16*
