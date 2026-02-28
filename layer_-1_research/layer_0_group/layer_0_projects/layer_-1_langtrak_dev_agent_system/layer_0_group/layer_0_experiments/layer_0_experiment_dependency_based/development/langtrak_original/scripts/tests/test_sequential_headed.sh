#!/bin/bash
# Run user story tests sequentially in headed mode for visual verification.
# Useful for debugging and watching the agent interact with the UI.

export FLASK_RELOADER=0
timestamp=$(date +%Y%m%d-%H%M%S)
artifact_dir="artifacts/story_runs/seq-headed-$timestamp"

echo "👀 Starting SEQUENTIAL HEADED run..."
echo "📂 Artifacts: $artifact_dir"

python3 scripts/automation/run_user_stories_with_server_check.py \
  --navigation-mode=both \
  --concurrency 1 \
  --port-base 41000 \
  --artifacts "$artifact_dir" \
  --headed \
  --mcp-start-timeout 120

echo "✅ Run complete. Check $artifact_dir/summary.json for results."
