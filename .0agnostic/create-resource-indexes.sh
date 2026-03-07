#!/usr/bin/env bash
# resource_id: "9f294247-a227-4bf1-8a51-bdee7555115c"
# resource_type: "script"
# resource_name: "create-resource-indexes"
#
# create-resource-indexes.sh — Create resource_index.json for entities
#
# Builds per-entity .0agnostic/resource_index.json files from tracked UUID-bearing files.
# Derived files are excluded. Resource paths are stored relative to the entity root.
#
# Usage:
#   create-resource-indexes.sh                         # Create indexes for all entities with .0agnostic/
#   create-resource-indexes.sh --entity <entity-path> # Create one entity index
#   create-resource-indexes.sh --dry-run              # Show what would change
#   create-resource-indexes.sh --verbose              # Show each entity processed

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET_ENTITY=""
DRY_RUN=false
VERBOSE=false

usage() {
    echo "Usage: create-resource-indexes.sh [--entity <entity-path>] [--dry-run] [--verbose]"
}

while [ $# -gt 0 ]; do
    case "$1" in
        --entity)
            if [ $# -lt 2 ] || [[ "$2" =~ ^- ]]; then
                echo "ERROR: --entity requires an entity path"
                exit 1
            fi
            TARGET_ENTITY="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "Create Resource Indexes — scanning entities in $ROOT"
echo ""

python3 - "$ROOT" "$TARGET_ENTITY" "$DRY_RUN" "$VERBOSE" <<'PY'
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone

root = os.path.abspath(sys.argv[1])
entity_arg = sys.argv[2]
dry_run = sys.argv[3].lower() == "true"
verbose = sys.argv[4].lower() == "true"


def vlog(message: str) -> None:
    if verbose:
        print(f"  [verbose] {message}")


def read_text(path: str, limit: int | None = None) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        return handle.read() if limit is None else handle.read(limit)


def extract_yaml_field(text: str, field: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    frontmatter = parts[1]
    pattern = re.compile(rf"^{re.escape(field)}:\s*['\"]?(.+?)['\"]?\s*$", re.MULTILINE)
    match = pattern.search(frontmatter)
    return match.group(1).strip() if match else ""


def extract_line_field(text: str, field: str) -> str:
    pattern = re.compile(rf"^{re.escape(field)}:\s*['\"]?(.+?)['\"]?\s*$", re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def extract_comment_field(text: str, field: str) -> str:
    for raw_line in text.splitlines():
        line = raw_line.strip()
        for prefix in ("#", "//", "/*", "*", "<!--"):
            if line.startswith(prefix):
                line = line[len(prefix):].strip()
        if line.endswith("*/"):
            line = line[:-2].strip()
        if line.endswith("-->"):
            line = line[:-3].strip()
        if line.startswith(f"{field}:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return ""


def extract_json_field(path: str, field: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return ""
    value = data.get(field, "")
    return value.strip() if isinstance(value, str) else ""


def is_derived_file(path: str, head_text: str) -> bool:
    base = os.path.basename(path)
    if base in {"CLAUDE.md", "AGENTS.md", "GEMINI.md", "OPENAI.md", ".cursorrules", "copilot-instructions.md"}:
        return True
    if base.endswith(".integration.md"):
        return True
    return "derived_from:" in head_text


def infer_resource_type(rel_path: str, head_text: str, ext: str) -> str:
    explicit = extract_yaml_field(head_text, "resource_type") or extract_comment_field(head_text, "resource_type")
    if explicit:
        return explicit

    base = os.path.basename(rel_path)
    if ext in {".sh", ".py"}:
        return "script"
    if ext in {".json", ".jsonld"}:
        return "data"
    if "/outputs/" in rel_path:
        return "output"
    if "/synthesis/" in rel_path:
        return "synthesis"
    if "/01_knowledge/" in rel_path:
        return "knowledge"
    if "/02_rules/" in rel_path:
        return "rule"
    if "/03_protocols/" in rel_path:
        return "protocol"
    if base == "0AGNOSTIC.md":
        return "agnostic"
    if base == "0INDEX.md":
        return "index"
    if base == "README.md":
        return "readme"
    return "document"


def infer_resource_name(path: str, head_text: str) -> str:
    explicit = extract_yaml_field(head_text, "resource_name") or extract_comment_field(head_text, "resource_name")
    if explicit:
        return explicit

    base = os.path.basename(path)
    if base.endswith(".jsonld"):
        return base[:-7]
    if base == ".cursorrules":
        return "cursorrules"
    return os.path.splitext(base)[0]


def generate_uuid() -> str:
    return str(uuid.uuid4())


def entity_output_path(entity_dir: str) -> str:
    return os.path.join(entity_dir, ".0agnostic", "resource_index.json")


def get_output_file_id(output_path: str) -> str:
    existing = extract_json_field(output_path, "file_id")
    return existing if existing else generate_uuid()


def resolve_entity_path(path_value: str) -> str:
    if os.path.isabs(path_value):
        return os.path.abspath(path_value)
    return os.path.abspath(os.path.join(root, path_value))


def validate_entity(entity_dir: str) -> None:
    if not os.path.isdir(entity_dir):
        raise RuntimeError(f"entity directory not found: {entity_dir}")
    if os.path.commonpath([root, entity_dir]) != root:
        raise RuntimeError(f"entity path is outside repo root: {entity_dir}")
    if not os.path.isfile(os.path.join(entity_dir, "0AGNOSTIC.md")):
        raise RuntimeError(f"0AGNOSTIC.md not found in entity: {entity_dir}")
    if not os.path.isdir(os.path.join(entity_dir, ".0agnostic")):
        raise RuntimeError(f".0agnostic directory not found in entity: {entity_dir}")


def discover_entities() -> list[str]:
    if entity_arg:
        entity_dir = resolve_entity_path(entity_arg)
        validate_entity(entity_dir)
        return [entity_dir]

    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        if "0AGNOSTIC.md" not in filenames or ".0agnostic" not in dirnames:
            continue
        if os.path.basename(dirpath).startswith("stage_"):
            continue
        found.append(os.path.abspath(dirpath))
    return sorted(found)


def build_index(entity_dir: str) -> tuple[str, dict, int]:
    entity_agnostic = os.path.join(entity_dir, "0AGNOSTIC.md")
    entity_text = read_text(entity_agnostic, 8192)
    entity_id = extract_yaml_field(entity_text, "entity_id") or extract_line_field(entity_text, "entity_id")
    if not entity_id:
        raise RuntimeError(f"entity_id missing in {entity_agnostic}")

    entity_name = os.path.basename(entity_dir)
    entity_rel = os.path.relpath(entity_dir, root)
    output_path = entity_output_path(entity_dir)
    file_id = get_output_file_id(output_path)

    raw = subprocess.check_output(
        ["git", "-C", root, "ls-files", "-z", "--", entity_rel],
        stderr=subprocess.DEVNULL,
    )

    entries = []
    seen: dict[str, str] = {}

    for item in raw.split(b"\0"):
        if not item:
            continue
        rel_repo_path = item.decode("utf-8", errors="ignore")
        full_path = os.path.join(root, rel_repo_path)
        if not os.path.isfile(full_path):
            continue

        rel_entity_path = os.path.relpath(full_path, entity_dir)
        if rel_entity_path == ".0agnostic/resource_index.json":
            continue

        head = read_text(full_path, 8192)
        if is_derived_file(full_path, head):
            continue

        ext = os.path.splitext(full_path)[1].lower()
        identifier = ""
        id_field = ""
        if ext in {".json", ".jsonld"}:
            identifier = extract_json_field(full_path, "file_id")
            id_field = "file_id" if identifier else ""
        else:
            identifier = extract_yaml_field(head, "resource_id") or extract_comment_field(head, "resource_id")
            id_field = "resource_id" if identifier else ""

        if not identifier:
            continue

        if identifier in seen:
            raise RuntimeError(
                f"duplicate resource UUID {identifier} in {rel_entity_path} and {seen[identifier]}"
            )

        seen[identifier] = rel_entity_path
        entries.append(
            {
                "resource_id": identifier,
                "id_field": id_field,
                "resource_type": infer_resource_type(rel_entity_path, head, ext),
                "resource_name": infer_resource_name(full_path, head),
                "path": rel_entity_path,
            }
        )

    entries.sort(key=lambda entry: entry["path"])

    index_data = {
        "file_id": file_id,
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "entity_id": entity_id,
        "entity_name": entity_name,
        "entity_path": entity_rel,
        "resources": entries,
    }
    return output_path, index_data, len(entries)


entities = discover_entities()
if not entities:
    print("No entities found with .0agnostic/ and 0AGNOSTIC.md")
    sys.exit(0)

written = 0
for entity_dir in entities:
    entity_rel = os.path.relpath(entity_dir, root)
    vlog(f"Processing entity: {entity_rel}")
    try:
        output_path, index_data, count = build_index(entity_dir)
    except RuntimeError as exc:
        msg = str(exc)
        if "entity_id missing" in msg:
            vlog(f"SKIP: {entity_rel} — no entity_id")
            continue
        print(f"  ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"  ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    if dry_run:
        print(f"  WOULD CREATE: {os.path.relpath(output_path, root)} ({count} resources)")
    else:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(index_data, handle, indent=2)
            handle.write("\n")
        print(f"  CREATED: {os.path.relpath(output_path, root)} ({count} resources)")
    written += 1

print("")
print("--- Create Resource Indexes Summary ---")
print(f"Entities processed: {len(entities)}")
if dry_run:
    print(f"Would create indexes: {written}")
else:
    print(f"Indexes created: {written}")
PY
