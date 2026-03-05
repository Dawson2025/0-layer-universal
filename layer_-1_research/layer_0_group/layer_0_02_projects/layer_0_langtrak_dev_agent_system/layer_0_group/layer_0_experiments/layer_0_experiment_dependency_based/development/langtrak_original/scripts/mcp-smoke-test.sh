#!/usr/bin/env bash
# resource_id: "4d905e02-6608-459c-81ef-2025d6651db3"
# resource_type: "script"
# resource_name: "mcp-smoke-test"
set -euo pipefail

# Simple launcher + smoke test for Playwright MCP server
# Usage: bash scripts/mcp-smoke-test.sh [PORT] [HOST] [--headed]

PORT=${1:-9234}
HOST=${2:-127.0.0.1}
HEADED=false
if [ "${3:-}" = "--headed" ]; then
  HEADED=true
fi

LOGFILE="/tmp/mcp-smoke-test.log"
rm -f "$LOGFILE"

export PLAYWRIGHT_BROWSERS_PATH=0

START_CMD=("bash" "scripts/mcp-start.sh" "--port" "$PORT")
if [ "$HEADED" = true ]; then
  START_CMD+=("--headed")
fi

echo "Starting Playwright MCP server on $HOST:$PORT... (logs -> $LOGFILE)"
"${START_CMD[@]}" > "$LOGFILE" 2>&1 &
MCP_PID=$!
echo "Started (pid=$MCP_PID). Waiting for port $PORT to listen..."

SECS=0
until ss -ltnp 2>/dev/null | grep -q ":$PORT\b"; do
  sleep 1
  SECS=$((SECS+1))
  if [ $SECS -ge 20 ]; then
    echo "Timed out waiting for server to listen on port $PORT"
    echo "--- server log ---"
    tail -n 200 "$LOGFILE" || true
    kill $MCP_PID 2>/dev/null || true
    exit 2
  fi
done

echo "Port $PORT is listening. Performing smoke test against /mcp..."

# Perform a GET to /mcp. The MCP server expects protocol traffic; a GET usually yields 'Invalid request'.
RESP=$(curl -sS --max-time 5 "http://$HOST:$PORT/mcp" || true)
echo "Response (first 200 chars): ${RESP:0:200}"

if echo "$RESP" | grep -qi "invalid request"; then
  echo "✅ Smoke test passed: server responded with expected 'Invalid request' message."
  RESULT=0
else
  echo "❌ Smoke test failed: unexpected response from /mcp"
  echo "--- server log tail ---"
  tail -n 200 "$LOGFILE" || true
  RESULT=3
fi

echo "Stopping server (pid=$MCP_PID)"
kill $MCP_PID 2>/dev/null || true
wait $MCP_PID 2>/dev/null || true

exit $RESULT
