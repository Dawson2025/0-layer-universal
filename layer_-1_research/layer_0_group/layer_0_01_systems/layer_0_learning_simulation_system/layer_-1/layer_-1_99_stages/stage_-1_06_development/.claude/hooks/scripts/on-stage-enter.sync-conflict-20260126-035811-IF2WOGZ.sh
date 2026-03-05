#!/bin/bash
# resource_id: "5a86a811-7951-4691-92da-5dedbcf71ce3"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-035811-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 06_development stage"

# Add custom initialization here
