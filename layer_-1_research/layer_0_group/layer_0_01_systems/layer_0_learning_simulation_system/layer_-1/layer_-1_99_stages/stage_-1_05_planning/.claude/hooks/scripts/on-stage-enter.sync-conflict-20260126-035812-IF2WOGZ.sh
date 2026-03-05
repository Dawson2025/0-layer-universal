#!/bin/bash
# resource_id: "6a12a620-5a79-4e97-8ddc-5aad24fa9b47"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-035812-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 05_planning stage"

# Add custom initialization here
