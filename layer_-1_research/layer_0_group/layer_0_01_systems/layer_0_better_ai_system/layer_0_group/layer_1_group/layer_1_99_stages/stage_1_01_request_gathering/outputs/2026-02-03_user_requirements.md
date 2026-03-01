# User Requirements - 2026-02-03

## Session Context

User session discussing AI context flow architecture improvements.

---

## Requirements Identified

### 1. Stage Completeness

**User Statement**: "never skip stages, we need all of them even if we aren't going to fill each of them currently"

**Requirement**: All 11 stages must always be created when an entity uses stages. Empty stages are valid; missing stages are not.

---

### 2. Propagation Chain Architecture

**User Statement**: "you are forgetting that we need to make changes to 0AGNOSTIC.md and .0agnostic first, and then propagate those changes to the specific ai tools"

**Requirement**: Changes must flow through the proper propagation chain:
1. Knowledge (sub_layer docs)
2. → .0agnostic/ (skills)
3. → Tool-specific files (CLAUDE.md, GEMINI.md, AGENTS.md)
4. → Tool folders (.claude/, .gemini/, .codex/)

---

### 3. Minimal Tool Files with Pointers

**User Statement**: "CLAUDE.md files need to only have identity, critical rules, triggers, and pointers, and then point to the . folders like .claude and the skills folder"

**Requirement**: CLAUDE.md (and equivalent) should be minimal:
- Identity
- Critical rules
- Triggers
- Pointers to .claude/, skills/

---

### 4. Skills with References

**User Statement**: "skills folder in .claude, with SKILLS.md files, which can have references/ folder which has references to the sublayers and stages"

**Requirement**: Skills should have:
- SKILL.md (instructions/protocol)
- references/ folder (pointers to knowledge docs, not duplicates)

---

### 5. Architecture Diagrams Required

**User Statement**: "i want to see this kind of architecture diagramming when we want to make changes or updates to the context like this"

**Requirement**: All AI context changes must include propagation chain diagrams showing how the change flows through the system.

---

### 6. Merge Folder Consolidation

**User Statement**: "i want to combine and organize the merge folders into one .1merge folder"

**Requirement**: Consolidate `.1*_merge/` folders under single `.1merge/` parent while keeping original names.

---

### 7. Research Documentation

**User Statement**: "i want the things i say to be documented in the research stages"

**Requirement**: User decisions and requirements should be documented in the appropriate research stages where they belong.

---

## Summary

| # | Requirement | Stage to Document |
|---|-------------|-------------------|
| 1 | Stage Completeness Rule | 03_instructions |
| 2 | Propagation Chain | 05_design |
| 3 | Minimal CLAUDE.md | 05_design |
| 4 | Skills with References | 05_design |
| 5 | Diagrams Required | 03_instructions |
| 6 | .1merge consolidation | 05_design |
| 7 | Document in stages | 03_instructions |
