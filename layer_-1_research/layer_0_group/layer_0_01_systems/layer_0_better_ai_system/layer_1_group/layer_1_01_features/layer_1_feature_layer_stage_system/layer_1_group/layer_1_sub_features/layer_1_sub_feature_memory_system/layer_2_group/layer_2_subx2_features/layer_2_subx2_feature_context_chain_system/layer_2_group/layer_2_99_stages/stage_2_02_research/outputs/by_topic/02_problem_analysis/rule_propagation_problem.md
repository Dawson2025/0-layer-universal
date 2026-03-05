---
resource_id: "fa72d574-66be-474a-a8d2-b8e1427b3a7d"
resource_type: "output"
resource_name: "rule_propagation_problem"
---
# Rule Propagation Problem

**Status**: In Progress
**Related Needs**: rule_compliant, persistent_knowledge, discoverable
**Date**: 2026-01-26
**Updated**: 2026-01-26

---

<!-- section_id: "c99cc80b-5439-4797-8271-d40230f8b4b7" -->
## Problem Statement

Universal rules defined in the Layer-Stage system are NOT automatically applied to all sessions.

<!-- section_id: "9c15c75e-d687-4831-9d44-1367f4b1bf4f" -->
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

<!-- section_id: "35ff0662-13ad-47d5-bbc9-84b1bc1f00e3" -->
### The Problem

CLAUDE.md didn't properly instruct AI to traverse and read these rules.

<!-- section_id: "abb56262-614e-4e6d-8e24-efecc8188816" -->
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

<!-- section_id: "e957c7af-3c87-41aa-bbde-afd89489dfe0" -->
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

<!-- section_id: "4e5b24e3-5201-4da1-b664-1044ae86954a" -->
## Impact

| Scenario | Impact |
|----------|--------|
| User starts session outside project tree | No rules loaded |
| Rules defined deep in hierarchy | Only apply to that branch |
| Universal preferences | Must be duplicated or won't apply |

---

<!-- section_id: "55765214-88a5-4174-8c27-130a59b21692" -->
## Potential Solutions

<!-- section_id: "55ec3730-bf43-4c9c-92a5-577c28710399" -->
### Option A: Global Claude Settings File

Claude Code could support a global `~/.claude/CLAUDE.md` or `~/.claude/settings.json` with rules:

```
~/.claude/
└── CLAUDE.md    ← Always loaded first, then cascade from CWD
```

**Pros**: True universality
**Cons**: Requires Claude Code feature change (outside our control)

<!-- section_id: "7a9aca22-b7f1-447b-99eb-6ca70d55f7cf" -->
### Option B: Symlink/Include Pattern

Create symlinks or include directives:

```
/home/dawson/CLAUDE.md → symlink to 0_layer_universal/CLAUDE.md
```

**Pros**: Works with current Claude Code
**Cons**: Must maintain symlinks, clutters home directory

<!-- section_id: "a5f70329-dc9f-4339-95a6-42188e57832e" -->
### Option C: Always Start From Root

Convention: Always start Claude Code from within `0_layer_universal/`:

```bash
cd ~/dawson-workspace/code/0_layer_universal && claude
```

**Pros**: Simple, no changes needed
**Cons**: Relies on user behavior, easy to forget

<!-- section_id: "fd113bef-183b-4879-beb6-dd7c3ee9ea12" -->
### Option D: Startup Script/Alias

Create alias that ensures correct starting point:

```bash
alias ai='cd ~/dawson-workspace/code/0_layer_universal && claude'
```

**Pros**: Enforces correct behavior
**Cons**: Only works for this machine, must remember to use alias

<!-- section_id: "6555e298-645a-4942-b49e-0bdd702d59d4" -->
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

<!-- section_id: "a24adbb6-995e-4705-b783-f01c4d97a9b0" -->
### Option F: Use ~/.claude/settings.json for Rules

Claude Code does support `~/.claude/settings.json`. Could it include rules?

Need to research if this supports custom instructions or just permissions.

---

<!-- section_id: "18d41a82-2070-45a4-9404-5de76fc8c119" -->
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

<!-- section_id: "404a014e-b122-4ca8-b725-f62e68ba323a" -->
## Immediate Action Items

1. [ ] Add universal rules to `0_layer_universal/CLAUDE.md`
2. [ ] Create alias `ai` that starts Claude from correct directory
3. [ ] Research Claude Code's support for global settings
4. [ ] Document starting procedure in system README

---

<!-- section_id: "5489c808-9da3-4397-b93f-4b5c4fed6d18" -->
## Related Research

- Claude Code documentation on CLAUDE.md loading
- ~/.claude/ structure and capabilities
- How other AI tools handle global configuration

---

<!-- section_id: "6cf3a665-7ef9-4396-8a72-7d97bec6ef49" -->
## Solution Implemented

<!-- section_id: "8b421818-6e16-4bf5-8aad-f9e324acd015" -->
### Updated CLAUDE.md

The root CLAUDE.md now:
1. **Tells AI to read rules FIRST** from `sub_layer_0_02_rules/`
2. **Provides navigation table** for sub-layers and stages
3. **Stays lean** - navigation guide, not content container
4. **References .claude/** for tool permissions

<!-- section_id: "55de7b91-b241-4d8d-a439-922714395bca" -->
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

<!-- section_id: "83580034-b796-438e-a262-9b096d39ab6d" -->
## How .claude/ Fits Into The System

<!-- section_id: "46a2ea5d-e47c-426a-8189-01fe705751a5" -->
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

<!-- section_id: "84845f76-cad5-4361-9cb6-e868a59730a6" -->
### Root .claude/settings.json
```json
{
  "permissions": {
    "allowedTools": ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Task"]
  }
}
```

<!-- section_id: "97f21feb-729c-4491-916a-6f9082135ffe" -->
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

<!-- section_id: "e603af77-f35f-48e4-841b-e0e82d294d05" -->
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

<!-- section_id: "1b998c49-c05a-4f17-976e-2d705eb97ed6" -->
## Remaining Issues

<!-- section_id: "f23aadcb-2f13-4efe-9e0f-a3c316118e7c" -->
### Issue 1: Sessions Outside Tree

If session starts from `/home/dawson/` (outside tree), CLAUDE.md isn't loaded.

**Solutions**:
- Always start from within `0_layer_universal/`
- Create alias: `alias ai='cd ~/dawson-workspace/code/0_layer_universal && claude'`
- Request global CLAUDE.md support from Anthropic

<!-- section_id: "531bc4a2-a8c5-4bd2-8e3f-8750d526257e" -->
### Issue 2: AI Must Choose to Read Rules

CLAUDE.md says "read rules first" but doesn't enforce it.

**Solutions**:
- Make it very prominent in CLAUDE.md (done)
- Add to sub-layer prompts
- Consider hooks (if Claude Code supports)

---

<!-- section_id: "bc558fa4-1948-4d8b-9b78-243ba38bc4af" -->
## Actual Rules (From sub_layer_0_02_rules/)

<!-- section_id: "62798806-717a-43e1-a863-0658f05e47f7" -->
### AI_CONTEXT_MODIFICATION_PROTOCOL.md
- **Show diagram** before modifying AI context files
- Wait for **explicit user approval**
- Only then proceed

<!-- section_id: "9b1a516c-4b1d-44e5-8539-ebec102b7f16" -->
### AI_CONTEXT_COMMIT_PUSH_RULE.md
- After approved changes: **stage, commit, push**
- Applies to all `0_layer_universal/` modifications

<!-- section_id: "372b16dc-9370-49f1-b5c5-66ca85797c50" -->
### safety_governance.md
- Permission levels by layer
- Filesystem/network/command boundaries
- Human-in-the-loop gates
