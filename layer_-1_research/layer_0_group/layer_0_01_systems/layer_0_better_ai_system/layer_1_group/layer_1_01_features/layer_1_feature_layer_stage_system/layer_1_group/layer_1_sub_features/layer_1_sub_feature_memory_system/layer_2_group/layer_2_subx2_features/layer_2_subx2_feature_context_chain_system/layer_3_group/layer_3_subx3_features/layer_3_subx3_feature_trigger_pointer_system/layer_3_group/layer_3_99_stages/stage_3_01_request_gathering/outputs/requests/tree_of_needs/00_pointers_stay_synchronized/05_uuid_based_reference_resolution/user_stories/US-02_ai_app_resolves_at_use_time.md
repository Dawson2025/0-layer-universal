---
resource_id: "3e4f5a6b-7c8d-4e9f-0a1b-2c3d4e5f6a7b"
resource_type: "output"
resource_name: "US-02_ai_app_resolves_at_use_time"
---
# US-02: AI App Resolves References at Use Time

**Need**: [UUID-Based Reference Resolution](../README.md)

---

**As an** AI coding app (Claude Code, Codex, Gemini CLI, Copilot, Cursor, etc.) reading a CLAUDE.md or equivalent context file,
**I want** the file to contain UUID references with resolve-uuid instructions rather than hardcoded paths,
**So that** I can resolve references at the moment I need them, always getting the current path even if the context file hasn't been regenerated since the last move.

<!-- section_id: "4f5a6b7c-8d9e-4f0a-1b2c-3d4e5f6a7b8c" -->
### What Happens

1. AI app starts a session and reads CLAUDE.md (loaded automatically by the app)
2. CLAUDE.md contains a resources table with UUID references and resolve-uuid instructions:
   ```
   | pointer-sync.sh | UUID: 08a4e9bc-... | Run: resolve-uuid 08a4e9bc |
   ```
3. When the AI app needs to use pointer-sync.sh, it runs `resolve-uuid 08a4e9bc` via its bash capability
4. The function returns the current path (wherever the script lives right now)
5. The AI app uses that path — guaranteed correct, no stale reference possible

**Self-healing property:**
- Even if `agnostic-sync.sh` hasn't been re-run after a move, the AI app still resolves correctly
- The only requirement is that `pointer-sync.sh --rebuild-index` has been run (which updates the UUID → path mapping)
- There is no stale window between move and context file regeneration

<!-- section_id: "5a6b7c8d-9e0f-4a1b-2c3d-4e5f6a7b8c9d" -->
### Acceptance Criteria

- CLAUDE.md contains UUID references with resolve-uuid instructions (not just hardcoded paths)
- AI app can resolve any UUID reference by running a single bash command
- Resolution works in all major AI apps (Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor agent, Windsurf, Aider, Cline, Continue.dev)
- Resolution works in sandboxed environments (Codex, Cursor) — only reads a local JSON file
- No stale window: references work correctly even without re-running agnostic-sync.sh after a move
