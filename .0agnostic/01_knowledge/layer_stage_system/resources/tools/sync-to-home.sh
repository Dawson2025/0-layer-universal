#!/usr/bin/env bash
# Sync .0agnostic/ from 0_layer_universal to home directory
# Also updates ~/.claude/CLAUDE.md with relevant rule summaries
#
# Usage: bash sync-to-home.sh [repo_root]
#
# What it does:
# 1. Copies .0agnostic/ from repo to ~/.0agnostic/ (rsync, preserves structure)
# 2. Reports what changed (diff before copy)
# 3. Idempotent — safe to run multiple times

set -euo pipefail

REPO_ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)}"
SOURCE="$REPO_ROOT/.0agnostic"
DEST="$HOME/.0agnostic"

echo "======================================================="
echo "Sync .0agnostic/ to home directory"
echo "Source: $SOURCE"
echo "Dest:   $DEST"
echo "======================================================="
echo ""

if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Source directory does not exist: $SOURCE"
    exit 1
fi

# Show what will change
echo "Changes to sync:"
echo "---"
if command -v rsync > /dev/null 2>&1; then
    # Dry run first to show changes
    rsync -avn --delete \
        --exclude='.git' \
        --exclude='agnostic-sync.sh' \
        --exclude='*/tests/results/*.md' \
        "$SOURCE/" "$DEST/" 2>&1 | grep -E '^(deleting|>|<)' | head -30 || echo "  (no changes detected)"
    echo "---"
    echo ""

    # Actual sync
    rsync -av --delete \
        --exclude='.git' \
        --exclude='agnostic-sync.sh' \
        --exclude='*/tests/results/*.md' \
        "$SOURCE/" "$DEST/"

    echo ""
    echo "Sync complete."
else
    # Fallback to cp if rsync not available
    echo "rsync not found, using cp -r"
    cp -r "$SOURCE/"* "$DEST/"
    echo "Copy complete."
fi

echo ""
echo "======================================================="
echo "Home directory .0agnostic/ is now in sync with repo."
echo "======================================================="
