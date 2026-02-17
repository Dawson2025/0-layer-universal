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

### Claude Code (Best Support)

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

**Active avenues: 8/8** — Full coverage. All avenues supported natively or via tool calls.

### Codex CLI

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

**Active avenues: 5/8** — No path rules, no @imports. Compensate via AGENTS.md inline rules and skills.

### Gemini CLI

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | GEMINI.md | Medium | Model sometimes explicitly refuses instructions |
| 2. Path Rules | N/A | N/A | No native path-scoped rules |
| 3. Skills | Extensions with `skills/` | Low | Extension system, not standalone skills |
| 4. @import | N/A | N/A | No @import support |
| 5. JSON-LD/jq | Bash access | Medium | Can run jq |
| 6. .integration.md | File read | High | Markdown reads work well |
| 7. Episodic | File read | Medium | No auto-memory |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**Active avenues: 4/8** — Weakest support. Compensate by inlining more content in GEMINI.md and using extensions for skills.

### OpenCode

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | AGENTS.md | Model-dependent | Claude follows well, GPT-5.2 ignores |
| 2. Path Rules | N/A | N/A | No native path rules |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | Bash access | Medium | Model-dependent |
| 6. .integration.md | File read | High | Markdown works |
| 7. Episodic | File read | Medium | No auto-memory |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**Active avenues: 3-4/8** — Heavily dependent on model choice. Use Claude as the backend model for best adherence.

### Cursor

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.cursorrules` / `.cursor/rules/` | Medium | IDE-managed, may conflict with Cursor's own instructions |
| 2. Path Rules | `.cursor/rules/*.mdc` with auto-attach | High | Native glob-based auto-attachment |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | N/A | N/A | No bash access |
| 6. .integration.md | File read (limited) | Medium | Can read files but less autonomous |
| 7. Episodic | N/A | N/A | No persistent memory |
| 8. 0AGNOSTIC.md | File read (limited) | Medium | Can read but less autonomous |

**Active avenues: 2-3/8** — Relies heavily on path rules (.mdc) and system prompt. No skills, no @imports, no jq.

### Aider

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.aider/conventions.md` | Medium | Loaded at session start |
| 2. Path Rules | N/A | N/A | No path rules |
| 3. Skills | N/A | N/A | No skill system |
| 4. @import | N/A | N/A | No @import |
| 5. JSON-LD/jq | Bash access | Medium | Can run jq |
| 6. .integration.md | File read | High | Markdown works well |
| 7. Episodic | N/A | N/A | No persistent memory |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**Active avenues: 3/8** — Minimal native integration. Compensate by inlining critical content in conventions.md.

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
