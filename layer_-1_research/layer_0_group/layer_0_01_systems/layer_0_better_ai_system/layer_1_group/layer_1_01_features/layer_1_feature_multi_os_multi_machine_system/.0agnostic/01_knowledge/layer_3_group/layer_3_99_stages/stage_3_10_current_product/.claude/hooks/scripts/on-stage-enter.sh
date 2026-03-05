#!/bin/bash
# resource_id: "ebf8a0a9-16d5-4741-b405-9d75791dc24b"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 10_current_product stage"

# Add custom initialization here
