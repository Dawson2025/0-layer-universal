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
# Resolution: resource UUID first, then entity/stage UUIDs, then legacy name fallback.
#
# Usage:
#   pointer-sync.sh                           # Update all pointers
#   pointer-sync.sh --dry-run                 # Show what would change
#   pointer-sync.sh --validate                # Check all pointers resolve (exit 1 if broken)
#   pointer-sync.sh --verbose                 # Show each resolution step
#   pointer-sync.sh --rebuild-index           # Rebuild .uuid-index.json from all entities
#   pointer-sync.sh --lookup <uuid|name>      # Lookup UUID or entity name -> path, parent, children
#   pointer-sync.sh --find-references <uuid>  # Find all pointers referencing a UUID
#   pointer-sync.sh --children <uuid>         # List direct children of an entity
#   pointer-sync.sh --parent <uuid>           # Show parent (add --verbose for full chain to root)
#   pointer-sync.sh --query type=entity name=*memory*  # Query/filter index entries
#   pointer-sync.sh --detect-cycles           # Detect circular reference chains
#   pointer-sync.sh --gc                      # Remove orphaned entries from index
#   pointer-sync.sh --rebuild-dir-index       # Rebuild .dir-uuid-index.json from .dir-id files
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
REBUILD_DIR_INDEX=false
LOOKUP_TARGET=""
CHILDREN_TARGET=""
PARENT_TARGET=""
QUERY_ARGS=""

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run)        DRY_RUN=true; shift ;;
        --validate)       VALIDATE=true; shift ;;
        --verbose)        VERBOSE=true; shift ;;
        --rebuild-index)  REBUILD_INDEX=true; shift ;;
        --detect-cycles)  DETECT_CYCLES=true; shift ;;
        --gc)             GC_MODE=true; shift ;;
        --rebuild-dir-index) REBUILD_DIR_INDEX=true; shift ;;
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
        --children)
            if [ $# -lt 2 ] || [[ "$2" =~ ^- ]]; then
                echo "ERROR: --children requires a UUID argument"
                exit 1
            fi
            CHILDREN_TARGET="$2"
            shift 2
            ;;
        --parent)
            if [ $# -lt 2 ] || [[ "$2" =~ ^- ]]; then
                echo "ERROR: --parent requires a UUID argument"
                exit 1
            fi
            PARENT_TARGET="$2"
            shift 2
            ;;
        --query)
            shift
            QUERY_ARGS=""
            while [ $# -gt 0 ] && [[ ! "$1" =~ ^-- ]]; do
                QUERY_ARGS+="$1 "
                shift
            done
            QUERY_ARGS=$(echo "$QUERY_ARGS" | sed 's/ $//')
            if [ -z "$QUERY_ARGS" ]; then
                echo "ERROR: --query requires filter arguments (e.g., type=entity name=*memory*)"
                exit 1
            fi
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
            echo "  --children <uuid>           List direct children of an entity"
            echo "  --parent <uuid>             Show parent of an entity (walk up chain with --verbose)"
            echo "  --query <filters>           Query index (type=entity|stage|resource name=*pat* resource_type=rule)"
            echo "  --detect-cycles             Detect circular reference chains"
            echo "  --gc                        Remove orphaned entries from index"
            echo "  --rebuild-dir-index         Rebuild .dir-uuid-index.json from all .dir-id files"
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
    vlog "Building UUID index from all entities (with parent/children graph)..."

    python3 - "$ROOT" "$VERBOSE" <<'PYINDEX'
import json
import hashlib
import os
import re
import sys
from datetime import datetime, timezone

root = os.path.abspath(sys.argv[1])
verbose = sys.argv[2].lower() == "true"

def vlog(msg):
    if verbose:
        print(f"  [verbose] {msg}", file=sys.stderr)

def read_head(path, limit=8192):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read(limit)

def extract_field(text, field):
    """Extract field: value from text (handles entity_id:, etc.)."""
    pattern = re.compile(rf'^{re.escape(field)}:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)
    m = pattern.search(text)
    return m.group(1).strip() if m else ""

def extract_parent_ref(text):
    """Extract relative path from **Parent**: `../../../0AGNOSTIC.md` lines."""
    m = re.search(r'\*\*Parent\*\*:\s*`([^`]+)`', text)
    return m.group(1).strip() if m else ""

# ---- Phase 1: Scan all entities ----
uuids = {}
names = {}
seen = {}
duplicates = 0
entity_parent_map = {}  # entity_id -> parent_entity_id
entity_path_to_id = {}  # abs_path_of_entity_dir -> entity_id

vlog("Phase 1: Scanning entities...")
agnostic_files = []
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
    if "0AGNOSTIC.md" in files and "/layer_" in dirpath:
        agnostic_files.append(os.path.join(dirpath, "0AGNOSTIC.md"))
agnostic_files.sort()

for filepath in agnostic_files:
    text = read_head(filepath)
    eid = extract_field(text, "entity_id")
    if not eid:
        continue

    entity_dir = os.path.dirname(filepath)
    entity_name = os.path.basename(entity_dir)
    rel_path = os.path.relpath(entity_dir, root)

    if eid in seen:
        print(f"  WARN: Duplicate UUID {eid} at {rel_path} (already at {seen[eid]})", file=sys.stderr)
        duplicates += 1
        continue
    seen[eid] = rel_path

    # Resolve parent reference
    parent_ref = extract_parent_ref(text)
    parent_id = ""
    if parent_ref:
        parent_agnostic = os.path.normpath(os.path.join(entity_dir, parent_ref))
        if os.path.isfile(parent_agnostic):
            parent_text = read_head(parent_agnostic)
            parent_id = extract_field(parent_text, "entity_id")

    uuids[eid] = {"type": "entity", "name": entity_name, "path": rel_path}
    if parent_id:
        uuids[eid]["parent_id"] = parent_id
        entity_parent_map[eid] = parent_id

    names[entity_name] = eid
    entity_path_to_id[entity_dir] = eid

# Compute children for each entity
children_map = {}  # entity_id -> [child_entity_ids]
for child_id, parent_id in entity_parent_map.items():
    children_map.setdefault(parent_id, []).append(child_id)

# Add children[] to entity entries
for eid, child_ids in children_map.items():
    if eid in uuids:
        uuids[eid]["children"] = sorted(child_ids)

vlog(f"  Entities: {sum(1 for v in uuids.values() if v['type'] == 'entity')}")
vlog(f"  Parent links: {len(entity_parent_map)}")
vlog(f"  Entities with children: {len(children_map)}")

# ---- Phase 2: Scan stage indexes ----
vlog("Phase 2: Scanning stage indexes...")
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
    if "stage_index.json" not in files:
        continue
    index_path = os.path.join(dirpath, "stage_index.json")
    try:
        with open(index_path) as f:
            data = json.load(f)
    except Exception:
        vlog(f"WARN: Invalid JSON in {index_path}")
        continue

    stage_eid = data.get("entity_id", "")
    registry_dir = os.path.dirname(index_path)
    stages_dir = os.path.dirname(registry_dir)

    for s in data.get("stages", []):
        sid = s.get("stage_id", "")
        sname = s.get("stage_name", "")
        sdir = s.get("directory", "")
        if not sid or not sdir:
            continue

        stage_path = os.path.join(stages_dir, sdir)
        rel = os.path.relpath(stage_path, root)

        if sid in seen:
            print(f"  WARN: Duplicate UUID {sid} (stage) at {rel}", file=sys.stderr)
            duplicates += 1
            continue
        seen[sid] = rel

        entry = {"type": "stage", "name": sname, "entity_id": stage_eid, "path": rel}
        uuids[sid] = entry

vlog(f"  Stages: {sum(1 for v in uuids.values() if v['type'] == 'stage')}")

# ---- Phase 3: Scan resource indexes ----
vlog("Phase 3: Scanning resource indexes...")
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
    if "resource_index.json" not in files:
        continue
    index_path = os.path.join(dirpath, "resource_index.json")
    try:
        with open(index_path) as f:
            data = json.load(f)
    except Exception:
        vlog(f"WARN: Invalid JSON in {index_path}")
        continue

    entity_dir = os.path.dirname(os.path.dirname(index_path))
    entity_path = data.get("entity_path") or os.path.relpath(entity_dir, root)
    res_eid = data.get("entity_id", "")

    for resource in data.get("resources", []):
        rid = resource.get("resource_id", "")
        rname = resource.get("resource_name", "")
        rtype = resource.get("resource_type", "")
        id_field = resource.get("id_field", "")
        rpath = resource.get("path", "")
        if not rid or not rpath:
            continue

        rel = os.path.normpath(os.path.join(entity_path, rpath))

        if rid in seen:
            print(f"  WARN: Duplicate UUID {rid} (resource) at {rel}", file=sys.stderr)
            duplicates += 1
            continue
        seen[rid] = rel

        entry = {"type": "resource", "name": rname, "entity_id": res_eid,
                 "resource_type": rtype, "id_field": id_field, "path": rel}
        uuids[rid] = entry

vlog(f"  Resources: {sum(1 for v in uuids.values() if v['type'] == 'resource')}")

# ---- Build output ----
index_data = {
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "uuids": uuids,
    "names": names,
}

# Add checksum
payload = json.dumps(index_data, sort_keys=True, separators=(",", ":")).encode("utf-8")
index_data["checksum"] = "sha256:" + hashlib.sha256(payload).hexdigest()

print(json.dumps(index_data, indent=2))

if duplicates > 0:
    print(f"  WARNING: {duplicates} duplicate UUIDs detected", file=sys.stderr)
PYINDEX
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
    # Python script sends JSON to stdout, warnings to stderr
    local json_content
    json_content=$(build_uuid_index)

    atomic_write "$UUID_INDEX" "$json_content"

    # Generate flat .entity-lookup.tsv for fast entity lookup (no Python needed)
    local tsv_content
    tsv_content=$(python3 -c "
import json
with open('$UUID_INDEX') as f:
    data = json.load(f)
lines = ['name\tuuid\tpath\tparent_uuid']
for uid, entry in sorted(data.get('uuids', {}).items(), key=lambda x: x[1].get('name', '')):
    if entry.get('type') != 'entity':
        continue
    lines.append('\t'.join([
        entry.get('name', ''),
        uid,
        entry.get('path', ''),
        entry.get('parent_id', '')
    ]))
print('\n'.join(lines))
" 2>/dev/null)
    atomic_write "$ROOT/.entity-lookup.tsv" "$tsv_content"

    release_lock

    local count
    count=$(python3 -c "
import json
with open('$UUID_INDEX') as f:
    data = json.load(f)
print(len(data.get('uuids', {})))
" 2>/dev/null || echo "?")
    local entity_count
    entity_count=$(( $(wc -l < "$ROOT/.entity-lookup.tsv") - 1 ))
    echo "[pointer-sync] REBUILD index entries=$count entities=$entity_count (tsv)"
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

def show_entry(uid, entry):
    print(f'uuid: {uid}')
    print(f'type: {entry.get(\"type\", \"\")}')
    print(f'name: {entry.get(\"name\", \"\")}')
    print(f'path: {entry.get(\"path\", \"\")}')
    if entry.get('entity_id'):
        print(f'entity_id: {entry[\"entity_id\"]}')
    if entry.get('parent_id'):
        parent = data.get('uuids', {}).get(entry['parent_id'], {})
        print(f'parent_id: {entry[\"parent_id\"]}  ({parent.get(\"name\", \"?\")})')
    if entry.get('children'):
        print(f'children: {len(entry[\"children\"])}')
        for cid in entry['children']:
            child = data.get('uuids', {}).get(cid, {})
            print(f'  {cid}  {child.get(\"name\", \"?\")}')
    if entry.get('resource_type'):
        print(f'resource_type: {entry[\"resource_type\"]}')
    if entry.get('id_field'):
        print(f'id_field: {entry[\"id_field\"]}')

entry = data.get('uuids', {}).get(target)
if entry:
    show_entry(target, entry)
    sys.exit(0)

resolved_uuid = data.get('names', {}).get(target)
if resolved_uuid:
    resolved_entry = data.get('uuids', {}).get(resolved_uuid, {})
    show_entry(resolved_uuid, resolved_entry)
    sys.exit(0)

print(f'Not found: {target}')
sys.exit(1)
" 2>/dev/null
    exit $?
fi

# ===== COMMAND: --children =====
if [ -n "$CHILDREN_TARGET" ]; then
    load_uuid_index
    python3 -c "
import json, sys
target = '$CHILDREN_TARGET'
with open('$UUID_INDEX') as f:
    data = json.load(f)

entry = data.get('uuids', {}).get(target)
if not entry:
    print(f'Not found: {target}')
    sys.exit(1)

if entry.get('type') != 'entity':
    print(f'Not an entity (type={entry.get(\"type\")}). --children only works on entities.')
    sys.exit(1)

children = entry.get('children', [])
if not children:
    print(f'{entry[\"name\"]}: no children')
    sys.exit(0)

print(f'{entry[\"name\"]}: {len(children)} children')
print()
for cid in children:
    child = data.get('uuids', {}).get(cid, {})
    print(f'  {child.get(\"name\", \"?\")}')
    print(f'    uuid: {cid}')
    print(f'    path: {child.get(\"path\", \"?\")}')
" 2>/dev/null
    exit $?
fi

# ===== COMMAND: --parent =====
if [ -n "$PARENT_TARGET" ]; then
    load_uuid_index
    python3 - "$UUID_INDEX" "$PARENT_TARGET" "$VERBOSE" <<'PYPARENT'
import json, sys

index_path = sys.argv[1]
target = sys.argv[2]
verbose = sys.argv[3].lower() == "true"

with open(index_path) as f:
    data = json.load(f)

entry = data.get("uuids", {}).get(target)
if not entry:
    print(f"Not found: {target}")
    sys.exit(1)

if entry.get("type") != "entity":
    print(f"Not an entity (type={entry.get('type')}). --parent only works on entities.")
    sys.exit(1)

parent_id = entry.get("parent_id")
if not parent_id:
    print(f"{entry['name']}: root entity (no parent)")
    sys.exit(0)

parent = data.get("uuids", {}).get(parent_id, {})
print(f"parent of {entry['name']}:")
print(f"  name: {parent.get('name', '?')}")
print(f"  uuid: {parent_id}")
print(f"  path: {parent.get('path', '?')}")

# In verbose mode, walk the full chain to root
if verbose:
    print()
    print("Full parent chain:")
    current_id = target
    depth = 0
    visited = set()
    while current_id:
        if current_id in visited:
            print(f"{'  ' * depth}CYCLE DETECTED at {current_id}")
            break
        visited.add(current_id)
        e = data.get("uuids", {}).get(current_id, {})
        indent = "  " * depth
        print(f"{indent}{e.get('name', '?')}  ({current_id})")
        current_id = e.get("parent_id")
        depth += 1
PYPARENT
    exit $?
fi

# ===== COMMAND: --query =====
if [ -n "$QUERY_ARGS" ]; then
    load_uuid_index
    python3 - "$UUID_INDEX" "$QUERY_ARGS" <<'PYQUERY'
import json, sys, re, fnmatch

index_path = sys.argv[1]
query_str = sys.argv[2]

with open(index_path) as f:
    data = json.load(f)

# Parse key=value filters
filters = {}
for part in query_str.split():
    if "=" in part:
        key, val = part.split("=", 1)
        filters[key] = val

results = []
for uid, entry in data.get("uuids", {}).items():
    match = True
    for key, val in filters.items():
        if key == "type":
            if entry.get("type") != val:
                match = False
        elif key == "name":
            if not fnmatch.fnmatch(entry.get("name", ""), val):
                match = False
        elif key == "resource_type":
            if entry.get("resource_type") != val:
                match = False
        elif key == "entity_id":
            if entry.get("entity_id") != val:
                match = False
        elif key == "parent_id":
            if entry.get("parent_id") != val:
                match = False
        elif key == "has_children":
            has = bool(entry.get("children"))
            if val.lower() in ("true", "1", "yes"):
                if not has:
                    match = False
            else:
                if has:
                    match = False
        elif key == "path":
            if not fnmatch.fnmatch(entry.get("path", ""), val):
                match = False
        else:
            match = False
    if match:
        results.append((uid, entry))

results.sort(key=lambda x: x[1].get("path", ""))

print(f"{len(results)} result(s)")
print()
for uid, entry in results:
    etype = entry.get("type", "?")
    name = entry.get("name", "?")
    path = entry.get("path", "?")
    extras = []
    if entry.get("parent_id"):
        parent = data.get("uuids", {}).get(entry["parent_id"], {})
        extras.append(f"parent={parent.get('name', '?')}")
    if entry.get("children"):
        extras.append(f"children={len(entry['children'])}")
    if entry.get("resource_type"):
        extras.append(f"rtype={entry['resource_type']}")
    extra_str = f"  [{', '.join(extras)}]" if extras else ""
    print(f"  {name}  ({etype}){extra_str}")
    print(f"    {uid}")
    print(f"    {path}")
PYQUERY
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

# ===== COMMAND: --rebuild-dir-index =====
if $REBUILD_DIR_INDEX; then
    DIR_UUID_INDEX="$ROOT/.dir-uuid-index.json"
    DIR_TMP="${DIR_UUID_INDEX}.tmp.$$"
    echo "Rebuilding directory UUID index from .dir-id files..."

    python3 -c "
import json, os, datetime

root = '$ROOT'
index_path = '$DIR_TMP'
count = 0
directories = {}

for dirpath, dirnames, filenames in os.walk(root):
    if '.git' in dirpath.split(os.sep):
        continue
    dirid_path = os.path.join(dirpath, '.dir-id')
    if os.path.isfile(dirid_path):
        try:
            with open(dirid_path) as f:
                uuid = f.read().strip()
            if uuid and len(uuid) == 36:
                rel_path = os.path.relpath(dirpath, root)
                name = os.path.basename(dirpath)
                directories[uuid] = {'path': rel_path, 'name': name}
                count += 1
        except Exception:
            pass

data = {
    'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'count': count,
    'directories': directories
}

with open(index_path, 'w') as f:
    json.dump(data, f, separators=(',', ':'))
    f.flush()
    os.fsync(f.fileno())

print(f'[pointer-sync] dir-index built: {count} directories indexed')
" 2>&1

    if [ -f "$DIR_TMP" ]; then
        mv "$DIR_TMP" "$DIR_UUID_INDEX"
    fi
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

    # === RESOURCE RESOLUTION ===
    if [ -n "$CANONICAL_RESOURCE_ID" ]; then
        local_path=$(uuid_lookup "$CANONICAL_RESOURCE_ID")
        if [ -n "$local_path" ]; then
            CANONICAL_PATH="$ROOT/$local_path"
            vlog "  Resource resolved via UUID: $local_path"
        else
            vlog "  Resource UUID not in index — rebuilding..."
            do_rebuild_index >/dev/null 2>&1
            local_path=$(uuid_lookup "$CANONICAL_RESOURCE_ID")
            if [ -n "$local_path" ]; then
                CANONICAL_PATH="$ROOT/$local_path"
                vlog "  Resource resolved after rebuild: $local_path"
            else
                echo "  BROKEN: $RELATIVE_POINTER — resource UUID '$CANONICAL_RESOURCE_ID' not found"
                BROKEN=$((BROKEN + 1))
                continue
            fi
        fi
    fi

    if [ -z "$CANONICAL_PATH" ]; then
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
            echo "  SKIP: $RELATIVE_POINTER — no canonical_resource_id, canonical_entity_id, or canonical_entity"
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
    else
        vlog "  Using canonical_resource_id; skipping entity/stage fallback"
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
