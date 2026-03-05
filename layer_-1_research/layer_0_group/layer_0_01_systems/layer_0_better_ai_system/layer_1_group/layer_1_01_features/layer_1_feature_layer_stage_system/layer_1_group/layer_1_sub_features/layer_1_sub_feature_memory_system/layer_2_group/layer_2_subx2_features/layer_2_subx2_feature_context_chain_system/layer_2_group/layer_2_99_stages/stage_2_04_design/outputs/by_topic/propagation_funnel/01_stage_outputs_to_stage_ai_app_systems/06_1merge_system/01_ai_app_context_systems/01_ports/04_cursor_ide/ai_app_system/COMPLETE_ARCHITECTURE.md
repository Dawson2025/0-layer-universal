---
resource_id: "ab9fb9fc-5be9-4e0b-8e57-9b1fbc922506"
resource_type: "output"
resource_name: "COMPLETE_ARCHITECTURE"
---
# Cursor IDE — Complete Architecture

**Date**: 2026-02-27
**Focus**: How native mechanisms + application-implemented strategy work together

---

<!-- section_id: "0950d03b-6b0d-4b3c-af84-aa57c858c852" -->
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

<!-- section_id: "ce9f70ba-9848-43cf-bca1-75370664409f" -->
## Request-Response Flow

<!-- section_id: "4d3c6ae1-7d82-431c-a2f2-16fa8bf5f517" -->
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

<!-- section_id: "3aaf9104-b517-4565-baeb-36d66dc97944" -->
## Context Loading Pipeline

<!-- section_id: "0af9134b-c440-46b5-a57e-73132b52b488" -->
### Step 1: File Context

**Cursor Does**:
1. Monitor current file
2. Detect file type and language
3. Include file content in request
4. Include cursor position/selection

**You Control**:
- Which files are open (visibility)
- Whether context is used (always on)

<!-- section_id: "cd921142-7ce9-4d9a-af55-2c66f2cff410" -->
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

<!-- section_id: "a68bf6b6-07e7-415b-89d6-2da8607573a5" -->
### Step 3: Load Memory Bank

**Cursor Does**:
1. Scan `~/.cursor/memory_bank/` for memories
2. Find relevant memories (by context or user selection)
3. Include memory content in request

**You Control**:
- What memories exist
- When to create/update memories
- Which memories to reference

<!-- section_id: "6483a10b-d1ad-4c09-9f59-9c68405afe52" -->
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

<!-- section_id: "38782d3a-8a25-4728-841e-451989a2dc51" -->
### Step 5: Route to AI Model

**Cursor Does**:
1. Determine model (Claude, GPT-4, etc.)
2. Set generation parameters
3. Stream tokens in real-time

**You Control**:
- Model selection (via config)
- Generation parameters (temperature, max_tokens)

<!-- section_id: "7c6cbbeb-9ffd-4e5a-9ddd-73b9d3e5ae6c" -->
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

<!-- section_id: "7936a619-163b-44bc-b9c8-dc24221165ce" -->
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

<!-- section_id: "47267910-cd06-4047-a668-f518fde63181" -->
## Rule Application Examples

<!-- section_id: "a3bae4c9-16c0-4ff9-bc83-e728e11fd809" -->
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

<!-- section_id: "fc153d9b-4027-4c64-8b48-8e4726dd40cf" -->
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

<!-- section_id: "c40117a0-2151-4736-b155-0e6f99412c43" -->
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

<!-- section_id: "bfec3ffb-34c5-44f1-b254-a5bd833ffeb6" -->
## Memory Bank Integration

<!-- section_id: "4cbe3939-ef5c-4bf0-8d2e-1cb3c8b97f2f" -->
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

<!-- section_id: "356eb557-c7cd-4225-a0d3-e403c1283dc0" -->
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

<!-- section_id: "28664480-4e94-485c-87df-0fa47322c52c" -->
## Hooks Execution

<!-- section_id: "c1639046-702b-46cb-9326-1b2de374b579" -->
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

<!-- section_id: "2cbcf37e-2c0e-49c1-a9c2-221ea872bdf4" -->
## Semantic Search Example

<!-- section_id: "7d558630-2a77-477d-bb7f-83b0f9817c9f" -->
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

<!-- section_id: "49a85f0b-e183-4bf7-acff-56e252bf6108" -->
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

<!-- section_id: "c63583d1-fd47-4b45-bd07-9716c77701d7" -->
## Workflow Patterns

<!-- section_id: "7e3e6545-5567-4907-90d1-b41d2ef440cf" -->
### Chat-First Pattern
- Start with chat sidebar discussion
- Clarify requirements with AI
- Get outline before implementation
- Use inline suggestions for filling details

<!-- section_id: "48798063-4c07-4ab3-9cb0-8e4fe0743fcb" -->
### Code-First Pattern
- Write code normally
- Use inline suggestions for auto-completion
- Ask chat for explanations/refactoring
- Let Agent CLI handle bulk changes

<!-- section_id: "9039c302-804f-4b8e-b3f8-7a7bf461f6e5" -->
### Memory-Driven Pattern
- Create comprehensive project memory
- Reference memory in chat
- Delegate consistent work to Agent CLI
- Update memory as project evolves

---

<!-- section_id: "8dc6f6cc-057a-49af-8e55-f2f89d50493e" -->
## Performance Optimization

<!-- section_id: "20c6f547-8ac9-4dcd-8e39-6c20c3aa7564" -->
### Keep IDE Responsive
- Minimize rule file count (merge related rules)
- Keep Memory Bank lean (archive old memories)
- Disable unused MCP servers
- Test hooks don't create bottlenecks

<!-- section_id: "d5ded2c5-b09e-4354-955b-e3697ed7e47b" -->
### Optimize Token Usage
- Use inline suggestions (cheaper than chat)
- Keep rules concise (no unnecessary details)
- Reference external docs instead of embedding
- Use Memory Bank selectively (not every file)

