#!/bin/bash
#
# find-helper.sh - Helper for /find skill traversal
#
# Usage:
#   ./find-helper.sh list <directory>     - List 0INDEX.md children
#   ./find-helper.sh search <query>       - Find all 0INDEX.md files matching query
#   ./find-helper.sh path <directory>     - Show traversal path from root
#
# This script assists LLM agents with the /find skill by providing
# structured data about 0INDEX.md files in the hierarchy.
#

set -e

ROOT_DIR="${ROOT_DIR:-$(cd "$(dirname "$0")/../../.." && pwd)}"

# List children from a 0INDEX.md
list_children() {
    local dir="$1"
    local index_file="$dir/0INDEX.md"

    if [ ! -f "$index_file" ]; then
        echo "No 0INDEX.md found in $dir"
        ls -1 "$dir" 2>/dev/null || echo "Directory not found"
        return 1
    fi

    echo "Children from: $index_file"
    echo "---"
    # Extract the children table (simplified - looks for | Name | patterns)
    grep -E "^\| [a-zA-Z0-9_.-]+ \|" "$index_file" | grep -v "^\| Name \|" || echo "No children table found"
}

# Search for 0INDEX.md files containing query
search_indices() {
    local query="$1"

    echo "Searching for '$query' in 0INDEX.md files..."
    echo "---"
    find "$ROOT_DIR" -name "0INDEX.md" -exec grep -l -i "$query" {} \; 2>/dev/null | while read -r file; do
        echo "Found in: $file"
        grep -i "$query" "$file" | head -3
        echo ""
    done
}

# Show traversal path from root to directory
show_path() {
    local target="$1"
    local current="$ROOT_DIR"

    echo "Traversal path from root to: $target"
    echo "---"

    # Normalize paths
    target=$(cd "$target" 2>/dev/null && pwd)

    # Show each level with its 0INDEX.md status
    local relative="${target#$ROOT_DIR}"
    IFS='/' read -ra parts <<< "$relative"

    local path="$ROOT_DIR"
    echo "1. $path"
    [ -f "$path/0INDEX.md" ] && echo "   Has 0INDEX.md ✓"

    for part in "${parts[@]}"; do
        if [ -n "$part" ]; then
            path="$path/$part"
            echo "2. $path"
            [ -f "$path/0INDEX.md" ] && echo "   Has 0INDEX.md ✓"
        fi
    done
}

# Find all 0INDEX.md files
list_all_indices() {
    echo "All 0INDEX.md files in hierarchy:"
    echo "---"
    find "$ROOT_DIR" -name "0INDEX.md" 2>/dev/null | sort
}

# Main
case "$1" in
    list)
        if [ -z "$2" ]; then
            echo "Usage: $0 list <directory>"
            exit 1
        fi
        list_children "$2"
        ;;
    search)
        if [ -z "$2" ]; then
            echo "Usage: $0 search <query>"
            exit 1
        fi
        search_indices "$2"
        ;;
    path)
        if [ -z "$2" ]; then
            echo "Usage: $0 path <directory>"
            exit 1
        fi
        show_path "$2"
        ;;
    all)
        list_all_indices
        ;;
    *)
        echo "Usage: $0 {list|search|path|all}"
        echo ""
        echo "Commands:"
        echo "  list <directory>  - List children from 0INDEX.md"
        echo "  search <query>    - Search all indices for query"
        echo "  path <directory>  - Show traversal path from root"
        echo "  all               - List all 0INDEX.md files"
        exit 1
        ;;
esac

