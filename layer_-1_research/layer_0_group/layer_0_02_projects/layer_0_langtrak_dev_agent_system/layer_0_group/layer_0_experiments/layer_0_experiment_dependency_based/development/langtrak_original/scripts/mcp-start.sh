#!/usr/bin/env bash
# resource_id: "f5895d0c-86e1-47f1-bf31-31ebe406ed74"
# resource_type: "script"
# resource_name: "mcp-start"
# Helper script to start the Playwright MCP server for local development.
# Usage: bash scripts/mcp-start.sh [--headed] [--port PORT]

set -euo pipefail

PORT=9234
HOST=127.0.0.1
HEADED=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --headed)
      HEADED=true
      shift
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    *)
      echo "Unknown arg: $1"
      exit 1
      ;;
  esac
done

export PLAYWRIGHT_MCP_BROWSER=chromium
OUTPUT_DIR="${OUTPUT_DIR:-artifacts/mcp}"
mkdir -p "$OUTPUT_DIR"

if [ "$HEADED" = true ]; then
  # Headed is default in newer @playwright/mcp versions; do not pass --headless.
  exec npx -y @playwright/mcp@latest --port "$PORT" --host "$HOST" --browser=chromium --isolated --output-dir "$OUTPUT_DIR/mcp-$PORT"
else
  exec npx -y @playwright/mcp@latest --port "$PORT" --host "$HOST" --headless --browser=chromium --isolated --output-dir "$OUTPUT_DIR/mcp-$PORT"
fi
