---
resource_id: "4b487a9b-8e95-422c-9cf8-9192370a1adc"
resource_type: "output"
resource_name: "test_design_04_consolidation_funnel"
---
# Test Design: 04 Consolidation Funnel (Bottom-Up)

**Validates**: `stage_2_04_design/outputs/by_topic/04_context_propagation_funnel.md`
**Type**: Structural (bash) + Integration (bash)
**Script name**: `test_consolidation_funnel.sh`

---

## What We're Testing

Bottom-up consolidation: outputs → output_report → .0agnostic → stage_report → 0AGNOSTIC.md. This pattern should be consistent across all active stages. Cross-level flow: stage reports → entity from_below, entity reports → parent from_below. App-specific fan-out: 0AGNOSTIC.md → agnostic-sync → .1merge → generated tool files → AI app config systems (.claude/, .cursor/, .codex/, .gemini/, .github/).

---

## Test Cases

### TC-04-01: Active stages have outputs

**Steps**:
1. Find all stages marked "active" (have `outputs/` with content beyond .gitkeep)
2. For each, check `outputs/` contains at least one work product file

**Expected**: Every active stage has content in outputs/
**Type**: Structural

### TC-04-02: Active stages have stage reports

**Steps**:
1. For each active stage (has outputs with content)
2. Check `outputs/stage_report.md` exists
3. Verify it contains required sections: Status, Summary, Key Outputs, Findings, Open Items, Handoff
4. Verify it is under 30 lines (protocol requirement)

**Expected**: Every active stage has a stage_report.md with all required sections, <30 lines
**Type**: Structural

### TC-04-03: Stage report references outputs

**Steps**:
1. For each stage_report.md
2. Check it mentions at least one file from `outputs/` or `outputs/by_topic/`
3. Verify Key Outputs section has at least one entry

**Expected**: Stage reports reference their stage's outputs (not empty summaries)
**Type**: Structural

### TC-04-04: Entity has incoming stage reports (from_below)

**Steps**:
1. For context_chain_system entity, check `.0agnostic/05_handoff_documents/01_incoming/03_from_below/stage_reports/`
2. Verify it contains stage report copies for active stages
3. Cross-check: each file in from_below matches an actual stage_report.md

**Expected**: Entity's from_below/stage_reports/ mirrors active stage reports
**Note**: This requires sync-handoffs.sh to have been run
**Type**: Integration

### TC-04-05: Entity has consolidation reports (outgoing)

**Steps**:
1. Check `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/`
2. Verify `stages_report.md` exists (consolidation of all stage reports)
3. Verify it references all active stages
4. If entity has children: verify `child_layers_report.md` exists

**Expected**: Entity produces consolidation reports for its parent
**Type**: Structural

### TC-04-06: 0AGNOSTIC.md reflects current stage status

**Steps**:
1. Read entity 0AGNOSTIC.md Current Status section
2. Compare against stage_report.md statuses
3. Flag if 0AGNOSTIC.md status is stale (mentions fewer active stages than exist)

**Expected**: 0AGNOSTIC.md status is consistent with stage reports
**Type**: Structural (heuristic — fuzzy match on stage count)

### TC-04-07: Recursive pattern — child entity reports flow to parent

**Steps**:
1. For memory_system (parent of context_chain_system):
   - Check `from_below/layer_reports/` for context_chain_system layer_report
2. For context_chain_system:
   - Check `from_below/stage_reports/` for active stage reports

**Expected**: Reports flow upward at both stage→entity and entity→parent levels
**Type**: Integration

### TC-04-08: sync-handoffs.sh distributes correctly

**Steps**:
1. Run sync-handoffs.sh for context_chain_system
2. Verify stage reports appear in entity from_below/
3. Verify sibling stages get from_sides/ copies
4. Verify parent entity gets layer_report

**Expected**: sync-handoffs.sh populates all three directions (up, lateral, down)
**Type**: Integration

---

## App-Specific Propagation Test Cases

### TC-04-09: Generated tool files land in correct app config directories

**Steps**:
1. Run agnostic-sync.sh for entity
2. Verify each generated file exists at the expected location:
   - CLAUDE.md at entity root (consumed by `.claude/`)
   - AGENTS.md at entity root (consumed by `.codex/` / OpenAI tools)
   - GEMINI.md at entity root (consumed by `.gemini/`)
   - OPENAI.md at entity root
   - .cursorrules at entity root (consumed by `.cursor/`)
   - .github/copilot-instructions.md (consumed by GitHub Copilot)
3. Verify each file has content (non-empty)

**Expected**: All 6 generated files exist and have content
**Type**: Integration

### TC-04-10: Content profile correctness — Full vs Medium vs Lean

**Steps**:
1. Read generated CLAUDE.md — verify it contains ALL STATIC sections from 0AGNOSTIC.md (Full profile)
2. Read generated .cursorrules — verify it contains ONLY Identity + Navigation (Lean profile)
3. Read generated .github/copilot-instructions.md — verify it contains Identity + Triggers + Navigation (Medium profile)
4. Verify CLAUDE.md line count > copilot-instructions.md line count > .cursorrules line count

**Expected**: Full > Medium > Lean content volume, and each contains only its designated sections
**Type**: Structural

### TC-04-11: .1merge scoping — additions don't cross app boundaries

**Steps**:
1. Find entities where `.1merge/.1claude_merge/2_additions/` has content
2. Read the Claude additions content
3. Verify the additions text appears in CLAUDE.md
4. Verify the additions text does NOT appear in AGENTS.md
5. Verify the additions text does NOT appear in GEMINI.md
6. Verify the additions text does NOT appear in .cursorrules
7. Verify the additions text does NOT appear in copilot-instructions.md

**Expected**: Claude-specific additions stay in CLAUDE.md only — no cross-app leakage
**Type**: Integration

### TC-04-12: App config directories exist for active tools

**Steps**:
1. For each entity in the hierarchy:
   - Check `.claude/` exists (Claude Code config)
   - Check `.cursor/` exists (Cursor config)
   - Check `.github/` exists (GitHub Copilot config)
2. For root entity:
   - Check AGENTS.md exists (Codex consumption)
   - Check GEMINI.md exists (Gemini consumption)

**Expected**: Config directories present for all tools that have generated files
**Type**: Structural

### TC-04-13: App config surfaces populated from agnostic sources

**Steps**:
1. **Claude Code** (`.claude/`):
   - `rules/` has .md files (warm context derived from .0agnostic/02_rules/)
   - `skills/` has subdirs with SKILL.md (cold context from .0agnostic/)
   - `settings.json` exists (hooks, MCP servers)
   - `agents/` exists (agent definitions)
2. **Cursor IDE + Agent CLI** (`.cursor/`):
   - `rules/` has .md files (same rules system as IDE, usable by CLI)
   - `mcp.json` exists (MCP server config)
   - `.cursorrules` exists at entity root
3. **Codex CLI** (`.codex/` or root):
   - AGENTS.md exists at entity root
   - Check for `.codex/config.toml` if project-level overrides exist
4. **Gemini CLI** (`.gemini/` or root):
   - GEMINI.md exists at entity root
5. **GitHub Copilot** (`.github/`):
   - `copilot-instructions.md` has content

**Expected**: Each app's native config surfaces are populated with content derived from .0agnostic/
**Type**: Structural

### TC-04-16: Cursor CLI cross-consumption — reads CLAUDE.md and AGENTS.md as rules

**Steps**:
1. Verify CLAUDE.md exists at entity root (primary: Claude Code, secondary: Cursor CLI)
2. Verify AGENTS.md exists at entity root (primary: Codex CLI, secondary: Cursor CLI)
3. Verify CLAUDE.md content is valid rules content (no tool-specific instructions that would confuse Cursor)
4. Verify AGENTS.md content is valid rules content (no tool-specific instructions that would confuse Cursor)
5. Check that the Claude-specific `.1merge/.1claude_merge/2_additions/` content added to CLAUDE.md is Claude-specific (e.g., "Use Read tool") — this is acceptable since Cursor treats it as supplementary

**Expected**: CLAUDE.md and AGENTS.md are consumable by Cursor CLI as rules without breaking behavior
**Note**: Cursor CLI applies these as rules alongside .cursorrules and .cursor/rules/ — the Full-profile content serves double duty
**Type**: Structural (heuristic)

### TC-04-17: Each app's cascade/walk mechanism has matching generated files

**Steps**:
1. **Claude Code**: Verify CLAUDE.md files exist at multiple levels in the hierarchy (cascade walk)
2. **Codex CLI**: Verify AGENTS.md exists at project root (walk from ~/.codex/ → root → cwd)
3. **Gemini CLI**: Verify GEMINI.md exists at entity root (hierarchical: global → parent dirs → cwd → subdirs)
4. **Cursor**: Verify .cursorrules at root + .cursor/rules/ at relevant levels
5. For each app, check that the files are positioned where the app's native walker will find them

**Expected**: Generated files are placed where each app's cascade mechanism discovers them
**Type**: Structural

### TC-04-14: Complete pipeline — .0agnostic → 0AGNOSTIC → tool file → app config

**Steps**:
1. Check .0agnostic/01_knowledge/ has content (source tier)
2. Check 0AGNOSTIC.md references .0agnostic/ content (consolidation tier)
3. Run agnostic-sync.sh → verify CLAUDE.md generated (tool file tier)
4. Verify .claude/ directory has rules/ and skills/ populated (app config tier)
5. For Cursor: verify .cursorrules generated AND .cursor/ has config
6. For Copilot: verify .github/copilot-instructions.md generated

**Expected**: All 4 tiers of the complete pipeline are connected and populated
**Type**: Integration

### TC-04-15: .1merge directory structure per app

**Steps**:
1. List all subdirectories in `.1merge/`
2. For each tool merge dir found:
   - Verify 3-tier structure: `0_synced/`, `1_overrides/`, `2_additions/`
   - Record which apps have merge dirs
3. Check that at minimum `.1claude_merge/` exists (primary app)
4. Flag any app that has a generated tool file but no merge directory

**Expected**: Every app with a generated tool file has a corresponding .1merge directory with 3-tier structure
**Note**: Some merge dirs may be scaffolded (empty tiers) for apps not yet actively customized
**Type**: Structural

---

## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| Stage-internal funnel | TC-04-01, TC-04-02, TC-04-03 | New |
| Cross-level flow | TC-04-04, TC-04-07 | New |
| Consolidation reports | TC-04-05 | New |
| 0AGNOSTIC.md as entry point | TC-04-06 | New |
| sync-handoffs.sh | TC-04-08 | New |
| Recursive pattern | TC-04-07 | New |
| App-specific generated files | TC-04-09 | New |
| Content profile (Full/Medium/Lean) | TC-04-10 | New |
| .1merge scoping (no cross-app leak) | TC-04-11 | New |
| App config directories | TC-04-12 | New |
| App config surfaces populated | TC-04-13 | New |
| Complete 4-tier pipeline | TC-04-14 | New |
| .1merge per-app structure | TC-04-15 | New |
| Cursor CLI cross-consumption | TC-04-16 | New |
| Cascade/walk file placement | TC-04-17 | New |
| Codex cascade (AGENTS.override.md) | TC-04-13 partial | Covered in app surfaces |
| Gemini hierarchy (global→parent→cwd→sub) | TC-04-17 partial | Walk mechanism check |
| Windsurf / Cline / Aider configs | Not yet testable | Future apps not yet integrated |
