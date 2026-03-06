#!/bin/bash
# resource_id: "08a4e9bc-8cc1-457e-b966-0a912ae6dff7"
# resource_type: "script"
# resource_name: "pointer-sync"
#
# pointer-sync.sh — Auto-update pointer files when canonical paths change
#
# Finds all markdown files with pointer_to: in YAML frontmatter,
# resolves the canonical location, computes the relative path,
# and updates the pointer file's "Canonical location" line.
#
# Resolution: UUID-first (canonical_entity_id), name fallback (canonical_entity).
#
# Usage:
#   pointer-sync.sh                           # Update all pointers
#   pointer-sync.sh --dry-run                 # Show what would change
#   pointer-sync.sh --validate                # Check all pointers resolve (exit 1 if broken)
#   pointer-sync.sh --verbose                 # Show each resolution step
#   pointer-sync.sh --rebuild-index           # Rebuild .uuid-index.json from all entities
#   pointer-sync.sh --find-references <uuid>  # Find all pointers referencing a UUID
#   pointer-sync.sh --detect-cycles           # Detect circular reference chains
#   pointer-sync.sh --gc                      # Remove orphaned entries from index
#
# Designed to run from any directory within 0_layer_universal.
# Integrates with agnostic-sync.sh (called at end of sync).
#

set -euo pipefail

# --- Dependency check ---
if ! command -v python3 > /dev/null 2>&1; then
    echo "ERROR: python3 is required but was not found."
    exit 1
fi

# --- Configuration ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"  # 0_layer_universal root
UUID_INDEX="$ROOT/.uuid-index.json"
LOCK_DIR="${UUID_INDEX}.lock"
LOCK_HELD=false

DRY_RUN=false
VALIDATE=false
VERBOSE=false
REBUILD_INDEX=false
FIND_REFS=""
DETECT_CYCLES=false
GC_MODE=false
LOOKUP_TARGET=""

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run)        DRY_RUN=true; shift ;;
        --validate)       VALIDATE=true; shift ;;
        --verbose)        VERBOSE=true; shift ;;
        --rebuild-index)  REBUILD_INDEX=true; shift ;;
        --detect-cycles)  DETECT_CYCLES=true; shift ;;
        --gc)             GC_MODE=true; shift ;;
        --lookup)
            if [ $# -lt 2 ] || [[ "$2" =~ ^- ]]; then
                echo "ERROR: --lookup requires a UUID or entity name argument"
                exit 1
            fi
            LOOKUP_TARGET="$2"
            shift 2
            ;;
        --find-references)
            if [ $# -lt 2 ] || [[ "$2" =~ ^- ]]; then
                echo "ERROR: --find-references requires a UUID argument"
                exit 1
            fi
            FIND_REFS="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: pointer-sync.sh [OPTIONS]"
            echo ""
            echo "  --dry-run                   Show what would change without modifying files"
            echo "  --validate                  Check all pointers resolve; exit 1 if any broken"
            echo "  --verbose                   Show each resolution step"
            echo "  --rebuild-index             Rebuild .uuid-index.json from all entities"
            echo "  --lookup <uuid|name>        Lookup UUID entry or resolve entity name to UUID"
            echo "  --find-references <uuid>    Find all pointers referencing a UUID"
            echo "  --detect-cycles             Detect circular reference chains"
            echo "  --gc                        Remove orphaned entries from index"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# --- Counters ---
UPDATED=0
UNCHANGED=0
BROKEN=0
TOTAL=0

# --- Helper: verbose log ---
vlog() {
    if $VERBOSE; then
        echo "  [verbose] $*"
    fi
}

# --- Helper: compute relative path ---
relpath() {
    python3 -c "import os.path; print(os.path.relpath('$2', '$1'))"
}

# --- Helper: extract frontmatter field ---
extract_fm() {
    local field="$1"
    local file="$2"
    sed -n '/^---/,/^---/p' "$file" | tr -d '\r' | grep "^${field}:" | head -1 | sed "s/^${field}:[[:space:]]*//" | sed 's/^["'"'"']//;s/["'"'"']$//' || true
}

# --- Helper: check if file has pointer frontmatter ---
has_pointer_fm() {
    local file="$1"
    local first_line
    first_line=$(head -1 "$file" 2>/dev/null | tr -d '\r')
    if [ "$first_line" != "---" ]; then
        return 1
    fi
    sed -n '2,/^---/p' "$file" 2>/dev/null | tr -d '\r' | grep -q "^pointer_to:" 2>/dev/null
}

# --- Helper: generate UUID ---
generate_uuid() {
    if command -v uuidgen > /dev/null 2>&1; then
        uuidgen | tr '[:upper:]' '[:lower:]'
    elif [ -f /proc/sys/kernel/random/uuid ]; then
        cat /proc/sys/kernel/random/uuid
    else
        python3 -c "import uuid; print(uuid.uuid4())"
    fi
}

# --- Lock helpers ---
acquire_lock() {
    local max_wait=30
    local waited=0
    while ! mkdir "$LOCK_DIR" 2>/dev/null; do
        # Check for stale lock (older than 5 minutes)
        if [ -d "$LOCK_DIR" ]; then
            local lock_age
            lock_age=$(find "$LOCK_DIR" -maxdepth 0 -mmin +5 2>/dev/null | wc -l)
            if [ "$lock_age" -gt 0 ]; then
                vlog "Removing stale lock"
                rm -rf "$LOCK_DIR"
                continue
            fi
        fi
        sleep 1
        waited=$((waited + 1))
        if [ "$waited" -ge "$max_wait" ]; then
            echo "ERROR: Could not acquire index lock after ${max_wait}s"
            exit 1
        fi
    done
    LOCK_HELD=true
}

release_lock() {
    rm -rf "$LOCK_DIR" 2>/dev/null || true
    LOCK_HELD=false
}

cleanup_lock_on_exit() {
    if $LOCK_HELD; then
        release_lock
    fi
}
trap cleanup_lock_on_exit EXIT

# --- Atomic write helper ---
atomic_write() {
    local target="$1"
    local content="$2"
    local tmp="${target}.tmp.$$"
    echo "$content" > "$tmp"
    sync "$tmp" 2>/dev/null || true
    mv "$tmp" "$target"
}

# --- UUID Index: Build ---
build_uuid_index() {
    vlog "Building UUID index from all entities..."

    local uuids_json="{"
    local names_json="{"
    local first_uuid=true
    local first_name=true
    local duplicates=0

    # Track seen UUIDs for duplicate detection
    declare -A seen_uuids

    # Scan all 0AGNOSTIC.md for entity_id
    while IFS= read -r file; do
        local eid
        eid=$(grep "^entity_id:" "$file" 2>/dev/null | head -1 | sed 's/^entity_id:[[:space:]]*//' | sed 's/^["'"'"']//;s/["'"'"']$//' || true)
        if [ -z "$eid" ]; then
            continue
        fi

        local entity_dir
        entity_dir=$(dirname "$file")
        local entity_name
        entity_name=$(basename "$entity_dir")
        local rel_path="${entity_dir#$ROOT/}"

        # Duplicate detection
        if [ -n "${seen_uuids[$eid]+x}" ]; then
            echo "  WARN: Duplicate UUID $eid at $rel_path (already at ${seen_uuids[$eid]})"
            duplicates=$((duplicates + 1))
            continue
        fi
        seen_uuids[$eid]="$rel_path"

        if ! $first_uuid; then uuids_json+=","; fi
        first_uuid=false
        uuids_json+="
    \"$eid\": {\"type\": \"entity\", \"name\": \"$entity_name\", \"path\": \"$rel_path\"}"

        if ! $first_name; then names_json+=","; fi
        first_name=false
        names_json+="
    \"$entity_name\": \"$eid\""

    done < <(find "$ROOT" -name "0AGNOSTIC.md" -path "*/layer_*" -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null | sort)

    # Scan all stage_index.json for stage UUIDs
    while IFS= read -r index_file; do
        if ! python3 -c "import json; json.load(open('$index_file'))" 2>/dev/null; then
            vlog "WARN: Invalid JSON in $index_file — skipping"
            continue
        fi

        local stages_data
        stages_data=$(python3 -c "
import json
with open('$index_file') as f:
    data = json.load(f)
eid = data.get('entity_id', '')
for s in data.get('stages', []):
    sid = s.get('stage_id', '')
    sname = s.get('stage_name', '')
    sdir = s.get('directory', '')
    # Compute stage path relative to ROOT
    import os.path
    registry_dir = os.path.dirname('$index_file')
    stages_dir = os.path.dirname(registry_dir)
    stage_path = os.path.join(stages_dir, sdir)
    rel = os.path.relpath(stage_path, '$ROOT')
    print(f'{sid}|{sname}|{eid}|{rel}')
" 2>/dev/null || true)

        while IFS='|' read -r sid sname eid rel; do
            if [ -z "$sid" ]; then continue; fi

            if [ -n "${seen_uuids[$sid]+x}" ]; then
                echo "  WARN: Duplicate UUID $sid (stage) at $rel"
                duplicates=$((duplicates + 1))
                continue
            fi
            seen_uuids[$sid]="$rel"

            if ! $first_uuid; then uuids_json+=","; fi
            first_uuid=false
            uuids_json+="
    \"$sid\": {\"type\": \"stage\", \"name\": \"$sname\", \"entity_id\": \"$eid\", \"path\": \"$rel\"}"
        done <<< "$stages_data"

    done < <(find "$ROOT" -name "stage_index.json" -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null | sort)

    uuids_json+="
  }"
    names_json+="
  }"

    local timestamp
    timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    local full_json="{
  \"generated\": \"$timestamp\",
  \"uuids\": $uuids_json,
  \"names\": $names_json
}"

    # Compute and add checksum from canonical JSON (without checksum field)
    full_json=$(echo "$full_json" | python3 -c "
import sys, json, hashlib
data = json.load(sys.stdin)
payload = json.dumps(data, sort_keys=True, separators=(',', ':')).encode('utf-8')
data['checksum'] = 'sha256:' + hashlib.sha256(payload).hexdigest()
print(json.dumps(data, indent=2))
" 2>/dev/null || echo "$full_json")

    echo "$full_json"

    if [ "$duplicates" -gt 0 ]; then
        echo "  WARNING: $duplicates duplicate UUIDs detected" >&2
    fi
}

# --- UUID Index: Load ---
load_uuid_index() {
    if [ ! -f "$UUID_INDEX" ]; then
        vlog "No UUID index found — building..."
        do_rebuild_index
    fi

    # Validate parse + checksum
    if ! python3 -c "
import json, hashlib, sys
with open('$UUID_INDEX') as f:
    data = json.load(f)
checksum = data.get('checksum', '')
if not checksum.startswith('sha256:'):
    sys.exit(1)
existing = checksum.split(':', 1)[1]
payload = dict(data)
payload.pop('checksum', None)
computed = hashlib.sha256(
    json.dumps(payload, sort_keys=True, separators=(',', ':')).encode('utf-8')
).hexdigest()
sys.exit(0 if computed == existing else 1)
" 2>/dev/null; then
        vlog "UUID index is invalid or checksum-mismatched — rebuilding..."
        do_rebuild_index
    fi
}

# --- UUID Index: Lookup ---
# Returns the path for a UUID, or empty string
uuid_lookup() {
    local uuid="$1"
    if [ ! -f "$UUID_INDEX" ]; then
        return
    fi
    python3 -c "
import json
with open('$UUID_INDEX') as f:
    data = json.load(f)
entry = data.get('uuids', {}).get('$uuid')
if entry:
    print(entry.get('path', ''))
" 2>/dev/null || true
}

# --- UUID Index: Name lookup ---
name_to_uuid() {
    local name="$1"
    if [ ! -f "$UUID_INDEX" ]; then
        return
    fi
    python3 -c "
import json
with open('$UUID_INDEX') as f:
    data = json.load(f)
print(data.get('names', {}).get('$name', ''))
" 2>/dev/null || true
}

# --- Do rebuild index ---
do_rebuild_index() {
    acquire_lock
    local index_content
    index_content=$(build_uuid_index 2>&1)
    # Separate warnings from JSON
    local json_content
    json_content=$(echo "$index_content" | grep -v "^\s*WARN\|^\s*WARNING\|^\s*\[verbose\]" || true)
    local warnings
    warnings=$(echo "$index_content" | grep "^\s*WARN\|^\s*WARNING" || true)

    if [ -n "$warnings" ]; then
        echo "$warnings"
    fi

    atomic_write "$UUID_INDEX" "$json_content"
    release_lock

    local count
    count=$(python3 -c "
import json
with open('$UUID_INDEX') as f:
    data = json.load(f)
print(len(data.get('uuids', {})))
" 2>/dev/null || echo "?")
    echo "[pointer-sync] REBUILD index entries=$count"
}

# ===== COMMAND: --rebuild-index =====
if $REBUILD_INDEX; then
    echo "Rebuilding UUID index..."
    do_rebuild_index
    exit 0
fi

# ===== COMMAND: --lookup =====
if [ -n "$LOOKUP_TARGET" ]; then
    load_uuid_index
    python3 -c "
import json, sys
target = '$LOOKUP_TARGET'
with open('$UUID_INDEX') as f:
    data = json.load(f)

entry = data.get('uuids', {}).get(target)
if entry:
    print(f'uuid: {target}')
    print(f'type: {entry.get(\"type\", \"\")}')
    print(f'name: {entry.get(\"name\", \"\")}')
    print(f'path: {entry.get(\"path\", \"\")}')
    if entry.get('entity_id'):
        print(f'entity_id: {entry.get(\"entity_id\", \"\")}')
    sys.exit(0)

resolved_uuid = data.get('names', {}).get(target)
if resolved_uuid:
    resolved_entry = data.get('uuids', {}).get(resolved_uuid, {})
    print(f'name: {target}')
    print(f'uuid: {resolved_uuid}')
    print(f'type: {resolved_entry.get(\"type\", \"\")}')
    print(f'path: {resolved_entry.get(\"path\", \"\")}')
    sys.exit(0)

print(f'Not found: {target}')
sys.exit(1)
" 2>/dev/null
    exit $?
fi

# ===== COMMAND: --find-references =====
if [ -n "$FIND_REFS" ]; then
    echo "Finding references to UUID: $FIND_REFS"
    echo ""
    found=0

    while IFS= read -r file; do
        if has_pointer_fm "$file"; then
            local_eid=$(extract_fm "canonical_entity_id" "$file")
            local_sid=$(extract_fm "canonical_stage_id" "$file")
            local_rid=$(extract_fm "canonical_resource_id" "$file")

            if [ "$local_eid" = "$FIND_REFS" ] || [ "$local_sid" = "$FIND_REFS" ] || [ "$local_rid" = "$FIND_REFS" ]; then
                echo "  ${file#$ROOT/}"
                found=$((found + 1))
            fi
        fi
    done < <(grep -rl "^pointer_to:" "$ROOT" --include="*.md" 2>/dev/null || true)

    echo ""
    echo "$found reference(s) found"
    exit 0
fi

# ===== COMMAND: --detect-cycles =====
if $DETECT_CYCLES; then
    echo "Detecting reference cycles..."
    echo ""

    # Build edge list: source_entity -> target_entity
    python3 -c "
import os, re, sys

root = '$ROOT'
edges = []
entity_map = {}  # path -> entity_name

# Find all pointer files and extract edges
for dirpath, dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.md'):
            continue
        fpath = os.path.join(dirpath, f)
        try:
            with open(fpath) as fh:
                content = fh.read()
        except:
            continue

        if not content.startswith('---'):
            continue

        # Find frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        fm = parts[1]

        pointer_to = None
        source_entity = None
        target_entity = None

        for line in fm.strip().split('\n'):
            line = line.strip()
            if line.startswith('pointer_to:'):
                pointer_to = line.split(':', 1)[1].strip().strip('\"').strip(\"'\")
            if line.startswith('canonical_entity_id:'):
                target_entity = line.split(':', 1)[1].strip().strip('\"').strip(\"'\")
            elif line.startswith('canonical_entity:') and not target_entity:
                target_entity = line.split(':', 1)[1].strip().strip('\"').strip(\"'\")

        if not pointer_to or not target_entity:
            continue

        # Determine source entity (walk up from pointer file to find 0AGNOSTIC.md)
        d = dirpath
        source_id = None
        while d != root and d != '/':
            ag = os.path.join(d, '0AGNOSTIC.md')
            if os.path.exists(ag):
                with open(ag) as af:
                    for line in af:
                        if line.startswith('entity_id:'):
                            source_id = line.split(':', 1)[1].strip().strip('\"').strip(\"'\")
                            break
                if source_id:
                    break
            d = os.path.dirname(d)

        if source_id and target_entity:
            edges.append((source_id, target_entity))

# Detect cycles using DFS
graph = {}
for src, tgt in edges:
    graph.setdefault(src, []).append(tgt)

cycles = []
visited = set()
rec_stack = set()
path = []

def dfs(node):
    visited.add(node)
    rec_stack.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor in rec_stack:
            cycle_start = path.index(neighbor)
            cycle = path[cycle_start:] + [neighbor]
            cycles.append(cycle)
        elif neighbor not in visited:
            dfs(neighbor)

    path.pop()
    rec_stack.remove(node)

for node in graph:
    if node not in visited:
        dfs(node)

if cycles:
    print(f'Found {len(cycles)} cycle(s):')
    for c in cycles:
        print('  ' + ' -> '.join(c))
else:
    print('No cycles detected.')
sys.exit(0)
" 2>/dev/null
    exit $?
fi

# ===== COMMAND: --gc =====
if $GC_MODE; then
    echo "Garbage collecting orphaned index entries..."

    if [ ! -f "$UUID_INDEX" ]; then
        echo "No UUID index found. Run --rebuild-index first."
        exit 1
    fi

    acquire_lock
    GC_TMP="${UUID_INDEX}.gc.$$"
    python3 -c "
import json, os, hashlib

index_path = '$UUID_INDEX'
tmp_path = '$GC_TMP'
root = '$ROOT'

with open(index_path) as f:
    data = json.load(f)

orphaned = []
uuids = data.get('uuids', {})
for uid, entry in list(uuids.items()):
    path = entry.get('path', '')
    full_path = os.path.join(root, path)
    if not os.path.exists(full_path):
        orphaned.append((uid, path))
        del uuids[uid]

names = data.get('names', {})
valid_uuids = set(uuids.keys())
for name in list(names.keys()):
    if names[name] not in valid_uuids:
        del names[name]

if orphaned:
    data['uuids'] = uuids
    data['names'] = names
    payload = dict(data)
    payload.pop('checksum', None)
    data['checksum'] = 'sha256:' + hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(',', ':')).encode('utf-8')
    ).hexdigest()
    with open(tmp_path, 'w') as f:
        json.dump(data, f, indent=2)
    for uid, path in orphaned:
        print(f'  REMOVED: {uid} -> {path}')
    print(f'')
    print(f'[pointer-sync] GC removed={len(orphaned)} orphaned_uuids')
else:
    print('No orphaned entries found.')
" 2>/dev/null
    if [ -f "$GC_TMP" ]; then
        mv "$GC_TMP" "$UUID_INDEX"
    fi
    release_lock
    exit 0
fi

# ===== MAIN: Pointer sync =====

# Ensure index exists
load_uuid_index

echo "Pointer Sync — scanning for pointer files in $ROOT"
echo ""

# Find all pointer files
POINTER_FILES=()
while IFS= read -r file; do
    if has_pointer_fm "$file"; then
        POINTER_FILES+=("$file")
    fi
done < <(grep -rl "^pointer_to:" "$ROOT" --include="*.md" 2>/dev/null || true)

if [ ${#POINTER_FILES[@]} -eq 0 ]; then
    echo "No pointer files found (files with pointer_to: in YAML frontmatter)"
    exit 0
fi

echo "Found ${#POINTER_FILES[@]} pointer file(s)"
echo ""

# --- Process each pointer file ---
for POINTER_FILE in "${POINTER_FILES[@]}"; do
    TOTAL=$((TOTAL + 1))
    RELATIVE_POINTER="${POINTER_FILE#$ROOT/}"
    vlog "Processing: $RELATIVE_POINTER"

    # Extract frontmatter fields (UUID-first, then legacy)
    POINTER_TO=$(extract_fm "pointer_to" "$POINTER_FILE")
    CANONICAL_ENTITY_ID=$(extract_fm "canonical_entity_id" "$POINTER_FILE")
    CANONICAL_ENTITY=$(extract_fm "canonical_entity" "$POINTER_FILE")
    CANONICAL_ENTITY_NAME=$(extract_fm "canonical_entity_name" "$POINTER_FILE")
    CANONICAL_STAGE_ID=$(extract_fm "canonical_stage_id" "$POINTER_FILE")
    CANONICAL_STAGE=$(extract_fm "canonical_stage" "$POINTER_FILE")
    CANONICAL_STAGE_NAME=$(extract_fm "canonical_stage_name" "$POINTER_FILE")
    CANONICAL_SUBPATH=$(extract_fm "canonical_subpath" "$POINTER_FILE")
    CANONICAL_RESOURCE_ID=$(extract_fm "canonical_resource_id" "$POINTER_FILE")

    vlog "  pointer_to: $POINTER_TO"
    vlog "  canonical_entity_id: $CANONICAL_ENTITY_ID"
    vlog "  canonical_entity: ${CANONICAL_ENTITY:-$CANONICAL_ENTITY_NAME}"
    vlog "  canonical_stage_id: $CANONICAL_STAGE_ID"
    vlog "  canonical_stage: ${CANONICAL_STAGE:-$CANONICAL_STAGE_NAME}"
    vlog "  canonical_subpath: $CANONICAL_SUBPATH"
    vlog "  canonical_resource_id: $CANONICAL_RESOURCE_ID"

    if [ -z "$POINTER_TO" ]; then
        echo "  SKIP: $RELATIVE_POINTER — missing pointer_to field"
        continue
    fi

    # --- Resolve canonical path ---
    CANONICAL_PATH=""
    ENTITY_DIR=""

    # === ENTITY RESOLUTION ===
    if [ -n "$CANONICAL_ENTITY_ID" ]; then
        # UUID-first entity resolution
        local_path=$(uuid_lookup "$CANONICAL_ENTITY_ID")
        if [ -n "$local_path" ]; then
            ENTITY_DIR="$ROOT/$local_path"
            vlog "  Entity resolved via UUID: $local_path"
        else
            # Index miss — try auto-rebuild
            vlog "  UUID not in index — rebuilding..."
            do_rebuild_index >/dev/null 2>&1
            local_path=$(uuid_lookup "$CANONICAL_ENTITY_ID")
            if [ -n "$local_path" ]; then
                ENTITY_DIR="$ROOT/$local_path"
                vlog "  Entity resolved after rebuild: $local_path"
            else
                echo "  BROKEN: $RELATIVE_POINTER — entity UUID '$CANONICAL_ENTITY_ID' not found"
                BROKEN=$((BROKEN + 1))
                continue
            fi
        fi
    elif [ -n "$CANONICAL_ENTITY" ] || [ -n "$CANONICAL_ENTITY_NAME" ]; then
        # Legacy name-based resolution
        entity_name="${CANONICAL_ENTITY:-$CANONICAL_ENTITY_NAME}"
        ENTITY_DIR=$(find "$ROOT" -type d -name "$entity_name" -path "*/layer_*" 2>/dev/null | head -1)
        if [ -z "$ENTITY_DIR" ]; then
            echo "  BROKEN: $RELATIVE_POINTER — entity '$entity_name' not found"
            BROKEN=$((BROKEN + 1))
            continue
        fi
        vlog "  Entity resolved via name (legacy): ${ENTITY_DIR#$ROOT/}"
    else
        echo "  SKIP: $RELATIVE_POINTER — no canonical_entity_id or canonical_entity"
        continue
    fi

    CANONICAL_PATH="$ENTITY_DIR"

    # === STAGE RESOLUTION ===
    if [ -n "$CANONICAL_STAGE_ID" ]; then
        # UUID-first stage resolution via index
        local_path=$(uuid_lookup "$CANONICAL_STAGE_ID")
        if [ -n "$local_path" ]; then
            CANONICAL_PATH="$ROOT/$local_path"
            vlog "  Stage resolved via UUID: $local_path"
        else
            echo "  BROKEN: $RELATIVE_POINTER — stage UUID '$CANONICAL_STAGE_ID' not found"
            BROKEN=$((BROKEN + 1))
            continue
        fi
    elif [ -n "$CANONICAL_STAGE" ] || [ -n "$CANONICAL_STAGE_NAME" ]; then
        # Legacy name-based stage resolution
        stage_name="${CANONICAL_STAGE:-$CANONICAL_STAGE_NAME}"
        STAGE_DIR=$(find "$ENTITY_DIR" -type d -name "$stage_name" 2>/dev/null | while IFS= read -r d; do echo "${#d} $d"; done | sort -n | head -1 | sed 's/^[0-9]* //')
        if [ -z "$STAGE_DIR" ]; then
            echo "  BROKEN: $RELATIVE_POINTER — stage '$stage_name' not found in entity"
            BROKEN=$((BROKEN + 1))
            continue
        fi
        CANONICAL_PATH="$STAGE_DIR"
        vlog "  Stage resolved via name (legacy): ${STAGE_DIR#$ROOT/}"
    fi

    # === SUBPATH RESOLUTION ===
    if [ -n "$CANONICAL_SUBPATH" ]; then
        CANONICAL_PATH="$CANONICAL_PATH/$CANONICAL_SUBPATH"
        if [ ! -e "$CANONICAL_PATH" ]; then
            echo "  BROKEN: $RELATIVE_POINTER — subpath '$CANONICAL_SUBPATH' does not exist"
            BROKEN=$((BROKEN + 1))
            continue
        fi
        vlog "  Full path: ${CANONICAL_PATH#$ROOT/}"
    fi

    # --- Compute relative path ---
    POINTER_DIR=$(dirname "$POINTER_FILE")
    REL_PATH=$(relpath "$POINTER_DIR" "$CANONICAL_PATH")
    vlog "  Relative path: $REL_PATH"

    # --- Update the pointer file ---
    if grep -q '> \*\*Canonical location\*\*:' "$POINTER_FILE"; then
        CURRENT_LINE=$(grep '> \*\*Canonical location\*\*:' "$POINTER_FILE")
        NEW_LINE="> **Canonical location**: \`$REL_PATH\`"

        if [ "$CURRENT_LINE" = "$NEW_LINE" ]; then
            if ! $VALIDATE; then
                echo "  OK: $RELATIVE_POINTER (unchanged)"
            fi
            UNCHANGED=$((UNCHANGED + 1))
        else
            if $DRY_RUN; then
                echo "  WOULD UPDATE: $RELATIVE_POINTER"
                echo "    Old: $CURRENT_LINE"
                echo "    New: $NEW_LINE"
                UPDATED=$((UPDATED + 1))
            elif $VALIDATE; then
                echo "  STALE: $RELATIVE_POINTER"
                echo "    Current: $CURRENT_LINE"
                echo "    Should be: $NEW_LINE"
                BROKEN=$((BROKEN + 1))
            else
                LINE_NUM=$(grep -n '> \*\*Canonical location\*\*:' "$POINTER_FILE" | head -1 | cut -d: -f1)
                if [ -n "$LINE_NUM" ]; then
                    awk -v line="$LINE_NUM" -v newtext="$NEW_LINE" 'NR==line{print newtext;next}{print}' "$POINTER_FILE" > "${POINTER_FILE}.tmp"
                    mv "${POINTER_FILE}.tmp" "$POINTER_FILE"
                fi
                echo "  UPDATED: $RELATIVE_POINTER"
                echo "    -> $REL_PATH"
                UPDATED=$((UPDATED + 1))
            fi
        fi
    else
        echo "  WARN: $RELATIVE_POINTER — no 'Canonical location' line found to update"
        UNCHANGED=$((UNCHANGED + 1))
    fi
done

# --- Summary ---
echo ""
echo "--- Pointer Sync Summary ---"
echo "Total pointer files: $TOTAL"
if $DRY_RUN; then
    echo "Would update: $UPDATED"
elif $VALIDATE; then
    echo "Valid: $UNCHANGED"
    echo "Broken/stale: $BROKEN"
else
    echo "Updated: $UPDATED"
    echo "Unchanged: $UNCHANGED"
fi
echo "Broken: $BROKEN"

if [ "$BROKEN" -gt 0 ]; then
    exit 1
fi
exit 0
