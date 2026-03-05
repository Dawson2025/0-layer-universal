---
resource_id: "15d67213-f863-4d2e-bdbc-a9158e29825e"
resource_type: "rule"
resource_name: "browser_extraction_rule"
---
# Browser Extraction Rule

**Type**: Dynamic (loaded when triggered)
**Importance**: I2 (Standard)
**Scope**: All agents at all levels

## Rule

When the user provides a Perplexity URL or requests extraction of content/citations from a web page rendered with React, the agent MUST:

1. **Check** if Claude in Chrome MCP server is available (call `tabs_context_mcp`)
2. **If available**: Invoke `/perplexity-extract` skill for Perplexity URLs
3. **If not available**: Fall back to `WebFetch` for basic content, or inform the user that citation URL extraction requires Claude in Chrome

## Trigger Conditions

This rule activates when:
- User shares a URL matching `perplexity.ai/search/*` or `perplexity.ai/ask/*`
- User asks to "extract citations" or "get source URLs" from a Perplexity page
- User asks to extract content from a page and mentions that links/citations are important
- User mentions React-rendered content where standard link extraction fails
- User asks to open Claude in Chrome and navigate to or work in Perplexity (e.g., "open Perplexity in the browser", "search Perplexity for X", "use Perplexity to research Y")

## Why This Exists

Perplexity renders citation links via React components, NOT standard HTML anchors. Running `document.querySelectorAll('a[href]')` returns nearly zero external URLs. The `/perplexity-extract` skill uses React fiber traversal to access the component props where URLs are actually stored.

## Tool Specificity

This capability requires **Claude Code CLI** with **Claude in Chrome MCP server**. Other AI tools (Gemini CLI, Cursor Agent, Codex CLI) do not have access to this MCP server and cannot perform this extraction.

## Related Resources

| Resource | Location |
|----------|----------|
| Skill definition | `.claude/skills/perplexity-extract/SKILL.md` |
| React fiber method | `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_claude_in_chrome/.0agnostic/01_knowledge/perplexity_extraction/react_fiber_extraction.md` |
| Browser automation rules | `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_claude_in_chrome/.0agnostic/02_rules/static/browser_automation_rules.md` |
