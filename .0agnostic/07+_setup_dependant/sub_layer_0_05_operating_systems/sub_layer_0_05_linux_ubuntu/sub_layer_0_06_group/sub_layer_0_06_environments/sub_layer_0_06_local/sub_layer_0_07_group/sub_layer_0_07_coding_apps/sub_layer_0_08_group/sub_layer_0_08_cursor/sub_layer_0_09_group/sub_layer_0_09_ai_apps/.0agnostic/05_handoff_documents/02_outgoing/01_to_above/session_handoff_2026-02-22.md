---
resource_id: "89edc58b-ecb2-46da-9faa-90224325307e"
resource_type: "handoff"
resource_name: "session_handoff_2026-02-22"
---
# Session Handoff: Perplexity Extraction + 07+ Restructuring

**Date**: 2026-02-22
**From**: AI Apps Category (level 09)
**To**: Cursor (level 08) / Coding Apps (level 07)

<!-- section_id: "74085b57-9ef8-4392-93d5-e409e4efa786" -->
## What Was Done

<!-- section_id: "b5880cbf-75a7-4346-85a3-b1e943cf6e1e" -->
### 1. Perplexity Page Extraction Discovery
- Discovered that standard DOM queries return ~0 external links from Perplexity pages
- Found that React fiber traversal is the ONLY reliable method for citation extraction
- Extraction path: `span.citation.inline-flex` → `__reactFiber$*` → `memoizedProps.children.props.url`
- Tested on TTS research thread: extracted 18 unique citation URLs across 21 citation elements

<!-- section_id: "381ec028-eba6-47dd-bbfb-59f1f638b308" -->
### 2. `/perplexity-extract` Skill Created
- Location: `.claude/skills/perplexity-extract/SKILL.md`
- Registered in `.claude/skills/SKILLS.md`
- Full protocol with known limitations documented

<!-- section_id: "e76978be-a568-4176-84a1-8d05c5b82152" -->
### 3. 07+ Hierarchy Restructured
- Fixed numbering: 07 (Coding Apps) → 08 (Cursor) → 09 (AI Apps) → 10 (individual apps)
- Each level given full entity treatment: .0agnostic/, .1merge/, tool dirs, 12 stages
- `_shared/` content absorbed into `.0agnostic/01_knowledge/` at appropriate levels
- 0AGNOSTIC.md written and agnostic-sync.sh run at all 7 entities

<!-- section_id: "a532e55a-2b4c-4bb8-8297-be8e61742dc4" -->
### 4. Knowledge Populated
- Extraction rules at level 09: `.0agnostic/02_rules/static/perplexity_extraction_rules.md`
- Extraction protocol at level 09: `.0agnostic/03_protocols/perplexity_extraction_protocol.md`
- Test extraction output at: `layer_-1_research/layer_-1_better_ai_system/perplexity_extraction_2026-02-22_tts-research.md`

<!-- section_id: "1db24e06-9ece-4c1b-97a5-e4410fbe8ee2" -->
## Key Findings

1. No existing community tool extracts from Perplexity pages (all make new API calls)
2. React virtualization is the main technical challenge — must scroll to render DOM
3. The `__reactFiber$` key suffix changes per page load — always use `.find()`
4. YouTube and GitHub citations may vanish from DOM when scrolled past

<!-- section_id: "52c88890-0d1d-4bce-a23f-07c56caaa0ef" -->
## Open Items

- Avenue registration (context avenue web) for the extraction skill
- .1merge Claude adapter for tool-specific config
- Validate all entities with validate-entity.sh
