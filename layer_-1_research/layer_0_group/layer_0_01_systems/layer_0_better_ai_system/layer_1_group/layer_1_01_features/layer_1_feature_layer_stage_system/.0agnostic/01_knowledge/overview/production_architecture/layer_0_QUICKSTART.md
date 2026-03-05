---
resource_id: "940c22cb-9fbb-4d1a-bcca-38b9d4daa999"
resource_type: "knowledge"
resource_name: "layer_0_QUICKSTART"
---
# Quick Start Guide - Better AI System

<!-- section_id: "070bf538-c38c-46fb-852f-7ffb58948a2b" -->
## 5-Minute Setup

<!-- section_id: "a4eebe9c-3878-4039-9302-b4e7a770d066" -->
### 1. Read Your Context (30 seconds)

```bash
# Read the tool-agnostic context
cat 0AGNOSTIC.md

# Or read tool-specific (auto-generated)
cat CLAUDE.md  # For Claude Code
```

<!-- section_id: "971f6e6a-d68d-4cb1-bc97-37f47763b425" -->
### 2. Check Previous Sessions (30 seconds)

```bash
# See what happened before
cat outputs/episodic/index.md

# Read specific session
cat outputs/episodic/sessions/2026-01-30_session_001.md
```

<!-- section_id: "6a82a2c1-be0a-46f3-bcde-588efa4bb29a" -->
### 3. Start Working

You now have full context. Begin your task.

---

<!-- section_id: "fab45f2e-fef9-4d12-b50f-8052d00018d1" -->
## Essential Commands

<!-- section_id: "ce796e26-c800-45cc-abae-2bf2f9528c9b" -->
### Finding Information

```bash
# Search for content using /find skill
# Read: .0agnostic/skills/find.md for full instructions

# Quick search helper
bash .0agnostic/scripts/find-helper.sh search "SHIMI"
bash .0agnostic/scripts/find-helper.sh all  # List all indices
```

<!-- section_id: "01d5e9e8-bcb7-4c21-aa10-215d9c5186e4" -->
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

<!-- section_id: "391f5625-31cc-47eb-8909-694f9cc0b96b" -->
### Creating Session Records

```bash
# Quick session creation
bash .0agnostic/scripts/create-session.sh "my_agent" "Brief summary of work" "COMPLETED"

# Then edit the created file to add details
```

<!-- section_id: "cb311fbd-d13c-4c74-88b9-ffb1c4e653f3" -->
### Generating Tool-Specific Files

```bash
# After editing 0AGNOSTIC.md, regenerate tool files
bash .0agnostic/agnostic-sync.sh .
```

---

<!-- section_id: "ad7de260-32ee-4a46-9bbf-214db2d11ec3" -->
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
└── outputs/episodic/
    ├── sessions/         # Session records
    ├── changes/          # divergence.log, conflicts.log
    └── index.md          # Session index
```

---

<!-- section_id: "c060ad4d-8505-46be-be8d-034600623312" -->
## Common Workflows

<!-- section_id: "6f7b2721-3a45-4171-b5cc-d1692aa659ae" -->
### Starting a New Session

1. `cat 0AGNOSTIC.md` - Read context
2. `cat outputs/episodic/index.md` - Check history
3. Work on your task
4. Create session file when done

<!-- section_id: "03fc12b4-d445-42ab-9dfa-1341f9442fdf" -->
### Finding Where Something Is

1. Read `0INDEX.md` at current directory
2. Follow keywords to relevant child
3. Repeat until found
4. Or use: `bash .0agnostic/scripts/find-helper.sh search "keyword"`

<!-- section_id: "5d13e708-52a6-416e-9286-e1fa82bbb29a" -->
### Modifying Shared Outputs

1. Acquire lock
2. Make changes (atomic writes)
3. Track changes
4. Release lock
5. Create session record

<!-- section_id: "d06c7482-43b2-4bc0-be12-d640265b1a57" -->
### Syncing Tool-Specific Files

1. Edit `0AGNOSTIC.md` (source of truth)
2. Run `bash .0agnostic/agnostic-sync.sh .`
3. All tool files (CLAUDE.md, etc.) updated

---

<!-- section_id: "121e7a53-7f00-419d-8379-540066f24ef0" -->
## Key Concepts

| Concept | What It Does |
|---------|--------------|
| **0AGNOSTIC.md** | Single source of truth, tool-agnostic |
| **Episodic Memory** | Prevents agent amnesia across sessions |
| **File Locking** | Prevents multi-agent conflicts |
| **0INDEX.md** | Enables /find skill navigation |

---

<!-- section_id: "95bececc-a0db-445f-a201-4ef01d6b5d14" -->
## Need More Help?

- **Full rules**: `.0agnostic/rules/`
- **All scripts**: `.0agnostic/scripts/`
- **Skill docs**: `.0agnostic/skills/`
- **Test everything**: `bash .0agnostic/tests/integration-test.sh`

---

*Quick Start for Better AI System - Tool-agnostic, amnesia-free, conflict-safe*

