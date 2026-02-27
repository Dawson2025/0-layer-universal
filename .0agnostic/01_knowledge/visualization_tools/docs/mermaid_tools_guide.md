# Mermaid.js Tools Guide

Tools, MCP servers, and skills for creating architecture diagrams with Mermaid.js. Primary use: design stage (04) outputs, but available to any stage that needs visual documentation.

---

## MCP Server: claude-mermaid

**Package**: `claude-mermaid` (npm)
**Repo**: https://github.com/veelenga/claude-mermaid
**Scope**: User-level (available in all Claude Code sessions)

### Installation

```bash
# npm install (manual MCP registration)
npm install -g claude-mermaid
claude mcp add --scope user mermaid claude-mermaid

# OR plugin install (auto-registers MCP + skill)
/plugin marketplace add veelenga/claude-mermaid
/plugin install claude-mermaid@claude-mermaid
```

### Tools Provided

| Tool | Purpose | Parameters |
|------|---------|------------|
| `mermaid_preview` | Render diagram with live reload in browser | `diagram` (code), `preview_id`, `format` (svg/png/pdf), `theme` (default/forest/dark/neutral) |
| `mermaid_save` | Save rendered diagram to file | `save_path`, `preview_id`, `format` |

### Usage Pattern

1. Call `mermaid_preview` with diagram code and a `preview_id`
2. Browser opens at `http://localhost:3737/{preview_id}` with live reload
3. Iterate on the diagram — browser auto-refreshes via WebSocket
4. Call `mermaid_save` to export as SVG, PNG, or PDF
5. Multiple concurrent diagrams supported via different `preview_id` values

### Configuration

Working files stored at: `~/.config/claude-mermaid/live/`
Logs at: `~/.config/claude-mermaid/logs/` (`mcp.log`, `web.log`)
Port range: 3737-3747 (auto-selects available port)

---

## Skill: mermaid-diagrams

**Source**: Built into `claude-mermaid` plugin
**Type**: Claude Code skill with best practices and expert guidance

Provides Mermaid.js expertise including:
- Diagram type selection (flowchart, sequence, class, ER, state, gantt, etc.)
- Syntax best practices for each diagram type
- Theme and styling guidance
- Rendering troubleshooting

### Installation

Installed automatically with the plugin install method. For npm install, the skill may need manual setup.

---

## Mermaid Syntax Quick Reference

### Supported Diagram Types

| Type | Keyword | Best For |
|------|---------|----------|
| Flowchart | `flowchart TB/LR` | Architecture, dependency chains, data flow |
| Sequence | `sequenceDiagram` | API calls, agent communication, relay patterns |
| Class | `classDiagram` | OOP hierarchies, data models |
| ER | `erDiagram` | Database schemas, entity relationships |
| State | `stateDiagram-v2` | Workflow states, stage transitions |
| Gantt | `gantt` | Timelines, project schedules |
| Mindmap | `mindmap` | Feature hierarchies, brainstorming |

### Syntax Rules (Quarto/VS Code Compatibility)

These rules ensure diagrams render in Quarto 1.8+ and common Mermaid VS Code extensions:

1. **Use `flowchart` instead of `graph`** — `flowchart TB` is the modern syntax; `graph TB` is deprecated in some renderers
2. **Line breaks**: Use `<br/>` in node labels (NOT `\n` — that's invalid Mermaid)
3. **No HTML tags**: Avoid `<i>`, `<b>`, `<code>` inside node labels — they break rendering
4. **Colons in labels**: Safe inside double-quoted strings: `A["Layer 2: Infrastructure"]`
5. **Subgraph labels**: Avoid parentheses: use `subgraph CORE["Core Chain"]` not `subgraph CORE["Core (Layers 2-8)"]`
6. **Style directives**: `style NodeID fill:#color,color:#textcolor` — works for nodes and subgraphs
7. **Sequence diagrams**: Do NOT use `style` directives inside `sequenceDiagram` blocks

### Common Patterns for Architecture Diagrams

```
# Dependency chain (top-to-bottom)
flowchart TB
    A["Component A"] --> B["Component B"] --> C["Component C"]
    style A fill:#c53030,color:#fff

# Cross-cutting concerns (dotted lines)
    X["Cross-Cutter"] -.->|"relates to"| A
    X -.->|"relates to"| C

# Context model (subgraphs for grouping)
    subgraph ALWAYS["Always Loaded"]
        D["Own Context"]
        E["Neighbor Interfaces"]
    end
```

---

## Design Stage Integration

When working in **stage 04 (design)**:

1. Place diagram files at: `outputs/design_decisions/{topic}/diagrams/`
2. Name diagrams descriptively: `{project}_architecture_diagrams.md`
3. Include a **Diagram Index** table at the bottom of the file
4. Reference the companion design document: `../feature_design.md`
5. Use `mermaid_preview` to validate diagrams before committing
6. Export SVG/PNG for documentation that needs static images

### Diagram Types for Design Work

| Design Need | Recommended Diagram |
|-------------|-------------------|
| Feature dependency ordering | `flowchart TB` with `style` colors |
| Context cascade/flow | `flowchart LR` with subgraphs |
| Agent communication | `flowchart TB` with bidirectional arrows |
| Request relay chains | `sequenceDiagram` with participants |
| Data model relationships | `erDiagram` or `classDiagram` |
| Directory-to-concept mapping | `flowchart TB` with subgraphs |
| Context universality validation | `flowchart TB` with color-coded groups |

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| "No diagram type detected" | Renderer doesn't recognize `graph` | Use `flowchart` instead |
| "No diagram type detected" (empty text) | HTML tags breaking parser | Remove `<i>`, `<b>`, `<code>` tags |
| Line breaks not working | Using `\n` | Use `<br/>` instead |
| Diagrams not showing at all | No Mermaid extension installed | Install `bierner.markdown-mermaid` or use Quarto |
| Quarto + Mermaid extension conflict | Both trying to render | Disable one; prefer Quarto if it works |
| Style not applying to subgraph | Wrong syntax | `style SubgraphID fill:#color,color:#text` |
