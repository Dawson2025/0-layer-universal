---
resource_id: "d3f7f34f-c21c-4248-af57-9cfab457e201"
resource_type: "document"
resource_name: "perplexity-extract"
---
# Avenue 05 Registration: perplexity-extract skill

**Skill**: `/perplexity-extract`
**Location**: `.claude/skills/perplexity-extract/SKILL.md`
**Scope**: All AI apps at level 09 and below
**Trigger**: User provides a Perplexity search URL for content extraction

<!-- section_id: "7a857a63-5a38-40d1-bcd6-8dc2880b41b0" -->
## Description

Extracts structured content and citation source URLs from Perplexity search pages
using Claude in Chrome browser automation. Uses React fiber traversal as the only
reliable method for accessing citation URLs (standard DOM queries fail).

<!-- section_id: "c46d41ad-310a-4e31-9c71-5bb1149ee5af" -->
## Related Resources

| Resource | Location |
|----------|----------|
| Skill definition | `.claude/skills/perplexity-extract/SKILL.md` |
| Extraction rules | `.0agnostic/02_rules/static/perplexity_extraction_rules.md` |
| Extraction protocol | `.0agnostic/03_protocols/perplexity_extraction_protocol.md` |
| Test extraction | `layer_-1_research/layer_-1_better_ai_system/perplexity_extraction_2026-02-22_tts-research.md` |
