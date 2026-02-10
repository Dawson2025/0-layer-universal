# Git Commit Flow

**Purpose**: Show how context loads when an agent needs to commit changes.

---

## Current Flow: Git Commit

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    GIT COMMIT CONTEXT FLOW                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

    USER: "Commit these changes"
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 1: Agent has base context (from session start)                      │
    │                                                                           │
    │  Already loaded:                                                          │
    │  • System prompt (includes Git Safety Protocol)                           │
    │  • CLAUDE.md chain (includes AI Context Commit/Push Rule)                 │
    │                                                                           │
    │  Key rules already in context:                                            │
    │  • "NEVER update git config"                                              │
    │  • "NEVER run destructive git commands"                                   │
    │  • "Always create NEW commits rather than amending"                       │
    │  • "Use HEREDOC for commit messages"                                      │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 2: Agent checks if this is AI Context modification                  │
    │                                                                           │
    │  From ~/.claude/CLAUDE.md:                                                │
    │  "[CRITICAL] 2. AI Context Commit/Push Rule"                              │
    │  • Use "[AI Context]" prefix for context file commits                     │
    │  • Include Co-Authored-By line                                            │
    │                                                                           │
    │  Files being committed: CLAUDE.md, index.jsonld, SKILL.md                 │
    │  → YES, this is AI Context                                                │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 3: Agent MAY read additional rules (if instructed)                  │
    │                                                                           │
    │  From .../0_layer_universal/CLAUDE.md:                                    │
    │  "Git rules: sub_layer_0_04_rules/0_instruction_docs/git_commit_rule.md"  │
    │                                                                           │
    │  Agent could READ: git_commit_rule.md for detailed procedures             │
    │  (But usually system prompt has enough)                                   │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 4: Agent executes commit workflow                                   │
    │                                                                           │
    │  1. git status (check what's changed)                                     │
    │  2. git diff (see changes)                                                │
    │  3. git log (see recent commit style)                                     │
    │  4. git add [specific files]                                              │
    │  5. git commit -m "$(cat <<'EOF'                                          │
    │     [AI Context] description                                              │
    │                                                                           │
    │     Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>               │
    │     EOF                                                                   │
    │     )"                                                                    │
    │  6. git push (if requested)                                               │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

## Context Chain for Git Commit

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    CONTEXT CHAIN: GIT COMMIT                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

    SYSTEM PROMPT (TIER 0)
    ══════════════════════
    │
    │   Contains: Git Safety Protocol
    │   • NEVER update git config
    │   • NEVER run destructive commands
    │   • Always create NEW commits
    │   • Use HEREDOC format
    │   • Include Co-Authored-By
    │
    ▼
    GLOBAL CLAUDE.md (TIER 2)
    ═════════════════════════
    │
    │   ~/.claude/CLAUDE.md
    │   Contains: "[CRITICAL] 2. AI Context Commit/Push Rule"
    │   • Use "[AI Context]" prefix
    │   • git add → git commit → git push
    │   • Never skip git operations
    │
    ▼
    PATH CLAUDE.md (TIER 3)
    ═══════════════════════
    │
    │   .../0_layer_universal/CLAUDE.md
    │   Contains: Reference to detailed git rules
    │   • "Git rules: sub_layer_0_04_rules/.../git_commit_rule.md"
    │
    ▼
    ON-DEMAND (TIER 5) - Optional
    ═════════════════════════════
    │
    │   sub_layer_0_04_rules/0_instruction_docs/git_commit_rule.md
    │   Contains: Full detailed procedure
    │   (Agent reads if needs more detail)
    │
    ▼
    AGENT EXECUTES COMMIT
```

---

## Key Insight: Git Rules Come from Multiple Sources

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  SOURCE                          │  RULES PROVIDED                              │
├──────────────────────────────────┼──────────────────────────────────────────────┤
│  System Prompt (Anthropic)       │  Safety rules, HEREDOC format, Co-Author     │
│  ~/.claude/CLAUDE.md             │  [AI Context] prefix, commit sequence        │
│  .../0_layer_universal/CLAUDE.md │  Reference to detailed rules                 │
│  git_commit_rule.md (optional)   │  Full procedure if needed                    │
└──────────────────────────────────┴──────────────────────────────────────────────┘

Most git commit context comes from TIER 0 and TIER 2 (auto-loaded).
Agent rarely needs to read additional files for git operations.
```

---

*Last updated: 2026-02-05*
