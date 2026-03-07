#!/usr/bin/env bash
# resource_id: "d8e9f0a1-2b3c-4d5e-f6a7-8b9c0d1e2f3a"
# resource_type: "script"
# resource_name: "assign-section-uuids"
#
# Assigns a UUID v4 to every ## (h2) and ### (h3) heading in markdown files.
# Inserts <!-- section_id: "uuid" --> on the line above each heading.
# Skips headings inside code blocks (``` ... ```).
# Skips auto-generated files (CLAUDE.md, AGENTS.md, etc.).
#
# Usage: assign-section-uuids.sh [--dry-run] [--validate] [ROOT_DIR]

set -euo pipefail

DRY_RUN=false
VALIDATE=false
ROOT_DIR=""

for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        --validate) VALIDATE=true ;;
        *) ROOT_DIR="$arg" ;;
    esac
done

if [[ -z "$ROOT_DIR" ]]; then
    ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"  # tools/ → protocol/ → 03_protocols/ → .0agnostic/ → ROOT
fi

# Use Python for reliable multi-line processing
python3 - "$ROOT_DIR" "$DRY_RUN" "$VALIDATE" << 'PYTHON_SCRIPT'
import os, uuid, sys, re

root = sys.argv[1]
dry_run = sys.argv[2] == "True"
validate = sys.argv[3] == "True"

SKIP_NAMES = {
    'CLAUDE.md', 'AGENTS.md', 'GEMINI.md', 'OPENAI.md',
    '.cursorrules', 'copilot-instructions.md'
}
SKIP_DIRS = {'.git', 'node_modules', 'venv', '.venv', '__pycache__'}

total_files = 0
total_sections = 0
total_missing = 0
skipped_files = 0
duplicates = 0

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

    for fname in filenames:
        if not fname.endswith('.md'):
            continue
        if fname in SKIP_NAMES or fname.endswith('.integration.md'):
            skipped_files += 1
            continue

        fpath = os.path.join(dirpath, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception:
            continue

        if validate:
            # Check for duplicate section_ids and missing UUIDs
            seen_ids = set()
            in_code = False
            for i, line in enumerate(lines):
                if line.strip().startswith('```'):
                    in_code = not in_code
                    continue
                if in_code:
                    continue
                m = re.search(r'<!-- section_id: "([^"]+)" -->', line)
                if m:
                    sid = m.group(1)
                    if sid in seen_ids:
                        print(f"DUPLICATE: {sid} in {fpath}:{i+1}")
                        duplicates += 1
                    seen_ids.add(sid)
                if re.match(r'^#{2,3}\s', line.strip()):
                    if i == 0 or '<!-- section_id:' not in lines[i-1]:
                        print(f"MISSING: {fpath}:{i+1}: {line.strip()}")
                        total_missing += 1
            continue

        modified = False
        new_lines = []
        in_code = False
        file_sections = 0

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith('```'):
                in_code = not in_code
                new_lines.append(line)
                continue

            if in_code:
                new_lines.append(line)
                continue

            if re.match(r'^#{2,3}\s', stripped):
                if new_lines and '<!-- section_id:' in new_lines[-1]:
                    new_lines.append(line)
                    continue

                sid = str(uuid.uuid4())
                if dry_run:
                    print(f"[dry-run] Would add section_id {sid} before: {stripped}")
                else:
                    new_lines.append(f'<!-- section_id: "{sid}" -->\n')
                new_lines.append(line)
                modified = True
                file_sections += 1
                total_sections += 1
            else:
                new_lines.append(line)

        if modified and not dry_run:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            total_files += 1

if validate:
    print(f"\nValidation complete:")
    print(f"Missing section_ids: {total_missing}")
    print(f"Duplicate section_ids: {duplicates}")
    sys.exit(1 if total_missing > 0 or duplicates > 0 else 0)
else:
    print(f"\n=== Section UUID Assignment Complete ===")
    print(f"Files modified:    {total_files}")
    print(f"Sections added:    {total_sections}")
    print(f"Files skipped:     {skipped_files} (auto-generated)")
    if dry_run:
        print("(dry run — no files modified)")
PYTHON_SCRIPT
