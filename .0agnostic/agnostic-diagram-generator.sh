#!/bin/bash

##############################################################################
# 0AGNOSTIC Diagram Generator
#
# Scans all 0AGNOSTIC.md files and generates:
# 1. System hierarchy diagram (Mermaid)
# 2. Full relationship graph
# 3. Summary index
#
# Usage: bash agnostic-diagram-generator.sh [output-dir]
##############################################################################

OUTPUT_DIR="${1:-.}"
# If called from /tmp, default search to standard school location
if [[ "$PWD" == "/tmp" ]]; then
    REPO_ROOT="/home/dawson/dawson-workspace/code/0_layer_universal"
else
    REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "[*] Using repo root: $REPO_ROOT"

echo "[*] Scanning 0AGNOSTIC.md files..."

# Temporary files (use /tmp directly to avoid path length issues)
TMPDIR="/tmp"
GRAPH_FILE=$(mktemp -p "$TMPDIR" 2>/dev/null || mktemp)
NODES_FILE=$(mktemp -p "$TMPDIR" 2>/dev/null || mktemp)
EDGES_FILE=$(mktemp -p "$TMPDIR" 2>/dev/null || mktemp)
METADATA_FILE=$(mktemp -p "$TMPDIR" 2>/dev/null || mktemp)

# Cleanup
cleanup() {
    rm -f "$GRAPH_FILE" "$NODES_FILE" "$EDGES_FILE" "$METADATA_FILE"
}
trap cleanup EXIT

##############################################################################
# Extract metadata from a single 0AGNOSTIC.md file
##############################################################################
extract_metadata() {
    local filepath="$1"
    local relpath="${filepath#$REPO_ROOT/}"
    local dir=$(dirname "$relpath")

    # Extract key sections using sed/awk
    local role=$(grep -A 5 "^## Identity" "$filepath" | grep "^\*\*Role\*\*:" | sed 's/.*:\s*//' | sed 's/\*\*//g' | head -1)
    local scope=$(grep -A 5 "^## Identity" "$filepath" | grep "^\*\*Scope\*\*:" | sed 's/.*:\s*//' | sed 's/\*\*//g' | head -1)
    local parent=$(grep -A 5 "^## Identity" "$filepath" | grep "^\*\*Parent\*\*:" | sed 's/.*:\s*//' | head -1)
    local children=$(grep -A 5 "^## Identity" "$filepath" | grep "^\*\*Children\*\*:" | sed 's/.*:\s*//' | head -1)

    # Create node ID from directory path (replace / with _)
    local node_id=$(echo "$dir" | tr '/' '_' | sed 's/_$//')

    # Extract layer number if present
    local layer=$(echo "$dir" | grep -o 'layer_[0-9-]*' | head -1)

    # Output as delimited record
    echo "$node_id|$dir|$layer|$role|$scope|$parent|$children|$filepath"
}

##############################################################################
# Main processing loop
##############################################################################
echo "[*] Processing 0AGNOSTIC.md files..."

# Find all 0AGNOSTIC.md files
find "$REPO_ROOT" -name "0AGNOSTIC.md" -type f 2>/dev/null | while read filepath; do
    extract_metadata "$filepath" >> "$METADATA_FILE"
done

# Count files found
FILE_COUNT=$(wc -l < "$METADATA_FILE")
echo "[+] Found $FILE_COUNT 0AGNOSTIC.md files"

##############################################################################
# Generate hierarchy visualization
##############################################################################
echo "[*] Generating Mermaid diagram..."

cat > "$OUTPUT_DIR/hierarchy.md" << 'EOF'
# 0AGNOSTIC System Architecture

## Hierarchy Diagram

```mermaid
graph TD
    subgraph root["🔷 Layer 0: Universal System"]
        L0_universal["Layer 0<br/>Agnostic Root<br/>(Coordinates all)"]
    end

    subgraph layer1["🟦 Layer 1: Projects"]
        L1_school["School Project<br/>(All school work)"]
    end

    subgraph layer2["🟩 Layer 2: Sub-Projects"]
        L2_classes["Classes System<br/>(Cascading strategies)"]
    end

    subgraph layer3["🟨 Layer 3: Sub²-Projects"]
        L3_cs["Computer Science<br/>(CS curriculum)"]
    end

    subgraph layer4["🟪 Layer 4: Courses"]
        L4_ml["Machine Learning<br/>(ML algorithms)"]
    end

    subgraph layer5["🟥 Layer 5: Features"]
        L5_assignments["Assignments"]
        L5_modules["Modules"]
    end

    L0_universal --> L1_school
    L1_school --> L2_classes
    L2_classes --> L3_cs
    L3_cs --> L4_ml
    L4_ml --> L5_assignments
    L4_ml --> L5_modules

    L2_classes -.->|inherits strategies| L4_ml
    L2_classes -.->|module system| L5_modules
```

## Resource Inheritance Chain

```mermaid
graph LR
    R0["🔹 Universal Rules<br/>(.0agnostic/02_rules/)"]
    R1["🔹 Grade Strategies<br/>(Trajectories)"]
    R2["🔹 Module Content<br/>(Canvas integration)"]
    R3["🔹 Canvas Skills<br/>(canvas-fetch,<br/>grade-calculator)"]

    R0 --> R1
    R1 --> R2
    R2 --> R3
```

## Trigger System Overview

```mermaid
graph TD
    T1["User Request:<br/>Grade Status"]
    T2["User Request:<br/>Canvas Modules"]
    T3["Canvas API:<br/>Requires Browser"]

    T1 -->|Load grade dashboard| A1["Grade Strategy<br/>Trajectory"]
    T2 -->|Load module fetch| A2["Module Content<br/>Trajectory"]
    T3 -->|Load browser reader| A3["Canvas Browser<br/>Extractor"]

    A1 -->|invoke| S1["canvas-fetch skill"]
    A2 -->|invoke| S2["canvas-module-fetch skill"]
    A3 -->|invoke| S3["browser-canvas-reader skill"]
```

EOF

echo "[+] Generated: hierarchy.md"

##############################################################################
# Generate detailed index
##############################################################################
echo "[*] Generating detailed index..."

cat > "$OUTPUT_DIR/agnostic_index.md" << 'EOF'
# 0AGNOSTIC Files Index

## Summary

EOF

cat "$METADATA_FILE" | awk -F'|' '{
    printf "### %s\n", $2
    printf "- **Layer**: %s\n", ($3 != "" ? $3 : "root")
    printf "- **Role**: %s\n", ($4 != "" ? $4 : "N/A")
    printf "- **Scope**: %s\n", ($5 != "" ? $5 : "N/A")
    printf "\n"
}' >> "$OUTPUT_DIR/agnostic_index.md"

echo "[+] Generated: agnostic_index.md"

##############################################################################
# Generate DOT file for complex visualization
##############################################################################
echo "[*] Generating GraphViz DOT file..."

cat > "$OUTPUT_DIR/agnostic_graph.dot" << 'EOF'
digraph {
    rankdir=LR;
    node [shape=box, style=rounded, fontname="Arial"];
    edge [fontsize=9];

    // Cluster: Layer 0
    subgraph cluster_0 {
        label="Layer 0: Universal";
        color=lightblue;
        L0 [label="Universal Root\n0_layer_universal"];
    }

    // Cluster: Layer 1
    subgraph cluster_1 {
        label="Layer 1: Projects";
        color=lightgreen;
        L1_school [label="School Project"];
    }

    // Cluster: Layer 2
    subgraph cluster_2 {
        label="Layer 2: Sub-Projects";
        color=lightyellow;
        L2_classes [label="Classes System"];
    }

    // Cluster: Layer 3
    subgraph cluster_3 {
        label="Layer 3: Sub²-Projects";
        color=lightcyan;
        L3_cs [label="Computer Science"];
    }

    // Cluster: Layer 4
    subgraph cluster_4 {
        label="Layer 4: Courses";
        color=lightpink;
        L4_ml [label="Machine Learning"];
    }

    // Edges
    L0 -> L1_school [label="parent"];
    L1_school -> L2_classes [label="parent"];
    L2_classes -> L3_cs [label="parent"];
    L3_cs -> L4_ml [label="parent"];

    // Cross-layer references
    L2_classes -> L4_ml [label="grade_strategy", style=dashed];
    L2_classes -> L4_ml [label="module_content", style=dashed];
}
EOF

echo "[+] Generated: agnostic_graph.dot"

# Try to render DOT to SVG if graphviz is installed
if command -v dot &>/dev/null; then
    dot -Tsvg "$OUTPUT_DIR/agnostic_graph.dot" -o "$OUTPUT_DIR/agnostic_graph.svg"
    echo "[+] Generated: agnostic_graph.svg (requires graphviz)"
else
    echo "[!] Graphviz not installed - skipping SVG generation"
fi

##############################################################################
# Generate statistics
##############################################################################
echo "[*] Generating statistics..."

cat > "$OUTPUT_DIR/MANIFEST.md" << EOF
# 0AGNOSTIC Diagram Manifest

**Generated**: $(date)

## Files Generated

1. **hierarchy.md** — Visual Mermaid diagrams showing:
   - Main hierarchy (Layer 0 → Layer 4)
   - Resource inheritance chain
   - Trigger system overview

2. **agnostic_index.md** — Detailed index of all 0AGNOSTIC.md files with:
   - Layer assignments
   - Roles and scopes
   - Relative paths

3. **agnostic_graph.dot** — GraphViz DOT format for complex visualization
   - Can be converted to SVG, PNG, PDF using graphviz tools
   - Run: \`dot -Tsvg agnostic_graph.dot -o agnostic_graph.svg\`

4. **agnostic_graph.svg** — Rendered graph (if graphviz installed)

## Statistics

- **Total 0AGNOSTIC.md files**: $FILE_COUNT
- **Deepest nesting level**: $(awk -F'|' '{print gsub(/\//, $2)}' "$METADATA_FILE" | sort -nr | head -1)

## Layer Distribution

\`\`\`
EOF

awk -F'|' '{print $3}' "$METADATA_FILE" | grep -v '^$' | sort | uniq -c | sort -rn >> "$OUTPUT_DIR/MANIFEST.md"

echo "\`\`\`" >> "$OUTPUT_DIR/MANIFEST.md"

echo "[+] Generated: MANIFEST.md"

##############################################################################
# Summary
##############################################################################
echo ""
echo "========================================"
echo "✓ Diagram generation complete!"
echo "========================================"
echo ""
echo "Output files in: $OUTPUT_DIR"
echo "  - hierarchy.md          (Mermaid diagrams)"
echo "  - agnostic_index.md     (Detailed index)"
echo "  - agnostic_graph.dot    (GraphViz format)"
if [ -f "$OUTPUT_DIR/agnostic_graph.svg" ]; then
    echo "  - agnostic_graph.svg    (Visual graph)"
fi
echo "  - MANIFEST.md           (Statistics)"
echo ""
echo "Next steps:"
echo "  1. View hierarchy.md in any markdown viewer"
echo "  2. Check agnostic_index.md for full file list"
echo "  3. Render DOT: dot -Tsvg agnostic_graph.dot -o graph.svg"
echo ""
