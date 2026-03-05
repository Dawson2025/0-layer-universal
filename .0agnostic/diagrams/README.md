---
resource_id: "02e9dc7f-9195-4538-a1c1-5c0c42f28fd9"
resource_type: "document"
resource_name: "README"
---
# 0AGNOSTIC Visualization Tools

This directory contains tools and diagrams for visualizing the hierarchical structure of your AI context system (0AGNOSTIC).

<!-- section_id: "8aa92290-d371-4a93-beeb-d0b279c06a2f" -->
## 📊 Generated Diagrams

<!-- section_id: "feabcf43-2337-430b-81e9-0dc72dd860c5" -->
### 1. **01_hierarchy.md** — Visual Overview (Best Starting Point)

Contains three Mermaid diagrams:

- **Layer Hierarchy** — Shows the complete structure from Layer 0 (Universal) → Layer 4 (Courses) and down to Layer 5
- **Resource Inheritance** — Shows how rules, protocols, and strategies cascade from universal to course level
- **Trigger System** — Shows how user events, API events, and triggers activate resource loading
- **Current vs. Ideal Path Organization** — Compares your current deep nesting (155+ chars) with a flattened alternative

**Use this first** to understand the overall architecture visually.

---

<!-- section_id: "a3fd427f-16d2-48be-8493-03cf53db25fa" -->
### 2. **02_metadata_patterns.md** — Best Practices & Transition Guide

Documents four key patterns:

1. **Parent-Child Inheritance** — How relationships are declared in metadata
2. **Trigger-Based Loading** — How triggers wire dependencies together (without filesystem depth)
3. **Shared Skill Parameterization** — How skills are generic and reusable
4. **Cross-Layer References** — How to reference between layers without deep nesting

Plus a recommended **3-phase transition strategy** to flatten your filesystem while preserving all relationships through metadata.

**Use this** to understand how to refactor your system.

---

<!-- section_id: "ccb8fcd6-fe5d-46b3-a60c-67cde406ca60" -->
## 🛠️ Tools

<!-- section_id: "d6f60529-ee99-45b9-9975-f6ba7bce4d65" -->
### Python Generator

```bash
python3 generate_diagrams.py
```

Regenerates the diagrams if you modify your 0AGNOSTIC.md structure.

**Why Python?** Avoids the long-path issues that prevent bash scripts from running when the current working directory path is too long (like yours at 155+ characters).

<!-- section_id: "505871a3-9a43-45ae-992f-c203ec714a2b" -->
### Bash Generator (for reference)

```bash
bash ../agnostic-diagram-generator.sh [output-dir]
```

More comprehensive scanning of all 0AGNOSTIC.md files. Note: May fail if run from a deeply nested directory due to path length limits.

---

<!-- section_id: "05437c12-8722-4196-bd31-a2bee1135a8b" -->
## 🎯 Key Insights from These Diagrams

<!-- section_id: "344a29ce-8687-4884-b0c1-6f5a668a2254" -->
### The Core Problem

Your system has **deep nesting** to represent relationships:

```
0_layer_universal/
└── layer_1/
    └── layer_1_projects/
        └── layer_1_project_school/
            └── layer_2/
                └── layer_2_sub_projects/
                    └── layer_2_sub_project_classes/
                        └── ...
```

**Results**: 155+ character paths → Bash tool failures, terminal truncation, tooling friction

<!-- section_id: "f7c92d5c-eada-4ea6-88bb-0988d363f21a" -->
### The Solution

**Separate concerns**:
- **Filesystem**: Keep flat and navigable (30-40 character paths)
- **Relationships**: Encode in metadata (0AGNOSTIC.md, triggers, pointers)

```
school/
├── 0AGNOSTIC.md (declares relationships)
└── .0agnostic/

classes/
├── 0AGNOSTIC.md (declares: "parent: school, triggers: grade-strategy")
└── .0agnostic/

machine_learning/
├── 0AGNOSTIC.md (declares: "parent: cs, inherits: grade-strategy")
└── .0agnostic/
```

**Result**: All relationships preserved, paths manageable, tools work

---

<!-- section_id: "68d60242-442a-4167-92ec-c86ebcdb8d71" -->
## 📋 How Tools Work With This Pattern

| Tool | Purpose | How It Reads Your System |
|------|---------|------------------------|
| **Mermaid** | Generate diagrams | Parse 0AGNOSTIC.md Identity sections → extract Role, Parent, Children → render graph |
| **Obsidian** | Knowledge graph | Scan .md files with bidirectional links → visualize as interactive graph |
| **Custom Script** | Auto-generate docs | Read trigger tables → generate trigger documentation → create index |
| **IDE Dependency Graph** | Code visualization | Follow imports → visualize code dependencies (same principle as 0AGNOSTIC relationships) |

---

<!-- section_id: "c3601f97-6ba9-470f-9c9c-ed174d901188" -->
## 🚀 Next Steps

<!-- section_id: "b1d8f969-a2d7-4544-88ca-59c261f32da8" -->
### Option 1: Use Visualizations to Understand Current System

1. Open `01_hierarchy.md` in any markdown viewer (GitHub, VS Code, Obsidian)
2. Read the Mermaid diagrams to understand layer relationships
3. Check `02_metadata_patterns.md` for how your triggers and skills work

<!-- section_id: "f545e22f-9e7e-42b0-81a8-7f15f8835cbc" -->
### Option 2: Plan a Refactoring

1. Study `02_metadata_patterns.md` — "Recommended Transition Strategy" section
2. Create a flattened directory structure in a branch
3. Run `generate_diagrams.py` on the new structure to verify relationships
4. Compare old vs. new diagrams

<!-- section_id: "227fce25-ba9d-4bad-9159-2686eedb7814" -->
### Option 3: Extend the Tools

The `generate_diagrams.py` script is **highly extensible**:

```python
def generate_custom_diagram():
    """Add your own diagram types here."""
    # Parse YAML, JSON, or AGNOSTIC structure
    # Generate Mermaid, PlantUML, or other formats
    # Return markdown string
```

Add more diagram types (data flow, dependency matrix, etc.) by extending the script.

---

<!-- section_id: "5fa5194d-a83e-4808-b6ea-a1628f5a2d79" -->
## 📝 File Reference

| File | Purpose | Generated By | Editable? |
|------|---------|--------------|-----------|
| `01_hierarchy.md` | Visual diagrams (Mermaid) | Python script | No (regenerate with script) |
| `02_metadata_patterns.md` | Best practices & transition guide | Python script | No (regenerate with script) |
| `generate_diagrams.py` | Tool to regenerate diagrams | Manual (part of this repo) | **Yes** — extend/customize |
| `agnostic-diagram-generator.sh` | Bash version (reference) | Manual (parent dir) | **Yes** — modify as needed |
| `agnostic_graph.dot` | GraphViz format (for custom rendering) | Bash script | Can be converted to SVG/PNG with `dot` command |
| `MANIFEST.md` | Statistics about your 0AGNOSTIC files | Bash script | No (regenerate) |

---

<!-- section_id: "8635b2c8-9dee-46b1-b008-e346d482f07f" -->
## 🔧 Troubleshooting

<!-- section_id: "ecd32d4c-081c-46b3-b82d-617a0098ed04" -->
### Issue: "Command not found: generate_diagrams.py"

**Solution**: Run with explicit Python:
```bash
python3 /path/to/generate_diagrams.py
```

<!-- section_id: "5b95995e-4e15-4aa2-88c6-238c7fc77833" -->
### Issue: Bash script fails with "ENAMETOOLONG" or "name too long"

**Solution**: This is exactly the problem these diagrams highlight! Either:

1. Run from a shorter directory:
   ```bash
   cd /tmp && bash /absolute/path/to/script.sh
   ```

2. Use the Python version instead (it handles long paths better)

<!-- section_id: "7346cc6c-3709-46bc-8240-ec4d0a96c2c2" -->
### Issue: Mermaid diagrams not rendering in my editor

**Options**:
1. Use VS Code with Markdown Preview (built-in)
2. Use GitHub (renders Mermaid by default)
3. Use Obsidian (community plugin)
4. Copy code blocks to [mermaid.live](https://mermaid.live/)

---

<!-- section_id: "5606c611-a16d-48a9-933d-f1a141d94043" -->
## 📚 Related Resources

- **Metadata pattern guide**: `02_metadata_patterns.md` (this directory)
- **0AGNOSTIC system**: `../0AGNOSTIC.md` (parent)
- **Trigger rules**: `.../02_rules/` (rule definitions)
- **Knowledge base**: `../01_knowledge/` (background docs)

---

Generated: 2026-02-28
Status: Ready for visualization and refactoring planning
