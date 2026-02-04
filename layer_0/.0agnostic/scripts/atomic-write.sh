#!/bin/bash
#
# atomic-write.sh - Atomic file writes for data safety
#
# Usage:
#   ./atomic-write.sh <target_file>
#   (Reads content from stdin, writes atomically to target)
#
# Example:
#   echo "content" | ./atomic-write.sh output.md
#   cat data.txt | ./atomic-write.sh output.md
#
# How it works:
#   1. Writes content to temporary file
#   2. Uses atomic rename (mv) to replace target
#   3. No partial writes possible
#

set -e

TARGET_FILE="$1"

if [ -z "$TARGET_FILE" ]; then
    echo "Usage: $0 <target_file>"
    echo "Content is read from stdin"
    exit 1
fi

# Create temp file in same directory (ensures same filesystem for atomic mv)
TARGET_DIR=$(dirname "$TARGET_FILE")
TEMP_FILE=$(mktemp "${TARGET_DIR}/.atomic_XXXXXX")

# Ensure cleanup on exit
cleanup() {
    rm -f "$TEMP_FILE" 2>/dev/null || true
}
trap cleanup EXIT

# Write stdin to temp file
cat > "$TEMP_FILE"

# Atomic rename
mv "$TEMP_FILE" "$TARGET_FILE"

echo "Atomically wrote: $TARGET_FILE"

