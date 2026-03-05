#!/bin/bash
# resource_id: "2abf8606-d85b-4423-bb05-1c7f5021ad24"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 01_request_gathering stage"

# Add custom initialization here
