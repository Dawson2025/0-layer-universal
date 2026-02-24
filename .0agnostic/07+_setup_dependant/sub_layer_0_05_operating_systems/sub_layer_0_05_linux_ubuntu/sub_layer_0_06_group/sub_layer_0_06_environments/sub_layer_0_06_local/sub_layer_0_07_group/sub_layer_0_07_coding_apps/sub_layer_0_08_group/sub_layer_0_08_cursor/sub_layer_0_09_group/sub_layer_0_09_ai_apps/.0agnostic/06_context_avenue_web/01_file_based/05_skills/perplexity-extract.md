# Avenue 05 Registration: perplexity-extract skill

**Skill**: `/perplexity-extract`
**Location**: `.claude/skills/perplexity-extract/SKILL.md`
**Scope**: All AI apps at level 09 and below
**Trigger**: User provides a Perplexity search URL for content extraction

## Description

Extracts structured content and citation source URLs from Perplexity search pages
using Claude in Chrome browser automation. Uses React fiber traversal as the only
reliable method for accessing citation URLs (standard DOM queries fail).

## Related Resources

| Resource | Location |
|----------|----------|
| Skill definition | `.claude/skills/perplexity-extract/SKILL.md` |
| Extraction rules | `.0agnostic/02_rules/static/perplexity_extraction_rules.md` |
| Extraction protocol | `.0agnostic/03_protocols/perplexity_extraction_protocol.md` |
| Test extraction | `layer_-1_research/layer_-1_better_ai_system/perplexity_extraction_2026-02-22_tts-research.md` |
