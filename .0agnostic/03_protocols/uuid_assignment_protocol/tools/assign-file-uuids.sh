#!/usr/bin/env bash
# resource_id: "68c9cfcc-9915-47f6-be3a-2c75fbd7ef7e"
# resource_type: "script"
# resource_name: "assign-file-uuids"
# assign-file-uuids.sh — Assign resource_id/file_id UUIDs to every file
# Phase 1b of the UUID Identity System implementation
#
# Usage:
#   assign-file-uuids.sh [--dry-run] [--type=TYPE] [--verbose] [REPO_ROOT]
#
# Types: md, sh, json, jsonld, derived, py, js, html, css, txt, yaml, qmd, ini, rules, svg, env
#
# What it does:
#   - .md/.qmd files: adds resource_id in YAML frontmatter
#   - .sh/.py/.yaml/.yml/.ini/.rules/.env files: adds resource_id as # comment header
#   - .js/.mjs/.jsx files: adds resource_id as // comment header
#   - .css files: adds resource_id as /* */ comment header
#   - .html/.svg files: adds resource_id as <!-- --> comment header
#   - .txt files: adds resource_id as # comment header
#   - .json/.jsonld files: adds file_id in JSON root object
#   - Auto-generated files (CLAUDE.md, AGENTS.md, etc.): adds derived_from comment
#
# Only processes files tracked by git (skips submodule contents)

set -euo pipefail

DRY_RUN=false
VERBOSE=false
FILE_TYPE=""
REPO_ROOT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --verbose) VERBOSE=true; shift ;;
    --type=*) FILE_TYPE="${1#--type=}"; shift ;;
    *) REPO_ROOT="$1"; shift ;;
  esac
done

if [[ -z "$REPO_ROOT" ]]; then
  REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo ".")
fi

# Counters
declare -A COUNTS
COUNTS[md_added]=0
COUNTS[md_skipped]=0
COUNTS[sh_added]=0
COUNTS[sh_skipped]=0
COUNTS[json_added]=0
COUNTS[json_skipped]=0
COUNTS[jsonld_added]=0
COUNTS[jsonld_skipped]=0
COUNTS[derived_added]=0
COUNTS[derived_skipped]=0
COUNTS[hash_added]=0
COUNTS[hash_skipped]=0
COUNTS[slash_added]=0
COUNTS[slash_skipped]=0
COUNTS[css_added]=0
COUNTS[css_skipped]=0
COUNTS[html_added]=0
COUNTS[html_skipped]=0
COUNTS[errors]=0

log() { echo "$@"; }
verbose() { if [[ "$VERBOSE" == true ]]; then echo "  [v] $*" >&2; fi; return 0; }

gen_uuid() {
  if command -v uuidgen &>/dev/null; then
    uuidgen | tr '[:upper:]' '[:lower:]'
  elif [[ -f /proc/sys/kernel/random/uuid ]]; then
    cat /proc/sys/kernel/random/uuid
  else
    python3 -c "import uuid; print(uuid.uuid4())"
  fi
}

# Determine resource_type from file path
# IMPORTANT: filename-based matches return immediately to prevent
# the path-based case from also firing (which caused the multi-line
# resource_type bug — "agnostic\ndocument" etc.)
get_resource_type() {
  local filepath="$1"
  local basename
  basename=$(basename "$filepath")

  # Filename-specific types take priority — return immediately on match
  case "$basename" in
    0AGNOSTIC.md) echo "agnostic_document"; return ;;
    0INDEX.md) echo "index_document"; return ;;
    README.md) echo "readme"; return ;;
    SKILL.md) echo "skill"; return ;;
    *.integration.md) echo "integration"; return ;;
    CLAUDE.md|AGENTS.md|GEMINI.md|OPENAI.md) echo "derived"; return ;;
    .cursorrules) echo "derived"; return ;;
  esac

  # Path-based types — only reached for files without a filename match above
  case "$filepath" in
    */01_knowledge/*) echo "knowledge" ;;
    */02_rules/*) echo "rule" ;;
    */03_protocols/*) echo "protocol" ;;
    */04_episodic_memory/*) echo "episodic" ;;
    */05_handoff_documents/*) echo "handoff" ;;
    */outputs/*) echo "output" ;;
    */synthesis/*) echo "synthesis" ;;
    *) echo "document" ;;
  esac
}

# Check if file is auto-generated (derived)
is_derived() {
  local basename
  basename=$(basename "$1")
  case "$basename" in
    CLAUDE.md|AGENTS.md|GEMINI.md|OPENAI.md|.cursorrules) return 0 ;;
    *.integration.md) return 0 ;;
    copilot-instructions.md) return 0 ;;
  esac
  return 1
}

# Find the entity_id from the nearest 0AGNOSTIC.md
find_source_uuid() {
  local filepath="$1"
  local dir
  dir=$(dirname "$filepath")

  while [[ "$dir" != "/" && "$dir" != "." ]]; do
    if [[ -f "$dir/0AGNOSTIC.md" ]]; then
      local uuid
      uuid=$(grep -m1 'entity_id:' "$dir/0AGNOSTIC.md" 2>/dev/null | sed 's/.*entity_id:[[:space:]]*//' | tr -d '"' | tr -d "'")
      if [[ -n "$uuid" ]]; then
        echo "$uuid"
        return 0
      fi
    fi
    dir=$(dirname "$dir")
  done
  return 1
}

# Process a .md file — add resource_id in YAML frontmatter
process_md() {
  local file="$1"
  local rel="${file#$REPO_ROOT/}"

  # Skip derived files
  if is_derived "$file"; then
    return 0
  fi

  # Check if already has resource_id
  if head -20 "$file" 2>/dev/null | grep -q '^resource_id:'; then
    COUNTS[md_skipped]=$((${COUNTS[md_skipped]} + 1))
    return 0
  fi

  local first_line
  first_line=$(head -1 "$file" 2>/dev/null) || return 0

  local uuid
  uuid=$(gen_uuid)
  local rtype
  rtype=$(get_resource_type "$rel")
  local rname
  rname=$(basename "$file" .md)

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add resource_id to: $rel"
    COUNTS[md_added]=$((${COUNTS[md_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"

  if [[ "$first_line" == "---" ]]; then
    # Has existing frontmatter — insert resource_id after first ---
    {
      echo "---"
      echo "resource_id: \"$uuid\""
      echo "resource_type: \"$rtype\""
      echo "resource_name: \"$rname\""
      tail -n +2 "$file"
    } > "$tmp"
  else
    # No frontmatter — add new frontmatter block
    {
      echo "---"
      echo "resource_id: \"$uuid\""
      echo "resource_type: \"$rtype\""
      echo "resource_name: \"$rname\""
      echo "---"
      cat "$file"
    } > "$tmp"
  fi

  mv "$tmp" "$file"
  COUNTS[md_added]=$((${COUNTS[md_added]} + 1))
  verbose "Added resource_id to: $rel"
}

# Process a .sh file — add resource_id in comment header
process_sh() {
  local file="$1"
  local rel="${file#$REPO_ROOT/}"

  # Check if already has resource_id
  if head -5 "$file" 2>/dev/null | grep -q '^# resource_id:'; then
    COUNTS[sh_skipped]=$((${COUNTS[sh_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)
  local rname
  rname=$(basename "$file" .sh)

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add resource_id to: $rel"
    COUNTS[sh_added]=$((${COUNTS[sh_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"
  local first_line
  first_line=$(head -1 "$file" 2>/dev/null) || return 0

  if [[ "$first_line" == "#!"* ]]; then
    # Has shebang — insert after it
    {
      echo "$first_line"
      echo "# resource_id: \"$uuid\""
      echo "# resource_type: \"script\""
      echo "# resource_name: \"$rname\""
      tail -n +2 "$file"
    } > "$tmp"
  else
    # No shebang — insert at top
    {
      echo "# resource_id: \"$uuid\""
      echo "# resource_type: \"script\""
      echo "# resource_name: \"$rname\""
      cat "$file"
    } > "$tmp"
  fi

  mv "$tmp" "$file"
  COUNTS[sh_added]=$((${COUNTS[sh_added]} + 1))
  verbose "Added resource_id to: $rel"
}

# Process a .json file — add file_id to root object
process_json() {
  local file="$1"
  local rel="${file#$REPO_ROOT/}"

  # Check if already has file_id
  if grep -q '"file_id"' "$file" 2>/dev/null; then
    COUNTS[json_skipped]=$((${COUNTS[json_skipped]} + 1))
    return 0
  fi

  # Verify it's valid JSON with a root object
  if ! python3 -c "import json; d=json.load(open('$file')); assert isinstance(d, dict)" 2>/dev/null; then
    verbose "Skipping non-object JSON: $rel"
    COUNTS[json_skipped]=$((${COUNTS[json_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add file_id to: $rel"
    COUNTS[json_added]=$((${COUNTS[json_added]} + 1))
    return 0
  fi

  # Use python3 for safe JSON manipulation
  python3 -c "
import json, sys, collections
with open('$file', 'r') as f:
    content = f.read()
data = json.loads(content, object_pairs_hook=collections.OrderedDict)
if isinstance(data, dict):
    new = collections.OrderedDict()
    new['file_id'] = '$uuid'
    new.update(data)
    with open('$file', 'w') as f:
        json.dump(new, f, indent=2, ensure_ascii=False)
        f.write('\n')
" 2>/dev/null

  if [[ $? -eq 0 ]]; then
    COUNTS[json_added]=$((${COUNTS[json_added]} + 1))
    verbose "Added file_id to: $rel"
  else
    COUNTS[errors]=$((${COUNTS[errors]} + 1))
    log "  ERROR: Failed to add file_id to $rel"
  fi
}

# Process a .jsonld file — add file_id to root object
process_jsonld() {
  local file="$1"
  local rel="${file#$REPO_ROOT/}"

  # Check if already has file_id
  if grep -q '"file_id"' "$file" 2>/dev/null; then
    COUNTS[jsonld_skipped]=$((${COUNTS[jsonld_skipped]} + 1))
    return 0
  fi

  # Verify it's valid JSON
  if ! python3 -c "import json; json.load(open('$file'))" 2>/dev/null; then
    verbose "Skipping invalid JSONLD: $rel"
    COUNTS[jsonld_skipped]=$((${COUNTS[jsonld_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add file_id to: $rel"
    COUNTS[jsonld_added]=$((${COUNTS[jsonld_added]} + 1))
    return 0
  fi

  python3 -c "
import json, sys, collections
with open('$file', 'r') as f:
    content = f.read()
data = json.loads(content, object_pairs_hook=collections.OrderedDict)
if isinstance(data, dict):
    new = collections.OrderedDict()
    new['file_id'] = '$uuid'
    new.update(data)
    with open('$file', 'w') as f:
        json.dump(new, f, indent=2, ensure_ascii=False)
        f.write('\n')
" 2>/dev/null

  if [[ $? -eq 0 ]]; then
    COUNTS[jsonld_added]=$((${COUNTS[jsonld_added]} + 1))
    verbose "Added file_id to: $rel"
  else
    COUNTS[errors]=$((${COUNTS[errors]} + 1))
    log "  ERROR: Failed to add file_id to $rel"
  fi
}

# Process a derived/auto-generated file
process_derived() {
  local file="$1"
  local rel="${file#$REPO_ROOT/}"

  # Check if already has derived_from
  if head -5 "$file" 2>/dev/null | grep -q 'derived_from:'; then
    COUNTS[derived_skipped]=$((${COUNTS[derived_skipped]} + 1))
    return 0
  fi

  # Find source UUID from nearest 0AGNOSTIC.md
  local source_uuid
  source_uuid=$(find_source_uuid "$file") || true

  if [[ -z "$source_uuid" ]]; then
    verbose "No source entity_id found for derived file: $rel"
    COUNTS[derived_skipped]=$((${COUNTS[derived_skipped]} + 1))
    return 0
  fi

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add derived_from to: $rel (source: $source_uuid)"
    COUNTS[derived_added]=$((${COUNTS[derived_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"
  local basename_f
  basename_f=$(basename "$file")

  case "$basename_f" in
    *.md)
      # Markdown derived file — add as HTML comment at top
      {
        echo "<!-- derived_from: \"$source_uuid\" -->"
        cat "$file"
      } > "$tmp"
      ;;
    .cursorrules|copilot-instructions.md)
      # Config files — add as comment
      {
        echo "# derived_from: \"$source_uuid\""
        cat "$file"
      } > "$tmp"
      ;;
    *)
      verbose "Unknown derived file type: $basename_f"
      COUNTS[derived_skipped]=$((${COUNTS[derived_skipped]} + 1))
      return 0
      ;;
  esac

  mv "$tmp" "$file"
  COUNTS[derived_added]=$((${COUNTS[derived_added]} + 1))
  verbose "Added derived_from to: $rel"
}

# Process files that use # comment syntax (py, yaml, yml, ini, rules, txt, env)
process_hash_comment() {
  local file="$1"
  local ext="$2"
  local rel="${file#$REPO_ROOT/}"

  # Check if already has resource_id
  if head -5 "$file" 2>/dev/null | grep -q '^# resource_id:'; then
    COUNTS[hash_skipped]=$((${COUNTS[hash_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)
  local rname
  rname=$(basename "$file" ".$ext")
  local rtype
  rtype=$(get_resource_type "$rel")

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add resource_id to: $rel"
    COUNTS[hash_added]=$((${COUNTS[hash_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"
  local first_line
  first_line=$(head -1 "$file" 2>/dev/null) || return 0

  if [[ "$first_line" == "#!"* ]]; then
    {
      echo "$first_line"
      echo "# resource_id: \"$uuid\""
      echo "# resource_type: \"$rtype\""
      echo "# resource_name: \"$rname\""
      tail -n +2 "$file"
    } > "$tmp"
  else
    {
      echo "# resource_id: \"$uuid\""
      echo "# resource_type: \"$rtype\""
      echo "# resource_name: \"$rname\""
      cat "$file"
    } > "$tmp"
  fi

  mv "$tmp" "$file"
  COUNTS[hash_added]=$((${COUNTS[hash_added]} + 1))
  verbose "Added resource_id to: $rel"
}

# Process files that use // comment syntax (js, mjs, jsx)
process_slash_comment() {
  local file="$1"
  local ext="$2"
  local rel="${file#$REPO_ROOT/}"

  if head -5 "$file" 2>/dev/null | grep -q '^// resource_id:'; then
    COUNTS[slash_skipped]=$((${COUNTS[slash_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)
  local rname
  rname=$(basename "$file" ".$ext")
  local rtype
  rtype=$(get_resource_type "$rel")

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add resource_id to: $rel"
    COUNTS[slash_added]=$((${COUNTS[slash_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"
  {
    echo "// resource_id: \"$uuid\""
    echo "// resource_type: \"$rtype\""
    echo "// resource_name: \"$rname\""
    cat "$file"
  } > "$tmp"

  mv "$tmp" "$file"
  COUNTS[slash_added]=$((${COUNTS[slash_added]} + 1))
  verbose "Added resource_id to: $rel"
}

# Process .css files — use /* */ comment syntax
process_css() {
  local file="$1"
  local rel="${file#$REPO_ROOT/}"

  if head -5 "$file" 2>/dev/null | grep -q 'resource_id:'; then
    COUNTS[css_skipped]=$((${COUNTS[css_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)
  local rname
  rname=$(basename "$file" .css)
  local rtype
  rtype=$(get_resource_type "$rel")

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add resource_id to: $rel"
    COUNTS[css_added]=$((${COUNTS[css_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"
  {
    echo "/* resource_id: \"$uuid\" */"
    echo "/* resource_type: \"$rtype\" */"
    echo "/* resource_name: \"$rname\" */"
    cat "$file"
  } > "$tmp"

  mv "$tmp" "$file"
  COUNTS[css_added]=$((${COUNTS[css_added]} + 1))
  verbose "Added resource_id to: $rel"
}

# Process .html/.svg files — use <!-- --> comment syntax
process_html_comment() {
  local file="$1"
  local ext="$2"
  local rel="${file#$REPO_ROOT/}"

  if head -5 "$file" 2>/dev/null | grep -q 'resource_id:'; then
    COUNTS[html_skipped]=$((${COUNTS[html_skipped]} + 1))
    return 0
  fi

  local uuid
  uuid=$(gen_uuid)
  local rname
  rname=$(basename "$file" ".$ext")
  local rtype
  rtype=$(get_resource_type "$rel")

  if [[ "$DRY_RUN" == true ]]; then
    verbose "Would add resource_id to: $rel"
    COUNTS[html_added]=$((${COUNTS[html_added]} + 1))
    return 0
  fi

  local tmp="${file}.uuid.tmp"
  local first_line
  first_line=$(head -1 "$file" 2>/dev/null) || return 0

  if [[ "$first_line" == "<!DOCTYPE"* || "$first_line" == "<!doctype"* ]]; then
    {
      echo "$first_line"
      echo "<!-- resource_id: \"$uuid\" -->"
      echo "<!-- resource_type: \"$rtype\" -->"
      echo "<!-- resource_name: \"$rname\" -->"
      tail -n +2 "$file"
    } > "$tmp"
  elif [[ "$first_line" == "<?xml"* ]]; then
    {
      echo "$first_line"
      echo "<!-- resource_id: \"$uuid\" -->"
      echo "<!-- resource_type: \"$rtype\" -->"
      echo "<!-- resource_name: \"$rname\" -->"
      tail -n +2 "$file"
    } > "$tmp"
  else
    {
      echo "<!-- resource_id: \"$uuid\" -->"
      echo "<!-- resource_type: \"$rtype\" -->"
      echo "<!-- resource_name: \"$rname\" -->"
      cat "$file"
    } > "$tmp"
  fi

  mv "$tmp" "$file"
  COUNTS[html_added]=$((${COUNTS[html_added]} + 1))
  verbose "Added resource_id to: $rel"
}

log "=== File UUID Assignment Tool ==="
log "Repo root: $REPO_ROOT"
[[ "$DRY_RUN" == true ]] && log "Mode: DRY RUN"
[[ -n "$FILE_TYPE" ]] && log "Filter: --type=$FILE_TYPE"
log ""

# Get list of git-tracked files (excludes submodule contents)
get_tracked_files() {
  local ext="$1"
  git -C "$REPO_ROOT" ls-files -- "*.$ext" 2>/dev/null
}

# Process .md files
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "md" ]]; then
  log "Processing .md files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue

    if is_derived "$local_file"; then
      continue  # Handle in derived pass
    fi
    process_md "$local_file"
  done < <(get_tracked_files "md")
  log "  .md: ${COUNTS[md_added]} added, ${COUNTS[md_skipped]} already had ID"
fi

# Process .sh files
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "sh" ]]; then
  log "Processing .sh files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_sh "$local_file"
  done < <(get_tracked_files "sh")
  log "  .sh: ${COUNTS[sh_added]} added, ${COUNTS[sh_skipped]} already had ID"
fi

# Process .json files
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "json" ]]; then
  log "Processing .json files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_json "$local_file"
  done < <(get_tracked_files "json")
  log "  .json: ${COUNTS[json_added]} added, ${COUNTS[json_skipped]} already had ID"
fi

# Process .jsonld files
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "jsonld" ]]; then
  log "Processing .jsonld files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_jsonld "$local_file"
  done < <(get_tracked_files "jsonld")
  log "  .jsonld: ${COUNTS[jsonld_added]} added, ${COUNTS[jsonld_skipped]} already had ID"
fi

# Process derived/auto-generated files
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "derived" ]]; then
  log "Processing derived files..."
  for pattern in CLAUDE.md AGENTS.md GEMINI.md OPENAI.md .cursorrules copilot-instructions.md; do
    while IFS= read -r rel_file; do
      [[ -z "$rel_file" ]] && continue
      local_file="$REPO_ROOT/$rel_file"
      [[ -f "$local_file" ]] || continue
      process_derived "$local_file"
    done < <(git -C "$REPO_ROOT" ls-files -- "*/$pattern" "$pattern" 2>/dev/null)
  done
  # Also handle .integration.md
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_derived "$local_file"
  done < <(git -C "$REPO_ROOT" ls-files -- "*.integration.md" 2>/dev/null)
  log "  derived: ${COUNTS[derived_added]} added, ${COUNTS[derived_skipped]} already had ref"
fi

# Process .py files (# comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "py" ]]; then
  log "Processing .py files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_hash_comment "$local_file" "py"
  done < <(get_tracked_files "py")
  log "  .py: ${COUNTS[hash_added]} added, ${COUNTS[hash_skipped]} already had ID"
  # Reset for next type
  py_added=${COUNTS[hash_added]}
  py_skipped=${COUNTS[hash_skipped]}
  COUNTS[hash_added]=0
  COUNTS[hash_skipped]=0
fi

# Process .js files (// comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "js" ]]; then
  log "Processing .js/.mjs/.jsx files..."
  for ext in js mjs jsx; do
    while IFS= read -r rel_file; do
      [[ -z "$rel_file" ]] && continue
      local_file="$REPO_ROOT/$rel_file"
      [[ -f "$local_file" ]] || continue
      process_slash_comment "$local_file" "$ext"
    done < <(get_tracked_files "$ext")
  done
  log "  .js/.mjs/.jsx: ${COUNTS[slash_added]} added, ${COUNTS[slash_skipped]} already had ID"
fi

# Process .html files (<!-- --> comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "html" ]]; then
  log "Processing .html files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_html_comment "$local_file" "html"
  done < <(get_tracked_files "html")
  log "  .html: ${COUNTS[html_added]} added, ${COUNTS[html_skipped]} already had ID"
fi

# Process .svg files (<!-- --> comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "svg" ]]; then
  log "Processing .svg files..."
  html_before=${COUNTS[html_added]}
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_html_comment "$local_file" "svg"
  done < <(get_tracked_files "svg")
  svg_added=$(( ${COUNTS[html_added]} - html_before ))
  log "  .svg: $svg_added added"
fi

# Process .css files (/* */ comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "css" ]]; then
  log "Processing .css files..."
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_css "$local_file"
  done < <(get_tracked_files "css")
  log "  .css: ${COUNTS[css_added]} added, ${COUNTS[css_skipped]} already had ID"
fi

# Process .qmd files (YAML frontmatter like .md)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "qmd" ]]; then
  log "Processing .qmd files..."
  qmd_added=0
  qmd_skipped=0
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    # Reuse md processing but track separately
    before=${COUNTS[md_added]}
    process_md "$local_file"
    if [[ ${COUNTS[md_added]} -gt $before ]]; then
      qmd_added=$((qmd_added + 1))
    else
      qmd_skipped=$((qmd_skipped + 1))
    fi
  done < <(get_tracked_files "qmd")
  log "  .qmd: $qmd_added added, $qmd_skipped already had ID"
fi

# Process .yaml/.yml files (# comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "yaml" ]]; then
  log "Processing .yaml/.yml files..."
  for ext in yaml yml; do
    while IFS= read -r rel_file; do
      [[ -z "$rel_file" ]] && continue
      local_file="$REPO_ROOT/$rel_file"
      [[ -f "$local_file" ]] || continue
      process_hash_comment "$local_file" "$ext"
    done < <(get_tracked_files "$ext")
  done
  log "  .yaml/.yml: ${COUNTS[hash_added]} added, ${COUNTS[hash_skipped]} already had ID"
fi

# Process .txt files (# comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "txt" ]]; then
  log "Processing .txt files..."
  COUNTS[hash_added]=0
  COUNTS[hash_skipped]=0
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_hash_comment "$local_file" "txt"
  done < <(get_tracked_files "txt")
  log "  .txt: ${COUNTS[hash_added]} added, ${COUNTS[hash_skipped]} already had ID"
fi

# Process .rules files (# comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "rules" ]]; then
  log "Processing .rules files..."
  COUNTS[hash_added]=0
  COUNTS[hash_skipped]=0
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_hash_comment "$local_file" "rules"
  done < <(get_tracked_files "rules")
  log "  .rules: ${COUNTS[hash_added]} added, ${COUNTS[hash_skipped]} already had ID"
fi

# Process .ini files (# comment — ini also supports ; but # is safer)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "ini" ]]; then
  log "Processing .ini files..."
  COUNTS[hash_added]=0
  COUNTS[hash_skipped]=0
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_hash_comment "$local_file" "ini"
  done < <(get_tracked_files "ini")
  log "  .ini: ${COUNTS[hash_added]} added, ${COUNTS[hash_skipped]} already had ID"
fi

# Process .env files (# comment)
if [[ -z "$FILE_TYPE" || "$FILE_TYPE" == "env" ]]; then
  log "Processing .env files..."
  COUNTS[hash_added]=0
  COUNTS[hash_skipped]=0
  while IFS= read -r rel_file; do
    [[ -z "$rel_file" ]] && continue
    local_file="$REPO_ROOT/$rel_file"
    [[ -f "$local_file" ]] || continue
    process_hash_comment "$local_file" "env"
  done < <(get_tracked_files "env")
  log "  .env: ${COUNTS[hash_added]} added, ${COUNTS[hash_skipped]} already had ID"
fi

log ""
log "=== Summary ==="
total_added=$(( ${COUNTS[md_added]} + ${COUNTS[sh_added]} + ${COUNTS[json_added]} + ${COUNTS[jsonld_added]} + ${COUNTS[derived_added]} + ${COUNTS[slash_added]} + ${COUNTS[css_added]} + ${COUNTS[html_added]} + ${py_added:-0} ))
total_skipped=$(( ${COUNTS[md_skipped]} + ${COUNTS[sh_skipped]} + ${COUNTS[json_skipped]} + ${COUNTS[jsonld_skipped]} + ${COUNTS[derived_skipped]} + ${COUNTS[slash_skipped]} + ${COUNTS[css_skipped]} + ${COUNTS[html_skipped]} + ${py_skipped:-0} ))
log "Total added: $total_added"
log "Total skipped: $total_skipped"
log "Errors: ${COUNTS[errors]}"
[[ "$DRY_RUN" == true ]] && log "(Dry run — no files were modified)"
