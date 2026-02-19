# AutoGen Agent Context

## Identity

**Role**: Root Manager
**Scope**: Coordinates all layers in the AI context system
**Layer**: Root (contains layer_0, layer_1, layer_-1_research)




## Critical Rules

These rules apply to EVERY AI agent at this level and below:

### 1. AI Context Modification Protocol

Before modifying AI context files:
1. **Show propagation chain diagram** - source → sync → tool-specific
2. **Show before/after diagrams** - current state vs proposed
3. **Wait for user approval**
4. **Execute approved changes**

**Scope**: `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`, `.claude/`, `.0agnostic/`, `*_rules/`, `*_prompts/`, `*_knowledge/`

### 2. Stage Completeness Rule

When creating entities with stages: **ALL 11 stages MUST exist**.

Empty stages are valid. Missing stages are NOT.

**Reference**: `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md`

### 3. AI Context Commit/Push Rule

After approved changes:
1. `git add [specific files]`
2. `git commit -m "[AI Context] description"`
3. `git push`

### 4. Submodule Integrity Protocol

When any nested repository exists in a child path:
1. The parent repository MUST track it as a real submodule (mode `160000` gitlink) and MUST have a matching entry in `.gitmodules`.
2. Never leave a gitlink without `.gitmodules` mapping. This breaks recursive submodule operations.
3. Commit/push order is always bottom-up:
   - deepest child repo first
   - then each parent repo submodule pointer
   - root repo last
4. Before ending a session, run:
   - `git submodule status --recursive`
   - `find . -name .git | sed 's#/.git$##'` (sanity check for unexpected nested repos)
5. Any nested repo discovered without mapping must be either:
   - properly registered as a submodule, or
   - de-initialized as a standalone repo and converted to regular tracked files.





## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
