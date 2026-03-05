#!/usr/bin/env bash
# resource_id: "7b25656d-2b5e-4bd2-8374-66d031f97a19"
# resource_type: "script"
# resource_name: "recover_missing_setup_files.sync-conflict-20260126-035815-IF2WOGZ"
set -euo pipefail

usage() {
  echo "Usage: $0 [--dry-run] <mapping_csv>" >&2
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

dry_run=false
if [[ "${1:-}" == "--dry-run" ]]; then
  dry_run=true
  shift
fi

map_file="${1:-}"
if [[ -z "$map_file" || ! -f "$map_file" ]]; then
  usage
  exit 1
fi

while IFS=',' read -r source_type original_commit original_path target_path root_cause; do
  if [[ "$source_type" == "source_type" ]]; then
    continue
  fi

  if [[ "$source_type" != "filesystem" ]]; then
    echo "Unsupported source_type: $source_type (expected filesystem)" >&2
    exit 1
  fi

  if [[ ! -f "$original_path" ]]; then
    echo "Missing source file: $original_path" >&2
    exit 1
  fi

  if [[ "$dry_run" == "true" ]]; then
    echo "DRY RUN: copy $original_path -> $target_path"
    continue
  fi

  mkdir -p "$(dirname "$target_path")"
  cp -p "$original_path" "$target_path"
  echo "Copied $original_path -> $target_path"
done < "$map_file"
