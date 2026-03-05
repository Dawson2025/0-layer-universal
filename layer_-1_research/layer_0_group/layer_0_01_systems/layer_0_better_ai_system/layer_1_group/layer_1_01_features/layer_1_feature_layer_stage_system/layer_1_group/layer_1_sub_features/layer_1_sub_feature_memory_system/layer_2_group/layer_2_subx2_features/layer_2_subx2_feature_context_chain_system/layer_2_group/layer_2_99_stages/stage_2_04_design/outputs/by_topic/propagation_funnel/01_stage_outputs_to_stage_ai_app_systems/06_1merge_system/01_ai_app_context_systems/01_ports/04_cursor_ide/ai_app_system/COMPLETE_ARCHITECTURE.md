---
resource_id: "ab9fb9fc-5be9-4e0b-8e57-9b1fbc922506"
resource_type: "output"
resource_name: "COMPLETE_ARCHITECTURE"
---
# Cursor IDE — Complete Architecture

**Date**: 2026-02-27
**Focus**: How native mechanisms + application-implemented strategy work together

---

## System Overview

Cursor IDE combines **native mechanisms** (what it provides) with **application-implemented strategy** (what you provide):

```
┌──────────────────────────────────────────────┐
│ Cursor IDE Native Mechanisms                 │
├──────────────────────────────────────────────┤
│ • .cursor/rules configuration system         │
│ • Semantic search (embeddings + index)       │
│ • Memory Bank (persistent state)             │
│ • Tab context (automatic IDE context)        │
│ • MCP integration (tool routing)             │
│ • Agent CLI (autonomous execution)           │
│ • Hooks system (automation triggers)         │
│ • Built-in AI assistant (Claude/GPT-4)       │
│ • Cloud agents (remote execution)            │
│ • VS Code fork architecture                  │
└──────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────┐
│ Your Strategy (What You Provide)             │
├──────────────────────────────────────────────┤
│ • .cursor/rules content (conventions)        │
│ • Memory Bank organization (what to store)   │
│ • MCP server selection & config              │
│ • Hooks configuration (automation)           │
│ • Semantic search queries (when/how)         │
│ • Agent task definition (what to delegate)   │
│ • IDE workflow (how to work effectively)     │
└──────────────────────────────────────────────┘
                           ↓
                    Working System
```

---

## Request-Response Flow

### When You Ask Cursor IDE

```
1. You type in chat sidebar or invoke inline suggestion

2. Cursor IDE prepares context:
   ├─ Current file content
   ├─ Current selection
   ├─ Open tabs (file list)
   ├─ .cursor/rules files (applied)
   ├─ Relevant memories (from Memory Bank)
   └─ File path (for rule matching)

3. Cursor routes to AI model:
   ├─ Claude (default)
   ├─ GPT-4 (if configured)
   └─ Other (if custom endpoint)

4. AI generates response:
   ├─ Applies rules from .cursor/rules
   ├─ References memories if relevant
   ├─ Understands code context
   └─ Streams response in real-time

5. Cursor IDE displays response:
   ├─ Chat sidebar (for chat mode)
   ├─ Inline suggestions (for completion)
   ├─ Code insertion (if requested)
   └─ Saves to Memory Bank (if user saves memory)

6. Optional: Agent CLI execution
   ├─ User approves before shell commands
   ├─ Cursor Agent executes task
   ├─ State persists across turns
   └─ Results shown in terminal/IDE
```

---

## Context Loading Pipeline

### Step 1: File Context

**Cursor Does**:
1. Monitor current file
2. Detect file type and language
3. Include file content in request
4. Include cursor position/selection

**You Control**:
- Which files are open (visibility)
- Whether context is used (always on)

### Step 2: Load .cursor/rules

**Cursor Does**:
1. Find `.cursor/rules/` directory (project or global)
2. Parse all YAML files
3. Merge by precedence (global → project → component-specific)
4. Apply "Always Apply" rules to every request

**You Control**:
- Rule content (what conventions matter)
- Rule organization (global vs. project)
- Rule application mode (Always Apply, Intelligently, etc.)

### Step 3: Load Memory Bank

**Cursor Does**:
1. Scan `~/.cursor/memory_bank/` for memories
2. Find relevant memories (by context or user selection)
3. Include memory content in request

**You Control**:
- What memories exist
- When to create/update memories
- Which memories to reference

### Step 4: Prepare MCP Tools

**Cursor Does**:
1. Read `.cursor/mcp.json` configuration
2. Launch MCP servers
3. List available tools
4. Make tools available to AI

**You Control**:
- Which servers to configure
- Server credentials
- When to use specific tools

### Step 5: Route to AI Model

**Cursor Does**:
1. Determine model (Claude, GPT-4, etc.)
2. Set generation parameters
3. Stream tokens in real-time

**You Control**:
- Model selection (via config)
- Generation parameters (temperature, max_tokens)

### Step 6: Execute (Optional)

**If Agent CLI**:
1. Parse task description
2. Autonomously execute steps
3. Request user approval for shell commands
4. Save session state

**You Control**:
- Task definition (what to delegate)
- Approval policy (interactive or batch)

---

## Context Composition

At any point, Cursor IDE includes:

```
┌─ Current File Content
├─ Cursor Position/Selection
├─ Open Tabs List
├─ .cursor/rules (parsed & merged)
├─ Relevant Memory Bank entries
├─ MCP tool descriptions
├─ Model configuration
└─ Available response space
```

**Token Budget** (typical):
- ~100-500 tokens: Current file
- ~50-200 tokens: Selection context
- ~200-500 tokens: Applied rules
- ~200-1000 tokens: Memory Bank
- ~100-200 tokens: MCP tool descriptions
- ~X tokens: Response space (remainder)

---

## Rule Application Examples

### Example 1: Code Style

**Rule File** (`~/.cursor/rules/javascript-style.md`):
```yaml
---
mode: "Always Apply"
---
- Use camelCase for variables
- Use PascalCase for components
- Prefer const over let
```

**Effect**:
- Every JavaScript file gets these rules
- Cursor suggests code following these patterns
- Code completion respects these conventions

### Example 2: Project-Specific Rules

**Rule File** (`project/.cursor/rules/project-patterns.md`):
```yaml
---
mode: "Intelligently"
glob: "src/**/*.tsx"
---
- All components use hooks
- State management via Redux
- API calls via custom hook
```

**Effect**:
- Cursor applies these rules when editing React components
- Suggests patterns specific to your project

### Example 3: Security Rules

**Rule File** (`~/.cursor/rules/security.md`):
```yaml
---
mode: "Always Apply"
---
- Never hardcode API keys
- Validate all inputs
- Use HTTPS for external requests
- Sanitize HTML content
```

**Effect**:
- Every code suggestion includes security awareness
- Cursor warns about insecure patterns

---

## Memory Bank Integration

### When Memory Matters

```
Session 1:
- You work on authentication module
- Cursor asks questions, learns context
- You create memory: "Auth module decisions and patterns"

Later (different session):
- You open auth-related file
- Cursor detects relevance
- Automatically includes memory
- Understands your past decisions
- Suggests consistent patterns
```

---

## Agent CLI Execution Flow

```
$ cursor agent "Refactor src/auth.js to async/await"

1. Cursor Agent reads task
2. Analyzes current project structure
3. Loads relevant rules and memories
4. Plans refactoring steps
5. Asks for approval before each shell command
6. Executes: "mv src/auth.js src/auth.js.bak" (USER APPROVES)
7. Executes: "npm test" (USER APPROVES)
8. Generates refactored code
9. Saves state (resumable session)
10. Reports completion

Output:
✅ Refactored 15 functions to async/await
✅ All tests passing (1200ms)
⚠️ Need to update type definitions in auth.d.ts (manual)
```

---

## Hooks Execution

### File Save Trigger

```
1. User saves file: src/utils.js

2. Cursor checks hooks:
   ├─ pre-save: eslint --fix matches (src/**/*.js)
   ├─ pre-save: Run eslint --fix src/utils.js
   ├─ Wait for completion...
   ├─ File saved

3. post-save: npm test matches (src/**/*.test.js)
   └─ File doesn't match, skip

Result: Code auto-formatted, user didn't need to run eslint manually
```

---

## Semantic Search Example

### Query: "How do we handle authentication?"

```
1. User opens semantic search (Cmd/Ctrl + Shift + /)
2. Types: "How do we handle authentication?"
3. Cursor generates embeddings for query
4. Searches vector index
5. Returns top results:
   - src/auth/login.ts (94% match)
   - src/middleware/auth.ts (89% match)
   - src/hooks/useAuth.ts (85% match)
6. User jumps to most relevant file
7. Context already loaded in Memory Bank
```

---

## The System Works When

✅ **.cursor/rules are accurate** (reflect your actual conventions)
✅ **Memory Bank is maintained** (memories updated, stale ones removed)
✅ **MCP servers are configured** (only needed tools enabled)
✅ **Hooks are tested** (automation doesn't slow IDE)
✅ **Semantic search queries are specific** (natural language, not keywords)
✅ **Agent tasks are bounded** (specific and safe)
✅ **IDE workflow matches your style** (chat-first vs. code-first)
✅ **Rules and memories updated together** (consistency)

The system fails when any of these are missing or outdated.

---

## Workflow Patterns

### Chat-First Pattern
- Start with chat sidebar discussion
- Clarify requirements with AI
- Get outline before implementation
- Use inline suggestions for filling details

### Code-First Pattern
- Write code normally
- Use inline suggestions for auto-completion
- Ask chat for explanations/refactoring
- Let Agent CLI handle bulk changes

### Memory-Driven Pattern
- Create comprehensive project memory
- Reference memory in chat
- Delegate consistent work to Agent CLI
- Update memory as project evolves

---

## Performance Optimization

### Keep IDE Responsive
- Minimize rule file count (merge related rules)
- Keep Memory Bank lean (archive old memories)
- Disable unused MCP servers
- Test hooks don't create bottlenecks

### Optimize Token Usage
- Use inline suggestions (cheaper than chat)
- Keep rules concise (no unnecessary details)
- Reference external docs instead of embedding
- Use Memory Bank selectively (not every file)

