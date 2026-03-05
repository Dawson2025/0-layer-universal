---
resource_id: "15d67213-f863-4d2e-bdbc-a9158e29825e"
resource_type: "rule"
resource_name: "browser_extraction_rule"
---
# Browser Extraction Rule

**Type**: Dynamic (loaded when triggered)
**Importance**: I2 (Standard)
**Scope**: All agents at all levels

<!-- section_id: "6ec179d6-d372-4ea8-ba21-b6d5de30149d" -->
## Rule

When the user provides a Perplexity URL or requests extraction of content/citations from a web page rendered with React, the agent MUST:

1. **Check** if Claude in Chrome MCP server is available (call `tabs_context_mcp`)
2. **If available**: Invoke `/perplexity-extract` skill for Perplexity URLs
3. **If not available**: Fall back to `WebFetch` for basic content, or inform the user that citation URL extraction requires Claude in Chrome

<!-- section_id: "940547e1-d8ed-4a50-90c2-68820ed2c765" -->
## Trigger Conditions

This rule activates when:
- User shares a URL matching `perplexity.ai/search/*` or `perplexity.ai/ask/*`
- User asks to "extract citations" or "get source URLs" from a Perplexity page
- User asks to extract content from a page and mentions that links/citations are important
- User mentions React-rendered content where standard link extraction fails
- User asks to open Claude in Chrome and navigate to or work in Perplexity (e.g., "open Perplexity in the browser", "search Perplexity for X", "use Perplexity to research Y")

<!-- section_id: "7615d4d7-f299-445d-970e-d5e43a48bd4d" -->
## Why This Exists

Perplexity renders citation links via React components, NOT standard HTML anchors. Running `document.querySelectorAll('a[href]')` returns nearly zero external URLs. The `/perplexity-extract` skill uses React fiber traversal to access the component props where URLs are actually stored.

<!-- section_id: "9704aa3e-3c95-4cfe-9df7-02dce9f4187b" -->
## Tool Specificity

This capability requires **Claude Code CLI** with **Claude in Chrome MCP server**. Other AI tools (Gemini CLI, Cursor Agent, Codex CLI) do not have access to this MCP server and cannot perform this extraction.

<!-- section_id: "13794949-0acf-4aed-94e4-666275dbc1df" -->
## Related Resources

| Resource | Location |
|----------|----------|
| Skill definition | `.claude/skills/perplexity-extract/SKILL.md` |
| React fiber method | `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_claude_in_chrome/.0agnostic/01_knowledge/perplexity_extraction/react_fiber_extraction.md` |
| Browser automation rules | `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_claude_in_chrome/.0agnostic/02_rules/static/browser_automation_rules.md` |
