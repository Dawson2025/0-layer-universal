# Claude Code Enforcement System - Quick Reference

## The 5 [CRITICAL] Rules

### Rule 1: Context Modification Protocol
```
YOU WILL NOT modify AI context files without:
1. Showing a DIAGRAM with full paths
2. WAITING for explicit user APPROVAL
3. Executing EXACTLY as approved
```
**Applies to**: `CLAUDE.md`, `.claude/`, `*_rules/`, `*_prompts/`, `*_knowledge/`, `status.json`

---

### Rule 2: Commit/Push Rule
```
After approved context changes, YOU WILL:
1. git add [specific files]
2. git commit -m "[AI Context] description"
3. git push
```
**YOU WILL NOT**: Skip ops, amend commits, commit without approval

---

### Rule 3: Context Traversal Rule
```
Before starting ANY task, YOU WILL:
1. Read all CLAUDE.md files (root to working directory)
2. Identify layer (0, 1, -1) and stage (01-11)
3. Check relevant sub_layers
4. Read status.json if exists
```
**YOU WILL NOT**: Assume context, skip identification, start without understanding

---

### Rule 4: Documentation Protocol
```
Document in correct LAYER:
  layer_0/        (universal)
  layer_1/        (projects)
  layer_-1/       (research)

AND correct STAGE (01-11):
  01: request_gathering
  02: research
  03: instructions
  04: planning
  05: design
  06: development
  07: testing
  08: criticism
  09: fixing
  10: current_product
  11: archives
```

---

### Rule 5: Research and Sources Practice
```
When doing research, YOU WILL:
1. Include "Sources:" section at bottom
2. Format as markdown links: [Title](URL)
3. NOT hide or omit sources
```

---

## Enforcement Architecture

```
MACHINE LEVEL (HIGHEST)
├─ /etc/claude-code/managed-settings.json
└─ Cannot be overridden

    ↓ (Inherited)

USER LEVEL (GLOBAL)
├─ ~/.claude/CLAUDE.md (instructions)
├─ ~/.claude/settings.json (permissions)
└─ Cannot be overridden by projects

    ↓ (Can add but not remove)

PROJECT LEVEL (SPECIFIC)
├─ ./CLAUDE.md (project context)
├─ .claude/settings.json (project permissions)
└─ Cannot override parent levels
```

---

## Self-Compliance Checklist

**Before completing ANY task, verify**:

- ✅ Did I read the relevant CLAUDE.md files?
- ✅ Did I identify the current layer and stage?
- ✅ Did I follow the [CRITICAL] rules for this task type?
- ✅ If I modified context files, did I show a diagram and wait for approval?
- ✅ If I did research, did I include a Sources: section?
- ✅ If I committed changes, did I use the [AI Context] format?
- ✅ Did I document work in the correct layer and stage?

**If you cannot check ALL boxes: DO NOT complete the task.**

---

## File Locations

### Machine Level
```
/etc/claude-code/managed-settings.json
```

### User Level
```
~/.claude/CLAUDE.md
~/.claude/settings.json
~/.claude/.git/
```

### This Documentation
```
/home/dawson/dawson-workspace/code/0_layer_universal/
  layer_-1_research/layer_-1_better_ai_system/
  layer_-1/layer_-1_99_stages/stage_-1_10_current_product/

├── README.md (entry point)
├── NOTES.md (this file)
├── outputs/
│   ├── claude_code_enforcement_system.md (full guide)
│   └── setup_checklist.md (verification)
└── [other stage files]
```

---

## Common Workflows

### Adding Context Instructions
1. Modify `~/.claude/CLAUDE.md`
2. Run: `cd ~/.claude && git add CLAUDE.md`
3. Run: `git commit -m "[AI Context] description of change"`
4. Run: `git push`

### Updating Permissions
1. Modify `~/.claude/settings.json`
2. Run: `cd ~/.claude && git add settings.json`
3. Run: `git commit -m "[AI Context] permission update"`
4. Run: `git push`

### Starting a New Task
1. ✅ Read CLAUDE.md files in path (root → working directory)
2. ✅ Identify layer and stage
3. ✅ Check sub_layers if needed
4. ✅ Do your work
5. ✅ Before finishing: Run self-compliance check

### Documenting Work
1. Determine correct LAYER (0, 1, or -1)
2. Determine correct STAGE (01-11)
3. Create file in: `layer_X/layer_X_99_stages/stage_X_##_name/`
4. Add appropriate CLAUDE.md header if needed
5. Commit with git if in tracked directory

---

## Enforcement Statements

**Rule violations are NOT optional:**
- ❌ "I'll follow it next time" - NO, follow it now
- ❌ "It doesn't apply here" - Machine-level rules apply EVERYWHERE
- ❌ "I'll show a diagram later" - Diagram required BEFORE changes
- ❌ "This is just quick" - Rules apply regardless of urgency

**If you cannot follow a rule**: STOP WORK and ask for clarification.

---

## Key Phrases

| Phrase | Meaning |
|--------|---------|
| "YOU WILL" | Mandatory command - no exceptions |
| "YOU WILL NOT" | Absolute prohibition - no workarounds |
| "Failure to follow stops all work immediately" | Rule violation = task halted |
| "Before completing ANY task" | Applies universally, no exclusions |
| "Machine-level enforcement" | System-wide, cannot be bypassed |
| "Immutable" | Cannot be changed, overridden, or negotiated |

---

## Emergency Reference

**Rule 1 - When modifying context files**:
  - STOP
  - Create diagram
  - Get approval
  - Then execute

**Rule 2 - After context changes**:
  - `git add [files]`
  - `git commit -m "[AI Context] description"`
  - `git push`

**Rule 3 - Before starting tasks**:
  - Read CLAUDE.md files
  - Identify layer/stage
  - Proceed with context

**Rule 4 - When documenting**:
  - Check correct layer
  - Check correct stage
  - Place file accordingly

**Rule 5 - When researching**:
  - Include Sources: section
  - Format as markdown links
  - No exceptions

---

## Escalation

If you encounter a situation where:
- ❓ Rules conflict with each other
- ❓ A rule prevents necessary work
- ❓ You need clarification on a rule

**DO THIS**:
1. Document the conflict/issue
2. STOP WORK (do not proceed)
3. Ask for clarification
4. Wait for guidance

Do NOT:
- ❌ Guess how to apply rules
- ❌ Pick which rules to follow
- ❌ Proceed despite uncertainty

---

## Status

✅ **Machine-Level**: Active and enforced
✅ **User-Level**: Active and enforced
✅ **Project-Level**: Framework ready (inherited from above)
✅ **Documentation**: Complete

**Last Updated**: January 29, 2026
