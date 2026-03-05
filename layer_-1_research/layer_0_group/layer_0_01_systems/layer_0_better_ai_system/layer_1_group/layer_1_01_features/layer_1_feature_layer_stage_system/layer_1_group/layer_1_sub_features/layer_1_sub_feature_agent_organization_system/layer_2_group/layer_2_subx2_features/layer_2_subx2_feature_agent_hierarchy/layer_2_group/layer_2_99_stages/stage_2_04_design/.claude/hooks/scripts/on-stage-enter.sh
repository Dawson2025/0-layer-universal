#!/bin/bash
# resource_id: "90391cf1-e9f9-4b0f-83b3-8d44769578ab"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 04_design stage"

# Add custom initialization here
