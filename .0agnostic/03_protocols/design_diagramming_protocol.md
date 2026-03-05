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

<!-- section_id: "78bd3eab-dc65-4b58-a82d-9faab118a628" -->
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

<!-- section_id: "7b12db43-777a-412c-95b7-14e21b59b867" -->
## Step 2: Write the Diagram

<!-- section_id: "ea03d4cd-0617-4d8c-ab70-812b792bfb60" -->
### Syntax Rules (Required)

These rules prevent rendering failures across Quarto, VS Code Mermaid extensions, and the claude-mermaid MCP server:

1. **Use `flowchart`** — NOT `graph` (deprecated in many renderers)
2. **Line breaks**: `<br/>` — NOT `\n`
3. **No HTML tags**: No `<i>`, `<b>`, `<code>` inside labels
4. **Quoted labels with colons**: `A["Layer 2: Infrastructure"]` — colons are safe inside double quotes
5. **No parentheses in subgraph labels**: Use `subgraph X["Core Chain"]` not `subgraph X["Core (2-8)"]`
6. **No `style` inside `sequenceDiagram`**: Style directives only work in flowchart/graph types
7. **Color coding**: Use `style NodeID fill:#hexcolor,color:#textcolor` for visual grouping

<!-- section_id: "bad0425d-3937-4b1a-8e9b-79d7cd42200a" -->
### Naming Convention

| Element | Convention | Example |
|---------|-----------|---------|
| Node IDs | Short, uppercase or camelCase | `L2`, `INFRA`, `authCheck` |
| Subgraph IDs | UPPERCASE descriptive | `ALWAYS`, `CORE`, `UNIVERSAL` |
| Labels | Human-readable in quotes | `["Layer 2: Infrastructure<br/>Database, Auth"]` |

<!-- section_id: "f2d26922-2325-4a5e-9092-39fd860058e3" -->
## Step 3: Preview with MCP Server

Use the `mermaid_preview` tool to validate before committing:

```
mermaid_preview:
  diagram: <your mermaid code>
  preview_id: "design-{topic}"
  theme: "default"          # or forest, dark, neutral
```

The diagram opens in browser at `http://localhost:3737/{preview_id}` with live reload. Iterate until correct.

<!-- section_id: "90324347-1de2-4e92-b764-8d630a007b52" -->
## Step 4: Save Output

<!-- section_id: "2304aab7-c839-4257-8bde-1747e1f66122" -->
### For markdown documentation (default)

Place diagram in a markdown file with ` ```mermaid ` code fences:

```
outputs/design_decisions/{topic}/diagrams/{project}_architecture_diagrams.md
```

Or alongside the design document:

```
outputs/by_topic/diagrams/
```

<!-- section_id: "f5d9e579-9a17-463f-8823-b32e3917e7f5" -->
### For static images (presentations, external docs)

Export via `mermaid_save`:

```
mermaid_save:
  save_path: "./outputs/design_decisions/{topic}/diagrams/{name}.svg"
  preview_id: "design-{topic}"
  format: "svg"             # or png, pdf
```

<!-- section_id: "3f21cede-f13c-451c-b8bc-bcd6dd4576c2" -->
## Step 5: Document in Design File

Every diagram file should include:

1. **Title** with descriptive name
2. **Companion reference**: Link to the design document it visualizes
3. **Diagram Index**: Table at bottom listing all diagrams with descriptions
4. **Date**: When the diagrams were created/updated

<!-- section_id: "12274478-2ea8-4c22-b732-4bf4580bd4a6" -->
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

<!-- section_id: "80e3c777-4459-4ab9-a05e-c57ea59ca6aa" -->
## Available Skills

| Skill | When to Use |
|-------|-------------|
| `mermaid-diagrams` | Expert guidance on diagram types, syntax, and best practices (from claude-mermaid plugin) |
| `document-skills:canvas-design` | When you need static visual designs (PNG/PDF) beyond what Mermaid can do |
| `document-skills:frontend-design` | When designing UI components that need visual mockups |

<!-- section_id: "e8df9d13-a87f-42b7-962d-529b32438009" -->
## Troubleshooting

| Problem | Fix |
|---------|-----|
| "No diagram type detected" | Change `graph` to `flowchart` |
| "No diagram type detected" (empty text) | Remove HTML tags from labels |
| Line breaks not rendering | Use `<br/>` not `\n` |
| Quarto + extension conflict | Disable one renderer; check Quarto version |
| Style not applying to subgraph | Verify subgraph ID matches style directive |

<!-- section_id: "ef8e2337-7395-443c-9705-f1fdebe75dfe" -->
## Reference

- Full tool documentation: `.0agnostic/01_knowledge/visualization_tools/docs/mermaid_tools_guide.md`
- Mermaid official docs: https://mermaid.js.org/
- claude-mermaid repo: https://github.com/veelenga/claude-mermaid
