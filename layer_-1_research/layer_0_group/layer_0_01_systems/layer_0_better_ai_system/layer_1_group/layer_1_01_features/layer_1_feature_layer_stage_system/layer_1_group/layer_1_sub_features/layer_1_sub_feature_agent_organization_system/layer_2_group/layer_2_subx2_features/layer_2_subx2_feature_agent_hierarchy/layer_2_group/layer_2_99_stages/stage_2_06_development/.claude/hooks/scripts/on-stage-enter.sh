#!/bin/bash
# resource_id: "16abc762-b622-4b47-8a26-dbd1c54e8bbd"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 06_development stage"

# Add custom initialization here
