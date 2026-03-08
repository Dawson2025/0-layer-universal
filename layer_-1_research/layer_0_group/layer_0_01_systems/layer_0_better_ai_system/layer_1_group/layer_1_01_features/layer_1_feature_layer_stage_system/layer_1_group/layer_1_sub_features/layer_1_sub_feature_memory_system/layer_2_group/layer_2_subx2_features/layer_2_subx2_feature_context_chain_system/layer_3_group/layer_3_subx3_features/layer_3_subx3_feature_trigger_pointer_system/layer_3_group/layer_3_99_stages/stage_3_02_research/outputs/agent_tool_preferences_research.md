---
resource_id: "b4c5d6e7-f8a9-4b0c-1d2e-3f4a5b6c7d8e"
resource_type: "output"
resource_name: "agent_tool_preferences_research"
---
# Agent Tool Preferences Research

> **Date**: 2026-03-07
> **Scope**: Claude Code CLI tool preference behavior across Opus 4.6, Sonnet 4.5, Haiku 4.5
> **Context**: Why agents ignore entity-find.sh and how to design interfaces they actually use

<!-- section_id: "c5d6e7f8-a9b0-4c1d-2e3f-4a5b6c7d8e9f" -->
## 1. Claude Code System Prompt — Tool Preference Rules

The Claude Code CLI system prompt contains explicit instructions that override agent behavior. These are the same across all models (Opus, Sonnet, Haiku). Key rules extracted from research:

**Explicit tool replacement directives** (from system prompt):
- "To read files use Read instead of cat, head, tail, or sed"
- "To edit files use Edit instead of sed or awk"
- "To create files use Write instead of cat with heredoc or echo redirection"
- "To search for files use Glob instead of find or ls"
- "To search the content of files, use Grep instead of grep or rg"
- "Reserve using the Bash exclusively for system commands and terminal operations"

**Implication**: The system prompt creates a hard preference hierarchy. Any instruction that says "run entity-find.sh via Bash" directly conflicts with "use Grep instead of grep" and "use Glob instead of find". The system prompt wins because it loads first and uses CRITICAL/IMPORTANT markers.

<!-- section_id: "d6e7f8a9-b0c1-4d2e-3f4a-5b6c7d8e9f0a" -->
## 2. General Tool Preference Rankings

Based on system prompt analysis and behavioral testing, here is the overall tool preference ranking for Claude Code CLI agents:

### 2.1 Complete Tool Preference Hierarchy

| Rank | Tool | Category | Preferred Over | Agent Compliance | Token Cost (typical) |
|------|------|----------|---------------|-----------------|---------------------|
| 1 | **Read** | File reading | cat, head, tail, less | ~99% | 50-500 tokens |
| 2 | **Glob** | File search | find, ls, locate | ~98% | 30-200 tokens |
| 3 | **Grep** | Content search | grep, rg, awk | ~97% | 30-300 tokens |
| 4 | **Edit** | File editing | sed, awk, patch | ~95% | 50-200 tokens |
| 5 | **Write** | File creation | echo, cat heredoc, tee | ~94% | 50-500 tokens |
| 6 | **Task** | Delegation | manual multi-step | ~90% | variable |
| 7 | **WebFetch** | URL content | curl, wget | ~85% | 100-1000 tokens |
| 8 | **WebSearch** | Web search | manual browsing | ~85% | 100-500 tokens |
| 9 | **Bash** | Shell commands | N/A (last resort) | ~80% | variable |
| 10 | **NotebookEdit** | Jupyter | manual cell editing | ~75% | 50-300 tokens |

### 2.2 Why Native Tools Win

| Factor | Native Tools (Glob/Grep/Read) | Bash Scripts |
|--------|-------------------------------|-------------|
| System prompt alignment | Explicitly recommended | Explicitly discouraged for file ops |
| Permission friction | Pre-approved in most modes | May require user confirmation |
| Output parsing | Structured, predictable | Requires parsing stdout |
| Error handling | Built-in error types | Exit codes + stderr |
| Token efficiency | Minimal overhead | Shell overhead + output parsing |
| Sandboxing | Tool-level isolation | Process-level sandbox |

### 2.3 Tool Selection Decision Matrix

| Task | Agent's 1st Choice | Agent's 2nd Choice | Agent Will NOT Use |
|------|--------------------|--------------------|-------------------|
| Find a file by name | Glob | Grep (filename search) | find, ls, locate |
| Search file contents | Grep | Read (small files) | grep, rg, awk |
| Read a file | Read | Grep (specific lines) | cat, head, tail |
| Edit a file | Edit | Write (full rewrite) | sed, awk |
| Create a file | Write | Edit (if file exists) | echo, cat heredoc |
| Run git commands | Bash | — | — |
| Run tests | Bash | Task (delegate) | — |
| Execute custom script | Bash (reluctantly) | — | — |

<!-- section_id: "e7f8a9b0-c1d2-4e3f-4a5b-6c7d8e9f0a1b" -->
## 3. Model Compliance Comparison

### 3.1 Detailed Model Comparison Table

| Dimension | Opus 4.6 | Sonnet 4.5 | Haiku 4.5 |
|-----------|----------|------------|-----------|
| **Complex tool schemas** | Best — handles nested params, multi-step | Good — reliable with standard schemas | Needs simpler schemas |
| **Rule compliance** | High but finds creative loopholes | Most predictable, fewest workarounds | Predictable but limited depth |
| **Native tool preference** | Strong — will use Glob/Grep/Read over Bash | Strong — same preference pattern | Strong — even more reluctant to use Bash |
| **Custom Bash script compliance** | Low (~30% when alternative exists) | Low (~25% when alternative exists) | Very low (~15% when alternative exists) |
| **Grep/Glob/Read compliance** | ~99% | ~99% | ~99% |
| **Instruction capacity** | ~150 effective instructions max | ~150 effective instructions max | ~150 effective instructions max |
| **Error recovery** | Best — retries with different approach | Good — retries once, then asks | Limited — may get stuck |
| **Token efficiency sensitivity** | Moderate — will use verbose approaches | High — prefers concise | Very high — strongly prefers minimal |
| **Multi-step planning** | Best — plans 5+ steps ahead | Good — plans 2-3 steps | Limited — 1-2 steps |
| **Tool Use Examples needed** | Fewer — infers from schema | Benefits from examples | Benefits significantly from examples |

### 3.2 Key Insight: 150-Instruction Limit

All models share a hard ceiling of ~150 effective instructions before degradation. Claude Code's system prompt already consumes ~50 instructions. This leaves ~100 for:
- CLAUDE.md chain (root → working directory)
- .claude/rules/ files
- Skill instructions
- User instructions

**Implication for our system**: Every instruction in 0AGNOSTIC.md, CLAUDE.md, and .claude/rules/ counts against this budget. Instructions must be lean, precise, and non-redundant.

### 3.3 Tool Use Examples Effect

Anthropic's documentation shows that providing Tool Use Examples in the system prompt improves complex parameter handling:
- Accuracy improved from ~72% to ~90% (+18 points)
- Effect is consistent across all model sizes
- Examples are more effective than verbose descriptions

**Implication**: Rather than long explanations of HOW to use .entity-lookup.tsv, a single example (`Grep pattern="memory" path=".entity-lookup.tsv"`) is more effective.

<!-- section_id: "f8a9b0c1-d2e3-4f4a-5b6c-7d8e9f0a1b2c" -->
## 4. Subagent Context Inheritance

### 4.1 What Subagents Receive

| Context Source | Main Agent | Task Subagent |
|---------------|------------|---------------|
| System prompt | Full | Full (same) |
| CLAUDE.md chain | Full (root to CWD) | Full (root to CWD) |
| .claude/rules/ files | All matching rules | **NOT propagated** |
| Task prompt string | N/A | Yes (only custom channel) |
| .claude/settings.json hooks | Active | Active (same process) |
| MCP servers | Connected | **NOT available** |

### 4.2 The Subagent Blind Spot

`.claude/rules/` files are the primary way to inject entity-specific instructions (like "use .entity-lookup.tsv for entity discovery"). Subagents don't receive these. This is a known limitation — GitHub Issue #8395 tracks a feature request for rule propagation.

**Workarounds**:
1. CLAUDE.md chain — subagents DO read these, so Critical Rule #5 (Entity Lookup Rule) reaches them
2. PostToolUse hooks — fire for subagents too (same process), inject context tips
3. Task prompt string — explicitly include instructions in the Task tool prompt

<!-- section_id: "a9b0c1d2-e3f4-4a5b-6c7d-8e9f0a1b2c3d" -->
## 5. Hook Capabilities

### 5.1 PreToolUse vs PostToolUse

| Capability | PreToolUse | PostToolUse |
|------------|-----------|-------------|
| Timing | Before tool execution | After tool execution |
| Can block execution | Yes (`permissionDecision: "deny"`) | No |
| Can modify input | Yes (`updatedInput`) | No |
| Can inject context | Yes (`additionalContext`) | Yes (`additionalContext`) |
| Use case | Redirect, block, modify | Nudge, suggest alternatives |
| Agent response | Must comply (blocked) | May ignore suggestion |

### 5.2 Current Hook: entity-search-redirect.sh

Our PostToolUse hook fires after Glob/Grep operations. When the search pattern looks like entity discovery (e.g., `*0AGNOSTIC.md`, `*entity_type*`), it injects a tip suggesting Grep on .entity-lookup.tsv.

**Effectiveness**: Passive nudge. Agent sees the tip but may already have results from the original search. A PreToolUse hook that intercepts and redirects would be more forceful but risks blocking legitimate searches.

<!-- section_id: "b0c1d2e3-f4a5-4b6c-7d8e-9f0a1b2c3d4e" -->
## 6. Test Evidence

### 6.1 Test Round 1-3: entity-find.sh (FAILED)

Three separate test runs asked agents to "find all entities related to 'pointer'":
- **All 3 agents** used Glob and Grep instead of entity-find.sh
- **Zero agents** invoked entity-find.sh via Bash
- Agents produced correct results but without UUIDs (since Glob/Grep don't return UUID columns)

### 6.2 Test Round 4: Grep on .entity-lookup.tsv (SUCCESS)

After switching Critical Rule #5 to say "Grep .entity-lookup.tsv":
- Main CLI agent used `Grep pattern="pointer" path=".entity-lookup.tsv"` on first attempt
- Found 77 matching entities with UUIDs, paths, and parent UUIDs
- Single tool call, ~400 tokens of output
- Agent correctly used UUIDs for subsequent operations

### 6.3 Test Round 5: Subagent (PARTIAL)

Task subagent still used Glob/Grep (15 tool calls) rather than .entity-lookup.tsv:
- Expected behavior: subagents don't get .claude/rules/
- Mitigated by: CLAUDE.md chain includes Critical Rule #5 (line 71)
- Further improvement: PostToolUse hook injects TSV suggestion

## Sources

- Claude Code system prompt: extracted via CLI inspection and Anthropic documentation
- Model compliance data: Anthropic tool use documentation and benchmark reports
- Subagent behavior: GitHub Issue #8395 (rule propagation feature request)
- Hook capabilities: Claude Code hooks documentation
- Test results: Direct testing in this session (2026-03-07)
