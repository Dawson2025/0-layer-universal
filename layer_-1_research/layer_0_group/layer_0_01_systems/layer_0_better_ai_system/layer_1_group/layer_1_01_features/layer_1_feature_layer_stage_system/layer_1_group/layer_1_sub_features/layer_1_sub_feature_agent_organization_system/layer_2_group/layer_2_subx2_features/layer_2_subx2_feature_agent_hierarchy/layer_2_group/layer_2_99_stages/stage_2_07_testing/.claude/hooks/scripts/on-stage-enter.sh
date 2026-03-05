#!/bin/bash
# resource_id: "5d54799a-60dc-44a3-ab45-fb495e57ccfc"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 07_testing stage"

# Add custom initialization here
