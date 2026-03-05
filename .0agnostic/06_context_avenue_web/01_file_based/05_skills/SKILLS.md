---
resource_id: "46856c54-d6ac-428d-ab64-6abb559c8ecb"
resource_type: "document"
resource_name: "SKILLS"
---
# Skills Index

<!-- section_id: "6b05d5ed-3a63-4e1f-9ec2-6cdb9d11fbda" -->
## Purpose

Skills provide task-specific instructions with references to knowledge. Load the relevant skill before executing a task.

---

<!-- section_id: "2d79cef5-95dd-4586-aa13-9c4f0180359d" -->
## Available Skills

| Skill | Trigger | Folder |
|-------|---------|--------|
| entity-creation | Creating layers, stages, features, projects | `entity-creation/` |
| context-gathering | Understanding current location in hierarchy | `context-gathering/` |
| handoff-creation | Creating handoff documents | `handoff-creation/` |
| stage-workflow | Working through stages | `stage-workflow/` |

---

<!-- section_id: "2400f669-c150-4d54-b8fb-d5aa216fa3a3" -->
## How to Use Skills

1. Identify the task
2. Load the skill folder
3. Read `SKILL.md` for instructions
4. Read files in `references/` for detailed knowledge
5. Execute following the skill protocol

---

<!-- section_id: "f73d1e43-da95-4a1f-a910-7b46aaf62538" -->
## Skill Structure

```
skill-name/
├── SKILL.md              ← Instructions and protocol
└── references/           ← Pointers to knowledge docs
    └── (symlinks or paths to sub_layer docs)
```

---

*Skills are synced to tool-specific folders (.claude/skills/, .codex/skills/, etc.) via agnostic-sync.sh*
