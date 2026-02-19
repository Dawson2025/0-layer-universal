#!/usr/bin/env bash
# agnostic-sync.sh - Sync 0AGNOSTIC.md + .0agnostic/ to tool-specific formats
# Location: layer_0/layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant/scripts/
#
# Usage: agnostic-sync [options] [path]
#   --dry-run    Show what would be done without doing it
#   --force      Overwrite even if target is newer
#   --verbose    Show detailed output
#   --help       Show this help message

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Defaults
DRY_RUN=false
FORCE=false
VERBOSE=false
TARGET_DIR="."

# Source file names (numbered for explicit ordering)
AGNOSTIC_MD="0AGNOSTIC.md"
AGNOSTIC_DIR=".0agnostic"

# Shim templates
CLAUDE_SHIM="# CLAUDE.md - Auto-generated from 0AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit 0AGNOSTIC.md instead, then run: agnostic-sync
# Generated: $(date -Iseconds)

"

AGENTS_SHIM="# AGENTS.md - Auto-generated from 0AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit 0AGNOSTIC.md instead, then run: agnostic-sync
# Generated: $(date -Iseconds)

"

GEMINI_SHIM="# GEMINI.md - Auto-generated from 0AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit 0AGNOSTIC.md instead, then run: agnostic-sync
# Generated: $(date -Iseconds)

"

# Functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[OK]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_verbose() {
    if [[ "$VERBOSE" == "true" ]]; then
        echo -e "${BLUE}[VERBOSE]${NC} $1"
    fi
}

show_help() {
    cat << EOF
agnostic-sync - Sync 0AGNOSTIC.md + .0agnostic/ to tool-specific formats

USAGE:
    agnostic-sync [options] [path]

OPTIONS:
    --dry-run    Show what would be done without doing it
    --force      Overwrite even if target is newer
    --verbose    Show detailed output
    --help       Show this help message

ARGUMENTS:
    path         Directory containing 0AGNOSTIC.md (default: current directory)

EXAMPLES:
    agnostic-sync                     # Sync current directory
    agnostic-sync --dry-run           # Preview changes
    agnostic-sync /path/to/layer      # Sync specific directory
    agnostic-sync --verbose --force . # Force sync with detailed output

SOURCE FILES (edit these):
    0AGNOSTIC.md      - Primary agnostic context (sorts first)
    .0agnostic/       - Agnostic resources (sorts before .claude/)
      ├── skills/     - Skill definitions
      ├── agents/     - Agent definitions
      ├── rules/      - Rule definitions
      └── automation/ - Hooks/automation

GENERATED FILES (do not edit):
    0AGNOSTIC.md       →  CLAUDE.md, AGENTS.md, GEMINI.md
    .0agnostic/skills  →  .claude/skills/
    .0agnostic/agents  →  .claude/agents/
    .0agnostic/rules   →  .claude/rules/, .cursor/rules/
    .0agnostic/automation → .claude/hooks/

PRESERVED FILES (not overwritten):
    .claude/settings.json
    .claude/mcp.json
    .cursor/settings.json
    Any file starting with "# MANUAL"
EOF
}

# Check if file should be preserved (has MANUAL marker or is settings)
should_preserve() {
    local file="$1"
    local basename=$(basename "$file")

    # Always preserve settings files
    if [[ "$basename" == "settings.json" || "$basename" == "mcp.json" ]]; then
        return 0
    fi

    # Check for MANUAL marker in first line
    if [[ -f "$file" ]] && head -n1 "$file" 2>/dev/null | grep -q "# MANUAL"; then
        return 0
    fi

    return 1
}

# Generate tool-specific MD file from 0AGNOSTIC.md
generate_md() {
    local source="$1"
    local target="$2"
    local shim="$3"

    if [[ ! -f "$source" ]]; then
        log_warn "Source not found: $source"
        return 1
    fi

    if [[ -f "$target" ]] && should_preserve "$target"; then
        log_warn "Preserving manual file: $target"
        return 0
    fi

    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY-RUN] Would generate: $target"
        return 0
    fi

    log_verbose "Generating $target from $source"
    echo -e "$shim" > "$target"
    cat "$source" >> "$target"
    log_success "Generated: $target"
}

# Copy directory with preservation rules
copy_dir() {
    local source="$1"
    local target="$2"

    if [[ ! -d "$source" ]]; then
        log_verbose "Source directory not found: $source"
        return 0
    fi

    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY-RUN] Would copy: $source → $target"
        return 0
    fi

    # Create target directory
    mkdir -p "$target"

    # Copy files, respecting preservation rules
    find "$source" -type f | while read -r file; do
        local relative="${file#$source/}"
        local target_file="$target/$relative"
        local target_dir=$(dirname "$target_file")

        # Check if target should be preserved
        if [[ -f "$target_file" ]] && should_preserve "$target_file"; then
            log_warn "Preserving: $target_file"
            continue
        fi

        mkdir -p "$target_dir"
        cp "$file" "$target_file"
        log_verbose "Copied: $relative"
    done

    log_success "Copied: $source → $target"
}

# Convert rules to Cursor .mdc format
convert_to_mdc() {
    local source="$1"
    local target="$2"

    if [[ ! -d "$source" ]]; then
        log_verbose "Source rules directory not found: $source"
        return 0
    fi

    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY-RUN] Would convert to MDC: $source → $target"
        return 0
    fi

    mkdir -p "$target"

    # Convert each .md file to .mdc
    find "$source" -name "*.md" -type f | while read -r file; do
        local basename=$(basename "$file" .md)
        local target_file="$target/${basename}.mdc"

        if [[ -f "$target_file" ]] && should_preserve "$target_file"; then
            log_warn "Preserving: $target_file"
            continue
        fi

        # MDC format: just copy with different extension for now
        # Future: add Cursor-specific frontmatter if needed
        cp "$file" "$target_file"
        log_verbose "Converted: $basename.md → $basename.mdc"
    done

    log_success "Converted rules to MDC: $target"
}

# Main sync function
sync_directory() {
    local dir="$1"

    log_info "Syncing: $dir"

    # Check for 0AGNOSTIC.md
    if [[ ! -f "$dir/$AGNOSTIC_MD" ]]; then
        log_warn "No $AGNOSTIC_MD found in $dir"
        log_info "Checking for $AGNOSTIC_DIR/ folder only..."
    else
        # Generate tool-specific MD files
        generate_md "$dir/$AGNOSTIC_MD" "$dir/CLAUDE.md" "$CLAUDE_SHIM"
        generate_md "$dir/$AGNOSTIC_MD" "$dir/AGENTS.md" "$AGENTS_SHIM"
        generate_md "$dir/$AGNOSTIC_MD" "$dir/GEMINI.md" "$GEMINI_SHIM"
    fi

    # Sync .0agnostic/ folders
    if [[ -d "$dir/$AGNOSTIC_DIR" ]]; then
        log_info "Syncing $AGNOSTIC_DIR/ resources..."

        # Skills
        copy_dir "$dir/$AGNOSTIC_DIR/skills" "$dir/.claude/skills"

        # Agents
        copy_dir "$dir/$AGNOSTIC_DIR/agents" "$dir/.claude/agents"

        # Rules (to both .claude and .cursor)
        copy_dir "$dir/$AGNOSTIC_DIR/rules" "$dir/.claude/rules"
        convert_to_mdc "$dir/$AGNOSTIC_DIR/rules" "$dir/.cursor/rules"

        # Automation → Hooks
        copy_dir "$dir/$AGNOSTIC_DIR/automation" "$dir/.claude/hooks"
    else
        log_verbose "No $AGNOSTIC_DIR/ folder found in $dir"
    fi

    log_success "Sync complete: $dir"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --force)
            FORCE=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            show_help
            exit 0
            ;;
        -*)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
        *)
            TARGET_DIR="$1"
            shift
            ;;
    esac
done

# Resolve target directory
TARGET_DIR=$(realpath "$TARGET_DIR")

if [[ ! -d "$TARGET_DIR" ]]; then
    log_error "Directory not found: $TARGET_DIR"
    exit 1
fi

# Run sync
echo ""
echo "=========================================="
echo "  agnostic-sync"
echo "=========================================="
echo ""

if [[ "$DRY_RUN" == "true" ]]; then
    log_warn "DRY RUN MODE - No changes will be made"
    echo ""
fi

sync_directory "$TARGET_DIR"

echo ""
echo "=========================================="
log_success "Done!"
