#!/bin/bash
# resource_id: "1a5ddff5-c97f-4578-8c01-e7a6bdcdbfde"
# resource_type: "script"
# resource_name: "agnostic-sync"
# agnostic-sync.sh - Sync 0AGNOSTIC.md to tool-specific system prompts
# Usage: ./agnostic-sync.sh [all|claude|cursor|copilot|gemini|aider|codex]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check if 0AGNOSTIC.md exists
if [[ ! -f "$PROJECT_ROOT/0AGNOSTIC.md" ]]; then
    log_error "0AGNOSTIC.md not found at $PROJECT_ROOT"
    exit 1
fi

sync_claude() {
    log_info "Syncing to Claude..."

    # Copy .0agnostic content to merge workspace
    if [[ -d "$PROJECT_ROOT/.0agnostic" ]]; then
        cp -r "$PROJECT_ROOT/.0agnostic/agents" "$PROJECT_ROOT/.1claude_merge/0_synced/" 2>/dev/null || true
        cp -r "$PROJECT_ROOT/.0agnostic/skills" "$PROJECT_ROOT/.1claude_merge/0_synced/" 2>/dev/null || true
        cp -r "$PROJECT_ROOT/.0agnostic/hooks" "$PROJECT_ROOT/.1claude_merge/0_synced/" 2>/dev/null || true
    fi

    # Generate CLAUDE.md from 0AGNOSTIC.md
    cat > "$PROJECT_ROOT/CLAUDE.md" << 'HEADER'
# Claude Code Context

## Identity
HEADER

    # Extract and transform content from 0AGNOSTIC.md
    sed -n '/^## Identity/,/^## Triggers/p' "$PROJECT_ROOT/0AGNOSTIC.md" | head -n -1 | tail -n +2 >> "$PROJECT_ROOT/CLAUDE.md"

    cat >> "$PROJECT_ROOT/CLAUDE.md" << 'MIDDLE'

## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Proposals**: `layer_-1_group/layer_-1_00_layer_registry/proposals/`
- **Features**: `layer_0_group/layer_0_features/`

## Key Behaviors
MIDDLE

    # Add triggers as behaviors
    sed -n '/^## Triggers/,/^## Pointers/p' "$PROJECT_ROOT/0AGNOSTIC.md" | head -n -1 | tail -n +2 >> "$PROJECT_ROOT/CLAUDE.md"

    cat >> "$PROJECT_ROOT/CLAUDE.md" << 'FOOTER'

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
FOOTER

    # Create .claude directory structure if needed
    mkdir -p "$PROJECT_ROOT/.claude"

    log_info "Claude sync complete"
}

sync_cursor() {
    log_info "Syncing to Cursor..."

    # Generate .cursorrules
    cat > "$PROJECT_ROOT/.cursorrules" << 'HEADER'
# Cursor Rules - Auto-generated from 0AGNOSTIC.md

HEADER

    # Extract identity
    sed -n '/^## Identity/,/^## Triggers/p' "$PROJECT_ROOT/0AGNOSTIC.md" | head -n -1 >> "$PROJECT_ROOT/.cursorrules"

    cat >> "$PROJECT_ROOT/.cursorrules" << 'FOOTER'

# Navigation
- Resources: .0agnostic/
- Proposals: layer_-1_group/layer_-1_00_layer_registry/proposals/

---
*Auto-generated from 0AGNOSTIC.md*
FOOTER

    mkdir -p "$PROJECT_ROOT/.cursor/rules"
    log_info "Cursor sync complete"
}

sync_gemini() {
    log_info "Syncing to Gemini..."

    # Generate GEMINI.md
    cat > "$PROJECT_ROOT/GEMINI.md" << 'HEADER'
# Gemini Context - Auto-generated from 0AGNOSTIC.md

HEADER

    cat "$PROJECT_ROOT/0AGNOSTIC.md" >> "$PROJECT_ROOT/GEMINI.md"

    cat >> "$PROJECT_ROOT/GEMINI.md" << 'FOOTER'

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
FOOTER

    log_info "Gemini sync complete"
}

sync_codex() {
    log_info "Syncing to Codex..."

    # Generate AGENTS.md
    cat > "$PROJECT_ROOT/AGENTS.md" << 'HEADER'
# OpenAI Codex/Agents Context - Auto-generated from 0AGNOSTIC.md

HEADER

    cat "$PROJECT_ROOT/0AGNOSTIC.md" >> "$PROJECT_ROOT/AGENTS.md"

    cat >> "$PROJECT_ROOT/AGENTS.md" << 'FOOTER'

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
FOOTER

    log_info "Codex sync complete"
}

sync_copilot() {
    log_info "Syncing to Copilot..."

    mkdir -p "$PROJECT_ROOT/.github/instructions"

    # Generate copilot-instructions.md
    cat > "$PROJECT_ROOT/.github/copilot-instructions.md" << 'HEADER'
# GitHub Copilot Instructions - Auto-generated from 0AGNOSTIC.md

HEADER

    cat "$PROJECT_ROOT/0AGNOSTIC.md" >> "$PROJECT_ROOT/.github/copilot-instructions.md"

    cat >> "$PROJECT_ROOT/.github/copilot-instructions.md" << 'FOOTER'

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
FOOTER

    log_info "Copilot sync complete"
}

sync_aider() {
    log_info "Syncing to Aider..."

    # Generate .aider.conf.yml (basic config)
    cat > "$PROJECT_ROOT/.aider.conf.yml" << 'EOF'
# Aider Configuration - Auto-generated from 0AGNOSTIC.md

# Read the project context
read:
  - 0AGNOSTIC.md
  - 0INDEX.md

# Project description (from 0AGNOSTIC.md Identity section)
# Layer -1 Research Project: better_ai_system
# Researching improvements to AI system architecture

---
# Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh
EOF

    log_info "Aider sync complete"
}

sync_all() {
    log_info "Syncing all tools..."
    sync_claude
    sync_cursor
    sync_gemini
    sync_codex
    sync_copilot
    sync_aider
    log_info "All tools synced successfully!"
}

# Main
case "${1:-all}" in
    all) sync_all ;;
    claude) sync_claude ;;
    cursor) sync_cursor ;;
    copilot) sync_copilot ;;
    gemini) sync_gemini ;;
    aider) sync_aider ;;
    codex) sync_codex ;;
    *)
        echo "Usage: $0 [all|claude|cursor|copilot|gemini|aider|codex]"
        exit 1
        ;;
esac
