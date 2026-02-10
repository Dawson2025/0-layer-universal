# Quick Start Guide - Better AI System

## 5-Minute Setup

### 1. Read Your Context (30 seconds)

```bash
# Read the tool-agnostic context
cat 0AGNOSTIC.md

# Or read tool-specific (auto-generated)
cat CLAUDE.md  # For Claude Code
```

### 2. Check Previous Sessions (30 seconds)

```bash
# See what happened before
cat .0agnostic/episodic_memory/index.md

# Read specific session
cat .0agnostic/episodic_memory/sessions/2026-01-30_session_001.md
```

### 3. Start Working

You now have full context. Begin your task.

---

## Essential Commands

### Finding Information

```bash
# Search for content using /find skill
# Read: .0agnostic/skills/find.md for full instructions

# Quick search helper
bash .0agnostic/scripts/find-helper.sh search "SHIMI"
bash .0agnostic/scripts/find-helper.sh all  # List all indices
```

### Working with Shared Files

```bash
# 1. Acquire lock before modifying
bash .0agnostic/scripts/lock-manager.sh acquire my_scope my_agent

# 2. Do your work (use atomic writes for safety)
echo "content" | bash .0agnostic/scripts/atomic-write.sh output.md

# 3. Track your change
bash .0agnostic/scripts/track-change.sh output.md CREATED my_agent

# 4. Release lock when done
bash .0agnostic/scripts/lock-manager.sh release my_scope my_agent
```

### Creating Session Records

```bash
# Quick session creation
bash .0agnostic/scripts/create-session.sh "my_agent" "Brief summary of work" "COMPLETED"

# Then edit the created file to add details
```

### Generating Tool-Specific Files

```bash
# After editing 0AGNOSTIC.md, regenerate tool files
bash .0agnostic/agnostic-sync.sh .
```

---

## Directory Structure

```
layer_0/
├── 0AGNOSTIC.md          # READ THIS FIRST (tool-agnostic context)
├── CLAUDE.md             # Auto-generated for Claude Code
├── .0agnostic/
│   ├── rules/            # Detailed rules
│   ├── scripts/          # Helper scripts
│   └── skills/           # Skill documentation (/find, etc.)
├── .locks/               # File locks (don't edit manually)
└── .0agnostic/episodic_memory/
    ├── sessions/         # Session records
    ├── changes/          # divergence.log, conflicts.log
    └── index.md          # Session index
```

---

## Common Workflows

### Starting a New Session

1. `cat 0AGNOSTIC.md` - Read context
2. `cat .0agnostic/episodic_memory/index.md` - Check history
3. Work on your task
4. Create session file when done

### Finding Where Something Is

1. Read `0INDEX.md` at current directory
2. Follow keywords to relevant child
3. Repeat until found
4. Or use: `bash .0agnostic/scripts/find-helper.sh search "keyword"`

### Modifying Shared Outputs

1. Acquire lock
2. Make changes (atomic writes)
3. Track changes
4. Release lock
5. Create session record

### Syncing Tool-Specific Files

1. Edit `0AGNOSTIC.md` (source of truth)
2. Run `bash .0agnostic/agnostic-sync.sh .`
3. All tool files (CLAUDE.md, etc.) updated

---

## Key Concepts

| Concept | What It Does |
|---------|--------------|
| **0AGNOSTIC.md** | Single source of truth, tool-agnostic |
| **Episodic Memory** | Prevents agent amnesia across sessions |
| **File Locking** | Prevents multi-agent conflicts |
| **0INDEX.md** | Enables /find skill navigation |

---

## Need More Help?

- **Full rules**: `.0agnostic/rules/`
- **All scripts**: `.0agnostic/scripts/`
- **Skill docs**: `.0agnostic/skills/`
- **Test everything**: `bash .0agnostic/tests/integration-test.sh`

---

*Quick Start for Better AI System - Tool-agnostic, amnesia-free, conflict-safe*

