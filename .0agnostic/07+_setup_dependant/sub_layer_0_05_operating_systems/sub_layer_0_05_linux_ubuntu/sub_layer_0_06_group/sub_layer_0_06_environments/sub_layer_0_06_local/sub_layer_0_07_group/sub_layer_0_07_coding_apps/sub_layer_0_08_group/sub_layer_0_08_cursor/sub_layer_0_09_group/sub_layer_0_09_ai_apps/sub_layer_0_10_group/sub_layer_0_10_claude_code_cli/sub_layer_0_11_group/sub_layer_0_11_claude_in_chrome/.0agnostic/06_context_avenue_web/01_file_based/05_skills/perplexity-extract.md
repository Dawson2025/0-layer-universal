---
resource_id: "710ce3f6-746f-468f-a892-94996a352446"
resource_type: "document"
resource_name: "perplexity-extract"
---
# Avenue 05 Registration: perplexity-extract skill (Claude in Chrome)

**Skill**: `/perplexity-extract`
**Location**: `.claude/skills/perplexity-extract/SKILL.md`
**Scope**: Claude in Chrome feature — Perplexity page content extraction
**Trigger**: User provides a Perplexity search URL for content extraction

## Description

This skill is Claude in Chrome-specific because it depends on:
- `javascript_tool` for React fiber traversal in the page context
- `navigate` for loading Perplexity URLs
- `computer` (scroll) for forcing React virtualization to render all answers
- `get_page_text` for capturing answer text

No other MCP server or API can perform page-level extraction from Perplexity.

## Key Knowledge

| Resource | Location |
|----------|----------|
| React fiber extraction method | `.0agnostic/01_knowledge/perplexity_extraction/react_fiber_extraction.md` |
| Browser automation rules | `.0agnostic/02_rules/static/browser_automation_rules.md` |
| Content extraction workflow | `.0agnostic/03_protocols/content_extraction_workflow.md` |
| Skill definition | `.claude/skills/perplexity-extract/SKILL.md` |
