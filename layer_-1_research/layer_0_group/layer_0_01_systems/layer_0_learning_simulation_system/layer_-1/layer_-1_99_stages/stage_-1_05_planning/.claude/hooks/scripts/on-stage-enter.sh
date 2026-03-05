#!/bin/bash
# resource_id: "24b07b2a-7b4d-4c00-9200-31771a2e8f52"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 05_planning stage"

# Add custom initialization here
