# 0AGNOSTIC System Implementation Instructions

**Date**: 2026-01-30
**Stage**: stage_-1_03_instructions
**Status**: FINISHED - Ready for Design
**Revision**: 1.0

---

## Overview

The **AGNOSTIC System** enables tool-portable AI context by:

1. **0AGNOSTIC.md** (tool-agnostic source)
   - ~200-400 token lean context file
   - Always loaded by AI agent
   - Contains: Identity, Triggers, Pointers

2. **.0agnostic/** (structured on-demand resources)
   - Skills, rules, agents, automation scripts
   - Loaded only when needed
   - Keeps main context lean

3. **agnostic-sync.sh** (transformation script)
   - Generates tool-specific formats from source
   - CLAUDE.md (Claude), AGENTS.md (AutoGen), GEMINI.md (Gemini)
   - Preserves tool-specific files during sync

---

## Constraint 1: 0AGNOSTIC.md Structure

### Purpose

One lean, always-loaded context file that:
- Fits in every AI tool's context window
- Provides enough info for agent to function
- Points to detailed information (on-demand)

### Template

```markdown
# 0AGNOSTIC.md - [Layer/Stage Name]

## Identity
Who am I? What is my role and scope?

- **Role**: [Agent role]
- **Layer**: [Layer number]
- **Stage**: [Stage number (if applicable)]
- **Scope**: [What I can/cannot do]
- **Parent**: [Where to escalate]

## Navigation
How do I understand this system?

- **Self**: This file (always loaded)
- **Detailed context**: `.0agnostic/` folder (on-demand)
- **Universal rules**: `layer_0_group/` (read once per session)
- **Specific scope**: [Link to CLAUDE.md or similar]

## Triggers
When should I use different capabilities?

| Trigger | Action |
|---------|--------|
| **Need rules?** | Load `.0agnostic/rules/` |
| **Need examples?** | Load `.0agnostic/agents/` |
| **Need skills?** | Load `.0agnostic/skills/` |

## Pointers
Where are key resources?

- **Setup**: Run `./agnostic-sync.sh` to generate tool-specific files
- **Status**: Check `status.json` for current state
- **Help**: Read `.0agnostic/README.md`

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Generated from this file (don't edit) |
| `AGENTS.md` | AutoGen format (generated) |
| `GEMINI.md` | Google Gemini format (generated) |
| `.0agnostic/` | Detailed resources (on-demand) |

## Standards

1. **Output-First**: Write outputs to files before responding
2. **Episodic Memory**: Log all work to outputs/episodic/
3. **Handoffs**: Use hand_off_documents/ for agent communication
4. **Atomic**: Use .tmp files, atomic rename for writes

---

[Optional: Add specific content for your role]
```

### Content Guidelines

**Identity Section** (Required):
- ✅ Role, Layer, Stage, Scope
- ✅ Who is my parent? Who are my children (if any)?
- ❌ Don't duplicate information from parent context

**Navigation Section** (Required):
- ✅ Links to .0agnostic/ resources
- ✅ Link to universal rules (layer_0)
- ❌ Don't list every file (use .0agnostic/ instead)

**Triggers Section** (Required):
- ✅ When to load each resource
- ✅ Examples: "Need rules? Load ..."
- ❌ Don't explain how everything works (save for detailed docs)

**Pointers Section** (Required):
- ✅ Key file locations
- ✅ How to setup or extend
- ❌ Don't repeat system structure (assumed known)

**Token Budget**:
- Target: 200-400 tokens
- **Never exceed**: 500 tokens (or it won't fit in small context)
- Use bullets, tables, short links to save tokens

---

## Constraint 2: .0agnostic/ Folder Structure

### Purpose

On-demand resources kept separate from lean context file. Only loaded when agent explicitly needs them.

### Standard Structure

```
.0agnostic/
├── README.md              ← Overview of all resources
├── rules/
│   ├── multi_agent_sync_protocol.md
│   ├── conflict_resolution.md
│   └── episodic_memory.md
├── skills/
│   ├── skill_1/
│   │   ├── SKILL.md       ← Official Anthropic skill format
│   │   ├── scripts/
│   │   │   └── implementation.sh
│   │   └── references/
│   │       └── docs.md
│   └── skill_2/
│       └── SKILL.md
├── agents/
│   ├── agent_example.md   ← Example agent configurations
│   └── agent_specialization.md
├── automation/
│   ├── setup.sh           ← Setup scripts
│   ├── validate.sh        ← Validation scripts
│   └── repair.sh          ← Repair/recovery scripts
└── templates/
    ├── 0AGNOSTIC.md.template
    └── handoff_template.md
```

### Naming Convention

**Use `.0agnostic/` not `.agnostic/`:**
- ✅ `.0agnostic/` (sorts first, explicit ordering)
- ❌ `.agnostic/` (sorts alphabetically with other files)

**Use `0AGNOSTIC.md` not `AGNOSTIC.md`:**
- ✅ `0AGNOSTIC.md` (sorts first in listings)
- ❌ `AGNOSTIC.md` (sorts alphabetically)

**Why**: File listing puts metadata files first, avoiding "I looked but didn't see it" problems.

### Content Rules

**Keep 0AGNOSTIC.md small** (200-400 tokens):
- Move detailed content to .0agnostic/
- Use .0agnostic/ for anything >50 lines

**Keep .0agnostic/ organized**:
- Each skill gets its own folder
- Each rule gets its own file
- README.md explains what each resource does

**Documentation Standards**:
- Every file has header: purpose, when to read, revision
- Cross-references use relative paths
- Examples show actual usage

---

## Constraint 3: agnostic-sync.sh Behavior

### Purpose

Transform 0AGNOSTIC.md + .0agnostic/ into tool-specific formats automatically.

### Transformation Rules

| Source | Target | Transformation |
|--------|--------|-----------------|
| `0AGNOSTIC.md` | `CLAUDE.md` | Use as-is (Claude native) |
| `0AGNOSTIC.md` | `AGENTS.md` | Convert tables, remove Claude-specific |
| `0AGNOSTIC.md` | `GEMINI.md` | Convert to Gemini format |
| `.0agnostic/skills/` | `.claude/skills/` | Copy structure (Claude) |
| `.0agnostic/rules/` | Embedded in CLAUDE.md | Include key rules |

### Generated Files

**CLAUDE.md** - Claude Code format:
```markdown
# [Auto-generated from 0AGNOSTIC.md]
# Edit 0AGNOSTIC.md, then run: agnostic-sync.sh
# Generated: [timestamp]

[0AGNOSTIC.md content here]

---

## Key Rules

[Rules from .0agnostic/rules/ embedded]

---

## Available Skills

[List skills from .0agnostic/skills/]
```

**AGENTS.md** - AutoGen format:
```yaml
# [Auto-generated from 0AGNOSTIC.md]
# Edit 0AGNOSTIC.md, then run: agnostic-sync.sh

agent:
  name: [Role from Identity]
  description: [From 0AGNOSTIC.md]
  skills: [List from .0agnostic/skills/]
  rules: [List from .0agnostic/rules/]
```

### File Preservation

**NEVER overwrite these tool-specific files:**
- `settings.json` (tool settings)
- `mcp.json` (MCP server configs)
- `.claude/mcp.json` (Claude-specific)
- Custom scripts in `.claude/commands/`

**Always preserve** by excluding from sync:

```bash
# In agnostic-sync.sh:
preserve_patterns=(
  "settings.json"
  "mcp.json"
  ".claude/mcp.json"
  ".claude/commands/*"
  ".claude/scripts/*"
)
```

### Sync Behavior

```bash
# Run to update CLAUDE.md, AGENTS.md, GEMINI.md:
./agnostic-sync.sh

# Options:
./agnostic-sync.sh --dry-run    # Show what will change, don't commit
./agnostic-sync.sh --force      # Force update even if files exist
./agnostic-sync.sh --verbose    # Show detailed output
```

**Never commit** generated files to git:
- ✅ Commit: 0AGNOSTIC.md, .0agnostic/
- ✅ Commit: agnostic-sync.sh
- ❌ Commit: CLAUDE.md, AGENTS.md, GEMINI.md, .claude/skills/

---

## Implementation: Three Stages

### Stage 1: Create 0AGNOSTIC.md (IMMEDIATE)

**At each layer/stage that needs context:**

1. Copy template from `layer_0_group/.../templates/0AGNOSTIC.md.template`
2. Fill in Identity section (who am I?)
3. Fill in Navigation section (where are my resources?)
4. Keep under 400 tokens
5. Test: Can you understand your role from this file alone?

**Locations to start:**

```
~/0_layer_universal/layer_0_group/0AGNOSTIC.md
~/0_layer_universal/layer_1/0AGNOSTIC.md
~/0_layer_universal/layer_-1_research/0AGNOSTIC.md
~/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_-1_group/layer_-1_99_stages/stage_-1_02_research/0AGNOSTIC.md
```

**Deliverable**: 5-10 0AGNOSTIC.md files at key layers/stages

### Stage 2: Build .0agnostic/ Resources (NEXT)

**For each 0AGNOSTIC.md, create .0agnostic/ folder:**

1. Create `.0agnostic/README.md` (list what's available)
2. Add rules: `rules/multi_agent_sync_protocol.md`, etc.
3. Add skills: `skills/[skill_name]/SKILL.md`
4. Add templates for new agents to use

**Example .0agnostic/ structure:**

```
stage_-1_02_research/.0agnostic/
├── README.md
├── rules/
│   ├── research_protocol.md
│   └── output_first_protocol.md
├── skills/
│   ├── 02_research-workflow/
│   │   └── SKILL.md
│   └── handoff-protocol/
│       └── SKILL.md
└── templates/
    └── research_output_template.md
```

### Stage 3: Run agnostic-sync.sh (FINAL)

**For each .0agnostic/ folder:**

1. Run `agnostic-sync.sh` in that directory
2. Verify generated CLAUDE.md, AGENTS.md, GEMINI.md
3. Test: Can tool load context and execute?
4. Commit 0AGNOSTIC.md + .0agnostic/, not generated files

**Commands:**

```bash
# Test what will be generated:
./agnostic-sync.sh --dry-run --verbose

# Generate for real:
./agnostic-sync.sh

# Verify no generated files in git:
git status | grep -E "CLAUDE.md|AGENTS.md|GEMINI.md"  # Should be empty
```

---

## CLAUDE.md Integration

When .0agnostic/ system is active, each generated CLAUDE.md should include:

```markdown
## [MANDATORY] Using the AGNOSTIC System

This file was generated from `0AGNOSTIC.md`.

### To Modify Context
1. Edit `0AGNOSTIC.md` (not this file)
2. Run: `./agnostic-sync.sh`
3. Verify: `git status` shows no changed CLAUDE.md
4. (Generated files are not committed)

### To Add Resources
1. Create file in `.0agnostic/rules/`, `.0agnostic/skills/`, etc.
2. Reference in `0AGNOSTIC.md` triggers section
3. Run: `./agnostic-sync.sh`
4. Test: New resource available in context

### To Use in Different Tool
1. Run: `./agnostic-sync.sh` (generates AGENTS.md, GEMINI.md)
2. Copy AGENTS.md to your AutoGen config
3. Copy GEMINI.md to your Gemini prompt
4. Keep 0AGNOSTIC.md as source of truth
```

---

## Testing the System

### Test 1: Create 0AGNOSTIC.md

- [ ] Create `0AGNOSTIC.md` in test directory
- [ ] Fill in Identity section
- [ ] Under 400 tokens?
- [ ] Can you understand role from file alone?

### Test 2: Run agnostic-sync.sh

- [ ] Run `agnostic-sync.sh` in directory with 0AGNOSTIC.md
- [ ] CLAUDE.md generated successfully?
- [ ] Content matches 0AGNOSTIC.md?
- [ ] AGENTS.md, GEMINI.md also generated?

### Test 3: Verify Not Committed

- [ ] `git add .` in directory
- [ ] `git status` shows: 0AGNOSTIC.md ✅, .0agnostic/ ✅
- [ ] `git status` shows: CLAUDE.md ❌, AGENTS.md ❌, GEMINI.md ❌

### Test 4: Use in Tool

- [ ] Provide CLAUDE.md to Claude (copy content)
- [ ] Agent understands its role?
- [ ] Agent can navigate to .0agnostic/ resources?
- [ ] Skill loading works?

### Test 5: Modify and Resync

- [ ] Edit 0AGNOSTIC.md (change description)
- [ ] Run `./agnostic-sync.sh`
- [ ] CLAUDE.md reflects change?
- [ ] No merge conflicts?

---

## Success Criteria

✅ **AGNOSTIC system is working when:**

1. Single 0AGNOSTIC.md per context layer/stage
2. CLAUDE.md generated automatically
3. No tool-specific files committed to git
4. Agent understands role from 0AGNOSTIC.md alone
5. Resources in .0agnostic/ are on-demand (not always loaded)
6. Same source (0AGNOSTIC.md) works across tools

❌ **Needs improvement if:**

1. Multiple CLAUDE.md versions (conflicting edits)
2. agnostic-sync.sh fails or overwrites needed files
3. 0AGNOSTIC.md exceeds 500 tokens (too much always-loaded content)
4. Resources in 0AGNOSTIC.md that should be in .0agnostic/
5. Tool-specific customizations lost after sync

---

## Maintenance

### When to Review

- **Monthly**: Check that .0agnostic/ resources are up-to-date
- **Per session**: Run agnostic-sync.sh before committing
- **When adding feature**: Add skill or rule to .0agnostic/

### Updating 0AGNOSTIC.md

```bash
# Edit 0AGNOSTIC.md:
vim 0AGNOSTIC.md

# Check token count:
wc -w 0AGNOSTIC.md  # Should be 40-200 words (~200-400 tokens)

# Test sync:
./agnostic-sync.sh --dry-run

# If dry run looks good:
./agnostic-sync.sh

# Commit:
git add 0AGNOSTIC.md .0agnostic/
git commit -m "[AI Context] Updated 0AGNOSTIC context"
git push
```

---

## Migration Path (If Existing CLAUDE.md)

If you have existing CLAUDE.md:

1. **Extract to 0AGNOSTIC.md**:
   - Keep Identity, Navigation, Triggers (~300 tokens)
   - Move detailed content to .0agnostic/

2. **Organize into .0agnostic/**:
   - Rules → .0agnostic/rules/
   - Skills → .0agnostic/skills/
   - Examples → .0agnostic/agents/

3. **Test agnostic-sync.sh**:
   - Verify generated CLAUDE.md matches original behavior
   - Test in tool

4. **Commit**:
   - Add: 0AGNOSTIC.md, .0agnostic/, agnostic-sync.sh
   - Ignore: CLAUDE.md, AGENTS.md, GEMINI.md (add to .gitignore)
   - Remove: Old CLAUDE.md from git

