---
resource_id: "89edc58b-ecb2-46da-9faa-90224325307e"
resource_type: "handoff"
resource_name: "session_handoff_2026-02-22"
---
# Session Handoff: Perplexity Extraction + 07+ Restructuring

**Date**: 2026-02-22
**From**: AI Apps Category (level 09)
**To**: Cursor (level 08) / Coding Apps (level 07)

## What Was Done

### 1. Perplexity Page Extraction Discovery
- Discovered that standard DOM queries return ~0 external links from Perplexity pages
- Found that React fiber traversal is the ONLY reliable method for citation extraction
- Extraction path: `span.citation.inline-flex` → `__reactFiber$*` → `memoizedProps.children.props.url`
- Tested on TTS research thread: extracted 18 unique citation URLs across 21 citation elements

### 2. `/perplexity-extract` Skill Created
- Location: `.claude/skills/perplexity-extract/SKILL.md`
- Registered in `.claude/skills/SKILLS.md`
- Full protocol with known limitations documented

### 3. 07+ Hierarchy Restructured
- Fixed numbering: 07 (Coding Apps) → 08 (Cursor) → 09 (AI Apps) → 10 (individual apps)
- Each level given full entity treatment: .0agnostic/, .1merge/, tool dirs, 12 stages
- `_shared/` content absorbed into `.0agnostic/01_knowledge/` at appropriate levels
- 0AGNOSTIC.md written and agnostic-sync.sh run at all 7 entities

### 4. Knowledge Populated
- Extraction rules at level 09: `.0agnostic/02_rules/static/perplexity_extraction_rules.md`
- Extraction protocol at level 09: `.0agnostic/03_protocols/perplexity_extraction_protocol.md`
- Test extraction output at: `layer_-1_research/layer_-1_better_ai_system/perplexity_extraction_2026-02-22_tts-research.md`

## Key Findings

1. No existing community tool extracts from Perplexity pages (all make new API calls)
2. React virtualization is the main technical challenge — must scroll to render DOM
3. The `__reactFiber$` key suffix changes per page load — always use `.find()`
4. YouTube and GitHub citations may vanish from DOM when scrolled past

## Open Items

- Avenue registration (context avenue web) for the extraction skill
- .1merge Claude adapter for tool-specific config
- Validate all entities with validate-entity.sh
