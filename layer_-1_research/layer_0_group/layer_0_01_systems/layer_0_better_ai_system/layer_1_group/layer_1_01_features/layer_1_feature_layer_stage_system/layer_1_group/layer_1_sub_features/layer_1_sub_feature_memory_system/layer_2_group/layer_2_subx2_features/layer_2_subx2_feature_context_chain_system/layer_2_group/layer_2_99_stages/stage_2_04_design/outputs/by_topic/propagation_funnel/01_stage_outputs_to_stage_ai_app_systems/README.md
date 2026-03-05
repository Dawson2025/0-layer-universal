---
resource_id: "d9da9b25-24d5-483f-9240-38029c456d39"
resource_type: "readme
output"
resource_name: "README"
---
# Level 01: Stage Outputs → Stage Report

**Purpose**: Aggregate all outputs from a stage and produce comprehensive stage report

**Flow**:
```
Raw Stage Outputs (01_outputs/)
            ↓
    (Analyze & Synthesize)
            ↓
   Stage Report (02_output_reports/)
            ↓
    0AGNOSTIC.md, CLAUDE.md, .1merge rules
            ↓
    AI App–specific Contexts (.claude/, .cursor/, etc.)
```

## Subdirectories

### `01_outputs/`
**Content**: Raw stage outputs collected from stage execution
- Research documents
- Design specifications
- Planning roadmaps
- Implementation notes
- Test results
- Any files produced during stage work

**Naming**: Group by purpose or type
- `by_purpose/` — Organized by functional purpose
- `by_topic/` — Organized by topic domain
- `raw/` — Unprocessed files

### `02_output_reports/`
**Content**: Processed reports analyzing stage outputs
- `stage_NNN_report.md` — Comprehensive stage summary
  - Key deliverables
  - Findings and decisions
  - Connections to other stages
  - Propagation rules

### `03_0agnostic_system/`
**Content**: Context system for this stage
- `0AGNOSTIC.md` — Source of truth (stage identity)
- `.0agnostic/` directory structure
  - `01_knowledge/` — Stage knowledge
  - `02_rules/{static,dynamic}/` — Stage rules
  - `03_protocols/` — Stage protocols
  - etc.

### `1merge_system/`
**Content**: Merge rules for porting to AI apps
- `.1claude_merge/` — Claude Code specific
  - `1_overrides/tool_boilerplate.md`
  - `2_additions/` — Custom additions
- `.1cursor_merge/` — Cursor IDE specific
- `.1codex_merge/` — OpenAI/Codex specific
- `.1gemini_merge/` — Google Gemini specific
- `.1github_merge/` — GitHub Copilot specific

### AI App Directories (`.claude/`, `.cursor/`, `.codex/`, `.gemini/`, `.github/`)
**Content**: Final context for each AI app
- `CLAUDE.md` — Full context for Claude Code
- `.cursor/rules` — Cursor IDE rules
- `CODEX.md` — OpenAI/Codex context
- `GEMINI.md` — Gemini context
- `.github/copilot-instructions.md` — GitHub Copilot
- Supporting skill files, rule files, knowledge files

## Output Files (Created Here)

- `stage_report.md` — Comprehensive summary
- `0AGNOSTIC.md` — Stage context
- `CLAUDE.md` — Claude Code context (auto-generated from 0AGNOSTIC.md)
- `AGENTS.md` — Agent coordination context
- `GEMINI.md` — Gemini context
- `OPENAI.md` — OpenAI context
- `.cursorrules` — Cursor context (lean)
- `.github/copilot-instructions.md` — Copilot context (medium)

## Workflow

1. **Collect** — Place all stage outputs in `01_outputs/`
2. **Analyze** — Review outputs, identify key findings
3. **Synthesize** — Create `02_output_reports/stage_report.md`
4. **Define** — Create `03_0agnostic_system/0AGNOSTIC.md`
5. **Generate** — Run agnostic-sync.sh to create CLAUDE.md, etc.
6. **Merge** — Apply .1merge rules to create app-specific contexts
7. **Deploy** — Place outputs in `.claude/`, `.cursor/`, etc.
8. **Verify** — Check that all AI apps can load context

## Integration

**Input From**: Stage execution (stages 01-11)
**Output To**: Level 02 (stage_reports → layer_reports aggregation)
**Cross-ref**: Links to parent stage, child stages, related entities

---

**Status**: Directory structure created, documentation in progress
**Next**: Populate with actual stage outputs and reports
