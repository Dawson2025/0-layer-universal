#!/bin/bash
# resource_id: "11b6ef3a-1a0d-47c6-9329-8d2159226515"
# resource_type: "script"
# resource_name: "on-stage-enter"
# Hook script: Called when entering this stage
# Customize as needed

STAGE_DIR="$(dirname "$(dirname "$0")")"
echo "Entering 10_current_product stage"

# Add custom initialization here
