#!/usr/bin/env bash
# resource_id: "51d595a0-6424-4c57-ad95-aa61e07cc3ef"
# resource_type: "script"
# resource_name: "create-resource-index"
#
# create-resource-index.sh - Build a per-entity resource index from tracked files.
#
# Usage:
#   create-resource-index.sh --entity <entity-path> [--root <repo-root>] [--output <path>] [--verbose]
#
# Notes:
#   - Only tracked files are scanned.
#   - Auto-generated files that only carry `derived_from` are excluded.
#   - Output paths in the index are relative to the entity root.

set -euo pipefail

ROOT=""
ENTITY=""
OUTPUT=""
VERBOSE=false

usage() {
    echo "Usage: create-resource-index.sh --entity <entity-path> [--root <repo-root>] [--output <path>] [--verbose]"
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
        --entity)
            if [ $# -lt 2 ]; then
                echo "ERROR: --entity requires a path"
                exit 1
            fi
            ENTITY="$2"
            shift 2
            ;;
        --output)
            if [ $# -lt 2 ]; then
                echo "ERROR: --output requires a path"
                exit 1
            fi
            OUTPUT="$2"
            shift 2
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
            echo "ERROR: unknown option: $1"
            exit 1
            ;;
    esac
done

if [ -z "$ENTITY" ]; then
    usage
    exit 1
fi

if [ -z "$ROOT" ]; then
    ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
fi

if [ ! -d "$ROOT" ]; then
    echo "ERROR: repo root not found: $ROOT"
    exit 1
fi

python3 - "$ROOT" "$ENTITY" "$OUTPUT" "$VERBOSE" <<'PY'
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

root = os.path.abspath(sys.argv[1])
entity_arg = sys.argv[2]
output = sys.argv[3]
verbose = sys.argv[4].lower() == "true"

if os.path.isabs(entity_arg):
    entity_dir = os.path.abspath(entity_arg)
else:
    entity_dir = os.path.abspath(os.path.join(root, entity_arg))

if not os.path.isdir(entity_dir):
    print(f"ERROR: entity directory not found: {entity_dir}", file=sys.stderr)
    sys.exit(1)

if not os.path.commonpath([root, entity_dir]) == root:
    print(f"ERROR: entity path is outside repo root: {entity_dir}", file=sys.stderr)
    sys.exit(1)

entity_agnostic = os.path.join(entity_dir, "0AGNOSTIC.md")
if not os.path.isfile(entity_agnostic):
    print(f"ERROR: 0AGNOSTIC.md not found in entity: {entity_dir}", file=sys.stderr)
    sys.exit(1)


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        return handle.read()


def read_head(path: str, limit: int = 8192) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        return handle.read(limit)


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
    pattern = re.compile(rf"{re.escape(field)}:\s*['\"]?([0-9a-zA-Z_.-]+(?:-[0-9a-zA-Z_.-]+)*)['\"]?")
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def extract_comment_value(text: str, field: str) -> str:
    pattern = re.compile(rf"{re.escape(field)}:\s*['\"]?(.+?)['\"]?\s*$", re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


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
    for field in ("resource_type",):
        value = extract_yaml_field(head_text, field) or extract_comment_value(head_text, field)
        if value:
            return value

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
    if os.path.basename(rel_path) == "0AGNOSTIC.md":
        return "agnostic"
    if os.path.basename(rel_path) == "0INDEX.md":
        return "index"
    if os.path.basename(rel_path) == "README.md":
        return "readme"
    return "document"


def infer_resource_name(path: str, head_text: str) -> str:
    for field in ("resource_name",):
        value = extract_yaml_field(head_text, field) or extract_comment_value(head_text, field)
        if value:
            return value
    base = os.path.basename(path)
    if base.endswith(".jsonld"):
        return base[:-7]
    return os.path.splitext(base)[0]


entity_text = read_head(entity_agnostic)
entity_id = extract_yaml_field(entity_text, "entity_id") or extract_line_field(entity_text, "entity_id")
if not entity_id:
    print(f"ERROR: entity_id missing in {entity_agnostic}", file=sys.stderr)
    sys.exit(1)

entity_name = os.path.basename(entity_dir)
entity_rel = os.path.relpath(entity_dir, root)

raw = subprocess.check_output(
    ["git", "-C", root, "ls-files", "-z", "--", entity_rel],
    stderr=subprocess.DEVNULL,
)

entries = []
seen = {}

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

    ext = os.path.splitext(full_path)[1].lower()
    head = read_head(full_path)
    if is_derived_file(full_path, head):
        continue

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
        print(
            f"ERROR: duplicate resource UUID {identifier} in {rel_entity_path} and {seen[identifier]}",
            file=sys.stderr,
        )
        sys.exit(1)

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
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "entity_id": entity_id,
    "entity_name": entity_name,
    "entity_path": entity_rel,
    "resources": entries,
}

payload = json.dumps(index_data, indent=2) + "\n"

if output:
    output_path = output if os.path.isabs(output) else os.path.abspath(os.path.join(os.getcwd(), output))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(payload)
    print(f"WROTE: {output_path}")
else:
    sys.stdout.write(payload)

if verbose:
    print(f"Indexed {len(entries)} resources for {entity_rel}", file=sys.stderr)
PY
