#!/bin/bash
# resource_id: "779863ea-9b65-42c3-a39f-6efd3e4dfca6"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 10_current_product stage"

# Add custom initialization here
