#!/usr/bin/env bash
# resource_id: "1e4111fe-d8df-4388-9678-c35006f5f547"
# resource_type: "script"
# resource_name: "uuid-query"
#
# uuid-query.sh - On-demand UUID lookup across entity, stage, resource,
# file, directory, derived_from, and section identifiers.
#
# Usage:
#   uuid-query.sh <uuid-or-entity-name>
#   uuid-query.sh --type entity|stage|resource|file|dir|section|derived <query>
#   uuid-query.sh --root /path/to/0_layer_universal <query>

set -euo pipefail

TYPE_FILTER=""
ROOT=""
QUERY=""
VALID_TYPES="entity stage resource file dir section derived"
INDEX_MATCHED=false
DEEP_SCAN_REQUIRED=false

usage() {
    echo "Usage: uuid-query.sh [--root PATH] [--type KIND] <uuid-or-entity-name>"
    echo ""
    echo "Kinds: entity, stage, resource, file, dir, section, derived"
}

is_uuid() {
    [[ "$1" =~ ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ ]]
}

while [ $# -gt 0 ]; do
    case "$1" in
        --root)
            if [ $# -lt 2 ]; then
                echo "ERROR: --root requires a path"
                exit 1
            fi
            ROOT="$2"
            shift 2
            ;;
        --type)
            if [ $# -lt 2 ]; then
                echo "ERROR: --type requires a kind"
                exit 1
            fi
            TYPE_FILTER="$2"
            shift 2
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            if [ -n "$QUERY" ]; then
                echo "ERROR: only one query is supported"
                exit 1
            fi
            QUERY="$1"
            shift
            ;;
    esac
done

if [ -z "$QUERY" ]; then
    usage
    exit 1
fi

if [ -n "$TYPE_FILTER" ] && [[ " $VALID_TYPES " != *" $TYPE_FILTER "* ]]; then
    echo "ERROR: unsupported kind: $TYPE_FILTER"
    exit 1
fi

if [ -z "$ROOT" ]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null || true)"
fi

if [ ! -d "$ROOT" ]; then
    echo "ERROR: repo root not found: $ROOT"
    exit 1
fi

UUID_INDEX="$ROOT/.uuid-index.json"
TMP_RESULTS="$(mktemp)"
cleanup() {
    rm -f "$TMP_RESULTS"
}
trap cleanup EXIT

add_result() {
    local kind="$1"
    local id="$2"
    local path="$3"
    local detail="$4"

    if [ -n "$TYPE_FILTER" ] && [ "$TYPE_FILTER" != "$kind" ]; then
        return 0
    fi

    printf '%s\t%s\t%s\t%s\n' "$kind" "$id" "$path" "$detail" >> "$TMP_RESULTS"
}

query_uuid_index() {
    if [ ! -f "$UUID_INDEX" ]; then
        return 1
    fi

    local index_results
    index_results="$(python3 - "$UUID_INDEX" "$QUERY" <<'PY'
import json
import sys

index_path, query = sys.argv[1], sys.argv[2]
with open(index_path, encoding="utf-8") as handle:
    data = json.load(handle)

uuids = data.get("uuids", {})
names = data.get("names", {})

if query in uuids:
    entry = uuids[query]
    detail = f"name={entry.get('name', '')}"
    if entry.get("entity_id"):
        detail += f" entity_id={entry.get('entity_id', '')}"
    print(f"{entry.get('type', 'unknown')}\t{query}\t{entry.get('path', '')}\t{detail}")
elif query in names:
    resolved = names[query]
    entry = uuids.get(resolved, {})
    detail = f"name={query}"
    if entry.get("entity_id"):
        detail += f" entity_id={entry.get('entity_id', '')}"
    print(f"{entry.get('type', 'entity')}\t{resolved}\t{entry.get('path', '')}\t{detail}")
PY
)"

    if [ -z "$index_results" ]; then
        return 1
    fi

    while IFS=$'\t' read -r kind ident path detail; do
        [ -n "$kind" ] || continue
        add_result "$kind" "$ident" "$path" "$detail"
    done <<< "$index_results"

    INDEX_MATCHED=true
    return 0
}

scan_rg_pattern() {
    local kind="$1"
    local pattern="$2"

    if [ -n "$TYPE_FILTER" ] && [ "$TYPE_FILTER" != "$kind" ]; then
        return 0
    fi

    while IFS=: read -r file line match; do
        [ -n "$file" ] || continue
        local rel="${file#$ROOT/}"
        local ident="$QUERY"
        add_result "$kind" "$ident" "$rel:$line" "$match"
    done < <(rg -n --no-heading --hidden -g '!**/.git/**' -S "$pattern" "$ROOT" 2>/dev/null || true)
}

scan_dir_ids() {
    if [ -n "$TYPE_FILTER" ] && [ "$TYPE_FILTER" != "dir" ]; then
        return 0
    fi

    while IFS= read -r dir_id_file; do
        [ -n "$dir_id_file" ] || continue
        local rel_dir
        rel_dir="${dir_id_file#$ROOT/}"
        rel_dir="${rel_dir%/.dir-id}"
        add_result "dir" "$QUERY" "$rel_dir" ".dir-id"
    done < <(rg -l --hidden -g '.dir-id' -g '!**/.git/**' -x "$QUERY" "$ROOT" 2>/dev/null || true)
}

query_uuid_index || true

if is_uuid "$QUERY"; then
    if [ "$INDEX_MATCHED" = false ]; then
        DEEP_SCAN_REQUIRED=true
    elif [ -n "$TYPE_FILTER" ] && [ "$TYPE_FILTER" != "entity" ] && [ "$TYPE_FILTER" != "stage" ]; then
        DEEP_SCAN_REQUIRED=true
    fi
fi

if [ "$DEEP_SCAN_REQUIRED" = true ]; then
    scan_rg_pattern "resource" "resource_id:[[:space:]]*\"?$QUERY\"?"
    scan_rg_pattern "file" "\"file_id\"[[:space:]]*:[[:space:]]*\"$QUERY\""
    scan_rg_pattern "derived" "derived_from:[[:space:]]*\"$QUERY\""
    scan_rg_pattern "section" "section_id:[[:space:]]*\"$QUERY\""
    scan_dir_ids
fi

if [ ! -s "$TMP_RESULTS" ]; then
    echo "No matches found for: $QUERY"
    exit 1
fi

sort -u "$TMP_RESULTS" | while IFS=$'\t' read -r kind ident path detail; do
    echo "kind: $kind"
    echo "id: $ident"
    echo "path: $path"
    if [ -n "$detail" ]; then
        echo "detail: $detail"
    fi
    echo ""
done
