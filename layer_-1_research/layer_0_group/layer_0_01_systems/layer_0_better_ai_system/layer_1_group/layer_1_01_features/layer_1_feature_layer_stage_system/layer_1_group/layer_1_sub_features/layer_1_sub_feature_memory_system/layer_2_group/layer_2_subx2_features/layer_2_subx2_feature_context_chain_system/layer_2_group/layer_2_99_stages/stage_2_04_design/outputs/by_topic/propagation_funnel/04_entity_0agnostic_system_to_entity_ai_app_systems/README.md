# Level 04: Entity Context → AI Apps

**Purpose**: Port entity context to each AI app's native configuration system using .1merge three-tier merge

**Flow**:
```
Entity Context
(0AGNOSTIC.md + .0agnostic/)
            ↓
    (agnostic-sync.sh)
            ↓
   Tier 0: Synced Files
(CLAUDE.md, .cursorrules, GEMINI.md, etc.)
            ↓
    (.1merge Tier 1)
            ↓
   Tier 1: App-Specific Boilerplate
(tool_boilerplate.md for each app)
            ↓
    (.1merge Tier 2)
            ↓
   Tier 2: Custom Additions
(app-specific customizations)
            ↓
     (Merge & Deploy)
            ↓
   Final AI App Contexts
(.claude/, .cursor/, .codex/, .gemini/, .github/)
            ↓
    AI Apps Load Context
```

## Subdirectories

### `01_entity_context/`
**Content**: Input context from Level 03
- Entity `0AGNOSTIC.md` — Source of truth
- Entity `.0agnostic/` directory
  - `01_knowledge/`
  - `02_rules/`
  - `03_protocols/`
  - `04_episodic_memory/`
  - `05_handoff_documents/`
  - `06_context_avenue_web/`
  - `07+_setup_dependant/`

### `02_merge_system/`
**Content**: .1merge rules for three-tier merge
- `.1claude_merge/`
  - `1_overrides/tool_boilerplate.md`
  - `2_additions/` (if app-specific enhancements needed)
- `.1cursor_merge/`
  - `1_overrides/tool_boilerplate.md`
  - `2_additions/`
- `.1codex_merge/`
  - `1_overrides/tool_boilerplate.md`
  - `2_additions/`
- `.1gemini_merge/`
  - `1_overrides/tool_boilerplate.md`
  - `2_additions/`
- `.1github_merge/`
  - `1_overrides/tool_boilerplate.md`
  - `2_additions/`

**tool_boilerplate.md Format**:
```yaml
# .1claude_merge/1_overrides/tool_boilerplate.md

# Tier 1: App-Specific Boilerplate

## Claude Code Configuration

STATIC_SOURCE: CLAUDE.md            # Which Tier 0 file?
STATIC_DEST: .claude/CLAUDE.md      # Where to place?

SKILLS_SOURCE: .0agnostic/06_context_avenue_web/05_skills/
SKILLS_DEST: .claude/skills/        # Copy skills directory

RULES_SOURCE: .0agnostic/02_rules/
RULES_DEST: .claude/rules/          # Copy rules directory

AGENTS_SOURCE: AGENTS.md            # Coordination context
AGENTS_DEST: .claude/AGENTS.md

MERGE_PRECEDENCE: Tier2 > Tier1 > Tier0
```

### `03_ai_app_ports/`
**Content**: Processed outputs before final deployment
- `claude_port/` — Claude Code port (pre-deployment)
- `cursor_port/` — Cursor IDE port
- `codex_port/` — OpenAI/Codex port
- `gemini_port/` — Google Gemini port
- `github_port/` — GitHub Copilot port

Each port contains:
- `MERGED_CLAUDE.md` or equivalent (Tier 0+1+2 merged)
- All supporting files (skills, rules, knowledge)
- Validation report

### AI App Directories (`.claude/`, `.cursor/`, `.codex/`, `.gemini/`, `.github/`)
**Content**: Final context ready for AI app loading

**Claude Code (.claude/)**:
- `CLAUDE.md` — Main context file
- `AGENTS.md` — Agent coordination context
- `skills/` — Skill definitions
  - `[skill_name]/SKILL.md`
  - etc.
- `rules/` — Rule definitions
  - `static/`
  - `dynamic/`
- `knowledge/` — Knowledge files

**Cursor IDE (.cursor/)**:
- `.cursor/rules` — Cursor rules file
- Supporting skills and knowledge

**OpenAI/Codex (.codex/)**:
- `CODEX.md` — Main context
- Supporting files

**Google Gemini (.gemini/)**:
- `GEMINI.md` — Main context
- Supporting files

**GitHub Copilot (.github/)**:
- `copilot-instructions.md` — Main instructions
- `instructions/` — Supporting instruction files
- Settings configuration

## Three-Tier Merge Process

### Tier 0: Synced Content
**Source**: Entity `0AGNOSTIC.md` processed by agnostic-sync.sh
**Creates**:
- `CLAUDE.md` (full context)
- `AGENTS.md` (coordination)
- `GEMINI.md` (full context)
- `OPENAI.md` (full context)
- `.cursorrules` (lean context)
- `.github/copilot-instructions.md` (medium context)

**Regenerated whenever**: Entity `0AGNOSTIC.md` updated
**Frequency**: Every session if context changes
**Precedence**: Lowest (can be overridden by Tier 1+2)

### Tier 1: App-Specific Boilerplate
**Source**: `.1merge/[app]/1_overrides/tool_boilerplate.md`
**Defines**:
- Which Tier 0 files to use for this app
- Where to deploy each file (native app location)
- How to structure directories (app-native format)
- Special formatting rules (if any)

**Example** (Claude Code):
```yaml
CLAUDE_DEST: .claude/CLAUDE.md       # Deploy CLAUDE.md here
SKILLS_DEST: .claude/skills/         # Deploy skills directory here
RULES_DEST: .claude/rules/           # Deploy rules directory here
```

**Precedence**: Medium (can override Tier 0, can be overridden by Tier 2)

### Tier 2: Custom Additions
**Source**: `.1merge/[app]/2_additions/[custom_files].md`
**Adds**:
- App-specific rules not in entity context
- Custom enhancements
- Bug fixes or workarounds
- App-specific knowledge

**Example** (Claude Code addition):
```yaml
# .1claude_merge/2_additions/claude_extra_rules.md

# Claude Code–Specific Rules

## Extra Behavior

When user asks "what's my grade?", prefer /calc-dashboard over generic answer

Custom trigger for school assignments:
- Load memory/episodic.md on session start
- Update memory/episodic.md on session end
```

**Precedence**: Highest (can override Tier 0+1)

## Merge Execution Workflow

1. **Generate Tier 0**
   ```bash
   # Run from entity directory
   bash /path/to/agnostic-sync.sh .
   # Produces: CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules
   ```

2. **Read Tier 1** (for each app)
   ```
   Read .1[APP]_merge/1_overrides/tool_boilerplate.md
   Extract mapping rules: SOURCE → DEST
   ```

3. **Read Tier 2** (for each app)
   ```
   Read .1[APP]_merge/2_additions/[files].md
   Collect custom content
   ```

4. **Merge** (for each app)
   ```
   Merge Tier 2 > Tier 1 > Tier 0
   Resolve conflicts (Tier 2 wins)
   Produce final app-specific context
   ```

5. **Deploy** (for each app)
   ```
   Copy final context to native app location
   Claude Code: .claude/
   Cursor: .cursor/
   OpenAI: .codex/
   Gemini: .gemini/
   GitHub: .github/
   ```

6. **Verify**
   ```
   Check each app can load context
   Verify triggers parse correctly
   Test skill invocations
   Confirm knowledge accessible
   ```

## Integration with agnostic-sync.sh

The `agnostic-sync.sh` script handles Tier 0 generation:

```bash
# Pseudo-code (actual implementation varies)

0AGNOSTIC.md (input)
    ↓
Extract STATIC section between markers
    ↓
Generate CLAUDE.md (full context)
Generate AGENTS.md (coordination)
Generate GEMINI.md (full context)
Generate OPENAI.md (full context)
Generate .cursorrules (lean: Identity + Navigation)
Generate .github/copilot-instructions.md (medium: Identity + Triggers + Navigation)
```

After agnostic-sync.sh, apply .1merge tiers for app-specific customization.

## Validation Checklist

Before deploying to AI apps:

- [ ] Entity `0AGNOSTIC.md` exists and is complete
- [ ] Entity `.0agnostic/` directory structure created
- [ ] agnostic-sync.sh runs without errors
- [ ] Tier 0 files generated (CLAUDE.md, .cursorrules, etc.)
- [ ] .1merge boilerplate files exist for all 5 apps
- [ ] Merge process produces valid outputs
- [ ] Final context deploys to correct app locations
- [ ] Each app can load its context file
- [ ] Triggers evaluate correctly
- [ ] Skills are discoverable
- [ ] Knowledge files are accessible
- [ ] Rules are enforced

## Status

**Tier 0**: ✅ agnostic-sync.sh implemented (generates CLAUDE.md, .cursorrules, etc.)
**Tier 1**: 🔄 Designed (boilerplate specifications, needs implementation)
**Tier 2**: 🔄 Designed (custom additions framework, needs examples)
**Merge Orchestration**: 🔄 Designed (needs implementation script)
**Deployment**: 🔄 Designed (needs automation)

---

**Status**: Directory structure created, documentation in progress
**Next**: Implement .1merge boilerplate specifications and merge orchestration script

---

*Reference: Phase 2C-2E in Implementation Roadmap (stage_2_05_planning/outputs/01_implementation_roadmap.md)*
