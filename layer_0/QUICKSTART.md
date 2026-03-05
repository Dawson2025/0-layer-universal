---
resource_id: "ffd23c12-2351-46db-83d6-0948b628467c"
resource_type: "document"
resource_name: "QUICKSTART"
---
# Quick Start Guide - Better AI System

<!-- section_id: "51d322bb-e5bc-4e68-a096-4f057c1c5b3a" -->
## 5-Minute Setup

<!-- section_id: "bbab1539-f1a3-412a-8847-625c2dea66b3" -->
### 1. Read Your Context (30 seconds)

```bash
# Read the tool-agnostic context
cat 0AGNOSTIC.md

# Or read tool-specific (auto-generated)
cat CLAUDE.md  # For Claude Code
```

<!-- section_id: "ce90402c-e599-428c-948d-d1e87f71db09" -->
### 2. Check Previous Sessions (30 seconds)

```bash
# See what happened before
cat .0agnostic/episodic_memory/index.md

# Read specific session
cat .0agnostic/episodic_memory/sessions/2026-01-30_session_001.md
```

<!-- section_id: "6184c99f-890b-43cd-9ad8-90ccab476694" -->
### 3. Start Working

You now have full context. Begin your task.

---

<!-- section_id: "8a9850b8-5812-4c7e-8e4a-eac336285888" -->
## Essential Commands

<!-- section_id: "ead6e673-1146-4e83-9524-e1c024997ee4" -->
### Finding Information

```bash
# Search for content using /find skill
# Read: .0agnostic/skills/find.md for full instructions

# Quick search helper
bash .0agnostic/scripts/find-helper.sh search "SHIMI"
bash .0agnostic/scripts/find-helper.sh all  # List all indices
```

<!-- section_id: "4e5a41f0-7682-4fb4-b96e-092cff67d535" -->
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

<!-- section_id: "32513df1-86f9-44a4-984d-bc9aaf4740f3" -->
### Creating Session Records

```bash
# Quick session creation
bash .0agnostic/scripts/create-session.sh "my_agent" "Brief summary of work" "COMPLETED"

# Then edit the created file to add details
```

<!-- section_id: "238fbee4-a775-4fc4-8d7a-dfce2a2ddcc8" -->
### Generating Tool-Specific Files

```bash
# After editing 0AGNOSTIC.md, regenerate tool files
bash .0agnostic/agnostic-sync.sh .
```

---

<!-- section_id: "118fd785-2885-43f0-9c5e-6095131c2191" -->
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

<!-- section_id: "9a7baa4d-23d8-461c-9f72-5a99f3f6e83d" -->
## Common Workflows

<!-- section_id: "586905bc-19f1-446d-b0d5-d51b36384d3a" -->
### Starting a New Session

1. `cat 0AGNOSTIC.md` - Read context
2. `cat .0agnostic/episodic_memory/index.md` - Check history
3. Work on your task
4. Create session file when done

<!-- section_id: "174ee37e-e19b-469f-925c-c409a64d1611" -->
### Finding Where Something Is

1. Read `0INDEX.md` at current directory
2. Follow keywords to relevant child
3. Repeat until found
4. Or use: `bash .0agnostic/scripts/find-helper.sh search "keyword"`

<!-- section_id: "55ccbd17-2e77-4bb6-85ff-93bb436fb0c8" -->
### Modifying Shared Outputs

1. Acquire lock
2. Make changes (atomic writes)
3. Track changes
4. Release lock
5. Create session record

<!-- section_id: "834dddaf-2bd4-442c-819c-15e173df0ea7" -->
### Syncing Tool-Specific Files

1. Edit `0AGNOSTIC.md` (source of truth)
2. Run `bash .0agnostic/agnostic-sync.sh .`
3. All tool files (CLAUDE.md, etc.) updated

---

<!-- section_id: "e37fe0ed-070c-47c8-9eba-932684ea3a3b" -->
## Key Concepts

| Concept | What It Does |
|---------|--------------|
| **0AGNOSTIC.md** | Single source of truth, tool-agnostic |
| **Episodic Memory** | Prevents agent amnesia across sessions |
| **File Locking** | Prevents multi-agent conflicts |
| **0INDEX.md** | Enables /find skill navigation |

---

<!-- section_id: "1f780945-a69e-4f05-96b6-7b71b3233536" -->
## Need More Help?

- **Full rules**: `.0agnostic/rules/`
- **All scripts**: `.0agnostic/scripts/`
- **Skill docs**: `.0agnostic/skills/`
- **Test everything**: `bash .0agnostic/tests/integration-test.sh`

---

*Quick Start for Better AI System - Tool-agnostic, amnesia-free, conflict-safe*

