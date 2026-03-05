#!/bin/bash
# resource_id: "4880626f-d72b-4bbf-a750-af4ef54130d8"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-101457-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 11_archives stage"

# Add custom initialization here
