---
resource_id: "1fab2dd5-f44e-4099-857a-1653307ac0ca"
resource_type: "protocol"
resource_name: "design_diagramming_protocol"
---
# Design Diagramming Protocol

**Scope**: All design stages (stage 04) across all entities
**When**: Creating architecture diagrams, dependency visualizations, data flow diagrams, or any visual design documentation
**Tools**: claude-mermaid MCP server, mermaid-diagrams skill

---

## Step 1: Choose Diagram Type

Before writing any Mermaid code, identify what you're visualizing:

| Design Need | Diagram Type | Mermaid Keyword |
|-------------|-------------|-----------------|
| Feature/component dependency ordering | Flowchart (vertical) | `flowchart TB` |
| Data or context flow | Flowchart (horizontal) | `flowchart LR` |
| Agent-to-agent communication | Flowchart with bidirectional arrows | `flowchart TB` with `<-->` |
| Request relay / API sequence | Sequence diagram | `sequenceDiagram` |
| Class hierarchy / OOP model | Class diagram | `classDiagram` |
| Database schema / entity relationships | ER diagram | `erDiagram` |
| State transitions / workflow stages | State diagram | `stateDiagram-v2` |
| Feature decomposition / brainstorming | Mindmap | `mindmap` |
| Context grouping (what's loaded vs. on-demand) | Flowchart with subgraphs | `flowchart TB` with `subgraph` |

## Step 2: Write the Diagram

### Syntax Rules (Required)

These rules prevent rendering failures across Quarto, VS Code Mermaid extensions, and the claude-mermaid MCP server:

1. **Use `flowchart`** — NOT `graph` (deprecated in many renderers)
2. **Line breaks**: `<br/>` — NOT `\n`
3. **No HTML tags**: No `<i>`, `<b>`, `<code>` inside labels
4. **Quoted labels with colons**: `A["Layer 2: Infrastructure"]` — colons are safe inside double quotes
5. **No parentheses in subgraph labels**: Use `subgraph X["Core Chain"]` not `subgraph X["Core (2-8)"]`
6. **No `style` inside `sequenceDiagram`**: Style directives only work in flowchart/graph types
7. **Color coding**: Use `style NodeID fill:#hexcolor,color:#textcolor` for visual grouping

### Naming Convention

| Element | Convention | Example |
|---------|-----------|---------|
| Node IDs | Short, uppercase or camelCase | `L2`, `INFRA`, `authCheck` |
| Subgraph IDs | UPPERCASE descriptive | `ALWAYS`, `CORE`, `UNIVERSAL` |
| Labels | Human-readable in quotes | `["Layer 2: Infrastructure<br/>Database, Auth"]` |

## Step 3: Preview with MCP Server

Use the `mermaid_preview` tool to validate before committing:

```
mermaid_preview:
  diagram: <your mermaid code>
  preview_id: "design-{topic}"
  theme: "default"          # or forest, dark, neutral
```

The diagram opens in browser at `http://localhost:3737/{preview_id}` with live reload. Iterate until correct.

## Step 4: Save Output

### For markdown documentation (default)

Place diagram in a markdown file with ` ```mermaid ` code fences:

```
outputs/design_decisions/{topic}/diagrams/{project}_architecture_diagrams.md
```

Or alongside the design document:

```
outputs/by_topic/diagrams/
```

### For static images (presentations, external docs)

Export via `mermaid_save`:

```
mermaid_save:
  save_path: "./outputs/design_decisions/{topic}/diagrams/{name}.svg"
  preview_id: "design-{topic}"
  format: "svg"             # or png, pdf
```

## Step 5: Document in Design File

Every diagram file should include:

1. **Title** with descriptive name
2. **Companion reference**: Link to the design document it visualizes
3. **Diagram Index**: Table at bottom listing all diagrams with descriptions
4. **Date**: When the diagrams were created/updated

### Template

```markdown
# {Project} Architecture Diagrams

{Description of what these diagrams show.}

**Companion to**: `../design_document.md`
**Date**: YYYY-MM-DD

---

## 1. {Diagram Name}

{Brief description of what this diagram shows.}

` ` `mermaid
flowchart TB
    ...
` ` `

---

## Diagram Index

| # | Diagram | Shows |
|---|---------|-------|
| 1 | {Name} | {What it visualizes} |
```

## Available Skills

| Skill | When to Use |
|-------|-------------|
| `mermaid-diagrams` | Expert guidance on diagram types, syntax, and best practices (from claude-mermaid plugin) |
| `document-skills:canvas-design` | When you need static visual designs (PNG/PDF) beyond what Mermaid can do |
| `document-skills:frontend-design` | When designing UI components that need visual mockups |

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "No diagram type detected" | Change `graph` to `flowchart` |
| "No diagram type detected" (empty text) | Remove HTML tags from labels |
| Line breaks not rendering | Use `<br/>` not `\n` |
| Quarto + extension conflict | Disable one renderer; check Quarto version |
| Style not applying to subgraph | Verify subgraph ID matches style directive |

## Reference

- Full tool documentation: `.0agnostic/01_knowledge/visualization_tools/docs/mermaid_tools_guide.md`
- Mermaid official docs: https://mermaid.js.org/
- claude-mermaid repo: https://github.com/veelenga/claude-mermaid
