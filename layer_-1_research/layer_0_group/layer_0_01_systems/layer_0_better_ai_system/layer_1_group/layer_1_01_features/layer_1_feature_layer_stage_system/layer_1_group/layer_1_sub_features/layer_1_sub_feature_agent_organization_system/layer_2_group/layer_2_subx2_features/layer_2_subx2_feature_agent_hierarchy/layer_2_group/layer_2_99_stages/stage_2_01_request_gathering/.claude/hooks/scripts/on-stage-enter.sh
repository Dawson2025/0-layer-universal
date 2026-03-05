#!/bin/bash
# resource_id: "b668bce9-27ba-479c-a2c9-d627fd7778a5"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 01_request_gathering stage"

# Add custom initialization here
