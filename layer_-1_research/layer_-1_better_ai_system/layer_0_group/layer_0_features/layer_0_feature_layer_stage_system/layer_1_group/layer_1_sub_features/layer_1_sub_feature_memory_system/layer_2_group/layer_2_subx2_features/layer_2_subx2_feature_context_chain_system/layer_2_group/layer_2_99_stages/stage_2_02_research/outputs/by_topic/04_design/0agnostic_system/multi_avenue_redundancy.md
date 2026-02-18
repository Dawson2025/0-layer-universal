# Multi-Avenue Redundancy

## Purpose

How all context chaining avenues link together to ensure context is reliably loaded — even when individual avenues fail. This network is the **Avenue Web** (also called the **Web of Avenues** and `multi_avenue_redundancy_web`): a graph of context paths and reference paths that reinforce each other. Covers effectiveness per tool, how AALang/GAB and JSON-LD integrate, how the system prompt ties everything together, and the "any-one-fires" resilience model.

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

**Every avenue points to at least one other avenue.** The system is an **Avenue Web**, not a single chain.

---

## JSON-LD Traversal Methods Beyond jq

The current system uses jq-via-bash as the primary JSON-LD traversal mechanism (Avenue 5). Research reveals 6 additional methods that expand tool compatibility and provide fallbacks when jq is unavailable.

Our `.gab.jsonld` files use a flat `@graph` array with prefixed types (`gab:Mode`, `gab:Actor`, etc.), typically 500-1400 lines. Core operations: extract nodes by `@type`, get nodes by `@id`, follow inter-node references, extract constraints and skill mappings.

### Method Comparison

| Method | Installation | Universal Compatibility | Precision | Context Window Cost | Best For |
|--------|-------------|------------------------|-----------|-------------------|----------|
| **Native JSON parsing** | None | Highest (any scripting lang) | High (for flat @graph) | None (runs externally) | Maximum compatibility, simple queries |
| **LLM direct reading** | None | Highest (every tool) | Medium | High (full file in context) | Tools with no execution, exploration |
| **JS libraries (jsonld.js)** | `npm install jsonld` | Medium (needs Node.js) | High | None (runs externally) | Framing, expansion, context resolution |
| **Python libraries (rdflib/PyLD)** | `pip install rdflib` | Medium (needs Python) | High | None (runs externally) | SPARQL queries, Aider/Python workflows |
| **MCP server (custom)** | Custom build | High (any MCP client) | High | None (tool returns results) | Long-term standardization |
| **SPARQL/GraphQL-LD** | Library install | Medium | Highest | None (runs externally) | Complex multi-hop queries |

---

### Method 1: Native JSON Parsing (No Dependencies)

Since JSON-LD is valid JSON, any scripting language can traverse `@graph` arrays without JSON-LD-specific libraries. This is the most universally accessible method.

**jq (current approach)**:
```bash
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' file.gab.jsonld
```

**Node.js (no install needed)**:
```javascript
const doc = JSON.parse(require('fs').readFileSync('file.gab.jsonld'));
const modes = doc['@graph'].filter(n => n['@type'] === 'gab:Mode');
```

**Python (no install needed)**:
```python
import json
with open('file.gab.jsonld') as f:
    doc = json.load(f)
modes = [n for n in doc['@graph'] if n.get('@type') == 'gab:Mode']
```

**Limitations**: Does not resolve `@context` prefixes to full IRIs, does not handle cross-document `@id` references, does not support JSON-LD expansion/compaction. These limitations are irrelevant for our flat `@graph` structure with consistent prefixed types.

**Compatible tools**: Every tool with bash, Node.js, or Python access.

---

### Method 2: LLM Direct Reading

The AI agent reads the `.gab.jsonld` file with a file-read tool and extracts information using its language understanding. This is the universal fallback.

**Strengths**: Zero tooling required; LLMs understand JSON structure well; can follow `@id` references mentally; understands semantic meaning of fields like `constraints` and `purpose`.

**Weaknesses**: High context window consumption (a 1400-line file uses significant tokens); accuracy degrades on large files; no programmatic precision (results may vary between invocations); cannot efficiently cross-reference multiple files.

The `.integration.md` files exist precisely to optimize this method -- they provide the LLM a markdown summary without processing raw JSON-LD.

**Compatible tools**: Every AI coding tool (universal).

---

### Method 3: JavaScript Libraries (jsonld.js, Comunica)

**jsonld.js** (Digital Bazaar, v9.0.0) -- The W3C reference implementation. The `frame()` method is purpose-built for extracting typed nodes:

```javascript
const jsonld = require('jsonld');
const doc = JSON.parse(fs.readFileSync('file.gab.jsonld'));
const frame = { "@type": "gab:Mode" };
const result = await jsonld.frame(doc, frame);
```

**Comunica** (`@comunica/query-sparql`) -- A full SPARQL query engine for JavaScript that queries JSON-LD files directly, also supports GraphQL-LD queries.

| Tool | Can Use JS Libraries? | How |
|------|----------------------|-----|
| Cursor | Yes | Terminal / VS Code extensions |
| Windsurf | Yes | Terminal (VS Code-based) |
| Cline | Yes | Terminal access |
| Claude Code | Yes | `node -e '...'` via Bash tool |
| Copilot (VS Code) | No | No terminal execution |

---

### Method 4: Python Libraries (rdflib, PyLD)

**rdflib** (v6.0.1+) -- JSON-LD support built in. Full SPARQL query support:

```python
from rdflib import Graph
g = Graph()
g.parse('file.gab.jsonld', format='json-ld')
for mode in g.query('SELECT ?id ?purpose WHERE { ?id a <https://aalang.dev/gab/Mode> ; <https://layer-stage.dev/context/purpose> ?purpose }'):
    print(mode)
```

**PyLD** (Digital Bazaar) -- Python reference implementation with `frame()` support identical to jsonld.js.

| Tool | Can Use Python? | How |
|------|----------------|-----|
| Aider | Yes | Native Python runtime |
| Claude Code | Yes | `python3 -c '...'` via Bash |
| Cursor / Windsurf | Yes | Terminal commands |
| Open Interpreter | Yes | Native Python execution |
| ChatGPT Code Interpreter | Yes | Sandboxed Python |

---

### Method 5: Custom MCP Server

No JSON-LD-specific MCP server currently exists. Related servers (mcp-rdf-explorer, GraphDB MCP, SPARQL MCP) work with Turtle or SPARQL endpoints, not `.jsonld` files directly.

A purpose-built MCP server could expose:
- `gab_list_modes(file)` -- Return all Mode nodes
- `gab_get_node(file, id)` -- Return a node by `@id`
- `gab_get_constraints(file, mode_id)` -- Return constraints for a mode
- `gab_get_skills(file)` -- Return skill mappings
- `gab_get_transitions(file, mode_id)` -- Return mode transition graph

**Compatible tools**: Any MCP client (Claude Code, Cursor, Windsurf, Cline, Copilot).

This is the most forward-looking option -- every MCP-compatible tool would gain GAB traversal without per-tool configuration.

---

### Method 6: SPARQL / GraphQL-LD (Lightweight)

**JSON-LD Framing** is the most native query mechanism -- a frame acts as a "query by example":

```json
{
  "@type": "gab:Mode",
  "purpose": {},
  "constraints": {},
  "contains": { "@type": "gab:Persona" }
}
```

This extracts all Mode nodes with their purpose, constraints, and nested Persona nodes.

**Comunica SPARQL** queries JSON-LD files directly without a triplestore:

```javascript
const { QueryEngine } = require('@comunica/query-sparql');
const engine = new QueryEngine();
const result = await engine.query(`
  SELECT ?id ?purpose WHERE {
    ?id a <https://aalang.dev/gab/Mode> ;
        <https://layer-stage.dev/context/purpose> ?purpose .
  }
`, { sources: [{ type: 'file', value: 'file.gab.jsonld' }] });
```

---

### Recommended Approach per Tool

| Tool | Primary Method | Fallback |
|------|---------------|----------|
| **Claude Code** | jq via Bash (current) | Native JSON parsing, LLM direct reading |
| **Cursor / Windsurf** | Native JSON parsing (Node.js) | LLM direct reading, .integration.md |
| **Aider** | Native JSON parsing (Python) | LLM direct reading |
| **Codex CLI** | Native JSON parsing | LLM direct reading |
| **Gemini CLI** | Native JSON parsing | LLM direct reading |
| **Copilot (VS Code)** | LLM direct reading | .integration.md |
| **Cline / Roo Code** | Native JSON parsing | LLM direct reading |
| **Junie (JetBrains)** | LLM direct reading | .integration.md |
| **claude.ai (web)** | LLM direct reading | .integration.md |
| **All MCP clients** | Custom MCP server (future) | Native JSON parsing |

The three-avenue approach in AALang context loading remains sound: (1) jq for precision, (2) .integration.md for efficient LLM reading, (3) raw file reading as last resort. Native JSON parsing should be documented as the universal portable alternative to jq.

### JSON-LD Traversal Sources

- [jsonld.js -- Digital Bazaar (GitHub)](https://github.com/digitalbazaar/jsonld.js)
- [jsonld npm package](https://www.npmjs.com/package/jsonld)
- [PyLD -- Digital Bazaar (GitHub)](https://github.com/digitalbazaar/pyld)
- [RDFLib (GitHub)](https://github.com/RDFLib/rdflib)
- [Comunica SPARQL (GitHub)](https://github.com/comunica/comunica)
- [jsonld-streaming-parser.js (GitHub)](https://github.com/rubensworks/jsonld-streaming-parser.js/)
- [mcp-rdf-explorer (GitHub)](https://github.com/emekaokoye/mcp-rdf-explorer)
- [JSON-LD 1.1 Framing Specification (W3C)](https://w3c.github.io/json-ld-framing/)
- [GraphQL-LD (Comunica)](https://comunica.dev/docs/query/advanced/graphql_ld/)

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

### Cursor IDE (3-4/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.cursorrules` / `.cursor/rules/` always-type | Medium | IDE-managed, may conflict with Cursor's own system instructions |
| 2. Path Rules | `.cursor/rules/*.mdc` with auto-attach globs | High | Native glob-based auto-attachment with four activation modes |
| 3. Skills | Agent Skills (`SKILL.md`, v2.4+) | Medium | Progressive disclosure — description at start, full body on demand |
| 4. @import | N/A | N/A | No @import mechanism |
| 5. JSON-LD/jq | N/A | N/A | No bash access in IDE mode |
| 6. .integration.md | File read (limited) | Medium | Can read files but only when agent decides to |
| 7. Episodic | N/A | N/A | No persistent memory system (Notepads are session-scoped) |
| 8. 0AGNOSTIC.md | File read (limited) | Medium | Available but agent must decide to read it |

**What gets synced from .0agnostic/:**
- `rules/static/` → `.cursor/rules/*.mdc` with `alwaysApply: true` metadata (always loaded)
- `rules/dynamic/` → `.cursor/rules/*.mdc` with `globs: ["pattern"]` metadata (auto-attached by file pattern)
- `0AGNOSTIC.md` → `.cursorrules` (system prompt content, simplified)
- `protocols/` → `.cursor/skills/*/SKILL.md` (progressive disclosure, v2.4+)

**What gets added from .1merge/.1cursor_merge/:**
- Format transformations (`.md` → `.mdc` with Cursor metadata headers)
- Cursor Composer-specific rules
- `.mdc` templates for creating new rules
- Team Rules Dashboard configuration (enterprise)

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
- **No @import (Avenue 4):** Rules must be self-contained. No chaining.
- **No bash/jq (Avenue 5):** JSON-LD is inaccessible in IDE mode. All AALang constraints must be pre-transpiled into `.mdc` rules or the system prompt.
- **No episodic memory (Avenue 7):** No session continuity. Each session starts from rules and system prompt only. Notepads provide some reusable context but are not auto-loaded.

**Avenue chain example:**
```
Agent opens a file in layer_-1_research/:
  Avenue 2 fires: research_context.mdc auto-attaches (glob match)
    → tells agent about research workflow requirements
  Avenue 1 present: .cursorrules has general rules
  Avenue 3 possible: Agent Skill description matches research context
    → loads full SKILL.md with protocol steps
  Avenue 6 possible: agent MAY read .integration.md if instructed in the .mdc rule

Result: 2-3 avenues fire reliably — Cursor depends heavily on path rules and skills
```

**Key risk:** No bash access means JSON-LD (Avenue 5) is fully inaccessible in IDE mode. Everything must be pre-transpiled. The four activation modes (Always, Auto-Attach, Agent Requested, Manual) partially compensate by providing more granular control over WHEN rules load.

**Cursor's unique strengths:**
- **Four activation modes** (Always, Auto-Attach, Agent Requested, Manual) give more granular control over when rules load than most other tools
- **Semantic codebase indexing** — vector search via Turbopuffer gives automatic codebase awareness without reading every file
- **Agent Requested rules** — AI evaluates rule descriptions to decide relevance, similar to skill matching but at the rule level

---

### Cursor CLI (6-7/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.cursorrules` / `.cursor/rules/` + `AGENTS.md` + `CLAUDE.md` | High | Reads `.cursor/rules/*.mdc`, AGENTS.md, and CLAUDE.md at repo root |
| 2. Path Rules | `.cursor/rules/*.mdc` with auto-attach globs | High | Same glob-based auto-attachment as IDE, four activation modes |
| 3. Skills | Agent Skills (`SKILL.md`, v2.4+) | Medium | Progressive disclosure — description first, body on demand |
| 4. @import | `@file` / `@folder` references | Medium | Supports `@file` and `@folder` inline references but not `@Web` or `@Docs` |
| 5. JSON-LD/jq | Bash access (with approval gate) | Medium | Can run jq via shell, requires Y/N approval per command |
| 6. .integration.md | File read | High | Full file read access, markdown format works well |
| 7. Episodic | Session management (`cursor-agent resume`) | Medium | Session history via `cursor-agent ls` / `resume`, but no auto-memory |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**What gets synced from .0agnostic/:**
- `rules/static/` → `.cursor/rules/*.mdc` with `alwaysApply: true` (always loaded)
- `rules/dynamic/` → `.cursor/rules/*.mdc` with `globs: ["pattern"]` (auto-attached)
- `0AGNOSTIC.md` → `.cursorrules` + `AGENTS.md` (system prompt content)
- `protocols/` → `.cursor/skills/*/SKILL.md` (progressive disclosure)
- `skills/` → `.cursor/skills/` (direct copy)

**What gets added from .1merge/.1cursor_cli_merge/:**
- `.cursor/cli.json` (granular permission config: allow/deny/prompt per operation)
- Protocol overrides adapted for CLI's approval-gated bash execution
- CI/CD headless mode configurations (`-p` flag, `--output-format` settings)
- Cloud agent handoff patterns

**Compensation for weaknesses:**
- **Partial @import (Avenue 4):** `@file` and `@folder` work for explicit references, but no `@Web`, `@Docs`, or chain-depth semantics. Skills and rules must handle most context chaining.
- **Session-only episodic (Avenue 7):** `cursor-agent resume` provides session continuity but there is no auto-memory like Claude Code's MEMORY.md. System prompt should instruct explicit episodic file reads.

**Avenue chain example:**
```
Agent starts a task in the repository:
  Avenue 1 fires: .cursorrules + AGENTS.md loaded, rules section parsed
    → tells agent: "find .gab.jsonld, use jq for mode constraints"
  Avenue 2 fires: .mdc rules auto-attach for matching file patterns
    → path-specific context loaded automatically
  Avenue 3 activates: Agent Skill description matches task context
    → loads full SKILL.md content with protocol steps
  Avenue 5 available: agent runs jq via bash (with Y/N approval)
  Avenue 6 available: agent reads .integration.md

Result: 5 avenues fire — significantly more coverage than IDE mode
```

**Key risk:** Every bash command requires explicit Y/N approval in interactive mode (or `--force` in headless). This adds friction to Avenue 5 (jq) usage. In CI/CD headless mode, permissions must be pre-configured in `.cursor/cli.json`.

**Cursor CLI's unique strengths:**
- **Multi-model switching** — supports Sonnet 4, GPT-5, Opus 4.1, Grok, and auto-selection within the same session
- **Cloud Agents** — push conversations to background cloud agents, continue on web/mobile at cursor.com/agents
- **Three output formats** — text, JSON, and NDJSON streaming make it natively scriptable for CI/CD
- **Plan/Ask modes** — `--mode=plan` for research-first planning, `--mode=ask` for read-only exploration
- **Shared ecosystem** — inherits MCP servers, rules, and user preferences from the Cursor IDE automatically

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

### Amazon Q Developer (3-4/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.amazonq/rules/` with priority levels | Medium | Priority-based conflict resolution between overlapping rules |
| 2. Path Rules | N/A | N/A | No path-scoped rules; per-session toggle activates rules selectively |
| 3. Skills | Custom agents with `file://` glob resources | Low-Medium | Custom agents can dynamically include rule files via glob patterns |
| 4. @import | N/A | N/A | No @import mechanism |
| 5. JSON-LD/jq | Limited bash | Low | IDE environment, bash access more restricted |
| 6. .integration.md | File read | Medium | Can read project files when agent decides to |
| 7. Episodic | N/A | N/A | No persistent memory system |
| 8. 0AGNOSTIC.md | File read | Medium | Available but agent must decide to read |

**What gets synced from .0agnostic/:**
- `rules/static/` → `.amazonq/rules/*.md` with priority metadata (always loaded when toggled on)
- `0AGNOSTIC.md` → Project rules file (system prompt, simplified for Amazon Q format)

**What gets added from .1merge/.1amazonq_merge/:**
- Priority level metadata for conflict resolution between rules
- Security scanning rule templates (Amazon Q's unique code vulnerability detection)
- AWS-specific rules for Lambda, CDK, and other AWS service patterns
- Custom agent configurations with `file://` glob resource patterns

**Compensation for missing avenues:**
- **No path rules (Avenue 2):** Rules use explicit priority levels instead of path scoping. Per-session toggle lets users activate/deactivate rules manually, but there is no automatic file-pattern triggering.
- **No skills (Avenue 3):** Custom agents with `file://` glob resources provide partial skill-like behavior — dynamically including rule files matching glob patterns like `file://.amazonq/rules/**/*.md`.
- **No @import (Avenue 4):** Rules must be self-contained.
- **No episodic memory (Avenue 7):** No session continuity. Each session starts from rules only.

**Avenue chain example:**
```
Agent starts a coding task:
  Avenue 1 fires: .amazonq/rules/ loaded (priority-ordered)
    → highest-priority rules take precedence over lower ones
  Avenue 3 partial: custom agent includes matching rule files via globs
  Avenue 6 possible: agent MAY read .integration.md if instructed in rules

Result: 2-3 avenues fire — heavily dependent on rule quality and priority ordering
```

**Key risk:** Amazon Q is primarily AWS-focused with strong AWS service integration but weaker general-purpose context delivery. The per-session rule toggle means context depends on user configuration each session — no guaranteed automatic loading.

**Amazon Q's unique strengths:**
- **Priority-based conflict resolution** — explicit priority levels handle overlapping rules more predictably than implicit nesting
- **Security scanning integration** — scans code for vulnerabilities (exposed credentials, log injection) as part of the AI workflow
- **`@workspace` with 100K character context** — large context budget with automatic relevance selection
- **Per-session rule toggling** — rules can be checked/unchecked for individual sessions

---

### Cline / Roo Code (4-5/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.clinerules` / `.roo/rules/` + per-mode rule files | High | Mode-specific instructions with tool restrictions per mode |
| 2. Path Rules | Per-mode rule files (`.roo/rules-{mode-slug}/`) | Medium-High | Rules scoped to modes rather than file paths, but modes map to task types |
| 3. Skills | N/A | N/A | No skill system; Memory Bank files serve a similar role |
| 4. @import | N/A | N/A | No @import mechanism |
| 5. JSON-LD/jq | Bash access | Medium | Can run shell commands via terminal |
| 6. .integration.md | File read | High | Markdown reads work well |
| 7. Episodic | Memory Bank system | High | Structured persistent files: `activeContext.md`, `progress.md`, etc. AI self-updates |
| 8. 0AGNOSTIC.md | File read | High | Always available |

**What gets synced from .0agnostic/:**
- `rules/static/` → `.clinerules` (always loaded) or `.roo/rules/*.md` (always loaded)
- `rules/dynamic/` → `.roo/rules-{mode-slug}/*.md` (loaded only in matching mode)
- `0AGNOSTIC.md` → System instructions (simplified)
- Mode definitions from GAB → `.roomodes` (custom mode definitions with tool restrictions)

**What gets added from .1merge/.1cline_merge/ or .1merge/.1roo_merge/:**
- `.roomodes` with mode definitions including per-mode tool access controls
- Memory Bank templates (`projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`)
- MCP memory bank server configuration for persistent context
- Legacy compatibility rules (`.clinerules-{slug}` → `.roo/rules-{slug}/`)

**Memory Bank system files:**
```
memory_bank/
  projectbrief.md        → Project overview and goals
  productContext.md       → What the product does and why
  systemPatterns.md       → Architecture patterns and conventions
  techContext.md          → Technology stack and dependencies
  activeContext.md        → Current session focus (AI-updated)
  progress.md            → What works, what doesn't (AI-updated)
```

**Compensation for missing avenues:**
- **No skills (Avenue 3):** Memory Bank files serve as structured persistent context. The AI reads them at session start and updates them during work. Combined with per-mode rules, this covers much of what skills provide.
- **No @import (Avenue 4):** Memory Bank files are self-contained. Cross-references must be explicit file reads.
- **Mode-scoped rules (Avenue 2 alternative):** Instead of file-path scoping, Roo Code scopes rules to task modes (Architect, Code, Test, Debug). This is a different paradigm — context by intent rather than context by location.

**Avenue chain example:**
```
Agent enters "Architect" mode to plan a feature:
  Avenue 1 fires: .clinerules loaded + architect-mode system prompt
  Avenue 2 fires: .roo/rules-architect/ loaded with planning constraints
    → tools restricted: can read files and search, cannot write code
  Avenue 7 fires: Memory Bank files loaded
    → activeContext.md has current session focus
    → systemPatterns.md has architecture decisions
  Avenue 5 available: agent can run jq via shell
  Avenue 6 available: agent reads .integration.md

Result: 4 avenues fire — mode-based scoping provides strong task-type awareness
```

**Key risk:** The Memory Bank relies on the AI consistently updating its own context files. If the AI fails to update `activeContext.md` or `progress.md`, session continuity degrades. The `.roomodes` configuration adds complexity — misconfigured tool restrictions per mode can block necessary operations.

**Cline/Roo Code's unique strengths:**
- **Memory Bank system** — structured, purpose-specific persistent files that the AI self-maintains
- **Custom modes with tool restrictions** — different AI behaviors, instructions, and tool access per mode (Architect vs Code vs Test)
- **Per-mode rule files** — clean separation of concerns; architecture rules only load in architect mode
- **Just-in-time rule loading** — rules loaded only when relevant to current mode and task

---

### GitHub Copilot (3-4/8 Avenues)

| Avenue | Mechanism | Effectiveness | Notes |
|--------|-----------|--------------|-------|
| 1. System Prompt | `.github/copilot-instructions.md` + per-workspace settings | Medium | Project-level instructions, can vary per workspace |
| 2. Path Rules | N/A | N/A | No path-scoped rules; relies on semantic indexing for relevance |
| 3. Skills | Agent Skills (`.github/skills/*/SKILL.md`) | Medium | Progressive disclosure — same Agent Skills open standard as Claude Code |
| 4. @import | N/A | N/A | No @import mechanism |
| 5. JSON-LD/jq | Limited bash | Low | IDE extension, limited terminal access |
| 6. .integration.md | File read | Medium | Can read project files when agent decides to |
| 7. Episodic | Copilot Spaces (cross-artifact) | Medium-High | Persistent context containers combining code, issues, PRs, docs, notes |
| 8. 0AGNOSTIC.md | File read | Medium | Available but agent must decide to read |

**What gets synced from .0agnostic/:**
- `0AGNOSTIC.md` → `.github/copilot-instructions.md` (system prompt, GitHub-flavored)
- `rules/static/` → Inlined into instructions file (no separate rules mechanism)
- `protocols/` → `.github/skills/*/SKILL.md` (Copilot follows the Agent Skills standard)
- `skills/` → `.github/skills/` (direct copy)

**What gets added from .1merge/.1copilot_merge/:**
- GitHub-specific instructions (PR workflow, issue triage patterns)
- Copilot Spaces configuration references
- Per-workspace settings overrides (model selection, feature flags)
- Copilot Coding Agent configuration for autonomous PR creation from Issues

**Compensation for missing avenues:**
- **No path rules (Avenue 2):** Copilot relies on semantic indexing (`@workspace`) to determine relevant context rather than explicit file-path rules. The AI sees automatically-ranked code chunks.
- **No @import (Avenue 4):** Instructions must be self-contained.
- **Copilot Spaces (Avenue 7 alternative):** Instead of file-based episodic memory, Copilot Spaces aggregate repositories, code, PRs, issues, notes, and images into shareable context containers. These persist across sessions and are org-sharable.

**Avenue chain example:**
```
Agent starts from a GitHub Issue (Copilot Coding Agent):
  Avenue 1 fires: .github/copilot-instructions.md loaded
    → project-level coding standards applied
  Avenue 3 activates: Agent Skill matches issue context
    → loads SKILL.md with task-specific procedure
  Avenue 7 available: Copilot Space includes related PRs, docs, and notes
    → cross-artifact context provides broader awareness
  Avenue 6 possible: agent MAY read .integration.md if instructed

Result: 3 avenues fire reliably — semantic indexing compensates for missing path rules
```

**Key risk:** Copilot is tightly integrated with the GitHub ecosystem and VS Code. Outside of GitHub-hosted projects, context delivery degrades. Copilot Spaces require GitHub organization setup and are not purely file-based — they cannot be generated by agnostic-sync.

**Copilot's unique strengths:**
- **Copilot Spaces** — cross-artifact context containers combining code, issues, PRs, documentation, notes, and images into a single searchable context
- **Agent Skills** — same open standard as Claude Code, enabling cross-tool skill portability
- **Semantic indexing** — `@workspace` provides automatically relevance-ranked code context
- **Autonomous PR creation** — Copilot Coding Agent creates PRs from Issues, referencing Skills during execution
- **Per-workspace settings** — different models, feature flags, and instructions per project

---

### Summary: Avenue Coverage Across All Tools

| Avenue | Claude Code | Codex CLI | Gemini CLI | Cursor IDE | Cursor CLI | OpenCode | Cline/Roo | Amazon Q | Copilot | Aider | Windsurf | Junie |
|--------|:----------:|:---------:|:----------:|:----------:|:----------:|:--------:|:---------:|:--------:|:-------:|:-----:|:--------:|:-----:|
| 1. System Prompt | High | Medium | Medium* | Medium | High | Model-dep | High | Medium | Medium | Medium | Medium | Medium |
| 2. Path Rules | High | -- | -- | High | High | -- | Medium-High | -- | -- | -- | -- | -- |
| 3. Skills | Medium | Medium | Low | Medium | Medium | -- | -- | Low-Medium | Medium | -- | -- | -- |
| 4. @import | High | -- | -- | -- | Medium | -- | -- | -- | -- | -- | -- | -- |
| 5. JSON-LD/jq | Medium | Medium | Medium | -- | Medium | Model-dep | Medium | Low | Low | Medium | Low | Low |
| 6. .integration.md | High | High | High | Medium | High | High | High | Medium | Medium | High | Medium | Medium |
| 7. Episodic | High | Medium | Medium | -- | Medium | Medium | High | -- | Medium-High | -- | -- | -- |
| 8. 0AGNOSTIC.md | High | High | High | Medium | High | High | High | Medium | Medium | High | Medium | Medium |
| **Active Avenues** | **8/8** | **5/8** | **4/8** | **3-4/8** | **6-7/8** | **3-4/8** | **4-5/8** | **3-4/8** | **3-4/8** | **3/8** | **2-3/8** | **2-3/8** |

*Gemini CLI's Avenue 1 is degraded due to documented model-level instruction refusal.

**Reliability ranking** (based on avenue coverage, effectiveness, and unique compensating features):

1. **Claude Code** — Full coverage, all avenues native or via tools. The only tool with 8/8 avenues.
2. **Cursor CLI** — 6-7 avenues including bash, path rules, skills, and session management. Multi-model flexibility and cloud agents add depth. Strongest CLI alternative to Claude Code.
3. **Codex CLI** — 5 avenues with solid skills + bash. AGENTS.override.md pattern and sandboxed execution add safety.
4. **Cline/Roo Code** — 4-5 avenues. Memory Bank system provides the best structured episodic memory. Custom modes with per-mode tool restrictions are unique. No skills but Memory Bank compensates.
5. **Gemini CLI** — 4 avenues, but Avenue 1 unreliability from model-level instruction refusal is a significant weakness. Bidirectional traversal and extensions system are architecturally strong.
6. **Cursor IDE** — 3-4 avenues. Path rules and skills (v2.4+) are strong, but no bash/jq access limits depth. Semantic codebase indexing compensates significantly.
7. **OpenCode** — 3-4 avenues, model-dependent. Excellent with Claude backend, poor with GPT. Zero-config LSP integration is unique.
8. **Amazon Q** — 3-4 avenues. Priority-based rules and security scanning are unique but limited general-purpose context delivery. AWS-focused.
9. **GitHub Copilot** — 3-4 avenues. Copilot Spaces and semantic indexing are powerful but GitHub-ecosystem-dependent. Agent Skills follow the same open standard as Claude Code.
10. **Aider** — 3 avenues. System prompt + bash only, but automatic repo map via tree-sitter + PageRank is the most technically sophisticated context mechanism among CLI tools.
11. **Windsurf** — 2-3 avenues. Four rule activation modes and AI-auto-generated memories add depth, but no path rules, skills, or bash limits coverage.
12. **Junie** — 2-3 avenues. IDE inspections feedback loop and AST-aware navigation are unique strengths, but minimal autonomous context loading.

**Key changes from previous ranking:**
- **Cursor** split into IDE (3-4/8) and CLI (6-7/8) — the CLI is a fundamentally different tool with bash, AGENTS.md, session management, and broad context support
- **Cline/Roo Code** added at rank 4 — Memory Bank and custom modes provide strong context delivery despite missing skills
- **Amazon Q** added at rank 8 — priority-based rules and security scanning are unique but general context is limited
- **GitHub Copilot** added at rank 9 — Copilot Spaces and Agent Skills are strong but ecosystem-locked
- **Cursor IDE** dropped from rank 5 to rank 6 — with Cursor CLI now listed separately, the IDE's lack of bash access is more apparent

---

## Unique Per-Tool Avenues

Each AI coding tool has context delivery avenues that Claude Code CLI lacks. This section identifies those gaps, assesses their impact, and maps which can be leveraged by the agnostic system through `.1merge/` generation.

### Claude Code Baseline

For reference, Claude Code CLI provides: CLAUDE.md hierarchy (always loaded), skills (`.claude/skills/`), MCP tools, hooks, auto-memory, agent teams (research preview), and path-scoped rules.

---

### 1. Cursor

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| Glob-based auto-attach rules | `.cursor/rules/*.mdc` with `globs: src/**/*.tsx` -- rules auto-activate on file pattern match | HIGH | YES -- `.1merge/` generates `.cursor/rules/*.mdc` |
| Four rule activation modes | `alwaysApply`, auto-attached (glob), agent-requested (AI picks by description), manual (`@ruleName`) | HIGH | PARTIAL -- skills approximate agent-requested mode |
| Semantic codebase indexing | Embeddings via OpenAI, stored in Turbopuffer vector DB. `@codebase` retrieves semantically similar code | VERY HIGH | NO -- infrastructure feature |
| `@web`, `@docs`, `@git` references | Inline context injection from web, docs, and git | MEDIUM-HIGH | NO -- IDE feature |
| Notepads | Persistent scratchpads with `@` references, reusable across sessions | MEDIUM | PARTIAL -- approximated by skills |
| Background Agents | Parallel agents on separate branches | HIGH | NO -- infrastructure |
| Team Rules Dashboard | Centralized org-wide rule management | MEDIUM | NO -- platform feature |

**Key insight**: Semantic codebase indexing is Cursor's single biggest advantage. Glob-based auto-attach is the most replicable advantage for the agnostic system.

---

### 2. Windsurf / Cascade

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| AI-auto-generated memories | Cascade creates and persists context automatically, workspace-scoped | HIGH | PARTIAL -- Claude Code auto-memory is closest equivalent |
| Four rule activation modes | Manual, Always On, Model Decision, Glob-based | HIGH | YES -- `.1merge/` generates `.windsurf/rules/` |
| Workflows | `.windsurf/workflows/` markdown files defining step-by-step procedures | MEDIUM-HIGH | YES -- skills approximate this |
| Enterprise system-level rules | Admin rules that cannot be overridden by users | MEDIUM | NO -- platform feature |
| RAG-based workspace indexing | Retrieval-Augmented Generation over entire local codebase | HIGH | NO -- infrastructure |

**Key insight**: Auto-generated memories and the Model Decision rule activation mode are the standout features.

---

### 3. OpenAI Codex CLI

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| `AGENTS.override.md` | Override files take precedence at every level, enabling personal overrides | MEDIUM-HIGH | YES -- `.1merge/` overrides analog |
| Configurable fallback filenames | `project_doc_fallback_filenames` in config.toml accepts arbitrary names | MEDIUM | YES -- agnostic sync handles mapping |
| 32 KiB instruction chain budget | `project_doc_max_bytes` limits total context, concatenates root-down | MEDIUM | YES -- could implement as rule |
| Sandboxed execution | OS-level sandbox, no network, workspace-only writes | HIGH | NO -- infrastructure |
| MCP server self-exposure | Codex CLI exposable as MCP server for orchestration | MEDIUM | NO -- architecture feature |

**Key insight**: The override mechanism and budget management are directly useful patterns.

---

### 4. Google Gemini CLI

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| Bidirectional directory traversal | Loads GEMINI.md walking UP to git root AND DOWN into subdirectories | HIGH | YES -- agnostic-sync generates GEMINI.md at all levels |
| `@path/to/file.md` imports | Inline modularization of context files | MEDIUM-HIGH | YES -- usable in generated GEMINI.md |
| Extensions system | Bundle MCP servers + context + commands as installable packages | HIGH | PARTIAL -- skills approximate partially |
| Conductor extension | Product knowledge and tech decisions as versioned markdown driving agent behavior | HIGH | YES -- aligned with layer-stage approach |
| Tool restrictions per extension | `excludeTools` disables built-in tools per context | MEDIUM | NO -- tool management infrastructure |
| `/memory show` and `/memory refresh` | Inspect loaded context, force re-scan | MEDIUM | NO -- tool-specific feature |

**Key insight**: Bidirectional traversal (downward scan into subdirectories) and `@import` are the most significant unique avenues.

---

### 5. Aider

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| Automatic repo map (tree-sitter) | AST parsing, dependency graph, PageRank symbol ranking, configurable token budget | VERY HIGH | NO -- deep infrastructure |
| Graph-based symbol ranking | NetworkX PageRank with personalization factors | HIGH | NO -- algorithm, not file format |
| `conventions.md` | Standing coding instructions, community conventions repository | MEDIUM | YES -- already covered by `0AGNOSTIC.md` |
| Architect mode | Two-model pipeline: architect for planning, editor for implementation | HIGH | NO -- architecture feature |
| Configurable `map-tokens` budget | User controls repo map context allocation | MEDIUM | NO -- requires repo map infrastructure |

**Key insight**: The repo map is the most technically sophisticated context delivery mechanism among CLI tools. Zero-config, ranked, budget-aware codebase awareness.

---

### 6. OpenCode

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| Zero-config LSP integration | Auto-detects language, spins up correct LSP server, exposes diagnostics + navigation | HIGH | NO -- infrastructure |
| LSP tool exposure | AI uses goToDefinition, findReferences, hover, workspaceSymbol, callHierarchy | HIGH | NO -- tool infrastructure |
| Auto-compact | Summarizes conversation on context window overflow | MEDIUM | NO -- runtime feature |

**Key insight**: Deep LSP integration providing semantic code tools to the AI is the standout feature.

---

### 7. GitHub Copilot

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| Copilot Spaces | Containers combining repos, code, PRs, issues, notes, images as context | VERY HIGH | NO -- platform infrastructure |
| Agent Skills (`/.github/skills/`) | Procedural knowledge auto-referenced during autonomous PR creation | HIGH | YES -- same Agent Skills standard |
| Semantic indexing for search | Builds/maintains semantic code search index | HIGH | NO -- platform infrastructure |
| `@workspace` context | Auto-includes most relevant code chunks from periodically-updated index | HIGH | NO -- IDE extension feature |

**Key insight**: Copilot Spaces is the most innovative -- aggregating diverse artifacts into a single context container.

---

### 8. JetBrains Junie

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| IDE inspections as AI context | Hundreds of language-specific static analysis checks validating AI output | VERY HIGH | NO -- requires JetBrains IDE |
| AST-aware project navigation | Search-everywhere, source-code traversal, AST-aware tools | VERY HIGH | NO -- IDE infrastructure |
| `.junie/guidelines.md` | Project-level guidelines, community guidelines repository | MEDIUM | YES -- `.1merge/` generates this |
| IDE refactoring tools | Semantically-aware rename, extract, inline using full dependency graph | HIGH | NO -- IDE feature |
| Project model access | Understands module structure, build config, dependency relationships | HIGH | NO -- IDE feature |

**Key insight**: IDE inspections and AST-aware navigation give Junie fundamentally different code understanding quality compared to CLI tools.

---

### 9. Amazon Q Developer

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| `.amazonq/rules/` with priority levels | Explicit priority levels for conflict resolution | MEDIUM-HIGH | YES -- `.1merge/` generates these |
| Selective rule activation per session | Toggle rules on/off per session | MEDIUM | NO -- UI feature |
| `@workspace` (100K char context) | Large-budget automatic relevance selection | HIGH | NO -- IDE extension |
| Security scanning integration | Vulnerability detection in AI workflow | MEDIUM | NO -- AWS infrastructure |
| Custom agents with `file://` globs | Dynamic rule inclusion via glob patterns | MEDIUM | YES -- replicable pattern |

**Key insight**: Priority-based rule conflict resolution and per-session toggling are the most interesting patterns.

---

### 10. Cline / Roo Code

| Avenue | Description | Effectiveness | Agnostic Leverage |
|--------|-------------|---------------|-------------------|
| Memory Bank system | Structured files: `projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `activeContext.md`, `progress.md` | HIGH | YES -- implementable as convention |
| Custom modes via `.roomodes` | Different AI behaviors per mode with tool restrictions and file access controls | HIGH | PARTIAL -- GAB modes approximate conceptually |
| Per-mode rule files | `.roo/rules-{mode-slug}/` directories with mode-specific instructions | HIGH | YES -- `.1merge/` generates per-mode rules |
| MCP Memory Bank servers | Dedicated MCP servers for persistent project context | MEDIUM-HIGH | YES -- usable with Claude Code |
| Just-in-time rule loading | Adaptive loading based on current mode and task | HIGH | PARTIAL -- skills provide on-demand loading |

**Key insight**: Structured Memory Bank and custom modes with per-mode rules/tool restrictions are the standout features.

---

### Tier Summary

#### Tier 1 -- High Impact, Claude Code Has No Equivalent

1. **Semantic codebase indexing / vector search** (Cursor, Copilot, Windsurf)
2. **Automatic repo map via tree-sitter + PageRank** (Aider)
3. **IDE inspections as AI feedback loop** (Junie)
4. **Copilot Spaces** (Copilot) -- cross-artifact context containers

#### Tier 2 -- High Impact, Claude Code Has Partial Equivalent

5. **Glob-based auto-attach rules** (Cursor, Windsurf, Amazon Q)
6. **AI-decided rule loading** (Cursor agent-requested, Windsurf Model Decision)
7. **Memory Bank structured files** (Cline/Roo Code)
8. **Custom modes with tool restrictions** (Roo Code)
9. **Bidirectional traversal + imports** (Gemini CLI)
10. **Extensions as distributable context bundles** (Gemini CLI)

#### Tier 3 -- Medium Impact, Useful Patterns

11. **Override files** (Codex CLI `AGENTS.override.md`)
12. **Priority-based rule conflict resolution** (Amazon Q)
13. **Context budget management** (Codex 32KiB, Aider map-tokens)
14. **Context visibility commands** (Gemini CLI `/memory show`)
15. **Auto-compact on context overflow** (OpenCode)

---

### Agnostic System Leverage Mapping

Avenues the `.1merge/` system can generate from `0AGNOSTIC.md`:

| Tool File | Generated From | Unique Features Carried |
|-----------|---------------|----------------------|
| `.cursor/rules/*.mdc` | `0AGNOSTIC.md` sections | Glob auto-attach frontmatter, activation modes |
| `.windsurf/rules/*.md` | `0AGNOSTIC.md` sections | Glob patterns, model-decision descriptions |
| `.windsurf/workflows/*.md` | Stage procedures | Step-by-step workflow templates |
| `AGENTS.md` + `AGENTS.override.md` | `0AGNOSTIC.md` | Override pattern for personal customization |
| `GEMINI.md` (with `@imports`) | `0AGNOSTIC.md` | Modular context via imports |
| `.junie/guidelines.md` | `0AGNOSTIC.md` | Persistent project guidelines |
| `.amazonq/rules/*.md` | `0AGNOSTIC.md` sections | Priority levels, activation modes |
| `.clinerules-{mode}` | `0AGNOSTIC.md` mode sections | Per-mode instructions |
| `.roomodes` | GAB mode definitions | Custom mode definitions with tool restrictions |
| Memory bank files | Episodic memory / status.json | Structured persistent context |

Avenues that **cannot** be leveraged: vector search indexing, IDE inspections, LSP integration, sandboxed execution, and platform-specific collaborative features (Copilot Spaces). These require native tool support or dedicated MCP servers to approximate.

### Unique Avenues Sources

- [A Deep Dive into Cursor Rules and Background Agents](https://medium.com/@duraidw/title-a-deep-dive-into-cursor-rules-and-background-agents-51d65c6a9619)
- [Cursor 1.7: Agent Autocomplete, Hooks & Team Rules](https://skywork.ai/blog/cursor-1-7-2025-agent-autocomplete-hooks-team-rules/)
- [How Cursor Indexes Codebases Fast](https://read.engineerscodex.com/p/how-cursor-indexes-codebases-fast)
- [Cascade Memories Documentation](https://docs.windsurf.com/windsurf/cascade/memories)
- [Using Windsurf Rules, Workflows, and Memories](https://www.paulmduvall.com/using-windsurf-rules-workflows-and-memories/)
- [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)
- [Provide Context with GEMINI.md Files](https://geminicli.com/docs/cli/gemini-md/)
- [Gemini CLI Extensions](https://google-gemini.github.io/gemini-cli/docs/extensions/)
- [Aider Repository Map](https://aider.chat/docs/repomap.html)
- [OpenCode LSP Servers Documentation](https://opencode.ai/docs/lsp/)
- [About GitHub Copilot Spaces](https://docs.github.com/en/copilot/concepts/context/spaces)
- [Junie Documentation](https://www.jetbrains.com/help/idea/junie.html)
- [JetBrains Junie Guidelines](https://github.com/JetBrains/junie-guidelines)
- [Creating Project Rules for Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-project-rules.html)
- [Cline Memory Bank Documentation](https://docs.cline.bot/prompting/cline-memory-bank)
- [Customizing Modes in Roo Code](https://docs.roocode.com/features/custom-modes)

---

## Unexplored and Novel Context Avenues

Research (February 2026) identified 27 context delivery avenues beyond the original 8. These range from MCP server primitives to multi-agent isolation patterns. Each is assessed for mechanism, current tool support, reliability, and agnostic system integration potential.

---

### Avenue Summary Table

| # | Avenue | Mechanism | Reliability | Agnostic Fit | Tier |
|---|--------|-----------|-------------|-------------|------|
| 1 | MCP Resources / Prompts | Server-side read-only data + dynamic templates | High | Strong | 1 |
| 2 | Git Hooks / Agent Hooks | Scripts at lifecycle events | Mixed | Moderate | 2 |
| 3 | LSP Integration | Semantic code intelligence via protocol | High (code), Low (instructions) | Supplementary | 3 |
| 4 | IDE Workspace Settings | Tool-specific config directories | High (native), Zero (cross-tool) | Core (.1merge/) | 2 |
| 5 | Environment Variables | Process-level config flags | Low (instructions), High (config) | Supplementary | 4 |
| 6 | Package Manifest Metadata | AI fields in package.json / pyproject.toml | Low | Poor | 4 |
| 7 | Codebase Indexing / Embeddings | Vector embeddings + semantic search | High | Strong (via MCP) | 1 |
| 8 | Repo Maps / Code Graphs | Static analysis + AST + dependency ranking | Very High | Supplementary | 2 |
| 9 | Session Persistence | Cross-session memory + progressive disclosure | High | Strong | 1 |
| 10 | CI/CD Feedback | Build/test results as agent context | Moderate | Moderate | 3 |
| 11 | Documentation APIs | MCP servers serving hosted docs | High | Strong | 2 |
| 12 | Semantic Code Search | Hybrid BM25 + dense vector retrieval | High | Strong (via MCP) | 2 |
| 13 | Custom Tool Definitions | MCP tools, skills, subagents, plugins | Very High | Core | 1 |
| 14 | Browser / Web Context | Web search, URL fetch, browser automation | Moderate | Supplementary | 3 |
| 15 | Team Context Distribution | Version-controlled rules, sync tools, standards | High | Direct overlap | 1 |
| 16 | DevContainers | Container-defined agent environments | Medium | Moderate | 3 |
| 17 | Docstrings / Type Annotations | Code-embedded implicit instructions | Medium | Supplementary | 3 |
| 18 | Plugins / Extension Distribution | Distributable context bundles | High | Strong | 2 |
| 19 | Agent Client Protocol (ACP) | Standardized editor-agent communication | Emerging | Future target | 4 |
| 20 | Context Compaction Hooks | Re-inject critical context after compaction | High | Strong | 1 |
| 21 | Multi-Agent Isolation | Subagents with task-specific context windows | High | Strong | 2 |
| 22 | Agent-to-Agent Protocol (A2A) | Standardized cross-agent handoff and delegation | Emerging | Strong (orchestration) | 2 |
| 23 | MCP Advanced Primitives | Roots, Elicitation, Sampling, list_changed notifications | High | Strong | 1 |
| 24 | Telemetry-as-Context | OpenTelemetry traces/spans as runtime context | High | Strong (ops + debugging) | 2 |
| 25 | Policy-as-Context | Runtime policy decision engines (OPA/OPAL) gating context/tool use | Medium-High | Strong (governance) | 2 |
| 26 | Provenance/Attestation | SLSA/in-toto/Sigstore trust metadata for context/toolchain integrity | Medium | Strong (trust/compliance) | 3 |
| 27 | Credentialed Agent Identity | Verifiable credentials for agent identity/authorization context | Emerging | Moderate-Strong | 3 |

---

### Context Chaining vs Reference Chaining

This system uses both context chaining (what content is loaded) and reference chaining (what pointer is followed next).

Both chaining types together form the **Avenue Web** (the **Web of Avenues**, `multi_avenue_redundancy_web`).

| Chain Type | Goal | Static Examples | Dynamic Examples |
|-----------|------|-----------------|-----------------|
| Context chaining | Load sufficient working context at each step | AGENTS.md, rules files, repo maps, MCP Resources | Session memory, semantic retrieval, CI feedback, telemetry |
| Reference chaining | Route the agent to the next context artifact/tool/query | @imports, file pointers, index manifests, path rules | MCP Prompts/templates, elicitation flows, tool outputs with follow-up handles |

Practical rule: every critical instruction should be reachable through both a context path and a reference path, with at least one static and one dynamic route.

---

### Ranked Avenues to Use (Context + Reference Chaining)

Ranking emphasizes reliability, cross-tool portability, and immediate implementation value for the 0Agnostic system.

| Rank | Avenue(s) | Why Use First |
|------|-----------|---------------|
| 1 | 1 + 13 + 23 (MCP Resources/Prompts + Custom Tools + Advanced MCP Primitives) | Highest portability and control; covers static context, dynamic references, and runtime refresh. |
| 2 | 15 + 20 (Team Distribution + Compaction Hooks) | Makes behavior consistent across users and prevents context loss after compaction. |
| 3 | 9 + 7 + 12 (Session Persistence + Embeddings + Semantic Search) | Best path to token-efficient dynamic loading with high recall. |
| 4 | 24 (Telemetry-as-Context) | Converts failures and runtime behavior into actionable context for fast iteration. |
| 5 | 8 + 11 (Repo Maps + Documentation APIs) | Strong retrieval quality for code structure and dependency docs. |
| 6 | 2 + 25 (Hooks + Policy-as-Context) | Enforces lifecycle and governance constraints at runtime. |
| 7 | 22 + 21 (A2A + Multi-Agent Isolation) | Scales context handling across specialist agents without full-context sharing. |
| 8 | 18 + 4 (Plugins + IDE Workspace Settings) | Good distribution and native UX, weaker portability. |
| 9 | 26 + 27 (Provenance + Credentialed Identity) | Important for trust/compliance and enterprise governance; less immediate for core loading. |
| 10 | 3 + 10 + 14 + 16 + 17 | Valuable supplemental sources, but secondary for core chaining architecture. |
| 11 | 19 + 5 + 6 | Monitor or avoid as primary context channels for now. |

---

### Tier 1 -- High Impact, Implement Now

#### 1. MCP Resources and Prompts

MCP exposes three primitives beyond tools: **Resources** (structured read-only data, application-initiated), **Prompts** (dynamic instruction templates), and **Tools** (callable functions, model-initiated). An MCP server can serve as a universal knowledge base for the agnostic system.

- **VS Code**: Full MCP spec support (Resources + Prompts) since June 2025
- **Cursor**: Added MCP Prompts, Resources, and Elicitation in early 2026
- **Claude Code**: MCP tools natively; Resources/Prompts support varies
- **Google Developer Knowledge API** (Feb 2026): MCP server serving 40M+ pages of developer docs
- **MATLAB MCP Server**: Demonstrated coding guidelines served as Resources

**Agnostic integration**: Expose layer-stage knowledge, rules, and principles as Resources; stage workflows as Prompts. A single MCP server works across all tools.

#### 7. Codebase Indexing / Embeddings

Vector embeddings capture semantic meaning of code. Hybrid search (BM25 keyword + dense vector) achieves 40% token reduction vs grep-based approaches.

- **Cursor**: Core feature with OpenAI embeddings in Turbopuffer
- **Roo Code**: Gemini Embedding for semantic search
- **Zilliz claude-context**: Open-source MCP server providing hybrid code search
- **Aider**: Deliberately eschews embeddings, uses graph-based structural analysis instead

**Agnostic integration**: An MCP server indexing the layer-stage knowledge system with embeddings enables cross-tool "find the relevant rule" queries.

#### 9. Session Persistence / Progressive Disclosure

Multi-layer persistence: in-session history, cross-session memory, auto-compaction, and progressive disclosure (high-level summaries first, detail on demand).

- **Claude Code**: Auto-memory (`MEMORY.md` first 200 lines), manual `/memory`
- **claude-mem**: Third-party plugin with 3-layer progressive disclosure (10x token savings)
- **Codex**: Automatic compaction with encrypted content items
- **Google ADK**: Session, State, and Memory as three distinct persistence layers

**Agnostic integration**: The episodic memory system (`outputs/episodic/`) already implements cross-session persistence tool-agnostically. Standard session output formats in `.0agnostic/memory/` would extend this.

#### 13. Custom Tool/Function Definitions

The most flexible avenue -- custom tools can implement any context delivery logic.

- **Claude Code**: Skills, subagents, plugins, hooks, MCP tools
- **Cursor**: Custom tools through MCP and agent mode
- **Continue.dev**: Custom context providers, tools, slash commands
- **Codex**: Agents SDK for custom workflows

**Agnostic integration**: MCP tools in `.0agnostic/mcp/` are the most portable approach.

#### 15. Team Context Distribution

Shared rules ensuring all team members' AI agents follow the same standards.

- **AGENTS.md**: Open standard backed by Linux Foundation's Agentic AI Foundation, supported by 60,000+ projects
- **AI Rules Sync (AIS)**: Manages rules in git repos, syncs via symlinks
- **ai-rulez**: Generates for 18 tools from single `.ai-rulez/` directory, supports remote includes
- **Ruler**: Centralized management generating for multiple AI assistants

**Agnostic integration**: Direct overlap with `0AGNOSTIC.md` -> `agnostic-sync.sh`. The `.1merge/` 3-tier system (synced -> overrides -> additions) is more sophisticated than existing tools.

#### 20. Context Compaction Hooks

When context windows fill, compaction summarizes the conversation. A `SessionStart` hook with `compact` matcher re-injects critical context after every compaction.

- **Claude Code**: Native hook system supports this pattern
- **Codex**: Automatic compaction with encrypted content preservation

**Agnostic integration**: Define "compaction-safe" context -- the minimal essential subset that must survive compression -- in `.0agnostic/compact/`.

---

### Tier 2 -- High Impact, Investigate

#### 2. Git Hooks / Agent Hooks

Git hooks fire at git lifecycle points (pre-commit, post-commit, pre-push). Claude Code's hooks system extends this with 14 lifecycle events (`PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`, etc.) that receive JSON payloads and can block actions or inject context.

**Agnostic integration**: Standard git hooks in `.0agnostic/hooks/` enforce cross-tool rules. Tool-specific hooks are more powerful but non-portable.

#### 4. IDE Workspace Settings

Each tool has its own config directory (`.cursor/rules/`, `.windsurf/rules/`, `.github/copilot-instructions.md`, `.continue/`). High native reliability, zero cross-tool portability.

**Agnostic integration**: This is the core problem `.1merge/` solves -- generating tool-specific files from `0AGNOSTIC.md`.

#### 8. Repo Maps / Code Graphs

Aider's approach: tree-sitter AST parsing, dependency graph construction, PageRank symbol ranking, budget-aware selection (default 1024 tokens). Distinct from embeddings -- uses static analysis, not semantic similarity.

**Agnostic integration**: The `0INDEX.md` files serve a similar purpose at the documentation level. A code graph generator in `.0agnostic/tools/` could produce maps any tool consumes.

#### 11. Documentation APIs / @docs References

Documentation-as-a-service for AI agents. Google's Developer Knowledge API (Feb 2026) provides searchable access to 40M+ pages via MCP.

**Agnostic integration**: Define documentation sources in `.0agnostic/docs/` mapping project dependencies to documentation MCP servers or URLs.

#### 12. Semantic Code Search

Hybrid BM25 + dense vector retrieval. Zilliz claude-context reports 40% token reduction with no loss in recall.

**Agnostic integration**: Since semantic search servers expose themselves as MCP tools, reference them in `.0agnostic/mcp/` configs. Tool-agnostic by design.

#### 18. Plugins / Extension Distribution

Claude Code plugins bundle skills, hooks, commands, subagents into distributable packages. Gemini CLI Extensions package MCP servers + context + commands.

**Agnostic integration**: `.0agnostic/plugins/` could define plugin manifests mapping to tool-specific distribution formats.

#### 21. Multi-Agent / Subagent Isolation

Split work across subagents with isolated context windows. Each gets only task-relevant context. The orchestrator coordinates results without sharing full contexts.

- **Claude Code**: Native subagents
- **Codex**: Multi-agent support
- **Cursor**: Subagents via Composer 1.5
- **LangGraph**: Multi-agent patterns

**Agnostic integration**: Layer-stage hierarchy naturally maps to subagent specialization -- a testing subagent loads stage 07 context, a design subagent loads stage 05.

---

### Tier 3 -- Supplementary Value

#### 3. LSP Integration

Provides semantic code intelligence (go-to-definition, find-references, hover, diagnostics). Claude Code added native LSP support in Dec 2025 for 11 languages. The axivo/mcp-lsp bridge makes LSP available to any MCP client.

High for code understanding; not designed to carry instructions.

#### 10. CI/CD Feedback Loops

Agents submit code, CI runs, results feed back, agents iterate. Spotify documented the "outer loop" pattern; Elastic uses self-correcting monorepos.

**Agnostic integration**: Standardize how test results are presented to agents in `.0agnostic/ci/`.

#### 14. Browser / Web Context

Built-in WebSearch, WebFetch, Playwright MCP, claude-in-chrome. Valuable for up-to-date information but has network dependency and token cost.

#### 16. DevContainers

`devcontainer.json` defines AI agent environments: env vars, tools, setup scripts, context files. Docker Desktop has experimental agent sandboxes.

**Agnostic integration**: `.0agnostic/devcontainer/` could define standard container configs including the full context chain.

#### 17. Docstrings / Type Annotations

Well-written docstrings serve as implicit instructions to AI agents. No special tool support needed -- all agents benefit from code-level documentation.

**Agnostic integration**: Define docstring conventions in layer_0 rules that improve AI performance across tools.

---

### Tier 4 -- Monitor for Future

#### 5. Environment Variables

`CLAUDE_ENV_FILE`, Codex cloud env, DevContainer env. Effective for config flags and paths; poor for complex instructions.

#### 6. Package Manifest Metadata

Could carry AI instructions in `package.json`, `pyproject.toml`, `Cargo.toml` extension fields. No major tool reads these for AI instructions. Dedicated files (AGENTS.md, CLAUDE.md) have won this space.

#### 19. Agent Client Protocol (ACP)

New open standard by Zed Editor (Aug 2025) -- standardizes editor-agent communication. First reference implementation: Gemini CLI. Could become another output target for the agnostic system.

---

### Integration Priority Matrix

| Priority | Action | Avenue(s) |
|----------|--------|-----------|
| **Now** | Build MCP server for layer-stage knowledge | 1 (Resources/Prompts), 13 (Custom Tools) |
| **Now** | Implement advanced MCP primitives in server/client contracts | 23 (Roots, Elicitation, Sampling, list_changed) |
| **Now** | Add AGENTS.md generation to agnostic-sync.sh | 15 (Team Distribution) |
| **Now** | Define compaction-safe context | 20 (Compaction Hooks) |
| **Next** | Evaluate semantic search MCP server | 7 (Embeddings), 12 (Semantic Search) |
| **Next** | Add telemetry pipeline into agent feedback loops | 24 (Telemetry-as-Context) |
| **Next** | Add documentation source mapping | 11 (Documentation APIs) |
| **Next** | Add policy enforcement checks for tool/context admission | 25 (Policy-as-Context), 2 (Hooks) |
| **Next** | Evaluate ai-rulez / AIS compatibility | 15 (Team Distribution) |
| **Later** | Add A2A handoff contracts for subagent orchestration | 22 (A2A), 21 (Multi-Agent Isolation) |
| **Later** | Leverage Claude Code LSP + MCP-LSP bridge | 3 (LSP) |
| **Later** | Include agnostic context in DevContainer specs | 16 (DevContainers) |
| **Later** | Define session output format standards | 9 (Session Persistence) |
| **Later** | Standardize CI/CD feedback presentation | 10 (CI/CD) |
| **Later** | Add provenance + attestation metadata for context/toolchain trust | 26 (Provenance/Attestation) |
| **Watch** | Track verifiable credential adoption for agent identity | 27 (Credentialed Agent Identity) |
| **Watch** | Agent Client Protocol (ACP) development | 19 (ACP) |

### Novel Avenues Sources

- [Model Context Protocol Specification (Nov 2025)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Anthropic 2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
- [Context Engineering for Coding Agents -- Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)
- [Context Engineering for Agents -- LangChain](https://blog.langchain.com/context-engineering-for-agents/)
- [AGENTS.md Standard](https://agents.md/)
- [Google Developer Knowledge API and MCP Server](https://developers.googleblog.com/introducing-the-developer-knowledge-api-and-mcp-server/)
- [Claude Code Hooks Guide](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code LSP Support](https://www.aifreeapi.com/en/posts/claude-code-lsp)
- [Agent Client Protocol -- PromptLayer](https://blog.promptlayer.com/agent-client-protocol-the-lsp-for-ai-coding-agents/)
- [Aider Repository Map](https://aider.chat/docs/repomap.html)
- [Zilliz claude-context MCP Server](https://github.com/zilliztech/claude-context)
- [claude-mem Plugin](https://github.com/thedotmack/claude-mem)
- [AI Rules Sync (AIS)](https://github.com/lbb00/ai-rules-sync)
- [ai-rulez Universal Configuration Manager](https://github.com/Goldziher/ai-rulez)
- [VS Code Full MCP Spec Support](https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support)
- [Spotify Background Coding Agents Feedback Loops](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3)
- [MATLAB MCP Server Coding Guidelines](https://blogs.mathworks.com/deep-learning/2025/12/11/matlab-mcp-server-update-bringing-your-coding-guidelines-directly-to-ai/)
- [Docker Sandboxes for Agent Safety](https://www.docker.com/blog/docker-sandboxes-a-new-approach-for-coding-agent-safety/)
- [Cursor MCP Features](https://webrix.ai/blog/cursor-mcp-features-blog-post)
- [MCP-LSP Bridge Server](https://github.com/axivo/mcp-lsp)

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
| Cursor IDE | No | Partial | Yes (.mdc) | Yes (SKILL.md, v2.4+) |
| Cursor CLI | Yes (Bash) | Yes (file read) | Yes (.mdc) | Yes (SKILL.md, v2.4+) |
| Aider | Yes (Bash) | Yes (file read) | No | No |
| Cline/Roo Code | Yes (Bash) | Yes (file read) | No (mode-scoped) | No |
| Amazon Q | Limited | Partial | No | No |
| GitHub Copilot | Limited | Partial | No | Yes (.github/skills/) |

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
7. **Leverage .1merge/ for tool-specific unique features** — glob rules, mode definitions, priority levels, Memory Bank files
8. **MCP is the universal bridge** — invest in MCP servers for cross-tool capability gaps (embeddings, documentation, GAB traversal)
9. **Compaction-safe context must be defined** — critical rules survive context window compression
10. **Use both context chaining and reference chaining** — critical rules need a static+dynamic load path and a static+dynamic pointer path

---

*Multi-avenue redundancy documentation for the 0Agnostic System*
*Created: 2026-02-16*
*Updated: 2026-02-17 — Added JSON-LD traversal methods, unique per-tool avenues (10 tools), unexplored avenues (21 avenues), new tool coverage (Cursor CLI, Amazon Q, Cline/Roo Code, GitHub Copilot), updated summary table (12 tools)*
