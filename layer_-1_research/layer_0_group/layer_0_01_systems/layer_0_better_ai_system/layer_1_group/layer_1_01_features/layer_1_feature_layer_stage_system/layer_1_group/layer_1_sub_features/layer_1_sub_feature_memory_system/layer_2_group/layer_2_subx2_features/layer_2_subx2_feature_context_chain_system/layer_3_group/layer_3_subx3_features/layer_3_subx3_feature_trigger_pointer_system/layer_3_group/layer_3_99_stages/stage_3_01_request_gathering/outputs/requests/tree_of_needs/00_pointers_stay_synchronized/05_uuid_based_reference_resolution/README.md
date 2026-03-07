---
resource_id: "1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d"
resource_type: "output"
resource_name: "uuid_based_reference_resolution_needs"
---
# Branch 05: UUID-Based Reference Resolution

**Core Question**: How do we eliminate the "bajillion file changes" problem when anything moves?

<!-- section_id: "2b3c4d5e-6f7a-4b8c-9d0e-1f2a3b4c5d6e" -->
## Definition

> All references throughout the codebase — in scripts, documentation, context files, hooks, and AI app context surfaces — use UUID as the primary reference mechanism. Paths are derived at the moment of use via a resolution function. Moving anything requires only rebuilding the UUID index; no manual grep-and-replace across files.

---

<!-- section_id: "3c4d5e6f-7a8b-4c9d-0e1f-2a3b4c5d6e7f" -->
## The Problem

Branches 01-04 solved pointer file synchronization. But the broader problem remains: **every reference across the entire codebase uses hardcoded filesystem paths**. When anything moves — a script, a directory, an entity, a stage — all path references break.

Evidence from the script protocol migration (2026-03-07):
- Moved 12 scripts into organized protocol directories
- Had to manually update **81+ files** with new paths
- This is exactly the problem the UUID system was built to solve, but UUIDs existed only as metadata alongside paths — nothing actually resolved via UUID at runtime

What breaks when things move:
- **0AGNOSTIC.md files**: Resource tables, pointer references, command examples
- **Generated context files**: CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md
- **Scripts calling scripts**: agnostic-sync.sh calling pointer-sync.sh via hardcoded path
- **Git hooks**: pre-commit and post-merge hooks referencing scripts by path
- **Knowledge docs, rules, protocols, skills**: All contain path references
- **Stage outputs**: Design docs, implementation plans, current product descriptions

---

<!-- section_id: "4d5e6f7a-8b9c-4d0e-1f2a-3b4c5d6e7f8a" -->
## The Vision

A system where:
- **UUID is the primary reference mechanism** — scripts, docs, and context files reference things by UUID, not path
- **A `resolve-uuid` function** resolves UUID → current path at runtime (~5ms lookup)
- **`{{resolve:UUID}}` syntax** in 0AGNOSTIC.md source files gets resolved by agnostic-sync.sh during generation
- **Self-healing context files** — AI apps that can run bash resolve UUIDs at the moment of use, no stale window
- **Move workflow is trivial**: `mv` → `rebuild-index` → done. No grep-and-replace.

---

<!-- section_id: "5e6f7a8b-9c0d-4e1f-2a3b-4c5d6e7f8a9b" -->
## Three Needs

| Need | Question | Description |
|------|----------|-------------|
| need_01_resolve_uuid_function | How do references resolve at runtime? | Shell function that looks up UUID in index, returns current path |
| need_02_placeholder_syntax | How do source files reference by UUID? | `{{resolve:UUID}}` syntax in 0AGNOSTIC.md, resolved during agnostic-sync.sh generation |
| need_03_self_healing_context_files | How do AI app context files stay current? | UUID + resolve instructions in CLAUDE.md etc., apps resolve at moment of use |
| need_04_move_workflow | What's the end-to-end move workflow? | `mv` → `rebuild-index` → optional `agnostic-sync.sh` → commit |

---

<!-- section_id: "6f7a8b9c-0d1e-4f2a-3b4c-5d6e7f8a9b0c" -->
## Key Insight

The OS fundamentally requires filesystem paths at the syscall level — every `open()`, `exec()`, `source` call needs a path. But that doesn't mean source code has to contain paths. UUID is the **stable identity**; the path is a **derived, ephemeral convenience**. A one-line resolution function bridges the gap:

```bash
# Instead of:
bash ".0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh" --validate

# You write:
bash "$(resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)" --validate
```

Research confirms that **all major AI coding apps can run bash** (Claude Code, Codex CLI, Gemini CLI, Copilot CLI/VS Code, Cursor agent, Windsurf, Aider, Amazon Q, Cline, Continue.dev, Open Interpreter). This means UUID references with resolve-uuid instructions can go in **all** ported context files — no app needs pre-resolved paths as its primary mechanism.

---

<!-- section_id: "7a8b9c0d-1e2f-4a3b-4c5d-6e7f8a9b0c1d" -->
## Success Criteria

The branch is satisfied when:
- [ ] `resolve-uuid` function exists and resolves any UUID to its current path in <10ms
- [ ] Scripts use `resolve-uuid` for cross-protocol calls instead of hardcoded paths
- [ ] 0AGNOSTIC.md files use `{{resolve:UUID}}` placeholders for script/resource references
- [ ] `agnostic-sync.sh` resolves `{{resolve:UUID}}` placeholders during generation
- [ ] Generated context files (CLAUDE.md, AGENTS.md, etc.) include UUID references with resolve-uuid instructions
- [ ] Moving a file/directory/entity requires only: `mv` + `rebuild-index` — no file-by-file path updates
- [ ] Pre-commit hook validates that all UUID references resolve to existing paths
- [ ] Auto-rebuild of UUID index via git hooks (post-checkout, post-merge)
