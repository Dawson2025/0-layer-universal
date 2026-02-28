#!/bin/bash
# Run user story tests in parallel HEADLESS mode for maximum speed.
# Ideal for rapid validation and CI/CD.

export FLASK_RELOADER=0
timestamp=$(date +%Y%m%d-%H%M%S)
artifact_dir="artifacts/story_runs/parallel-fast-$timestamp"

echo "🚀 Starting PARALLEL HEADLESS run..."
echo "📂 Artifacts: $artifact_dir"

python3 scripts/automation/run_user_stories_with_server_check.py \
  --navigation-mode=both \
  --concurrency 5 \
  --port-base 42000 \
  --artifacts "$artifact_dir" \
  --mcp-start-timeout 60 \
  --stagger 2.0

echo "✅ Run complete. Check $artifact_dir/summary.json for results."
