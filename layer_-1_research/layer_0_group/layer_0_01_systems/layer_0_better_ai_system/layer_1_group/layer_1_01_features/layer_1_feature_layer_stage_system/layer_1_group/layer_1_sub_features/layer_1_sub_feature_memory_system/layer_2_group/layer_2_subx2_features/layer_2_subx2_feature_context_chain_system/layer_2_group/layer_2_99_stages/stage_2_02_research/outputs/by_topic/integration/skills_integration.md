---
resource_id: "045d53af-f837-43cc-8e68-71223ef3875d"
resource_type: "output"
resource_name: "skills_integration"
---
# Skills Integration with AALang

> **VERIFIED 2026-02-07**: The skills controllability problem is real and well-documented across multiple sources. See `verification_results.md` for evidence.

## The Problem

Skills (files and folders in `.claude/skills/`, `.claude/commands/`, etc.) are not being used by AI agents in situations where they should be. The agent either:
- Doesn't recognize when a skill applies
- Doesn't know the skill exists (silently excluded due to char budget)
- Invokes it incorrectly or at the wrong time

**Root cause (verified)**: There is NO algorithmic trigger system. Skill invocation is purely semantic LLM reasoning (non-deterministic). The agent reads skill descriptions from an `<available_skills>` list in its tools array and decides based on its own judgment. Additionally, all skill descriptions must fit within a ~16K character budget — skills that exceed this are **silently dropped**.

---

## Current Skills Architecture

```
.claude/
├── skills/
│   ├── skill_name.md          ← Markdown file defining the skill
│   └── skill_folder/          ← Folder with multiple files
│       ├── instructions.md
│       └── templates/
└── commands/
    └── command_name.md        ← Slash commands
```

Skills are:
- **Markdown-based**: Natural language descriptions of when/how to use them
- **Community-shareable**: Standard format that anyone can create and share
- **Passively discovered**: The agent sees them listed in system context and decides whether to use them
- **Trigger-dependent**: Rely on the agent's judgment to match user intent to skill applicability

---

## Integration Approaches (REVISED after verification)

> **CORRECTION**: Approaches A and the JSON-LD router are abandoned. Research shows JSON-LD is the worst format for LLM instruction following (0.34 accuracy, 3-5x token cost). All approaches now use markdown.

### Approach 1: Better Skill Descriptions (Immediate)

The simplest fix — improve YAML frontmatter descriptions using WHEN/WHEN NOT patterns:

```yaml
---
name: handoff-creation
description: |
  WHEN to use: User says "end session", "hand off", "transition", "save progress",
  or when completing work that spans multiple sessions in the layer-stage system.
  WHEN NOT to use: Simple single-session tasks, quick questions, file edits that
  don't need cross-session tracking.
---
```

Evidence shows specific descriptions with explicit trigger conditions significantly improve auto-invocation rates.

### Approach 2: Increase Character Budget (Immediate)

Set `SLASH_COMMAND_TOOL_CHAR_BUDGET=30000` or higher in `.claude/settings.json` to prevent skills from being silently dropped. Default is ~16K which is too small for a system with many skills.

### Approach 3: Skill Hints in CLAUDE.md (Immediate)

Add explicit skill routing hints to CLAUDE.md:

```markdown
## Skill Usage Guide
- When ending a session or transitioning work: use `/handoff-creation`
- When gathering context about current layer position: use `/context-gathering`
- When committing AI context changes: use `/commit`
```

This is an acknowledged hack, but it works because CLAUDE.md is always in static context.

### Approach 4: Path-Specific Rules (Medium-term)

Use `.claude/rules/*.md` with `paths:` YAML frontmatter to inject skill hints only when working in relevant directories:

```markdown
---
paths:
  - "layer_*/hand_off_documents/**"
---
When working with hand-off documents, use the `/handoff-creation` skill
to ensure proper formatting and cross-session tracking.
```

This targets skill hints to specific contexts without bloating the global CLAUDE.md.

### Approach 5: Skill Routing Skill (Medium-term)

Create a meta-skill that recommends other skills based on current context:

```
.claude/skills/skill-router/SKILL.md
```

When invoked, it:
1. Reads the current working directory and task context
2. Checks which skills are available
3. Recommends which skills apply to the current situation
4. Explains how to invoke each recommended skill

### Approach 6: AALang-to-Markdown Transpiler (Long-term)

Build a tool that takes AALang .gab.jsonld definitions and produces optimized markdown skill instructions:

```
orchestrator.gab.jsonld (formal 5-mode definition)
       │
       │ transpiler
       ▼
.claude/skills/orchestration/SKILL.md (optimized markdown)
├── Same behavioral specification
├── 3-5x fewer tokens
├── WHEN/WHEN NOT trigger conditions
└── Step-by-step mode execution in prose
```

This bridges AALang's design precision with markdown's runtime efficiency.

---

## Verified Technical Details

### How Skills Are Actually Discovered

Skills use a **three-level progressive disclosure** system:

1. **Level 1 — Metadata in system prompt** (always loaded): Claude Code scans skill directories at startup, reads YAML frontmatter from each SKILL.md, constructs an `<available_skills>` list embedded in the Skill tool description. This is what the LLM sees.

2. **Level 2 — Full SKILL.md** (on-demand): When Claude decides a skill is relevant (or user types `/skill-name`), the full SKILL.md body loads into conversation context.

3. **Level 3 — Supporting files** (on-demand): Additional files in the skill directory are read only when Claude explicitly reads them.

### Character Budget Constraint

All skill descriptions combined must fit within **~16K characters** (2% of context window). Skills exceeding this are **silently excluded**. Check with `/context` command. Override with:

```json
// .claude/settings.json
{
  "env": {
    "SLASH_COMMAND_TOOL_CHAR_BUDGET": "30000"
  }
}
```

### Skill Invocation Modes

| Frontmatter | User can invoke | Claude can invoke |
|-------------|----------------|------------------|
| (default) | Yes | Yes |
| `disable-model-invocation: true` | Yes | No |
| `user-invocable: false` | No | Yes |

---

## Open Questions (Revised)

1. ~~Does Claude Code follow JSON-LD references?~~ → **No. Only @import and YAML frontmatter.**

2. **Can path-specific rules effectively route skills?** Need to test whether `.claude/rules/*.md` with `paths:` frontmatter actually triggers skill usage.

3. **What's the optimal skill description length?** Too short = missed triggers. Too long = hits char budget. What's the sweet spot?

4. **Can hooks supplement skill routing?** Hooks can't invoke skills directly (`type: "skill"` doesn't exist), but can they inject context that improves skill selection?

5. **Does listing skills in CLAUDE.md actually improve invocation rates?** Multiple sources say yes, but we need to verify.

---

## Prototype Plan (Revised)

1. Pick 2-3 existing skills that are known to be underused
2. Rewrite their descriptions with WHEN/WHEN NOT patterns
3. Add skill hints to CLAUDE.md for the most critical skills
4. Increase `SLASH_COMMAND_TOOL_CHAR_BUDGET` to 30000
5. Add path-specific rules for layer-stage directories
6. Test across multiple sessions to see if invocation improves
7. Document results and iterate

---

## Sources

- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Inside Claude Code Skills (Mikhail.io)](https://mikhail.io/2025/10/claude-code-skills/)
- [Claude Skills: The Controllability Problem (paddo.dev)](https://paddo.dev/blog/claude-skills-controllability-problem/)
- [Skills Not Triggering (blog.fsck.com)](https://blog.fsck.com/2025/12/17/claude-code-skills-not-triggering/)
- [Claude Code Skills Deep Dive (Lee Han Chung)](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)

---

*Research feature: layer_0_feature_aalang_integration/skills_integration*
*Last updated: 2026-02-07*
