# System Context Hierarchy - Research in Progress

**Status**: Active Research
**Date Started**: 2026-01-27
**Related Work**: `system_prompt_architecture.md` (research), `system_prompt_architecture_instructions.md` (approved)

---

## Overview

Research into how AI context files (CLAUDE.md, agnostic.md, .claude/) should be structured hierarchically across the entire filesystem from user home directory down through project layers.

## Key Findings

### 1. Claude Code CLAUDE.md Loading Behavior

**Discovery**: Claude Code walks the directory tree **upward only**, not downward.

```
When starting Claude Code at: /home/dawson/dawson-workspace/code/layer_0/
Loaded into system prompt:
  - ~/.claude/CLAUDE.md (global, always)
  - /home/dawson/CLAUDE.md (if exists)
  - /home/dawson/dawson-workspace/CLAUDE.md (if exists)
  - /home/dawson/dawson-workspace/code/CLAUDE.md (if exists)
  - /home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
  - /home/dawson/dawson-workspace/code/0_layer_universal/layer_0/CLAUDE.md

NOT loaded (child directories):
  - /home/dawson/dawson-workspace/code/0_layer_universal/layer_1/CLAUDE.md
  - Any subdirectories below CWD
```

**Implication**: Starting at the deepest relevant level (the work location) gives maximum context, not starting at the root.

### 2. Global vs. Directory-Level Context

**Finding**: Two approaches for global context:

| File | Location | When Loaded | Purpose |
|------|----------|------------|---------|
| Global CLAUDE.md | `~/.claude/CLAUDE.md` | Every session, always | User-global preferences |
| Home Directory CLAUDE.md | `~/CLAUDE.md` | Via upward walk from any CWD | Directory-specific |

**Current Implementation**: We created both:
- `/home/dawson/CLAUDE.md` (directory-level, works via walk)
- `/home/dawson/dawson-workspace/CLAUDE.md` (directory-level)
- `/home/dawson/dawson-workspace/code/CLAUDE.md` (directory-level)

**Note**: The official global location is `~/.claude/CLAUDE.md` (inside `.claude/` config folder).

### 3. Agnostic vs. Claude-Specific Context

**Pattern Discovered**:
```
any_directory/
├── CLAUDE.md      ← Claude-specific (manager roles, rules, delegations)
└── agnostic.md    ← Tool-agnostic (framework, structure, conventions)
```

**Rationale**:
- `agnostic.md` = works with any AI tool (ChatGPT, Claude, Gemini, etc.)
- `CLAUDE.md` = specific to Claude Code capabilities and patterns

**Current Implementation**: Created both at all levels:
- Root: `/home/dawson/{CLAUDE.md, agnostic.md}`
- Workspace: `/home/dawson/dawson-workspace/{CLAUDE.md, agnostic.md}`
- Code: `/home/dawson/dawson-workspace/code/{CLAUDE.md, agnostic.md}`
- System: `/home/dawson/dawson-workspace/code/0_layer_universal/{CLAUDE.md, agnostic.md}`
- Layers: Each layer (layer_0, layer_1, layer_-1_research) has both

### 4. Linux Filesystem Hierarchy Learned

**Confirmed Standard**:
```
/                    ← System root (OS-critical only)
/etc/                ← System-wide configuration
/home/               ← User home directories container
/home/USERNAME/      ← Individual user's files (this is where ~ points)
/var/                ← Runtime data (logs, caches)
/opt/                ← Third-party software
/usr/                ← System programs and libraries
```

**Key Insight**: User files NEVER go above `/home/USERNAME/`. Everything there is operating system territory.

**Multi-user Implications**:
- `/home/thomas/` is isolated from `/home/dawson/` by default (700 permissions)
- `sudo` bypasses these restrictions (runs as root)
- Password not needed if user is sudoer

### 5. Concern About Starting Agents at Higher Levels

**Question Posed**: "Is it a problem if I don't start agents from high enough in the directory tree?"

**Answer**: Not really. The upward CLAUDE.md walk ensures context accumulates. Starting too high is actually worse because:
- Agent gets less specific context in the system prompt
- Agent has too much authority scope, not enough focus

**Best Practice**: Start at the level containing all directories your task needs.

## Implementation Status

### Completed
- [x] Container-as-Manager pattern (Phase 1-4 of system prompt architecture)
- [x] Four-directional hand_off_documents at all layers/stages
- [x] CLAUDE.md files at: user root, workspace, code root, system root, and all main layers
- [x] agnostic.md files at same locations
- [x] Registry conversion (stage_00 = data only, container = manager)

### In Progress
- [ ] Apply context files to all 70+ stages containers
- [ ] Apply context files to all sub_layers containers
- [ ] Apply context files to individual stages and sub_layers
- [ ] Create .claude/ configurations at key levels

### Not Yet Attempted
- [ ] Hand_off_documents for all individual stages
- [ ] Four-directional handoffs for sub_layers
- [ ] Test delegation flows across hierarchy

## Open Questions

1. **Should we create `~/.claude/CLAUDE.md` as the official global file?** Currently relying on `/home/dawson/CLAUDE.md` via directory walk, but standard says to use `~/.claude/CLAUDE.md`.

2. **How deep should context files go?** Every stage? Every sub_layer? Or just at container levels?

3. **What should go in agnostic.md vs CLAUDE.md at each level?**
   - Currently: agnostic has framework/structure, CLAUDE has manager roles/rules
   - Could they be organized differently?

4. **Should `.claude/` folders have settings.json at every level?** Currently only at some.

## References

- `system_prompt_architecture.md` - Full architecture design
- `system_prompt_architecture_instructions.md` - Implementation instructions
- `system_prompt_architecture_plan.md` - Implementation plan
- `ai_context_filesystem_locations.md` - Where to place context files across filesystem
- Perplexity research on Claude Code behavior
- Perplexity research on Linux filesystem hierarchy

## Next Steps

1. Decide on `~/.claude/CLAUDE.md` global implementation
2. Plan Phase 5 (all remaining containers and individual stages)
3. Create test delegation scenario to verify handoff system
4. Document best practices for starting agents
