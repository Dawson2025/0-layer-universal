# Multi-Avenue Redundancy

## Purpose

How all context chaining avenues link together to ensure context is reliably loaded — even when individual avenues fail. Covers effectiveness per tool, how AALang/GAB and JSON-LD integrate, how the system prompt ties everything together, and the "any-one-fires" resilience model.

---

## The Problem: No Single Avenue Is Reliable

Every context delivery mechanism has failure modes:

| Avenue | Failure Mode |
|--------|-------------|
| System prompt (CLAUDE.md) | "May or may not be relevant" disclaimer degrades adherence |
| Path-specific rules | Only fire on file pattern matches, not task type |
| Skills | Non-deterministic (~37% baseline activation rate) |
| @imports | 5-hop limit, first external import requires user approval |
| JSON-LD/jq | Requires tool call, worst LLM comprehension format |
| .integration.md | Agent must be told to look for them |
| Episodic memory | Manual creation, can be stale |
| 0AGNOSTIC.md | Agent must be instructed to read it |

**No single avenue exceeds ~80% reliability on its own.** But by linking them all together so they reinforce each other, the probability of ALL failing drops below 5%.

---

## The 8 Avenues

### Avenue 1: System Prompt (CLAUDE.md Chain / AGENTS.md / GEMINI.md)

The always-present foundation. Contains compact pointers to all other avenues.

- **Static** — loaded in every API message
- **Generated** from `0AGNOSTIC.md` via `agnostic-sync.sh`
- **Contains**: trigger tables, @import references, jq instructions, skill pointers

### Avenue 2: Path-Specific Rules (.claude/rules/ with paths: frontmatter)

Rules that auto-load when the agent works with matching file paths.

- **Automatic** — no agent decision needed
- **Synced** from `.0agnostic/rules/static/` (always-loaded) and `.0agnostic/rules/dynamic/` (path-scoped)
- **Dynamic rules** contain triggers that point to protocols and skills

### Avenue 3: Skills (.claude/skills/ — progressive disclosure)

On-demand procedures that load full content only when invoked.

- **Two invocation paths**: user types `/skill-name` (100% reliable) or agent auto-invokes (probabilistic)
- **Synced** from `.0agnostic/protocols/` and `.0agnostic/skills/`
- **Descriptions** load at session start; full content loads on invocation

### Avenue 4: @import References

Inline references in CLAUDE.md or rules that load referenced file content.

- **Progressive** — content loads when the agent encounters the reference
- **Chain depth**: up to 5 hops
- **Points to**: knowledge files, detailed guides, reference material in `.0agnostic/knowledge/`

### Avenue 5: JSON-LD Agent Definitions (.gab.jsonld via jq)

Structured agent definitions navigated via selective jq queries.

- **Design-time source of truth** for agent behavior
- **Selective navigation**: load 2-5% of file per query
- **Contains**: mode constraints, skill mappings, state transitions

### Avenue 6: Integration Summaries (.integration.md)

Auto-generated markdown from JSON-LD — the runtime-readable version.

- **Transpiled** by `jsonld-to-md.sh` from `.gab.jsonld`
- **Markdown format** — highest LLM comprehension accuracy
- **Contains**: mode table, constraints, skill mappings (same as JSON-LD, but readable)

### Avenue 7: Episodic Memory

Session records that provide cross-session continuity.

- **Auto-memory** (`MEMORY.md` first 200 lines) loads automatically
- **Episodic files** (`outputs/episodic/index.md`) load on-demand
- **Contains**: what was done, decisions made, files changed

### Avenue 8: 0AGNOSTIC.md (Direct Read)

The agent can always read the source of truth directly.

- **Always available** — it's a file in the repository
- **Contains**: the complete agnostic context (before tool-specific generation)
- **Fallback of last resort**: if all generated files are missing, the source is still there

---

## How Avenues Link Together

The system prompt (Avenue 1) is the root node that connects to all others:

```
Avenue 1 (System Prompt)
    │
    ├── Trigger tables ────────────────→ Avenue 3 (Skills)
    │   "When creating entities,          "/entity-creation"
    │    use skill..."
    │
    ├── @import references ────────────→ Avenue 4 (@imports)
    │   "@knowledge/entity_lifecycle/     loads knowledge file
    │    INSTANTIATION_GUIDE.md"
    │
    ├── jq instructions ───────────────→ Avenue 5 (JSON-LD)
    │   "Find .gab.jsonld, run:           loads mode constraints
    │    jq '...Mode...' file"
    │
    ├── Pointers ──────────────────────→ Avenue 6 (.integration.md)
    │   "Read matching                    loads transpiled summary
    │    .integration.md"
    │
    └── Episodic reference ────────────→ Avenue 7 (Episodic Memory)
        "Read episodic_memory/            loads session history
         index.md if resuming"

Avenue 2 (Path Rules) ── fires automatically ──→ Avenue 3 (Skills)
    "When in research/,                           "Use /stage-workflow"
     follow protocol..."                     ──→ Avenue 5 (JSON-LD)
                                                  "Read .gab.jsonld"

Avenue 3 (Skills) ── references ──→ Avenue 4 (@imports to knowledge)
    "Read knowledge/X               ──→ Avenue 6 (.integration.md)
     before proceeding"                 "Check mode constraints"

Avenue 5 (JSON-LD) ── generates ──→ Avenue 6 (.integration.md)
    jsonld-to-md.sh transpiles          Same info, markdown format
```

**Every avenue points to at least one other avenue.** The system is a web, not a chain.

---

## Avenue Effectiveness by Tool

### Claude Code (Best Support — 8/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | CLAUDE.md chain (walks upward) | High | Survives context compaction |
| 2. Path Rules | `.claude/rules/` with `paths:` | High | Native, auto-loaded by path match |
| 3. Skills | `.claude/skills/` | Medium | Non-deterministic auto-invoke (~37-100% depending on description quality) |
| 4. @import | `@path/to/file` in CLAUDE.md | High | Native, 5-hop chain support |
| 5. JSON-LD/jq | Bash tool runs jq | Medium | Requires tool call, but reliable when executed |
| 6. .integration.md | Read tool | High | Markdown — highest LLM accuracy |
| 7. Episodic | Auto-memory (MEMORY.md) | High | First 200 lines auto-loaded |
| 8. 0AGNOSTIC.md | Read tool | High | Always available |

**What gets synced from .0agnostic/:**
- `rules/static/` → `.claude/rules/*.md` (auto-loaded at session start)
- `rules/dynamic/` → `.claude/rules/*.md` with `paths:` frontmatter (auto-loaded per directory)
- `protocols/` → `.claude/skills/*/SKILL.md` (progressive disclosure — descriptions at start, full content on invoke)
- `skills/` → `.claude/skills/` (direct copy)
- `agents/` → `.claude/agents/` (direct copy)

**What gets added from .1merge/.1claude_merge/:**
- `settings.json` (hooks, permissions)
- Claude-specific skills (e.g., `/claude-project-setup`)
- Override protocols with Claude-specific tool calls (Read, Write, Edit, Task)
- Additional rules about Claude Code features (auto-memory, @imports, Agent Teams)

**Compensation strategy:** None needed — Claude Code supports all 8 avenues natively. The full multi-avenue redundancy model works as designed.

**Avenue chain example:**
```
Agent enters layer_-1_research/ directory:
  Avenue 2 fires: .claude/rules/research-context.md auto-loads
    → tells agent: "use /stage-workflow, read .gab.jsonld"
  Avenue 3 activates: /stage-workflow skill matches research context
    → loads full protocol with steps
  Avenue 1 present: CLAUDE.md trigger table reinforces skill usage
  Avenue 5 available: agent can run jq for precise mode constraints
  Avenue 6 available: .integration.md provides readable mode table

Result: 5 avenues independently point to the same workflow
```

---

### Codex CLI (5/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | AGENTS.md (walks from project root to cwd) | Medium | 32KB silent truncation if too large |
| 2. Path Rules | N/A | N/A | No native path-scoped rules |
| 3. Skills | `.agents/skills/` | Medium | Scans cwd up to repo root |
| 4. @import | N/A | N/A | No @import support |
| 5. JSON-LD/jq | Bash access | Medium | Can run jq, but must be instructed |
| 6. .integration.md | File read | High | Markdown reads work well |
| 7. Episodic | File read | Medium | No auto-memory, must be instructed |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `AGENTS.md` (system prompt content)
- `rules/static/` → Inlined into `AGENTS.md` as a rules section (Codex has no separate rules directory)
- `protocols/` → `.agents/skills/` (Codex scans this directory for skills)
- `skills/` → `.agents/skills/` (merged with protocols)

**What gets added from .1merge/.1codex_merge/:**
- `config.toml` (Codex CLI configuration)
- Protocol overrides adapted for Codex's sandbox environment
- Additional knowledge about Codex's 32KB truncation behavior

**Compensation for missing avenues:**
- **No path rules (Avenue 2):** Inline the most critical path-context triggers into AGENTS.md itself. The agent always sees them. Less precise than path-scoping but better than nothing.
- **No @import (Avenue 4):** Skills must include all necessary context inline rather than referencing external files. Make Codex skills more self-contained.
- **No auto-memory (Avenue 7):** AGENTS.md should instruct the agent to read episodic files on session start. The instruction is in the system prompt (Avenue 1).

**Avenue chain example:**
```
Agent starts a task in the repository:
  Avenue 1 fires: AGENTS.md loaded with rules and trigger section
    → tells agent: "find .gab.jsonld, use jq for mode constraints"
  Avenue 3 activates: .agents/skills/ scanned, context-gathering matches
    → loads full skill content
  Avenue 5 available: agent runs jq via bash
  Avenue 6 available: agent reads .integration.md

Result: 4 avenues fire — adequate coverage despite missing path rules
```

**Key risk:** AGENTS.md has a 32KB silent truncation limit. If content is too large, rules and triggers at the end are silently dropped. Keep AGENTS.md concise — put detail in skills, not in the system prompt.

---

### Gemini CLI (4/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | GEMINI.md | Medium | Model sometimes explicitly refuses instructions — documented P0 issue |
| 2. Path Rules | N/A | N/A | No native path-scoped rules |
| 3. Skills | Extensions with `skills/` | Low | Extension system, not standalone skills. Must be packaged as extensions. |
| 4. @import | N/A | N/A | No @import support |
| 5. JSON-LD/jq | Bash access | Medium | Can run jq via shell |
| 6. .integration.md | File read | High | Markdown reads work well when the model cooperates |
| 7. Episodic | File read | Medium | No auto-memory |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `GEMINI.md` (system prompt content)
- `rules/static/` → Inlined into `GEMINI.md` (Gemini has no separate rules directory)
- `protocols/` → `.gemini/extensions/*/skills/` (packaged as extension skills)
- `skills/` → `.gemini/extensions/*/skills/` (merged with protocols)

**What gets added from .1merge/.1gemini_merge/:**
- Extension definitions (Gemini's equivalent of skills, but bundled differently)
- Gemini-specific knowledge about extension architecture
- Override protocols adapted for Gemini's tool access patterns

**Compensation for missing avenues:**
- **No path rules (Avenue 2):** Inline all rules in GEMINI.md. Use stronger, more explicit language since Gemini has been documented to refuse instructions (the model may say "I don't follow .gemini instructions").
- **No @import (Avenue 4):** Extensions must be self-contained with all necessary context.
- **No auto-memory (Avenue 7):** GEMINI.md should instruct episodic file reads explicitly.
- **Model refusal (Avenue 1 degraded):** This is Gemini CLI's unique failure mode. The model itself sometimes refuses to follow GEMINI.md. Compensate by putting the most critical rules as early in GEMINI.md as possible, and by duplicating critical rules inside extension skills so they're reinforced when skills load.

**Avenue chain example:**
```
Agent starts a task:
  Avenue 1 fires: GEMINI.md loaded (but model may partially ignore)
    → tells agent about jq instructions and extension usage
  Avenue 3 partially activates: extension skill triggered
    → loads skill content with embedded rules (compensates for Avenue 1 weakness)
  Avenue 5 available: agent runs jq via shell
  Avenue 6 available: agent reads .integration.md

Result: 3-4 avenues fire — but Avenue 1 reliability is lower than other tools
```

**Key risk:** Gemini's model-level instruction refusal is unique and unpredictable. No amount of prompt engineering fully solves it. Design for graceful degradation — the system must work even if GEMINI.md is partially ignored.

---

### OpenCode (3-4/8 Avenues, Model-Dependent)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | AGENTS.md | Model-dependent | Claude Opus follows well; GPT-5.2 largely ignores |
| 2. Path Rules | N/A | N/A | No native path rules |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | Bash access | Model-dependent | Works when model cooperates |
| 6. .integration.md | File read | High | Markdown reads are model-independent |
| 7. Episodic | File read | Medium | No auto-memory, must be instructed |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `AGENTS.md` (system prompt — shared format with Codex)
- `rules/static/` → Inlined into `AGENTS.md` (no separate rules mechanism)

**What gets added from .1merge/.1opencode_merge/:**
- Model-specific instructions (different phrasings for Claude vs GPT backends)
- Knowledge about OpenCode's behavior differences per backend model

**Compensation for missing avenues:**
- **No path rules (Avenue 2):** All rules inline in AGENTS.md.
- **No skills (Avenue 3):** All protocols must be in AGENTS.md or the agent must be told to read protocol files directly. This is the biggest gap — no progressive disclosure.
- **No @import (Avenue 4):** AGENTS.md must instruct direct file reads.
- **Model-dependent adherence (Avenue 1 degraded):** When using GPT-5.2 as backend, AGENTS.md instructions may be largely ignored. The system still works via file reads (Avenue 6, 8) if the agent reads them — but it may not read them without Avenue 1 triggering the read.

**Avenue chain example (Claude backend):**
```
Agent starts a task:
  Avenue 1 fires: AGENTS.md loaded, Claude Opus follows instructions
    → tells agent to read .integration.md, run jq
  Avenue 5 activated: agent runs jq, gets mode constraints
  Avenue 6 activated: agent reads .integration.md

Result: 3 avenues fire — adequate for Claude backend
```

**Avenue chain example (GPT backend):**
```
Agent starts a task:
  Avenue 1 partially fires: AGENTS.md loaded, GPT-5.2 may ignore parts
    → agent may or may not follow jq/read instructions
  Avenue 6 available: IF agent reads .integration.md, it works
  Avenue 8 available: IF agent reads 0AGNOSTIC.md, it works

Result: 1-2 avenues fire — unreliable with GPT backend
```

**Key risk:** OpenCode's effectiveness is almost entirely determined by which backend model is used. With Claude, it works. With GPT, it's unreliable. Recommend Claude as the backend model.

---

### Cursor (2-3/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.cursorrules` / `.cursor/rules/` always-type | Medium | IDE-managed, may conflict with Cursor's own system instructions |
| 2. Path Rules | `.cursor/rules/*.mdc` with auto-attach globs | High | Native glob-based auto-attachment — Cursor's strongest avenue |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | N/A | N/A | No bash access in most modes |
| 6. .integration.md | File read (limited) | Medium | Can read files but only when agent decides to |
| 7. Episodic | N/A | N/A | No persistent memory system |
| 8. 0AGNOSTIC.md | File read (limited) | Medium | Available but agent must decide to read it |

**What gets synced from .0agnostic/:**
- `rules/static/` → `.cursor/rules/*.mdc` with `alwaysApply: true` metadata (always loaded)
- `rules/dynamic/` → `.cursor/rules/*.mdc` with `globs: ["pattern"]` metadata (auto-attached by file pattern)
- `0AGNOSTIC.md` → `.cursorrules` (system prompt content, simplified)

**What gets added from .1merge/.1cursor_merge/:**
- Format transformations (`.md` → `.mdc` with Cursor metadata headers)
- Cursor Composer-specific rules
- `.mdc` templates for creating new rules

**Format transformation (.md → .mdc):**
```
Source (.0agnostic/rules/dynamic/research_context.md):
---
paths: layer_-1_research/**
---
# Research context rule...

Target (.cursor/rules/research_context.mdc):
---
description: Research context rule
globs: ["layer_-1_research/**"]
alwaysApply: false
---
# Research context rule...
```

**Compensation for missing avenues:**
- **No skills (Avenue 3):** Protocols must be inlined in `.mdc` rules or the system prompt. No progressive disclosure — everything loads immediately or not at all.
- **No @import (Avenue 4):** Rules must be self-contained. No chaining.
- **No bash/jq (Avenue 5):** JSON-LD is inaccessible. All AALang constraints must be pre-transpiled into `.mdc` rules or the system prompt.
- **No episodic memory (Avenue 7):** No session continuity. Each session starts from rules and system prompt only.

**Avenue chain example:**
```
Agent opens a file in layer_-1_research/:
  Avenue 2 fires: research_context.mdc auto-attaches
    → tells agent about research workflow requirements
  Avenue 1 present: .cursorrules has general rules
  Avenue 6 possible: agent MAY read .integration.md if instructed in the .mdc rule

Result: 2 avenues fire reliably — Cursor depends heavily on path rules
```

**Key risk:** Cursor has no progressive disclosure. Everything must be in `.mdc` rules or the system prompt. This means static context is larger (all protocols inline) and there's no on-demand loading. Keep `.mdc` rules focused and concise to avoid overwhelming the context.

**Cursor's unique strength:** Four activation modes (Always, Auto-Attach, Agent Requested, Manual) give more granular control over WHEN rules load than most other tools. Use auto-attach extensively to compensate for missing skills.

---

### Aider (3/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.aider/conventions.md` or `CONVENTIONS.md` | Medium | Loaded at session start, limited length |
| 2. Path Rules | N/A | N/A | No path-scoped rules |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | Bash access | Medium | Can run shell commands |
| 6. .integration.md | File read | High | Markdown reads work well with capable models |
| 7. Episodic | N/A | N/A | No persistent memory system |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `CONVENTIONS.md` or `.aider/conventions.md` (system prompt, heavily condensed)
- `rules/static/` → Inlined into conventions file (Aider has no separate rules mechanism)

**What gets added from .1merge/.1aider_merge/:**
- Conventions file with Aider-specific formatting
- Rules condensed for Aider's more limited context handling

**Compensation for missing avenues:**
- **No path rules (Avenue 2):** All rules inline in conventions. No path-scoping — every rule loads every time.
- **No skills (Avenue 3):** No progressive disclosure. All protocols must be condensed into conventions or the agent must be told to read files.
- **No @import (Avenue 4):** Conventions must be self-contained.
- **No episodic memory (Avenue 7):** No session continuity between Aider sessions.

**Avenue chain example:**
```
Agent starts an Aider session:
  Avenue 1 fires: conventions.md loaded
    → tells agent about jq instructions and file reading
  Avenue 5 available: agent can run jq via shell
  Avenue 6 available: agent can read .integration.md

Result: 3 avenues available — heavily dependent on Avenue 1 quality
```

**Key risk:** Aider's conventions file is the single point of failure. If the conventions are too long, Aider may not follow them well. If too short, they miss critical context. Aider works best for code-focused tasks where the conventions can be kept lean. For complex context-heavy workflows (entity creation, stage management), other tools are more appropriate.

---

### Windsurf (2-3/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.windsurfrules` | Medium | Loaded at session start |
| 2. Path Rules | N/A | N/A | No path-scoped rules |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | Limited bash | Low | Bash access more restricted than CLI tools |
| 6. .integration.md | File read | Medium | Can read files but less autonomous than CLI tools |
| 7. Episodic | N/A | N/A | No persistent memory |
| 8. 0AGNOSTIC.md | File read | Medium | Available but agent must decide to read |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `.windsurfrules` (system prompt, simplified)
- `rules/static/` → Inlined into `.windsurfrules`

**Compensation strategy:** Similar to Cursor but without path rules. System prompt is the primary avenue. Keep it focused and critical-only.

---

### Junie / JetBrains AI (2-3/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.junie/guidelines.md` | Medium | JetBrains-specific format |
| 2. Path Rules | N/A | N/A | No path-scoped rules |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | Limited | Low | IDE environment, bash less accessible |
| 6. .integration.md | File read | Medium | Can read project files |
| 7. Episodic | N/A | N/A | No persistent memory |
| 8. 0AGNOSTIC.md | File read | Medium | Available |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `.junie/guidelines.md` (system prompt in Junie format)
- `rules/static/` → Inlined into guidelines

**Compensation strategy:** Similar to Aider — system prompt is primary. Junie is IDE-embedded with limited autonomous capabilities.

---

### Summary: Avenue Coverage Across All Tools

| Avenue | Claude Code | Codex CLI | Gemini CLI | OpenCode | Cursor | Aider | Windsurf | Junie |
|--------|:----------:|:---------:|:----------:|:--------:|:------:|:-----:|:--------:|:-----:|
| 1. System Prompt | High | Medium | Medium* | Model-dep | Medium | Medium | Medium | Medium |
| 2. Path Rules | High | -- | -- | -- | High | -- | -- | -- |
| 3. Skills | Medium | Medium | Low | -- | -- | -- | -- | -- |
| 4. @import | High | -- | -- | -- | -- | -- | -- | -- |
| 5. JSON-LD/jq | Medium | Medium | Medium | Model-dep | -- | Medium | Low | Low |
| 6. .integration.md | High | High | High | High | Medium | High | Medium | Medium |
| 7. Episodic | High | Medium | Medium | Medium | -- | -- | -- | -- |
| 8. 0AGNOSTIC.md | High | High | High | High | Medium | High | Medium | Medium |
| **Active Avenues** | **8/8** | **5/8** | **4/8** | **3-4/8** | **2-3/8** | **3/8** | **2-3/8** | **2-3/8** |

*Gemini CLI's Avenue 1 is degraded due to documented model-level instruction refusal.

**Reliability ranking** (based on avenue coverage and effectiveness):
1. **Claude Code** — Full coverage, all avenues native or via tools
2. **Codex CLI** — Good coverage, skills + bash compensate for missing path rules
3. **Gemini CLI** — Moderate coverage, but Avenue 1 unreliability is a significant weakness
4. **OpenCode** — Model-dependent, excellent with Claude backend, poor with GPT
5. **Cursor** — Path rules are strong, but no skills/jq/episodic severely limits depth
6. **Aider** — System prompt + bash, minimal native integration
7. **Windsurf** — Similar to Cursor but without path rules
8. **Junie** — IDE-embedded, minimal autonomous capability

---

## AALang/GAB Integration

AALang agent definitions (`.gab.jsonld`) are the design-time source of truth for agent behavior. They integrate through four independent avenues:

### Redundancy Chain for AALang

```
1. CLAUDE.md jq instructions (Avenue 1 + 5)
   System prompt tells agent: "Find nearest .gab.jsonld, run jq"
   Agent gets: mode constraints, skill mappings, transitions
   ↓ if jq not run...

2. .integration.md (Avenue 6)
   Transpiled markdown next to .gab.jsonld
   Agent reads: mode table, constraints, skill mappings
   Same information, no tool call needed
   ↓ if .integration.md not read...

3. Skills reference integration summaries (Avenue 3 + 6)
   SKILL.md content says: "Check mode constraints in .integration.md"
   Agent reads integration summary when skill is invoked
   ↓ if skill not invoked...

4. Path rules point to AALang files (Avenue 2 + 5)
   .claude/rules/research-context.md auto-loads
   Content says: "Find .gab.jsonld, read .integration.md"
   Automatic trigger — no agent decision needed
```

**If ANY one of these four fires → agent gets AALang constraints.**

### Per-Tool AALang Access

| Tool | jq Access | .integration.md | Path Rules → AALang | Skills → AALang |
|------|-----------|-----------------|--------------------|----|
| Claude Code | Yes (Bash) | Yes (Read) | Yes (native) | Yes (native) |
| Codex CLI | Yes (Bash) | Yes (file read) | No | Yes (.agents/skills/) |
| Gemini CLI | Yes (Bash) | Yes (file read) | No | Partial (extensions) |
| OpenCode | Yes (Bash) | Yes (file read) | No | No |
| Cursor | No | Partial | Yes (.mdc) | No |
| Aider | Yes (Bash) | Yes (file read) | No | No |

Tools without path rules or skills rely on system prompt jq instructions (Avenue 1+5) and direct .integration.md reads (Avenue 6) for AALang access.

---

## How the System Prompt Ties Everything Together

The system prompt is the switchboard — it doesn't contain detailed content, but it connects to all avenues:

```markdown
## Triggers (~10 lines)
| Situation              | Action                               |
|------------------------|--------------------------------------|
| New task               | /context-gathering                   |
| Creating entities      | /entity-creation                     |
| Working stages         | /stage-workflow                      |
| Ending session         | /handoff-creation                    |
| Modifying AI context   | Show diagram first (inline rule)     |

## Context Loading (~15 lines)
1. Find nearest .gab.jsonld → jq for mode constraints
2. Read matching .integration.md
3. Check .claude/rules/ for path-specific rules
4. Check .claude/skills/ for available procedures
5. Read episodic_memory/index.md if resuming

## @imports (~5 lines)
@knowledge/entity_lifecycle/INSTANTIATION_GUIDE.md
@knowledge/layer_stage_system/OVERVIEW.md
```

**Total: ~30-40 lines** — but these connect to ALL 8 avenues.

---

## The "Any-One-Fires" Resilience Model

```
Scenario: Agent needs to follow research workflow

Avenue 1 (system prompt): Trigger table says "use /stage-workflow"     → ✓ or ✗
Avenue 2 (path rule):     research-context.md auto-loads in research/  → ✓ or ✗
Avenue 3 (skill):         /stage-workflow description matches          → ✓ or ✗
Avenue 5 (JSON-LD):       Agent runs jq, gets ResearchMode constraints → ✓ or ✗
Avenue 6 (.integration.md): Agent reads mode table                     → ✓ or ✗

Each avenue has independent ~60-80% chance of firing.
Probability of ALL five failing: 0.4^5 = 1.0%
Probability of AT LEAST ONE firing: 99%
```

Compare to a single-avenue system:
```
Only Avenue 3 (skill): /stage-workflow description matches → ✓ or ✗
Probability of firing: ~37-80% (depending on description quality)
Probability of failure: 20-63%
```

**Multi-avenue redundancy reduces context loading failure from ~40% to ~1%.**

---

## Design Principles

1. **Every piece of context must be reachable through at least 3 independent avenues**
2. **Static avenues (system prompt, path rules) are the foundation** — they fire without agent decision
3. **Dynamic avenues (skills, @imports, jq) provide depth** — full content when needed
4. **The system prompt is a switchboard, not a textbook** — pointers only, content elsewhere
5. **Tools with fewer avenues get more content inlined** — compensate for missing mechanisms
6. **Graceful degradation is mandatory** — the system works with partial avenue coverage

---

*Multi-avenue redundancy documentation for the 0Agnostic System*
*Created: 2026-02-16*
