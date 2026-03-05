#!/bin/bash
# resource_id: "0c7c76dc-acbc-4be2-9d92-905387c498a9"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-101455-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 01_request_gathering stage"

# Add custom initialization here
