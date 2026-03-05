#!/bin/bash
# resource_id: "b7bb5614-7dfa-473f-9e8a-96c05791cdab"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-101457-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 05_planning stage"

# Add custom initialization here
