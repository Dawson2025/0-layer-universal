#!/bin/bash
# resource_id: "06b6f137-2963-4c36-a69c-b4229c3633b1"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-101457-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 06_development stage"

# Add custom initialization here
