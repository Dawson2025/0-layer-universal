#!/bin/bash
# resource_id: "0e121caa-e8e8-4eaf-9304-1c6ec81ac75f"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-101457-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 00_stage_registry stage"

# Add custom initialization here
