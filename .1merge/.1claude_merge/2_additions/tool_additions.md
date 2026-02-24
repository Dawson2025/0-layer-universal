# Claude Code CLI — Universal Additions

## Browser Extraction Capabilities

Claude Code CLI has browser extraction capabilities via the **Claude in Chrome** MCP server. When you need to extract content from web pages — especially pages that use React rendering (Perplexity, SPAs) — use the following:

### Available Skills

| Skill | Trigger | What It Does |
|-------|---------|--------------|
| `/perplexity-extract` | User provides a Perplexity URL | Extracts structured content + citation source URLs using React fiber traversal |

### When to Use Browser Extraction

- User shares a Perplexity search URL and wants the content/citations preserved
- User needs citation URLs from a Perplexity page (standard copy/paste loses them)
- Content extraction from React-rendered pages where `querySelectorAll('a[href]')` fails
- Any page where URLs are stored in React component props, not DOM attributes
- User asks to open Claude in Chrome and navigate to or work in Perplexity (e.g., "open Perplexity in the browser", "search Perplexity for X")

### Prerequisites

- Claude in Chrome MCP server must be connected (check with `tabs_context_mcp`)
- If MCP server is not available, fall back to `WebFetch` for basic content or ask the user to copy/paste

### Key Knowledge

- React fiber traversal (`__reactFiber$*` → `memoizedProps.children.props`) is the ONLY reliable method for Perplexity citation URLs
- Standard DOM queries return ~0 external links on Perplexity
- Must scroll through all answers before extraction (React virtualization unloads offscreen DOM)
- Detailed knowledge at: `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_claude_in_chrome/.0agnostic/01_knowledge/perplexity_extraction/`
