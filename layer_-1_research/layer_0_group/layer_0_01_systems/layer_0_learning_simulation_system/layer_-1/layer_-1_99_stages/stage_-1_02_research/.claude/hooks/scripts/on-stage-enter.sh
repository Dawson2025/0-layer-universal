#!/bin/bash
# resource_id: "7b48eac0-de25-4332-9850-0eb3d810ffd4"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 02_research stage"

# Add custom initialization here
