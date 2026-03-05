#!/bin/bash
# resource_id: "823d4505-29b7-4d56-bd81-73a85b10c4fe"
# resource_type: "script"
# resource_name: "on-stage-enter.sync-conflict-20260126-101453-IF2WOGZ"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 10_current_product stage"

# Add custom initialization here
