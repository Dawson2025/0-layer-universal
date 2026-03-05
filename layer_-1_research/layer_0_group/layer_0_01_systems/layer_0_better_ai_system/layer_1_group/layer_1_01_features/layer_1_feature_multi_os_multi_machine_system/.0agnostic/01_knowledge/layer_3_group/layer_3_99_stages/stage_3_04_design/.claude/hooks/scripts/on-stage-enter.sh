#!/bin/bash
# resource_id: "71235abb-189a-45f5-9f2e-bedc16780fd6"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 04_design stage"

# Add custom initialization here
