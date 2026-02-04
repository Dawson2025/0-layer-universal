# Skills Index

## Purpose

Skills provide task-specific instructions with references to knowledge. Load the relevant skill before executing a task.

---

## Available Skills

| Skill | Trigger | Folder |
|-------|---------|--------|
| entity-creation | Creating layers, stages, features, projects | `entity-creation/` |
| context-gathering | Understanding current location in hierarchy | `context-gathering/` |
| handoff-creation | Creating handoff documents | `handoff-creation/` |
| stage-workflow | Working through stages | `stage-workflow/` |

---

## How to Use Skills

1. Identify the task
2. Load the skill folder
3. Read `SKILL.md` for instructions
4. Read files in `references/` for detailed knowledge
5. Execute following the skill protocol

---

## Skill Structure

```
skill-name/
├── SKILL.md              ← Instructions and protocol
└── references/           ← Pointers to knowledge docs
    └── (symlinks or paths to sub_layer docs)
```

---

*Skills are synced to tool-specific folders (.claude/skills/, .codex/skills/, etc.) via agnostic-sync.sh*
