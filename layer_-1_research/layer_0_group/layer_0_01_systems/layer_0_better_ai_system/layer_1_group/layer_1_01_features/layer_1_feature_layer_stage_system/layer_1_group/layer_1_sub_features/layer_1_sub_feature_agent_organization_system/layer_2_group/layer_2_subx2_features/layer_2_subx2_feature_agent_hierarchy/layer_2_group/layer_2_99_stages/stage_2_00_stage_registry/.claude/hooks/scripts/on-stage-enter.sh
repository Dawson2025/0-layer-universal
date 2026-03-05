#!/bin/bash
# resource_id: "876f3674-b4a2-41f7-9ff5-0f06cbacb7b2"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 00_stage_registry stage"

# Add custom initialization here
