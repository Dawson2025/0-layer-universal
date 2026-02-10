# Rule Propagation Problem

**Status**: In Progress
**Related Needs**: rule_compliant, persistent_knowledge, discoverable
**Date**: 2026-01-26
**Updated**: 2026-01-26

---

## Problem Statement

Universal rules defined in the Layer-Stage system are NOT automatically applied to all sessions.

### The Actual Rules Location

Rules are properly organized in:
```
layer_0_group/layer_0_04_sub_layers/sub_layer_0_02_rules/
├── AI_CONTEXT_MODIFICATION_PROTOCOL.md   ← Show diagram before modifying
├── AI_CONTEXT_COMMIT_PUSH_RULE.md        ← Commit/push after changes
├── AI_DOCUMENTATION_PROTOCOL.md
├── CROSS_OS_COMPATIBILITY_RULES.md
├── LAYER_CONTEXT_HEADER_PROTOCOL.md
├── safety_governance.md
├── sequential_development_methodology.md
└── 0_instruction_docs/
    ├── git_commit_rule.md
    ├── MASTER_TERMINAL_EXECUTION_REFERENCE.md
    └── subagent_usage_decision_matrix.md
```

### The Problem

CLAUDE.md didn't properly instruct AI to traverse and read these rules.

### Example

User defined rules about git commit/push in `0_layer_universal/CLAUDE.md`:
- "Ask before git push"
- "Ask before git commit"
- "Ask before making filesystem changes"

**Session A** (started in `0_layer_universal/`):
- Rules loaded via CLAUDE.md cascade
- AI follows the rules

**Session B** (started in `/home/dawson/`):
- Outside the tree
- Rules NOT loaded
- AI doesn't know about the rules

### Root Cause

Claude Code's CLAUDE.md cascade only walks UP from the current directory:

```
Session starts at: /home/dawson
Claude Code looks for CLAUDE.md in:
  /home/dawson/CLAUDE.md         ← Not found
  /home/CLAUDE.md                ← Not found
  /CLAUDE.md                     ← Not found

Never reaches: /home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
```

---

## Impact

| Scenario | Impact |
|----------|--------|
| User starts session outside project tree | No rules loaded |
| Rules defined deep in hierarchy | Only apply to that branch |
| Universal preferences | Must be duplicated or won't apply |

---

## Potential Solutions

### Option A: Global Claude Settings File

Claude Code could support a global `~/.claude/CLAUDE.md` or `~/.claude/settings.json` with rules:

```
~/.claude/
└── CLAUDE.md    ← Always loaded first, then cascade from CWD
```

**Pros**: True universality
**Cons**: Requires Claude Code feature change (outside our control)

### Option B: Symlink/Include Pattern

Create symlinks or include directives:

```
/home/dawson/CLAUDE.md → symlink to 0_layer_universal/CLAUDE.md
```

**Pros**: Works with current Claude Code
**Cons**: Must maintain symlinks, clutters home directory

### Option C: Always Start From Root

Convention: Always start Claude Code from within `0_layer_universal/`:

```bash
cd ~/dawson-workspace/code/0_layer_universal && claude
```

**Pros**: Simple, no changes needed
**Cons**: Relies on user behavior, easy to forget

### Option D: Startup Script/Alias

Create alias that ensures correct starting point:

```bash
alias ai='cd ~/dawson-workspace/code/0_layer_universal && claude'
```

**Pros**: Enforces correct behavior
**Cons**: Only works for this machine, must remember to use alias

### Option E: CLAUDE.md Tells AI to Read Universal Rules

Add instruction in root CLAUDE.md:

```markdown
## Universal Rules
ALWAYS read and follow rules from:
/home/dawson/dawson-workspace/code/0_layer_universal/RULES.md

Do this FIRST before any other action.
```

**Pros**: Self-bootstrapping
**Cons**: Circular - only works if CLAUDE.md is loaded!

### Option F: Use ~/.claude/settings.json for Rules

Claude Code does support `~/.claude/settings.json`. Could it include rules?

Need to research if this supports custom instructions or just permissions.

---

## Recommended Approach

**Short-term**: Option C + Option D
- Create alias to always start from correct location
- Document as required practice

**Medium-term**: Research Option A + Option F
- Investigate if Claude Code supports global CLAUDE.md
- Test if settings.json can include instructions

**Long-term**: Advocate for Option A
- Request feature from Anthropic: global CLAUDE.md support

---

## Immediate Action Items

1. [ ] Add universal rules to `0_layer_universal/CLAUDE.md`
2. [ ] Create alias `ai` that starts Claude from correct directory
3. [ ] Research Claude Code's support for global settings
4. [ ] Document starting procedure in system README

---

## Related Research

- Claude Code documentation on CLAUDE.md loading
- ~/.claude/ structure and capabilities
- How other AI tools handle global configuration

---

## Solution Implemented

### Updated CLAUDE.md

The root CLAUDE.md now:
1. **Tells AI to read rules FIRST** from `sub_layer_0_02_rules/`
2. **Provides navigation table** for sub-layers and stages
3. **Stays lean** - navigation guide, not content container
4. **References .claude/** for tool permissions

### CLAUDE.md Pattern

```markdown
## FIRST: Read Universal Rules

**BEFORE doing any work**, read and follow rules from:
layer_0_group/layer_0_04_sub_layers/sub_layer_0_02_rules/

## Navigation: How to Find Things

| Sub-Layer | Purpose | When to Read |
|-----------|---------|--------------|
| sub_layer_0_02_rules/ | Universal rules | ALWAYS |
...
```

---

## How .claude/ Fits Into The System

### Current State

```
0_layer_universal/
├── .claude/
│   └── settings.json    ← Tool permissions only
│
└── layer_-1_research/.../stage_-1_02_research/
    └── .claude/
        └── settings.json    ← Context (stage, layer, purpose)
```

### Root .claude/settings.json
```json
{
  "permissions": {
    "allowedTools": ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Task"]
  }
}
```

### Stage .claude/settings.json
```json
{
  "context": {
    "stage": "stage_-1_02_research",
    "layer": -1,
    "purpose": "Explore problem space, gather information"
  },
  "permissions": { "allow": [], "deny": [], "ask": [] },
  "env": {},
  "hooks": {}
}
```

### Proposed: Use .claude/ for Rule References

Could add to root `.claude/settings.json`:
```json
{
  "permissions": { ... },
  "rules": {
    "universal": "layer_0_group/layer_0_04_sub_layers/sub_layer_0_02_rules/",
    "always_read": [
      "AI_CONTEXT_MODIFICATION_PROTOCOL.md",
      "AI_CONTEXT_COMMIT_PUSH_RULE.md"
    ]
  }
}
```

**Note**: This would require Claude Code to support custom fields. Currently it only uses `permissions`.

---

## Remaining Issues

### Issue 1: Sessions Outside Tree

If session starts from `/home/dawson/` (outside tree), CLAUDE.md isn't loaded.

**Solutions**:
- Always start from within `0_layer_universal/`
- Create alias: `alias ai='cd ~/dawson-workspace/code/0_layer_universal && claude'`
- Request global CLAUDE.md support from Anthropic

### Issue 2: AI Must Choose to Read Rules

CLAUDE.md says "read rules first" but doesn't enforce it.

**Solutions**:
- Make it very prominent in CLAUDE.md (done)
- Add to sub-layer prompts
- Consider hooks (if Claude Code supports)

---

## Actual Rules (From sub_layer_0_02_rules/)

### AI_CONTEXT_MODIFICATION_PROTOCOL.md
- **Show diagram** before modifying AI context files
- Wait for **explicit user approval**
- Only then proceed

### AI_CONTEXT_COMMIT_PUSH_RULE.md
- After approved changes: **stage, commit, push**
- Applies to all `0_layer_universal/` modifications

### safety_governance.md
- Permission levels by layer
- Filesystem/network/command boundaries
- Human-in-the-loop gates
